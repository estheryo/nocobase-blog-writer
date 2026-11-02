# 写到 NocoBase 时用的说法和链接

> **团队维护**：这个文件是文章里关于 NocoBase 的唯一标准说法。产品定位、链接或价格变了，只改这里，所有新文章都会跟着变。
> 最后更新：2026-11-02。来源：www.nocobase.com、docs.nocobase.com 的《What is NocoBase 3》《Coming from NocoBase 2》《Glossary / 术语表》；链接已逐个打开检查。

目录
1. 默认用 NocoBase 3 的说法
2. 两个版本怎么区分（最重要）
3. 术语表
4. 💬 栏目说明
5. 产品信息块和常用链接
6. 能力点：NocoBase 3 / NocoBase 2 分开写
7. 核心观点
8. 不要这样写

---

## 1. 默认用 NocoBase 3 的说法

团队决定（2026-11-02）：**文章里的「NocoBase」默认指 NocoBase 3**，用官网的标准说法。

英文标准句：
> NocoBase is the open-source platform for building, running, and evolving business systems with AI. Agents write the code and do the work, NocoBase provides the foundation and governance, and people make the decisions.

中文标准句：
> NocoBase 是用 AI 持续开发和运行业务系统的开源平台。Agent 写代码、做执行，NocoBase 提供底座和治理能力，人来做决策。

一句话版本（官网版本菜单）：`NocoBase 3: The development platform for agents` / 「NocoBase 3：面向 Agent 的开发平台」

NocoBase 3 由三部分组成：

| 产品 | 英文定义 | 中文定义 |
|---|---|---|
| NocoBase Core | The open-source application foundation for business systems built and run with AI. Permissions, workflows, files, and 20+ other building blocks come ready to use, so agents build only what is specific to your business, all on one consistent architecture. | 开发和运行业务系统的开源底座。权限、工作流、文件等 20 多种构件开箱即用，Agent 只写企业自己的业务部分，并且都在同一套架构上。 |
| NocoBase Studio | The governance platform for people and agents building software together. It brings Claude Code, Codex, and OpenCode into one agent team. Available in the commercial editions. | 人与 Agent 协同开发的治理平台，把 Claude Code、Codex、OpenCode 组织成一支 Agent 团队。在商业版中提供。 |
| NocoBase Solution(s) | A line of open-source, agent-driven business apps built on Core, such as NocoCRM and NocoITAM. | 基于 Core 的开源业务应用，例如 NocoCRM、NocoITAM，内置业务 Agent。 |

## 2. 两个版本怎么区分（最重要）

### 本质区别（官方说法）

> In NocoBase 2, tables, pages, permissions, and workflows exist as **configuration** stored in the database, and the platform reads that configuration to render the interface. In NocoBase 3, they are all **code**, in your own repository, written by agents.

中文：NocoBase 2 里，表、页面、权限、工作流是存在数据库里的**配置**；NocoBase 3 里，它们都是由 Agent 写在你自己代码仓库里的**代码**。

| | NocoBase 3（默认） | NocoBase 2 |
|---|---|---|
| 官方一句话 | The development platform for agents / 面向 Agent 的开发平台 | AI + no-code development platform / AI + 无代码开发平台 |
| 怎么搭系统 | Agent（Claude Code、Codex 等）在应用代码仓库里写代码；数据结构用 migration，页面用 UI 组件库，流程用记录生命周期 | 在界面里拖拽配置页面和区块；在工作流画布上配置流程；在数据源管理里建表 |
| 插件 | 注册进应用的插件清单（通常由 Agent 完成） | 在插件管理器里启用 |
| 业务里的 AI | **业务 Agent**（business agent），由 Agents 插件接入，和人用同一套角色和权限 | **AI 员工**（AI employees） |
| 团队协作 | NocoBase Studio：Agent 团队推进 issue，人在关键处验收 | — |
| 现成应用 | NocoCRM、NocoITAM、NocoReach 等 Solution 应用 | 2025 年的 CRM Solution 等方案（不要和 NocoCRM 混为一谈） |
| 官网 / 文档 | www.nocobase.com / docs.nocobase.com | nocode.nocobase.com / nocode.docs.nocobase.com |
| 定价 | www.nocobase.com/pricing/ | nocode.nocobase.com/en/commercial |

