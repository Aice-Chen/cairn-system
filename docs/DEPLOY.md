# 部署与接入

按顺序完成下面各步。想让 Codex 代为执行时，把 CODEX_DEPLOY.md 交给它，本文件作为它的命令参考。

文中的占位符：`learn.example.com` 为你的域名，`<你>` 为你的 GitHub 用户名，`<VPS IP>` 为服务器 IP。两个仓库：系统仓库 `<你>/learning-system`（公开），数据仓库 `<你>/learning-data`（私有）。

## 0. 准备

- 一台 VPS，系统 Ubuntu 24.04。1 核、1 GB 内存加 1 GB swap 可以运行；2 GB 内存更宽裕。
- 一个域名，GitHub 账号。

## 1. 建立数据仓库（笔记本上）

```bash
git clone https://github.com/<你>/learning-system.git
cp -r learning-system/templates/data learning-data
cd learning-data
```

填写 profile/10-learner.md 和 profile/20-preferences.md，然后在 GitHub 上新建私有仓库 `learning-data`（不要初始化 README），推送：

```bash
git init -b main
git add .
git commit -m "建立学习数据仓库"
git remote add origin git@github.com:<你>/learning-data.git
git push -u origin main
```

以后在本地学习时，Claude Code 和 Codex 就在这个目录中运行。

## 2. 服务器基础环境

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y git curl syncthing debian-keyring debian-archive-keyring apt-transport-https
sudo adduser --disabled-password --gecos "" learning

sudo ufw allow OpenSSH
sudo ufw allow 80,443/tcp
sudo ufw allow 22000/tcp
sudo ufw enable
```

VPS 服务商的安全组里也要放行 22、80、443 和 22000（TCP）。

## 3. 域名解析

添加一条 A 记录：`learn` → `<VPS IP>`，用 `getent ahostsv4 learn.example.com` 确认解析生效。

## 4. 克隆两个仓库

以下命令用 learning 用户执行（`sudo -iu learning`）。

系统仓库是公开的，用 HTTPS 克隆即可：

```bash
git clone https://github.com/<你>/learning-system.git ~/system
```

数据仓库需要读写权限。生成一把只用于它的部署密钥：

```bash
ssh-keygen -t ed25519 -f ~/.ssh/learning_data_deploy -N ""
cat ~/.ssh/learning_data_deploy.pub
```

把公钥添加到 learning-data 仓库的 Settings → Deploy keys，勾选 Allow write access。然后：

```bash
cat >> ~/.ssh/config << 'CFG'
Host github.com
  IdentityFile ~/.ssh/learning_data_deploy
  IdentitiesOnly yes
CFG
ssh-keyscan github.com >> ~/.ssh/known_hosts
git clone git@github.com:<你>/learning-data.git ~/data
```

## 5. 安装依赖并运行测试

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
source ~/.local/bin/env
cd ~/system/server
uv sync --locked --extra test
uv run --locked --extra test python -m pytest -q
```

`server/uv.lock` 记录经过测试的依赖版本，`--locked` 在依赖配置与锁文件不一致时停止，避免部署时改写锁文件。测试使用临时的数据目录，不会读到 ~/data；GitHub OAuth 和实际客户端按后面的步骤验证。

## 6. 创建 GitHub OAuth App

GitHub → Settings → Developer settings → OAuth Apps → New OAuth App：

- Application name：learning-mcp
- Homepage URL：`https://learn.example.com`
- Authorization callback URL（新界面中叫 Redirect URI）：`https://learn.example.com/auth/callback`

创建后记下 Client ID，再生成 client secret。

## 7. 环境变量文件

以 learning 用户建立 `~/learning.env`，权限设为 600：

```bash
LEARNING_SYSTEM_DIR=/home/learning/system
LEARNING_DATA_DIR=/home/learning/data
LEARNING_TRANSPORT=http
LEARNING_HOST=127.0.0.1
LEARNING_PORT=8000
LEARNING_BASE_URL=https://learn.example.com
LEARNING_GITHUB_CLIENT_ID=<Client ID>
LEARNING_GITHUB_CLIENT_SECRET=<Client secret>
LEARNING_JWT_SIGNING_KEY=<用 openssl rand -hex 32 生成>
LEARNING_ALLOWED_GITHUB_USER=<你>
LEARNING_GIT_NAME=learning-mcp
LEARNING_GIT_EMAIL=learning-mcp@users.noreply.github.com
TZ=Asia/Shanghai
```

TZ 决定 log 的日期和时间。签名密钥以后不要更换，否则所有客户端都要重新授权。

## 8. 用 systemd 运行服务

