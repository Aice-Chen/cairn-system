# Cairn

Cairn 是一个远程的 AI 辅助学习系统。AI 读取学习材料和学习者的状态，从自然交流中觉察理解程度，有针对性地讲解，并在每次学习后记录观察。学习状态保存在自己的服务器上，claude.ai、ChatGPT、手机，以及本地的 Claude Code 和 Codex 都通过同一个 MCP 服务读写。

系统分为两个独立的 Git 仓库：`cairn-system` 是本仓库，可以公开；`cairn-data` 是由 templates/data/ 建立的私有个人数据仓库。

本地将两个仓库放在同一个 Cairn 目录下：

```text
Cairn/
├── system/    cairn-system：程序、协作说明、规范和模板
└── data/      cairn-data：个人资料、学习状态、材料和本地笔记
```

开发系统时打开 `system/`，学习时打开 `data/`。父目录 Cairn 只用于组织文件，不是第三个 Git 仓库。服务器继续使用 `/home/learning/system` 和 `/home/learning/data`；MCP 连接名 `learning`、服务及命令名 `learning-mcp`、环境变量 `LEARNING_*` 均沿用现有标识。

| 位置 | 内容 |
|---|---|
| DESIGN.md | 设计原则、架构、演进与迁移、决策记录 |
| harness/guide.md | 学习协作说明，由 start_session 返回给模型 |
| harness/standards/ | 数据文件的格式规范 |
| templates/data/ | 数据仓库模板 |
| templates/project-instructions.md | 网页端 Project 指令 |
| docs/DEPLOY.md | 部署与客户端接入 |
| docs/CODEX_DEPLOY.md | 交给 Codex 执行的部署任务 |
| server/ | MCP 服务端，SPEC.md 为工具规格 |

## 日常使用

| 你说 | 模型做什么 |
|---|---|
| 今天学 embedded-101 Lab2 | 调用 start_session 读取状态；有材料变化时先更新登记，再开始学习 |
| 收尾 | 写一条学习记录，更新进度 |
| 整合 | 综合近期记录更新概念掌握情况，列出变更等你确认后写入 |
| 加入资源，附链接或文件 | 下载公开文件，建立该资源的进度 |
| 检查 cs336 的更新 | 重新读取资源主页，下载并登记新增的材料 |
| 看看我的作业（本地客户端） | 读代码和提交历史，分析其中反映出的理解程度 |
| 直接讲 / 考我 | 切换为直接讲解 / 集中检验 |

## 放入材料前

数据仓库的 sources/ 里只放模型可以直接读取的文件，转换在放入前完成：

| 材料 | 处理方式 |
|---|---|
| 文字为主的 PDF | 用 markitdown 转成 md：`markitdown 文件.pdf -o 文件.md`，扫一眼公式和表格，有损坏就保留 PDF |
| 图表、公式为主的 PDF | 保留 PDF 原件 |
| 整本书 | 按章拆开，每章一个文件 |
| pptx、docx | 导出为 PDF，再按上面两条判断 |
| 网页、视频 | 转成 md 或文稿 |

sources/ 下的第一层文件夹是资源，用英文小写名，如 `embedded-101`、`cs336`；资源内部可以按周、按讲自由建子文件夹。