### 什么时候写 NocoBase 2

- 文章讲的是**无代码 / 低代码 / 可视化搭建**：拖拽页面、工作流画布、插件管理器、在界面里改字段
- 文章用到 **AI 员工**、AI Builder，或者是基于 NocoBase 2 界面截图的教程
- 主关键词是 no-code、low-code、Airtable/Smartsheet 替代品这一类，读者要的就是无代码工具

这时：
- 第一次出现写全称「NocoBase 2」，介绍用 NocoBase 2 的说法：`NocoBase 2 is an open-source AI + no-code development platform for building business systems.` /「NocoBase 2 是开源的 AI + 无代码开发平台，用来搭建业务系统。」
- 链接用 nocode.nocobase.com 和 nocode.docs.nocobase.com，价格看 NocoBase 2 的商业版页面
- 在合适的位置加一句过渡，让读者知道还有 NocoBase 3：
  > NocoBase 2 is still available at nocode.nocobase.com. For teams that build with coding agents, NocoBase 3 is the development platform for agents: agents write the business code on NocoBase Core, and people review and decide.

  中文：「NocoBase 2 仍在 nocode.nocobase.com 提供。如果团队用编码工具和 Agent 来开发，可以看看 NocoBase 3：Agent 在 NocoBase Core 上写业务代码，人来审核和决策。」

### 盘点和对比文里怎么选版本

- 先看这篇文章比的是什么：比无代码工具，就介绍 NocoBase 2；比 AI 开发、Agent、业务系统底座、内部工具开发框架，就介绍 NocoBase 3
- 同一节里只写一个版本，所有能力、价格、链接都对应这个版本
- 确实需要两个都提时，分成两段写清楚，不要写成同一个产品同时具备两边的特性

### 版本状态和迁移，只写已经确认的

- **发布状态**：截至 2026-10-31，GitHub 上 NocoBase 3 的发布标记为 beta（`nocobase-v3-beta/…`），NocoBase 2 仍在持续发布稳定版（v2.2.37）。写作时到 https://github.com/nocobase/nocobase/releases 查当天状态；不要把 NocoBase 3 写成「正式版」或「GA」
- **迁移**：NocoBase 2 的应用不能原地升级到 3，需要在 3 上重建应用再导入业务数据；官方迁移工具和 NocoBase 2 的维护计划还没有公布。不要承诺迁移工具或 NocoBase 2 的维护期限
- **审计日志**：NocoBase 3 目前还没有（官方文档写明 not available yet）。审计日志是 NocoBase 2 的功能

## 3. 术语表

全站（文档、官网、产品界面）统一用词，来自官方术语表：

| English | 中文 | 说明 |
|---|---|---|
| agent（正文里小写） | Agent | AI 执行者的统称：一个编码工具加一个模型。中文不用「智能体」「代理」「Coding Agent」 |
| coding tool | 编码工具 | Claude Code、Codex、OpenCode、Cursor 等 |
| business agent | 业务 Agent | 在应用里按权限处理业务的 Agent。**NocoBase 2 里叫 AI employee / AI 员工** |
| development agent | 开发 Agent | 写应用代码的 Agent，只在要和业务 Agent 对比时用 |
| app | 应用 | 用 NocoBase 模板创建的一份代码仓库，部署后是一个业务系统，归你所有 |
| building blocks | 构件 / 基础能力 | Core 提供的权限、工作流、文件等 |
| record lifecycle | 记录生命周期 | NocoBase 3 的流程都基于它：状态存在记录字段里，状态之间的流转写在代码里 |
| permission set / role | 权限集 / 角色 | 界面上显示为「角色」 |
| data scope | 数据范围 | 一个操作能作用于哪些记录，比如「我负责的订单」 |
| System settings | 系统设置 | 应用里的管理入口 |
| issue | issue | Studio 里交付工作的基本单位，不叫 ticket 或工单 |
| agent team | Agent 团队 | 团队启用的全部 Agent |
| NocoBase Solution / Solution app | NocoBase Solutions / Solution 应用 | NocoCRM、NocoITAM 等 |

