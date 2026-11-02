#!/usr/bin/env python3
"""NocoBase 博客文章自检（英文或中文 Markdown）。

用法：python3 check_article.py <article.md>

检查长度、结构、SEO 字段、关键词覆盖、AI 腔词汇、段落长度、链接和图片。
阈值来自官网博客 AI & No-Code 栏目 2026 年的文章统计和 2026-10 的 SEO 审计。
只输出报告，不修改文件。
"""
import re
import statistics
import sys
from pathlib import Path

EN_FLUFF = [
    "seamless", "seamlessly", "robust", "powerful", "comprehensive", "cutting-edge", "game-changer",
    "game changer", "revolutionize", "revolutionise", "transformative", "unparalleled", "streamline",
    "streamlines", "streamlined", "leverage", "leverages", "leveraging", "harness", "utilize", "empower",
    "empowers", "unlock", "unlocks", "elevate", "supercharge", "delve", "dive into", "deep dive",
    "landscape", "realm", "tapestry", "in today's", "fast-paced", "ever-evolving", "rapidly evolving",
    "it's worth noting", "it is worth noting", "notably", "importantly", "moreover", "furthermore",
    "additionally", "in conclusion", "in summary", "look no further", "whether you're", "perfect for",
    "ideal solution", "crucial", "pivotal", "paramount", "plethora", "myriad", "boost",
]
ZH_FLUFF = [
    "赋能", "助力", "打造", "加持", "无缝", "一站式", "强大", "全面", "高效", "轻松", "降本增效",
    "数字化转型", "在当今", "值得一提的是", "总而言之", "综上所述", "痛点", "抓手", "颠覆", "极致", "您",
]
ALLOWED_EMOJI = set("💬💡🎉🚀🔎⭐❤✅❌👉📌⚠🙌💕") | {"️"}
EMOJI_RE = re.compile("[\U0001F300-\U0001FAFF☀-➿⭐]")
BAD_IMG_NAME = re.compile(r"(^|/)(image|img|group|screenshot|untitled|截图|屏幕)[\s%_\-]*\d*\.(png|jpe?g|gif|webp)$|(^|/)\d+\.(png|jpe?g|gif|webp)$", re.I)


def parse(path):
    text = open(path, encoding="utf-8").read()
    meta = {}
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if m:
        for line in m.group(1).splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                meta[k.strip()] = v.strip().strip('"').strip("'")
        text = text[m.end():]
    return meta, text


