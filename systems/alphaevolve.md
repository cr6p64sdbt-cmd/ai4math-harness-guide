---
system_id: "alphaevolve"
name: "AlphaEvolve"
record_updated: "2026-09-20"
versions_checked: ["arXiv:2506.13131v1", "google-deepmind/alphaevolve_results@9909c1347ea1", "google-deepmind/alphaevolve_results@4226acbf237ff9ad10ba7673a2af127a2d8a5971"]
primary_sources: ["https://arxiv.org/html/2506.13131v1", "https://github.com/google-deepmind/alphaevolve_results/tree/9909c1347ea1"]
reproducibility: "PUBLIC-RESULT-CERTIFICATE / INTERNAL-SEARCH-NOT-REPRODUCIBLE"
---

# AlphaEvolve：以可评价的程序为研究对象

## 对象、成果与阅读入口

AlphaEvolve 是 Google DeepMind 报告的**进化式 coding agent**：人给出初始程序、允许改写的代码区域、评价函数和可选背景；模型提出代码修改；评价器运行候选，记录分数和反馈；数据库将有价值的旧程序重新送入下一轮提示。它适合候选程序能够自动评分的构造、搜索和算法优化问题。模型本身不负责判定数学命题真伪。系统最具体、可核查的数学案例是 [4×4 矩阵乘法的 48 项张量分解](../dossiers/2025-alphaevolve-matrix-multiplication.md)。[本批来源记录](../references/notes/2026-09-20-alphaevolve-expansion.md)列出固定版本、工件和检查边界。

