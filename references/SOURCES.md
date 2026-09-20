# 来源与复用入口

核查日期：2026-09-20。本页回答“以后从哪里拿材料、应使用哪个版本、能复用到哪一层”。链接指向官方材料；历史案例配置与当前实现分列。未安装或执行任何外部 harness。复用之前仍应核对上游更新、许可、模型可用性与所需权限。

## Danus：事实依赖与长期证明状态

- **[最新版全框架教程](../systems/danus/FRAMEWORK-GUIDE.md)** → [版本确认与哈希](notes/2026-09-20-danus-latest-version.md) → [状态/提交/记忆接口](notes/2026-09-20-danus-state-map.md) → [运行/停止/恢复/写作接口](notes/2026-09-20-danus-runtime-map.md)。2026-09-20再查默认分支为codex，HEAD `6d92e8d`（8月27日），与上次快照相同；latest release `v0.1.0`不是最新分支代码。


- [系统论文 2607.06447v2](https://arxiv.org/html/2607.06447v2)、[YTD 案例 2608.19301v1](https://arxiv.org/html/2608.19301v1)：前者解释架构，后者 Appendix A 给运行贡献与配置；两者不是同一次实验。
- [官方仓库](https://github.com/frenzymath/Danus)；[main 固定快照](https://github.com/frenzymath/Danus/tree/1a2cb99f9b16abb6b82d1bda207ed8a822f12743)；[codex 固定快照与 README](https://github.com/frenzymath/Danus/tree/6d92e8d415933ca2ef52fd1a4da73fdfcd418f1c)。复用先按对应分支 README 理解启动入口、模型接口、事实与任务记录，再查看档案的代码定位。
- codex README 把该实现关联到 YTD，但未给出足够信息将原运行完整绑定到一个可重放的历史 commit。不要把目前可下载等同于历史复现。
- [codex LICENSE：Apache-2.0](https://github.com/frenzymath/Danus/blob/6d92e8d415933ca2ef52fd1a4da73fdfcd418f1c/LICENSE)。许可证覆盖范围仍以原文件为准，模型服务另有条款。
- [系统说明](../systems/danus.md) · [数学案例](../dossiers/2026-ytd-disproof-ai-workflow.md) · [源码、版本与查询收据](notes/2026-09-20-danus-source-audit.md)。未知项：完整原始日志、精确运行快照、独立复跑成本。

## ProofCouncil：作者、批评者与多模型意见

- [系统论文 2607.09474v1](https://arxiv.org/html/2607.09474v1)；[当前已查官方代码快照](https://github.com/eth-sri/proof-council/tree/e7e1ea5236585e817a09de0e416a57c6c3013f77)。当前配置包含较新模型，不能解释五月案例的历史运行。
- **复现案例优先入口**：[FirstProof 固定工件仓库](https://github.com/1stproof/batch-2/tree/274625a22e4748d5f9264ba3614353461520bd20)。`batch-2-submissions/improofbench/configs/workflows/author_critic.yaml` 与 `author_critic_long.yaml` 是当时工作流配置；`batch-2-AI-solutions/problem-03/submission-A.tex` 是提交结果；`batch-2-reviews/problem-03/` 是外部审稿；`batch-2-raw-outputs/IMProofBench/WorkflowRuns/` 有过程工件。
- [官方评审报告](https://1stproof.org/assets/docs/report.pdf) §5.3；报告 URL 可变，历史代码链接已固定 commit。[当前代码 LICENSE：MIT](https://github.com/eth-sri/proof-council/blob/e7e1ea5236585e817a09de0e416a57c6c3013f77/LICENSE)；竞赛工件的再分发权限不由另一仓库的许可证自动覆盖。
- [系统说明](../systems/proof-council.md) · [P3 数学案例](../dossiers/2026-proof-council-firstproof.md) · [来源收据与详细路径](notes/2026-09-20-proof-council-source-audit.md)。可学习轮次文件、反馈与终稿对照；模型随机性、所有工具调用的可重放性仍有限。

## Aristotle：自然语言到 Lean 的服务与证书

- [系统论文](https://arxiv.org/abs/2510.01346v2)、[数学论文 2601.07421v5](https://arxiv.org/html/2601.07421v5)。系统论文不是案例运行配置快照；首轮运行使用的内部构建版本未知。
- [官方服务入口](https://aristotle.harmonic.fun)、[客户端 aristotlelib 2.1.0](https://pypi.org/project/aristotlelib/2.1.0/)：公开 Python 客户端不等于公开内部证明搜索系统。已查元数据要求 Python >=3.10；其 license 与 license_expression 均未提供，不能据此推断可任意再分发。
- **证书入口**：[固定 Lean 文件](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/v4.24.0/ErdosProblems/Erdos728b.lean)。该文件说明 Lean 4.24.0、Mathlib `f897ebcf72cd16f89ab4577d0c826cd14afaafc7`；文件 SHA-256 为 `40f4cbf2ccaefa5d84fc44ece63d1e4c3fed3e47b631057ef337fc92465d7b9f`。
- [系统说明](../systems/aristotle-harmonic.md) · [#728 案例与命题对应差异](../dossiers/2026-erdos-728-aristotle.md) · [来源收据](notes/2026-09-20-formal-source-audit.md)。后续复用应先核对准确 theorem statement，再考虑在独立任务中重放 Lean；本轮没有构建或 kernel replay。

## FunSearch：可计算评价引导程序进化

- [官方论文与发布入口](https://deepmind.google/discover/blog/funsearch-making-new-discoveries-in-mathematical-sciences-using-large-language-models/)、[固定官方仓库](https://github.com/google-deepmind/funsearch/tree/cc53f274237d7ab05c19df939edbc1f9616a7c19)。`implementation/funsearch.py` 是协调入口，`sampler.py` 生成候选，`evaluator.py` 评价，`programs_database.py` 管理岛群，`config.py` 给公开默认值。
- `LLM._draw_sample` 和 `Sandbox.run` 是留给使用者实现的接口；下载仓库不等于获得原论文的 Codey 模型与生产隔离环境。cap-set notebook 与 `cap_set/n8_size512.txt` 是最直接的数学工件入口。
- [代码 LICENSE：Apache-2.0](https://github.com/google-deepmind/funsearch/blob/cc53f274237d7ab05c19df939edbc1f9616a7c19/LICENSE)；README 标注其他材料 CC BY 4.0。论文 PDF 是作者接受稿，不按代码许可证推断再分发权限。
- [系统说明](../systems/funsearch.md) · [512-cap 案例](../dossiers/2023-funsearch-capset.md) · [来源收据、PDF 与数据哈希](notes/2026-09-20-funsearch-source-audit.md) · [本项目独立检查脚本](../scripts/check_funsearch_capset.py) · [固定点集](data/funsearch-n8-size512.txt)。脚本只检查有限工件，不运行外部实现。

## 复用时保存什么

每次专题更新记录：原始 URL、访问日期、论文版本、代码 commit、确实读过的位置、配置与产物的对应关系，以及缺失项。保存文件时另记 SHA-256。动态首页仅作为继续查找入口，不能替代已固定的证据。其余候选与阅读深度见[候选目录](../CANDIDATES.md)；本次扩充的固定入口如下。

## QED：证明计划与分层核验

- [系统论文2604.24021v4](https://arxiv.org/html/2604.24021v4)、[数学论文2605.20623v1](https://arxiv.org/html/2605.20623v1)；§2–4分别是不同假设的下界，§5为贡献说明。
- [当前代码121900964e6572aaf094412d434b5ac2a792a65f](https://github.com/proofQED/QED/tree/121900964e6572aaf094412d434b5ac2a792a65f) → README、`config.yaml`、`prompts/decomposition-prover/`、`code/decomposition_prover.py`。MIT许可；配置有高权限示例，未运行。
- [旧P3工件03faa8238aef4710084b117657ec9f0f7e80fe57](https://github.com/proofQED/QED/tree/03faa8238aef4710084b117657ec9f0f7e80fe57/proved_statements/analysis-Apr-24-2026)用于历史案例；当前模型不能倒填旧运行。论文与旧README的verifier型号记载有冲突。
- [系统](../systems/qed.md) · [案例](../dossiers/2026-qed-transport-diffusion.md) · [读取位置与版本差异](notes/2026-09-20-qed-expansion.md)。完整调用日志、确切历史配置仍缺。

## Albilich：状态、证明债务与集成

- [系统论文2607.27705v1](https://arxiv.org/html/2607.27705v1)、[数学论文2608.00703v1](https://arxiv.org/html/2608.00703v1)；后者定理1.1是经人类检查修订后的公开数学稿。
- [代码36c648cb3bc8d550fbe5c4035f177ef4c0a5f1c7](https://github.com/uw-math-ai/albilich/tree/36c648cb3bc8d550fbe5c4035f177ef4c0a5f1c7)，Apache-2.0。入口 README、`agents/generation/phase2/`、`experiments/kourovka/21.142/`；精选证明、审稿和metrics与当前runtime分开。
- 先读[归档自审](https://github.com/uw-math-ai/albilich/blob/36c648cb3bc8d550fbe5c4035f177ef4c0a5f1c7/experiments/aaai27-final-paper/README.md)，不要照引有冲突的CAS对照统计；早期运行commit未完整恢复。
- [系统](../systems/albilich.md) · [案例](../dossiers/2026-albilich-group-theory.md) · [来源收据](notes/2026-09-20-albilich-expansion.md)。可复用状态/集成思路，不宣称已复现原成果。

## AlphaEvolve：程序进化与精确结果工件

- [系统论文2506.13131v1](https://arxiv.org/html/2506.13131v1)，§2为系统、§3.1为矩阵结果、Fig.4为搜索程序改写线索。
- [论文相邻结果快照9909c1347ea1b28d0c17dcb1f879a1c91b7dec3a](https://github.com/google-deepmind/alphaevolve_results/tree/9909c1347ea1b28d0c17dcb1f879a1c91b7dec3a)：`mathematical_results.ipynb`零基cell36数据、cell4验证器。README明确不提供运行AlphaEvolve的代码；软件Apache-2.0、其他材料CC BY4.0。
- [当前结果快照4226acbf237ff9ad10ba7673a2af127a2d8a5971](https://github.com/google-deepmind/alphaevolve_results/tree/4226acbf237ff9ad10ba7673a2af127a2d8a5971)与前者notebook不同，案例核验固定前者。
- [系统](../systems/alphaevolve.md) · [案例](../dossiers/2025-alphaevolve-matrix-multiplication.md) · [SHA-256与读取记录](notes/2026-09-20-alphaevolve-expansion.md) · [本项目精确整数检查](../scripts/check_alphaevolve_rank48.py)。仅解析数据并核恒等式，不运行外部notebook；完整搜索、成本、prompts与历史日志未公开。

## ★ 符号 Lyapunov

- [论文2410.08304v1](https://arxiv.org/html/2410.08304v1)，§4数据生成、§5实验、附录F真实输出；[官方代码ce72b4ccbbe3fc00ee869c88b64a293381965a0b](https://github.com/facebookresearch/Lyapunov/tree/ce72b4ccbbe3fc00ee869c88b64a293381965a0b)。CC BY-NC4.0；仓库已归档。
- 从README/配置进入 `src/envs/ode.py` 的生成与 `check_lyap_validity`，对照有限盒、SOS、SHGO及返回码。论文模型与公开训练配置有差异，不能据下载源码声称历史权重和搜索已恢复。
- [系统](../systems/symbolic-lyapunov.md) · [案例](../dossiers/2024-symbolic-lyapunov-planar.md) · [源码位置与阅读范围](notes/2026-09-20-dynamics-source-audit.md)。具体函数可手算验证，整个实验集未验收。

## ◇ PINN 奇性发现与动力系统补充来源

- [奇性论文2509.14185v1](https://arxiv.org/html/2509.14185v1)和[后续2511.22819v1](https://arxiv.org/html/2511.22819v1)分别引用；后续梯度归一化不能解释早期运行。已查集合未取得可绑定原案例的官方完整runtime、权重及日志，社区复刻不替代官方入口。
- [系统](../systems/pinn-singularity-discovery.md) · [数值案例](../dossiers/2025-pinn-unstable-singularities.md) · [来源收据](notes/2026-09-20-dynamics-source-audit.md)。公开数学/方法描述可学习，严格爆破验证和完整复现未完成。
- **◇高价值来源剖面**：[fluid_lean@d0124689230b58b4f86e7b90ac59de06404b3b6b](https://github.com/tristanbuckmaster/fluid_lean/tree/d0124689230b58b4f86e7b90ac59de06404b3b6b) → Boussinesq/Euler目录README、`formalization.yaml`、`Challenge.lean`、`Solution.lean`。Apache-2.0；版本、作者PDF字节哈希和命题对应差异见[来源收据](notes/2026-09-20-fluid-lean-source-audit.md)，解释见[剖面](../dossiers/2026-fluid-lean-source-profile.md)。未进行Lean构建；没有据公开证明工程重建未知agent流程。

质量复评后的排除/暂缓来源仅留在[判断记录](notes/2026-09-20-dynamics-adjudication.md)，不作为复用推荐。符号Lyapunov补核NeurIPS正式稿并保留方法档案；RL与AI Poincaré的出处及排除理由见该记录。

## QED 完整框架学习入口（2026-09-20）

[中文全框架教程](../systems/qed/FRAMEWORK-GUIDE.md)以固定 commit 的源码为依据；[控制流定位](notes/2026-09-20-qed-control-map.md)与[模型/提示词接口定位](notes/2026-09-20-qed-interface-map.md)提供官方链接、函数及行号。此次仅静态阅读 harness，不执行外部程序、不读取生成数学论文作证明审查。
