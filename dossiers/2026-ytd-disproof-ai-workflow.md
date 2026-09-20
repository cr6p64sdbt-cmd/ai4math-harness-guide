---
case_id: "case-2026-ytd-disproof-ai-workflow"
title: "YTD 声称证伪：具体数学工作与 Danus 研究过程"
record_updated: "2026-09-20"
event: "events/2026/2026-08-19-ytd-disproof-claim.md"
systems: ["systems/danus.md", "Codex / GPT-5.6-sol", "Claude Code / Fable 5"]
mathematical_status: "OPEN"
workflow_status: "WORKFLOW-DOCUMENTED / CODEX-BRANCH-PUBLIC / HISTORICAL-RUN-NOT-REPRODUCED"
---

# YTD 声称证伪：具体数学工作与 Danus 研究过程

> **版本勘误（2026-09-20）。** 旧档案中的“改进版 Danus 尚未开源”已过期。官方 [`codex` 分支](https://github.com/frenzymath/Danus/tree/6d92e8d415933ca2ef52fd1a4da73fdfcd418f1c)公开，并称其是解决 YTD 的版本；2026-08-23 的 [`bbb4fd6` 提交](https://github.com/frenzymath/Danus/commit/bbb4fd6848ad8d7024494dcf5f7ac6f283cedbb3)称与内部 v3 设计对齐。公开代码没有把论文的原始问题 prompt、运行日志、事实图和模型快照全部绑定到一个历史 commit；故本档案的案例复现状态仍是 **未复现**。

## 分层判断

- **数学结论**：`OPEN`。已确认 arXiv v1 的准确主张，但本项目尚未独立检查其 79 页证明、引用和关键分类链。
- **AI 贡献**：作者提供了显著强于普通 disclosure 的过程报告，包括模型、两个运行阶段、人工转向、运行时间和 fact-graph 统计。
- **工作流复现**：`PUBLIC-CODEX-BRANCH / HISTORICAL-RUN-NOT-REPRODUCED`。改进版实现现已公开；本项目未运行它，也没有取得这次 fresh run 的完整输入与状态。
- **“全 AI”表述**：不采用。第一次运行有关键人工判断；第二次 fresh run 据作者报告无需该提示，但仍有人类给定问题、运行系统、讨论表达、最终润色和承担正确性责任。

## 准确的数学目标

### 读这个结果所需的最低背景

一对极化簇 $(X,A)$ 是复射影代数簇 $X$ 加上一条 ample 线丛 $A$。直观上，$A$ 指定研究哪一个 Kähler 类，也固定了代数几何中衡量退化的尺度；同一个 $X$ 换一条极化线丛，问题就可能变。cscK metric 是该类中标量曲率为常数的 Kähler 度量。它的存在是解析命题，不能只检查一个有限参数表。

test configuration 是把 $(X,A^e)$ 放进以一条复直线为参数的代数退化族：非零参数处仍是原对象，中心纤维可以不同，同时带有一参数群作用。Donaldson–Futaki invariant 为这种退化赋一个数。本文所用 K-polystability 要求：**每个正整数 $e$、每个正规 ample 代数 test configuration** 的 invariant 非负；若等于零，退化须是文中允许的 polarized product。因而“检查一批自然想到的退化都没问题”远不够；还要覆盖任意退化，并单独解决等号情形。[Conjecture 1.1、Definition 2.2、Theorem A/B](https://arxiv.org/html/2608.19301v1)

要以此反驳“K-polystable 则存在 cscK”这一方向，作者须同时履行两项证明义务：一是上述**全称的代数稳定性**，二是这个极化类中**不存在** cscK 度量。论文实际上证明更强的解析否定：连 extremal Kähler metric 也不存在。下面的巨大整数是构造特定线丛和边界多项式的数据，不是可忽略的装饰。[Theorem A、§1.3–1.4](https://arxiv.org/html/2608.19301v1)

预印本的准确对象是四条复光滑射影曲线 `C_0,\ldots,C_3` 的乘积 `B` 上的射影线丛。令 `M=\boxtimes_i M_i`、`L=\boxtimes_i L_i`，在**商空间约定**下取

```math
X=\mathbb P_B(\mathcal O_B\oplus L),\qquad
A=\mathcal O_X(1)\otimes\pi^*M.
```

论文 Theorem A 指定曲线亏格为 `(3846511,10591,76,46)`，`M_i` 的度数为 `(461999,13962,1068,260)`，`L_i` 的度数为 `(13397971,-11635,-712,-104)`，并要求不同曲线 Jacobian 之间的 `\operatorname{Hom}(\operatorname{Pic}^0(C_i),\operatorname{Pic}^0(C_j))=0`（`i\ne j`）。这些不是“任选四条曲线”或连续自由参数；来源见 [Theorem A 与 Construction 3.7](https://arxiv.org/html/2608.19301v1)。预印本声称：

1. $X$ 光滑、$A$ ample，且 $\operatorname{Aut}^{0}(X)=\mathbb C^{*}$；
2. 对**每个正整数 exponent `e`**，每个以 `(X,A^e)` 为一般纤维的**正规、ample 的代数 test configuration**，其 Donaldson–Futaki invariant 非负；零值仅是纤维伸缩的整一参数子群与极化 scalar character 给出的 polarized product。这是文中所用 K-polystability 的精确类目；
3. `c_1(A)` 中没有 extremal Kähler metric，因此没有 cscK metric；
4. 因而 Conjecture 1.1 所写的“一般光滑极化复射影簇，K-polystability 等价于 cscK 存在”的方向受到反例挑战。

上述为**作者的定理声明**，非本项目验收。本文不把 Fano、uniform 或 completed K-stability 版本与 Conjecture 1.1 合并。后续数学审计须逐个检查原文 §3、§5–7 的关键接口。[Conjecture 1.1、Theorem A、§7](https://arxiv.org/html/2608.19301v1)

## 研究时间线

### 阶段A：开放问题探索

作者报告在用 Claude Code 探索多个开放问题时发现了可能突破的初步迹象。

### 阶段B：三个系统协作

Claude Code（Fable 5）、Codex（GPT-5.6-sol）和 Danus 协作寻找反例和证明。作者在一个关键节点判断：已构造的例子可能反驳 Codogni–Stoppa 猜想或 cscK YTD 猜想，并要求 agents 集中判断究竟哪个命题失败。

作者把这次人工判断称为关键输入。这意味着第一阶段不能描述成完全无人干预的自主发现。

### 阶段C：改进版Danus从原问题重新运行

为了判断 AI 实际贡献，团队把原始问题重新交给一个改进版 Danus，不提供先前发现。论文报告该系统在运行 5 小时 29 分钟后得到反例和一份完整证明，并且比第一次协作更快。

这是重要的归因证据，但仍是同一团队的内部复跑；没有已检查的冻结代码、日志和第三方复现，因此等级是 `WORKFLOW-DOCUMENTED` 而非 `REPRODUCIBLE`。

### 阶段D：写作与检查

正文经过作者与 Danus 多轮讨论以改善表达，论文称这些讨论没有改变数学内容；最后由人类进行润色和检查。作者在正文中承担最终正确性责任。

## 系统配置

### 首次协作运行

- named systems：Claude Code / Fable 5、Codex / GPT-5.6-sol、Danus；
- Danus component：8 个 Rethlas workers，其中 4 个 `xhigh`、4 个 `high`；
- final fact graph：616 个 verifier-gated facts；
- global memory：353 conclusions、143 obstacles、96 directions、33 proof attempts、26 plans、17 counterexamples、2 dead ends；
- verification records：924；
- 进入最终主定理 dependency closure 的 facts：88，占 14%；其余 528 个未用于论文主链；
- 88 个 closure facts 中，论文报告 6 个来自文献重述，82 个由 swarm 证明。

这些数字说明搜索远宽于最终证明，但不能单独证明 verifier 正确或 AI 贡献具有因果独立性。

### 改进版Danus独立重跑

- main agent：Codex-based implementation，GPT-5.6-sol；
- proof workers：Rethlas workers 改用 GPT-5.6-sol；fresh run 的 proof-worker 总数未在已读附录中明确；
- exploratory subagents：main agent 调度 Codex subagents 作高层探索，本案例为 3 个；其输出不能与 verifier-gated proof-worker facts 等同；
- API：作者称 whole system 使用单一 API；
- strategy：移除 GPT-5.5 Pro consultation，main agent 直接做数学和全局策略；
- changes：强化全局 strategy reflection，并把 fact granularity 调整为更长、更复杂的局部结果；
- runtime：作者报告 5 小时 29 分钟；
- release：附录脚注写“即将开放”；截至 2026-09-20 官方 `codex` 分支已可读，但没有论文运行的精确代码与日志快照。

### 作者执行的基线对照

作者还报告把原始问题交给 QED、ProofCouncil、MechMath、直接 Codex、Claude Code 和 GPT-5.6-sol Pro。按论文设置，前几类系统在 12 小时内没有给出完整解；直接 Codex 生成后自行否决了一份证明。即使给定反例、只要求验证，也没有系统在相同时间限制内完成。

这些是作者执行的对比，不是独立 benchmark；预算等价性、prompt 细节和环境控制尚不足以支持强因果结论。

## AI完成的工作

按作者报告，可归给 AI systems 的内容包括：

- 在开放问题探索中发现候选方向；
- 构造具体五维簇候选；
- 搜索和组织证明该候选满足稳定性与分析性质所需的长链条；
- 通过 workers 提交大量局部 facts，并在 verifier 反馈下修复；
- 在 fresh run 中从原始问题重新得到反例和完整证明；
- 把 fact graph 转写为论文，并参与改善表达。

这里的“完整证明”仍是论文作者对系统产出的描述；本项目未把它升级为独立成立的数学证明。

## 人的参与

- 选择开放问题和初始探索环境；
- 识别候选可能击中两个不同猜想，并在第一次运行中作关键战略聚焦；
- 启动并配置系统，决定进行 fresh rerun；
- 与 Danus 讨论论文表达；
- 最终润色、检查并承担论文正确性责任；
- 决定公开哪些方法、统计和系统信息。

第二次运行减少了数学提示，但没有消除问题设定、实验控制、发布和最终责任中的人类角色。

## 研究机制重建

下图按附录叙述顺序标出事件，同时把**原始协作的结果**与**后续归因复测**区分开；并非逐分钟运行日志。正文没有公布每个事实或改道的准确时间。

```text
原始问题 → 广泛探索 → 人识别关键分叉 → 三系统集中研究
         → 局部提交、LLM 验证、修复 → 事实图与改道 → 原始协作的主结果
                                                       ↓
归因复测：只给原题、不给上述发现 → improved Danus fresh run
                                      → 作者报告 5 小时 29 分钟重得结果
                                                       ↓
正文经作者与 Danus 讨论表达 → 最终人工润色和检查

注意：归因复测是另一次运行，其事实与统计不能拼入原始协作的事实图。
```

可研究的机制是并行路线、verified-fact 与 unverified-memory 分离、依赖图、fresh verifier、全局反思、级联撤销和成稿后二次验证；它们如何影响有效研究时长，现有案例没有提供受控归因。

## 复现条件核查

### 已公开材料

- YTD arXiv v1 及 Appendix A；
- Danus 架构论文 v2；
- Danus 公开仓库和基础运行说明；
- 第一阶段和 fresh run 的部分模型、worker、时间与统计信息。

### 独立重跑仍缺少的材料

- 论文历史运行所用的冻结 commit 与运行环境；公开 `codex` 分支当前 HEAD 是 6d92e8d415933ca2ef52fd1a4da73fdfcd418f1c，不能倒推为当时快照；
- 原始 problem prompt、系统 prompt、角色 skills 和完整参数；
- fresh run 的 fact graph、global/local memory 与完整日志；
- 原始协作运行报告的 924 条 verification records 所对应的逐条工件与日志；
- API snapshot、模型确定性信息、费用和计算资源；
- 独立团队使用相同输入和版本的复跑。

结论：`PUBLIC-RELATED-IMPLEMENTATION / PARTIAL PROCESS DISCLOSURE / NO INDEPENDENT REPRODUCTION YET`。

## 数学证据核查

当前只完成以下层级：

- 已确认准确 arXiv 版本、主命题和 AI 附录；
- 已确认作者给出的 case/process 统计；
- 尚未 faithful-transcribe 关键定理和证明；
- 尚未逐项核对 K-polystability 分类链、nonexistence 链及引用适用性；
- 尚未确认独立专家审查、正式同行评审或形式证书。

因此数学状态保持 `OPEN`，不采用标题式 `DISPROVED` 作为本项目判定。

## 可学习的方法

可以保存并未来分别试验的假设包括：

1. 长证明需要结构化事实依赖，而不只是扩大上下文；
2. 证明路线和反例路线应并行，而不是过早锁定猜想真假；
3. verifier 应与生成上下文分离，并能读取明确依赖；
4. 失败、障碍和未验证策略应保留，但不能进入 truth store；
5. 定期全局反思可能比固定 plan 更适合长程搜索；
6. 论文写作需要独立于 fact-level verification 的第二检查层。

不能据此推出“安装 Danus 就会提高本项目研究能力”。该案例同时改变了基础模型、orchestration、并行计算预算、事实粒度和人类介入，没有受控消融。

## 未解决问题与更新条件

- arXiv 发布 v2 或勘误；
- 若发布 YTD run 的精确 commit、原始 prompt、日志或 fact graph，更新历史运行绑定；
- 独立数学家发布逐项验证、反例或批评；
- 论文进入正式同行评审或发表；
- 第三方在冻结版本上复现 fresh run；
- 作者公布完整成本和对比实验协议。

## 原始来源

- [YTD arXiv:2608.19301v1](https://arxiv.org/html/2608.19301v1)，Conjecture 1.1、Theorems A–C、§3–7、Appendix A；复查于 2026-09-20。
- [Danus system paper arXiv:2607.06447v2](https://arxiv.org/html/2607.06447v2)，§2.1–2.7；复查于 2026-09-20。
- [Danus official `codex` branch at 6d92e8d](https://github.com/frenzymath/Danus/tree/6d92e8d415933ca2ef52fd1a4da73fdfcd418f1c)，复查于 2026-09-20。

## 为什么构造候选不等于证伪

前人的 [ACG+08 工作在原文 §1.3 的定位](https://arxiv.org/html/2608.19301v1) 已给出类似射影丛机制：其 extremal polynomial 在有理点正，却在一个无理内点有重零点。这样的候选暗示解析度量可能不存在，但 **K-polystability 的量词遍及所有正规 ample 代数 test configurations**；只验两个零/无穷截面的 Ross–Thomas 退化不能完成这一量词。这正是作者在 [附录 A](https://arxiv.org/html/2608.19301v1) 把本例称为“需证明的反例”而非有限计算证书的原因。

本篇把基底改成四条曲线的乘积，得到五维 `X`。正文 §1.3 称第四个因子及曲线 Jacobian 间的 Hom 消失为任意代数退化的刚性和乘法结构提供条件。附录 A 表 3 报告：较简单的一、二、三曲线候选家族被排除，四因子形状由此确定。这里能核对的是**论文叙述和最终对象**；原始实验日志未公布，不能逐轮确认每一排除结果何时影响选型。[Theorem A、§1.3、附录 A 表 3](https://arxiv.org/html/2608.19301v1)

### 正文证明结构：两个方向加一个等号关口

1. **解析不存在。** Construction 3.7 构造 `(X,A)`，Proposition 3.8 处理光滑性、ampleness 和 `\operatorname{Aut}^0(X)`。Lemma 3.19 给出极值多项式
   `F_{x^*}(z)=\frac{45}{3472}(1-z^2)(z^2-4z-1)^2`，其内点重根 `z_0=2-\sqrt5` 无理。Proposition 3.13 的证明再把该内点零值与非零纤维圆作用生成向量场的正定度量范数冲突起来，推出没有 extremal metric。多项式的形式是**论文给出的精确代数桥**；本项目未独立重做 `p_c,q_c` 的系数计算或解析定理适用性。[Lemma 3.19、Proposition 3.13](https://arxiv.org/html/2608.19301v1)
2. **全体配置非负。** Proposition 3.12 先给出标量曲率与平均值之 $L^2$ 距离趋零的一列 Kähler 度量；Proposition 5.3 将它们缩放到每个 $c_1(A^e)$，再分别用 Theorem 5.1 的 Donaldson 型标量曲率下界和 Theorem 5.2 的零范数配置结论，推出对**所有**正规 ample test configurations 有 $\operatorname{DF}\geq0$。这一链条依赖被引分析定理的适用条件，本项目尚未逐项核对。[§4–5，Proposition 5.3](https://arxiv.org/html/2608.19301v1)
3. **零值必须是 product。** §1.4 说明这是最难的新增部分。Theorem B 称若 `\operatorname{DF}=0`，那么每个 `V_{em,j}=H^0(B,M^{em}\otimes L^j)` 块的滤过只有单一跳跃 `\alpha m+\beta j`，其中 `\alpha,\beta` 为整数；故配置由纤维伸缩和 scalar character 产生。§6 讨论 normal section algebra、marked rigidity、residual filtrations 和 oriented Smith spectrum。§7 把 Proposition 5.3、Theorem B 与 Proposition 3.13 接合为 Theorem A。[Theorem B、§6–7](https://arxiv.org/html/2608.19301v1)

**一个可追踪的研究步骤。** 候选 `(X,A)` 的边界多项式有无理内点重根，这为“解析上不可实现”提供了可定位信号；但假若只证明某几类代数配置 `\operatorname{DF}>0`，仍存在其他配置破坏 K-polystability 的逻辑空隙。论文的路线是将任意配置转成滤过，再用正反 initial filtrations 的仿射性和零值刚性将其逼到 product 情形。附录 A 把最终 88 个事实中的 20 个归入 Veronese/ray、14 个归入 scalar profile、10 个归入 Newton–Okounkov transform、10 个归入 Duistermaat–Heckman 结构、7 个归入 comparator/Smith spectrum；这支持“系统内部确曾分工处理该链条”的作者报告，**不提供每个 fact 的原始文本或独立证明审计**。[§4–7、附录 A 表 2](https://arxiv.org/html/2608.19301v1)

## 从运行记录学到什么，哪些只是待试假设

| 实际报告的做法 | 解决的问题与适用前提 | 风险、效果证据和待检验点 |
|---|---|---|
| 首轮并行证明、反例与人类聚焦 | 在两个可能受挑战的猜想间继续判别；人能识别关键数学分叉 | 作者明确称人工转向关键；不能记作完全自主。 |
| fresh improved-Danus 从原题重跑 | 测试先前人工提示是否为必要条件 | 作者报告 5 小时 29 分钟完成；同团队内部复跑，缺输入、日志和独立复现。 |
| 事实依赖闭包与废弃路线并存 | 让大范围探索不污染最终证明 | 616 个事实中 88 个入闭包；其余包含 64 个放弃的 torus-specialization 路线、58 个前件未消去的条件性结果、56 个指出错误步骤的事实、24 个排除候选家族的事实。数量不等于真实性或因果收益。[附录 A 表 1–3](https://arxiv.org/html/2608.19301v1) |
| Danus 通用写作流程设有整篇 LLM 复核；YTD 附录确认作者与 Danus 讨论表达、最终人类检查 | 处理事实图到论文的拼接错误 | YTD 本次的逐项与整篇 verifier transcript 均未公开，不能从通用设计推出实际检查明细。 |

注意首轮的 **8 个 Rethlas workers、616 个事实和 924 条验证记录**属于原始三系统协作；fresh run 附录只明确 **3 个 Codex 探索性 subagents**、新主 agent 设计和 5 小时 29 分钟。不能把首轮统计搬到 fresh run。[附录 A](https://arxiv.org/html/2608.19301v1)

本项目阅读深度为 **section-summary 加承重位置定位**。已读 Theorem A/B、Construction 3.7、Lemma 3.19、Proposition 3.13 的结尾、§7 汇总和附录 A；尚未逐行验算 §4–6 的普遍配置分类、核对外部定理的原文假设，也未做 PDF faithful excerpt 或独立专家审查。因此 `OPEN` 保持不变。具体来源与版本记录见 [Danus 来源审计](../references/notes/2026-09-20-danus-source-audit.md)。
