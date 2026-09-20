# fluid_lean 两个流体 PDE 工件：来源收据与未验收接口

- 核查日期：2026-09-20；访问模式：公开、只读。
- 准确定位的官方仓库：[tristanbuckmaster/fluid_lean@d0124689230b58b4f86e7b90ac59de06404b3b6b](https://github.com/tristanbuckmaster/fluid_lean/tree/d0124689230b58b4f86e7b90ac59de06404b3b6b)，GitHub commit API 时间 2026-09-08 04:07:52 UTC，提交说明 `Add affinecore, boussinesq-blowup, and euler-blowup Lean projects`。
- 读物范围：两个项目的 README、`formalization.yaml`、`Challenge.lean`、`Solution.lean`、`comparator.json`、`lean-toolchain`，和两份作者 PDF 的摘要及定理/AI 说明相关页。没有下载长期保存 PDF；下列哈希是本次从作者页面读取的**远端字节**，用于未来判断版本漂移，不能当作本地长期副本。

|来源|精确位置及用途|本次 SHA-256／版本|
|---|---|---|
|[作者 Boussinesq PDF](https://cims.nyu.edu/~tristanb/boussinesq.pdf)|76 页；摘要 PDF 第 1 页，方程 (1.1) 第 2 页，Theorem 1.1 第 3 页，§2 “AI statement” PDF 第 7–8 页|`895a628d1783bcb039374686f50b895b5f450f53b8ef8aa173523487a7a4a21b`，846615 bytes|
|[作者 Euler PDF](https://cims.nyu.edu/~tristanb/euler.pdf)|摘要 PDF 第 1 页，方程 (1.1) 第 1–2 页，Theorem 1.1 第 2 页；通过作者 URL 直接读取并在内存中 `pdftotext` 前 5 页，web PDF 入口返回 Internal Error|`97ef408bff09b4f6ed9f3867734d1eb2245f3f34e6334b28136c84c02d0ae8d8`，1105306 bytes|
|[Boussinesq README](https://github.com/tristanbuckmaster/fluid_lean/blob/d0124689230b58b4f86e7b90ac59de06404b3b6b/boussinesq-blowup/README.md)|定理自然语言第 9–28 行；构建、结构与 AI 作者声明第 31–71 行|固定 commit|
|[Boussinesq formalization.yaml](https://github.com/tristanbuckmaster/fluid_lean/blob/d0124689230b58b4f86e7b90ac59de06404b3b6b/boussinesq-blowup/formalization.yaml)|项目描述、status、automation、fidelity、review；`review.status: unreviewed` 约第 76 行|固定 commit|
|[Boussinesq Challenge](https://github.com/tristanbuckmaster/fluid_lean/blob/d0124689230b58b4f86e7b90ac59de06404b3b6b/boussinesq-blowup/Challenge.lean#L67-L80) / [Solution](https://github.com/tristanbuckmaster/fluid_lean/blob/d0124689230b58b4f86e7b90ac59de06404b3b6b/boussinesq-blowup/Solution.lean#L8-L25)|定义层 Challenge 第 8–64 行；顶层定理第 67–80 行；Solution 同名陈述第 8–20 行、证明桥第 21–25 行|Challenge `6804cbb60c016907e4fe31ac69cc530c0e3df1cc40db3f72ee2995306d9ac222`；Solution `eebf2ef2b4f88de536ce395dbd2eef60071d58dc5a5c8e70d38cff3f277cf5da`|
|[Euler README](https://github.com/tristanbuckmaster/fluid_lean/blob/d0124689230b58b4f86e7b90ac59de06404b3b6b/euler-blowup/README.md)|定理自然语言第 9–28 行；构建、结构与 AI 作者声明第 31–64 行|固定 commit|
|[Euler formalization.yaml](https://github.com/tristanbuckmaster/fluid_lean/blob/d0124689230b58b4f86e7b90ac59de06404b3b6b/euler-blowup/formalization.yaml)|项目描述、status、automation、fidelity、review；`review.status: author-verified` 约第 72 行|固定 commit|
|[Euler Challenge](https://github.com/tristanbuckmaster/fluid_lean/blob/d0124689230b58b4f86e7b90ac59de06404b3b6b/euler-blowup/Challenge.lean#L56-L67) / [Solution](https://github.com/tristanbuckmaster/fluid_lean/blob/d0124689230b58b4f86e7b90ac59de06404b3b6b/euler-blowup/Solution.lean#L8-L26)|定义层 Challenge 第 8–53 行；顶层定理第 56–67 行；Solution 同名陈述第 8–18 行、证明桥第 19–26 行|Challenge `470a2468cc22abe02b56fe77061ef379150363da4cb6af2e66bcd66cb6f07cc5`；Solution `579ee0830b3083f78efef039c5abf581ba7d880fc1ee41467ed0437995519880`|
|[两个 comparator.json：B](https://github.com/tristanbuckmaster/fluid_lean/blob/d0124689230b58b4f86e7b90ac59de06404b3b6b/boussinesq-blowup/comparator.json) / [E](https://github.com/tristanbuckmaster/fluid_lean/blob/d0124689230b58b4f86e7b90ac59de06404b3b6b/euler-blowup/comparator.json)|各 13 行：challenge/solution 模块、定理名、`propext`、`Quot.sound`、`Classical.choice` 允许列表|配置只读，未运行比较器|

## 静态核对得到的确定事实

1. 两份 `Challenge.lean` 在同名定理末尾各有**一个** `sorry`，这是作者所称“只装陈述的模板”中的占位；两份 `Solution.lean` 可见文本无 `sorry`。我们以同名 `theorem … :` 到 `:= by` 为界抽取，逐字符比较 Challenge 与 Solution 顶层**命题文本完全一致**。这项静态检查不能覆盖导入的证明库、隐藏公理或语义定义。
2. 两目录的 `lean-toolchain` 都为 `leanprover/lean4:v4.32.2`。README 写 `lake-manifest.json` 中 Mathlib commit `81a5d257c8e410db227a6665ed08f64fea08e997`，并报 Boussinesq 构建约 1500 模块/高内存、Euler 约 1100 模块。这些是作者构建指南；我们没有安装工具、没有执行 `lake build` 或 `PrintAxioms.lean`。
3. Boussinesq 顶层：`∀ κ > 0`；温度梯度存在趋于无穷的逐时刻下界；涡量是 `∀ M, ∃ᶠ τ in 𝓝[<] T` 的 limsup 性质。Euler 顶层：涡量逐时刻趋无穷下界，且另有任意大积分的可积下界；不可混用 B 的 limsup 与 E 的全极限。
4. 作者 PDF 的加强条件与 Lean 顶层不逐字相同：B 论文 Theorem 1.1 固定 $u_0=0$、特定初始温度、全程状态支集，Lean 顶层只显式要求初始 $u$ 紧支；E 论文 Theorem 1.1 对任意圆环中心/半径给出轴对称构造及环量和 meridional 条件，Lean 顶层没有相应量词/性质。两个 Lean 顶层都对力写半开 $[0,T)$ 上每阶导数有界，不字面写跨越爆破时刻的 $C^\infty$ 延拓。后者可能由有界导数另行推出，但本批未核。**不得把作者更强手稿定理整体叫作已经由这些顶层陈述逐字形式化。**
5. README 与 YAML 说所有 Lean 代码由 Claude 在 Alpöge 指导下生成；B YAML `review.unreviewed`，E YAML `review.author-verified`。B 作者手稿 §2 报告 Claude/Codex 参与更广义的证明路线与写作迭代，分别记录才不混淆。

## 未做与下一步

未检查全部证明依赖、无占位全仓搜索、实际 kernel 重放、`#print axioms` 输出、comparator 运行、数值区间证书的精确目标及论文证明的全部分析假设。`formalization.yaml` 中 `sorry_count: 0` 是它排除 Challenge 模板后的作者元数据，不是本批运行结果。论文来源的完整阅读也是摘要/命题/AI 说明级，不用于宣称数学定理已独立证明。若正式验收，先补命题语义对照（尤其额外几何/初值条件），再在资源允许时以该固定 commit 重放两个隔离 Lean 项目及比较器；不要在这个来源剖面中捏造结果。

日期仅由 GitHub commit API 的 2026-09-08 给定。检索中曾见一条 NYU 新闻页面标“2027”，与本轮时点不符，**未用于定年或数学验收**。
