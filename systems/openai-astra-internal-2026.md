---
system_id: "openai-astra-internal-2026"
name: "OpenAI Astra internal mathematics system (2026 release snapshot)"
record_updated: "2026-08-24"
versions_checked: ["internal Astra version described 2026-08-01", "ten-proofs GitHub main retrieved 2026-08-24"]
primary_sources: ["https://openai.com/index/ten-advances-in-mathematics/", "https://cdn.openai.com/pdf/ten-proofs-oai.pdf", "https://cdn.openai.com/pdf/reasoning-walkthroughs.pdf", "https://github.com/openai/ten-proofs"]
reproducibility: "PRIVATE-MODEL / PUBLIC-OUTPUT-ARTIFACTS"
---

# OpenAI Astra internal mathematics system（2026 发布快照）

## 系统概述

这里的 Astra 是 OpenAI 尚未公开的下一代模型的一个内部版本，而不是当前可安装的 open-source theorem prover。可核查材料支持重建“生成数学论证 → 协助成稿 → 生成 Lean certificate → 发布可读 reasoning narration”的流水线，但不支持重建其内部 agent architecture 或训练机制。

## 版本对应

| 记录 | 可确认内容 | 不可确认内容 |
|---|---|---|
| 2026-08-01 official release | 内部 Astra 版本生成十项数学论证；总 token 量按 Sol API rate 估算约 2,000 美元 | model checkpoint、context、prompt、worker 数、sampling、工具权限 |
| bundled paper，2026-08-06 update | 十章线性 manuscripts | 原始输出到成稿的逐步 diff 与人工修订量 |
| `openai/ten-proofs`，检索于 2026-08-24 | 十项 Lean certificates、Lean 4.32.0/Mathlib 项目、构建与 Comparator 入口 | 发现过程和 formalization 过程的完整 trace |
| reasoning walkthroughs | 模型生成的可读过程叙述 | 原始 chain-of-thought 或逐次决策日志 |

`Astra` 是来源给出的 family/name；本项目没有把它等同于 Sol，也没有从价格换算反推底层模型。

## 架构与数据流

公开证据只支持下面的外部流水线：

```text
selected open problems
        ↓
internal Astra generates mathematical arguments
        ↓
humans + the same model prepare manuscripts
        ↓
model produces one Lean certificate per argument
        ↓
Lean/Mathlib build + Comparator-compatible challenge interface
        ↓
separate model-generated reasoning walkthroughs
        ↓
public paper, certificates and narrations
```

是否存在 orchestrator、并行 workers、retrieval service、长期 memory、独立 LLM verifier 或自动失败恢复，在已检查来源中均为 `UNKNOWN`。不能把 Danus、Claude multiagent 或其他项目的结构倒填给 Astra。

## 模型与角色分工

- mathematical argument generation：内部版本 Astra；准确 checkpoint 未公开；
- manuscript preparation：人类与同一模型协作；逐章人机编辑比例未公开；
- formalization：官方称模型 formalized each argument，且人类帮助 formalize；准确交互次数和人工修补量未公开；
- narration：发布的是一个模型对探索过程的重构叙述，不是原始 hidden reasoning trace；
- validation：公开 Lean repository 支持 kernel checking 和 Comparator，但官方没有给出逐项独立外部审计结果。

## 使用方式

当前不能给出 Astra 的真实使用教程，因为模型、API 和运行配置没有公开。唯一可实际执行的是检查发布后的 Lean 工件：

1. 安装与仓库匹配的 Lean/elan 环境；
2. clone `openai/ten-proofs`；
3. 获取固定 Mathlib cache；
4. 运行 `lake build All`；
5. 对目标 challenge 按仓库说明运行 Comparator，以隔离 trusted statement 与 submitted solution；
6. 另行人工核对 Lean statement 与论文自然语言命题是否等价。

这只能复核输出工件，不能复现发现。若未来开放 Astra，应另建新版本记录，不用公开版的新规格倒填 2026-08-01 的案例。

## 验证与失败处理

Lean kernel 可以检查一个 proof term 是否证明了编码后的 proposition；它不会自动判断：

- proposition 是否准确表达论文声称的数学命题；
- definitions 是否偷换范围或弱化结论；
- imported axioms、外部计算或 trusted boundary 是否符合预期；
- manuscript 的每个中间论证是否与形式证书一致；
- AI 的发现贡献是否按来源描述发生。

量子 parallel-repetition 章节的公开纠错说明，线性论文即使有对应证书仍需独立 manuscript audit。纠错作者给出了局部修复，但明确没有独立验证主定理。

## 复现条件、成本与安全边界

- 发现系统：`NOT PUBLICLY REPRODUCIBLE`；
- 结果工件：paper、walkthroughs、Lean code 可公开取得；
- 成本：官方只给出按 Sol API rate 估算的约 2,000 美元 token 成本，未给 wall time、硬件、失败预算或人工成本；
- 权限与密钥：未知；本项目不保存任何凭据，也不尝试调用未公开系统；
- 复现结论：`OUTPUT-CHECKABLE / DISCOVERY-NOT-RERUNNABLE`。

## 有公开依据的案例

- [OpenAI 十项结果工作流审计](../dossiers/2026-openai-ten-advances-workflow.md)

## 可学习的方法

1. 把自然语言 proof、形式 statement 与 proof term 同时发布，允许三者之间做语义审计；
2. 给每项结果独立 challenge interface，比只发布组合 PDF 更可检查；
3. 可读 walkthrough 应明确标为 reconstruction，避免被误当原始运行日志；
4. 对组合发布应逐项维护 version、correction 和 verification 状态，而不是给整包一个通过标签；
5. 形式化之后仍需要 manuscript-level adversarial review。

这些是可检验的发布与验证设计，不是对 Astra 能力因果来源的判断。

## 证据缺口

- model checkpoint、训练/推理规格、context window 和 sampling；
- 原始 prompts、worker/orchestrator topology、检索与工具调用；
- 每题 token、wall time、失败路线和 stopping condition；
- 人工编辑和 formalization repair 的逐项记录；
- paper statement 与 Lean statement 的独立语义审计；
- 十项结果的逐项专家验证与第三方重放。

## 原始来源

- [OpenAI official release](https://openai.com/index/ten-advances-in-mathematics/)，检索于 2026-08-24。
- [Bundled paper](https://cdn.openai.com/pdf/ten-proofs-oai.pdf)，检索于 2026-08-24。
- [Reasoning walkthroughs](https://cdn.openai.com/pdf/reasoning-walkthroughs.pdf)，检索于 2026-08-24。
- [Lean certificates repository](https://github.com/openai/ten-proofs)，检索于 2026-08-24。
