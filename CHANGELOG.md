# 更新记录

## 2026-11-02 · v1.2

团队决定：默认用官网的 NocoBase 3 说法，同时区分 NocoBase 2 和 NocoBase 3。

- `nocobase-facts.md` 按官网和官方文档重写：NocoBase 3 的标准说法（Core / Studio / Solution）；两个版本的本质区别（配置 vs 代码）和各自的能力、链接、价格；什么时候写 NocoBase 2；两个版本之间的过渡句；官方术语表（agent、业务 Agent、编码工具，不用「智能体」）
- 💬 栏目说明换成 NocoBase 3 的新版本（旧文章里的「most extensible AI-powered no-code/low-code」不再使用）
- 只写已经确认的版本信息：NocoBase 3 目前在 GitHub 上标记为 beta，不写成正式版；没有审计日志；NocoBase 2 不能原地升级，不承诺迁移工具
- 搭建教程先定版本：新教程默认基于 NocoBase 3（Agent 在应用代码仓库里写代码），NocoBase 2 教程要写明版本
- SEO 关键词和版本的对应：no-code / low-code 类词对应 NocoBase 2，AI coding / Agent 类词对应 NocoBase 3
- 自检脚本新增版本和术语检查：旧版栏目说明、AI 员工没标 NocoBase 2、把 NocoBase 3 写成无代码或正式版、提到 NocoBase 3 的审计日志、「智能体 / 代理」

## 2026-11-02 · v1.1

根据第一轮测试（3 个题目，用 Skill / 不用 Skill 各写一篇）修正：

- **不再照抄例句**：测试稿把参考文件里的例句原样搬进了新文章。现在明确要求只学结构，自检脚本也会报出与例句连续 8 个词（中文 16 个字）相同的地方
- **动笔前查重**：新增 `references/existing-posts.md`（全部 229 篇已发布文章）。测试时两个题目都撞上了旧文（2024 年的 Retool 替代品文、中文 NocoBase vs Appsmith）
- **段落规则不再矛盾**：「可引用段落 130–170 词」改为「一组 2–4 个短段落、合计 130–170 词」，单段仍不超过 70 词
- **打不开 Reddit 时的备选来源**：Hacker News、官方社区论坛、GitHub Discussions、X；都找不到就改用读者熟悉的场景加有出处的数据
- 篇幅按正文计算，不含表格、产品信息块、FAQ 和相关阅读

## 2026-10-30 · v1.0

- 首版：分析官网博客 147 篇 AI & No-Code 文章，以 2026 年的写法为范本
- 第一轮测试：用 Skill 写的检查项全部通过（37/37），不用 Skill 的通过 43%
