# 动力系统定向来源核查（2026-09-20）

公开读取，外部代码只读；没有训练、执行下载代码或保存新 PDF。解释笔记不是 faithful excerpt。总体检索范围与实际查询见[本批收据](2026-09-20-expansion-survey.md)。

## 符号 Lyapunov：论文、代码和验证器

- [2410.08304v1 HTML](https://arxiv.org/html/2410.08304v1)、[版本页](https://arxiv.org/abs/2410.08304)：版本页本次只列2024-10-10 v1。尝试v2 HTML未取得正文后回版本页核实，没有用不存在的新版本。
- 实际阅读 §§2–4、§5.4 表6、§5.5、§6、附录D表12及F.1–F.2；其余不是全文逐行审计。核F.1向量场、非多项式输出和beam100，F.2的导数半负和非孤立平衡点。Table6 Poly5的findlyap为0.7%，2.1%属于LyzNet，不能串列；NonPoly的12.7%与SMT选定球8.3%不等于全空间完备判定。
- [官方仓库](https://github.com/facebookresearch/Lyapunov/tree/ce72b4ccbbe3fc00ee869c88b64a293381965a0b)，固定commit `ce72b4ccbbe3fc00ee869c88b64a293381965a0b`；README显示2026-04-02归档。读README、LICENSE（CC BY-NC 4.0）、训练/反向非多项式生成配置。论文8层与公开训练配置6层不能混成同一运行。库的发布时间/归档不是论文案例运行日期。
- [src/envs/ode.py](https://github.com/facebookresearch/Lyapunov/blob/ce72b4ccbbe3fc00ee869c88b64a293381965a0b/src/envs/ode.py)：`test_V_positive` 约127–201行、`check_lyap_validity` 2146–2293行，及 `gen_lyap_fun`/`gen_lyap_system`/`gen_lyapunov` 生成入口。检查路径有目标表达式匹配快捷返回、SOS或SHGO、有限盒与随机起点；所读路径未见完整径向无界检验。不同负返回码区分无效、超时和其他失败，不能解释为不存在。
- 本项目对F.1函数给显式配方和子水平集界；对F.2给精确导数、解极限与平衡线，详见[案例](../../dossiers/2024-symbolic-lyapunov-planar.md)。未核所引Ahmadi不存在全局多项式函数定理，未复跑数据和训练。

## 不稳定流体奇性：数值方法与后续版本分开

- [2509.14185v1](https://arxiv.org/html/2509.14185v1)，2025-09-17；[版本页](https://arxiv.org/abs/2509.14185)。本次仅v1。读主文各类发现、Methods 2–6、13–19，网络表示、GN优化、误差网络与谱诊断；未取得其正文所说将另行公开的完整补充包。
- 原文CCF第二不稳定候选约0.4703、残差约1e-7；不能与已知稳定/第一不稳定分支1e-13混写。Boussinesq第四候选的低可信度按原文保留。50k步/约3 A100小时是局部方法比较，不是全部研究费用。
- [2511.22819v1](https://arxiv.org/html/2511.22819v1)，2025-11-28；[版本页](https://arxiv.org/abs/2511.22819)。读摘要、引言、§2.1及式1–4、Fig.2，部分后续章节；不冒充完整阅读全文。Fig.2的CCF第二分支单阶段值0.47132422与旧近似不同，梯度归一化是后续方法，不倒填首篇。
- [作者NASA报告，2026-03-05](https://nas.nasa.gov/pubs/ams/2026/03-05-26.html)的摘要将工作称为数值构造并展望计算机辅助证明，不支持称已严格解决无外力Euler爆破。未读其全部讲座幻灯片。
- 搜索出现社区复刻，未作为作者官方runtime入口；第三方实现与官方训练运行不得等同。本次所查原文没有取得能绑定全部案例的官方代码/权重/种子/日志。状态为 `NOT-FOUND-IN-CHECKED-SET`，不是断言全网不存在。

## 补充条目与固定源码入口

|条目|原始来源与版本|实际读取|未检查|
|---|---|---|---|
|RL解析Lyapunov|[2502.02014v1](https://arxiv.org/html/2502.02014v1)；[官方代码6465235610870dc16450196cbff39b8bea77729f](https://github.com/JieFeng-cse/Analytical-Lyapunov-Function-Discovery/tree/6465235610870dc16450196cbff39b8bea77729f)，2025-07-20|引言、§3–4、表1、F.1；README、根目录树|会议最终版差异、完整代码、声称新的电网函数及新颖性、全部SMT记录|
|AI Poincaré 2.0|[2203.12610摘要页](https://arxiv.org/abs/2203.12610)；[1ddede901bb26b85e52164e32a97599965218812](https://github.com/KindXiaoming/aipoincare_2.0/tree/1ddede901bb26b85e52164e32a97599965218812)，2022-04-14|摘要、README、固定树；发现README启动文件与树不匹配|全文、每项守恒量、训练代码及运行环境|
|fluid_lean|[独立来源收据](2026-09-20-fluid-lean-source-audit.md)|作者PDF具体定理、README、形式声明与元数据；由受委派来源核查后主控整合|完整Lean重放、整个证明工程、prompt与运行历史|

RL F.1阻尼号和半负导数的缺口由本项目单独补核，见[补充对照](2026-09-20-dynamics-adjudication.md)。没有把其简单函数成功当作新的极限环成果。两补充代码根目录没有可见LICENSE文件，未完成全依赖授权审计。

## 关联追踪与范围外线索

从Lyapunov论文相关工作/检索进一步找到RL方法及[CoNSAL 2406.15675](https://arxiv.org/abs/2406.15675)作者代码入口；CoNSAL仅定位，未另算已读候选。守恒量路线沿作者论文找到AI Poincaré 2.0。流体作者关联材料指向fluid_lean，具体归因依该库的作者声明，不能只因作者重合就给其他论文贴AI标签。

曾定位[2609.16470v1](https://arxiv.org/html/2609.16470v1)的IPM光滑外力工作，但本次读取未获得足以确认AI贡献的记录，未单列AI成果。检索出现时间晚于本次日期的院系新闻页面，不用其日期锚定成果；优先使用固定提交和作者文件。没有找到足够原始证据的平面极限环/分岔结果只记已查集合缺口。

同日收录复评已取代上述初始入选决定：RL暂缓、AI Poincaré撤出，符号Lyapunov保留为方法样本。历史查阅事实保留；当前16候选、9组深读、1个补充条目。详见[收录复评](2026-09-20-dynamics-adjudication.md)。
