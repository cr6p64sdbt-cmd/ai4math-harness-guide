---
case_id: "2026-proof-council-firstproof-p3"
title: "ProofCouncil 在 FirstProof 第二批 P3：加权 Bernoulli 和的部分结果"
record_updated: "2026-09-20"
event: "events/2026/2026-07-10-proof-council-firstproof.md"
systems: ["proof-council"]
mathematical_status: "OPEN"
workflow_status: "WORKFLOW-DOCUMENTED / PUBLIC-TRACES-PARTLY-READ"
---

# FirstProof P3：加权 Bernoulli 和何时至少以概率 \(p\) 超过均值？

## 先给判断

**完整分类仍是 `OPEN`。** ProofCouncil 交卷明确把 \(0\le p\le1/3\) 全体成立写成未证猜想；已证明的范围包括 \(p=1/k\)、\(p=2/k\)（\(k\ge6\)）、\(p=1/2,1\)，并排除了 \((1/3,1/2)\cup(1/2,1)\)。官方报告将该提交评为 **Minor Revisions**，理由是正确且有新意的**部分进展**，不是完成了全部 \(p\) 的判定。[提交开头、各命题](https://github.com/1stproof/batch-2/blob/274625a22e4748d5f9264ba3614353461520bd20/batch-2-AI-solutions/problem-03/submission-A.tex)、[官方报告 §5.3，PDF 第 27 页](https://1stproof.org/assets/docs/report.pdf)。

数学结论分层：提交中的局部断言有三位匿名审稿人评价和可读论证；本项目只重建了关键 coloring reduction 与简单反例，**没有逐行复核全部 pairing lemma 或运行 formal kernel**。AI 贡献是官方封闭题目输入后由系统生成这些部分论证；“首次发现”的优先权只能限于报告称 `p=2/k` 家族的证明 *appears to be novel*，不能扩张为完整原创解答。[官方报告 §3.3、§5.3](https://1stproof.org/assets/docs/report.pdf)、[审稿 1](https://github.com/1stproof/batch-2/blob/274625a22e4748d5f9264ba3614353461520bd20/batch-2-reviews/problem-03/submission-A/submission-A-reviewer-1.tex)、[审稿 2](https://github.com/1stproof/batch-2/blob/274625a22e4748d5f9264ba3614353461520bd20/batch-2-reviews/problem-03/submission-A/submission-A-reviewer-2.tex)、[审稿 3](https://github.com/1stproof/batch-2/blob/274625a22e4748d5f9264ba3614353461520bd20/batch-2-reviews/problem-03/submission-A/submission-A-reviewer-3.tex)。

## 数学对象与问题原意

任取有限 \(m\ge1\) 与非负权重 \(w_i\ge0\)、\(\sum_i w_i=1\)。令 \(v_i\) 独立同分布为 Bernoulli\((p)\)，即 \(v_i=1\) 的概率为 \(p\)。随机和 \(X=\sum_iw_iv_i\) 的均值是 \(p\)。问题要求找出哪些 \(p\in[0,1]\) 对**每一个**有限权重向量都满足

\[
\Pr(X\ge p)\ge p. \tag{P}
\]

量词次序很关键：固定某组 \(w\) 的结论不足以回答题目；在某个 \(p\) 找到一组反例权重，就可排除该 \(p\)。当 \(m=1,w_1=1\) 时等号成立，因此右侧 \(p\) 是可能的最优统一下界。人类作者 Milojević–Sudakov 的官方题目与解答载于 [FirstProof 报告 §3.3](https://1stproof.org/assets/docs/report.pdf)、[人类解答引言](https://github.com/1stproof/batch-2/blob/274625a22e4748d5f9264ba3614353461520bd20/batch-2-human-solution/problem-03/human-solution.tex)。

原题不是要求证明某个已公布定理：挑战时答案未向参赛系统公开；但其作者已有未发表解答。人类解答给出与 Manickam–Miklós–Singhi（MMS）子集和问题的关联，并借 Pokrovskiy 的结果覆盖极小 \(p\)（报告写 \(p\le10^{-46}\)），同样没有解决猜想中的全部 \(p\le1/3\)。因此本例是**研究问题的独立部分进展**，不是形式化现成证明，也不是完整判定。[报告 §3.3](https://1stproof.org/assets/docs/report.pdf)、[人类解答 §1](https://github.com/1stproof/batch-2/blob/274625a22e4748d5f9264ba3614353461520bd20/batch-2-human-solution/problem-03/human-solution.tex)。

## 系统交出了哪些具体数学内容

| 范围或主张 | 提交给出的内容 | 本轮证据界限 |
| --- | --- | --- |
| \(1/3<p<1/2\) | \(m=3,w_i=1/3\) 时概率是 \(3p^2-2p^3<p\)。 | 可直接核对的反例；非本案的新意。 |
| \(1/2<p<1\) | \(m=2,w_i=1/2\) 时概率为 \(p^2<p\)。 | 可直接核对的反例。 |
| \(p=1/k\) | coloring criterion 的 \(a=1,b=k\) 情形。 | 此家族在先前文献已知；缺引文是审稿问题。 |
| \(p=2/k,\ k\ge6\) | `pairs` 引理：任意总和 1 的 \(k\) 个非负数，至少 \(k-1\) 对之和不小于 \(2/k\)；再用 coloring criterion。 | 三位审稿人视为正确，官方报告称该家族“似乎新”；本项目未独立逐行重证引理。 |
| \(p=1/2,1\) | 对称性与端点直接成立。 | 基础结论。 |
| 全部 \(0\le p\le1/3\) | 明确列为 conjecture，给出等价形式、乘法闭性等。 | 仍未证明；不能由已有离散 \(p\) 家族推成区间。 |

上述位置在[提交 §Positive values、§Values that cannot work、§Equivalent forms](https://github.com/1stproof/batch-2/blob/274625a22e4748d5f9264ba3614353461520bd20/batch-2-AI-solutions/problem-03/submission-A.tex)；官方判读见[报告 §5.3](https://1stproof.org/assets/docs/report.pdf)。

## 关键研究步骤：从随机不等式到组合计数

这个步骤值得学习，因为它把“对所有权重的随机尾概率”转成一个可单独证明或证伪的有限组合陈述。设 \(p=a/b\)，先独立、均匀地把每个原指标染成 \(b\) 种颜色之一，颜色 \(j\) 的总权重是 \(x_j\)。假设**每一种**非负、总和为 1 的 \(b\) 元组 \(x\) 至少有

\[
\binom{b-1}{a-1}=\frac{a}{b}\binom ba
\]

个 \(a\) 元颜色集合 \(J\) 满足 \(\sum_{j\in J}x_j\ge a/b\)。在随机染色和均匀选 \(J\) 后，成功概率至少 \(a/b\)。由于颜色对称，固定任一个 \(J\) 也一样；每个原指标落入该固定 \(J\) 的事件独立且概率恰为 \(a/b\)，所以得到原式 (P)。这就是[提交的 coloring criterion 及证明](https://raw.githubusercontent.com/1stproof/batch-2/274625a22e4748d5f9264ba3614353461520bd20/batch-2-AI-solutions/problem-03/submission-A.tex)。

组合假设经 \(y_j=x_j-1/b\) 改写后变成“总和为 0 的 \(b\) 个数，至少有 \(\binom{b-1}{a-1}\) 个非负 \(a\) 元子集和”，正是 MMS 类型问题的形式。**提交没有识别并正确引证完整既有 MMS 理论**；官方报告称这使它错过借 Pokrovskiy 覆盖 \(p\le10^{-46}\) 的路径。更微妙的是，提交自己给出 \(p=3/10\) 的反例：七个 \(x_j=1/7\)、三个 0，则达阈值的三元组仅 \(\binom73=35<\binom92=36\)。所以这个“逐个着色状态均成立”的充分条件在整个猜想区间里会失败；继续研究需要更细的**平均**信息，不能机械把充分条件当成等价条件。[提交对应段落](https://raw.githubusercontent.com/1stproof/batch-2/274625a22e4748d5f9264ba3614353461520bd20/batch-2-AI-solutions/problem-03/submission-A.tex)、[报告 §3.3、§5.3](https://1stproof.org/assets/docs/report.pdf)。

## 可核查的运行过程与失败修正

主办方规定：题目与原答案在测试前分离，四套系统通过 API 各自一次性运行，随后匿名专家审稿；ProofCouncil 是 System A。[官方 Second Batch 页面](https://1stproof.org/second-batch.html)、[报告 §2、§4](https://1stproof.org/assets/docs/report.pdf)。五月冻结 [README](https://github.com/1stproof/batch-2/blob/274625a22e4748d5f9264ba3614353461520bd20/batch-2-submissions/improofbench/README.md) 说明初始 5 轮、续到 10 轮，并在时间与预算允许时逐批续跑；`answer.tex`、研究笔记和原始轨迹保存。具体 P3 的逐轮档案公开在 [FirstProof 原始运行目录](https://github.com/1stproof/batch-2/tree/274625a22e4748d5f9264ba3614353461520bd20/batch-2-raw-outputs/IMProofBench/WorkflowRuns/firstproof-prob-003-20260529T215332Z-6a40eb14)。

本轮检查了 P3 的 [round-0/answer.tex](https://github.com/1stproof/batch-2/blob/274625a22e4748d5f9264ba3614353461520bd20/batch-2-raw-outputs/IMProofBench/WorkflowRuns/firstproof-prob-003-20260529T215332Z-6a40eb14/ac_workspaces/prob-003-50f20aa0b43c/.ac/round-0/answer.tex)、[round-10/answer.tex](https://github.com/1stproof/batch-2/blob/274625a22e4748d5f9264ba3614353461520bd20/batch-2-raw-outputs/IMProofBench/WorkflowRuns/firstproof-prob-003-20260529T215332Z-6a40eb14/ac_workspaces/prob-003-50f20aa0b43c/.ac/round-10/answer.tex) 和最终 [submission-A.tex](https://github.com/1stproof/batch-2/blob/274625a22e4748d5f9264ba3614353461520bd20/batch-2-AI-solutions/problem-03/submission-A.tex)。初稿把整个猜想区间断言为已解决，并引用所谓 “Kellerer weighted Bernoulli inequality” 作为承担全部困难的外部引理；第 10 轮快照已删去这个冒进主张，改写为“仅部分结果”，并包含 coloring criterion、`p=2/k` 引理与公开缺口。**这说明输出随轮次修正；本轮尚未逐条读取中间 Critic/compute 对话，故不能确定哪条反馈触发了纠正。** 这也是本案最具体的审稿教训：引用一个与目标几乎同义的“已知定理”必须核原文，不能因模型署上作者名就接受。

论文 §3.2.2 报告 council 中 GPT-5.5-Pro、Claude Opus 和 Gemini 对 P3 提供过方向或类比，compute worker 也被较多使用；这些是作者对日志的归纳。对 P3 究竟哪一次调用提出了 coloring criterion 或 pairing lemma，本轮没有建立可定位的因果链，不能归给某个单独模型。[ProofCouncil 论文 §3.2.2](https://arxiv.org/html/2607.09474)。

## 人与验证器分别做了什么

- **人类出题方**：Milojević、Sudakov提供原问题与封存的人类解答；FirstProof 组织者设定测试与盲审。审稿人在 AI 输出之后指出缺失的 MMS/Pokrovskiy 关联和引文缺口，并把数学内容评价为正确、有部分新意。[报告 §2、§3.3、§5.3](https://1stproof.org/assets/docs/report.pdf)。
- **AI 系统**：在固定题目上写出交卷，提出组合充分条件与 \(2/k\) 家族等，修正早期过度完成宣称；具体每轮谁做哪一步须进一步审计公开轨迹。
- **内部 Critic**：论文 §3.2.2 将 P3 列为值得注意的失败情形：Critic 在各阶段拒绝，外部审稿给 minor revisions。但提交明示 \(p\le1/3\) 的完整分类未证；内部 answer_ready 是“当前证明完整且正确”的退出信号，外部决定认可的是可发表的正确部分进展。由于判准不同，**不能仅由两项决定不一致就称其为假阴性**；是否还存在对已证明局部命题的误拒，需要查看逐轮 Critic 文本及其明确目标。P8 的内部误接纳与专家拒绝则有被指出的具体未证断言，说明内审不具 formal kernel 的约束力。[论文 §3.2.2](https://arxiv.org/html/2607.09474)。
- **外部专家**：三位审稿人建议 Minor Revisions，评论重点与强弱有所不同；官方编辑决定是可核查的评估结果，并不等于本项目完成了全部数学重证。[报告 §5.3](https://1stproof.org/assets/docs/report.pdf)。

## 学习价值、风险及更新点

可单独试验的做法是：让作者保留“已证/猜想/失败引用”三个明确层次；给审稿人完整论证和文献引用核查任务；针对一个可检查的有限组合命题调用辅助模型或 CAS；保存轮次快照，比较早期错误怎样消失。它们的适用前提是目标量词已钉牢、外部结果可取得原文、最终主张由人工或更强证据独立验收。本案例的效果证据是实际产物和盲审意见；**没有消融实验**证明其中单个设计导致了新家族发现。

复现边界：代码、配置、匿名提交、审稿与原始轨迹公开，但本项目未执行 harness，未完整重放 P3 的每轮消息，也未支付 API 成本。官方论文给出整批平均模型调用费用约 350 美元/有交卷题；本轮**没有从 P3 token 日志核出其单题精确成本**。后续优先检查 P3 逐轮 Critic/compute 消息和人工解答的引用对应，再对 pairing lemma 做逐行独立数学复核；任何新版配置或官方更正需重新绑定版本。[系统档案](../systems/proof-council.md)、[来源审计](../references/notes/2026-09-20-proof-council-source-audit.md)。
