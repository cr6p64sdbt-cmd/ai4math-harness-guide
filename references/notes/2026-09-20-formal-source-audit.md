# 2026-09-20 形式化路线来源审计：Aristotle / Erdős #728

## 搜索约定与实际范围

- 阶段：四席深读中的形式化席；`OPEN-ONLY`，公开网页与原始论文、公开源码只读。
- 对象：可解释 harness 工作流、具有具体研究数学问题与公开 Lean 工件的系统。排除仅竞赛 benchmark、仅宣传页、仅 `sorry` 目标陈述。
- 时间政策：无硬性年份门槛；重点核 2025–2026 年材料。检索日：2026-09-20。
- 去重单位：系统 + 具体数学结果 + 实际运行版本；Aristotle #728 初次输出、第二次输出、Alexeev 简化文件不混作一个字节版本。
- 证据上限：论文/源码阅读与静态核对；未运行 Lean、Aristotle 或其他 harness，未做独立数论证明审查；不作穷尽新颖性结论。
- 停止条件：找到满足上述条件且原始论文与 Lean 文件可读的一例，完成系统及案例档案；其余路线留候选。

## 实际检索与取得路线

| 目的 | 实际查询或路径 | 取得结果 | 状态 |
| --- | --- | --- | --- |
| 广域定位 | web 查询 `site:arxiv.org Aristotle Harmonic AI mathematician Lean Erdős problem formalized theorem paper 2026`、`site:arxiv.org AxiomProver research mathematics Lean theorem 2026`、`site:harmonic.fun Aristotle Lean math research proof paper Erdős problem` | 找到 [#728 论文](https://arxiv.org/abs/2601.07421)、[Aristotle 系统论文](https://arxiv.org/abs/2510.01346v2)、Ax-Prover/Grasshopper 等线索 | locator 后转原文 |
| 证明工件 | web 查询 `Resolution of Erdős Problem #728 Aristotle Lean code github Sothanaphan Barreto`、`site:github.com Erdos 728 Aristotle Lean`；论文 v5 参考文献 [1] | [Alexeev 的 `Erdos728b.lean`](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/v4.24.0/ErdosProblems/Erdos728b.lean)；[另一 `Erdos728p.lean`](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/v4.24.0/ErdosProblems/Erdos728p.lean) | b 文件正文已读；p 仅检查来源区别 |
| 系统机制 | [Aristotle 系统论文 PDF](https://arxiv.org/pdf/2510.01346v2)，读 §2.1–2.3、§3.1、§4 | proof search、引理循环、Lean 反馈、IMO 人工 formal statement、几何部件 | section-summary |
| 数学原文 | [Sothanaphan arXiv v5 PDF](https://arxiv.org/pdf/2601.07421v5)，读摘要、§§1–6、证明故事附录、相关文献段 | Theorem 1、Lemmas 1–14 骨架、§6 Lean 映射、时间线 | section-summary；承重证明未逐行复核 |
| 代码直接取得 | GitHub raw URL 的 commit `8822f7ddef30fadbd92e1c6ab4ed897af356af5e`，静态检索 `sorry`/`axiom`/`admit`，读主定义和顶层声明；`git ls-remote ... HEAD` 取得 hash | b 文件 `sorry` 全词 0、活动 `axiom` 声明 0、`admit` 0；UTF-8 文本 SHA-256 `40f4cbf2ccaefa5d84fc44ece63d1e4c3fed3e47b631057ef337fc92465d7b9f` | 静态文本检查，非 kernel replay |
| 工具链 | [项目 `lean-toolchain`](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/v4.24.0/lean-toolchain)、[`lakefile.toml`](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/v4.24.0/lakefile.toml) | Lean 4.24.0 / Mathlib `f897ebcf72cd16f89ab4577d0c826cd14afaafc7` | 源码核对，未安装/构建 |
| 对照与 API | [Formal Conjectures #728 目标](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/728.lean)、[Harmonic 维护的 PyPI 页面](https://pypi.org/project/aristotlelib/)、[Tao 的 AI contributions wiki](https://github.com/teorth/erdosproblems/wiki/AI-contributions-to-Erd%C5%91s-problems) | 区分待证 `sorry` 目标与已发布证明文件；当前 SDK 版本 2.1.0 | 来源作用不同，不替代 paper/Lean |

没有调用机构订阅、SSO、Zotero 或引用索引；`erdosproblems.com/728` 直接打开在 web 工具返回内部错误，因此具体时间线主要根据论文附录而非本站线程逐帖核对。没有保存 PDF；重复精读的需求未达到全文转译门槛。没有建立“无先前解答”的独立引文网络证明；这里只记录论文作者截至 2026-01-27 的报告。发现、全文取得与证据接受分开处理。

## 原文与形式化的承重对照

| 事项 | 准确定位 | 本次判读 |
| --- | --- | --- |
| 论文强命题 | [v5 Theorem 1, p.2；§5, p.10](https://arxiv.org/pdf/2601.07421v5) | 任给 $C_1<C_2$、$0<\varepsilon<1/2$，无限多三元组，且双侧比例界与双侧对数窗 |
| Lean 第一顶层 | [`good_triples` L501–504，`erdos_728` L1344–1366](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/v4.24.0/ErdosProblems/Erdos728b.lean#L1344-L1366) | `.Infinite` 与双侧比例界，只有对数下界 |
| Lean 第二顶层 | [`erdos_728_fc` L1375–1414](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/v4.24.0/ErdosProblems/Erdos728b.lean#L1375-L1414) | 对任意上下常数存在一组，仅下比例界，非无限多声明 |
| 公理注释 | [L1416–1420](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/v4.24.0/ErdosProblems/Erdos728b.lean#L1416-L1420) | 源文件写有 `#print axioms` 和普通公理列表注释，未在本地执行 |

结论：论文最强定理不能仅由目前列出的任一 Lean 顶层声明**直接**读出。可能通过文件中已有构造引理拼成对应形式定理，但这仍须实际形式化与 kernel replay。静态无 `sorry` 只回答源码文本中没有占位词，不回答 Mathlib 依赖、公理或 statement 是否适配论文。

## 相关候选与拒绝误用

- [Ax-Prover（arXiv:2510.12787）](https://arxiv.org/abs/2510.12787)：Lean/MCP 多代理框架，含抽象代数、量子等 benchmark 与密码学形式化案例；本轮只发现摘要，未进入深读，不能对其研究级数学成果作肯定判定。
- [Grasshopper Aristotle API 案例（arXiv:2605.20120）](https://arxiv.org/abs/2605.20120)：作者摘要明确主定理仍有一个 `sorry`，适合失败边界对照，不能列为已完成定理。
- [AlphaProof + AlphaGeometry 2](https://www.nature.com/articles/s41586-025-09462-5)：系统论文/竞赛形式验证候选，研究级新数学成果需要另选案例；本轮未读正文。
- [Formal Conjectures #728](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/728.lean)：含 `sorry` 的形式目标与外部证明链接，不把这个文件本身列为 kernel 证书。

重新打开条件：取得顶层 statement 对齐的文件、运行固定 Lean 环境及公理审计、取得原始交互日志，或出现勘误/正式独立复现。仍使用 `NOT-FOUND-IN-CHECKED-SET` 描述有界检索的阴性结果。

版本补核：2026-09-20 打开 arXiv 版本页，系统论文最新为 2510.01346v2（2025-10-10），数学论文为2601.07421v5（2026-01-26；初版2026-01-12）；已将系统论文入口固定到v2。版本页确认不构成案例内部系统版本的绑定。
