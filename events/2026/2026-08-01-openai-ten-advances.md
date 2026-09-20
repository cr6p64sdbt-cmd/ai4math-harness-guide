---
id: "event-2026-08-01-openai-ten-advances"
title: "OpenAI 发布 Astra 生成的十项数学与理论计算机科学结果"
event_date: "2026-08-01"
retrieved_at: "2026-08-24"
area: ["AI-assisted-mathematics", "formalization", "theoretical-computer-science", "discrete-mathematics"]
event_type: "multi-result-research-release"
source_claim: "OpenAI 声称一个内部版本的 Astra 生成了十项开放问题的数学论证，随后由人类借助同一模型整理成稿，并由模型为每项结果生成 Lean certificate。"
mathematical_status: "OPEN"
evidence_level: "PRIMARY-SOURCE-CHECKED"
source_reading_status: "section-summary"
ai_roles: ["open-problem-solving", "proof-generation", "formalization", "reasoning-narration", "paper-drafting-assistance"]
human_roles: ["result-selection", "manuscript-preparation", "formalization-assistance", "publication", "final-responsibility"]
autonomy_evidence: "WORKFLOW-DOCUMENTED"
primary_sources: ["https://openai.com/index/ten-advances-in-mathematics/", "https://cdn.openai.com/pdf/ten-proofs-oai.pdf", "https://cdn.openai.com/pdf/reasoning-walkthroughs.pdf", "https://github.com/openai/ten-proofs", "https://arxiv.org/abs/2608.14673"]
system_records: ["systems/openai-astra-internal-2026.md"]
score_math_importance: 3
score_ai_centrality: 3
score_source_strength: 2
score_mechanism_auditability: 2
signal_score: 10
dossier: "dossiers/2026-openai-ten-advances-workflow.md"
---

# OpenAI 发布 Astra 生成的十项数学与理论计算机科学结果

## 事件内容

OpenAI 于 2026-08-01 发布一份组合论文，汇集十项横跨高维球堆积、编码理论、群论、算子代数、算术电路、量子复杂性、格问题、Ehrhart 体积、Ramsey 数与极值图论的结果。官方说明把数学论证归给内部版本 Astra，把成稿、形式化协助和最终责任归给人类团队与模型的后续协作。

本事件卡记录的是一次具有十个数学子声明的发布，不把十项结果压缩成一个已经被本项目证明的总体命题。

## 准确主张与范围

官方页面称十项结果分别解决或推进长期开放问题，并称每一项都有 Lean certificate。组合论文在本次检查时标为 2026-08-06 更新版；本项目没有逐章核对十项 theorem statement、全部引用假设及其 Lean statement 是否完全等价。

其中第六章关于量子 parallel repetition 的一条 greedy conditioning lemma 随后出现公开纠错：纠错作者指出打印证明中的 continuation test 把 success/failure 的方向写反，给出局部修复，并明确说该修复不构成对主定理的独立验证。因而不能从“修复是局部的”推出整章主定理已获独立确认。

## AI与人的贡献

按 OpenAI 的公开说明：

- Astra 内部版本生成数学论证；
- 人类使用同一模型把论证整理成 manuscripts；
- 模型为每项论证生成 Lean certificates；
- 另一个模型把原始探索过程重构为 reasoning walkthroughs；
- 人类团队帮助成稿与形式化，并承担正确性责任。

公开材料没有给出完整 prompt、逐问题运行日志、候选失败路线、worker 配置或人工逐次干预记录，因此“论证完全由 AI 生成”目前仍属于来源方的过程声明，而不是独立审计结论。

## 证据评估

- `mathematical_status = OPEN`：十项结果不能因组合论文、官方声明或 Lean 仓库的存在而整体提升为 `PROVED`；本项目尚未逐项锁定 statement、依赖和证明对应关系。
- `evidence_level = PRIMARY-SOURCE-CHECKED`：已核对官方发布、组合论文、reasoning walkthroughs、Lean 仓库和独立纠错预印本。
- `source_reading_status = section-summary`：完成发布说明和工件结构级核查，未做十章 proof-grade 阅读。
- `autonomy_evidence = WORKFLOW-DOCUMENTED`：已公开模型名、粗粒度阶段、token 成本估算和证明工件，但缺少足以重跑发现过程的版本与日志。

## 已查阅来源

- [OpenAI official release](https://openai.com/index/ten-advances-in-mathematics/)，发布于 2026-08-01，检索于 2026-08-24。
- [Ten Advances bundled paper](https://cdn.openai.com/pdf/ten-proofs-oai.pdf)，本次取得的文件标注更新于 2026-08-06，检索于 2026-08-24。
- [Reasoning walkthroughs](https://cdn.openai.com/pdf/reasoning-walkthroughs.pdf)，作为模型重构的可读叙述检查，不当作原始运行日志。
- [OpenAI Lean certificates repository](https://github.com/openai/ten-proofs)，用于核对十项 formalization 与构建入口。
- [Correction to the greedy conditioning lemma, arXiv:2608.14673v1](https://arxiv.org/abs/2608.14673)，提交于 2026-08-03。

## 未解决问题

- 十项 paper statements 与 Lean challenge statements 是否逐项语义等价，外部依赖是否完整？
- 2026-08-06 组合论文更新与 2026-08-03 纠错之间的准确版本关系是什么？
- Astra 的冻结版本、system prompt、问题分配、运行日志和失败路线是否会公开？
- 是否会出现逐项独立专家验证、第三方 kernel replay 或正式同行评审？
