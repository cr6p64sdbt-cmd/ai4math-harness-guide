# ProofCouncil / FirstProof P3 来源审计（2026-09-20）

## 本批检索契约与状态

- 阶段：`deep-evidence`，针对已指定的 ProofCouncil 系统和一个可读、可评估的具体案例；不作 AI4Math 全领域穷尽或新颖性穷尽检索。
- 目标：核对系统架构、官方挑战所用版本、数学题目、提交结果、官方评估及可见失败；排除用新版配置解释旧成绩。
- 路线：`OPEN-ONLY`；本地 `INDEX.md`、`STATUS.md`、`WORKFLOW.md` 与模板；arXiv 原始 HTML；作者仓库；FirstProof 官方站、报告和官方 GitHub 仓库。实际查询包括 `ProofCouncil FirstProof problem...`、`site:firstproof.org second batch official evaluation...`，再追踪官方页面关联链接。新闻/社区搜索结果没有用于接受数学结论。
- 发现路线、全文路线、证据接受分开：论文由 arXiv 取得；官方解答/审稿/日志由 FirstProof 站定位后从官方 GitHub 读取；代码由两个官方仓库读取。未涉及机构认证或付费来源。
- 停止条件：找到一个题目原文、匿名提交、三份审稿、人类解答、冻结系统配置和至少两轮运行快照，足以写出有边界的教学型案例。本次达到。其余九题、全部中间消息和引文网络不在本次读取集，不能作负面穷尽断言。

## 来源清单、版本与实际读取深度

