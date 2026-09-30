"""系统目录与数据目录的文件读写和不变量。

系统目录（系统仓库）提供协作说明和格式规范，只读；数据目录（数据仓库）存放
profile/、state/ 和 sources/，服务端在这里写入。这里只处理存取和可以确定的规则：
路径、命名、log 不可覆盖、整合标记校验、新材料检测、数据格式版本。
内容本身的格式由 harness/standards/ 规定，服务端不解析。
"""

from __future__ import annotations

import json
import os
import re
from dataclasses import dataclass, field
from datetime import datetime
from io import BytesIO
from pathlib import Path

from pypdf import PdfReader, PdfWriter

RESOURCE_RE = re.compile(r"^[a-z0-9][a-z0-9-]*$")
STANDARD_NAMES = ("log-format", "progress-format", "concepts-format", "materials")

# 数据仓库的格式版本。改动原始数据的格式时加一，并附带迁移，见 DESIGN.md"演进与迁移"。
SUPPORTED_FORMAT_VERSION = 1
TEXT_SUFFIXES = {
    ".md", ".markdown", ".txt", ".srt", ".vtt", ".csv", ".json", ".yaml", ".yml",
    ".py", ".c", ".h", ".cc", ".cpp", ".hpp", ".cu", ".cuh", ".rs", ".go", ".js",
    ".ts", ".sh", ".toml", ".ini", ".cfg", ".tex", ".rst", ".html", ".css", ".sql",
}
SKIP_NAMES = {".stfolder", ".stversions", ".stignore", ".DS_Store", "Thumbs.db", ".gitkeep"}


class StoreError(Exception):
    """可以直接展示给模型的错误。"""


@dataclass
class SourceEntry:
    rel: str            # sources/<资源名>/ 下的相对路径；代码仓库以 / 结尾
    size: int
    mtime: float
    is_repo: bool = False
    file_count: int = 0


@dataclass
class MaterialChanges:
    new: list[str] = field(default_factory=list)        # 未登记：自身路径和上层文件夹都不在 progress 中
    updated: list[str] = field(default_factory=list)    # 自身已登记，修改时间晚于 progress
    in_folder: list[str] = field(default_factory=list)  # 所在文件夹已登记，修改时间晚于 progress（多为新放入的文件）
    missing: list[str] = field(default_factory=list)    # progress 中登记了、但已不存在的路径

    def describe(self) -> str:
        lines = []
        if self.new:
            lines.append("未登记的新材料：" + "、".join(self.new))
        if self.updated:
            lines.append("已更新的材料（修改时间晚于 progress）：" + "、".join(self.updated))
        if self.in_folder:
            lines.append("已登记文件夹中新增或修改的文件：" + "、".join(self.in_folder))
        if self.missing:
            lines.append("progress 中登记了、但已不存在的路径（可能被移动或改名）：" + "、".join(self.missing))
        return "\n".join(lines) or "没有新材料。"

    def status_of(self, rel: str) -> str:
        if rel in self.new:
            return "未登记"
        if rel in self.updated:
            return "已更新"
        if rel in self.in_folder:
            return "文件夹已登记，有新增或修改"
        return "已登记"


# 路径两侧不能紧挨着这些字符，否则视为另一条更长路径的一部分
_PATH_CHARS = r"A-Za-z0-9_.\-/"
MATERIAL_SUFFIXES = TEXT_SUFFIXES | {".pdf", ".ipynb"}
# progress 中看起来像登记路径的片段：带后缀的文件，或以 / 结尾的文件夹
_REGISTERED_PATH_RE = re.compile(
    rf"(?<![{_PATH_CHARS}])((?:[^\s|/、，,;；()（）\[\]`\"']+/)*[^\s|/、，,;；()（）\[\]`\"']+\.[A-Za-z][A-Za-z0-9]{{0,7}}"
    rf"|(?:[^\s|/、，,;；()（）\[\]`\"']+/)+)(?![{_PATH_CHARS}])"
)


def _path_registered(text: str, rel: str) -> bool:
    """rel（文件）是否作为完整路径出现在 text 中。"""
    return re.search(rf"(?<![{_PATH_CHARS}]){re.escape(rel)}(?![{_PATH_CHARS}])", text) is not None


def _folder_registered(text: str, folder: str) -> bool:
    """folder 是否作为文件夹登记在 text 中（写作 week03/ 或 week03）。

    右侧用包含中文的字符类判断，这样登记了"第六周/讲义.pdf"不会被当成登记了整个"第六周/"。
    """
    pattern = rf"(?<![{_PATH_CHARS}]){re.escape(folder)}/?(?![\w.\-/])"
    return re.search(pattern, text) is not None


