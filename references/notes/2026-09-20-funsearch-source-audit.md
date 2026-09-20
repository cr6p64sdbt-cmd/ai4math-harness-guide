# FunSearch 原始来源与有限证书检查记录

日期：2026-09-20；access mode：`OPEN-ONLY`；用途：程序搜索路线教学深读。阅读状态：`section-summary`，另有明确限定到 512 点数据的精确检查。本记录不是原文转译。

## 来源、版本和实际范围

| 来源 | 版本/定位 | 实际读取与用途 |
|---|---|---|
| [论文 DOI](https://doi.org/10.1038/s41586-023-06924-6) | Nature 2023 online publication | 原链接及 DOI 路由均遇 idp 重定向抓取失败，未取得该页面正文，不将失败解释为论文不存在 |
| [官方博客](https://deepmind.google/blog/funsearch-making-new-discoveries-in-mathematical-sciences-using-large-language-models/) | 2023-12-14，页面有 2024 更新 | 仅用于发现作者稿的官方开放链接；2024 更新不倒填 2023 案例 |
| [作者接受稿 PDF](https://storage.googleapis.com/deepmind-media/DeepMind.com/Blog/funsearch-making-new-discoveries-in-mathematical-sciences-using-large-language-models/Mathematical-discoveries-from-program-search-with-large-language-models.pdf) | 64 个 PDF 页，含封面及补充材料 | 读 §1、§2.1、Methods A.1、Supplementary A.3/A.5/E.1/E.2；不是全篇逐行复核 |
| [官方结果库](https://github.com/google-deepmind/funsearch/tree/cc53f274237d7ab05c19df939edbc1f9616a7c19) | commit `cc53f274237d7ab05c19df939edbc1f9616a7c19`，GitHub API 查询当前 main 后冻结 | README、implementation 文件和 cap-set notebook/数据；没有执行任何外部代码 |

本地 PDF：[romera-paredes-2023-funsearch-author.pdf](../papers/romera-paredes-2023-funsearch-author.pdf)，SHA-256：`bfb903bf99a6ad6633e2f12869ddd9fb2abcb8babfa83783b6aaa41f62b91fd0`。官方说明为作者接受稿，供个人使用、不再分发；文件被 Git ignore。取得路线为官方博客的开放作者稿链接，不绕过 Nature 登录。

## 关键定位

- PDF 第 3–7 页（正文 §1、Figure 1–2）：输入规范、程序库、prompt、执行反馈和分布式方法。
- PDF 第 7–10 页（§2.1、Figure 4–5）：cap set 定义、496→512、人工解释与 admissible-set 对称性。
- PDF 第 17 页（Methods A.1）：按分数排列两个函数、island 采样和四小时重置。
- PDF 第 31 页（Supplementary A.3/Figure A.3）：八维 140 次实验，4 次达到 512。
- PDF 第 33 页（Supplementary A.5）：admissible-set 两百万样本的历史费用估算；不等于 cap-set 单例账单。
- PDF 第 50–51 页（Supplementary E.1/E.2、Table E.2）：140 evaluators 等配置以及人工抽取反射规律。正文约 150 与表中 140 分开记录。

代码均固定到上述 commit：

- [config.py](https://github.com/google-deepmind/funsearch/blob/cc53f274237d7ab05c19df939edbc1f9616a7c19/implementation/config.py)：默认 2 functions/prompt、10 islands、4h reset、15 samplers、140 evaluators、4 samples/prompt。
- [funsearch.py](https://github.com/google-deepmind/funsearch/blob/cc53f274237d7ab05c19df939edbc1f9616a7c19/implementation/funsearch.py)：`main` 接口、装饰器抽取、单线程第一个 sampler 无限循环。
- [sampler.py](https://github.com/google-deepmind/funsearch/blob/cc53f274237d7ab05c19df939edbc1f9616a7c19/implementation/sampler.py)：模型接口未实现；`sample` 循环。
- [evaluator.py](https://github.com/google-deepmind/funsearch/blob/cc53f274237d7ab05c19df939edbc1f9616a7c19/implementation/evaluator.py)：`Sandbox.run` 未实现、装入模板、检查执行与评分；不是通用数学真值判断。
- [programs_database.py](https://github.com/google-deepmind/funsearch/blob/cc53f274237d7ab05c19df939edbc1f9616a7c19/implementation/programs_database.py)：`Island`、`Cluster`、`_generate_prompt`、`reset_islands`。
- [cap_set.ipynb](https://github.com/google-deepmind/funsearch/blob/cc53f274237d7ab05c19df939edbc1f9616a7c19/cap_set/cap_set.ipynb)：按零起 cell index，2 是骨架，6 是发现函数，8 是原作者检查器，12 是人工显式构造；本批只读其 JSON 源文，未执行。

## 独立有限检查

数据来源：[n8_size512.txt](https://raw.githubusercontent.com/google-deepmind/funsearch/cc53f274237d7ab05c19df939edbc1f9616a7c19/cap_set/n8_size512.txt)。本地 [数据](../data/funsearch-n8-size512.txt)保持下载原始 bytes，12800 bytes；SHA-256 `8d6df45c3039b6a7ee1aae7216b100c3f4c075179dc6471f4f51b968a26d8905`。作者：Google DeepMind / FunSearch 团队；仓库声明非软件材料为 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)，本地文件未改动。该数学数据用于有限证书检查，非完整源码复制。

独立编写 [check_funsearch_capset.py](../../scripts/check_funsearch_capset.py)，仅用 Python 标准库；JSON 解析数值行，不 `eval` 或执行下载程序。精确检查所有不同点对的模 3 第三点，并检查坐标域、维数与唯一性。

实际运行 `python scripts/check_funsearch_capset.py`：正常 exit 0；512 点、8 维、130816 对、`PASS`，并通过合法/共线/重复/域外坐标控制样本。数学接口：任意不同 $x,y$ 的第三点唯一为 $-x-y$，在特征 3 下它不等于 $x,y$，所以检查覆盖全部不同三点。

证据仅闭合**冻结点列表是一个 512-cap**；没有检查搜索过程、新颖性、最大性、全部维数或渐近 bound。本批整体案例不提升为 `PROVED`。

## 实际检索与未检查项

查询包括 `Mathematical discoveries from program search arxiv pdf`、`site.github.com google-deepmind funsearch cap_set 512`。第三方命中只作 locator；最终回到官方博客、作者稿与官方仓库。GitHub API 用来读取 main SHA 与 tree，raw URL 用来只读源码和数据。

PDF 首次文本打印受 Windows GBK 输出限制中断，改用 `python -X utf8` 后成功；不把第一次失败当已读内容。没有完整重放发现实验，没有下载模型或安装环境，没有订阅数据库检索或全领域引用闭合。
