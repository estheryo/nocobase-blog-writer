---
name: nocobase-blog-writer
description: 按 NocoBase 官网博客「AI & No-Code」栏目的真实写法，产出自然、没有 AI 腔、SEO/GEO 友好的英文或中文文章，类型包括 GitHub 开源工具盘点、替代品/竞品对比、「用 AI + NocoBase 搭建 X」教程和概念解读。凡是给 NocoBase 写博客、SEO 文章、选型文、榜单、对比文、教程或长文落地页，或要给这类文章出大纲、改写、去 AI 味、做 SEO 检查，都使用这个技能，即使用户只说「写一篇关于 X 的文章」「出个选题大纲」「这篇读起来太像 AI 了」。Use it for any NocoBase blog post, SEO article, listicle, alternatives/comparison post, tutorial or rewrite, in English or Chinese.
---

# NocoBase 博客写作（AI & No-Code 栏目）

这个技能来自对官网博客「AI & No-Code」分类全部 147 篇文章（2024–2026，中英文各一份）的逐篇统计和精读。目标是写出读者分不出是不是 AI 写的、可以直接发布的 SEO 文章。

**以 2026 年的文章为范本，2024 年的文章是反面教材。** 同一个栏目，写法两年间变化很大：

| 指标（英文） | 2024 年 | 2026 年 |
|---|---|---|
| 空洞形容词（seamless、robust、comprehensive、powerful、streamline、leverage…）每千词 | 6.35 | **0.33** |
| 篇幅中位数 | 1,986 词 | **2,706 词** |
| 带对比表的文章 | 38% | **63%** |
| 带 FAQ 的文章 | 0 篇 | **21/43 篇** |

中文版同样如此：2024 年「强大」「灵活」「无缝」「轻松」「高效」随处可见，2026 年几乎消失。

## 四条底线

1. **不编造任何事实。** 这个栏目的说服力来自真实信息：真实的 Reddit/HN/X 讨论（带链接）、当天查到的 GitHub Stars、官网公开价格、产品文档里写着的功能。写之前去查（GitHub API、官网、文档、WebSearch）。查不到的就标 `【待核实：…】` 交给人工，绝不臆造帖子、引语、数字或客户案例。AI 写稿最容易在这里出事，一处编造就会毁掉整篇的可信度。
2. **先具体，后抽象。** 每个判断后面紧跟一个具体例子：真实的业务对象（客户、合同、工单、发票）、真实的角色（销售、财务、项目经理）、真实的流程（`Lead → Opportunity → Quotation → Closed deal`）。泛泛的形容词换成「它能做什么、给谁用、在什么场景」。
3. **克制、公平地写竞品。** 先客观讲清别人擅长什么，再说差异和局限；推荐 NocoBase 时附上条件（「如果你的目标是 X，可以先看 NocoBase」），不用 best、No.1 这类自封的说法。
4. **分清 NocoBase 3 和 NocoBase 2。** 文章里的「NocoBase」默认指 NocoBase 3，即官网说法「面向 Agent 的开发平台」：Agent 在 Core 上写代码，Studio 负责治理。NocoBase 2 是「AI + 无代码开发平台」：界面配置，有 AI 员工。两个版本的能力、术语、链接、价格都不一样。写无代码、可视化搭建、AI 员工这类主题时，明确写「NocoBase 2」。规则见 `references/nocobase-facts.md` 第 2 节。

## 工作流程

### 1. 明确任务

动笔前确认下面几项。用户只给了题目时，自己推断合理默认值，用三五行列出来请用户确认，然后继续，不要一连串追问。

- **主关键词和搜索意图**：读者搜什么，想解决什么问题
- **文章类型**：A 开源工具盘点 / B 替代品与对比 / C 搭建教程 / D 概念解读（见下表）
- **目标读者**：开发者、IT 负责人、业务团队、外包/集成商
- **语言**：英文、中文，或两版都要（中英文结构一致，标题和措辞各自本地化，见 `references/voice.md`）
- **NocoBase 的角度和版本**：这篇文章里 NocoBase 解决读者的哪个具体问题，用到哪些能力。写的是 NocoBase 3（默认）还是 NocoBase 2（无代码、AI 员工类主题）。产品说法、术语和链接以 `references/nocobase-facts.md` 为准
- **开头素材**：一条真实的社区讨论或行业现象；没有就去找（Reddit、Hacker News、X、Google Trends）

### 2. 调研

- **先查重**：在 `references/existing-posts.md` 里搜主关键词和近义词（比如 retool、appsmith、crm、ticket）。已经有同主题旧文时，按那个文件开头的规则处理（通常是建议在原 URL 上改写），并写进交付说明。不查重，新文章会和旧文互相抢排名
- 在 WebSearch 里搜主关键词，看排名前列的文章覆盖了什么、缺什么。我们要补上它们没讲清的部分（真实场景、成本、权限和长期维护）
- 找开头素材：真实社区讨论优先；打不开 Reddit 时的备选来源见 `references/article-types.md`「通用开头」
- 逐个核实要写的产品：官网、文档、价格页、GitHub 仓库、Stars（用 `https://api.github.com/repos/<owner>/<repo>` 取 `stargazers_count`，写成 `22.7k` 并在交付说明里注明查询日期）
- 从 `references/internal-links.md` 挑 8–15 篇相关旧文做内链

### 3. 列大纲

