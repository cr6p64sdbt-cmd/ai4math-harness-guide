# AI4Math 系统候选目录

已完成的完整框架教程：[Danus 最新公开版](systems/danus/FRAMEWORK-GUIDE.md)、[QED](systems/qed/FRAMEWORK-GUIDE.md)。下表的“深读”包括早期系统与成果背景档案，不等于全部候选都已完成全框架讲解。


检索截止：2026-09-20。首批13条，扩充后经质量复评保留 **16 个候选条目**；Rethlas 与 Archon 按共同论文的组合流程计为一条，不把模型版本重复计数。候选包含完整 harness、专用发现系统和作为对照的模型/工具链；不是16项已确认的原创数学突破。

先读 [入门导读](guides/START-HERE.md)，再按下面链接进入档案。查询、来源和停止边界见[首批收据](references/notes/2026-09-20-harness-survey.md)与[扩充收据](references/notes/2026-09-20-expansion-survey.md)。

## 一览：成果与方法分开看

“原始来源已读”仅表示下表所列范围已读，不表示数学已独立证明；“对照”不是负面评价。成果栏默认转述来源。

| # | 系统 / 类型 | 代表数学工作或评估对象 | 值得学习的方法 | 当前证据与阅读决定 |
|---|---|---|---|---|
| 1 | [Danus](systems/danus.md)：非形式化研究 harness | [YTD cscK 反例声称](dossiers/2026-ytd-disproof-ai-workflow.md)，另有系统论文六例 | 事实图、策略记忆、fresh verifier、依赖撤销、全局换路 | **深读**。论文与分支已查；重大主张仍 `OPEN`；历史运行未精确复现 |
| 2 | [ProofCouncil](systems/proof-council.md)：非形式化证明 harness | [FirstProof P3 加权 Bernoulli 部分结果](dossiers/2026-proof-council-firstproof.md) | Author/Critic 循环、按需顾问和 CAS、真实轮次快照 | **深读**。有官方盲审、提交与轨迹；完整分类仍 `OPEN` |
| 3 | [Albilich](systems/albilich.md)：可干预研究 harness | [Kourovka 21.142群嵌入反例](dossiers/2026-albilich-group-theory.md) | 状态图、proof debt、局部与整体集成分离、advisor | **新增深读**。最终论文与旧AI草稿路线不同；归档自审更正部分统计，未独立验全文 |
| 4 | [QED](systems/qed.md)：多 agent 证明 harness | [输运–扩散范数下界](dossiers/2026-qed-transport-diffusion.md) | 分解/证明/验证分离、承重步骤、失败分层重试 | **新增深读；◇相邻PDE**。四个定理假设已分列；历史模型记载冲突，未独立审全文 |
| 5 | [Aletheia](https://arxiv.org/html/2602.10177v1)：内部研究 agent | eigenweights、独立集与部分 Erdős 问题，作者按贡献层级分类 | Generator/Verifier/Reviser、检索、推理预算 | 对照。读引言、§2 与贡献分类；未查各数学论文全文或内部 runtime |
| 6 | [Aristotle](systems/aristotle-harmonic.md)：自然语言＋形式证明系统/服务 | [Erdős #728 阶乘整除](dossiers/2026-erdos-728-aristotle.md)；IMO 为另一评估 | 引理提出、Lean 状态搜索、失败反馈、证书与语义分开 | **深读**。公开 Lean 源码已静态查；完整论文命题验收 `UNASSESSED`；未 kernel replay |
| 7 | [Rethlas → Archon](https://arxiv.org/html/2604.03789v1)：非形式化到形式化组合流程 | Anderson 问题：weak quasi-complete 不必 quasi-complete 的环，作者报告形式化反例 | Matlas 定理检索、自然语言发现、LeanSearch 与形式化补缺口 | 候补深读。读 §4 命题/路线及相关工作；未完整构建形式工程或核 Jensen 引用 |
| 8 | [DeepSeek-Prover-V2](https://github.com/deepseek-ai/DeepSeek-Prover-V2)：形式证明模型与训练流程 | miniF2F、PutnamBench、ProverBench；本条不宣称新数学定理 | 递归子目标、形式反馈、合成训练数据 | 模型对照。读官方 README 与论文摘要；基准性能不等于开放研究能力 |
| 9 | [LeanDojo / ReProver](https://github.com/lean-dojo/LeanDojo)：工具库＋检索证明模型 | Mathlib 定理基准及证明环境交互 | 可用前提检索、proof state/tactic 数据、程序化调用 Lean | 工具对照。读官方 README；不是通用自主研究 harness；原库现标 deprecated，指向 v2 |
| 10 | [AlphaGeometry](https://github.com/google-deepmind/alphageometry)：专用神经符号证明系统 | 官方库 IMO-AG-30 上 25/30，对照 DDAR 14/30 | 模型提辅助构造，专用符号引擎演绎 | 专用路线对照。读代码说明与结果表；竞赛题不计新数学发现，不能泛化到任意 ODE |
| 11 | [FunSearch](systems/funsearch.md)：LLM 程序进化搜索 | [八维 512-cap](dossiers/2023-funsearch-capset.md)，另有 admissible sets | 固定骨架、精确评价、islands、多次搜索、人理解代码结构 | **深读**。论文/源码/有限数据已读；本地精确核查有限证书，未复跑搜索 |
| 12 | [AlphaEvolve](systems/alphaevolve.md)：进化式 coding agent | [4×4复矩阵48次乘法](dossiers/2025-alphaevolve-matrix-multiplication.md) | 多模型改程序、分级评价、程序数据库 | **新增深读**。固定工件4096坐标通过独立整数检查；完整搜索代码未公开 |
| 13 | [AlphaTensor](https://github.com/google-deepmind/alphatensor)：强化学习算法发现系统 | 矩阵乘法张量分解；官方库有标准与模 2 算术工件 | 将分解转为序贯决策、输出可检验代数证书 | 历史对照。读官方成果库说明；不是 LLM harness，训练系统与结果工件分开 |
| 14 | [符号 Lyapunov](systems/symbolic-lyapunov.md)：专门符号生成系统 | [平面系统非多项式证书重发现](dossiers/2024-symbolic-lyapunov-planar.md) | 反向造数据、beam、符号/数值验证 | **新增深读；★平面ODE**。方法贡献及随机系统实验支持保留；简单例仅教学，整体实验不等于全局严格认证 |
| 15 | [PINN奇性发现](systems/pinn-singularity-discovery.md)：神经数值搜索 | [CCF、IPM、Boussinesq自相似候选](dossiers/2025-pinn-unstable-singularities.md) | 结构表示、GN优化、误差网络、后续梯度归一化 | **新增深读；◇相邻PDE**。数值发现，未严格证明爆破；不是LLM harness |
| 16 | [fluid_lean](dossiers/2026-fluid-lean-source-profile.md)：一次性形式化工程 | 带光滑外力的Euler/Boussinesq爆破 | 巨型Lean工程、区间证书、命题对照 | 高价值补充来源；**◇相邻PDE**。未重放，原论文加强条件与顶层声明有差异；harness过程不足 |

## 深读怎样从四组扩充到九组

首批四组分别覆盖事实图、证明修订、形式化和有限构造。第二批按数学成果、过程公开与方法差异新增QED、Albilich、AlphaEvolve；再加入与你的方向直接相关的符号Lyapunov和有代表性的PINN数值发现。详细分类与优先级见[分层阅读](guides/PRIORITIES.md)，方向标注见[动力系统专题](guides/DYNAMICAL-SYSTEMS.md)。

fluid_lean数学重要，但本轮缺少足够工作流材料，因此先做来源剖面；RL与AI Poincaré已撤出精选目录，理由见[收录复评](references/notes/2026-09-20-dynamics-adjudication.md)，不再作为方向相关即收录的补充。这是阅读和证据分层，不是宣称后者数学价值低或系统性能差。

## 有价值的限制与后续问题

### Albilich：不要只摘摘要的“10/10”

论文内部十题完成与人工九题明确匹配不能混写。第二批进一步读到固定仓库的[论文数据自审](https://github.com/uw-math-ai/albilich/blob/36c648cb3bc8d550fbe5c4035f177ef4c0a5f1c7/experiments/aaai27-final-paper/README.md)：摘要无CAS的9/10找不到对应归档；17.91 CAS-on归档5.250897M tokens与论文6.784M不一致，且对照prompts/搜索设置不同。因此撤回首批把32%当作已核实资源改善的简略表述，更不能据此推因果效果。两次根问题都未解决。详见[系统档案](systems/albilich.md)。

### QED：分析成果已完成本批定向深读

[案例](dossiers/2026-qed-transport-diffusion.md)已分列无扩散剪切、有扩散剪切、归一化负Sobolev范数和快速时间周期流的定理范围，并对无扩散关键步骤作说明。尚缺完整逐轮日志和全篇独立数学审稿；二维环面PDE不算平面ODE成果。

### Rethlas/Archon：检索到定理只是第一步

论文 §4.2 把关键转向归于 Matlas 找到 Jensen 的外部定理。学习重点应是怎样从引用候选回到假设匹配，以及形式化阶段怎样填自然语言证明留下的缺口。本批没有独立核 Jensen 原文，不能将这一引用链接受为本项目证明。[原文 §4](https://arxiv.org/html/2604.03789v1)

## 历史档案和未进入本批的范围

原有 [OpenAI 十项结果](dossiers/2026-openai-ten-advances-workflow.md)与 [Claude ζ 案例](dossiers/2026-claude-zeta-bound-workflow.md)保留为 2026-08-24 的历史记录，本批未刷新全部外部来源，不将其旧复现状态当作当前事实，也不为凑候选数重新计算。

未覆盖所有内部系统、所有 2026-09 新预印本、商业服务或社区复刻；未使用订阅引文索引。任何“没有找到”的结论仅为 `NOT-FOUND-IN-CHECKED-SET`。后续按你的学习问题扩展，不固定周报产量。
