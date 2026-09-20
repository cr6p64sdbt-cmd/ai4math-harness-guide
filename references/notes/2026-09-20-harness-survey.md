# 首批 harness 学习检索收据

日期：2026-09-20。任务是有界检索和方法学习，非数学成果排行榜或穷尽综述。交付：[候选目录](../../CANDIDATES.md)、[导读](../../guides/START-HERE.md)、[比较](../../guides/COMPARISON.md)、[集中来源与复用入口](../SOURCES.md)。

## 范围、单位与停止条件

公开来源；自然语言证明/长程研究、形式化、可计算评价驱动发现三条路线。无硬性年份下限，以有具体数学工件、工作流可解释为标准。先查旧Danus版本，再从起始线索及相关工作扩展。去重以系统或明确组合流程为单位：Rethlas/Archon合为一条，基础模型和工具类显式标记，不当成多个研究成功案例。

本轮形成13个目录条目、四个深读席位：Danus、ProofCouncil、Aristotle、FunSearch。两个非形式证明席位、一个形式化席位、一个程序搜索席位均有可访问原始来源及具体案例；达到本批停止条件。没有搜索所有年份、所有系统或完整前向引文网络。额外发现但未筛入主目录的Ax-Prover、Grasshopper、AlphaProof等保留于形式化检索收据，未计为主目录条目。

## 实际查阅路线

以下为实际使用的主要查询与跳转，不把未执行的检索写成已覆盖。

- 广域：`AI mathematics research harness ProofCouncil Albilich QED Danus github`；`AlphaEvolve mathematical discoveries official research FunSearch`。
- 构造来源：`"Mathematical discoveries from program search" arxiv pdf`；`site:github.com google-deepmind funsearch cap_set 512`。从官方发布页取得作者接受稿，再读官方源代码与点集。
- 形式化对照：`site:arxiv.org AlphaGeometry AlphaProof DeepSeek Prover V2 mathematical reasoning`；形式化深读使用的额外查询见[形式化收据](2026-09-20-formal-source-audit.md)。
- 从Albilich的Related Work继续查Aletheia、Rethlas/Archon和LeanDojo；从AlphaEvolve引言及相关方法继续查FunSearch、AlphaTensor。是引用/相关工作扩展，没有运行完整引用索引或前向引文扫描。
- Danus、ProofCouncil的具体原文、版本与工件检索分别见[Danus收据](2026-09-20-danus-source-audit.md)、[ProofCouncil收据](2026-09-20-proof-council-source-audit.md)。

## 候选来源实际阅读范围

