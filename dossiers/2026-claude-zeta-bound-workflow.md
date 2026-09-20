---
case_id: "case-2026-claude-zeta-bound-workflow"
title: "Claude ζ 零点比例结果：多 agent 发现与形式化工作流审计"
record_updated: "2026-08-24"
event: "events/2026/2026-08-10-claude-zeta-bound.md"
systems: ["systems/claude-research-multiagent-2026.md"]
mathematical_status: "OPEN"
workflow_status: "WORKFLOW-DOCUMENTED / FORMAL-OUTPUT-CHECKABLE / DISCOVERY-NOT-REPRODUCIBLE"
---

# Claude ζ 零点比例结果：多 agent 发现与形式化工作流审计

## 分层判断

- **数学结论**：`OPEN`。论文声称无条件下界，并有公开、固定版本的 Lean formalization；本项目尚未运行 proof replay 或检查 formal statement 与论文命题的全部语义接口。
- **AI 贡献**：来源报告 Claude 从一个更大的失败目标中提出关键 rank--trace 路线并完成证明搜索，公开过程统计显著强于普通 AI disclosure。
- **人类贡献**：人给出 RH 挑战与第二轮继续指令；Anthropic 数学家检查、理解、验证并以作者身份表述；另有人协作形式化，外部专家短时检查。
- **复现**：formal output 较可复核，discovery 不可复跑。未发布模型与 orchestration 缺失阻止 `REPRODUCIBLE`。
- **准确表述**：这是 RH 邻近的无条件比例下界，不是 Riemann hypothesis 的证明。

## 准确的数学目标

令 (N(T_1,T_2)) 计数 critical strip 内高度区间中的 zeta zeros（按重数），并令 (N_0^s) 计数临界线上的单零点。论文声称：

- dyadic 与 cumulative 形式的 (liminf N_0^s/N \ge 2/3)；
- distinct zeros 比例至少 (5/6)；
- Montgomery--Taylor 最优窗口给出约 (0.67250) 与 (0.83625)；
- primitive Dirichlet characters 对应的 (L(s,\chi)) 有类似结论。

公开 Lean README 把这些组织为 Theorems A--E，并说明 definitions 直接基于 Mathlib 的 `riemannZeta`、`analyticOrderAt` 等对象。后续审计需要逐一定义核对，不能只看 decimal constants。

## 研究时间线

1. Jarred Sumner 用自然语言要求未发布 Claude 研究版本“take a real stab” at RH。
2. 第一轮 Claude Code session 产生约 650 个想法，没有成功。
3. 人类要求再试，并主要提供鼓励性短消息。
4. 第二轮约一天半，coordinator 调度约 60 个 subagents；两名 agents 发展关键数学思想，其他 agents 贡献、失败、验证或写作。
5. agents 运行数值检查、搜索反例、下载 54 篇 arXiv papers 检查 prior art，并从头独立重证。
6. Claude 主动建议写成 paper，并建议由人类 number theorist 验证。
7. Levent Alpöge 与 Ralph Furman 检查、理解并表述结果；Brian Conrey 与 Dan Goldston短时 examined paper。
8. Claude 与 Eric Easley 并行生成 Lean formalization，并以 Comparator 检查接口发布。
9. 论文 v1 于 2026-08-13 提交，v2 于 2026-08-19 更新。

## 系统配置

- interface：Claude Code；
- model：unreleased research version of Claude，准确 checkpoint 未公开；
- sessions：2；
- output budget：总计 31M output tokens；
- first search：约 650 failed ideas；
- second search：约 1.5 days、约 60 subagents；
- tool activity：2,400 shell commands、数百 Python scripts；
- literature lane：下载 54 篇 arXiv papers；
- role accounting：2 key-math、13 idea contributors、30 unsuccessful idea agents、13 validators、2 initial paper writers；
- human prompt activity：公开概述为初始挑战、再试和鼓励；完整 system/user transcripts 尚未在本项目做逐条 intake；
- formalization：Lean 4.33.0-rc2，Mathlib commit `51e6992efd06126df61a496bebf8f49482a4e129`，仓库声称 Theorems A--E `sorry`-free；
- verification commands：build headline modules、print axioms、Comparator replay。

## AI完成的工作

按来源报告，AI 贡献覆盖：

- 探索 RH 与邻近路线，生成大量候选；
- 识别将 Aryan、Baluyot--Goldston--Suriajaya--Turnage-Butterbaugh 与 Bombieri 输入结合的方向；
- 提出在 Weil Hermitian form 上使用 rank--trace inequality，并用 inertia 处理 off-line pairs 的关键组织；
- 展开 analytic inputs 与 finite-compression argument；
- 写脚本做数值筛查；
- 搜索反例、互审、prior-art check 和 independent re-proof；
- 生成初始 paper，并建议 human expert validation；
- 与人协作 formalize Theorems A--E。

