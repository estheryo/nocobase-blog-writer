# 四种文章类型的骨架

每种类型都从 2026 年的真实文章归纳而来，例句均摘自已发布的文章。小标题请沿用这里的固定说法（英文 / 中文），读者和搜索引擎都会把它们当作可预期的结构。

目录
- 通用开头和结尾
- A. 开源工具盘点
- B. 替代品与对比
- C. 搭建教程
- D. 概念解读

---

## 通用开头和结尾

### 开头（第一个正文 H2 之前，150–350 词）

按优先级选一种：

1. **真实社区讨论**（最常用）：说清出处，概括发帖人的处境，必要时用列表总结评论区的两种观点，再引出本文。
   > Recently, we came across a discussion about alternatives in the Smartsheet community on [Reddit](…). The original poster works for a construction company with about 100 employees and belongs to a seven-person department. Previously, everyone managed projects according to their own habits…
   >
   > The comments showed that opinions about Smartsheet were mixed.

   中文：「最近，我们在 Reddit 的 Smartsheet 社区看到了一则关于替代方案的讨论。发帖者来自一家约 100 人的建筑公司……」

   要求：链接真实可点开；配一张截图占位 `![reddit-<主题>.png](…)`；转述而不是大段引用；不编造点赞数和原话。

   **打不开 Reddit 时**（部分环境会被拦截），按顺序找别的真实来源：
   - 用 WebSearch 搜 `site:reddit.com <主题>`，能看到摘要就记下链接，并在交付说明里标 `【待核实：Reddit 原帖内容】`，请人工打开确认
   - Hacker News（`https://hn.algolia.com/api/v1/search?query=<主题>`）
   - 产品官方社区论坛（如 `community.retool.com`）、GitHub Issues / Discussions
   - X 上的公开帖子
   - 都找不到时，改用第 2 种开头（读者熟悉的工作场景），配一个能查到出处的数据（Google Trends、公开报告）

   只引用自己打开核实过的内容，不凭搜索摘要补全对方没说过的细节。

2. **读者熟悉的工作场景**：
   > If you've worked on CRM systems, internal management systems, approval workflows, or admin dashboards, you're probably familiar with this experience: every project starts from scratch, and the same set of CRUD logic gets implemented all over again.

3. **一个反常识的问题**，下一句直接给答案：
   > Do you also think no-code belongs to the "pre-AI era"? … The answer is yes.

4. **接续系列**：在开头放 1–2 条 💡 链接，指向同系列的旧文，再说「这次我们看另一个方向」。
   > Over the past few weeks, we have organized several open source tools that work well with popular AI Agents:

开头的收尾用一句话说明本文怎么挑、讲什么：
> Based on these needs, we selected several representative Smartsheet alternatives, including open-source platforms. The following sections introduce each product's positioning, core capabilities, major differences from Smartsheet, pricing, and suitable team types.

接着放 💬 栏目说明（原文见 `nocobase-facts.md`）。

### 结尾

- 收束段：回到开头的问题，或总结 AI 与平台各自负责什么（2–4 句），不写「In conclusion」
- 分享句（一句）：
  > We hope this article helps you find a Smartsheet alternative that better fits your team. Feel free to share it with teams evaluating project management tools, open-source self-hosted platforms, or enterprise business systems.

  中文：「希望这篇文章能帮助你更快找到适合团队的 X。也欢迎分享给正在评估……的团队。」
- `Related reading:` / `相关阅读：` 列表，6–12 篇站内旧文

---

## A. 开源工具盘点

**标题**：`Top N Open Source <Category> by GitHub Stars` / `N Open-Source <Category> on GitHub Worth Watching` / `<Hot Tool> and N Open-Source Tools for <Use Case>` / `After <Hot Tool>: N Open-Source Tools You Should Know`
中文：`GitHub 上 Stars 最多的 N 个开源 X` / `在用 X 之后，你需要这 N 个开源工具`

**骨架**

```
## TL;DR（可选，2–3 句：结论 + 本文覆盖哪几类工具）
（开头场景 → 需求分成两三类 → 选取方法：「we collected high-star projects under GitHub's [topic] and selected N…」）
| Category | Project | GitHub Stars | Positioning |     ← 总览表，NocoBase 第一行
💬 栏目说明
## <分组名>（项目多时按类别分组，如 Enterprise AI Assistant / Personal AI Assistant）
## 1. NocoBase
Website / GitHub / Docs / Online Demo / Stars    ← 每项单独一行
![截图]
### Introduction（简介）
### Core features（核心特点）
### Suitable scenarios（适合场景）
## 2. <下一个项目>
…
## FAQ
## 1. What should you consider when choosing …?
## 2. If I want to …, which one should I choose?
…
⭐ 分享句
Related reading:
```

**每个项目的写法**
- Introduction 写两段：第一段说清它是什么，常用「It is more like a …」给出直观定位；第二段说它的价值在哪、和同类有什么不同
  > CopilotKit is a frontend framework for building AI Copilots, generative UI, and Agent applications. It is better understood as a development framework for in-app AI Assistants.
