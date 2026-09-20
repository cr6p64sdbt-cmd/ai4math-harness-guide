# AI4Math harness 学习仓库

本项目按需检索AI参与数学研究的方法，区分数学成果、系统机制和可复现证据。现有16个候选、9组系统与成果背景档案，以及2篇完整框架教程，另有1个补充专题条目；检索截至2026-09-20，不声称穷尽或所有候选均有已确认突破。

## 从这里开始

1. [项目任务说明](PROJECT-BRIEF.md)：用户要求、最新澄清与工作边界。
2. **[Danus 最新公开版全框架教程](systems/danus/FRAMEWORK-GUIDE.md)**：本次重点；探索通道、持久 workers、事实图、调度与成稿。
3. [QED 全框架教程](systems/qed/FRAMEWORK-GUIDE.md)：对照计划与整篇证明修订的另一条路线。
4. [中文入门导读](guides/START-HERE.md) → [16个候选目录](CANDIDATES.md) → [分类阅读](guides/PRIORITIES.md)。
5. [★ 平面ODE与动力系统专题](guides/DYNAMICAL-SYSTEMS.md)：方向标记用于选择阅读，数学仅简要筛选。
6. [横向比较与方法卡](guides/COMPARISON.md) · [来源与复用入口](references/SOURCES.md)。

下表是系统概览与既有成果背景，不把每篇概览都称为全框架教程。历史数学检查已做的部分保留，今后不默认重复或扩展。

|系统|研究组织重点|数学案例|
|---|---|---|
|[FunSearch](systems/funsearch.md)|程序生成、精确评价、岛群搜索|[八维512-cap构造](dossiers/2023-funsearch-capset.md)：独立有限证书检查已完成|
|[ProofCouncil](systems/proof-council.md)|作者、批评者、多模型咨询|[加权Bernoulli问题](dossiers/2026-proof-council-firstproof.md)：受审的部分进展，完整分类未解决|
|[Danus](systems/danus.md) · [全框架](systems/danus/FRAMEWORK-GUIDE.md)|长期事实图、任务分工、依赖检查|[YTD cscK反例声称](dossiers/2026-ytd-disproof-ai-workflow.md)：补充数学路线、版本与贡献边界|
|[Aristotle](systems/aristotle-harmonic.md)|非形式思路、Lean搜索、形式证书|[Erdős #728](dossiers/2026-erdos-728-aristotle.md)：论文与Lean声明分层核对|
|[QED](systems/qed.md)|证明计划、分层核验、失败重试|[◇ 输运–扩散下界](dossiers/2026-qed-transport-diffusion.md)：分析命题与参数范围|
|[Albilich](systems/albilich.md)|证明状态图、债务、局部与整体集成|[Kourovka 21.142](dossiers/2026-albilich-group-theory.md)：运行草稿与人类修订论文分开|
|[AlphaEvolve](systems/alphaevolve.md)|程序进化、级联评价、搜索算法改写|[4×4复矩阵48次乘法](dossiers/2025-alphaevolve-matrix-multiplication.md)：4096坐标独立整数检查通过|
|[符号Lyapunov](systems/symbolic-lyapunov.md)|反向数据生成、候选表达式与检查器|[★ 平面系统非多项式证书](dossiers/2024-symbolic-lyapunov-planar.md)：可手算核验的重发现|
|[PINN奇性发现](systems/pinn-singularity-discovery.md)|神经数值优化、结构约束、误差修正|[◇ 不稳定自相似奇性](dossiers/2025-pinn-unstable-singularities.md)：数值候选，不是严格爆破证明|

补充阅读：[◇ fluid_lean来源剖面](dossiers/2026-fluid-lean-source-profile.md)。★为平面ODE直接相关，◆为其他ODE/动力系统直接相关，◇为相邻PDE。补充层表示阅读/流程证据范围，不等于数学重要性低。

## 状态、来源与后续更新

- [当前状态与验收](STATUS.md) · [按需检索工作流](WORKFLOW.md) · [首批收据](references/notes/2026-09-20-harness-survey.md) · [扩充批次收据](references/notes/2026-09-20-expansion-survey.md)
- [事件统计](STATS.md)：仅从`events/`生成；候选数不是成果数，统计含历史记录。
- [事件卡模板](templates/event-card.md) · [系统模板](templates/system-dossier.md) · [案例模板](templates/case-dossier.md)

## 历史记录

固定四周试点已按实际产物结束，仅有[2026-W35周报](briefs/2026-W35.md)，未补造其余周次。周报及旧档案是当时的观察快照，不能直接当作当前核实结论；Danus最新情况以本批档案为准。

- [OpenAI Astra旧系统档案](systems/openai-astra-internal-2026.md) · [十项结果旧案例](dossiers/2026-openai-ten-advances-workflow.md) · [事件](events/2026/2026-08-01-openai-ten-advances.md)
- [Claude旧系统档案](systems/claude-research-multiagent-2026.md) · [ζ零点比例旧案例](dossiers/2026-claude-zeta-bound-workflow.md) · [事件](events/2026/2026-08-10-claude-zeta-bound.md)
- [YTD更新后的事件卡](events/2026/2026-08-19-ytd-disproof-claim.md)；原[周报模板](templates/weekly-brief.md)保留供历史格式参考。

`systems/`讲系统，`dossiers/`讲成果，`events/`提供统计，`guides/`提供教学路径，`references/`保存来源和批次记录。默认只读公开外部材料；不运行外部系统、不修改其他研究项目、不创建自动化。分享和复用范围见[README](README.md)及[许可说明](LICENSE.md)。

收录质量复评：方向相关不降低门槛；保留符号Lyapunov的方法价值，暂缓RL电网案例、撤下AI Poincaré推荐。详见[三项复评](references/notes/2026-09-20-dynamics-adjudication.md)。
