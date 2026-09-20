# QED 固定 commit 的运行与模型接口图谱

## 范围与证据

本文只读取官方仓库 `proofQED/QED@121900964e6572aaf094412d434b5ac2a792a65f` 的 `README.md`、`run.sh`、`config.yaml`、`code/model_runner.py` 和 `prompts/` 活跃模板，并与本项目的 [QED 系统档案](../../systems/qed.md)及[扩展来源收据](2026-09-20-qed-expansion.md)对照。没有运行 QED、没有调用任何外部模型，也没有读取 `pipeline.py` 或 `decomposition_prover.py`；后两者负责的状态机和实际调用方由另一份接口分析覆盖。

固定来源入口：

- [README.md](https://github.com/proofQED/QED/blob/121900964e6572aaf094412d434b5ac2a792a65f/README.md)（本次引用行号均对应该 commit）。
- [run.sh](https://github.com/proofQED/QED/blob/121900964e6572aaf094412d434b5ac2a792a65f/run.sh)
- [config.yaml](https://github.com/proofQED/QED/blob/121900964e6572aaf094412d434b5ac2a792a65f/config.yaml)
- [code/model_runner.py](https://github.com/proofQED/QED/blob/121900964e6572aaf094412d434b5ac2a792a65f/code/model_runner.py)
- [prompts/](https://github.com/proofQED/QED/tree/121900964e6572aaf094412d434b5ac2a792a65f/prompts)

## 用户入口：输入、参数和输出

| 接口事实 | 固定文件位置 | 准确含义 |
|---|---|---|
|默认命令|`README.md` L243–266；`run.sh` L1–9、L25–36|先把 LaTeX 题面放在 `problem/problem.tex`，执行 `bash run.sh`。脚本将 Python 解析为 `conda run -n agent which python`，所以环境名固定为 `agent`。|
|位置参数|`run.sh` L7–9、L33–36|`$1` 覆盖题面路径，`$2` 覆盖输出目录，`$3` 覆盖配置路径；省略时分别为脚本目录下的 `problem/problem.tex`、`proof_output`、`config.yaml`。脚本把三者传给 `pipeline.py --input --output --config`。|
|启动前检查|`run.sh` L11–23|每次启动先运行 `code/smoke_test.py --config <config>`；然后创建输出目录的 `human_help/`，从仓库级 `human_help/*` 用 `cp -n` 补入尚不存在的文件。|
|题面约束|`README.md` L247–264|输入是 LaTeX 数学题面；示例使用 `problem` 环境。仓库文档没有在此入口声明更窄的语法校验。|
|输出|`README.md` L266、L529–561|最终证明为 `<output>/proof.md`。Medium/Hard 另有 `proof_effort_summary.md` 和 decomposition 工件；Easy 由 Stage 0 直接写 proof 并跳过 Stage 1/2。token 记录为根目录 `TOKEN_USAGE.md` 与 `token_usage.json`。|
|恢复|`README.md` L502–514|用同一输入、输出、配置命令重跑；文档声称会跳过已完成 survey，并从 decomposition 的 `attempt/revision/proof` 层级恢复。此处只是 README 行为声明，本笔记没有读取恢复实现。|

## 配置的当前有效值与继承

`config.yaml` 是该快照的实际示例配置；它不是历史 PDE 运行配置。全局字段如下（[config.yaml L12–47](https://github.com/proofQED/QED/blob/121900964e6572aaf094412d434b5ac2a792a65f/config.yaml#L12-L47)）：

| provider | 当前配置值 | 运行含义 |
|---|---|---|
|Claude|`cli_path: claude`；`permission_mode: bypassPermissions`；全局 `provider: api_key`；`api_key.model: claude-fable-5`；`api_key.key: ""`|默认走 API-key 分支但 key 为空；订阅和 Bedrock 分支也在文件中给出。配置的 `bypassPermissions` 是高权限示例，不能直接照搬。|
|Codex|`cli_path: codex`；`model: gpt-5.6-sol`；`reasoning_effort: xhigh`|Codex 全局默认。|
|Gemini|`cli_path: gemini`；`model: gemini-3.1-pro-preview`；`approval_mode: yolo`；`thinking_level: HIGH`；`api_key: ""`|空 key 表示依赖 CLI 已有登录；`yolo` 是高权限示例。|

`prover.mode` 当前为 `decomposition`，注释称只有该模式支持（[config.yaml L52–58](https://github.com/proofQED/QED/blob/121900964e6572aaf094412d434b5ac2a792a65f/config.yaml#L52-L58)）。Stage 0 `pipeline.literature_survey` 与 Stage 2 `pipeline.proof_summary` 当前均指定 Codex（[config.yaml L66–85](https://github.com/proofQED/QED/blob/121900964e6572aaf094412d434b5ac2a792a65f/config.yaml#L66-L85)）。decomposition 的六个角色为 decomposer、single_prover、regulator、structural_verifier、detailed_verifier、verdict；前两个显式写 `gpt-5.6-sol/xhigh`，其余只写 `provider: codex`，因此按配置注释继承全局 Codex 值（[config.yaml L94–123](https://github.com/proofQED/QED/blob/121900964e6572aaf094412d434b5ac2a792a65f/config.yaml#L94-L123)）。standalone verifier 的四角色也都指定 Codex（[config.yaml L125–140](https://github.com/proofQED/QED/blob/121900964e6572aaf094412d434b5ac2a792a65f/config.yaml#L125-L140)）。

重试/换路限额是配置显式值：`max_proof_attempts: 8`、`max_revisions: 4`、`max_decompositions: 4`（`config.yaml` L94–98）。README 的关键字段表把第一项注释成“default: 4”（[README.md L432–444](https://github.com/proofQED/QED/blob/121900964e6572aaf094412d434b5ac2a792a65f/README.md#L432-L444)），与该快照配置的 8 不一致；复用时应以实际传入配置为准，不把 README 注释当有效运行值。

README 规定每个角色是至少含 `provider` 的字典；其他字段覆盖对应全局 provider 字段，未设置的字段回退全局。Codex 可覆盖 `model/reasoning_effort`，Gemini 可覆盖 `model/thinking_level/thinking_budget`，Claude 只可覆盖模型字符串而认证模式仍由全局 `claude.provider` 控制（[README.md L398–430](https://github.com/proofQED/QED/blob/121900964e6572aaf094412d434b5ac2a792a65f/README.md#L398-L430)）。

## CLI 适配与返回值

`model_runner.py` 定义统一的 `ModelRunnerError`，保存 provider、错误类型、exit code、stderr、stdout，并提供截断显示和完整日志详情（L20–73）。三个 wrapper 都在 `asyncio` executor 中同步执行 `subprocess.run`，函数成功返回纯文本 response（模块说明 L1–9；统一分发 L659–707）。

| provider | 实际命令构造 | 成功响应解析 | token 统计与失败边界 |
|---|---|---|---|
|Claude|`claude -p --output-format json --dangerously-skip-permissions --model <model> [--append-system-prompt <instructions>] <prompt>`（L80–113）|将 JSON 的 `result` 作为 response；从 `modelUsage[*].inputTokens/outputTokens` 求和（L173–186）。解析失败时记录错误，退回原始 stdout（L186–192）。|继承环境先剥离 `CLAUDE_CODE_USE_BEDROCK/ANTHROPIC_API_KEY/AWS_PROFILE/ANTHROPIC_MODEL`，再叠加配置 env（L115–120）。subprocess 异常、非零退出、空响应最多共 3 次调用尝试；退避数组为 30/60/120 秒（不能理解为初次之外必有 3 次重试）（L132–165、L194–242）；成功后 tracker 记录 provider/model/tokens/耗时（L249–258）。|
|Codex|`codex --search -m <model> -c model_reasoning_effort="<reasoning>" exec --json --dangerously-bypass-approvals-and-sandbox -C <working_dir> <prompt>`（L265–297）|把 stdout 按 JSONL 解码；最后/遍历到的 `item.completed` 中 `item.type == agent_message` 的 `text` 作为 response；`turn.completed.usage.input_tokens/output_tokens` 累加（L333–351）。解析失败退回原始 stdout（L352–359）。|非零退出在已有非空 response 时只记 warning；没有 response 才抛 `non_zero_exit`（L361–381）。空响应抛 `empty_response`；成功或失败都会在可达路径记录 tracker（L383–407）。命令含 `--dangerously-bypass-approvals-and-sandbox`，属于高权限运行边界。|
|Gemini|`gemini -m <model> --approval-mode <approval_mode> -o json -p <prompt>`（L414–446）|解析 JSON 的 `response`；从 `stats.models[*].tokens` 累加 `input`，并把 `candidates` 与 `thoughts` 都算入 output（L524–539）。解析失败退回原始 stdout（L539–545）。|若设置 thinking 参数，临时创建 `qed-gemini-home-*/.gemini/settings.json`，写入模型匹配的 thinkingConfig，并通过 `GEMINI_CLI_HOME` 传给子进程（L448–488）；非零退出或空响应直接抛错（L547–577），完成后 tracker 记录（L579–587）。API key 若非空通过子进程环境 `GEMINI_API_KEY` 注入（L448–452）。|

按角色解析时，`resolve_agent_provider_config` 要求字典中有合法 `provider`，只接受 `claude/codex/gemini`；Codex/Gemini 做浅层全局字段覆盖，Claude 把 per-agent `model` 写入当前认证块，其余覆盖项写到 Claude 顶层（L594–652）。`run_model_for_agent` 再把合并后的 provider 配置交给统一 dispatcher；Claude 的 per-agent model 同时覆盖 `claude_opts`（L708–742）。因此配置能表达“每个角色换模型/推理参数”，但不能为单个 Claude 角色换认证模式。

## prompt 模板接口与返回格式

以下是模板文件自身明确的占位符和输出契约。实际由谁读取、如何替换占位符、调用顺序和工作目录，属于未读取的 `pipeline.py`，不能仅凭模板断言完整装配顺序。

| 模板 | 可核对的输入 | 要求的返回/文件格式 |
|---|---|---|
|`prompts/literature_survey.md`|题面 `{problem_file}`；输出根 `{output_dir}`；输出文件 `{difficulty_file}`、`{related_work_file}`、Easy 分支 `{proof_file}`；还给出 `{output_dir}/tmp/`（L151–187）|先输出 Easy/Medium/Hard 难度评估；Easy 必须直接写完整 `proof_file` 并停止，Medium/Hard 写 `related_work`。模板要求引用自检和固定 Markdown 标题（L13–50、L56–145）。|
|`prompts/decomposition-prover/decomposition.md`|模式 `{mode}`；题面、survey、`human_help`、plan history、当前 decomposition、上一轮 proof/verification、regulator guidance；路径占位符见 L77–148|输出写入 `{output_file}`，必须是指定 YAML 结构，包含 `problem_id`、带依赖的 steps、`key_steps`/`source_nodes` 和 `<cite>` 信息；CREATE/REVISE/REWRITE 有不同约束（L157–239）。|
|`single_prover.md`|题面、decomposition、survey、human guidance、上一轮 proof、上一轮 verification；`{output_dir}/tmp/`（L83–146、L329–348）|把完整证明写到 `{output_file}`，题面数学内容逐字复制；使用 decomposition 的 STEP ID；外部结果用完整 `<cite>...</cite>`，原创承重步骤用 `<key-original-step>...</key-original-step>`。文件还要求 scratchpad 和 deviation 区段（L159–220、L246–328）。|
|`proof_verify_structural.md`|题面 `{problem_file}`、证明 `{proof_file}`、计划 `{decomposition_file}`、全局规则和 `{output_dir}/tmp/`（L231–262）|输出 `{output_file}` 为 Phases 1–5 报告；逐项报告题面完整性、原创性、引用、计划遵循、key step 和额外规则，最终必须给 `Overall Verdict: PASS/FAIL`（L265–424）。|
|`proof_verify_detailed.md`|题面、证明、结构报告、计划、`{output_dir}/tmp/`（L136–167）|输出 Phase 6 逐 STEP 检查、key step、依赖链、coverage、assembly coherence，最终 `Overall Verdict: PASS/FAIL`（L170–280）。模板明确不重复做 citation/计划遵循检查。|
|`regulator.md`|模式、verification phase、当前状态、计划、proof、报告、attempt history、三个限额和 plan history（L1–147）|普通模式输出 `REVISE_PROOF`、`REVISE_PLAN` 或 `REWRITE` 的 Markdown 决策及指导；最终失败模式输出 failure analysis（L176–287）。若选 REVISE_PLAN/REWRITE，必须追加结构化 plan-history 条目。|
|`verdict_proof.md`|STRUCTURAL 模式读结构报告；FINAL 模式读验证报告（L1–61）|响应必须精确为单词 `DONE` 或 `CONTINUE`；任一 FAIL、报告缺失或不确定都应 `CONTINUE`（L61–85）。|
|`proof_effort_summary.md`|只读 output directory `{output_dir}` 中的全部生成文件（L56–76）|写 `{output_file}` 的 Markdown 总结，包含问题概览、最终状态、逐 attempt、路线、数学洞见、资源用量和 Pipeline Result（L9–54、L78–104）。|

README 还规定 proof 中 `<cite>` 必须包含类型、标题、作者、来源 URL、精确陈述和用途，原创非平凡步骤要用 `<key-original-step>` 包住（[README.md L478–493](https://github.com/proofQED/QED/blob/121900964e6572aaf094412d434b5ac2a792a65f/README.md#L478-L493)）。这是 prompt/验收格式要求，不等于数学证明已由形式化 kernel 验证。

## 依赖、成本与权限边界

- README 的前提是 Python 3.11+、PyYAML，以及至少一个 Claude/Codex/Gemini CLI；安装入口和 CLI 验证见 [README.md L170–218](https://github.com/proofQED/QED/blob/121900964e6572aaf094412d434b5ac2a792a65f/README.md#L170-L218)。`run.sh` 强制使用 conda 环境 `agent`，所以 Python 依赖必须装在该环境。
- 模型 CLI 是 npm 全局工具，认证由各 CLI/配置负责。Claude 可选 subscription、AWS Bedrock 或 API key；Gemini 可用 API key 或已有 CLI 登录；Codex 使用自身认证（[README.md L344–395](https://github.com/proofQED/QED/blob/121900964e6572aaf094412d434b5ac2a792a65f/README.md#L344-L395)）。本笔记没有验证这些账号或当前模型名是否仍可用。
- 权限风险来自代码实际命令：Claude 强制 `--dangerously-skip-permissions`，Codex 强制 `--dangerously-bypass-approvals-and-sandbox`，Gemini 默认来自配置的 `approval_mode: yolo`。这意味着复用前必须单独审查 CLI 账号、工作目录、网络、费用和可写权限；仓库公开源码本身不提供隔离保证。
- 每次调用的 stderr、响应片段、调用标签、耗时和 token 数可写入 pipeline 提供的 logger/tracker；README 说明日志包含完整 streaming output、工具调用、模型响应与 token stats，并维护 `TOKEN_USAGE.md`（[README.md L516–527](https://github.com/proofQED/QED/blob/121900964e6572aaf094412d434b5ac2a792a65f/README.md#L516-L527)）。这些是记录机制，不是价格结算；固定源码没有在这些接口里给出模型单价或总成本公式。
- README 的“每次调用为非阻塞 executor、从 JSON stdout 解析 token”与 `model_runner.py` 实现相符（[README.md L485–493](https://github.com/proofQED/QED/blob/121900964e6572aaf094412d434b5ac2a792a65f#L485-L493)；代码位置为 `model_runner.py` L122–130、L299–306、L481–497）。

## 明确缺口与不可从本接口图谱推出的事实

1. 未读取 `pipeline.py`，因此不能在本笔记中确认模板的实际替换函数、调用顺序、每个角色传入的 `claude_opts/instructions`、prompt 是否经过额外前后缀、或某个输出文件由哪个调用最终写入。
2. 未读取 `decomposition_prover.py`，因此不从这些 prompt 模板推断 attempt/revision/proof 的状态转移、恢复实现或 regulator 输出解析。
3. 当前 `config.yaml` 的模型和权限是 2026-08-16 快照的示例值；不能据此重建 2026-04/05 PDE 案例。已有来源收据明确记载历史模型冲突和缺少全量调用日志。
4. `model_runner.py` 的 JSON 解析与 tracker 记录证明“代码试图怎样记录 token”，不证明每个 CLI 版本都会输出完全相同 schema，也不证明 token 能换算成美元成本。
5. prompt 中的 PASS/DONE、专家评价或“rigorous”措辞是工作流输出契约；本项目仍按 `PROVED/CONDITIONAL/OPEN` 等数学证据等级独立判断，不能把模型返回格式当成数学证明。
