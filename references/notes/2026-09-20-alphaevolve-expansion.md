# AlphaEvolve 本批来源和核查记录（2026-09-20）

## 检索问题、路线与版本

本批问题是：AlphaEvolve 的公开系统机制是什么？4×4 矩阵乘法 48 次方案到底在哪个数域、可检验到何种程度？可供以后复用的版本入口在哪里？由本项目 [候选目录](../../CANDIDATES.md)出发，实际用 `AlphaEvolve 4x4 complex matrix multiplication 48`、官方结果仓库名和 arXiv 编号检索；发现路线是公开搜索，内容验收仅取下列作者论文、官方仓库与相关数学作者的后续论文。社区复述只当定位，未作结论依据。没有做数据库级穷尽优先权调查。

|角色|固定原始入口|实际读取|版本和范围|
|---|---|---|---|
|系统与案例论文|[Novikov 等，arXiv:2506.13131v1](https://arxiv.org/html/2506.13131v1)，[版本页](https://arxiv.org/abs/2506.13131)|§1 表 1，§2.1–2.6，§3.1 表 2、Fig. 4，§3.2 人工建议说明，§4 Fig. 8，附录 A 标题|2025-06-16 v1；2026-09-20 版本页仅列 v1；HTML section summary，未做全文证明逐行审计|
|结果仓库，论文相邻固定快照|[google-deepmind/alphaevolve_results@9909c1347ea1b28d0c17dcb1f879a1c91b7dec3a](https://github.com/google-deepmind/alphaevolve_results/tree/9909c1347ea1b28d0c17dcb1f879a1c91b7dec3a)|README、LICENSE、`mathematical_results.ipynb` cells 3–4、35–37|commit 日期 2025-06-17；第 36 cell 三矩阵和第 37 cell 验证调用是本案工件|
|结果仓库，访问时 HEAD|[4226acbf237ff9ad10ba7673a2af127a2d8a5971](https://github.com/google-deepmind/alphaevolve_results/tree/4226acbf237ff9ad10ba7673a2af127a2d8a5971)|GitHub API commit 清单及文件 blob/大小|2026-01-05；当前 notebook Git blob `1a33a2510b43f87366d564c72b89b02ea989b276`，不同于 2025-06-17 blob `52dc7ff9ca284ea6edc6961f77892a59a8c1afef`；未比较全部 cell 变化|
|后续背景|[Dumas–Pernet–Sedoglavic，arXiv:2506.13242v7](https://arxiv.org/abs/2506.13242)|摘要、版本史|作者报告有理系数、非交换 48 次方案；仅用于防止把旧复系数方案误写成最广适用结果；未审全文证明|

原始论文 [§3.1 表 2](https://arxiv.org/html/2506.13131v1)的比较是 4×4 复矩阵乘法张量秩上界：Strassen 两级 49、AlphaEvolve 48。同节明确有特征 2 上 47 的不同数域结果；脚注指出其他少于 49 的算术方案不一定是可递归的矩阵乘法张量分解。当前后续论文不属于 AlphaEvolve 2025 案例的组成部分。

## 工件的静态及独立有限检查

仅以 HTTPS 在内存中读取固定 notebook 的 JSON，**未安装或运行作者 notebook 和外部 harness**。原始字节 SHA-256：`589ce95c3ff63ab2ea506e2e6ced44213d6e76f4bdb4b1b73e78d240bcc15008`。没有把该大 notebook 或 PDF 保存进仓库。复核入口是本项目自编的 [scripts/check_alphaevolve_rank48.py](../../scripts/check_alphaevolve_rank48.py)：`python -X utf8 scripts/check_alphaevolve_rank48.py`。

- 官方 notebook 第 4 cell：`verify_tensor_decomposition` 检查三因子形状，以 `np.einsum` 重建张量，并用 `np.array_equal` 核对；源码只读，未执行。
- 第 35 cell 标 `Rank-48 decomposition of <4,4,4> over 0.5*C`；第 36 cell 赋值 `decomposition_444`；第 37 cell 给定 `n=m=p=4, rank=48` 并调用官方函数。
- 自编脚本先核原始字节哈希，再解析第 36 cell 的 Python AST，只接受数值字面量、正负号及加减，拒绝其余表达式；**不会 `exec` notebook 代码**。它得到三组 16×48 因子矩阵，逐个检查实部和虚部乘 2 后为整数。
- 对 $a=(i,j), b=(j',k), c=(k',i')$，目标 $T_{a,b,c}=1$ 恰在 $i=i', j=j', k=k'$ 时成立。把三组因子各乘 2 后，脚本在高斯整数对 $\mathbb Z[i]$ 上计算 $\sum_{r=1}^{48}(2U_{a,r})(2V_{b,r})(2W_{c,r})$，与 $8T_{a,b,c}$（`(8,0)` 或 `(0,0)`）比较。这是整数精确检查，不依赖浮点乘积相等。
- 2026-09-20 实际运行：`ALPHAEVOLVE-RANK48-EXACT-CHECK: PASS sha256=589ce95c3ff63ab2ea506e2e6ced44213d6e76f4bdb4b1b73e78d240bcc15008 factors=3x16x48 coordinates=4096 target_ones=64 arithmetic=Gaussian-integers`。此前一次性浮点检查也得到 4096 项相等；本次固定脚本把验收提升为精确整数算术，并提供可重跑入口。

此项检查给固定工件的**有限代数身份**，不是 AlphaEvolve 内部搜索复现、来源优先权审计或 48 的下界证明。脚本依赖 HTTPS 读取固定 URL；若未来来源不可访问，现有笔记和哈希不能替代未保存的 notebook 字节。若进一步增强独立性，应取得另一份独立实现的交叉检查；本轮未做第二实现。

## harness 复用入口与不可得项

1. 机制接口在[论文 §2.1–2.6](https://arxiv.org/html/2506.13131v1)：`evaluate`、`EVOLVE-BLOCK`、旧候选/反馈提示、Gemini 2.0 Flash/Pro、分级评价、数据库、异步流水线。
2. 本案关键实例在[论文 §3.1 与 Fig. 4](https://arxiv.org/html/2506.13131v1)：优化分解的程序、多种随机种子、最低秩与成功比例、整数/半整数舍入、十五次变异的图示程序。图示与最终工件的逐轮绑定未公开。
3. 可复核的最终工件在[固定 notebook](https://github.com/google-deepmind/alphaevolve_results/blob/9909c1347ea1b28d0c17dcb1f879a1c91b7dec3a/mathematical_results.ipynb)；[README](https://github.com/google-deepmind/alphaevolve_results/blob/9909c1347ea1b28d0c17dcb1f879a1c91b7dec3a/README.md)明确说明**不含运行 AlphaEvolve 的代码**。许可：README 说软件 Apache-2.0、其他材料 CC BY 4.0；[LICENSE](https://github.com/google-deepmind/alphaevolve_results/blob/9909c1347ea1b28d0c17dcb1f879a1c91b7dec3a/LICENSE)有 Apache-2.0 文本。这是**结果仓库**的许可来源，不代表内部 harness 获许可。
4. 原始提示、模型调用比例、内部搜索代码/数据库、完整候选及失败记录、4×4 运行配置、墙钟时间、GPU/TPU 用量、美元成本、人工中途干预和具体停止条件均未在所读材料取得。不可据公开数学证书推断这些量。

本次取证全程为公开来源、只读。未保存 PDF，因此无 PDF SHA-256；读 HTML 对机制足够，数学工件另有固定 notebook 字节 hash。后续重点更新触发：官方释放搜索代码/配置，或公开本案例的逐轮日志与成本。对 ODE / 动力系统仅作适用前提分析，本批未找到经核实的该方向 AlphaEvolve 成果。