```bash
sudo tee /etc/systemd/system/learning-mcp.service << 'UNIT'
[Unit]
Description=Learning MCP server
After=network-online.target
Wants=network-online.target

[Service]
User=learning
Group=learning
WorkingDirectory=/home/learning/system/server
EnvironmentFile=/home/learning/learning.env
ExecStart=/home/learning/system/server/.venv/bin/learning-mcp
Restart=on-failure
RestartSec=5
UMask=0027
NoNewPrivileges=true
PrivateTmp=true
ProtectSystem=full

[Install]
WantedBy=multi-user.target
UNIT
sudo systemctl daemon-reload
sudo systemctl enable --now learning-mcp
sudo systemctl status learning-mcp
```

服务直接使用第 5 步安装好的虚拟环境，启动时不安装或更新依赖。

## 9. Caddy 提供 HTTPS

```bash
curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/gpg.key' | sudo gpg --dearmor -o /usr/share/keyrings/caddy-stable-archive-keyring.gpg
curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/debian.deb.txt' | sudo tee /etc/apt/sources.list.d/caddy-stable.list
sudo apt update && sudo apt install -y caddy
```

`/etc/caddy/Caddyfile`：

```
learn.example.com {
    reverse_proxy 127.0.0.1:8000
}
```

```bash
sudo systemctl reload caddy
curl -s -o /dev/null -w "%{http_code}\n" -X POST https://learn.example.com/mcp
curl -s https://learn.example.com/.well-known/oauth-authorization-server
```

第一条应当输出 401，第二条应当返回包含 authorization_endpoint 的 JSON。站点根路径没有首页，返回 404 属于正常。

443 端口由 Caddy 使用。以后在同一台服务器上部署其他服务时，需要分配其他端口，或者用 SNI 分流共用 443。

## 10. Syncthing 同步材料

服务器上：`sudo systemctl enable --now syncthing@learning`。它的管理界面只监听本机，在笔记本上用 SSH 隧道访问：

```bash
ssh -N -L 18384:127.0.0.1:8384 <你的 SSH 用户>@<VPS IP>
```

浏览器打开 `http://127.0.0.1:18384`。笔记本上安装 Syncthing 后配对：

1. 两端互相添加设备。笔记本添加服务器时，地址填 `tcp://<VPS IP>:22000`。
2. 共享同一个文件夹，ID 为 `learning-sources`：笔记本路径为本地数据仓库的 `sources`，服务器路径为 `/home/learning/data/sources`。
3. 两端都为这个文件夹开启"简易版本控制"。

只用固定地址直连时，可以关闭全局发现、本地发现、中继和 NAT 穿透。直连不稳定时，可以让 Syncthing 的连接走代理（支持通过 all_proxy 环境变量使用 SOCKS5）。

## 11. 接入客户端

| 客户端 | 做法 |
|---|---|
| claude.ai 网页端、桌面端、手机 App | 设置 → 连接器 → 添加自定义连接器，URL `https://learn.example.com/mcp`，用 GitHub 授权 |
| ChatGPT | 在设置中开启开发者模式，创建连接器，URL 同上，认证方式选 OAuth。菜单名称以当前界面为准 |
| Claude Code | 在本地数据仓库目录运行 `claude mcp add --transport http learning https://learn.example.com/mcp --scope user`，再运行 `/mcp` 完成授权 |
| Codex | `codex mcp add learning --url https://learn.example.com/mcp`，再 `codex mcp login learning` |

网页端在 claude.ai 和 ChatGPT 中各建一个学习用的 Project，填入 templates/project-instructions.md 里的指令，并启用 learning 连接器。

## 12. 实测清单

在每个客户端上依次检查，不通过的客户端记进数据仓库的 DEPLOYMENT.md，以后不在上面学习：

1. 连接：能完成 GitHub 授权。
2. 工具可见：说"开始学 <某个资源>"，模型应当调用 start_session，返回中能看到 profile。
3. 协作说明生效：学一小段，看讲解方式是否符合协作说明和 profile；说"收尾"后，数据仓库里应当出现一条"收尾"提交。
4. PDF：让模型用 read_source 读一份课件，说出其中某一页的内容；看不到时它应当直接告诉你。

## 13. 更新

**系统更新**（系统仓库有了新提交）：

```bash
sudo -iu learning bash -c '
set -e
cd /home/learning/system
git pull --ff-only
cd server
/home/learning/.local/bin/uv sync --locked --extra test
/home/learning/.local/bin/uv run --locked --extra test python -m pytest -q
' &&
sudo systemctl restart learning-mcp &&
sudo systemctl --no-pager status learning-mcp
```

只改了 harness/ 时，`git pull` 之后就已生效，重启也无妨。改了服务端代码或依赖时，必须走完整个流程。重启后再做第 9 步的两项检查。

如果新版本提升了数据格式版本，服务会拒绝启动并提示迁移，按那个版本的发布说明执行迁移后再重启。

**个人数据**：在本地数据仓库修改 profile/ 后 commit 并 push，服务端在下一次 start_session 时拉取，不需要操作服务器。

**日志**：`sudo journalctl -u learning-mcp -f`。
