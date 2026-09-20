# Albilich 扩充来源收据（2026-09-20）

## 范围与读取层级

本批只考察 Albilich 的公开系统机制和 Kourovka 21.142 案例。发现路线：复用 [原候选目录](../../CANDIDATES.md)的 Albilich 条目，直接读系统论文与官方代码；以 `"Kourovka" "21.142" invariably generated alternating group 2026`、`"Albilich" "21.142" proof group theory independent`、`"Kourovka Notebook" "21.142" Zalesskii original` 作一次有界补检，找到作者单独的群论数学论文。搜索结果仅作 locator，结论据下列原文。未搜索全部被引或引用者；“未找到独立复核”只指这次已查集合，不能推断不存在。

访问方式：arXiv 开放 HTML、GitHub 官方仓库与固定 raw 文件。未触发机构认证。未保存 PDF 或代码快照，未运行仓库代码、CAS 或 harness；因此本批没有本地 PDF SHA-256 或系统 replay。阅读深度为 `section-summary` 加若干局部证明逐段阅读，**未达到**整篇数学证明的 `assumptions-checked` 或项目 `PROVED` 验收。

## 已读的一手来源

|编号|版本与 URL|实际读取位置|所支持的范围|
|---|---|---|---|
|A1|[系统论文 arXiv:2607.27705v1](https://arxiv.org/html/2607.27705v1)，2026-07-30|§1 Terminology、§2、§3 Proof-State Architecture（式 (1)–(3)、角色表、局部/集成验证、撤销、调度、MCP），§4 实验表和 Kourovka、§5 Limitations|架构语义、作者实验报告、验证边界；论文不是外部数学审稿|
|A2|[作者数学论文 arXiv:2608.00703v1](https://arxiv.org/html/2608.00703v1)，2026-08-01|摘要、§1 Theorem 1.1 与 AI 声明、§2 Def. 2.1/Lemmas 2.2/2.3/2.5、§3 Lemma 3.1/Prop. 3.3/Lemma 3.7/Props. 3.12–3.14/Remark 3.15、§4 Theorem 4.1 及证明|最终公开数学命题、作者修订后的证明路线；未逐一检查其外引原文与所有高秩分支|
|A3|[官方代码仓库固定快照](https://github.com/uw-math-ai/albilich/tree/36c648cb3bc8d550fbe5c4035f177ef4c0a5f1c7)，commit `36c648cb3bc8d550fbe5c4035f177ef4c0a5f1c7`，提交日期 2026-09-07|README 的 Current release、Experiment data policy、Quickstart、Proof state、Roles、The loop；目录树与 `store.py`、`patches.py`、`scheduler.py`、`verification.py`、`integration.py`、`retrieval.py`、`cas_reproduction.py` 函数入口；[LICENSE](https://github.com/uw-math-ai/albilich/blob/36c648cb3bc8d550fbe5c4035f177ef4c0a5f1c7/LICENSE)|当前公开使用接口和状态实现入口；LICENSE 为 Apache-2.0；不能当成 7 月运行的精确代码|
|A4|[21.142 固定实验目录](https://github.com/uw-math-ai/albilich/tree/36c648cb3bc8d550fbe5c4035f177ef4c0a5f1c7/experiments/kourovka/21.142)|`problem.md`、`README.md`、`metrics.json`、`report.md` 的头部/Final Proof/路线与债务；`evidence/` 下选定文件，见下表|原输入、内部结论、资源口径与精选运行工件|
|A5|[AAAI-27 论文数据索引](https://github.com/uw-math-ai/albilich/blob/36c648cb3bc8d550fbe5c4035f177ef4c0a5f1c7/experiments/aaai27-final-paper/README.md)|Supported paper results、Unmatched manuscript values、Integrity|作者仓库自审指出的论文数值与归档不一致|
|A6|[仓库第四轮系统复核](https://github.com/uw-math-ai/albilich/blob/36c648cb3bc8d550fbe5c4035f177ef4c0a5f1c7/docs/fourth_pass_systems_review.md)|2026-09-01 Executive assessment|仓库自身明确其是研究协调器，绿测试不证明非形式化数学正确或一般研究能力|

归档明确说公开的是 prompt、报告、汇总指标和**去重精选**证明/CAS证据；不包括原始 child-session 日志、临时 SQLite 和本地绝对路径。[归档总 README](https://github.com/uw-math-ai/albilich/blob/36c648cb3bc8d550fbe5c4035f177ef4c0a5f1c7/experiments/README.md)。`SHA256SUMS` 为仓库中各公开工件的完整性清单；本项目未下载所有文件并重算，因此不能把清单存在写成“本地全部哈希通过”。

## 21.142 中实际读取的工件

以下均在固定目录 `experiments/kourovka/21.142/evidence/`，文件可由 [证据目录](https://github.com/uw-math-ai/albilich/tree/36c648cb3bc8d550fbe5c4035f177ef4c0a5f1c7/experiments/kourovka/21.142/evidence)定位：

|文件|实际读取的作用|
|---|---|
|[`proof_minimal_host_monolithic_wreath_reduction_rev107.md`](https://github.com/uw-math-ai/albilich/blob/36c648cb3bc8d550fbe5c4035f177ef4c0a5f1c7/experiments/kourovka/21.142/evidence/proof_minimal_host_monolithic_wreath_reduction_rev107.md)|最小宿主、正规子群、唯一 $S^t$、坐标嵌入|
|[`verification_minimal_host_monolithic_wreath_reduction_rev109.md`](https://github.com/uw-math-ai/albilich/blob/36c648cb3bc8d550fbe5c4035f177ef4c0a5f1c7/experiments/kourovka/21.142/evidence/verification_minimal_host_monolithic_wreath_reduction_rev109.md)|内部 reviewer 核上述局部论证，明说不验后续经典群模块|
|[`proof_terminal_cfsg_projective_degree_root_rev128.md`](https://github.com/uw-math-ai/albilich/blob/36c648cb3bc8d550fbe5c4035f177ef4c0a5f1c7/experiments/kourovka/21.142/evidence/proof_terminal_cfsg_projective_degree_root_rev128.md)|分类、射影表示维数、经典群模块并成终端引理|
|[`verification_terminal_simple_factor_exclusion_rev130.md`](https://github.com/uw-math-ai/albilich/blob/36c648cb3bc8d550fbe5c4035f177ef4c0a5f1c7/experiments/kourovka/21.142/evidence/verification_terminal_simple_factor_exclusion_rev130.md)|内部 verifier 的终端引理反馈|
|[`advisor_root_spine_verifier_handoff_rev136.md`](https://github.com/uw-math-ai/albilich/blob/36c648cb3bc8d550fbe5c4035f177ef4c0a5f1c7/experiments/kourovka/21.142/evidence/advisor_root_spine_verifier_handoff_rev136.md)|建议将两前提接成根命题并交 verifier|
|[`verification_root_counterexample_cfsg_terminal_rev149.md`](https://github.com/uw-math-ai/albilich/blob/36c648cb3bc8d550fbe5c4035f177ef4c0a5f1c7/experiments/kourovka/21.142/evidence/verification_root_counterexample_cfsg_terminal_rev149.md)|内部根级推理反馈|

归档 report 的 `Final Proof` 没有外部引用，是因为它把外部群论引用封装在之前已“内部验收”的前提里；不能由“末步没有引用”推出整个证明不依赖外部定理。该报告同时列出 14 个 active blocking debts（注释 `ledger only`）。我们没有完整数据库依赖回放，无法判定这些债务是否影响根路线的真实闭合。[固定 `report.md`](https://github.com/uw-math-ai/albilich/blob/36c648cb3bc8d550fbe5c4035f177ef4c0a5f1c7/experiments/kourovka/21.142/report.md)。

## 版本对应与不能直接继承的结果

1. **运行版本**：`metrics.json` 记录日期 2026-07-14、`gpt-5.6-sol`/`xhigh`、80 runs、29,684,464 gross tokens、revision 156。当前 2026-09 固定 README 默认 `gpt-6-astra`/`xhigh`，架构增添了多项功能，不能说这些新功能促成 7 月成果。报告控制事件出现代码短 SHA `bf52f5d`；对当前公开仓库 GitHub commits API 的精确查询返回 `No commit found`，故运行源码无法按这一短 SHA 唯一固定。
2. **数学稿不是原样输出**：7 月 `report.md` 的主结构是“最小宿主 $S^t$ + 终端单因子排除”；8 月 [数学论文 §2–4](https://arxiv.org/html/2608.00703v1) 改为“组合因子中的交错群截面 + Collins 控制”，并声明人类作者检查修订。不得倒推出最终稿每一行由 Albilich 自主完成。
3. **数值冲突**：[作者库论文数据索引](https://github.com/uw-math-ai/albilich/blob/36c648cb3bc8d550fbe5c4035f177ef4c0a5f1c7/experiments/aaai27-final-paper/README.md)称其所查 40 个 proof-state 数据库和分支历史中未找到 RealMath `no-CAS 9/10` 的归档；17.91 的 CAS-on 数据归档为 **5,250,897** total tokens，系统论文详细表为 **6,784,000** 左右。索引还说 17.91 的 CAS on/off 历史问题提示/搜索设置并不完全匹配。故论文“32% token reduction”不能用现有归档解释成严格的单因素受控效果。两臂均只是 partial，未解根题。
4. **21.142 advisor 对照**：论文 Table 5 的两个 proof state 起点与模型等作者说明相同，但只有一对运行，无 advisor 臂在 operator stop 时没有根结论，且不到完整两倍时间允额。这提供机制探索线索，不是总体成功率估计。

## 后续若要升高证据级别

- 对最终群论定理：先取得 Collins 2008 Theorem A、有限单群分类与所用经典群自同构结果的原文，逐项匹配数学论文 Lemma 3.11、Proposition 3.12、Proposition 3.14 的域特征、小秩例外、截面/表示维数接口；必要时作 faithful excerpt。完成前保持 `UNASSESSED`。
- 对历史流程：取得可公开的原始 child 日志、完整状态数据库/事件和精确运行代码 commit；比较报告中 active debts 与集成证明依赖，核历史人类 steering。缺失不能用当前 README 或精选文件推断。
- 对复用：先读 [系统档案](../../systems/albilich.md)中的版本与权限边界，再读 [案例](../../dossiers/2026-albilich-group-theory.md)；如未来需要隔离试运行，应另有明确授权和独立验收。当前文件只是来源与研究方法说明。
