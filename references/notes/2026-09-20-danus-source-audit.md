# Danus / YTD 来源复查记录（2026-09-20）

本笔记服务于 [Danus 系统档案](../../systems/danus.md)与 [YTD 案例深读](../../dossiers/2026-ytd-disproof-ai-workflow.md)。访问模式：公开来源、只读；未保存 PDF，未运行或安装外部 harness。文中源码位置为公开仓库固定 commit 的阅读定位，不代表本项目已经做实现验证。

## 检索范围与实际路线

- 先读本项目 `INDEX.md`、`STATUS.md`、`WORKFLOW.md`、旧系统和案例档案，找到旧状态“改进版未开放”。
- 直接打开 arXiv 系统论文 2607.06447v2、YTD 论文 2608.19301v1、官方 GitHub `frenzymath/Danus`；再查 arXiv abstract 页面确认：系统论文仍以 v2 为最近修订（2026-07-08），YTD 仍是 v1（2026-08-19）。
- 公共搜索式包括“Danus improved Codex GPT-5.6-sol release”“YTD 2608.19301 version September 2026”“Danus 2607.06447 version”“YTD disproof comments correction”。搜索结果仅用于定位，结论回到 arXiv 正文与官方仓库。
- `git ls-remote` 读取 2026-09-20 分支 HEAD：`main=1a2cb99f9b16abb6b82d1bda207ed8a822f12743`；`codex=6d92e8d415933ca2ef52fd1a4da73fdfcd418f1c`。GitHub 官方 commits API 显示 codex 现 HEAD 为 2026-08-27 README 链接更新；`bbb4fd6848ad8d7024494dcf5f7ac6f283cedbb3`（2026-08-23）提交信息为“Align the codex branch with the internal Danus v3 design”。这证实相关公开代码存在，但**没有证明那次历史运行恰用这个 commit**。
- 未执行系统性 forward-citation、付费数据库或独立专家评论搜索；“未找到独立验证”仅限本次查阅集合。

## 原始来源与读到的具体内容

| 来源、版本 | 已读位置与用途 | 阅读深度 / 未覆盖 |
|---|---|---|
| [Danus 论文 arXiv:2607.06447v2](https://arxiv.org/html/2607.06447v2)；[版本页](https://arxiv.org/abs/2607.06447) | §2.1 任务到论文的流程；§2.2 DAG、依赖和撤销；§2.3 local/global memory；§2.4 论文版主 agent；§2.5 worker、verifier、3–9 worker；§2.6 Matlas 和工具；§2.7 进度与整篇检查；§3 案例声明。 | 正文 section-summary。未审计六案例对应原论文的证明。 |
| [YTD arXiv:2608.19301v1](https://arxiv.org/html/2608.19301v1)；[版本页](https://arxiv.org/abs/2608.19301) | Conjecture 1.1 精确的 normal ample 所有 exponent 约定；Theorems A、B；§1.3–1.4 先例和等号难点；Construction 3.7、Proposition 3.8、Lemma 3.19 的多项式及无理重根；Proposition 3.12 的近似 cscK 度量、Proposition 3.13 末段的范数冲突；§4 的滤过分析与 Proposition 5.3 的一般下界路线；§6 标题/结构；§7 Theorem A 的依赖汇总；Appendix A 两次运行、模型配置、人类介入与表 1–3。 | 数学“section-summary + 关键式定位”，未逐行复核 §4–6、外部引文和 79 页全证明；无 faithful proof excerpt，状态不得升级为 PROVED/DISPROVED。 |
| [Danus `codex` README@6d92e8d](https://github.com/frenzymath/Danus/blob/6d92e8d415933ca2ef52fd1a4da73fdfcd418f1c/README.md) | “This branch is the version that solved YTD”、Codex 主协调者、无外部 strategy consult、目录、quickstart 与自带密钥。 | README 阅读；该句为维护者的版本声明，不是运行身份的加密绑定。 |
| [`ARCHITECTURE.md@6d92e8d`](https://github.com/frenzymath/Danus/blob/6d92e8d415933ca2ef52fd1a4da73fdfcd418f1c/ARCHITECTURE.md)、[`AGENTS.md@6d92e8d`](https://github.com/frenzymath/Danus/blob/6d92e8d415933ca2ef52fd1a4da73fdfcd418f1c/AGENTS.md) | §3 fact ID 内容、权限、角色、策略记忆；主 agent 做高层数学思考的操作要求。两文件的“main does no math”与“main does high-level math”文字有范围不一之处。 | 文档阅读；未追踪所有命令实现路径。 |
| [`danus/gateway/roles.py@6d92e8d`](https://github.com/frenzymath/Danus/blob/6d92e8d415933ca2ef52fd1a4da73fdfcd418f1c/danus/gateway/roles.py)、[安全文档@6d92e8d](https://github.com/frenzymath/Danus/blob/6d92e8d415933ca2ef52fd1a4da73fdfcd418f1c/docs/security-and-trust.md) | 角色工具表：worker 能 `fact_submit`，main 不能，verifier 只读；安全文档 §1–4 明示 cold-start LLM verdict 不是 formal proof、write-gate 和 sandbox bypass。 | 静态片段阅读；没有运行接口测试或完整安全审计。 |
| [`config/danus.env.example@6d92e8d`](https://github.com/frenzymath/Danus/blob/6d92e8d415933ca2ef52fd1a4da73fdfcd418f1c/config/danus.env.example) | 当前可配置模型、effort、后端、服务端口与运行目录。 | 只说明当前模板；不能倒填论文案例参数。 |

## 版本变化与纠错

旧档案写“YTD improved Danus 尚未公开”，这是依据 2026-08-19 [YTD 附录 A 脚注](https://arxiv.org/html/2608.19301v1) 的当时承诺；公开分支在 2026-08-23 已出现对齐内部 v3 设计的提交，2026-08-27 HEAD 可读取。故系统档案和案例档案改为“相关实现已公开／历史运行未复现”。系统论文 §2 的 Claude Code/Opus 4.8 + GPT-5.5 workers 与 YTD 附录的 Codex/GPT-5.6-sol 不能混写。

旧 dossier 原本只概称“五维簇 + K-polystability + nonexistence”，本次补充了 Theorem A 的对象、全部正 exponent 与 normal ample 类目、Theorem B 的等号刚性和 §3–7 的依赖顺序。它仍是来源导读，不能替代逐定理假设核对。

## 剩余缺口与更新条件

1. YTD 第一次协作和 fresh run 的原始 prompt、人工操作时间线、完整事实图、验证记录与论文运行环境快照尚未取得。附录的 616/88/924 统计只属**原始协作运行**；fresh run 只明确 3 个探索性 Codex subagents 和 5 小时 29 分钟。不能把两个运行的统计合并。
2. 没有本项目对 Theorem B 中全部正规 test configurations 分类的重建，也没有逐行核对 Proposition 5.3、Proposition 3.13 的外部引文及所有参数。作者报告的人类终审不能自动升格为项目独立验收。
3. 公共 `codex` 代码可以检查模块设计，但确切案例运行是否逐字节使用 `bbb4fd6`、后续 `6d92e8d` 或内部未公开变体，尚未闭合；需 release/tag、run manifest 或带时间戳的工件。
4. 费用、失败尝试总数、不同基线的等预算性、第三方复跑与系统消融未在已读来源中闭合。若出现 arXiv 新版、勘误、正式审读或运行工件，再定向更新。
