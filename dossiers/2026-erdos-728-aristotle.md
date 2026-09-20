---
case_id: "2026-erdos-728-aristotle"
title: "Erdős #728：GPT-5.2 Pro 提出论证、Aristotle 生成 Lean 证明"
record_updated: "2026-09-20"
event: "events/2026/2026-01-26-erdos-728-aristotle.md"
systems: ["aristotle-harmonic", "gpt-5.2-pro"]
mathematical_status: "UNASSESSED"
workflow_status: "WORKFLOW-DOCUMENTED / ORIGINAL-RUN-NOT-REPRODUCIBLE"
---

# Erdős #728：从自然语言数论思路到 Lean 证书

> 本案例选作**有新数学问题、明确 AI 分工、公开 Lean 源码**的形式化路线样本。`UNASSESSED` 表示本项目尚未完成论文完整 Theorem 1 的数学与形式化对应验收；它不对学界目前是否已解决 #728 下结论，也不暗示结果错误。公开源码包含可检查的非平凡定理；本项目未执行 Lean，且顶层声明与论文最强命题之间有具体差异。系统机制见 [Aristotle 档案](../systems/aristotle-harmonic.md)，检索收据见 [来源审计](../references/notes/2026-09-20-formal-source-audit.md)。

## 数学对象与问题