## 4. 💬 栏目说明（每篇固定一次，放在开头之后）

新文章用 NocoBase 3 的版本：

英文：
```
💬 Hey, you're reading the NocoBase blog. NocoBase is the open-source platform for building, running, and evolving business systems with AI: agents write the code, NocoBase provides the foundation and governance, and people make the decisions. → [Explore NocoBase on GitHub](https://github.com/nocobase/nocobase)
```

中文：
```
💬 嗨！你正在阅读 NocoBase 博客。NocoBase 是用 AI 持续开发和运行业务系统的开源平台：Agent 写代码、做执行，NocoBase 提供底座和治理能力，人来做决策。→ [欢迎在 GitHub 上了解我们](https://github.com/nocobase/nocobase)
```

旧文章里的「the most extensible AI-powered no-code/low-code development platform」是 NocoBase 2 时期的说法，新文章不再使用。

## 5. 产品信息块和常用链接

NocoBase 3（默认）：
```
- Website: https://www.nocobase.com/
- Documentation: https://docs.nocobase.com/
- Pricing: https://www.nocobase.com/pricing/
- GitHub: https://github.com/nocobase/nocobase
- GitHub Stars: <写作当天用 API 查询，如 24.8k>
```

NocoBase 2（只在写 NocoBase 2 时用）：
```
- Website: https://nocode.nocobase.com/
- Documentation: https://nocode.docs.nocobase.com/
- Pricing: https://nocode.nocobase.com/en/commercial
- Online Demo: https://demo.nocobase.com/new
- GitHub: https://github.com/nocobase/nocobase
```

两个版本在同一个 GitHub 仓库，Stars 是同一个数字。中文版文章：官网用 `https://www.nocobase.com/zh-CN/`，文档用 `https://docs.nocobase.com/zh-CN/`。

| 用途 | 地址 |
|---|---|
| NocoBase 3 是什么 | https://docs.nocobase.com/start/what-is-nocobase |
| 从 NocoBase 2 过来 | https://docs.nocobase.com/start/from-v2 |
| Core | https://www.nocobase.com/core/ · 文档 https://docs.nocobase.com/core/ |
| Studio | https://www.nocobase.com/studio/ |
| Solution 总览 | https://www.nocobase.com/solutions/ |
| NocoCRM / NocoITAM / NocoReach | https://www.nocobase.com/solution-crm/ · /solution-itam/ · /solution-reach/ |
| 定价（NocoBase 3） | https://www.nocobase.com/pricing/ |
| 合作伙伴 | https://www.nocobase.com/partner/ · /find-partner/ |
| 客户案例 | https://www.nocobase.com/customers/ |
| NocoBase 2 官网 / 文档 | https://nocode.nocobase.com/ · https://nocode.docs.nocobase.com/ |
| NocoBase 2 AI Builder / MCP / CLI | https://nocode.docs.nocobase.com/ai-builder · /ai/mcp/ · /api/cli/ |

⚠️ **已失效**：`https://nocode.nocobase.com/en/ai-blueprints`（404），不要再引用。

**定价（NocoBase 3，写作前到定价页核对）**：Community 免费开源，包含 Core 和全部 Solution 应用，可以用于生产和客户交付；Professional $8,000 一次性买断，包含 Studio、1 年升级和支持、一次部署；Enterprise 按需报价。NocoBase 2 有自己的商业版价格，不要和 3 混用。

## 6. 能力点：NocoBase 3 / NocoBase 2 分开写

每篇挑 2–4 个和主题相关的写，每个配一个具体例子，不要全部罗列。

**NocoBase 3**

