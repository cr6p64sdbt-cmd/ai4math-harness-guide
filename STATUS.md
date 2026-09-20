# 当前状态

更新：2026-09-20。状态：`PUBLIC-REPOSITORY-PUBLISHED`。

## 当前目标与用户澄清

学习已有 AI4Math 成果背后的 harness。**数学只做简要筛选，排除明显薄弱条目；不默认核对证明、读生成数学论文或重放证书。** 用户原话及解释已补录到[PROJECT-BRIEF.md](PROJECT-BRIEF.md)，并同步 AGENTS、WORKFLOW 和模板。此前过度展开的数学审查不再驱动默认后续任务。

## 本轮交付

- **[Danus 最新公开版全框架教程](systems/danus/FRAMEWORK-GUIDE.md)**：22节，覆盖新版主控、探索与证明双通道、三层记忆、提交、依赖撤销、worker循环、停止恢复、配置及论文/报告流程；含教学例子与QED比较。
- 2026-09-20再核官方默认分支为codex，HEAD仍为 `6d92e8d415933ca2ef52fd1a4da73fdfcd418f1c`（2026-08-27）。[版本确认](references/notes/2026-09-20-danus-latest-version.md)区分latest release、标签和当前HEAD；不宣称上游刚更新。
- [事实/验证/记忆定位](references/notes/2026-09-20-danus-state-map.md)、[运行/成稿定位](references/notes/2026-09-20-danus-runtime-map.md)：两个有界子代理分工，主控整合并抽查提交闸门、worker停止和写作默认值。未展开数学审查。
- [QED 全框架教程](systems/qed/FRAMEWORK-GUIDE.md)保留作对照。目前共2篇完整框架教程，既有9组系统/成果背景档案不自动算成9篇完整教程。
- 阅读入口已同步：INDEX、START-HERE、PRIORITIES、COMPARISON、DYNAMICAL-SYSTEMS、CANDIDATES、SOURCES、Danus概览；PROJECT-BRIEF补录本次要求。

## 存量材料与边界

候选目录仍为16项；11篇顶层系统档案、12篇案例/剖面、11张事件卡，其中含2组旧Astra/Claude记录和1篇补充fluid_lean剖面。原9组系统/案例包括 Danus、ProofCouncil、Aristotle、FunSearch、QED、Albilich、AlphaEvolve、符号Lyapunov、PINN。候选数不是成功成果数。

此前 FunSearch/AlphaEvolve 有限证书检查、若干案例定向数学复评保留在各原始记录，不在本轮重复验证。RL暂缓、AI Poincaré撤出推荐的记录保留为历史选择，本轮不重审或自动恢复。旧四周试点按实际1篇周报结束，不补造记录。

QED 的讲解基于 `121900964e6572aaf094412d434b5ac2a792a65f`。本轮静态阅读，没有运行验证；上层成功标记和恢复分支的局限已说明。当前配置不能倒填历史数学案例，历史调用、人类干预和费用资料仍不完整。流程完整介绍不等于效果已由本项目实验确认。

## 验收与后续入口

当前所有教程只读公开源码，不代表已试运行。Danus最新契约的30分钟/4小时复盘与旧操作文档有漂移，正文已说明；纯文本数学限制、MCP与宿主权限差别、停止与恢复接口分别讲清。数学成果仅复用既有背景，未新增证明检查。

本轮361个本地Markdown链接无缺失；Danus教程22节、319行，引用标签全部有定义；官方链接固定到已核HEAD。`python scripts/build_stats.py --check`通过，11张事件卡统计一致；`git diff --check`通过，仅既有换行转换提示。无新增事件，不改统计接口。

公开仓库：[cr6p64sdbt-cmd/ai4math-harness-guide](https://github.com/cr6p64sdbt-cmd/ai4math-harness-guide)。[README](README.md)介绍下载与导入，[LICENSE.md](LICENSE.md)说明本项目文字、代码和第三方数据的复用范围。第三方论文 PDF、凭据和运行缓存没有进入 Git。

后续从[首页](INDEX.md)进入 Danus，再对照 QED；继续介绍其他系统时按价值选材料，不把数学审查缺口自动变成下轮任务。未安装或运行外部harness，未写其他研究项目，未创建自动化。
