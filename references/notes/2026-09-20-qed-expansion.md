# QED 与输运–扩散案例：2026-09-20 来源收据

## 本批范围与证据上限

- 任务：为 AI4Math 学习仓库深读 QED harness 及其最贴近动力系统读者的二维流体混合/PDE 成果；不作其他候选的排序，不查 research 1，不运行外部 harness。
- 阶段：已有候选 QED 的 deep reading，不是平面 ODE 文献的优先权或新颖性审查。时间范围为截至 2026-09-20 可见公开版本；访问模式 OPEN-ONLY；机构身份/访问无需使用。
- 查找路径：项目 CANDIDATES.md 原有 QED 入口 → QED 系统论文 arXiv:2604.24021v4 Appendix A.4 的数学论文引用 → An–Xu arXiv:2605.20623v1 → 官方仓库 proved_statements、README、配置和源码。网页搜索没有用于证明判断。没有前向引文索引，也不作“没有其他结果”的断言。
- 阅读级别：数学论文 §1–4 的定理陈述和选定承重推导、§5 AI 工作说明为 section-summary；旧 P3 的输入、证明和关键 Fourier tail 步骤直接对照并做局部手算；并非全文 faithful excerpt 或项目 proof acceptance。本文没有保存 PDF；因此没有下载 hash，也没有把 HTML 页面当作 PDF 视觉校对。

## 原始来源与复用路径