def split_frontmatter(text: str) -> tuple[dict[str, str], str]:
    """拆出简单的 frontmatter（key: value 形式），返回 (字段, 正文)。"""
    if not text.startswith("---"):
        return {}, text
    lines = text.splitlines(keepends=True)
    if not lines or lines[0].strip() != "---":
        return {}, text
    fields: dict[str, str] = {}
    for i in range(1, len(lines)):
        line = lines[i]
        if line.strip() == "---":
            return fields, "".join(lines[i + 1:]).lstrip("\n")
        if ":" in line:
            key, _, value = line.partition(":")
            fields[key.strip()] = value.strip().strip('"')
    return {}, text


def human_size(size: int) -> str:
    if size < 1024:
        return f"{size} B"
    if size < 1024 * 1024:
        return f"{size / 1024:.0f} KB"
    return f"{size / 1024 / 1024:.1f} MB"


def parse_pages(spec: str, total: int) -> list[int]:
    """把 "5-12,20" 解析成从 0 开始的页序列表。页码从 1 开始。"""
    pages: list[int] = []
    for part in spec.replace("，", ",").split(","):
        part = part.strip()
        if not part:
            continue
        if "-" in part:
            a, _, b = part.partition("-")
            start, end = int(a), int(b)
        else:
            start = end = int(part)
        if start < 1 or end > total or start > end:
            raise StoreError(f"页码范围 {part} 无效，这份 PDF 共 {total} 页。")
        pages.extend(range(start - 1, end))
    if not pages:
        raise StoreError("pages 参数为空。")
    return pages


