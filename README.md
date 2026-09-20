# AI4Math harness 学习仓库

这是一个中文、按需更新的 AI 数学研究方法学习仓库。重点是理解公开 harness 怎样安排任务、调用模型和工具、保存研究状态、处理失败与组织验证。数学成果只作简要筛选与背景介绍；各系统的作者声明、公开证据和本仓库判断分别记录。

## 从哪里开始

1. [项目首页与阅读路径](INDEX.md)：候选、系统、案例及专题的总导航。
2. [Danus 最新公开版全框架教程](systems/danus/FRAMEWORK-GUIDE.md)：多路探索、持久 workers、事实图、依赖撤销和成稿。
3. [QED 全框架教程](systems/qed/FRAMEWORK-GUIDE.md)：证明计划、分层核验、三级重试和恢复。
4. [方法比较](guides/COMPARISON.md)及[来源与复用索引](references/SOURCES.md)：选择其他系统并追溯论文、固定代码版本和配置。

与平面 ODE、动力系统有关的材料见[专题入口](guides/DYNAMICAL-SYSTEMS.md)。★表示平面 ODE 直接相关，◇表示相邻 PDE；“方法可能迁移”不等于已有该方向研究成果。

## 怎样在自己的项目中使用

可以阅读或复制需要的教程、系统档案、模板和统计脚本。复制后保留来源和版本链接，并按 [LICENSE.md](LICENSE.md) 的范围标注出处。每篇系统教程都应先看固定 commit、公开程度和缺失信息；这里的介绍不替代实际运行测试。

`AGENTS.md` 与 `WORKFLOW.md` 是**本仓库的工作规则**。若你的项目已有规则，先比较并选择需要的条款，不要直接覆盖。教程中的上游命令和配置用于理解原系统；是否安装、运行或接入自己的研究环境，应另作决定。

把下面这段话交给你自己的 agent，即可让它按你的研究目标挑选和吸收方法：

> 请阅读 https://github.com/cr6p64sdbt-cmd/ai4math-harness-guide 的 README、INDEX、相关系统的 FRAMEWORK-GUIDE 和 references/SOURCES.md。先问清我的数学任务、可用工具与验证要求，再列出最适合借鉴的 1–2 个 harness 机制：每项注明原始来源、对应版本、输入输出、状态管理、验证方式、公开证据缺口，以及接入我项目需要改动什么。先给可审阅的改造方案，不要直接覆盖我项目现有的 AGENTS.md/WORKFLOW.md，也不要把作者声明或 LLM 检查当作数学证明。

如果只想阅读材料，无须安装原 harness。需要运行原系统时，请回到各篇教程的固定版本和上游仓库核对环境、权限与成本。

可以用 Git 克隆整个仓库：

```bash
git clone https://github.com/cr6p64sdbt-cmd/ai4math-harness-guide.git
```

项目默认不跟踪第三方论文 PDF、运行时目录或凭据。PDF 请从[来源索引](references/SOURCES.md)中的原始入口获取；随仓库提供的第三方结果数据有单独的来源及许可说明，见 [LICENSE.md](LICENSE.md)。

## 内容状态

截至 2026-09-20，仓库收录 16 个候选、9 组系统及成果背景档案、2 篇完整框架教程。候选不等于成功案例，模型或 LLM verifier 给出的 PASS 也不等于数学证明。当前状态、已核来源和缺口见 [STATUS.md](STATUS.md)。