- Core features 写三条，格式为 `- 名称 : 一句解释`
  > - Containerized runtime : Agents run in independent containers, making it easier to isolate the file system and runtime environment.
- Suitable scenarios 写三条，每条是一个具体用法，不写「适合各种企业」
- NocoBase 这一节可以多 2–4 个要点，每个要点后面跟一段解释和一个例子。NocoBase 3 选这些：现成构件让 Agent 只写业务部分、统一的项目结构和开发规范、变更就是代码、业务 Agent、Studio 的 Agent 团队、自托管。盘点的是无代码工具时，介绍 NocoBase 2，选这些：AI 参与搭建、AI 员工、无代码继续维护、权限与工作流（见 `nocobase-facts.md` 第 2、6 节）

**FAQ**：5–7 题，按「如果我想做 X，该选哪个」来问，每题答案点名 1–2 个项目并说明原因。可以放一题专门问 NocoBase。

---

## B. 替代品与对比

**标题**：`How to Choose a <Product> Alternative: N Tools Compared` / `Best Open Source <Category>: A vs B vs C` / `A vs B: <差异点> vs <差异点>` / `Replace <X> with A or B? A Cost-by-Cost Comparison`
中文：`N 款 X 替代品：适合……的工具` / `A vs B：……与……`

**骨架（多产品替代品）**

```
（开头：先公平地讲被替代产品的长处 → 「However, a tool that works well at the beginning may not remain suitable for every stage…」→ 真实讨论 → 支持/反对两组要点）
（选取说明 + 「Before examining each product in detail, use the comparison table below…」）
| Product | Open Source | Primary Positioning | Similarities to X | Key Differences |
💬 栏目说明
## 1. NocoBase: For Teams <具体处境>
### Product Information（产品信息）    Website / Documentation / Pricing / GitHub / GitHub Stars
### What Is NocoBase?（NocoBase 是什么？）
### Why Can It Replace X?（为什么可以作为 X 替代品？）
### Key Differences From X（与 X 的核心差异）
### Which Teams Is It Best For?（适合哪些团队？）
🎉 产品公告（可选，blockquote）
## 2. <Product>: For Teams <具体处境>
…（同样五个 H3）
## Three-Year Pricing Summary（三年使用成本）   ← 说明计算口径：公开年付价、5 人和 15 人、三年
| Product | Reference Plan | 3-Year Cost for 5 Users | 3-Year Cost for 15 Users | Pricing Notes |
## FAQ（可选）
分享句 + Related reading
```

**写法要点**
- H2 格式固定为「序号. 产品名: For <团队/处境>」，一句话说明这个产品适合谁
- Key Differences 先讲被替代产品的方式，再讲这个产品的方式：
  > Smartsheet mainly uses worksheets as the collaboration entry point… NocoBase starts with a data model and then configures pages, permissions, operations, and workflows around that data.（这是 NocoBase 2 的写法）

  写 NocoBase 3 时，差异落在「代码和底座」上，比如：
  > Retool apps are configured inside Retool's builder. With NocoBase 3, the app is a code repository you own: agents write the business parts on Core's building blocks, such as permissions and approvals, and every change can be reviewed, tested, and rolled back.
- Which Teams 用列表写清条件（「Already use X to manage…」「Need different operating interfaces for…」），竞品也写同样具体的适用团队
- 诚实写局限：
  > However, teams that rely heavily on Smartsheet's task dependencies, resource management, and project portfolio capabilities should still confirm whether Airtable can cover their existing processes.
- 价格必须来自官网公开价格，写明方案名和计费方式，表格下面不写夸张结论

**两两对比（A vs B）**：按维度分 H2（Data / Pages / Permissions / Workflows / AI / Deployment / Pricing），每个维度先各讲一段再给小结；最后一节写 `How to Choose`，按读者情况分别推荐。

---

## C. 搭建教程

**标题**：`How to Build a Production-Ready <System> with AI and NocoBase` / `How to Design <System>: Data Model, Lifecycle, and Workflows` / `<System>: Vibe Coding vs NocoBase + AI`
中文：`如何用 AI 和 NocoBase 搭建一套可投入生产的 X` / `X 系统搭建指南：从需求梳理到落地`

**先定版本**。两个版本的搭建方式完全不同，步骤、截图和术语都不能混写：

| | NocoBase 3（默认） | NocoBase 2 |
|---|---|---|
| 搭建方式 | 用 NocoBase 模板创建应用（一个代码仓库），在应用目录里用 Claude Code、Codex 等编码工具描述需求，Agent 写 migration、页面（UI 组件库）、流程（记录生命周期）、权限 | 编码工具通过 CLI / Skills / MCP 连接 NocoBase 2，用 AI Builder 生成，之后在无代码界面里调整 |
| 检查方式 | 看 Agent 的改动、运行测试、在应用里实际操作；团队协作时用 Studio，Agent 附报告和截图交给人验收 | 在界面里检查数据表、页面和工作流配置 |
| 业务里的 AI | 业务 Agent（Agents 插件） | AI 员工 |
| 参考 | docs.nocobase.com 的 Core 入门教程 | nocode.docs.nocobase.com/ai-builder |

