---
case_id: "2026-qed-transport-diffusion"
title: "QED 的二维输运–扩散下界：剪切混合与快速周期流"
record_updated: "2026-09-20"
event: "events/2026/2026-05-20-qed-transport-diffusion.md"
systems: ["qed"]
mathematical_status: "UNASSESSED"
workflow_status: "WORKFLOW-DOCUMENTED"
---

# QED 的输运–扩散 PDE 案例

**领域标记：动力系统相邻的 PDE / 流体混合，非平面 ODE。** 它研究二维环面上的被动标量随时间流场演化：剪切输运产生细尺度，扩散耗散高频。傅里叶模态、时间周期算子和谱估计有方法交集；论文没有平面自治向量场的平衡点、极限环或分岔命题。

## 分层判断

- **作者与专家声明：** [An–Xu 数学论文 v1](https://arxiv.org/html/2605.20623v1) 提出三组下界。§5 说问题由人提出，QED 无 PDE 专家运行中指导地生成推导和自检，Xu 后审查正确性并整理成文。[QED 系统论文 v4 Appendix A.4](https://arxiv.org/html/2604.24021v4#A1.SS4) 将其列为成功项目。
- **本项目数学状态：UNASSESSED。** 已读 Theorem 2.1、3.1、3.2、4.1 和选定承重证明段，对 Theorem 2.1 的傅里叶链作局部手算核对；没有独立审完全部 63 页证明、外部谱定理与函数空间细节。UNASSESSED 是本项目未验收，不是宣称学界问题仍 OPEN。
- **AI 贡献证据：** 2026-04-24 官方目录保留旧 P3 的“构造还是证明不可能”的输入、AI 的否定证明和专家评论。数学论文 §2 最终为该不可能性命题。论文 §5 报整组 66 候选、14 个机器接受和专家确认；没有公开完整逐轮日志可重建每次修正。
- **复现边界：** 源码、配置、数学稿和局部旧工件可读；历史运行 commit、API 状态、账单和所有核验报告未绑定。不能把当前 gpt-5.6-sol 配置倒填到 2026-04/05。

## 数学对象 → 原有问题 → 具体结果

在周期二维环面 $\mathbb T^2=[-\pi,\pi]^2$ 上，设非零光滑、平均零的初值 $\rho_0$。带扩散问题是

$$
\partial_t\rho+u(t,x,y)\cdot\nabla\rho=\nu\Delta\rho,\qquad \nu>0.
$$

速度散度为零。无扩散时改记 $\theta$。零均值函数的 $\dot H^{-1}$ 范数给傅里叶模态 $(k,m)$ 权重 $(k^2+m^2)^{-1}$；$\|\rho\|_{\dot H^{-1}}/\|\rho\|_2$ 可理解为一种混合长度。这里的**下界**限制混合长度或 $L^2$ 能量下降得有多快，并非增强混合的上界。[数学论文 §1，式 (1.1)–(1.3)](https://arxiv.org/html/2605.20623v1#S1)

|情形与假设|精确结论|原文定位|
|---|---|---|
|**无扩散剪切：** $\partial_t\theta+U(y,t)\partial_x\theta=0$；$0\ne\theta_0\in C^\infty$、平均零；$U\in L_t^\infty W_y^{1,1}$。|存在 $c_*(\theta_0,U)>0$，对全部 $t\ge0$，$\|\theta(t)\|_{\dot H^{-1}}\ge c_*/(1+t^2)$。因此原题所问的正指数上界不可能。|[Theorem 2.1](https://arxiv.org/html/2605.20623v1#S2.Thmtheorem1)。不能推广成任意有界剪切都不可能指数混合。|
|**带扩散剪切：** $\partial_t\rho+U(t,y)\partial_x\rho=\nu\Delta\rho$；$0\ne\rho_0\in C^\infty$、平均零；实值 $U\in L^\infty_{t,y}$；文中 $0<\nu\ll1$。|显式 $c_2(\rho_0,U,\nu)>0$ 满足 $\|\rho(t)\|_2\ge\|\rho_0\|_2e^{-c_2t}$，对固定数据有 $c_2\le C(\rho_0,U)/\nu$；另有显式 $c_*(\rho_0,U,\nu)>0$ 使 $\|\rho(t)\|_{\dot H^{-1}}/\|\rho(t)\|_2\ge c_*$，均全 $t\ge0$。|[Theorems 3.1–3.2](https://arxiv.org/html/2605.20623v1#S3)。常数依赖初值频谱，不能说对一切 $\nu$、一切初值统一正下界。|
|**快速周期流：** $u(t+L)=u(t)$，实值、散度零，$u\in L_t^\infty W_{x,y}^{1,\infty}$，$\rho_0$ 如上，$0<\nu\ll1$；实际速度 $u(At,x,y)$。|给出取决于 $\rho_0,u,L,\nu$ 的显式充分阈值 $A_0$ 和 $C,c_A>0$；对 $A>A_0$、全部 $t\ge0$，$\|\rho(t)\|_2\ge Ce^{-c_At}$。|[Theorem 4.1、§4 STEP5](https://arxiv.org/html/2605.20623v1#S4)。快频条件不能删；时间不变流是特例。|

论文 §1 将第一组放在粗糙剪切混合背景中，§3 对照 Huang–Xu 的剪切下界，§4 扩大到有足够快时间振荡的流。这里“显式”仍涉及平均算子的谱根空间、投影和 Sylvester 常数，并不意味着给定流场后容易数值算出。§4 STEP5 给阈值公式，本档未验收其所有正则性估计。[论文 §1、§4](https://arxiv.org/html/2605.20623v1)

有一处**需要克制解释**：论文 Remark 3.1(3) 说对 AI 的“$\nu$-sharpness”请求没有被完全理解，仍保留热方程单模例子。因此不能把该例子概括成作者已经完整证明了全类最优的 $\nu$ 指数；它说明在初值可随 $\nu$ 改变时不能忽略初始频率。[原文 §3 Remark 3.1、STEP8](https://arxiv.org/html/2605.20623v1#S3)

## 有来源支持的研究过程和配置

1. **人提出题面。** Xu 给 An 四道流体混合问题。[2026-04-24 官方目录 README](https://github.com/proofQED/QED/blob/03faa8238aef4710084b117657ec9f0f7e80fe57/proved_statements/analysis-Apr-24-2026/README.md) 记 P1–P4；旧 P3 要找 $L_t^\infty W_y^{1,1}$ 剪切和初值使 $\dot H^{-1}$ 指数下降，**或证明不可能**。不能将后来 63 页数学稿当作最初 prompt。
2. **simple-mode 旧运行。** 同一 README 记 Codex GPT-5.4 prover、Gemini 3.1 Pro verifier、无 brainstorm、九轮上限；P1/P2 九轮全被 verifier 拒绝，P3 第 1 轮、P4 第 3 轮成功，随后专家验收。系统论文 v4 §5.1 另称该项目的前两个内部问题用 GPT-5.4 simple mode。旧目录 P3/P4 和 Appendix C 内部 P1/P2 是不同编号口径，本档不作无证据的一一对应。
3. **后续扩展。** [数学论文 §3–4](https://arxiv.org/html/2605.20623v1) 给显式常数、混合尺度和周期流长证明。[系统论文 v4 §5.1、Appendix C](https://arxiv.org/html/2604.24021v4#A3) 记后续内部问题用 GPT-5.5/xhigh decomposition mode，整组费用约 600 美元；[2026-05-19 官方目录 README](https://github.com/proofQED/QED/blob/121900964e6572aaf094412d434b5ac2a792a65f/proved_statements/analysis-May-19-2026/README.md) 也记 GPT-5.5 prover/verifier。数学论文 §5 报全组 66 候选、14 机器接受、少于 36 小时、约 600 美元 API 费。均为作者报告，未获账单和全量轨迹。
4. **人终审和写作。** 数学论文 §1/§5 称专家运行中不给 PDE 提示，最终核查、修订文字并组稿。Remark 3.3 承认原 AI 证明的非齐次 $H^{-1}$ 改为齐次记法时调整常数。人的数学审查和论文责任是真实贡献，不能略去。

**核验模型的资料冲突。** 前述旧目录明确记 Gemini 3.1 Pro verifier，系统论文 §5.1 却写该项目初期两题 “all agents” Codex GPT-5.4。这里保留两种原文说法；未取得历史配置，不能据其一修正其二。旧目录 P3/P4 和系统论文 Appendix C 内部 P1/P2 的编号也不能直接对应。

## 一个关键步骤：从构造问题转向“不可能”

旧 P3 的[原始输入](https://github.com/proofQED/QED/blob/03faa8238aef4710084b117657ec9f0f7e80fe57/proved_statements/analysis-Apr-24-2026/problem-3.md#L3-L18)要求找一个正指数下降例子，或否定存在性。[同一快照的证明](https://github.com/proofQED/QED/blob/03faa8238aef4710084b117657ec9f0f7e80fe57/proved_statements/analysis-Apr-24-2026/problem-3-correct-proof.md#L41-L42)选择否定支，与数学论文 §2 Theorem 2.1 对应。下面是**工件中的数学路线重述**，不是补造的机器运行日志。

1. 减掉 $U$ 的 $y$ 平均仅产生 $x$ 平移，不改傅里叶模绝对值。若初值无非零 $x$-模，解定常且 $\dot H^{-1}$ 恒正。这是不能遗漏的退化分支。[原证明 Steps 1–2](https://github.com/proofQED/QED/blob/03faa8238aef4710084b117657ec9f0f7e80fe57/proved_statements/analysis-Apr-24-2026/problem-3-correct-proof.md#L48-L120)
2. 否则固定 $k\ne0$ 的非零 $x$-模，$F_k(y,t)=F_k^0(y)e^{ik\Phi(y,t)}$，$\Phi(y,t)=\int_0^tU(y,s)\,ds$。该模的 $L_y^2$ 质量 $S>0$ 不变，且一维 $W^{1,1}$ 控制给 $\|\partial_y F_k(t)\|_1\le A+Bt$。[原证明 Steps 3–4](https://github.com/proofQED/QED/blob/03faa8238aef4710084b117657ec9f0f7e80fe57/proved_statements/analysis-Apr-24-2026/problem-3-correct-proof.md#L121-L190)
3. 对 $y$ 模分部积分，$|\widehat F_k(m,t)|\le(A+Bt)/|m|$，故 $|m|>N$ 的能量 $\le2(A+Bt)^2/N$。取 $N(t)\asymp(A+Bt)^2/S$，至少 $S/2$ 留在 $|m|\le N(t)$。负 Sobolev 权重给 $\|\theta(t)\|_{\dot H^{-1}}\ge c/(1+t^2)$，与指数上界矛盾。[原证明 Steps 5–7](https://github.com/proofQED/QED/blob/03faa8238aef4710084b117657ec9f0f7e80fe57/proved_statements/analysis-Apr-24-2026/problem-3-correct-proof.md#L191-L333)

本项目局部核对了指数：单系数 $m^{-1}$ 给尾 $O((A+Bt)^2/N)$；选 $N=O(1+t^2)$，平方范数下界为常数乘 $(1+t^4)^{-1}$，开方是常数乘 $(1+t^2)^{-1}$。尚未验收整个证明或独立 prior-art。

旧目录只记录 P3 第 1 轮通过及最终证明，没有完整 verifier 报告和逐 token 轨迹；不能叙述具体异议如何触发修订。P1/P2 也只知九轮拒绝，失败原因未知。

## 验证、贡献与复现边界

|主张|原始位置|本次实际检查|未解决问题|
|---|---|---|---|
|无扩散下界|[P3 题面](https://github.com/proofQED/QED/blob/03faa8238aef4710084b117657ec9f0f7e80fe57/proved_statements/analysis-Apr-24-2026/problem-3.md)、[旧证明](https://github.com/proofQED/QED/blob/03faa8238aef4710084b117657ec9f0f7e80fe57/proved_statements/analysis-Apr-24-2026/problem-3-correct-proof.md)、[Theorem 2.1](https://arxiv.org/html/2605.20623v1#S2.Thmtheorem1)|对照题面/结论、退化分支和关键傅里叶链|未逐行通读所有常数、外部已有工作|
|带扩散下界与尺度|[Theorems 3.1–3.2](https://arxiv.org/html/2605.20623v1#S3)|核参数、全时量词和低高频屏障框架|resolvent 与频谱常数未完整验收|
|快速周期流|[Theorem 4.1，§4 STEP3–5](https://arxiv.org/html/2605.20623v1#S4)|核 $u,\rho_0,\nu,A$ 条件、伴随观测量路线|谱根空间、Sylvester/抛物平均估计未重建|
|AI 自主和成本|[数学论文 §5](https://arxiv.org/html/2605.20623v1#S5)、[系统论文 §5.1](https://arxiv.org/html/2604.24021v4#S5.SS1)|来源间配置声明对照|历史代码、日志、账单不完整|

LLM verifier 检查论文所设结构与逐步证明，却不是 formal kernel。Xu 的终审比模型自评强，但本项目没有取得可重建的全文证明验收。旧 P3 证实了 AI 提供否定路线和最终证明工件；作者对长篇后续步骤的贡献归因，则主要依赖论文陈述。论文 §5 的 66/14 与系统论文 §5.2 的 GPT-5.5 verifier 子集 214/17 是**不同统计口径**，不能相加或互换。[系统档案](../systems/qed.md#验证器的能力边界)

## 来源、复用与学习顺序

[QED 系统档案](../systems/qed.md)给固定源码、配置、权限；[本批来源收据](../references/notes/2026-09-20-qed-expansion.md)列实际查阅范围。数学从 [An–Xu 2605.20623v1 §2–4](https://arxiv.org/html/2605.20623v1) 查；流程从 [QED 2604.24021v4 §4、Appendix C](https://arxiv.org/html/2604.24021v4) 查；旧 P3 [题面](https://github.com/proofQED/QED/blob/03faa8238aef4710084b117657ec9f0f7e80fe57/proved_statements/analysis-Apr-24-2026/problem-3.md)与[证明](https://github.com/proofQED/QED/blob/03faa8238aef4710084b117657ec9f0f7e80fe57/proved_statements/analysis-Apr-24-2026/problem-3-correct-proof.md)是最直接的输入到产物链。当前实现固定 121900964e6572aaf094412d434b5ac2a792a65f。本批未下载 PDF，因此没有本地 PDF hash；也未运行外部 harness。

建议按 **§2 原题与分支 → §3 低高频能量屏障 → §4 平均算子根空间和伴随可观测量** 学习。先核 $\nu,A,t$ 量词，再评判方法能否迁移。若要把 §4 用作自己的 PDE 证明依据，需先制作必要忠实摘录并逐条核其外部谱论前提。
