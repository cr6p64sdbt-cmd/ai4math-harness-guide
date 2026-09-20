# Danus 最新公开版本确认与阅读范围

查询日：2026-09-20。此处“最新”指查询时官方默认分支的 HEAD，不等同正式 release 或历史数学成果运行版本。

## 官方元数据

- [仓库 API](https://api.github.com/repos/frenzymath/Danus)：`default_branch = codex`。
- [分支 API](https://api.github.com/repos/frenzymath/Danus/branches)、[tags API](https://api.github.com/repos/frenzymath/Danus/tags)、[最新 release API](https://api.github.com/repos/frenzymath/Danus/releases/latest)：最新 release 是 `v0.1.0`，发布时间 2026-07-07T18:58:19Z；release 不代表当前默认分支最新代码。
- [codex 最近提交](https://api.github.com/repos/frenzymath/Danus/commits?sha=codex&per_page=5)：8月23日 `bbb4fd6848ad8d7024494dcf5f7ac6f283cedbb3` 对齐内部 v3 设计；8月27日 HEAD 更新 README 的 YTD 链接。

|分支或标签|查询时 commit|提交日期（UTC）|
|---|---|---|
|`codex`|`6d92e8d415933ca2ef52fd1a4da73fdfcd418f1c`|2026-08-27T03:34:27Z|
|`main`|`1a2cb99f9b16abb6b82d1bda207ed8a822f12743`|2026-08-27T03:34:30Z|
|`v0.1.0`|`7aad41077147af7b8f2a697512075bb326ade992`|2026-07-07T18:48:56Z|
|`v0.1.0-codex`|`7a51336e53cd1d558d0e766a61eb0fed46ebb05b`|2026-08-11T12:05:39Z|

本轮 HEAD 与旧档案相同，新增的是完整框架解释和最新状态再确认，不声称发现了更晚的代码更新。YTD 原始运行未精确绑定到当前 HEAD。

## 读取范围与分工

主控读取 README、AGENTS、`.codex/config.toml`、`config/danus.env.example`、操作与信任文档；两份有界模块定位见[事实/验证/记忆](2026-09-20-danus-state-map.md)及[运行/停止/写作](2026-09-20-danus-runtime-map.md)。主控抽查关键接口后整合[完整教程](../../systems/danus/FRAMEWORK-GUIDE.md)。仅读取文本，不安装或运行 Danus，不获取或审读 AI 生成数学论文证明。

## 重要解释边界

- 最新 AGENTS 要求主控持续高层数学推理、探索性子代理与证明 workers 双通道、30分钟控制节拍、4小时全局复盘、纯文本数学。它们属于上游运行契约，不是本仓库新增指令。
- 旧 `docs/operating-guide.md` 仍写 main 不做数学、约2小时且新状态触发策略；与最新契约冲突。本文将其标为旧措辞，不拼成无冲突的统一规范。
- `.codex/config.toml` 主控 `ultra` 与环境模板的通用 `xhigh` 默认分属不同配置层，不能统一叫“全系统默认 ultra”。
- MCP 角色权限是工具暴露边界；高权限 shell 的宿主环境隔离仍需单独保证。

## 主控实际读取字节的 SHA-256

只记录本次通过固定 raw URL 读取的字节哈希，未保存完整源码包。每项链接都可用于以后重新取源。

|文件|SHA-256|
|---|---|
|[README.md](https://raw.githubusercontent.com/frenzymath/Danus/6d92e8d415933ca2ef52fd1a4da73fdfcd418f1c/README.md)|`24abd1150deb8b94db7d65c3c8fc80f82d033d6472ac8c89833ad9fd4367a046`|
|[AGENTS.md](https://raw.githubusercontent.com/frenzymath/Danus/6d92e8d415933ca2ef52fd1a4da73fdfcd418f1c/AGENTS.md)|`2a6ba2b3fd4e267e587e90bcc63c45d0f8c73bf16e403b3ba0e18a56673ae975`|
|[.codex/config.toml](https://raw.githubusercontent.com/frenzymath/Danus/6d92e8d415933ca2ef52fd1a4da73fdfcd418f1c/.codex/config.toml)|`dc9de6cb2e43c808a1be7a13eac5cfb0c4e1cf654775c001bd3543a25e9f2036`|
|[config/danus.env.example](https://raw.githubusercontent.com/frenzymath/Danus/6d92e8d415933ca2ef52fd1a4da73fdfcd418f1c/config/danus.env.example)|`1824ee1e6f3058f4d0c9d30a526fdd3a47ed734f6d12ed9fb7e3ac429efc774a`|
|[docs/operating-guide.md](https://raw.githubusercontent.com/frenzymath/Danus/6d92e8d415933ca2ef52fd1a4da73fdfcd418f1c/docs/operating-guide.md)|`068426835e2781072eb98d0be02754e46f5f709e39872f67f7a6a30ec780c775`|
|[docs/security-and-trust.md](https://raw.githubusercontent.com/frenzymath/Danus/6d92e8d415933ca2ef52fd1a4da73fdfcd418f1c/docs/security-and-trust.md)|`ba819d467157c3e4bf1366d499af44e655f9d4efd76c4e5ea6c0399e251d3cbc`|