def main(path):
    meta, body = parse(path)
    lines = body.splitlines()
    no_code = re.sub(r"```.*?```", "", body, flags=re.S)
    # 去掉图片、链接地址和裸 URL，只留下读者看到的文字
    no_code = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", no_code)
    no_code = re.sub(r"\]\([^)]*\)", "]", no_code)
    no_code = re.sub(r"https?://\S+", "", no_code)
    cjk = len(re.findall(r"[一-鿿]", no_code))
    zh = cjk > len(re.findall(r"[A-Za-z]+", no_code)) * 0.5
    warns, oks, infos = [], [], []

    def check(ok, good, bad):
        (oks if ok else warns).append(good if ok else bad)

    headings = [(len(m.group(1)), m.group(2).strip(), i + 1) for i, l in enumerate(lines) for m in [re.match(r"^(#{1,6})\s+(.*)", l)] if m]
    h1 = [h for h in headings if h[0] == 1]
    h2 = [h for h in headings if h[0] == 2]
    title = meta.get("title") or (h1[0][1] if h1 else "")
    desc = meta.get("description", "")

    # 长度
    if zh:
        check(3200 <= cjk <= 6000, f"正文 {cjk} 个汉字", f"正文 {cjk} 个汉字（2026 年中文文章中位数约 4,000，建议 3,200–6,000）")
    else:
        words = len(re.findall(r"[A-Za-z0-9’'\-]+", no_code))
        check(1800 <= words <= 4200, f"正文约 {words} 词", f"正文约 {words} 词（建议 1,800–4,200；2026 年中位数 2,706）")

    # SEO 字段
    tl = len(title)
    if zh:
        check(18 <= tl <= 32, f"标题 {tl} 字", f"标题 {tl} 字（中文建议 20–30 字）：{title}")
    else:
        check(45 <= tl <= 62, f"标题 {tl} 字符", f"标题 {tl} 字符（建议 50–60，超过 60 会被截断）：{title}")
    if desc:
        dl = len(desc)
        if zh:
            check(50 <= dl <= 85, f"description {dl} 字", f"description {dl} 字（中文建议 60–80 字）")
        else:
            check(115 <= dl <= 158, f"description {dl} 字符", f"description {dl} 字符（建议 120–155）")
    else:
        warns.append("front-matter 缺少 description")
    slug = meta.get("slug", "")
    if slug:
        check(bool(re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", slug)) and not re.search(r"(^|-)(the|a|an|of|20\d\d)(-|$)", slug),
              f"slug 格式正确：{slug}", f"slug 需小写连字符、不含 the/a/of/年份：{slug}")
    else:
        warns.append("front-matter 缺少 slug")

    # 结构
    check(len(h1) == 1, "H1 恰好 1 个", f"H1 有 {len(h1)} 个（应为 1 个）")
    check(5 <= len(h2) <= 12, f"H2 {len(h2)} 个", f"H2 {len(h2)} 个（建议 5–9 个）")
    for a, b in zip(headings, headings[1:]):
        if b[0] > a[0] + 1:
            warns.append(f"第 {b[2]} 行标题跳级（H{a[0]} → H{b[0]}）：{b[1]}")
    check("💬" in body, "有 💬 栏目说明", "缺少 💬 栏目说明（见 references/nocobase-facts.md）")
    check(bool(re.search(r"^\|.*\|\s*$", body, re.M)), "有对比表", "没有表格（2026 年 63% 的文章有对比表，盘点和对比类建议必加）")
    check(any(re.search(r"FAQ|常见问题|Frequently Asked", h[1], re.I) for h in headings), "有 FAQ", "没有 FAQ 小节（建议 5–7 题，利于 AI 搜索引用）")
    check(bool(re.search(r"Related reading|相关阅读", body, re.I)), "有 Related reading / 相关阅读", "缺少文末 Related reading / 相关阅读")
    if any(re.search(r"TL;?DR", h[1], re.I) for h in headings):
        infos.append("有 TL;DR")

    # 段落
    paras = []
    for block in re.split(r"\n\s*\n", re.sub(r"```.*?```", "", body, flags=re.S)):
        for l in block.splitlines():
            s = l.strip()
            if not s or re.match(r"^(#|\||>|!\[|[-*+] |\d+\.\s|💬|💡|🎉|🚀|⭐|❤|Related reading|相关阅读)", s):
                continue
            paras.append(s)
    if paras:
        if zh:
            lens = [len(re.findall(r"[一-鿿]", p)) for p in paras]
            long_p = [(p[:40], n) for p, n in zip(paras, lens) if n > 150]
            check(not long_p, f"段落中位数 {statistics.median(lens):.0f} 字，没有超过 150 字的段落",
                  f"{len(long_p)} 个段落超过 150 字，建议拆分：" + "；".join(f"「{p}…」({n}字)" for p, n in long_p[:3]))
        else:
            lens = [len(p.split()) for p in paras]
            long_p = [(p[:50], n) for p, n in zip(paras, lens) if n > 70]
            check(not long_p, f"段落中位数 {statistics.median(lens):.0f} 词，没有超过 70 词的段落",
                  f"{len(long_p)} 个段落超过 70 词，建议拆分：" + "; ".join(f'"{p}…" ({n}w)' for p, n in long_p[:3]))
            sents = [s for p in paras for s in re.split(r"(?<=[.!?])\s+", p) if len(s.split()) > 2]
            if sents:
                avg = statistics.mean(len(s.split()) for s in sents)
                check(avg <= 21, f"句子平均 {avg:.1f} 词", f"句子平均 {avg:.1f} 词，偏长（栏目约 15–17 词）")
            pron = [p[:40] for p in paras if re.match(r"^(It|This|These|They|That)\b", p)]
            if len(pron) > max(3, len(paras) * 0.08):
                warns.append(f"{len(pron)} 个段落以 It/This/These/They 开头，被单独引用时指代不清；改成直接写名词：" + "; ".join(pron[:3]))

    # AI 腔
    hits = []
    for i, l in enumerate(lines, 1):
        low = l.lower()
        for w in (ZH_FLUFF if zh else EN_FLUFF):
            if (w in l) if zh else re.search(r"\b" + re.escape(w) + r"\b", low):
                hits.append(f"第 {i} 行「{w}」")
    check(not hits, "没有发现空洞词 / AI 腔用语", f"发现 {len(hits)} 处空洞词或 AI 腔用语（见 references/voice.md 第 5 节）：" + "，".join(hits[:12]) + ("……" if len(hits) > 12 else ""))
    if not zh:
        words = max(1, len(no_code.split()))
        dashes = no_code.count("—")
        check(dashes / words * 1000 <= 1.2, f"破折号 {dashes} 个", f"破折号 {dashes} 个（每千词 {dashes / words * 1000:.1f}，建议不超过 1）")
    ex = len(re.findall(r"[!！]", no_code))
    check(ex <= 2, f"感叹号 {ex} 个", f"感叹号 {ex} 个，太多（全栏目 147 篇一共只有 91 个）")
    bad_emoji = sorted({e for e in EMOJI_RE.findall(no_code) if e not in ALLOWED_EMOJI})
    check(not bad_emoji, "emoji 只用作功能标记", f"出现装饰性 emoji：{' '.join(bad_emoji)}（只保留 💬💡🎉🚀🔎⭐❤️ 等功能标记）")

    # NocoBase 版本和术语（规则见 references/nocobase-facts.md 第 2、3 节）
    vissues = []
    if re.search(r"most extensible AI-powered no-code|极易扩展的 AI 无代码", body):
        vissues.append("用的是旧版 💬 栏目说明（NocoBase 2 时期），换成 nocobase-facts.md 第 4 节的新版本")
    has_v2 = re.search(r"NocoBase\s*2", body)
    if re.search(r"AI Employees?|AI employees?|AI 员工", no_code) and not has_v2:
        vissues.append("出现「AI 员工 / AI Employees」但全文没有写明 NocoBase 2；NocoBase 3 里叫业务 Agent（business agent）")
    for s in re.split(r"(?<=[.!?。！？])\s*", no_code):
        if re.search(r"NocoBase\s*3", s):
            if re.search(r"(?i)no-code platform|nocode platform|drag-and-drop|drag and drop|无代码平台|拖拽", s) and not re.search(r"NocoBase\s*2", s):
                vissues.append(f"把 NocoBase 3 和无代码 / 拖拽写在一起：「{' '.join(s.split())[-60:]}…」")
            if re.search(r"(?i)\bGA\b|generally available|正式版|正式发布", s):
                vissues.append(f"NocoBase 3 的发布状态以 GitHub releases 为准，不要写成正式版 / GA：「{' '.join(s.split())[-60:]}…」")
            if re.search(r"(?i)audit log|审计日志", s):
                vissues.append(f"NocoBase 3 目前没有审计日志：「{' '.join(s.split())[-60:]}…」")
    if zh:
        bad_terms = re.findall(r"智能体|(?<!商)代理(?!商)|Coding Agent", no_code)
        if bad_terms:
            vissues.append(f"术语：{len(bad_terms)} 处「智能体 / 代理 / Coding Agent」，官方术语写「Agent」「编码工具」")
    check(not vissues, "NocoBase 版本和术语没有发现问题", "；".join(vissues[:8]))

    # 链接与图片
    links = re.findall(r"(?<!!)\[[^\]]*\]\(([^)\s]+)\)", body) + re.findall(r"(?<![(\[])(https?://[^\s)]+)", body)
    internal = {u for u in links if "nocobase.com" in u}
    external = {u for u in links if u.startswith("http") and "nocobase.com" not in u}
    check(len(internal) >= 8, f"站内链接 {len(internal)} 个", f"站内链接只有 {len(internal)} 个（建议 8–15，见 references/internal-links.md）")
    check(len(external) >= 3, f"站外链接 {len(external)} 个", f"站外链接只有 {len(external)} 个（产品官网、GitHub、讨论帖、数据来源）")
    imgs = re.findall(r"!\[([^\]]*)\]\(([^)]*)\)", body)
    no_alt = [s for a, s in imgs if not a.strip() or re.search(r"\.(png|jpe?g|gif|webp)$", a.strip(), re.I)]
    bad_names = [s for a, s in imgs if BAD_IMG_NAME.search(s.split("?")[0])]
    infos.append(f"图片 {len(imgs)} 张")
    if no_alt:
        warns.append(f"{len(no_alt)} 张图片没有描述性 alt（alt 不能为空，也不能只是文件名）")
    if bad_names:
        warns.append(f"{len(bad_names)} 张图片文件名不具描述性，如 {bad_names[0]}")

    # 关键词
    kw = meta.get("primary_keyword", "").strip()
    if kw:
        k = kw.lower()
        first = " ".join(paras)[: (200 if zh else 700)].lower()
        h2_hits = sum(1 for h in h2 if k in h[1].lower())
        alt_hit = any(k in a.lower() for a, _ in imgs)
        for ok, label in [(k in title.lower(), "title"), (bool(h1) and k in h1[0][1].lower(), "H1"),
                          (k in first, "开头 100 词"), (k in desc.lower(), "description"),
                          (h2_hits >= 2, f"至少 2 个 H2（现在 {h2_hits} 个）"), (alt_hit, "图片 alt")]:
            check(ok, f"主关键词「{kw}」出现在 {label}", f"主关键词「{kw}」没有出现在 {label}")
    else:
        warns.append("front-matter 缺少 primary_keyword，跳过关键词检查")

    # 照抄参考文件里的例句：连续 8 个英文词（或 16 个汉字）相同就算照抄
    refs = Path(__file__).resolve().parent.parent / "references"
    examples = []
    for name in ("voice.md", "article-types.md", "nocobase-facts.md"):
        p = refs / name
        if p.exists():
            for l in p.read_text(encoding="utf-8").splitlines():
                l = l.strip()
                if l.startswith(">") or l.startswith("- `") or "「" in l:
                    examples.append(re.sub(r"[`>*\-「」]", " ", l))
    if zh:
        art = re.sub(r"[^一-鿿]", "", no_code)
        grams = {art[i:i + 16] for i in range(len(art) - 15)}
        src = [re.sub(r"[^一-鿿]", "", e) for e in examples]
        copied = sorted({e[i:i + 16] for e in src for i in range(len(e) - 15) if e[i:i + 16] in grams})
    else:
        toks = re.findall(r"[a-z0-9']+", no_code.lower())
        grams = {" ".join(toks[i:i + 8]) for i in range(len(toks) - 7)}
        copied = []
        for e in examples:
            et = re.findall(r"[a-z0-9']+", e.lower())
            hit = next((" ".join(et[i:i + 8]) for i in range(len(et) - 7) if " ".join(et[i:i + 8]) in grams), None)
            if hit and "nocobase" not in hit:  # 产品标准说法（如 💬 栏目说明）允许原样使用
                copied.append(hit)
    copied = list(dict.fromkeys(copied))
    check(not copied, "没有照抄参考文件里的例句",
          f"{len(copied)} 处与参考文件例句相同，改成这篇文章自己的说法：" + "；".join(f"「{c}」" for c in copied[:4]))

    todo = len(re.findall(r"【待核实|TODO|TBD|\[citation", body))
    if todo:
        infos.append(f"还有 {todo} 处【待核实】/TODO，发布前要处理")

    print(f"# 文章自检：{path}（{'中文' if zh else '英文'}）\n")
    print(f"## 需要处理（{len(warns)}）")
    for w in warns:
        print(f"- ⚠️ {w}")
    print(f"\n## 通过（{len(oks)}）")
    for o in oks:
        print(f"- ✅ {o}")
    if infos:
        print("\n## 信息")
        for i in infos:
            print(f"- {i}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(1)
    main(sys.argv[1])
