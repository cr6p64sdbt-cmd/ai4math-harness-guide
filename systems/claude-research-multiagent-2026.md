---
system_id: "claude-research-multiagent-2026"
name: "Claude research multiagent workflow (zeta run, 2026)"
record_updated: "2026-08-24"
versions_checked: ["unreleased research Claude described 2026-08-10", "zeta-23-lean main retrieved 2026-08-24"]
primary_sources: ["https://www.anthropic.com/research/riemann-zeta", "https://arxiv.org/abs/2608.13637", "https://github.com/anthropics/zeta-23-lean"]
reproducibility: "WORKFLOW-DISCLOSED / MODEL-PRIVATE / FORMAL-ARTIFACT-PUBLIC"
---

# Claude research multiagent workflow（ζ 运行，2026）

## 系统概述

这是对一次具体 Claude Code 长程研究运行的系统记录：一个未发布的 Claude 研究版本协调约 60 个同类 subagents，结合 shell、Python、文献下载、数值检查、互审与独立重证寻找数学结果。它没有公开为一个可复用产品，因此本档案不把这次案例特有的拓扑泛化为“Claude 的固定架构”。

## 版本对应

| 记录 | 版本与工件 | 状态 |
|---|---|---|
| Anthropic report，2026-08-10/13 | 未发布 research version of Claude；两次 Claude Code sessions；31M output tokens | 工作流披露，模型不可得 |
| arXiv:2608.13637v2，2026-08-19 | 人类作者验证和表述的 21 页论文 | 原始论文可得 |
| `anthropics/zeta-23-lean`，检索于 2026-08-24 | Lean 4.33.0-rc2，固定 Mathlib commit，Theorems A--E 与 Comparator interface | 形式工件可构建；本项目未运行 |

不得把后续公开 Claude 产品的能力、prompt 行为或工具默认值倒填到这次未发布研究版本。

## 架构与数据流

按官方过程报告，可以重建为：

```text
human prompt: take a real stab at RH
        ↓
Claude Code session 1: ~650 ideas → no successful route
        ↓ human: try again / encouragement
Claude Code session 2: coordinating ~60 subagents
        ├─ key-idea agents
        ├─ contributing idea agents
        ├─ failed exploration agents
        ├─ validator agents
        └─ paper-writing agents
        ↓
shell + Python numerical experiments + arXiv retrieval
        ↓
mutual review, counterexample search, prior-art check, independent re-proof
        ↓
paper draft + recommendation for human number-theorist validation
        ↓
human mathematical examination and communication
        ↓ parallel
Claude + human collaborator → Lean formalization → Comparator-compatible artifact
```

公开说明没有给出 subagent scheduler、shared memory、message topology、context compaction、candidate ranking、budget allocation 或 automatic stopping rule。这些字段保持 `UNKNOWN`。

## 模型与角色分工

- coordinator：未发布 research version of Claude，在 Claude Code 中运行；准确 family/checkpoint 未公开；
- workers：约 60 个 Claude subagents，是否完全同一 checkpoint 未说明；
- tool layer：shell commands、Python scripts、已知 zeta zeros 的 numerical checks、arXiv paper downloads；
- internal validation：13 个 agents 被报告为 validators，另有 agents 做 mutual review、counterexample search 和 from-scratch re-proof；
- writing：2 个 agents 帮助初始 paper，Claude 自主提出写成论文；
- human validation：Levent Alpöge、Ralph Furman；外部专家 Brian Conrey、Dan Goldston在短时间内 examined paper，但公开页没有把这表述为正式 referee acceptance；
- formalization：Claude 与 Eric Easley 协作，公开仓库声明 Theorems A--E 为 `sorry`-free Lean 4 formalization。

## 使用方式

### 案例披露的发现流程

