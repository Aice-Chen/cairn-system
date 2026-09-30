# Cairn 学习数据

Cairn 的个人数据仓库 cairn-data，保持私有。系统本身（服务端、协作说明、格式规范）在 cairn-system 仓库中。本地建议将两个仓库分别放在 Cairn/data 和 Cairn/system；学习时打开 Cairn/data。

| 位置 | 内容 | 谁来写 |
|---|---|---|
| profile/ | 背景、目标、协作偏好。每次会话开场时全部读入，保持精简；文件按文件名顺序读取，可用数字前缀控制顺序 | 学习者 |
| state/log/ | 每次学习的观察记录，写完不再修改 | learning 服务 |
| state/progress/ | 每个资源的进度 | learning 服务 |
| state/concepts.md | 概念掌握情况，整合时由 log 派生 | learning 服务 |
| sources/ | 学习材料，Syncthing 同步，不进 git | 学习者放入，或服务端下载 |
| FORMAT_VERSION | 数据格式版本，只在迁移时改动 | 迁移程序 |
| DEPLOYMENT.md | 部署记录：域名、服务器、组件版本（不含密钥） | 部署者 |

修改 profile/ 后 commit 并 push，服务端会在下一次 start_session 时拉取。
