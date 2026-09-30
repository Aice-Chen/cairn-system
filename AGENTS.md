# 学习系统源码仓库

这个仓库是学习系统本身：MCP 服务端、学习协作说明、格式规范和数据仓库模板。它不包含任何个人学习数据，个人数据在单独的私有数据仓库中。

- 修改前先读 DESIGN.md；涉及服务端的，再读 server/SPEC.md。按 DESIGN.md"修改系统的方式"，先向学习者说明要改什么、为什么，确认后再动手，改完追加决策记录。
- harness/guide.md 和 harness/standards/ 是交给学习会话中的模型的说明，由 start_session 和 read_standard 返回。在本仓库里做开发时，它们是要维护的内容。
- 改动原始数据的格式时，按 DESIGN.md"演进与迁移"处理：提升 SUPPORTED_FORMAT_VERSION，并在同一次提交中加入迁移。
- 个人数据、实例信息（域名、服务器地址、账号）和任何密钥都不进入本仓库；实例信息记在数据仓库的 DEPLOYMENT.md。
- 测试：`cd server && uv run --locked --extra test python -m pytest -q`。修改依赖时先运行 `uv lock`，把 pyproject.toml 和 uv.lock 一起提交。