1. 在 Claude Code 给出高层自然语言研究问题；
2. 允许系统先做宽搜索，并保留失败结果；
3. 失败后由人决定是否启动第二轮更深搜索；
4. 让 coordinator 分配 idea generation、validation、prior-art search、numerical testing 与 writing 等不同角色；
5. 用 shell/Python 快速否定候选，但不把数值支持升级为证明；
6. 对幸存证明路线安排反例搜索、互审和独立重证；
7. 先产生可供专家检查的 paper，再由领域数学家审查；
8. 将 theorem statements 独立形式化并通过 kernel/Comparator 检查。

这是一份 case-derived workflow，不是可直接复制的 recipe。因为模型 checkpoint、系统 prompt、subagent API 和调度器未公开，本项目不能实际复跑 discovery stage。

### 公开形式化工件检查

公开仓库说明的最小检查路径是：安装 `elan`，让 `lean-toolchain` 选择 Lean 4.33.0-rc2，执行 `lake exe cache get`、`lake build`、`lake build Solution Solution.XiPrime`，再运行 `PrintAxioms` 与 Comparator。仓库固定 Mathlib commit，并说明 headline theorems 预期只依赖 Lean 的标准 axioms。

本项目本周只核对说明，未下载数 GB cache、未 build，也不把仓库自述当作已由本项目重放。

## 验证与失败处理

该工作流有四种不同检查，不能合并：

1. numerical checks：快速筛除错误候选，不是证明；
2. Claude validators 与 re-proof agents：对抗性 LLM 检查，不是独立 kernel；
3. 人类 number theorists：理解、修正和承担 paper-level 责任；
4. Lean/Mathlib/Comparator：检查形式 statement 的 proof term 与 axiom boundary。

Lean 工件显著提高可检查性，但仍需确认 formal statement 与论文命题的语义一致，以及 formalization 是否覆盖所有被宣传的范围。

## 复现条件、成本与安全边界

- discovery：模型私有、调度与 prompts 不完整，`NOT RERUNNABLE`；
- process observability：官方链接提供 detailed transcripts，公开页给出 agent role counts 和工具规模，但本项目未把完整 transcript 做 proof-grade intake；
- formal output：仓库、toolchain、Mathlib commit、build/axiom/Comparator commands 公开，`PUBLICLY CHECKABLE`；
- compute：31M output tokens、约一天半、2,400 shell commands、数百 Python scripts；没有完整货币成本、硬件或失败预算；
- security：若未来复跑类似 harness，shell、批量下载和外部 API 必须在隔离目录、受限凭据和明确费用/时间上限下运行；当前不执行。

## 有公开依据的案例

- [Claude ζ 零点比例结果工作流审计](../dossiers/2026-claude-zeta-bound-workflow.md)

## 可学习的方法

1. 大规模 idea generation 后，应专门分配 agents 做否证和 prior-art search；
2. 失败路线数量是过程证据，不能从最终论文中删除后再宣称一步成功；
3. 数值实验、LLM re-proof、人类检查和 formal kernel 是互补而非替代关系；
4. 先由系统提出“请人类领域专家验证”，可作为高风险结果的停止与升级条件；
5. 将 trusted statement 与 solution 隔离，有助于检查形式证明是否只是在改写目标。

这些观察不能证明 60 agents 优于等 token 的单 agent；没有受控消融。

## 证据缺口

- 未发布 Claude 的 checkpoint、system prompt、temperature/effort 和 context；
- subagent 消息拓扑、共享 memory、调度策略和 stopping rule；
- 31M tokens 在两轮、各角色和失败路线中的分配；
- 人工消息、transcript 完整性与未发布运行的选择偏差；
- 第三方从零复跑 discovery 的可能性；
- 独立团队对 formal repository 的 build、axiom 与 semantic-equivalence audit。

## 原始来源

- [Anthropic methodology report](https://www.anthropic.com/research/riemann-zeta)，检索于 2026-08-24。
- [Alpöge--Furman paper, arXiv:2608.13637v2](https://arxiv.org/abs/2608.13637)，检索于 2026-08-24。
- [Zeta23 Lean repository](https://github.com/anthropics/zeta-23-lean)，检索于 2026-08-24。
