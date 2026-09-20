---
id: "event-2026-01-26-erdos-728-aristotle"
title: "Erdős #728：非形式推理与 Aristotle Lean 证明工件"
event_date: "2026-01-26"
retrieved_at: "2026-09-20"
area: ["number-theory", "formalization"]
event_type: "mathematical-writeup-version"
source_claim: "论文v5给出阶乘整除的双侧对数窗与无限多解；公开Lean工件与最强论文表述还需对应核验。"
mathematical_status: "UNASSESSED"
evidence_level: "PRIMARY-SOURCE-CHECKED"
source_reading_status: "section-summary"
ai_roles: ["informal-proof", "formalization"]
human_roles: ["problem-input", "scope-clarification", "writeup"]
autonomy_evidence: "WORKFLOW-DOCUMENTED"
primary_sources: ["https://arxiv.org/abs/2601.07421v5", "https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/v4.24.0/ErdosProblems/Erdos728b.lean"]
system_records: ["systems/aristotle-harmonic.md"]
score_math_importance: 2
score_ai_centrality: 3
score_source_strength: 2
score_mechanism_auditability: 1
signal_score: 8
dossier: "dossiers/2026-erdos-728-aristotle.md"
---

# Erdős #728：非形式推理与 Aristotle Lean 证明工件

论文v5给出阶乘整除的双侧对数窗与无限多解；公开Lean工件与最强论文表述还需对应核验。

本卡记录已核查的公开来源与研究流程，不把作者声明直接提升为本项目已证明结论。完整的对象、参数、AI与人的贡献、来源定位和验证边界见[案例深读](../../dossiers/2026-erdos-728-aristotle.md)；架构与复用条件见[系统档案](../../systems/aristotle-harmonic.md)。

事件日期取数学论文v5修订日，不是原发现日。顶层Lean声明与完整Theorem 1之间存在需补核的量词及边界差异；未运行Lean。UNASSESSED不意味着学界问题仍未解决。