| 来源 | 定位、版本 | 本轮实际读取 | 证据用途与上限 |
| --- | --- | --- | --- |
| [ProofCouncil 论文](https://arxiv.org/html/2607.09474) | `arXiv:2607.09474v1`，2026-07-10；§1、§2.1–2.2、§3.1–3.2、§4、贡献说明，附录 A 的目录与关键结果 | HTML 正文分节读取；未逐句审计附录 A 的全部证明或附录 C 全部 prompts | `section-summary`：系统架构、角色、整批评估、成本与失败案例；不是 P3 完整证明证书。 |
| [FirstProof Second Batch 官方页面](https://1stproof.org/second-batch.html) 与 [官方报告](https://1stproof.org/assets/docs/report.pdf) | 页面；报告 §2–§5，重点 §3.3、§4.1、§5.3；报告 PDF 第 14–15、21、27 页（网站 PDF 零起页与印刷页差一） | 读取评估设计、P3 题目及背景、系统 A 身份、P3 编辑决定与理由；未逐页核对全部 36 页 | `PRIMARY-SOURCE-CHECKED`：原题和官方评估。报告认为 P3 部分结果正确、新颖、Minor Revisions；**并未说完整分类已证**。 |
| [官方匿名提交 P3-A](https://github.com/1stproof/batch-2/blob/274625a22e4748d5f9264ba3614353461520bd20/batch-2-AI-solutions/problem-03/submission-A.tex) | `1stproof/batch-2` commit `274625a22e4748d5f9264ba3614353461520bd20`；`Problem statement`、`Positive values`、`Values that cannot work`、`Equivalent forms` | 读取约前 300 行并定位剩余正文；重建 coloring criterion 和两组简单反例，未逐行检查全篇 | `section-summary`，关键段落的局部 `assumptions-checked`；全篇数学状态仍依赖官方专家审稿，非本项目独立证明。 |
| [P3 三份匿名审稿](https://github.com/1stproof/batch-2/tree/274625a22e4748d5f9264ba3614353461520bd20/batch-2-reviews/problem-03/submission-A) | 同一官方 commit；各 reviewer 的 `Review` 与 `Recommendation`，没有逐条读完内嵌全文注释 | 核对每位的 correctness、novelty、presentation 判断及 MMS/引文意见 | `PRIMARY-SOURCE-CHECKED`：人工评估；审稿意见之间侧重点不同，报告编辑决定为最终官方口径。 |
| [P3 人类解答](https://github.com/1stproof/batch-2/blob/274625a22e4748d5f9264ba3614353461520bd20/batch-2-human-solution/problem-03/human-solution.tex) | 同一官方 commit，摘要与引言、MMS 叙述 | 核对原题、已知 (1/k)、MMS 与 Pokrovskiy 关联；未逐行核对其后完整论证 | 只作比较与前人成果定位，不冒充本项目数学复证明。 |
| [主办方冻结的系统代码](https://github.com/1stproof/batch-2/tree/274625a22e4748d5f9264ba3614353461520bd20/batch-2-submissions/improofbench) | 同一官方 commit；`configs/workflows/author_critic.yaml`、`author_critic_long.yaml`、`README.md` | 读取角色模型、轮次、budget、adapter、Docker/沙箱说明；未静态审计全部 Python，也未运行 | 五月挑战配置依据；总上限与默认值不是每题实际消耗。 |
| [官方 P3 原始运行快照](https://github.com/1stproof/batch-2/tree/274625a22e4748d5f9264ba3614353461520bd20/batch-2-raw-outputs/IMProofBench/WorkflowRuns/firstproof-prob-003-20260529T215332Z-6a40eb14) | `round-0/answer.tex`、`round-10/answer.tex`、`round-15/answer.tex`；`round-15/research_notes.tex` 定位 | 重点比较 round 0 与 round 10 正文、最终提交；未顺序读取完整 Critic、council 或 compute 对话 | 可确认早期过度宣称变为承认局部成果；**不能确认反馈的精确因果链**。 |
| [作者公开仓库](https://github.com/eth-sri/proof-council/tree/e7e1ea5236585e817a09de0e416a57c6c3013f77) | commit `e7e1ea5236585e817a09de0e416a57c6c3013f77`，2026-09-10；`README.md`、`configs/workflows/firstproof_submission.yaml` | 核对当前启动、CLI、输入输出和模型配置 | 此快照已有 `gpt-5.6-sol` 等，**不能倒填为五月官方评测配置**；未实际安装执行。 |

`ProofCouncil.pdf` 和 FirstProof 官方报告 PDF 均可公开获取，但本批阅读 HTML/在线 PDF 加官方 TeX 已满足教学解释与版本核查；没有保存 PDF，因此没有本地 PDF SHA-256。官方 GitHub commit 用作当前阅读的冻结定位；不声称 GitHub 未来 `main` 不变。

## 可检查的关键依据

1. **完整命题与未决部分**：官方报告 §3.3；P3-A 提交第 19–38 行写出量词与 `small-p assertion` 缺口；提交第 43–130 行给 coloring criterion、pairing lemma 与 \(p=2/k\)，第 197–224 行给反例与余下猜想。[提交原文](https://raw.githubusercontent.com/1stproof/batch-2/274625a22e4748d5f9264ba3614353461520bd20/batch-2-AI-solutions/problem-03/submission-A.tex)。
2. **审稿结论**：官方报告 §5.3（PDF 第 27 页）写 P3-A `Minor Revisions`，并称 \(p=2/k\) 的 pairing lemma 路线 *appears to be novel*，同时指出未抓到 MMS/Pokrovskiy。[官方报告](https://1stproof.org/assets/docs/report.pdf)。
3. **早期错误与后期收缩**：[round 0](https://raw.githubusercontent.com/1stproof/batch-2/274625a22e4748d5f9264ba3614353461520bd20/batch-2-raw-outputs/IMProofBench/WorkflowRuns/firstproof-prob-003-20260529T215332Z-6a40eb14/ac_workspaces/prob-003-50f20aa0b43c/.ac/round-0/answer.tex) 第 24–51 行以 Kellerer 归因声称覆盖整个 \(p\le1/3\)；[round 10](https://raw.githubusercontent.com/1stproof/batch-2/274625a22e4748d5f9264ba3614353461520bd20/batch-2-raw-outputs/IMProofBench/WorkflowRuns/firstproof-prob-003-20260529T215332Z-6a40eb14/ac_workspaces/prob-003-50f20aa0b43c/.ac/round-10/answer.tex) 第 19–39 行改为部分结果与明确开放缺口。尚未核对 Kellerer 原文，故这里只记录“未核实的引用支撑了过强宣称”，不独立断言其文献全部无关。
4. **版本差异**：[五月 `author_critic_long.yaml`](https://raw.githubusercontent.com/1stproof/batch-2/274625a22e4748d5f9264ba3614353461520bd20/batch-2-submissions/improofbench/configs/workflows/author_critic_long.yaml) 第 13–37 行与[九月 `firstproof_submission.yaml`](https://raw.githubusercontent.com/eth-sri/proof-council/e7e1ea5236585e817a09de0e416a57c6c3013f77/configs/workflows/firstproof_submission.yaml) 第 0–28 行模型配置不同。论文 §2.1 与 §3.2 提供比赛概括，公开库只是当前接口。
5. **内审边界**：论文 §3.2.2 把 P3 的持续拒绝与外审 minor revisions 并列，称为值得注意的失败情形，但没有直接使用“false negative”一词；P3 全题未完成而外审接受正确部分进展，两种判准未必一致。本项目不将 P3 判为已证实的内部假阴性。P8 的误接纳有外审指出的具体未证断言；P6 因 API timeout 无交卷。[论文](https://arxiv.org/html/2607.09474)。

## 未解决问题与复核入口

- P3 `pairs` 引理、乘法闭性与其余等价变形尚未全部逐行独立复核；审稿支持不能代替本项目的 proved 标签。若用于后续数学推导，先建立 faithful excerpt，核量词与证明每步。
- 原始轨迹中的逐次请求、Critic 所用完成判准、具体 council/compute 建议、哪个节点首次提出 coloring criterion 或 pairing lemma、每次状态翻转尚未完成因果审计。只能说论文报告这些组件在 P3 被使用。
- P3 单题成本、token、确切运行轮数/墙钟时间需从 `token_usage` 和 run summary 提取；本批只使用论文整批统计与快照轮号，不把轮号等同总执行轮数。
- MMS 与 Pokrovskiy 的原论文没有在本批独立全文核查；相关已知覆盖依据官方人类解答与专家评估，若做数学引用应另开来源级核对。
- 公开源码的可运行性、API 版本兼容、计算沙箱隔离和实际权限没有验证。任何试运行都需独立授权与隔离审计；本项目只读。

本审计对应 [系统档案](../../systems/proof-council.md) 与 [P3 案例](../../dossiers/2026-proof-council-firstproof.md)。
