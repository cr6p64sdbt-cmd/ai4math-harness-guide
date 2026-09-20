# 第二批扩充：检索范围与执行记录

日期：2026-09-20；状态：本批检索与资料扩充完成；数学验收范围见各案例。

用户要求按价值和重要性扩充四个深读，分类后补充证据或成果较有限的样本，并特别标注平面ODE、动力系统相关工作。采用process-math-pdfs的分阶段检索；公开来源、只读外部代码，不执行外部harness。

## 本批约定

- 优先级分开评价：数学成果重要性、证据成熟度、方法可学习性、与用户方向的相关性；不把较低学习优先级写成系统普遍较弱。
- 首先扩充QED、AlphaEvolve的具体成果，再加入机制透明的Albilich；动力系统定向检索Lyapunov函数、守恒量、自相似奇性、分岔和极限环。最终深读数量由可读原始来源决定，不限定四席。
- 相关性分为：直接ODE/动力系统问题、相邻PDE分析、通用方法迁移、无直接相关。平面ODE必须实际存在二维有限维系统，二维PDE不算平面ODE。
- 排除仅语言润色；区分研究级新结果、已知结果重证明/形式化、有限构造改进、数值发现及基准表现。
- 停止：完成至少三组新增通用系统/案例，并取得至少一个直接动力系统样本的详细来源；再补有限数量对照条目。没有查到AI解决平面极限环开放问题时只报告已查集合缺口。
- 发现路线：本地候选与上一批来源→公开搜索→官方论文/作者代码→相关工作和作者后续材料。没有机构订阅或全面引用索引，不作新颖性穷尽判断。

## 已执行的主要查询

- `AI mathematics discovery planar differential equations limit cycles Lyapunov symbolic regression new mathematical results`
- `machine learning discovery unstable singularities fluid dynamics 2025 2026 Buckmaster Lai Wang Gomez Serrano`
- `AI mathematician dynamical systems bifurcation QED research mathematics 2026`
- `site:arxiv.org "Global Lyapunov functions" symbolic transformers`
- `site:github.com "Lyapunov" "facebookresearch"`
- `site:arxiv.org Alpoge Buckmaster "forcing" 2026 blowup`
- `site:arxiv.org "AI" "limit cycles" planar`

搜索摘要和社区帖子只定位，不接受其“解决百年难题”等宣传判断。实际阅读与选择结果如下。


补充查询：`Analytical Lyapunov Function Discovery github`、`AI Poincare 2.0 github conservation`；QED、Albilich、AlphaEvolve按系统名、案例名、论文编号及官方仓库扩展。各分支的详细查询见下列收据；没有使用订阅引文数据库。

## 实际成果与筛选

|对象|决定及理由|来源、版本和阅读位置|
|---|---|---|
|QED|新增详细系统/输运扩散案例；研究级分析、过程可解释|[收据](2026-09-20-qed-expansion.md)|
|Albilich|新增详细系统/21.142案例；长期状态和集成机制清楚，保留数据冲突|[收据](2026-09-20-albilich-expansion.md)|
|AlphaEvolve|新增详细系统/复矩阵48项案例；最终工件可精确验算|[收据](2026-09-20-alphaevolve-expansion.md)|
|符号Lyapunov|新增详细系统/平面证书案例；直接ODE且可手算|[动力系统收据](2026-09-20-dynamics-source-audit.md)|
|PINN奇性|新增详细系统/数值候选案例；展示不同AI范式与验证边界|[动力系统收据](2026-09-20-dynamics-source-audit.md)|
|RL Lyapunov、AI Poincaré|两条补充对照；有定向价值但阅读较浅|[补充说明](2026-09-20-dynamics-adjudication.md)|
|fluid_lean|高价值来源剖面；原始数学/形式化工件可读，完整harness材料不足|[收据](2026-09-20-fluid-lean-source-audit.md)|

增加五个候选（两项新增深读、三项补充），原候选中三项升级深读：合计18候选、9组深读、3补充条目。保留两组历史档案不当作本批刷新。增加五张事件卡，共11张；三补充条目没有进入事件统计。方法分类见[优先阅读](../../guides/PRIORITIES.md)，方向标签见[专题](../../guides/DYNAMICAL-SYSTEMS.md)。

## 关键复核与证据缺口

主控核对QED原文Theorem2.1与傅里叶截止结论、Albilich数学Theorem1.1与最终路线，以及公开归档自审。其他定理范围和固定源码阅读见委派产物，不以角色名替代证据。AlphaEvolve新增独立整数脚本，对固定SHA-256数据的4096系数检查通过；没有执行外部notebook。符号Lyapunov对真实函数给完整初等推导；RL Van der Pol的半负导数另补不变集理由。没有审完整PDE/群论/几何证明，没有重放Lean。

fluid_lean论文加强条件与形式顶层的差别、Boussinesq的未审查标记、强迫条件均保留。PINN后续梯度归一化与原始运行分开；没有把其他流体形式化拼接为它的数值候选的严格证明。缺少的prompts、精确commit、成本和日志均写未知或已查集合未找到。

已达到本批停止条件，不继续堆积候选。未核平面极限环/分岔新证明，不能断言不存在；下次可按明确问题继续做定向检索。文件链接、元数据与统计最终验收结果见[当前状态](../../STATUS.md)。

最终文件验收：306个本地Markdown链接无缺失；九组元数据、事件关联与架构图通过；18条候选、11系统、12案例/剖面、11事件计数一致。统计--check与Git空白检查通过。首次检查器按系统ID单一格式判断，遇历史Danus路径表示后改为兼容既有两种表示再通过；未改统计schema。

同日收录复评已取代上述初始入选决定：RL暂缓、AI Poincaré撤出，符号Lyapunov保留为方法样本。历史查阅事实保留；当前16候选、9组深读、1个补充条目。详见[收录复评](2026-09-20-dynamics-adjudication.md)。