class LearningStore:
    def __init__(self, system_dir: Path, data_dir: Path) -> None:
        # 系统目录
        self.system = system_dir
        self.guide_path = system_dir / "harness" / "guide.md"
        self.standards = system_dir / "harness" / "standards"
        # 数据目录
        self.root = data_dir
        self.profile_dir = data_dir / "profile"
        self.state = data_dir / "state"
        self.log_dir = self.state / "log"
        self.progress_dir = self.state / "progress"
        self.concepts_path = self.state / "concepts.md"
        self.sources = data_dir / "sources"
        self.format_path = data_dir / "FORMAT_VERSION"

    # ---------- 基础 ----------

    @staticmethod
    def check_resource(name: str) -> str:
        name = (name or "").strip()
        if not RESOURCE_RE.match(name):
            raise StoreError(
                f"资源名 {name!r} 不符合规则：只能用小写字母、数字和连字符，例如 embedded-101、cs336。"
            )
        return name

    @staticmethod
    def _read(path: Path) -> str:
        return path.read_text(encoding="utf-8") if path.exists() else ""

    def check_format(self) -> None:
        """数据格式版本必须与本服务支持的版本一致，否则拒绝启动。"""
        if not self.format_path.exists():
            raise SystemExit(
                f"数据目录 {self.root} 中没有 FORMAT_VERSION。"
                "请确认 LEARNING_DATA_DIR 指向按 templates/data/ 建立的数据仓库。"
            )
        raw = self.format_path.read_text(encoding="utf-8").strip()
        try:
            version = int(raw)
        except ValueError:
            raise SystemExit(f"FORMAT_VERSION 的内容 {raw!r} 不是整数。")
        if version != SUPPORTED_FORMAT_VERSION:
            raise SystemExit(
                f"数据格式版本为 {version}，本服务支持的是 {SUPPORTED_FORMAT_VERSION}。"
                "需要先迁移数据或切换到对应版本的系统，见 DESIGN.md 的“演进与迁移”。"
            )

    def read_guide(self) -> str:
        return self._read(self.guide_path)

    def read_profile(self) -> list[tuple[str, str]]:
        """按文件名顺序返回 profile/ 下所有 md 文件的 (文件名, 内容)。"""
        if not self.profile_dir.exists():
            return []
        return [
            (p.name, self._read(p))
            for p in sorted(self.profile_dir.glob("*.md"))
            if not p.name.startswith(".")
        ]

    def read_standard(self, name: str) -> str:
        key = name.strip().removesuffix(".md")
        if key not in STANDARD_NAMES:
            raise StoreError("可读取的规范有：" + "、".join(STANDARD_NAMES))
        return self._read(self.standards / f"{key}.md")

    def list_resources(self) -> list[str]:
        names = {p.stem for p in self.progress_dir.glob("*.md")}
        if self.sources.exists():
            names |= {
                p.name for p in self.sources.iterdir()
                if p.is_dir() and not p.name.startswith(".") and RESOURCE_RE.match(p.name)
            }
        return sorted(names)

    # ---------- log ----------

    def list_logs(self) -> list[str]:
        if not self.log_dir.exists():
            return []
        return sorted(p.name for p in self.log_dir.glob("*.md"))

    def read_concepts(self) -> tuple[str | None, str]:
        """返回 (integrated_through, 完整文本)。"""
        text = self._read(self.concepts_path)
        fields, _ = split_frontmatter(text)
        marker = fields.get("integrated_through") or None
        return marker, text

    def unintegrated_logs(self) -> list[str]:
        marker, _ = self.read_concepts()
        logs = self.list_logs()
        if not marker:
            return logs
        return [name for name in logs if name > marker]

    def read_log(self, name: str) -> str:
        name = name.strip()
        if not name.endswith(".md"):
            name += ".md"
        if "/" in name or "\\" in name or name not in self.list_logs():
            raise StoreError(f"没有名为 {name} 的 log。")
        return self._read(self.log_dir / name)

    def search_logs(self, query: str, max_hits: int = 200) -> list[tuple[str, int, str]]:
        needle = query.strip().lower()
        if not needle:
            raise StoreError("搜索内容不能为空。")
        hits: list[tuple[str, int, str]] = []
        for name in self.list_logs():
            for lineno, line in enumerate(self._read(self.log_dir / name).splitlines(), 1):
                if needle in line.lower():
                    hits.append((name, lineno, line.strip()))
                    if len(hits) >= max_hits:
                        return hits
        return hits

    def write_log(self, resource: str, part: str, body: str, now: datetime | None = None) -> Path:
        resource = self.check_resource(resource)
        _, body = split_frontmatter(body.strip())
        body = body.strip()
        if not body:
            raise StoreError("log 正文不能为空。")
        now = now or datetime.now().astimezone()
        stem = f"{now:%Y-%m-%d %H%M} {resource}"
        self.log_dir.mkdir(parents=True, exist_ok=True)
        text = (
            "---\n"
            f"date: {now:%Y-%m-%d}\n"
            f"source: {resource}\n"
            f"part: {json.dumps(part.strip(), ensure_ascii=False)}\n"
            "---\n\n"
            f"{body}\n"
        )
        for n in range(1, 100):
            name = f"{stem}.md" if n == 1 else f"{stem} {n}.md"
            path = self.log_dir / name
            try:
                with open(path, "x", encoding="utf-8") as f:   # 排他创建：已存在就换名字
                    f.write(text)
                return path
            except FileExistsError:
                continue
        raise StoreError("同一分钟内的 log 过多，无法生成文件名。")

    # ---------- progress ----------

    def progress_path(self, resource: str) -> Path:
        return self.progress_dir / f"{self.check_resource(resource)}.md"

    def read_progress(self, resource: str) -> str | None:
        path = self.progress_path(resource)
        return self._read(path) if path.exists() else None

    def write_progress(self, resource: str, content: str) -> Path:
        content = content.strip()
        if not content:
            raise StoreError("progress 内容不能为空。")
        path = self.progress_path(resource)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content + "\n", encoding="utf-8")
        return path

    # ---------- concepts ----------

    def write_concepts(self, content: str, integrated_through: str) -> Path:
        marker = integrated_through.strip()
        if marker and not marker.endswith(".md"):
            marker += ".md"
        logs = self.list_logs()
        if marker not in logs:
            raise StoreError(f"integrated_through 指向的 log {marker!r} 不存在。")
        current, _ = self.read_concepts()
        if current and marker < current:
            raise StoreError(f"integrated_through 不能早于当前的标记 {current}。")
        _, body = split_frontmatter(content.strip())
        text = f"---\nintegrated_through: {marker}\n---\n\n{body.strip()}\n"
        self.concepts_path.write_text(text, encoding="utf-8")
        return self.concepts_path

    # ---------- sources ----------

    def source_dir(self, resource: str) -> Path:
        return self.sources / self.check_resource(resource)

    def iter_sources(self, resource: str) -> list[SourceEntry]:
        """列出材料。含 .git 的子文件夹视为一个代码仓库整体。"""
        base = self.source_dir(resource)
        if not base.exists():
            return []
        entries: list[SourceEntry] = []
        for dirpath, dirnames, filenames in os.walk(base):
            current = Path(dirpath)
            if current != base and (current / ".git").exists():
                count = sum(len(f) for _, _, f in os.walk(current))
                entries.append(SourceEntry(
                    rel=str(current.relative_to(base)).replace(os.sep, "/") + "/",
                    size=0, mtime=current.stat().st_mtime, is_repo=True, file_count=count,
                ))
                dirnames[:] = []
                continue
            dirnames[:] = sorted(d for d in dirnames if not d.startswith(".") and d not in SKIP_NAMES)
            for fname in sorted(filenames):
                if fname.startswith(".") or fname in SKIP_NAMES or fname.startswith("~syncthing~"):
                    continue
                path = current / fname
                st = path.stat()
                entries.append(SourceEntry(
                    rel=str(path.relative_to(base)).replace(os.sep, "/"),
                    size=st.st_size, mtime=st.st_mtime,
                ))
        return entries

    def material_changes(self, resource: str) -> MaterialChanges:
        """对比 sources/<资源名>/ 和 progress 中登记的路径，见 SPEC.md"新材料检测"。"""
        path = self.progress_path(resource)
        text = self._read(path)
        progress_mtime = path.stat().st_mtime if path.exists() else 0.0
        changes = MaterialChanges()
        for entry in self.iter_sources(resource):
            rel = entry.rel.rstrip("/")
            if entry.is_repo:
                own = _folder_registered(text, rel)
            else:
                own = _path_registered(text, rel)
            if own:
                if not entry.is_repo and entry.mtime > progress_mtime:
                    changes.updated.append(entry.rel)
                continue
            parents = rel.split("/")[:-1]
            covered = any(
                _folder_registered(text, "/".join(parents[: i + 1])) for i in range(len(parents))
            )
            if not covered:
                changes.new.append(entry.rel)
            elif not entry.is_repo and entry.mtime > progress_mtime:
                changes.in_folder.append(entry.rel)
        base = self.source_dir(resource)
        for token in sorted(set(_REGISTERED_PATH_RE.findall(text))):
            if token.endswith("/"):
                exists = (base / token.rstrip("/")).is_dir()
            else:
                if Path(token).suffix.lower() not in MATERIAL_SUFFIXES:
                    continue
                exists = (base / token).exists()
            if not exists:
                changes.missing.append(token)
        return changes

    def resolve_source_dir(self, resource: str, rel: str) -> Path:
        base = self.source_dir(resource).resolve()
        path = (base / rel).resolve()
        if base != path and base not in path.parents:
            raise StoreError("路径超出了该资源的材料文件夹。")
        return path

    def resolve_source(self, resource: str, rel: str) -> Path:
        base = self.source_dir(resource).resolve()
        path = (base / rel).resolve()
        if base != path and base not in path.parents:
            raise StoreError("路径超出了该资源的材料文件夹。")
        if not path.is_file():
            raise StoreError(f"找不到材料 {rel}。可以先用 list_sources 查看这个资源有哪些材料。")
        return path

    @staticmethod
    def pdf_info(path: Path, max_outline: int = 80) -> tuple[int | None, list[str], str | None]:
        """返回 (页数, 书签目录行, 错误说明)。"""
        try:
            reader = PdfReader(str(path))
            if reader.is_encrypted:
                return None, [], "PDF 已加密，无法读取页数和书签"
            total = len(reader.pages)
            lines: list[str] = []

            def walk(items, depth: int) -> None:
                for item in items:
                    if len(lines) >= max_outline:
                        return
                    if isinstance(item, list):
                        walk(item, depth + 1)
                        continue
                    try:
                        page = reader.get_destination_page_number(item) + 1
                        lines.append(f"{'  ' * depth}{item.title} → 第 {page} 页")
                    except Exception:
                        lines.append(f"{'  ' * depth}{getattr(item, 'title', '?')}")

            walk(reader.outline, 0)
            return total, lines, None
        except Exception as exc:  # 损坏或不规范的 PDF
            return None, [], f"无法解析 PDF：{exc.__class__.__name__}"

    @staticmethod
    def pdf_bytes(path: Path, pages: str | None) -> tuple[bytes, str]:
        """返回 (PDF 数据, 描述)。pages 为空时返回原件。"""
        if not pages:
            reader = PdfReader(str(path))
            return path.read_bytes(), f"共 {len(reader.pages)} 页"
        reader = PdfReader(str(path))
        indices = parse_pages(pages, len(reader.pages))
        writer = PdfWriter()
        for i in indices:
            writer.add_page(reader.pages[i])
        buf = BytesIO()
        writer.write(buf)
        return buf.getvalue(), f"截取第 {pages} 页，原文件共 {len(reader.pages)} 页"