**与动力系统的关系：本次未发现经核实的平面 ODE、分岔或极限环成果。** 若未来把严格的存在性判据、反例条件或有限参数证书写为评价器，可研究相似的程序搜索组织方式；这是迁移设想，不是 AlphaEvolve 已在这些方向成功的案例。[论文 §3.1–3.2](https://arxiv.org/html/2506.13131v1)的数学成果集中在矩阵乘法及构造优化。

## 版本和来源

|用途|固定来源|实际读到的内容|边界|
|---|---|---|---|
|系统论文|[arXiv:2506.13131v1](https://arxiv.org/html/2506.13131v1)，2025-06-16；[版本页](https://arxiv.org/abs/2506.13131)|§2.1–2.6、§3.1、§4、Fig. 4、附录 A|截至本次检索，arXiv 只有 v1；论文描述内部系统，不公开完整服务|
|论文相邻结果仓库|[alphaevolve_results@9909c1347ea1](https://github.com/google-deepmind/alphaevolve_results/tree/9909c1347ea1)，2025-06-17|README、`mathematical_results.ipynb` 第 3–4、35–37 个 cell|含数学数据与验证函数，不含搜索控制器|
|当前结果仓库|[alphaevolve_results@4226acbf237ff9ad10ba7673a2af127a2d8a5971](https://github.com/google-deepmind/alphaevolve_results/tree/4226acbf237ff9ad10ba7673a2af127a2d8a5971)，2026-01-05|仓库版本和工件清单|当前 notebook 与论文相邻版本 blob 不同；不把后续修订倒填旧运行|

论文和 notebook 来源日期均于 2026-09-20 复核。仓库 [README](https://github.com/google-deepmind/alphaevolve_results/blob/9909c1347ea1/README.md)明确说**没有运行 AlphaEvolve 的代码**，并区分软件的 Apache-2.0 与其他材料的 CC BY 4.0；[LICENSE](https://github.com/google-deepmind/alphaevolve_results/blob/9909c1347ea1/LICENSE) 附有 Apache-2.0 文本。结果仓库的许可不能据此推定内部系统开放或可使用。未保存论文 PDF；原文 HTML 足以定位本篇所引用的系统段落。

## 输入到输出的工作流

```mermaid
flowchart LR
  H[人：问题、初始程序、评价器、边界] --> P[提示采样器]
  D[(程序数据库：候选、分数、输出)] --> P
  P --> L[Gemini 2.0 Flash / Pro：提出代码修改]
  L --> A[应用差异块生成候选程序]
  A --> E[评价级联：执行、筛除、评分]
  E --> D
  D --> O[选出候选算法或数学工件]
  O --> V[独立核验具体数学命题]
```

论文 [§2.1](https://arxiv.org/html/2506.13131v1)要求人提供 `evaluate` 函数，返回一个或多个标量分数，默认越大越好。`# EVOLVE-BLOCK-START/END` 标记可修改范围，未标记的骨架负责调用结果。初始程序须完整可运行，即使性能很差。与只改短函数的 FunSearch 相比，论文 [表 1](https://arxiv.org/html/2506.13131v1)介绍它可改多个代码组件；这是系统宣称的接口范围，不表示所有任务都用到了所有功能。

[§2.2–2.3](https://arxiv.org/html/2506.13131v1)说明提示从数据库抽取旧程序、分数和输出，也可带人工问题描述、公式、文献、随机格式模板及共同演化的 meta prompt。模型以 `SEARCH/REPLACE` 差异块修改已有代码，短程序也可全量输出。论文报告使用 Gemini 2.0 Flash 提高采样吞吐，Gemini 2.0 Pro 偶尔提供能力更强的建议；每轮实际采样比例、具体提示和模型调用配置未公开。

[§2.4](https://arxiv.org/html/2506.13131v1)的评价可按难度级联：先小规模排除错误或低分候选，再进行昂贵评估。LLM 还可为难以程序化的属性提供辅助分数，例如简洁性。这类 LLM 分数不是数学验证。多指标分数可保留不同结构的有前景候选。[§2.5](https://arxiv.org/html/2506.13131v1)称数据库受 MAP-Elites 与 island 模型启发，在开发当前最优与保留多样性间折中；文中没有公开可逐步重演的数据库实现或淘汰日志。[§2.6](https://arxiv.org/html/2506.13131v1)报告异步 controller、模型采样器和评价节点，优化总吞吐量而非单次迭代延迟。

## 研究状态、错误和停止

这里的长期状态是**程序种群及其评分、输出**，不是一个证明义务图。选择路线主要通过改写程序和数据库中的候选组合实现；反馈不佳的程序可在级联评价中淘汰。来源没有提供数学事实的依赖图、正式撤销传播、失败尝试全集或可审计的每轮因果日志，因此不能把这些功能写成已实现。人工给出预算和停止条件的接口也没有完整公布；系统会迭代到外部资源/任务终止，但此 48 项案例的实际运行时间、尝试数、终止规则未知。

[§4 与 Fig. 8](https://arxiv.org/html/2506.13131v1)有进化、上下文、meta prompt、全文件演化和模型能力的消融，且图注称每设置有三次不同随机种子运行。这支持若干组件在论文任务集上有贡献；不能由曲线反推 4×4 单一结果必定由某组件造成。论文 [§3.1 Fig. 4](https://arxiv.org/html/2506.13131v1)展示一个经历 15 次变异的搜索程序，涉及 optimizer/初始化、离散化 loss、超参数搜索。它是可见的实际编辑线索，但没有完整 15 步逐轮记录，也未给出其与公开 48 项工件一对一的运行绑定。

## 验证与数学可信范围

评价器可能同时混合经验分数和严格判据，必须逐题判断。矩阵案例先用优化算法搜索近似低秩分解，再把系数舍入至整数或半整数，最后检查**张量恒等式**；数值 loss 小不足以证明恒等。公开 notebook 的 `verify_tensor_decomposition` 用 `np.einsum` 重建张量，`np.array_equal` 与目标比较；所给系数是半整数实部/虚部。本项目另以[自编整数检查器](../scripts/check_alphaevolve_rank48.py)把系数乘 2 转为高斯整数对，精确核对固定工件全部 4096 个系数，细节见[案例](../dossiers/2025-alphaevolve-matrix-multiplication.md)。没有运行外部 notebook 或内部系统。

验证一个具体分解只能证明一个**上界**，不证明张量秩恰为 48、算法运行最快、或者所有 14 项改进均正确。论文称“可证明正确”应对每个工件独立读其验证接口；本项目这里只核 4×4 工件。相关作者后续的[非交换 48 次有理系数算法](https://arxiv.org/abs/2506.13242)扩展适用范围；这不是 AlphaEvolve 原本的复系数分解。

## 公开使用与方法卡

最小**只读学习路径**：读论文 §2 的输入/反馈循环，读 §3.1 的张量案例，再在固定 [notebook](https://github.com/google-deepmind/alphaevolve_results/blob/9909c1347ea1/mathematical_results.ipynb) 对照第 4 个 cell 的验证函数、第 35–37 个 cell 的系数与调用。可复用的是问题接口设计、张量工件和检查思路；不能直接下载 notebook 就运行 AlphaEvolve 搜索。论文没有该案例的 token/API 费用、总计算成本、完整 prompt 和配置文件；公开仓库不包含这些材料。

|来源中的实际做法|解决的问题|适用前提|失败风险|效果证据|待检验迁移假设|
|---|---|---|---|---|---|
|标注可演化代码区并固定评价器（§2.1）|把开放探索接到稳定评分接口|对象能程序表示，判据可信|评价器漏掉数学条件|48 项工件可独立核验；§4 消融为任务集证据|ODE 搜索中可否把严格存在性条件写成可验证证书|
|数据库采样旧程序和反馈（§2.2、2.5）|保留有效路线及多样性|可接受大量自动评价|局部最优、错误评分反复强化|论文 §4 的任务集消融|对复杂解析证明需另设事实与假设状态|
|演化搜索算法本身（§3.1）|直接搜索分解效率低时改进求解策略|有可运行的搜索程序与预算|优化 loss 误导，随机种子依赖|论文报告 15 次变异示例、48 项分解|与数学启发式结合是否可帮助找严格证书|

上述迁移假设尚无本项目的 ODE 实验支持。再次更新应优先寻找：公开完整搜索日志与配置、实际成本、版本绑定，以及独立的新数学应用。不能用当前结果仓库的许可或 notebook 代替系统开放度的证据。
