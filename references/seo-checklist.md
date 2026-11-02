# SEO / GEO 检查清单

依据：栏目 147 篇文章的统计，以及 2026-10 对 www.nocobase.com 的 SEO/GEO 审计结论。凡是「栏目现状」与「目标」不一致的地方，以目标为准。

## 标题（title）

- 50–60 字符（栏目现状：中位数 59，但 112/245 页超过 70 字符被截断）
- 主关键词尽量放在前半段
- 标题超过 60 字符时，去掉品牌后缀（网站模板会自动加 ` — NocoBase`）
- 用数字、vs、How to、What Is 等具体格式，不用「Ultimate Guide」「Everything You Need to Know」
- 只有内容确实跟年份相关时才加年份（`2026 Edition`），并在年份变化时更新
- 中文标题 20–30 个汉字

## URL slug

- 小写英文、连字符分隔、只包含关键词：`best-smartsheet-alternatives`、`open-source-ai-crm`
- 不带日期、不带 `the/a/of`；中英文两版共用同一个 slug

## Meta description

- **120–155 字符**（栏目现状：中位数 168，148/245 页超过 160 被截断，务必控制）
- 动词开头：Compare / Learn / Explore / See how
- 写清楚覆盖什么、给谁看，包含主关键词
- 例：`Compare 7 Smartsheet alternatives by positioning, key differences, ideal teams, and estimated three-year costs.`（112 字符）
- 中文 60–80 个汉字

## 标题层级

- 全文只有 1 个 H1（文章标题），正文从 H2 开始（栏目里有 1 篇出现了 2 个 H1）
- H2 5–9 个；至少 2 个 H2 包含主关键词或它的变体
- 产品型 H2 统一写成「序号. 产品名: For …」；FAQ 的问题用 H3（或沿用栏目的 `## 1. 问题`）
- 不跳级（H2 → H4）

## 关键词

- 主关键词出现在：title、H1、前 100 词、至少 2 个 H2、description、至少 1 张图的 alt
- 次关键词自然分布在小标题和正文里；不堆砌，同一个词每段最多出现一次
- 在正文里也用读者的说法（`Smartsheet alternative`、`self-hosted CRM`、`open source AI CRM`），不只用我们的品类名

## GEO：让 AI 搜索引擎能引用

AI 引擎（ChatGPT、Perplexity、Google AI Overviews）喜欢引用能独立成立、信息密度高的段落。2026-10 审计时，全站段落的可引用性平均只有 37.6/100。

- **开头先给答案**：TL;DR 或第一段用 40–60 词直接回答标题里的问题
  > If you are looking for an open source AI CRM, NocoBase offers the deepest AI integration. Its AI employees can understand business context and actively participate in daily operations…
- **定义句**：每个产品或概念的第一句写成「X is a … for …」，不用代词开头
- **每个主要小节至少有一组 130–170 词的完整回答**：由 2–4 个短段落组成（单段仍然不超过 70 词），合在一起能独立回答一个具体问题，包含具体对象和数字。被 AI 引用时通常整组被摘出，所以这一组里不要依赖前文才能看懂
- **数字带出处和日期**：`GitHub Stars: 22.7k`，并在交付说明里记录查询日期；价格写明方案名和计费方式
- **对比表**：放在第一个产品 H2 之前（2026 年 63% 的文章有对比表）
- **FAQ**：5–7 题，问题照搜索习惯写（`Which … should I choose if …?`、`Is X free?`、`X vs Y?`），每个答案 40–120 词并且能独立成立。交付说明里提醒加 FAQPage 结构化数据
- 少用「it」「this」开头的段落。被单独引用时，读者不知道它指什么

## 链接

- **站内链接 8–15 个**（栏目中位数 13）：
  - 开头或段落中的 💡 Read more 1–2 个
  - 正文里写到 CRM、工单、资产管理等时，链接到对应的旧文或方案页
  - 文末 Related reading 6–12 篇，从 `internal-links.md` 中挑同一主题的
- **站外链接**：每个产品的官网、文档、价格页、GitHub；开头引用的讨论帖；统计数据的来源
- 锚文本写清楚内容（`How to Choose a Smartsheet Alternative`），不写「click here」
- 链接到 NocoBase 产品页时，使用 `nocobase-facts.md` 里的当前地址

## 图片

- 每个产品至少 1 张截图，教程每个检查点 1 张
- 文件名使用英文描述词：`nocobase-crm-pipeline-board.png`，不用 `Group 39.png`、`image1.png`
- 每张图都写 alt 文本，说明图里是什么，比如 `NocoBase CRM opportunity pipeline board grouped by stage`
- 社区讨论截图的 alt：`Reddit discussion in r/smartsheet about Smartsheet alternatives`

## 作者与日期

- 作者名写法和官网一致：`Deng Lijia`、`Yuan Tianqi`、`Zhang Lu`（审计发现 `Deng lijia` 和 `Deng Lijia` 两种写法并存，统一用首字母大写）
- 内容依赖的数据（Stars、价格、功能）写明时间，方便后续更新

## 篇幅

按正文计算，不含对比表、产品信息块、FAQ 和 Related reading（这些加起来常常有 800–1,500 词）：

- 盘点和对比文：2,200–3,800 词
- 教程：2,000–3,000 词
- 概念解读：2,200–3,000 词
- 不靠凑字数达标：每一节都要有新的信息
