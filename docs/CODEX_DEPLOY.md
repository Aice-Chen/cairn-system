# Cairn 部署任务说明（交给 Codex 执行）

## 任务

在一台新的 VPS 上部署 Cairn 学习系统，让各客户端通过 `https://<DOMAIN>/mcp` 使用它。DEPLOY.md 是命令参考；本文件规定分工、顺序、检查点和安全要求。

本次是部署任务。harness/guide.md 是学习会话的协作说明，与本任务无关。

## 参数

学习者在交给你之前填写，缺少任何一项时先问。

```
DOMAIN=            # 例如 learn.example.com
SSH_HOST=          # 本机 ~/.ssh/config 中指向 VPS 的别名；登录用户需要能免密 sudo
GITHUB_USER=
SYSTEM_REPO=cairn-system       # 公开
DATA_REPO=cairn-data           # 私有
TIMEZONE=Asia/Shanghai
LOCAL_DATA_DIR=    # 数据仓库在学习者电脑上的路径，例如 Cairn/data
```

本地建议使用 Cairn/system 和 Cairn/data 两个独立仓库目录。服务器内部继续使用 learning 用户、/home/learning/system、/home/learning/data、learning-mcp 服务和 learning 客户端连接名；仓库名称不作为服务器目录名。

## 工作方式

- 本地命令按学习者的 shell（PowerShell 或 bash）书写；服务器命令通过 `ssh -o BatchMode=yes $SSH_HOST` 执行，多行脚本整体传给服务器上的 bash。
- 每一步先检查现状再操作，保证可以重复执行。
- 密钥不进入对话、日志和 git：client secret 由学习者自己填入服务器上的环境变量文件；JWT 签名密钥在服务器上生成后直接写入；私钥留在生成它的机器上。确认是否已填好时，只检查占位符是否还在。
- 开启 ufw 之前，先放行 OpenSSH。
- 遇到预期之外的错误时，停下来说明现象和判断，等学习者决定。删除、覆盖已有配置、强制推送、修改服务器 SSH 设置，先征得同意。
- 每完成一个阶段，用一两句话报告结果和下一步。标有"检查点"的地方需要学习者操作。

## 阶段

0. **检查前提**：SSH 免密登录和免密 sudo；系统为 Ubuntu 24.04；本机 `gh auth status` 正常；$DOMAIN 已解析到服务器 IP；提醒学习者确认安全组已放行 22、80、443、22000/tcp。
1. **数据仓库**：按 DEPLOY.md 第 1 步，从系统仓库的 templates/data/ 在 $LOCAL_DATA_DIR 建立数据仓库，用 `gh repo create $GITHUB_USER/$DATA_REPO --private --source . --push` 推送。**检查点**：请学习者先填写 profile/ 的两个文件。
2. **服务器环境**：DEPLOY.md 第 2 步。
3. **两个仓库**：DEPLOY.md 第 4 步。部署密钥的公钥取回本机临时文件，用 `gh repo deploy-key add <文件> --repo $GITHUB_USER/$DATA_REPO --allow-write --title learning-vps` 添加后删除临时文件。
4. **依赖与测试**：DEPLOY.md 第 5 步，测试应当全部通过。
5. **环境变量**（含检查点）：按 DEPLOY.md 第 7 步建立文件，client id 和 secret 先写占位符 `<待填写>`，JWT 密钥在服务器上生成写入。**检查点**：请学习者按第 6 步建立 OAuth App，并把 Client ID 和 secret 填进文件。确认后检查占位符已不存在。
6. **服务与 HTTPS**：DEPLOY.md 第 8、9 步，完成两项验证。Caddyfile 已有其他站点时追加，不覆盖。
7. **Syncthing**：DEPLOY.md 第 10 步。先尝试用两端的命令行完成配对；不成功时交给学习者在界面操作（**检查点**）。用一个临时文件验证双向同步后删除。
8. **客户端**（学习者为主）：为当前 Codex 添加 learning 服务并请学习者完成登录；本机有 Claude Code 时一并添加。**检查点**：学习者接入网页端、建立 Project，并按第 12 步实测，把结果告诉你。
9. **部署记录**：在数据仓库中建立 DEPLOYMENT.md，记录部署日期、域名、SSH 别名、服务器路径、服务名、各组件版本、Syncthing 文件夹 ID、各客户端的实测结果，不含任何密钥。提交并推送。