设自然数 $a,b,n$，记 $k=a+b-n$。问题关心阶乘整除
\[
a!b!\mid n!k!
\]
可以在 $k$ 多大时成立。没有对 $a,b$ 位置的限制，问题存在容易的极端例子；读研究版本时须要求它们在 $n$ 的固定正比例区间内，并要求 $k$ 处于对数窗口。论文 [Introduction, pp.1–2](https://arxiv.org/pdf/2601.07421v5)解释了原网页措辞的歧义。案例过程先解决较弱版本，论坛讨论后再加强，因此不能把 1 月 4 日的首次输出直接算成最终目标。

论文 [Theorem 1, p.2](https://arxiv.org/pdf/2601.07421v5)的精确结果是：任给 $0<C_1<C_2$ 与 $0<\varepsilon<1/2$，有**无限多个** $(a,b,n)\in\mathbb N^3$，满足
\[
\varepsilon n\le a,b\le(1-\varepsilon)n,\qquad
a!b!\mid n!(a+b-n)!,\qquad
C_1\log n<a+b-n<C_2\log n.
\]
这比“某一组存在”强，也比“$k>C_1\log n$，没有上界”强。原文的对数是自然对数；$\varepsilon$、$C_1$、$C_2$ 是先固定再取无限多三元组。论文证明还构造了 $n=2m,b=m,a=m+k$，所以 $a,b$ 接近 $n/2$。[§3, p.4；§5, p.10](https://arxiv.org/pdf/2601.07421v5)

## 结果为什么有内容：一条可重建的证明骨架

取 $n=2m,b=m,a=m+k$ 后，整除化为
\[
\binom{m+k}{k}\mid\binom{2m}{m}.
\]
对每个素数 $p$ 比较两边的 $p$-进赋值。定义 $\kappa_p(m)=\nu_p\binom{2m}{m}$、$W_p(m,k)=\nu_p\prod_{i=1}^k(m+i)$、$V_p(m,k)=\max_{1\le i\le k}\nu_p(m+i)$。论文 Lemmas 1–4（pp.4–5）将证明压到 $V_p(m,k)\le\kappa_p(m)$：$W_p(m,k)\le\nu_p(k!)+V_p(m,k)$，而 $\nu_p\binom{m+k}{k}=W_p(m,k)-\nu_p(k!)$。Kummer 定理把 $\kappa_p(m)$ 解释为 $m+m$ 在 $p$ 进制中的进位数。[论文 §3](https://arxiv.org/pdf/2601.07421v5)

这产生两个不同的任务。若 $p>2k$，一项 $m+i$ 被 $p^J$ 整除时，$m$ 的低 $J$ 位足以迫使加倍时至少 $J$ 次进位；论文 Lemma 5（p.6）给出这部分。若 $p\le 2k$，寻找同一个 $m\in[M,2M]$，使它在每个相关进制中有足够多的“大数字位”以产生进位，同时避免区间 $m+1,\ldots,m+k$ 出现特别高的 $p$ 幂因子。这是该结果最值得学的“结构化搜索条件”：把不可直接搜索的无限整除问题变成有限区间上的**好进位**与**无尖峰**条件。[论文 §4.1–4.2.1, pp.6–7](https://arxiv.org/pdf/2601.07421v5)

关键非数值步骤是论文 [Lemmas 11–14, pp.8–10](https://arxiv.org/pdf/2601.07421v5)：对每个小素数分别上界“进位太少”和“高素数幂尖峰”两类坏 $m$ 的数量，再对素数并合；当 $k=\lfloor c\log M\rfloor$ 且 $M$ 足够大，坏集合大小严格小于 $[M,2M]$ 中的 $M+1$ 个整数，故好 $m$ 存在。取 $C_1<c<C_2$ 并令 $M$ 无界，原文在 §5 得出双侧窗口内的无限多个三元组。图 1 的数值图仅帮助观察，**不承担**坏集合上界证明。[论文 §5, p.10](https://arxiv.org/pdf/2601.07421v5)

这些是原文证明的**有定位摘要**，不是本项目独立复核了 Lemmas 1–14 的每行推导；本项目数学判断保持 `UNASSESSED`。

## 人、AI 与版本时间线

下表根据论文 v5 的 [“The story of this proof” 附录，pp.12–13](https://arxiv.org/pdf/2601.07421v5)重建。该附录依赖参与者报告；原始 GPT 与 Aristotle 的完整请求/响应日志未在本轮取得。

| 时间 | 有来源支持的动作 | 验收含义 |
| --- | --- | --- |
| 2026-01-04 | Kevin Barreto 以 GPT-5.2 Pro 的非形式化论证为输入操作 Aristotle，获得一个版本的 Lean 证明 | 目标网页措辞有歧义，论坛后来把这一版视为部分结果 |
| 2026-01-05–06 | Barreto 再问 GPT-5.2 Pro 能否加强到讨论后确定的目标；再次运行 Aristotle，1 月 6 日获得形式证明 | 论文作者据 Barreto 澄清与论坛讨论判断关键数学增强并未来自人的提示；这是**来源关于自主性的报告** |
| 2026-01-06 以后 | Boris Alexeev 对已有 Aristotle 证明再次运行 Aristotle 进行简化 | 论文 v5 映射的是 Alexeev 仓库的 `Erdos728b.lean`，不是原始运行逐字文件 |
| 2026-01-12–26 | Nat Sothanaphan 以 Alexeev Lean 文件为基础，将论证写成人可读稿；与 ChatGPT 协作写作并亲自修改、检查；v5 于 1 月 26 日提交 | 文字作者的核查增加可信度，不是形式声明语义等价的自动证书 |

人的职责包括选择/投递问题、根据论坛对目标歧义作判断、发起第二次模型请求、审视公开结果、文献检索和论文写作。AI 的可归因部分：GPT-5.2 Pro 提供并升级非形式化论证；Aristotle 将输入发展为 Lean 证明，Alexeev 的简化复跑也调用 Aristotle；ChatGPT 辅助将 Lean 论证整理成文字。**独立的具体贡献量、失败请求数、精确 prompts、随机种子、计算费用和每轮人类反馈均未知**。不能由“AI 自主解决”的作者判断推断全流程无人选择或审阅。[论文附录与 Acknowledgements, pp.2、12–13](https://arxiv.org/pdf/2601.07421v5)

## 从输入到证书：实际步骤与系统机制的关系

本案例可确认的数据流为：问题表述 → GPT-5.2 Pro 非形式化论证 → Aristotle 产出 Lean → 论坛指出原问题歧义 → GPT-5.2 Pro 给出加强思路 → Aristotle 再产 Lean → Alexeev 用 Aristotle 简化 → Sothanaphan 与 ChatGPT 整理成论文。这是来源记录的**案例外层协作**；Aristotle 内部的 tactic 树和每次 lemma revision 未公开，不能由[系统论文](../systems/aristotle-harmonic.md)的通用架构虚构 #728 的真实节点日志。

一个确实进入公开工件的关键接口是“小素数存在好 $m$”。论文 [Lemma 14, p.10](https://arxiv.org/pdf/2601.07421v5)说坏集合小于区间大小，从而选出对所有 $p\le2k$ 同时可用的 $m$。在 [固定 commit 的 `Erdos728b.lean`，`lemma_good_m_exists_any_c` 与 `erdos_728_fc`](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/v4.24.0/ErdosProblems/Erdos728b.lean)中，后者调用前者产生非空的 `Finset.Icc M (2*M) \ bad_m_set M c`，取出 $m$，再构造 `(m+k,m,2m)`。源码开头的 `W`、`kappa` 定义和 `lemma_forced_carries_largep` 对应论文的赋值与大素数进位接口；论文 §6 pp.10–11 另有完整的引理名对应表。它展示的是最终依赖结构；**不能**从最终 Lean 源码恢复模型先试过哪些失败路线。

## Lean 证书与论文命题的对应

项目当前只做公开源码静态阅读，未运行 `lake build` 或 `#print axioms`。检查对象固定为 [仓库 commit `8822f7ddef30fadbd92e1c6ab4ed897af356af5e` 的 `src/v4.24.0/ErdosProblems/Erdos728b.lean`](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/v4.24.0/ErdosProblems/Erdos728b.lean)、[Lean toolchain 4.24.0](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/v4.24.0/lean-toolchain)及 [Mathlib commit `f897ebcf72cd16f89ab4577d0c826cd14afaafc7`](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/v4.24.0/lakefile.toml)。代码中 `#print axioms` 后的注释记载 `propext`、`Classical.choice`、`Quot.sound`；这是**文件自带文本，非本地 replay 输出**。静态搜索未发现活动的 `sorry` 或 `axiom` 声明，不足以替代构建及完整依赖审计。[源码末尾](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/v4.24.0/ErdosProblems/Erdos728b.lean#L1416-L1420)

| 待比较命题 | 定位 | 直接覆盖范围 |
| --- | --- | --- |
| 论文 v5 Theorem 1 | [p.2](https://arxiv.org/pdf/2601.07421v5) | 任意 $C_1<C_2$、$\varepsilon$：双侧窗口内**无限多**，且 $a,b$ 有双侧比例约束 |
| `good_triples C ε` + `erdos_728` | [定义 L501–504；定理 L1344 起](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/v4.24.0/ErdosProblems/Erdos728b.lean#L501-L504) | 有比例约束、整除与 **$a+b>n+C\log n$ 的无限多**；集合定义中没有 $C_2$ 上界 |
| `erdos_728_fc` | [L1375 起](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/v4.24.0/ErdosProblems/Erdos728b.lean#L1375-L1383) | `∀ᶠ ε` 与任意 $0<C<C'$ 有 **一组**满足整除和双侧窗口的 $a,b,n$；未显式断言无限多，且结论仅写 $a,b>εn$，没有上比例界 |

这两条顶层定理**不能直接作为**论文 Theorem 1 的逐字形式证书。`erdos_728_fc` 的证明中可见 $M$ 的任意大阈值与 $m\in[M,2M]$ 的构造，故加强版可能能从已有引理正式推出；本项目未写/检查该推导。论文 §5 自身提供无限多的文字论证。正确的当前陈述是：“公开了与论文机制相关、静态看无活动 `sorry` 的 Lean 证明文件；其两个公开顶层声明分别证明较弱的明确命题；论文最强陈述的完整 formal statement 仍待核验或补建。”

另一个易误读点：Google DeepMind [Formal Conjectures 的 `728.lean`](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/728.lean)含目标 statement 和 `sorry`，并以元数据**指向** Alexeev 文件；目标库那一行本身不是证明。最初的 [`Erdos728p.lean`](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/v4.24.0/ErdosProblems/Erdos728p.lean)与论文 v5 指定的简化版 `Erdos728b.lean` 也必须分开阅读。[论文 §6 与参考文献 [1]](https://arxiv.org/pdf/2601.07421v5)

## 复现、验证与数学状态

**能检查**：论文 v5 全文、Lean 源码、工具链与 Mathlib 固定版本、相关 Lean 声明/证明依赖、论文 §6 的对应表，以及论坛和[Terence Tao 维护的 AI 贡献页面](https://github.com/teorth/erdosproblems/wiki/AI-contributions-to-Erd%C5%91s-problems)对过程与结果的外部讨论。仓库 README 提醒 `src` 子项目构建可能耗时很久；本任务只做阅读，不执行外部 harness/Lean。[lean-proofs README](https://github.com/plby/lean-proofs)

**尚不能复现**：历史 GPT-5.2 Pro/Aristotle 请求、系统版本、并行实例、失败率、模型内部搜索和服务端预算未公开；即使固定 Lean 工件成功构建，也只复核输出，不复跑发现过程。论文说 Alexeev 的简化文件是整理稿依据，这与最初 1 月 6 日产物不是同一字节版本。[论文附录](https://arxiv.org/pdf/2601.07421v5)

本项目判定：作者声称已解决 #728；公开工件强于普通自然语言 AI 证明，且有一份详细的人读证明与外部数学家讨论；**论文完整 Theorem 1 暂为 `UNASSESSED / PRIMARY-SOURCE-CHECKED / section-summary`**，因为本项目未 kernel replay，亦未把论文最强 statement 与一个完整 Lean 顶层命题逐项对应。这是项目验收状态，不对学界问题当前是否已解决下结论。对源码中两条较弱形式定理，可称“**作者公开了静态可读的形式证明候选**”，不能称本项目已独立验证。先验文献方面，论文 §2 指出与 Erdős、Pomerance 的工作接近但不相同；“没有先前解答”仅按论文截至 2026-01-27 的有界检索报告，不当作穷尽性新颖性证明。[论文 §2，附录](https://arxiv.org/pdf/2601.07421v5)

## 对学习研究方法有用的三点

| 来源中的做法 | 解决的问题和前提 | 风险 / 效果证据 | 待检验推测 |
| --- | --- | --- | --- |
| 先把目标转成 $p$-赋值与进位，再拆成大/小素数；[论文 §§3–4](https://arxiv.org/pdf/2601.07421v5) | 给形式化流程较清楚的中间不变量；需要正确的数论变换 | 可见 Lean 引理链；不能知道哪一部分由 GPT 独创 | 类似“桥接不变量”是否比直接攻顶层定理稳定 |
| 发现者给非形式化思路，证明系统做 Lean 搜索；[论文故事附录](https://arxiv.org/pdf/2601.07421v5) | 将长程数学探索与局部 kernel 检查连接；需准确转译 statement | #728 有源码但缺完整交互日志；人工选题/追问发挥作用 | 对开放问题如何定量区分两类模型贡献 |
| 最终证明再由人写成可读论证，并把论文引理映射到 Lean 名称；[论文 §6](https://arxiv.org/pdf/2601.07421v5) | 帮读者理解机器证明的数学内容；需逐项语义核查 | §6 给出映射，但最强 theorem 的量词仍有接口缺口 | 为每个结论同时提供可读稿、Lean statement 与对应表能否减少误读 |

## 更新触发

1. 出现直接断言“**无限多个 + 双侧对数窗口 + 双侧比例界**”的 Lean 顶层定理及固定环境时，逐定义检查并 replay。
2. 历史 GPT/Aristotle 请求、费用和失败路线公开时，补上贡献与效率判断；不能仅用最终稿反推。
3. 论文勘误、同行评审或具体反例出现时，按受影响的命题、Lean 映射和状态更新。