按 `references/article-types.md` 对应类型的骨架列大纲，H2/H3 用那里的固定说法。文章超过 2,000 词时，先把大纲给用户看一眼再写。

### 4. 写作

按 `references/voice.md` 写。写之前读一遍那里的「改写对照」，比读规则更快找到感觉。

参考文件里的例句都摘自已发布的文章，学的是结构和语气，**不要原样搬进新文章**。照抄几次，整个博客就会变成同一个模板。

### 5. 自检

1. 运行 `python3 scripts/check_article.py <文章.md>`（脚本路径相对本技能目录），按提示修改：空洞词、过长段落、标题和描述长度、缺失的模块
2. 对照 `references/seo-checklist.md` 过一遍
3. 只读开头三段和结尾两段，问自己：像不像一个做过这件事的人在讲话？有没有一句话换个产品名也成立？有的话就改到只适用于这篇文章

### 6. 交付

输出一个 Markdown 文件，格式如下：

```markdown
---
title: <SEO 标题，50–60 字符>
slug: <小写-连字符-关键词>
description: <meta description，120–155 字符>
primary_keyword: <主关键词>
secondary_keywords: [<2–5 个>]
category: AI & No-Code
author: <作者，写法和官网一致，如 Deng Lijia、Yuan Tianqi、Zhang Lu>
---

# <H1，可以和 title 不同，但必须包含主关键词>

<正文>
```

正文之后附一段「交付说明」（不发布），包括：
- 需要补的截图清单：文件名用英文描述词（如 `nocobase-crm-opportunity-board.png`）+ alt 文本
- 所有 `【待核实】` 项，以及 GitHub Stars 和价格的查询日期
- 两版都要时，另一种语言的标题和 description 建议

## 四种文章类型

| 类型 | 标题模式（真实例子） | 适用场景 |
|---|---|---|
| **A. 开源工具盘点** | `Top 8 Open Source AI Assistant Tools by GitHub Stars` / `After Claude Code: 6 Open-Source Tools You Should Know` | 某个热门话题、热门 AI 工具，或某个 GitHub topic 下的高星项目 |
| **B. 替代品与对比** | `How to Choose a Smartsheet Alternative: 7 Tools Compared` / `NocoBase vs Baserow: Flexible Databases vs Enterprise Systems` | 读者已经在用或在评估某个产品，想找替代或做选型 |
| **C. 搭建教程** | `How to Build a Production-Ready CRM with AI and NocoBase` / `How to Design an IT Asset Management System: Data Model, Lifecycle, and Workflows` | 用一个具体业务系统演示「AI + NocoBase」从需求到上线 |
| **D. 概念解读** | `What Is AI No-Code? A Practical Guide to No-Code Platforms in the AI Era` | 新概念、新趋势，读者想先搞懂再选工具 |

每种类型的完整骨架、固定小标题（中英文）和段落写法见 `references/article-types.md`。

## 语气要点（细则见 `references/voice.md`）

- **短段落**：英文段落中位数约 20 词，一段 1–3 句；转折处用单句成段（`But code is not the same as an application.`）。句子平均约 15 词
- **人称**：编辑动作用 we（`we selected`、`we came across`），对读者说话用 you；第一人称故事型开头可以用 I
- **措辞克制**：`better suited to`、`relatively`、`should still confirm whether…`；不用 seamless、robust、powerful、comprehensive、game-changer、unlock、empower、delve、In today's fast-paced world、In conclusion
- **中文**：不用「赋能」「助力」「无缝」「强大」「轻松」「打造」「一站式」「降本增效」「综上所述」；举例用「比如」「例如」
- **emoji 只做功能标记**：💬 栏目说明、💡 延伸阅读、🎉 产品公告、🚀 在线体验、⭐/❤️ 文末分享；正文里不装饰
- **破折号少用**：英文每千词不超过 1 个，改用逗号、冒号或句号

## NocoBase 在文中的位置

- 栏目说明句（💬 那一行）放在开头场景之后、第一个正文 H2 之前，原文见 `references/nocobase-facts.md`
- 盘点和对比文里 NocoBase 排第一、写得更深，但小标题结构和其他产品一致，不搞特殊版式
- 讲 NocoBase 时落到具体能力和具体场景，不写口号。NocoBase 3 常用：现成构件让 Agent 只写业务部分、统一的项目结构和开发规范、变更就是代码（可评审、可回滚）、业务 Agent、Studio、自托管。NocoBase 2 常用：可视化搭建、工作流画布、AI 员工。完整清单见 `references/nocobase-facts.md` 第 6 节
- 术语按官方术语表：英文正文里 agent 小写，business agent（NocoBase 2 叫 AI employee）；中文写「Agent」「业务 Agent」，不写「智能体」「代理」
- FAQ 里有 1–2 个问题按使用场景推荐 NocoBase，最后一个问题可以直接问 NocoBase（比如「Is NocoBase only for enterprises?」）

## 参考文件

| 文件 | 什么时候读 |
|---|---|
| `references/article-types.md` | 列大纲前，读对应类型那一节 |
| `references/voice.md` | 写作前；改写别人的稿子前 |
| `references/seo-checklist.md` | 定标题、slug、description 时；交付前自检 |
| `references/nocobase-facts.md` | 写到 NocoBase、放 CTA 和产品链接时 |
| `references/existing-posts.md` | 调研第一步：查有没有同关键词旧文 |
| `references/internal-links.md` | 选内链和文末「Related reading」时 |
| `scripts/check_article.py` | 每次交付前运行 |