|对象|原始来源与读到的位置|能支持什么 / 未做什么|
|---|---|---|
|Danus|系统2607.06447v2、YTD2608.19301v1、固定分支README/角色/配置等，详专门收据|系统与案例分开；未复跑，未接受全部几何证明|
|ProofCouncil|2607.09474v1正文、FirstProof P3提交/三审稿/配置、round-0和round-10|可解释部分结果与迭代；未审计全部题目与全部中间消息|
|Albilich|[2607.27705v1](https://arxiv.org/html/2607.27705v1) Related Work、Proof-State Architecture、实验与CAS消融；[官方仓库入口](https://github.com/uw-math-ai/albilich)|10个内部完成与9个人类匹配+1未闭合不能混写；32% token差异实验根目标均未解决，不能说成功率提高32%|
|QED|[2604.24021v4](https://arxiv.org/html/2604.24021v4) §3失败模式、§4流程、Appendix A.4；[代码入口](https://github.com/proofQED/QED)|18项中5项是作者报告；PDE数学论文尚未深读，作为后续优先项|
|Aletheia|[2602.10177v1](https://arxiv.org/html/2602.10177v1) §1–2与贡献分级|避免把重新发现已知工作计作原创；未查所有相关数学论文|
|Aristotle|系统2510.01346v2，#728论文2601.07421v5、固定Lean文件与工具链|静态核对及命题对应差异；无kernel replay|
|Rethlas/Archon|[2604.03789v1](https://arxiv.org/html/2604.03789v1) §4 Theorem 1及构造/检索/形式化路线|weak quasi-complete反例来源报告；HTML显示的日期信息存在不同层次，未重建版本历史，未查Jensen全部依赖|
|DeepSeek-Prover-V2|[官方README](https://github.com/deepseek-ai/DeepSeek-Prover-V2)、[2504.21801摘要](https://arxiv.org/abs/2504.21801)|模型与benchmark定位；不是具体研究成果深读|
|LeanDojo|[官方README](https://github.com/lean-dojo/LeanDojo)|检索/交互工具定位，原库deprecated提示；未执行或审计v2|
|AlphaGeometry|[官方README的结果与代码模块表](https://github.com/google-deepmind/alphageometry)|25/30及DDAR14/30的评估对象；无开放研究泛化结论|
|FunSearch|论文§1、§2.1、Methods A.1、Supplement A.3/A.5/E.2、代码五模块、notebook和512点列表，详[专门收据](2026-09-20-funsearch-source-audit.md)|有限证书独立检查；原模型/搜索未复跑|
|AlphaEvolve|[2506.13131v1](https://arxiv.org/html/2506.13131v1) §1–2及§3成果入口；[结果仓库](https://github.com/google-deepmind/alphaevolve_results)|架构与复数4×4的48乘法声明；未检验张量分解或全部问题库|
|AlphaTensor|[官方成果库README](https://github.com/google-deepmind/alphatensor)|强化学习/张量分解定位，区分标准数域与模2；未复跑训练|

## 选择依据与证据缺口

Danus展示长期事实依赖，但重大数学声称仍需独立核验；ProofCouncil有公开轮次、提交与外部审稿，能讲清“部分完成”；Aristotle提供非平凡研究问题与形式工件，能展示语义对应问题；FunSearch可用短定义和精确有限证书完整说明搜索/验证区别。四席并不声称是所有候选中最强系统。Albilich与QED仍有后续学习价值；AlphaEvolve需具体工件核查后再深读。

共同缺口包括精确历史模型可用性、完整prompts/失败尝试/人工介入、成本口径、独立复跑和控制变量实验。未知项不根据当前架构补写。未找到项的范围只限已读来源，即NOT-FOUND-IN-CHECKED-SET。

## 文件取得与访问边界

仅FunSearch作者接受稿按阅读需要保存于`references/papers/`（Git忽略），来源、版本说明与SHA-256见专门收据。其余PDF为工具在线阅读，未保存本地副本。FunSearch有限点集保存于`references/data/`并记录哈希；下载数据不执行其中代码。

Nature正文入口发生重定向/访问失败后改用官方开放接受稿；Erdős问题站直接访问失败，时间线依据论文附录。没有绕过认证或挑战页面，没有安装或运行外部harness。仅运行本项目自编有限证书检查及既有统计脚本。

## 旧试点收束

调整前实际产物是3张事件卡、3篇系统档案、3篇案例档案和1篇周报（2026-W35）。据此结束固定四周试点，不补造Week 2–4。旧Astra/Claude档案保留为历史阅读结果，本轮未重核其外部事实；旧Danus档案按新证据更新。此次新增三组事件/系统/案例，Danus一组扩充，候选目录独立于事件统计。

## 验收记录

验收命令、结果与剩余工作在[当前状态](../../STATUS.md)汇总。验收针对文件一致性、来源定位和已声明的有限检查，不代替四篇案例的完整数学证明审查。后续仅在有新问题、版本/工件更新或错误报告时按需重开。

## 同日第二批更正与扩充

首批四组与13候选是历史批次范围，现已扩至九组与18候选，见[第二批收据](2026-09-20-expansion-survey.md)。Albilich的CAS 32%节省不能继续当作已核实效果：固定公开仓库自审列出论文与归档token不匹配、无CAS 9/10缺归档、对照设置不同。以[Albilich新核查](2026-09-20-albilich-expansion.md)和更新后的候选表为准。旧查询记录保留，不把新增阅读倒填为首批已经完成。
