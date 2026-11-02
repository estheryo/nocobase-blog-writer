# nocobase-blog-writer

让 AI 按 NocoBase 官网博客「AI & No-Code」栏目的真实写法写 SEO 文章：结构、语气、SEO/GEO 要求都和已发布的 2026 年文章一致，并且不编造数据。

这个 Skill 是从官网博客 147 篇 AI & No-Code 文章（中英文各一份）逐篇分析归纳出来的。

## 安装

Claude Code 会自动加载 `~/.claude/skills/` 下的 Skill：

```bash
git clone https://github.com/estheryo/nocobase-blog-writer.git ~/.claude/skills/nocobase-blog-writer
```

更新到最新版：

```bash
git -C ~/.claude/skills/nocobase-blog-writer pull
```

## 怎么用

在 Claude Code 里直接说需求，不需要提 Skill 的名字：

- 「写一篇英文博客：开源 Retool 替代品，主关键词 open source retool alternative」
- 「帮我写一篇中文对比文：NocoBase vs Appsmith，给技术负责人看」
- 「用 AI + NocoBase 搭建一个工单系统，写成教程」
- 「这篇读起来太像 AI 了，按我们博客的风格改一下」（附上文章）
- 「先给我一个大纲」

产出是一个 Markdown 文件，包含 front-matter（title、slug、description、关键词）、正文，以及一段不发布的「交付说明」：需要补的截图和 alt 文本、需要人工核实的地方、数据的查询日期。

单独检查一篇文章：

```bash
python3 ~/.claude/skills/nocobase-blog-writer/scripts/check_article.py 文章.md
```

## 反馈

边用边反馈，有两种方式：

1. 在这个仓库开一个 Issue：贴上 AI 写的段落，说明哪里不对、希望怎么写
2. 直接在 Claude Code 里告诉维护这个 Skill 的会话

最有用的反馈是具体的：「这一段太像广告」「我们不会这样介绍竞品」「这个功能说错了」，最好附上你改好的版本。

## 文件结构

| 文件 | 作用 |
|---|---|
| `SKILL.md` | 主流程：明确任务 → 查重和调研 → 大纲 → 写作 → 自检 → 交付 |
| `references/article-types.md` | 四种文章骨架：开源工具盘点、替代品与对比、搭建教程、概念解读 |
| `references/voice.md` | 语气、句式、禁用词、改写对照、中英文两版的差异 |
| `references/seo-checklist.md` | 标题、slug、description、关键词、GEO、链接、图片 |
| `references/nocobase-facts.md` | **NocoBase 的标准说法、💬 栏目说明、常用链接**（产品信息变了只改这里） |
| `references/existing-posts.md` | 全部已发布文章，动笔前查重用 |
| `references/internal-links.md` | 按主题分组的内链库 |
| `scripts/check_article.py` | 自检脚本：AI 腔用语、照抄例句、段落长度、SEO 字段、关键词覆盖、链接、图片 |
| `evals/` | 回归测试题目（Skill 改动后用来对比效果） |

## 维护说明

- **版本**：文章里的「NocoBase」默认指 NocoBase 3，使用官网说法；写无代码、可视化搭建、AI 员工这类主题时明确写「NocoBase 2」。两个版本的说法、术语、链接、价格都在 `references/nocobase-facts.md`，产品信息有变化时只改这一个文件
- 文章清单和内链库来自 [nocobase/website-v3](https://github.com/nocobase/website-v3) 的 `homepage/content/blog/posts.json`，新文章多了以后需要重新生成
- 改动记录见 `CHANGELOG.md`