2026 年已发布的教程（CRM、IT 运维、工单、汽车租赁）都基于 NocoBase 2。新写的教程默认基于 NocoBase 3；如果要写 NocoBase 2 教程，标题或开头写明「NocoBase 2」。

**骨架**

```
## TL;DR（2–3 句：AI 能做到什么 + NocoBase 提供什么底座 + 结果）
## Background（背景）
（真实帖子：某人用 vibe coding 做了 X，前期很快，后来卡在权限、数据隔离、维护上 → 截图）
💬 栏目说明
（AI 能很快搭出框架，但离企业可用还有距离 → 「Today, however, there is another approach.」→ 「In this guide, we will show how…」）
🚀 在线 Demo 链接（可选）
## 1. Start with Real Business Requirements（从真实业务需求开始）
（一家具体的示例公司：行业、规模、团队、主要流程）
Lead → Company account → Opportunity → Quotation → Closed deal     ← 流程箭头单独成行
### Create the App and Connect Your Coding Tool（创建应用并接入编码工具）    ← NocoBase 3；NocoBase 2 写「Connect an AI Agent to NocoBase」
### Describe the Business in Natural Language（把业务情况整理成自然语言）
```prompt 代码块```
### Confirm AI's Understanding of the Business（确认 AI 对业务的理解）
## 2. Let AI Build <System>, Then Check the Core Business Logic（让 AI 搭建，并检查核心业务是否正确）
### Check <对象 A>   ### Check <对象 B>  …（每节：应该是什么样 → 截图 → 不对时怎么让 AI 改）
## 3. Turn the Basic <System> into a System the Team Can Actually Use（完善成团队真正使用的系统）
### Configure Permissions Around Team Responsibilities（按团队分工设置权限）
### Turn Repetitive Rules into Workflows（把日常规则配置成工作流）
### Add Business Agents for <场景>（配置业务 Agent）    ← NocoBase 2 写「Configure AI Employees」（配置 AI 员工）
### Keep Adjusting Based on Real Use（根据实际使用继续调整）
## 4. Run Through a Complete Real Process（跑通一遍完整流程）
（流程箭头 + 四个检查问题：数据关系、权限、自动化、业务 Agent 是否真的有用）
## Conclusion
（vibe coding 降低了从 0 到 1 的门槛；Agent 负责理解需求、写代码和迭代，NocoBase 提供权限、工作流等底座和统一的架构，人来审核和决策。NocoBase 3 目前没有审计日志，结论里不要提）
Ready to get started? <链接>
Related reading
```

**写法要点**
- 示例公司要具体到能想象：「a small B2B office furniture company… supplies design firms, architecture studios, hotels, coworking spaces」
- 每一步都写「检查什么」和「不对时怎么办」：
  > If the relationships between customers, opportunities, products, and quotations do not match the real business, describe the specific issue directly to AI and have it adjust the existing CRM.
- 权限、规则写成可以直接交给 AI 的句子：
  > Sales representatives can only view and manage the customers, opportunities, and follow-up items assigned to them; sales managers can view the entire team's data, reassign owners, and review sales progress…
- 设计类教程（数据模型、状态流转）用代码块画状态图，区分「状态」和「业务动作」
- 截图写成占位符，交付说明里列出每张图要截什么

---

## D. 概念解读

**标题**：`What Is <Concept>? A Practical Guide to <Category> in the <AI Era>` / `How to Start Using AI Without Replacing Existing Business Systems`
中文：`什么是 X？……的实用指南` / `企业如何在现有系统中引入 AI？`

**骨架**

```
## Introduction（引言）
（反常识问题 → 直接回答 → 证据，如 Google Trends 截图 → 「The problem is that many products can now be called X.」→ 「This article will answer two questions: 1. … 2. …」）
💬 栏目说明
💡 Read more: <相关旧文>
## What Is <Concept>?（什么是 X？）
（「At the most basic level, X refers to…」→ 「But this definition only explains part of the picture.」→ 3–4 条子类别 → 换个问法：「stop asking whether…, ask what problem it helps you solve」）
## Need 1: <读者的第一类需求>（需求一：……）
（场景 → 为什么普通做法不够 → 这类工具的价值 → 「Typical products include:」）
### <产品>  一行定位语（单独一行），然后 1–2 句说明 + 截图
## Need 2 / Need 3 / Need 4 …
## Product Decision Table（产品选型对照表）
| Product | Type | Open Source | Typical Use Cases | Target Users | Core Capabilities |
## FAQ（5 题：概念区别、怎么选、开源的好处、NocoBase 属于哪一类）
## Conclusion（回到开头的问题，给出更清楚的答案，2–4 个短段）
分享句 + Related reading
```

**写法要点**
- 定义句要能单独被引用：主语 + 是什么 + 用来做什么，一段 40–60 词
- 用「需求」组织文章，不用「产品类别」组织。读者带着问题来，按问题找答案
- 把 NocoBase 放在最贴近它定位的那个需求下，和同类产品并列介绍。NocoBase 3 属于「用 AI / Agent 开发能长期运行的业务系统」；NocoBase 2 属于「AI + 无代码搭建」。同一篇里两个都要出现时，分开放，各自写清版本