| 能力 | 具体写法示例 |
|---|---|
| 现成构件，Agent 只写业务部分 | `Say the purchasing team needs a supplier management system: agents write only the business parts, such as supplier profiles, purchase orders, and approval rules, and use Core's permissions and approvals as they are.` |
| 一套项目结构和开发规范 | 换开发者、换模型、换会话，Agent 都按同样的结构和随包发布的技能写代码，系统多年后架构仍然一致 |
| 变更就是代码 | 可以在分支上开发、评审、测试、按版本发布，出问题可以回滚；平台缺的能力 Agent 可以直接写 |
| 权限 | 认证、用户、授权插件，加上默认数据范围、共享规则、限制规则；默认模板自带用户管理、角色与权限页面 |
| 数据库 | 支持 SQLite、PostgreSQL、MySQL、SQL Server、Oracle；外部数据库作为第二个连接接入（达梦、人大金仓、OceanBase 在商业版） |
| 流程与审批 | 流程基于记录生命周期写在代码里，管理员在「流程管理」里看流程图、调参数（审批人、金额阈值）、查执行记录；审批插件是商业版功能 |
| 业务 Agent | 应用上线后，业务 Agent 在应用里调研客户、起草邮件、核对资产记录、处理工单，和人用同一套权限；需要决策时把证据交给负责人 |
| Studio | 一支 Agent 团队同时推进多个项目和 issue；需要人介入时附上报告、检查清单和截图；技能、知识库和项目记忆沉淀团队经验 |
| 自托管、不锁定 | Core、Solution、Studio 都运行在你自己的服务器上，代码和数据归你；模型和编码工具自己选；应用发布后独立运行 |

**NocoBase 2**（只在写 NocoBase 2 时用）

| 能力 | 具体写法示例 |
|---|---|
| 数据模型与关联 | `one customer can have multiple projects, while each project can be linked to contracts, tasks, invoices, and payment records` |
| 可视化搭建 | 表格、看板、表单、详情页、图表、操作按钮在界面里配置 |
| 角色权限 | `Sales representatives can only view the customers assigned to them; sales managers can view the entire team's data` |
| 工作流画布与审批 | 在工作流画布上配置触发条件和节点 |
| AI 参与搭建 | 编码工具通过 CLI、Skills、MCP 连接 NocoBase 2，用自然语言完成建模、页面、工作流配置，之后还能在无代码界面里继续改 |
| AI 员工 | 能读取当前页面和选中记录作为上下文，查询数据、整理信息、填写表单，也可以编排进工作流 |
| 审计日志、插件管理器 | NocoBase 2 有，NocoBase 3 的说法不同或暂未提供，不要混写 |

## 7. 核心观点

NocoBase 3 文章反复出现的观点，可以换角度复述，不要每篇照抄同一句：

> AI writes code fast. Building reliable business systems is still hard. Vibe coding gets the first version together quickly, but a business system is used for years: features keep getting added, processes keep changing, and people hand the work over. NocoBase adds the foundation and the governance on top of vibe coding, and your team keeps writing code with Claude Code, Codex, and other coding tools.

中文：AI 写代码很快，但做出可靠的业务系统仍然很难。vibe coding 能很快做出第一版，可业务系统要用很多年：功能不断增加，流程不断变化，人也会交接。NocoBase 在 vibe coding 之上补上底座和治理，团队继续用 Claude Code、Codex 等编码工具写代码。

## 8. 不要这样写

- 把 NocoBase 3 写成「无代码平台」「拖拽搭建」，或者说 NocoBase 3 有 AI 员工、审计日志、插件管理器
- 把 Studio、NocoCRM、NocoITAM 写成 NocoBase 2 的功能
- 说 NocoBase 2 可以一键升级到 3，或者承诺迁移工具、维护期限
- 把 NocoBase 3 写成正式版 / GA（以 GitHub releases 当天的状态为准）
- 中文用「智能体」「代理」「Coding Agent」，英文正文里把 agent 写成大写的 Agent
- 「NocoBase is the best …」「#1 …」「the only …」这类没有出处的最高级
- 不查最新数据就引用 GitHub Stars、价格、客户数；引用已下线的页面
