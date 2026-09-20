# fluid_lean：光滑外力下流体方程爆破的公开来源剖面

> **阅读层级：高价值来源剖面，尚非完整 harness／数学证明深读。** 本篇核对作者论文的定理入口和公开 Lean 顶层声明，记录 AI 参与的可见证据；没有执行 Lean、`comparator` 或逐行审阅千余证明模块。详见[版本与检查收据](../references/notes/2026-09-20-fluid-lean-source-audit.md)。

## 为什么与本项目相关，为什么不是平面 ODE

作者 Levent Alpöge 与 Tristan Buckmaster 的两个工作涉及无粘 Boussinesq 系统和三维不可压 Euler 方程的有限时间奇性构造，并公开了 [fluid_lean 固定版本](https://github.com/tristanbuckmaster/fluid_lean/tree/d0124689230b58b4f86e7b90ac59de06404b3b6b)。这些是对连续空间场 $\theta(t,x),u(t,x),p(t,x)$ 的**偏微分方程（PDE）**。Boussinesq 的“planar”指 $x\in\mathbb R^2$ 的二维**空间**，不是相平面上的有限维自治 ODE；Euler 是 $x\in\mathbb R^3$ 的 PDE。它们与用户的动力系统兴趣有实质关联：正则性、爆破、流与多尺度构造；但不能直接转用为平面 ODE 的极限环或分岔结论。

这条来源值得重点跟进，因为同时给出作者手稿、Lean 项目、定义层、待证陈述、证明桥接、比较器配置和 AI 使用声明。它也说明形式化后仍须逐项查**自然语言定理和 Lean 命题的对应关系**。目前公开的具体工作流程记录不足，故不将其称为一个可复用、已完整深读的新 harness，不进入本项目事件统计。

## 数学成果：两个不同的方程和爆破断言

|项目|作者手稿的命题入口|公开 Lean 顶层命题所写|本批差异判断|
|---|---|---|---|
|二维无粘 Boussinesq|[作者 Boussinesq 手稿](https://cims.nyu.edu/~tristanb/boussinesq.pdf)，Theorem 1.1（PDF 第 3 页）：$\mathbb R^2$ 上带温度力和动量力，光滑紧支初始温度、**初始速度为零**；力在爆破时刻仍光滑并支于固定球；$\theta$ 有界、$\|\nabla\theta(t)\|_\infty\to\infty$、$\limsup_{t\uparrow T_*}\|\omega(t)\|_\infty=\infty$；定理还规定初值形式及状态支集|[Boussinesq `Challenge.lean`](https://github.com/tristanbuckmaster/fluid_lean/blob/d0124689230b58b4f86e7b90ac59de06404b3b6b/boussinesq-blowup/Challenge.lean#L67-L80)：**对每个 $\kappa>0$** 存在 $T>0$、$\theta,u,p$ 与两种外力；初始 $\theta,u$ 紧支、有限能量；$\theta$ 有界、存在 $g(t)\to\infty$ 且每个 $t<T$ 有点 $|\nabla\theta|\ge g(t)$；涡量只要求临近 $T$ 的任意大阈值被频繁达到；每个较短区间内在有限能量 Lipschitz 类中唯一|梯度结论是趋于无穷，涡量是 **limsup** 而非全极限。Lean 顶层没有字面要求 $u(0)=0$、论文指定的初始温度函数、状态全程固定球支集或外力跨越 $T$ 的延拓|
|三维不可压 Euler|[作者 Euler 手稿](https://cims.nyu.edu/~tristanb/euler.pdf)，Theorem 1.1（PDF 第 2 页）：对任意指定圆环半径 $r_0>0$ 和高度 $z_0$，构造固定实心环内的轴对称初值和力；初始有非零 swirl、零 meridional 速度；环量与 meridional 速度有界，而 $\|\nabla\Gamma(t)\|_\infty$ 和 $\|\omega(t)\|_\infty$ 都趋于无穷，$\int_0^{T_*}\|\omega(t)\|_\infty dt=\infty$|[Euler `Challenge.lean`](https://github.com/tristanbuckmaster/fluid_lean/blob/d0124689230b58b4f86e7b90ac59de06404b3b6b/euler-blowup/Challenge.lean#L56-L67)：存在 $T>0$、紧支初始速度、带光滑外力的经典解；有 $g(t)\to\infty$ 在各时刻由某点涡量大小达到；非负可积下界的积分可任意大；较短区间内有限能量 Lipschitz 类唯一|Lean 顶层**没有字面列出**指定环位置、轴对称、swirl、meridional 有界、$\nabla\Gamma$ 爆破或状态环支集。这些可能在内部构造出现，但不能从顶层命题推断其已作为公开定理被检查|

两份 Lean 顶层对外力的要求是半开区间 $[0,T)$ 上 $C^\infty$、空间固定球支集、任意阶混合导数在该区间有界（`SmoothForce`）。两份作者手稿写外力延伸到闭区间、仍 $C^\infty$。二者可能存在可证明的延拓桥梁，但本批没有核对该桥梁；不把两种表述自动等同。[Boussinesq 定义层](https://github.com/tristanbuckmaster/fluid_lean/blob/d0124689230b58b4f86e7b90ac59de06404b3b6b/boussinesq-blowup/Challenge.lean#L25-L64)和[Euler 定义层](https://github.com/tristanbuckmaster/fluid_lean/blob/d0124689230b58b4f86e7b90ac59de06404b3b6b/euler-blowup/Challenge.lean#L8-L53)还分别定义了经典解、力正则性与允许比较的弱解类；仅核对末尾定理名不够。

上述差异不是对作者论文的反驳，也不能由静态阅读推出 Lean 证明错误。它们界定了本项目目前**能从顶层工件直接验收的命题范围**，并提示后续需要证明论文额外条件如何由内部构造推出、或另找相应形式陈述。[Boussinesq `formalization.yaml` 的 fidelity/review](https://github.com/tristanbuckmaster/fluid_lean/blob/d0124689230b58b4f86e7b90ac59de06404b3b6b/boussinesq-blowup/formalization.yaml#L64-L88)自己也记录了语义表示与 `unreviewed` 状态；[Euler 对应文件](https://github.com/tristanbuckmaster/fluid_lean/blob/d0124689230b58b4f86e7b90ac59de06404b3b6b/euler-blowup/formalization.yaml#L63-L85)标为作者已核对，但这不能代替本项目独立对照。

## AI 参与、形式化组织及其可学习程度

[Boussinesq 作者手稿 §2“AI statement”](https://cims.nyu.edu/~tristanb/boussinesq.pdf)明确说作者在 Córdoba–Martínez-Zoroa 多尺度路线及自己已有想法上，与 Claude 和 Codex 反复试探 ansatz、证明架构并整理写作；他们把首次 Boussinesq 解与当前简化版本分开，报告曾在 2026-08-22 对较早版本作 Lean 验证，随后经模型与人工编辑得到当前手稿。它**没有提供完整提示、代理日志、失败分支清单或当前版本的逐轮历史**，不能据此画出确定的模型接力时间线。

两目录 [README](https://github.com/tristanbuckmaster/fluid_lean/blob/d0124689230b58b4f86e7b90ac59de06404b3b6b/boussinesq-blowup/README.md) 和 `formalization.yaml` 则作另一层更具体的作者声明：**Lean 代码（包括顶层陈述）由 Claude 在 Levent Alpöge 指导下编写**。这与手稿提及 Codex 参与数学推导/写作不矛盾，但不能把 Codex 记为已核实的 Lean 代码作者。Boussinesq 元数据记顶层陈述的人工对应审阅为 `unreviewed`；Euler 元数据记为 `author-verified`、审阅人为 Alpöge。这些是仓库自述；本批没有独立核实人工审阅过程。

```mermaid
flowchart LR
  M[作者的多尺度思路与数学手稿] --> C[Claude 在人工指导下写 Lean 定义与证明：作者声明]
  C --> L[内部构造与数值区间证书模块]
  L --> S[Solution.lean：导出顶层命题]
  H[Challenge.lean：仅陈述的模板] --> K[comparator 配置：同一命题、允许公理、重放]
  S --> K
  K --> R[作者报告完成；本项目尚未运行重放]
```

两个项目均用 `Challenge.lean` 提供待证明的**可信命题模板**，末尾写 `by sorry`；`Solution.lean` 的同名定理则从库中主定理桥接，源码没有该占位。本批把两个顶层陈述的文字逐字比较，Challenge 与 Solution 相同。故不能因 Challenge 有 `sorry` 就说正式证明必然残缺，也不能因 Solution 看不到 `sorry` 就说整个库已通过 kernel。README 报告构建无错误、仅模板发出一次 `sorry` 警告，并报主定理仅依赖 Lean 标准公理 `propext`、`Classical.choice`、`Quot.sound`；**这些均未在本机执行验证**。两个项目的 [comparator 配置](https://github.com/tristanbuckmaster/fluid_lean/blob/d0124689230b58b4f86e7b90ac59de06404b3b6b/euler-blowup/comparator.json)列同名 theorem 和允许公理，具体代码安全与全量依赖仍需实际重放。

来源显示的研究接口为“作者确认命题含义 → 模型编写定义/推导/证书 → `Solution` 连接数学核心 → 比较器对照 `Challenge`”。对本项目的可学习点是将**陈述层、证明层和数值证书层分开**，并显式记录模型写出陈述后的人类语义审阅。可复用的是这个检查框架；完整生成 Lean 代码的 prompts、会话、预算、失败次数和内部研究 harness 均未公开。

## 当前判断与下一次核查

- **数学重要性：高。** 作者手稿提出光滑强迫下流体 PDE 的有限时间奇性及较强的唯一性/几何性质；与动力系统和奇性形成研究接近，但不是平面 ODE。重要性不是证明已被本项目验收的标签。
- **公开证据：有固定 Lean 大型工件与作者手稿；项目数学状态 `UNASSESSED`。** 本批只读作者定理、顶层定义/证明桥、元数据和比较器，未重放 Lean，也未核查所有引理、区间算术证书和手稿证明细节。
- **复用价值：中高，但主要是方法结构。** 顶层声明与论文额外性质存在可定位的对应缺口；原系统日志和完整自动化配置不公开。若后续要正式深读，应先核对附加性质的形式化陈述/证明，再做可用资源下的固定版本构建及 axiom 输出检查；对 Boussinesq 先取得作者对顶层陈述的审阅结论。

本专题只作来源剖面，后续进入完整案例深读须另开清晰验收范围，不能因“Lean 仓库很大”自动提高数学状态。
