---
id: "event-2026-08-10-claude-zeta-bound"
title: "Claude 研究运行发现 ζ 零点临界线与单零点比例的新下界"
event_date: "2026-08-10"
retrieved_at: "2026-08-24"
area: ["number-theory", "analytic-number-theory", "AI-assisted-mathematics", "formalization"]
event_type: "ai-discovered-theorem-claim"
source_claim: "Anthropic 与论文作者声称，一个未发布的 Claude 研究版本在尝试 Riemann hypothesis 时自主发现：至少三分之二的 Riemann zeta 非平凡零点是位于临界线上的单零点，至少六分之五互异；最优窗口给出 0.6725 与 0.8362，并推广到 primitive Dirichlet L-functions。"
mathematical_status: "OPEN"
evidence_level: "PRIMARY-SOURCE-CHECKED"
source_reading_status: "section-summary"
ai_roles: ["open-problem-exploration", "idea-generation", "proof-generation", "counterexample-search", "literature-search", "numerical-checking", "peer-review", "paper-drafting", "formalization"]
human_roles: ["initial-problem-prompt", "encouragement", "mathematical-validation", "formalization-collaboration", "paper-authorship", "final-responsibility"]
autonomy_evidence: "WORKFLOW-DOCUMENTED"
primary_sources: ["https://www.anthropic.com/research/riemann-zeta", "https://arxiv.org/abs/2608.13637", "https://github.com/anthropics/zeta-23-lean"]
system_records: ["systems/claude-research-multiagent-2026.md"]
score_math_importance: 3
score_ai_centrality: 3
score_source_strength: 2
score_mechanism_auditability: 2
signal_score: 10
dossier: "dossiers/2026-claude-zeta-bound-workflow.md"
---

# Claude 研究运行发现 ζ 零点临界线与单零点比例的新下界

## 事件内容

Anthropic 于 2026-08-10 报告，一个未发布的 Claude 研究版本在被要求“认真尝试”Riemann hypothesis 后没有解决 RH，却在相关的零点比例问题上找到新论证。论文于 2026-08-13 提交 arXiv，2026-08-19 更新到 v2；公开仓库提供对应 Lean 4 formalization。

这不是“Claude 证明了 Riemann hypothesis”。来源明确说 RH 仍未解决，结果是一个无条件的比例下界及其 Dirichlet (L)-function 推广。

## 准确主张与范围

论文摘要声称无条件证明：

- 至少 (2/3) 的 Riemann zeta 非平凡零点（按重数计）是位于临界线上的单零点；
- 至少 (5/6) 的零点互异；
- 使用 Montgomery--Taylor window 时常数分别提高到约 (0.6725) 与 (0.8362)；
- 对 primitive Dirichlet (L)-functions 有相应推广。

论文把关键机制概括为：在 Weil Hermitian form 的有限压缩上使用 rank--trace inequality，并借助 Sylvester's law of inertia 处理临界线外成对零点，从而使早期需要 RH 的论证无条件化。

## AI与人的贡献

按公开过程说明：

- Jarred Sumner 给出初始 RH 挑战，第一轮约 650 个想法全部失败；
- 第二轮运行约一天半，约 60 个 Claude subagents 产生和筛选路线；
- agents 运行 2,400 个 shell commands、编写数百个 Python scripts，并以数值检查、互审、反例搜索、54 篇 arXiv 文献检查和独立重证测试结果；
- 两个 subagents 被报告为关键数学思想的主要来源，13 个贡献想法，30 个未发展出新想法，13 个做验证，2 个帮助初稿写作；
- Levent Alpöge 与 Ralph Furman 检查、理解、验证并以作者身份表述结果；Eric Easley 与 Claude 协作完成 Lean formalization；Brian Conrey 与 Dan Goldston在短时间内检查论文。

模型协调细节、准确版本和完整 scheduler 未公开，因此这些角色分配仍是来源方的工作流披露。

## 证据评估

- `mathematical_status = OPEN`：有较强的公开 Lean 工件和人类检查，但本项目没有运行 kernel replay、检查 statement equivalence 或独立核对决定性 analytic inputs。
- `evidence_level = PRIMARY-SOURCE-CHECKED`：已读取官方方法说明、arXiv v2 元数据与 formalization 仓库说明。
- `source_reading_status = section-summary`：尚未对 21 页证明和 Lean declarations 建立 faithful excerpts。
- `autonomy_evidence = WORKFLOW-DOCUMENTED`：公开了 prompt 概要、两轮时间线、token/agent/command 规模和角色统计；基础模型未发布，不能标记为 `REPRODUCIBLE`。

## 已查阅来源

- [Anthropic methodology report](https://www.anthropic.com/research/riemann-zeta)，发布于 2026-08-10，更新于 2026-08-13，检索于 2026-08-24。
- [Alpöge--Furman, arXiv:2608.13637v2](https://arxiv.org/abs/2608.13637)，v1 提交于 2026-08-13，v2 更新于 2026-08-19。
- [Zeta23 Lean repository](https://github.com/anthropics/zeta-23-lean)，核对 theorem coverage、固定 toolchain 与检查命令，检索于 2026-08-24。

## 未解决问题

- 独立团队能否从仓库的 frozen toolchain 完成 build、axiom audit 和 Comparator replay？
- paper statements、Lean statements 和所有 analytic definitions 是否由独立领域专家确认语义一致？
- 未发布 Claude 的准确版本、system prompt、subagent orchestration 和全部 transcripts 是否足以重跑？
- 论文是否会出现数学勘误、独立 referee report 或正式发表版本？
