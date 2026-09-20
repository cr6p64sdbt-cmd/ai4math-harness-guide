---
id: "event-2026-08-19-ytd-disproof-claim"
title: "预印本声称证伪 cscK 版本的 Yau–Tian–Donaldson 猜想"
event_date: "2026-08-19"
retrieved_at: "2026-09-20"
area: ["differential-geometry", "algebraic-geometry", "AI-assisted-mathematics"]
event_type: "preprint-disproof-claim"
source_claim: "作者构造一个 K-polystable 但不存在常标量曲率 Kähler 度量的极化光滑射影五维簇，并据此声称证伪一般 cscK 版本的 Yau–Tian–Donaldson 猜想。"
mathematical_status: "OPEN"
evidence_level: "PRIMARY-SOURCE-CHECKED"
source_reading_status: "section-summary"
ai_roles: ["open-problem-exploration", "counterexample-construction", "proof-search", "claim-verification", "paper-drafting"]
human_roles: ["problem-selection", "strategic-redirection", "presentation-discussion", "final-polishing", "final-responsibility"]
autonomy_evidence: "WORKFLOW-DOCUMENTED"
primary_sources: ["https://arxiv.org/abs/2608.19301", "https://arxiv.org/html/2608.19301v1", "https://arxiv.org/abs/2607.06447", "https://github.com/frenzymath/Danus"]
system_records: ["systems/danus.md"]
score_math_importance: 3
score_ai_centrality: 3
score_source_strength: 2
score_mechanism_auditability: 2
signal_score: 10
dossier: "dossiers/2026-ytd-disproof-ai-workflow.md"
---

# 预印本声称证伪 cscK 版本的 Yau–Tian–Donaldson 猜想

## 事件内容

Jihao Liu 于 2026-08-19 提交 arXiv v1。摘要称构造了一个极化光滑射影五维簇，它是 K-polystable，但不存在 constant scalar curvature Kähler（cscK）metric。论文把这称为对一般 cscK Yau–Tian–Donaldson 猜想的反例。

本事件卡记录的是“预印本及其 AI 使用附录已经提出该结论”，不是本项目对 79 页数学证明的独立认可。

## 准确主张与范围

- 对象：一个极化光滑射影五维簇；
- 声称的稳定性：K-polystable；
- 声称的分析性质：不存在 cscK metric；
- 作者结论：一般 cscK 对应的充分性方向失败。

这里不把所有同名 YTD 定理或特殊情形合并处理。任何“YTD 整体已经被证伪”的表述都必须附带具体 formulation 和对象范围。

## AI与人的贡献

论文附录报告了两个不同阶段：

1. Claude Code（Fable 5）、Codex（GPT-5.6-sol）和 Danus 协作产生反例与证明；作者在识别一个候选可能击中两个不同猜想时提供了关键聚焦指令。
2. 改进版 Danus 随后只接收原始问题、不接收早期发现，作者报告其在 5 小时 29 分钟后独立得到反例和完整证明。

论文正文之后由作者与 Danus 多轮讨论表达，最后经过人工润色和检查。上述贡献分配来自作者附录，尚不是独立审计结论。

## 证据评估

- `mathematical_status = OPEN`：已经核对 arXiv v1 的准确声明和 AI 附录，但没有完成关键定理、引用和 79 页证明的独立数学核查。
- `evidence_level = PRIMARY-SOURCE-CHECKED`：使用的是论文、系统论文和官方代码仓库，而不是新闻摘要。
- `source_reading_status = section-summary`：已针对摘要和 Appendix A 进行章节级阅读，尚未建立 proof-grade faithful excerpts。
- `autonomy_evidence = WORKFLOW-DOCUMENTED`：附录提供运行阶段、模型和部分统计；相关 codex 分支实现现已公开，但精确历史运行快照与完整工件未闭合，不能标记为 `REPRODUCIBLE`。

## 已查阅来源

- [YTD preprint arXiv record, v1](https://arxiv.org/abs/2608.19301)，提交日期 2026-08-19，检索于 2026-08-24。
- [YTD preprint HTML, Appendix A](https://arxiv.org/html/2608.19301v1)，重点检查 AI 使用报告，检索于 2026-08-24。
- [Danus paper, arXiv:2607.06447v2](https://arxiv.org/abs/2607.06447)，用于核对公开版架构。
- [Danus official repository](https://github.com/frenzymath/Danus)，用于核对公开实现和运行边界。

## 未解决问题

- 论文的 K-polystability 与不存在 cscK metric 两个主链条是否经独立领域专家逐项验证？
- 公开 codex 分支如何与案例的确切运行 commit、配置、完整日志、fact graph 和 verifier 记录对应？
- 5 小时 29 分钟重跑是否能由独立团队在冻结版本上复现？
- 后续 arXiv 版本、正式同行评审或勘误是否改变命题范围和证明？

## 2026-09-20 更新

[固定 codex README](https://github.com/frenzymath/Danus/blob/6d92e8d415933ca2ef52fd1a4da73fdfcd418f1c/README.md) 将该分支关联到 YTD；旧“尚未公开”判断撤回。历史运行仍未独立复现。此次进一步读取数学对象、关键命题依赖与附录，定位见[来源复查收据](../../references/notes/2026-09-20-danus-source-audit.md)。原运行的8个证明workers及616/924统计，不得与fresh run的3个探索subagents混写。
