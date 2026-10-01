#!/usr/bin/env python3
"""检查 ZK Labs 文章头部的 Markdown 「连续行合并」风险。

背景：文章头部这几行若写成连续行，Markdown 会合并成一整段：
    **ZK Labs 市场观察 ｜ 副标题**
    署名：南野东亦 ｜ 日期
    **数据截点**：...
    **声明**：...
渲染后是流动文字，不是四行。修法 = 组内非末行行尾补两个空格（硬换行）。

用法：
    cd /root/zk-labs-research/_posts
    python3 <此脚本>            # 仅检查
    python3 <此脚本> --fix      # 检查并自动修复
"""
import glob, re, sys

HARD_BREAK = "  "  # 两个空格 = Markdown 硬换行

def is_plain(ln):
    s = ln.strip()
    if not s:
        return False
    if s.startswith(("#", ">", "|", "---", "- ", "* ", "+ ")):
        return False
    if re.match(r"^\d+\.\s", s):
        return False
    return True

def header_block(lines):
    """返回 (start, end) —— frontmatter 之后到第一个 --- 之前的正文头部。"""
    if not lines or lines[0].strip() != "---":
        return None
    try:
        fm_end = lines.index("---", 1)
    except ValueError:
        return None
    try:
        body_end = lines.index("---", fm_end + 1)
    except ValueError:
        body_end = len(lines)
    return fm_end + 1, body_end

def scan(path):
    """返回连续行分组列表。每项为 [(行号, 内容), ...]。"""
    lines = open(path, encoding="utf-8").read().split("\n")
    bounds = header_block(lines)
    if not bounds:
        return []
    start, end = bounds

    groups, cur = [], []
    for i in range(start, end):
        ln = lines[i]
        if is_plain(ln):
            cur.append((i + 1, ln))
            if ln.endswith(HARD_BREAK):  # 已硬换行，截断
                if len(cur) > 1:
                    groups.append(cur)
                cur = []
        else:
            if len(cur) > 1:
                groups.append(cur)
            cur = []
    if len(cur) > 1:
        groups.append(cur)
    return groups

def fix(path):
    lines = open(path, encoding="utf-8").read().split("\n")
    bounds = header_block(lines)
    if not bounds:
        return 0
    start, end = bounds
    changed, i = 0, start
    while i < end:
        if is_plain(lines[i]):
            j = i
            while j + 1 < end and is_plain(lines[j + 1]):
                j += 1
            for k in range(i, j):  # 组内除最后一行
                if not lines[k].endswith(HARD_BREAK):
                    lines[k] = lines[k].rstrip() + HARD_BREAK
                    changed += 1
            i = j + 1
        else:
            i += 1
    if changed:
        open(path, "w", encoding="utf-8").write("\n".join(lines))
    return changed

def main():
    do_fix = "--fix" in sys.argv
    files = sorted(glob.glob("*.md"))
    if not files:
        print("未找到 .md 文件（请在 _posts 目录下运行）")
        return 1

    total, touched = 0, []
    for f in files:
        n = fix(f) if do_fix else 0
        groups = scan(f)
        if n:
            total += n
            touched.append((f, n))
            print(f"✓ {f}: 修正 {n} 行")
        elif groups:
            print(f"⚠️  {f}: {len(groups)} 处连续行风险")
            for grp in groups:
                print(f"     L{grp[0][0]}–L{grp[-1][0]} ({len(grp)} 行): {grp[0][1][:60]}")

    print(f"\n扫描 {len(files)} 篇")
    if do_fix:
        print(f"修复 {len(touched)} 篇，共 {total} 行")
    else:
        bad = sum(1 for f in files if scan(f))
        print("✅ 未发现风险" if not bad else f"⚠️  {bad} 篇存在风险（加 --fix 自动修复）")
    return 0

if __name__ == "__main__":
    sys.exit(main())
