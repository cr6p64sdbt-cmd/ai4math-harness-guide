---
case_id: "2026-albilich-kourovka-21-142"
title: "Albilich 与 Kourovka 21.142：不变生成群的嵌入反例声称"
record_updated: "2026-09-20"
event: "events/2026/2026-08-01-albilich-kourovka-21-142.md"
systems: ["albilich"]
mathematical_status: "UNASSESSED"
workflow_status: "WORKFLOW-DOCUMENTED / CURATED-ARTIFACTS-READ / HISTORICAL-RUN-NOT-REPLAYED"
---

# Albilich 案例：Kourovka 21.142 的群论反例

## 先给分层判断

**数学成果的作者声明**：对每一对互异素数 $p,q$，足够大的交错群 $A_n$ 不能嵌入任何由阶为 $p,q$ 的两个元素*不变生成*的有限群。这否定 Kourovka Notebook 21.142 的全称嵌入问题；正式陈述见作者数学论文 [arXiv:2608.00703v1，Theorem 1.1 / 4.1](https://arxiv.org/html/2608.00703v1#S4)。

**本项目判断**：`UNASSESSED`，意为读到作者的非形式化证明及系统归档，但尚未逐项验证高秩经典群、外自同构、CFSG 和 Collins 定理的假设接口，也没有独立同行评审或形式化证书可据此接收整个结果。它不是“学界仍无此声称”，也不是对作者定理的否定。Albilich 的内部 `solved_final`、作者修订过的数学论文和本项目的独立验收三者分开。[系统论文 §4.3/§5](https://arxiv.org/html/2607.27705v1#S4)、[数学论文 AI 声明](https://arxiv.org/html/2608.00703v1#S1)。

**AI 贡献与人类贡献**：作者说 Albilich 参与了论证形成，公开了问题输入、一次运行的内部证明报告、精选 research/advisor/verifier/CAS 工件；数学论文明确说全部陈述和证明由作者检查、修订，作者承担责任。公开材料不足以给最终论文的每个引理分配“AI 首次发现”或“人首次修复”的细粒度比例。[数学论文 §1 的 Statement on the use of AI](https://arxiv.org/html/2608.00703v1#S1)、[固定实验目录](https://github.com/uw-math-ai/albilich/tree/36c648cb3bc8d550fbe5c4035f177ef4c0a5f1c7/experiments/kourovka/21.142)。

## 数学对象、原问题、命题量词

交错群 $A_n$ 由 $n$ 个符号上的偶置换组成，$n\ge5$ 时是非交换单群。两元素 $a,b\in G$ 的**不变生成**要求

\[
    \langle a^g,b^h\rangle=G\quad\text{对任意 }g,h\in G.
\]

比普通的 \(\langle a,b\rangle=G\) 强，因为允许两者**独立**共轭。一个直接的反证判据是：只要能把 $a,b$ 各自共轭到同一个真子群 $D<G$，它们就不能不变生成。正式论文将此写为 Lemma 2.2。[数学论文 Definition 2.1、Lemma 2.2](https://arxiv.org/html/2608.00703v1#S2)。

原问题（P. A. Zalesskii 提出）固定**互异素数** $p,q$，问是否每个有限群都可嵌入某个有限群 $G$，且 $G$ 能由一个阶恰为 $p$ 的元素与一个阶恰为 $q$ 的元素不变生成。量词是

\[
 \forall p\ne q\text{ 素数}\;\forall K\text{ 有限群}\;
 \exists G\text{ 满足所述不变生成条件且 }K\hookrightarrow G.
\]

作者答案为否：

\[
 \forall p\ne q\text{ 素数}\;\exists N(p,q)\;\forall n\ge N(p,q)\;
 \forall G\text{ 有限群}:\quad
 \bigl(G\text{ 满足上述生成条件}\bigr)\Longrightarrow A_n\not\hookrightarrow G.
\]

这是一族**依赖 $p,q$ 的存在性反例**，不是为每一对素数给出了最小的 $n$，也不是声称 $A_n$ 自身不能由任何两个素阶元素生成。[数学论文摘要、Theorem 1.1、Remark 3.15、Theorem 4.1](https://arxiv.org/html/2608.00703v1)。

## 两份结果工件为什么必须区分

|层次|实际命题与路线|可核查出处|项目判断|
|---|---|---|
|2026-07-14 内部运行|报告声称找到 $A_m$ 的反例；取**最小嵌入宿主**，化到 $S^t\le G\le\operatorname{Aut}(S)\wr\operatorname{Sym}(t)$；按简单群家族排除；末步将两生成元独立共轭进共同真子群|[固定 `problem.md`](https://github.com/uw-math-ai/albilich/blob/36c648cb3bc8d550fbe5c4035f177ef4c0a5f1c7/experiments/kourovka/21.142/problem.md)、[`report.md` Final Proof](https://github.com/uw-math-ai/albilich/blob/36c648cb3bc8d550fbe5c4035f177ef4c0a5f1c7/experiments/kourovka/21.142/report.md)|有作者精选工件及 LLM 内部核验；不是独立证明验收|
|2026-08-01 数学论文|最终稿改用**组合因子/截面**路线：若 $A_{n_0}\le H$，其简单组合因子必出现在 $H$ 某组合因子的一个截面中；证明不变生成的 $H$ 不可能有足够大交错截面的简单组合因子|[arXiv:2608.00703v1，Lemmas 2.5、3.13，Prop. 3.14，Thm. 4.1](https://arxiv.org/html/2608.00703v1)|作者明确检查、修订全文；不能把它说成内部运行原样生成|

这里的“截面”是 $U/V$，其中 $V\triangleleft U\le S$；“组合因子”是把群沿正规子群链拆解得到的简单商群。正式论文用这两个概念避免只盯着一个最小宿主。其主要中间结论是：对于固定 $p,q$，存在 $B(p,q)$，若 $S^t\le G\le\operatorname{Aut}(S)\wr\operatorname{Sym}(t)$ 仍被阶 $p,q$ 元素不变生成，则 $S$ 不可能有 $A_n$（$n>B(p,q)$）作为截面。[数学论文 Proposition 3.14](https://arxiv.org/html/2608.00703v1#S3)。

最终论文的证明结构可按依赖读：先用 Lemma 3.1 将单群的共同真子群提升到 wreath product；Proposition 3.3 处理大交错群；Proposition 3.12 处理高秩经典群；Lemma 3.13 用有限单群分类将残余家族转为有界射影表示维数；Proposition 3.14 引 Collins 的 Theorem A 控制可能出现的交错截面；Theorem 4.1 再由组合因子传递得到嵌入矛盾。[数学论文 §§2–4](https://arxiv.org/html/2608.00703v1)。我们只重建了该逻辑地图，尚未完成各引用的证明级适用性审查。

## 可追溯的运行过程

固定实验目录保留了 [问题文件](https://github.com/uw-math-ai/albilich/blob/36c648cb3bc8d550fbe5c4035f177ef4c0a5f1c7/experiments/kourovka/21.142/problem.md)、[运行摘要](https://github.com/uw-math-ai/albilich/blob/36c648cb3bc8d550fbe5c4035f177ef4c0a5f1c7/experiments/kourovka/21.142/README.md)、[内部报告](https://github.com/uw-math-ai/albilich/blob/36c648cb3bc8d550fbe5c4035f177ef4c0a5f1c7/experiments/kourovka/21.142/report.md)、[metrics](https://github.com/uw-math-ai/albilich/blob/36c648cb3bc8d550fbe5c4035f177ef4c0a5f1c7/experiments/kourovka/21.142/metrics.json)、[精选证据目录](https://github.com/uw-math-ai/albilich/tree/36c648cb3bc8d550fbe5c4035f177ef4c0a5f1c7/experiments/kourovka/21.142/evidence)及 [SHA256SUMS](https://github.com/uw-math-ai/albilich/blob/36c648cb3bc8d550fbe5c4035f177ef4c0a5f1c7/experiments/kourovka/21.142/SHA256SUMS)。项目只读，未运行仓库代码、未重放 SQLite。

|时序上能确认的阶段|公开工件中可看到什么|不应额外推断什么|
|---|---|---|
|输入|给出 21.142 的定义、精确问句，允许有条件地引外文献与有限计算|不能推断人类在运行中所有提示或实时 steering|
|分解与换路|证据目录留有 PSL、PSp、PSU、正交、交错群、终端 CFSG 相关证明及 verifier 文件，也有 advisor 针对瓶颈的建议；若干反例构造失败记录|这些是精选工件，不能重建 80 次 child session 的全部时间线|
|组装根证明|最小宿主引理和终端单因子引理先内部验收，advisor 文件建议把它们连成根路线；根验证文件检查最终矛盾的量词与前提|根一步正确不代表每个前置深层群论引理都经独立验证|
|运行结束|`metrics.json`：`gpt-5.6-sol`、`xhigh`、80 child runs、5h51m 生命周期、6h48m backend compute、29,684,464 gross tokens（含缓存输入），revision 156、`solved_final`|两种时间口径不能互换；token 不是美元账单；不能用 7 月运行配置解释 9 月仓库当前默认模型|

论文 §4.3 和固定 `README.md` 报告 11 个 claim 中 10 个被内部验收；一条根路线被集成。`report.md` 顶部同时记录“active debts 14 total, 14 blocking (ledger only)”，其 Final Proof 只依赖两个已验前提和根步。**这些残留债务与根路线的依赖关系没有由本项目重放数据库核对**，因此不能仅凭两个计数说整篇证明已闭合或未闭合。[归档 `report.md` 的头部、Final Proof 与 Active Proof Debts](https://github.com/uw-math-ai/albilich/blob/36c648cb3bc8d550fbe5c4035f177ef4c0a5f1c7/experiments/kourovka/21.142/report.md)。

### 一个可核查的关键步骤

公开 [最小宿主证明工件 `rev107`](https://github.com/uw-math-ai/albilich/blob/36c648cb3bc8d550fbe5c4035f177ef4c0a5f1c7/experiments/kourovka/21.142/evidence/proof_minimal_host_monolithic_wreath_reduction_rev107.md) 的输入是“若 $A_m$ 真能嵌入某个这样的 $G$，从所有宿主中取阶最小者”。候选推理：若某非平凡正规子群 $K\lhd G$ 与 $A_m$ 交平凡，则 $A_m$ 仍注入 $G/K$，不变生成传到该商群，两素数阶生成元的像也不得变成单位元（否则商群由一个元素生成而是循环群），得到更小宿主矛盾。由此 $A_m$ 包含于每个非平凡正规子群，继而得唯一非交换极小正规子群 $S^t$，并有某坐标上的 $A_m\hookrightarrow S$。[局部 verifier `rev109`](https://github.com/uw-math-ai/albilich/blob/36c648cb3bc8d550fbe5c4035f177ef4c0a5f1c7/experiments/kourovka/21.142/evidence/verification_minimal_host_monolithic_wreath_reduction_rev109.md)给出内部 `correct_no_gaps`，还特别说该验收**不覆盖**后续经典群家族模块。

接着 [终端引理候选 `rev128`](https://github.com/uw-math-ai/albilich/blob/36c648cb3bc8d550fbe5c4035f177ef4c0a5f1c7/experiments/kourovka/21.142/evidence/proof_terminal_cfsg_projective_degree_root_rev128.md) 调用有限单群分类、交错群最低射影表示维数及各经典群共同真子群模块。[局部验收 `rev130`](https://github.com/uw-math-ai/albilich/blob/36c648cb3bc8d550fbe5c4035f177ef4c0a5f1c7/experiments/kourovka/21.142/evidence/verification_terminal_simple_factor_exclusion_rev130.md)称其 `correct_no_gaps`。[advisor 根路线交接 `rev136`](https://github.com/uw-math-ai/albilich/blob/36c648cb3bc8d550fbe5c4035f177ef4c0a5f1c7/experiments/kourovka/21.142/evidence/advisor_root_spine_verifier_handoff_rev136.md)建议将两个前提接成根证明，[根 verifier `rev149`](https://github.com/uw-math-ai/albilich/blob/36c648cb3bc8d550fbe5c4035f177ef4c0a5f1c7/experiments/kourovka/21.142/evidence/verification_root_counterexample_cfsg_terminal_rev149.md)核最后一步。这是**来源支持的“输入→候选→内部检查→集成”链**；原始对话、完整失败顺序和人类运行中干预没有在该目录公开。

## AI 与人的分工

|行为|可确认的贡献|还不知道什么|
|---|---|---|
|AI 研究与策略|归档有 researcher、advisor、source-adaptation、CAS 与 verifier 各类工件；最终内部报告给出完整反例路线|每个具体引理最初由谁提出，以及人是否在关键时刻改过提示|
|AI 检查|局部与根级 verifier 文件可读；证据链记录哪一个工件承接哪个命题|这些是内部非形式化审稿，并非 formal kernel 或独立领域审稿|
|人类选题与修订|作者选择 Kourovka 问题、提供问题文件；最终数学论文明确声明作者检查、修订全部陈述和证明并负责|最终论文修改对应哪个具体 agent 轮次、每处修订的原因，未公开完整对照日志|

公开归档的 21.142 advisor 消融是一对单次比较：有 advisor 的分支在 80 个 child runs 后达到内部根完成；无 advisor 的新 proof state 有 110 runs、18 个已验 claims、16 条集成路线，却在操作员停止时没有根结论，且其预算只运行到预定的两倍上限之前。这支持“整体方向与组装可能重要”的**个案解释**，不支持“advisor 一般提高成功率”或“无 advisor 绝不会解决”。[系统论文 Table 5 与解释](https://arxiv.org/html/2607.27705v1#S4)、[固定实验 README](https://github.com/uw-math-ai/albilich/blob/36c648cb3bc8d550fbe5c4035f177ef4c0a5f1c7/experiments/kourovka/21.142/README.md)。

## 验证、复现与局限

|主张|来源定位|实际检查|未闭合处|本项目状态|
|---|---|---|---|---|
|不变生成的真子群判据与末步矛盾|数学论文 Lemma 2.2、Thm. 4.1；运行报告 Final Proof|本项目核了定义与末步使用的量词接口|依赖的终端引理尚未独立核|局部逻辑已重建，整体 `UNASSESSED`|
|最小宿主归约|运行 `proof_...rev107`、`verification_...rev109`|读了证明与内部反馈|没有用独立第二条论证审完所有技术细节|`PRIMARY-SOURCE-CHECKED`|
|经典群/有限单群的完整覆盖|数学论文 Props. 3.3、3.12、Lemma 3.13、Prop. 3.14；归档 `rev128/130`|已定位各承重接口|未核原始 Collins Theorem A、CFSG 与外自同构引用的准确适用条件；未逐项复核所有小秩和域特征分支|`UNASSESSED`|
|AI 历史运行本身复现|实验归档问题、report、metrics、精选 evidence 与哈希清单|静态读取，确认文件结构与指标口径|缺原始 child 日志、SQLite、精确运行代码 commit；未执行系统|`WORKFLOW-DOCUMENTED`，非 replay|
|最终论文与运行相同|两份原始文本|对照发现数学路线已经改变|无法按缺失的逐轮修订日志精确分配人/AI贡献|**不能当作相同工件**|

此案例对平面 ODE 没有直接数学结论；值得学习的是“证明债务如何挂到承重接口”“局部验收后如何再核全局量词”“上游修订如何影响整篇”，而不是把有限群论中的具体引理搬入 ODE 项目。系统机制见 [Albilich 档案](../systems/albilich.md)，版本/来源差异见 [本批收据](../references/notes/2026-09-20-albilich-expansion.md)。