|来源用途|固定入口与本次读过的位置|版本/访问状态|尚缺|
|---|---|---|---|
|系统论文|[QED arXiv:2604.24021v4](https://arxiv.org/html/2604.24021v4)：§3 七类失败；§4.1 simple、§4.2 decomposition、§4.3 验证、§4.5 人工指导、§4.7 恢复；§5.1 模型和费用、§5.2 验证计数；Appendix A.4 与 C|arXiv v4 于 2026-06-26，开放 HTML；2026-09-20 查|历史运行 commit、全量日志|
|数学论文|[An–Xu arXiv:2605.20623v1](https://arxiv.org/html/2605.20623v1)：§1、Theorem 2.1/证明关键链、Theorems 3.1/3.2、§3 低高频屏障、Theorem 4.1、§4 伴随观测量/快速相位、§5 AI 贡献|arXiv abstract 页显示唯一 v1 于 2026-05-20，63 页；开放 HTML；2026-09-20 查|没有完整证明审读、外部谱定理逐条核验|
|早期数学输入与输出|[2026-04-24 原始目录](https://github.com/proofQED/QED/tree/03faa8238aef4710084b117657ec9f0f7e80fe57/proved_statements/analysis-Apr-24-2026)：README、problem-3.md、problem-3-correct-proof.md|通过 GitHub commit API 查到该路径首个可见提交 03faa8238aef4710084b117657ec9f0f7e80fe57，提交日期 2026-04-24；固定只读|真正运行日志、verifier 各轮报告|
|后续 PDE 结果说明|[analysis-May-19-2026 README](https://github.com/proofQED/QED/blob/121900964e6572aaf094412d434b5ac2a792a65f/proved_statements/analysis-May-19-2026/README.md)、同目录 cited-theorems|2026-08-16 仓库固定快照；只读|目录未提供每个问题完整过程工件|
|当前系统源码|[官方仓库固定快照](https://github.com/proofQED/QED/tree/121900964e6572aaf094412d434b5ac2a792a65f)：README、config.yaml、code/pipeline.py、code/decomposition_prover.py、code/model_runner.py、prompts/decomposition-prover、LICENSE|GitHub API 查 main 为 121900964e6572aaf094412d434b5ac2a792a65f，commit 日期 2026-08-16；本次只读|与 4/5 月实验运行的历史 commit 关联未证实|

论文入口的 [arXiv abstract page](https://arxiv.org/abs/2605.20623) 明列 v1、63 页、2026-05-20；HTML 文章抬头却显示 “Date: August 24, 2026”。这两个日期冲突，不能用抬头日期代替 arXiv 版本记录，也不能据此推断事后有某次未显示的修订。本档固定 arXiv 版本号，待后续如有必要以 arXiv TeX/PDF 元数据核差异。

代码 [MIT LICENSE](https://github.com/proofQED/QED/blob/121900964e6572aaf094412d434b5ac2a792a65f/LICENSE)；arXiv HTML 标 CC BY 4.0。二者与模型服务许可不是一回事。当前仓库 config.yaml 写 Codex gpt-5.6-sol/xhigh、Claude bypassPermissions、Gemini yolo；旧 4 月目录明确 Codex GPT-5.4 + Gemini 3.1 Pro，数学论文 §3–4/系统论文 §5.1 写 GPT-5.5。**不能用当前 config 或代码默认值重建历史实验。**

## 关键出处对照

|事实或疑点|原始定位|审读结论|
|---|---|---|
|P3 的“找指数混合例子，或证不可能”|[旧 problem-3.md 行 3–18](https://github.com/proofQED/QED/blob/03faa8238aef4710084b117657ec9f0f7e80fe57/proved_statements/analysis-Apr-24-2026/problem-3.md#L3-L18)|精确输入含二择，不是事后把失败改写为成功|
|旧答案选否定支|[旧 proof 行 41–42、Steps 1–7](https://github.com/proofQED/QED/blob/03faa8238aef4710084b117657ec9f0f7e80fe57/proved_statements/analysis-Apr-24-2026/problem-3-correct-proof.md#L41-L42)|保留零 x 模退化分支；选择非零 x 模后用 W1,1 控 Fourier tail，得到全时 t^-2 下界|
|无扩散最终陈述|[数学论文 §2 Theorem 2.1](https://arxiv.org/html/2605.20623v1#S2.Thm1)|θ0 非零、平滑、平均零；U 属于 L∞t W1,1y；不是任意 L∞ 剪切|
|带扩散最终陈述|[§3 Theorems 3.1、3.2](https://arxiv.org/html/2605.20623v1#S3)|实值有界 U，初值平滑平均零，小 ν，常数依赖数据；§3 Remark 3.1(3) 指出 sharpness 请求理解不全|
|快周期结果|[§4 Theorem 4.1、STEP3–5](https://arxiv.org/html/2605.20623v1#S4)|u 为时周期且空间 Lipschitz/散度零，A 超过依赖数据的阈值；不是所有非自治流|
|案例模型和成本|[QED 系统论文 §5.1、Appendix C](https://arxiv.org/html/2604.24021v4#S5.SS1)、[数学论文 §5](https://arxiv.org/html/2605.20623v1#S5)|早期 simple GPT-5.4，后续 decomposition GPT-5.5/xhigh；整组约 600 美元、少于 36 小时均作者报告|
|机器核验|[QED 系统论文 §4.3、§5.2](https://arxiv.org/html/2604.24021v4#S4.SS3)|LLM 结构+细节检查；214/17 为使用 GPT-5.5 verifier 的子集；数学论文的 66/14 是 PDE 案例统计，口径不同|

## 阅读时发现的接口风险

旧分析目录 README 记 GPT-5.4 Codex prover / Gemini 3.1 Pro verifier，系统论文 v4 §5.1 写前两题 “all agents” Codex GPT-5.4。这是具体的历史配置冲突，缺日志时保留两种说法，不从当前配置推断过去。

1. arXiv v1 的正文日期与提交时间不一致，后续引用坚持明确版本号。
2. [早期 README](https://github.com/proofQED/QED/blob/03faa8238aef4710084b117657ec9f0f7e80fe57/proved_statements/analysis-Apr-24-2026/README.md) 将四道题记 P1–P4；系统论文 Appendix C 的 P1–P12 是该附录内部问题编号，不能靠数字直接对齐。
3. 数学论文 §3 Remark 3.1(3) 保留了 AI 没完全理解 sharpness 请求的记录；§3 Remark 3.3 承认齐次/非齐次 H^-1 常数修订。系统成功不是没有数学编辑。
4. 当前仓库有源码、prompt 和最终工件，但公开检查中未见全量中间计划、模型调用和每轮核验报告。论文 §5 “每一步完全可检查”属作者表述，复核历史运行仍要索取对应日志。
5. 63 页数学论文尤其 §4 的 Keldysh/Floquet/伴随束推导未做 faithful excerpt 和完整假设映射；本档只提供学习级 section-summary，不是可移植证明。

后续开启条件：获取历史日志和精确 commit；或为学术证明复用而对 §2–4 制作忠实摘录、检查引用的 Huang–Xu 与谱/抛物平均结果，并独立核全体参数量词。当前停止在学习与来源绑定层级，无新颖性穷尽结论。
