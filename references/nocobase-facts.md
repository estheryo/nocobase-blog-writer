# 写到 NocoBase 时用的说法和链接

> **团队维护**：这个文件是文章里关于 NocoBase 的唯一标准说法。产品定位、链接或价格变了，只改这里，所有新文章会跟着变。最后更新：2026-10-30（链接已逐个打开检查）。

## ⚠️ 待团队确认：用哪一套定位

目前有两套说法，写作时按用户指定的使用；用户没指定时，**先用 A（博客现行说法）**，并在交付说明里提醒这个分歧。

**A. 博客现行说法（2026 年文章，对应 NocoBase 2 的 AI + 无代码能力）**
> NocoBase is an open-source AI-powered no-code platform for building enterprise business systems such as CRM, ticketing, approvals, project management, and internal tools.

中文：NocoBase 是一个开源的 AI 无代码平台，用来搭建 CRM、工单、审批、项目管理等企业业务系统和内部工具。

**B. 官网现行说法（NocoBase 3，www.nocobase.com 首页）**
> NocoBase is the open-source platform for building, running, and evolving business systems with AI. Agents write the business code, NocoBase provides the foundation and governance, and people make the decisions.

2026-10 的 SEO/GEO 审计发现，站外几乎所有资料都还写着 no-code/low-code，官网却已经全面改用 B，两边没有衔接。如果团队决定在博客里切换到 B，建议加一句过渡说明，例如「NocoBase 2 remains available as an AI + no-code platform」，并保留 no-code/low-code 作为次要关键词。

## 💬 栏目说明（每篇固定一次，放在开头之后）

英文（全部 147 篇都用这一句）：
```
💬 Hey, you're reading the NocoBase blog. NocoBase is the most extensible AI-powered no-code/low-code development platform for building enterprise applications, internal tools, and all kinds of systems. It's fully self-hosted, plugin-based, and developer-friendly. → [Explore NocoBase on GitHub](https://github.com/nocobase/nocobase)
```

中文：
```
💬 嗨！你正在阅读 NocoBase 博客。NocoBase 是一个极易扩展的 AI 无代码/低代码开发平台，用于构建企业应用、内部工具和各类系统。它完全支持自托管，基于插件架构设计，开发者友好。→ [欢迎在 GitHub 上了解我们](https://github.com/nocobase/nocobase)
```

（如果团队把定位切换到 B，这两句要同步改。）

## 产品信息块

```
- Website: https://www.nocobase.com/
- Documentation: https://docs.nocobase.com/
- Online Demo: https://demo.nocobase.com/new
- GitHub: https://github.com/nocobase/nocobase
- GitHub Stars: <写作当天用 API 查询，如 24.8k>
```

中文版：官网用 `https://www.nocobase.com/zh-CN/`。

## 常用链接（2026-10-30 检查过，均可访问）

| 用途 | 地址 |
|---|---|
| 官网首页 | https://www.nocobase.com/ |
| 定价（NocoBase 3） | https://www.nocobase.com/pricing/ |
| 定价（NocoBase 2 商业版） | https://nocode.nocobase.com/en/commercial |
| NocoBase 3 文档 | https://docs.nocobase.com/ |
| NocoBase 2 文档（AI Builder、AI 员工等现有博客引用的功能） | https://nocode.docs.nocobase.com/ |
| AI Builder | https://nocode.docs.nocobase.com/ai-builder |
| MCP | https://nocode.docs.nocobase.com/ai/mcp/ |
| CLI | https://nocode.docs.nocobase.com/api/cli/ |
| 在线 Demo | https://demo.nocobase.com/new |
| NocoCRM（NocoBase 3 方案） | https://www.nocobase.com/solution-crm/ |
| NocoITAM | https://www.nocobase.com/solution-itam/ |
| 客户案例 | https://www.nocobase.com/customers/ |
| CRM 方案（NocoBase 2） | https://nocode.nocobase.com/en/solutions/all-in-one/crm |

⚠️ **已失效**：`https://nocode.nocobase.com/en/ai-blueprints`（返回 404，但 2026-07 的 Smartsheet 替代品文章里的 🎉 公告还在用）。不要再引用。

## 写 NocoBase 时常用的能力点

每次挑 2–4 个和文章主题相关的，每个配一个具体例子，不要全部罗列。

| 能力 | 具体写法示例 |
|---|---|
| 数据模型与关联 | `one customer can have multiple projects, while each project can be linked to contracts, tasks, invoices, and payment records` |
| 外部数据源 | 可以连接 MySQL、PostgreSQL 等已有数据库和 API，在现有数据上搭系统（写之前先查文档，确认支持哪些） |
| 页面搭建 | 表格、看板、表单、详情页、图表、操作按钮，通过可视化界面配置 |
| 角色权限 | 按角色设置数据范围和操作权限：`Sales representatives can only view the customers assigned to them; sales managers can view the entire team's data` |
| 工作流与审批 | `when an opportunity reaches the Closed stage, the system can automatically update the customer status and create follow-up tasks` |
| AI 参与搭建 | Claude Code、Codex、Cursor 等 AI Agent 通过 CLI、Skills、MCP 连接 NocoBase，用自然语言描述需求，由 AI 完成数据建模、页面、工作流、权限配置；生成的系统还能在无代码界面里继续调整 |
| AI 员工 | 能读取当前页面、数据区块和选中记录作为上下文，调用技能查询数据、整理信息、填写表单、分析趋势；也可以编排进工作流 |
| 无代码继续维护 | AI 生成后，字段、页面、菜单、按钮、权限、工作流都能在界面里改，不必每次回到代码 |
| 插件与扩展 | 插件化架构，可以开发插件扩展功能 |
| 自托管 | 可以私有化部署，数据和部署环境由团队自己掌控 |
| 定价方式 | 一次性授权，不按用户数收费（写具体价格前先查定价页，区分 NocoBase 2 和 3） |

## 文章里关于 NocoBase 的核心观点

2026 年的文章反复出现一个观点，可以在不同文章里换角度复述：

> AI can build the first version of a business system quickly. What makes it production-ready is the foundation underneath: data models, permissions, workflows, auditing, and long-term maintenance. NocoBase gives AI that foundation, so AI focuses on the business, and people review and make decisions.

中文：AI 能很快做出业务系统的第一版，但能不能投入生产，取决于底层的数据模型、权限、工作流、审计和长期维护。NocoBase 给 AI 提供这套底座，让 AI 专注业务本身，人来审核和决策。

## 不要这样写

- 「NocoBase is the best …」「#1 …」「the only …」：没有出处的最高级
- 列出 NocoBase 没有的功能，或把路线图写成已上线。不确定时查文档，或标 `【待核实】`
- 引用 GitHub Stars、价格、客户数时不查最新数据
- 引用已下线的页面（见上面的失效链接）