“自主发现”是论文和官方页面的 attribution。由于基础模型与完整调度记录未开放，本项目将其定为 `WORKFLOW-DOCUMENTED`，而不是 `INDEPENDENTLY-AUDITED`。

## 人的参与

- 选择著名开放问题作为起点；
- 在第一轮失败后决定继续，并发送鼓励性提示；
- Alpöge 与 Furman 进行领域数学检查、理解前人工作接口、修订和最终表述；
- Easley 与 Claude 共同完成 formalization；
- Conrey 与 Goldston短时间检查论文；
- 人类作者承担对发表命题与论证的责任。

“人只说了鼓励”只描述 discovery session 中 Jarred 的报告角色，不应抹去后续数学验证、写作、形式化协作和发布责任。

## 研究机制重建

```text
ambitious target (RH)
  → wide idea generation
  → 650-route failure signal
  → human authorizes deeper second attempt
  → coordinator allocates heterogeneous subagent roles
      ├─ derive key linear-algebra mechanism
      ├─ connect analytic-number-theory inputs
      ├─ run numerical falsification
      ├─ search prior art and counterexamples
      └─ independently re-prove surviving route
  → result is narrowed from RH to an unconditional proportion theorem
  → AI paper draft + explicit request for expert validation
  → human domain validation and communication
  → separate Lean formalization with fixed statements
  → kernel/axiom/Comparator checks
```

关键机制不是“鼓励 prompt”本身，而是系统允许在大目标失败后保留邻近结果、把 idea generation 与 adversarial validation 分工，并用外部数学软件和文献检索降低长程 hallucination 风险。

## 复现条件核查

### 已公开材料

- official process narrative with role counts and compute scale；
- arXiv v2 paper and provenance statement；
- formal Lean repository, frozen toolchain/Mathlib commit；
- trusted challenge definitions、solution、build、axiom audit 与 Comparator commands；
- 官方页面链接的 detailed transcripts（本项目未逐条归档或 proof-grade 转录）。

### 重做发现过程仍缺少的材料

- exact model checkpoint and API；
- system prompt、subagent templates、scheduler、shared state 与 compaction；
- 完整 machine-readable messages 和 tool outputs；
- budget allocation、stop criteria 与人工操作的完整时间线；
- 等 token 单 agent 或更小 swarm 对照。

结论：第三方可以尝试复核形式证明，但不能在相同系统上从 RH prompt 复现发现过程。

## 数学证据核查

当前支持：

- arXiv v2 明确声明 unconditional theorem、常数与 AI provenance；
- formal repository 明确列出 Theorems A--E、definitions、toolchain 和 axiom audit 预期；
- formal artifact 覆盖 headline results 的声明比普通“代码即将发布”更强。

仍未完成：

- 本项目本地 build 与 Comparator replay；
- `ChallengeDeps.lean` definitions 与 paper definitions 的逐项语义核对；
- rank--trace interface 和 analytic inputs 的 faithful excerpt/assumption check；
- 独立专家公开、可引用的完整 verification report；
- 正式同行评审。

因此保持 `PRIMARY-SOURCE-CHECKED / OPEN`。如果未来完成本地形式重放，也只会先提高 formal-artifact 证据，不自动完成 novelty 与 mathematical-meaning 审查。

## 可学习的方法

1. 允许从失败的大目标中提取精确、较小但新颖的 theorem；
2. 给 agents 明确区分 generator、validator、prior-art searcher 和 writer；
3. 把数值检查用于 falsification，避免作为 proof acceptance；
4. 要求幸存路线被另一组 agents 从头重证；
5. 在发布前触发 human-domain-expert gate 与 formal-kernel gate；
6. 发布固定 toolchain 和 trusted statement，让第三方能检查输出。

目前没有证据支持把“鼓励语”当作关键机制，也没有受控实验支持 60-agent 拓扑优于其他预算分配。

## 未解决问题与更新条件

- 第三方公开 build/Comparator/semantic audit；
- arXiv v3、勘误、referee report 或期刊发表；
- Anthropic 发布准确模型或可复用 research harness；
- detailed transcripts 被独立分析并形成可核查 intervention timeline；
- 受控比较 single-agent、multiagent、tool/no-tool 与不同 validation layers；
- 领域专家确认关键新意、历史归属和全部 analytic inputs。

## 原始来源

- [Anthropic methodology report](https://www.anthropic.com/research/riemann-zeta)，检索于 2026-08-24。
- [Alpöge--Furman, arXiv:2608.13637v2](https://arxiv.org/abs/2608.13637)，检索于 2026-08-24。
- [Zeta23 Lean repository](https://github.com/anthropics/zeta-23-lean)，检索于 2026-08-24。
