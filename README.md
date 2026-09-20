# AI4Math harness 学习仓库

这是一个中文、按需更新的 AI 数学研究方法学习仓库。重点是理解公开 harness 怎样安排任务、调用模型和工具、保存研究状态、处理失败与组织验证。数学成果只作简要筛选与背景介绍；各系统的作者声明、公开证据和本仓库判断分别记录。

## 从哪里开始

1. [项目首页与阅读路径](INDEX.md)：候选、系统、案例及专题的总导航。
2. [Danus 最新公开版全框架教程](systems/danus/FRAMEWORK-GUIDE.md)：多路探索、持久 workers、事实图、依赖撤销和成稿。
3. [QED 全框架教程](systems/qed/FRAMEWORK-GUIDE.md)：证明计划、分层核验、三级重试和恢复。
4. [方法比较](guides/COMPARISON.md)及[来源与复用索引](references/SOURCES.md)：选择其他系统并追溯论文、固定代码版本和配置。

与平面 ODE、动力系统有关的材料见[专题入口](guides/DYNAMICAL-SYSTEMS.md)。★表示平面 ODE 直接相关，◇表示相邻 PDE；“方法可能迁移”不等于已有该方向研究成果。

## 怎样在自己的项目中使用

本仓库可以作为不同 agent 应用的参考材料。能读取网页的 agent 可直接访问上述链接；能读取本地文件的 agent 可使用克隆后的目录。不能直接访问 GitHub 时，也可以通过仓库页面的 **Code → Download ZIP** 下载解压，再把相关 Markdown 文件提供给它。

建议先读 `INDEX.md` 和 `guides/COMPARISON.md`，选一个相关系统，再读其教程与 `references/SOURCES.md`。让 agent 结合你项目已有的规则和工具，挑选少量机制融入现有流程，并用一个小任务检查任务交接、状态保存和反馈是否顺畅。具体文件位置、角色名称和工具映射交给你的 agent 判断，无须照搬整套目录。

可以阅读或复制需要的教程、系统档案、模板和统计脚本。复制后保留来源和版本链接，并按 [LICENSE.md](LICENSE.md) 的范围标注出处。每篇系统教程都应先看固定 commit、公开程度和缺失信息；这里的介绍不替代实际运行测试。

`AGENTS.md` 与 `WORKFLOW.md` 是**本仓库的工作规则**。若你的项目已有规则，先比较并选择需要的条款，不要直接覆盖。教程中的上游命令和配置用于理解原系统；是否安装、运行或接入自己的研究环境，应另作决定。

把下面这段话交给你自己的 agent，即可让它按你的研究目标挑选和吸收方法：

> 请阅读 https://github.com/cr6p64sdbt-cmd/ai4math-harness-guide 的 README、INDEX、相关系统的教程和 references/SOURCES.md。结合我项目已有的目标、规则与工具，选择最适合借鉴的 1–2 个 harness 机制；仅在缺少必要信息时向我提问。简要说明来源、对应版本和需要的改动，并在我的授权范围内融入现有流程，用一个小任务检查接入是否有效。保留原项目规则，不要整套覆盖 AGENTS.md/WORKFLOW.md，也不要把作者声明或 LLM 检查当作数学证明。

如果只想阅读材料，无须安装原 harness。需要运行原系统时，请回到各篇教程的固定版本和上游仓库核对环境、权限与成本。

可以用 Git 克隆整个仓库：

```bash
git clone https://github.com/cr6p64sdbt-cmd/ai4math-harness-guide.git
```

项目默认不跟踪第三方论文 PDF、运行时目录或凭据。PDF 请从[来源索引](references/SOURCES.md)中的原始入口获取；随仓库提供的第三方结果数据有单独的来源及许可说明，见 [LICENSE.md](LICENSE.md)。

## 内容状态

截至 2026-09-20，仓库收录 16 个候选、9 组系统及成果背景档案、2 篇完整框架教程。候选不等于成功案例，模型或 LLM verifier 给出的 PASS 也不等于数学证明。当前状态、已核来源和缺口见 [STATUS.md](STATUS.md)。
