#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""fix_blockquote_pipes.py — 修复非表格行里的半角竖线

成因：中文原文在**正文、引用块、列表**里用全角「｜」作并列分隔；英文译稿换成了半角「|」，
kramdown(GFM) 会把含「|」的段落当成表格解析 —— 结果是一行三列的假表格，页面排版崩掉。

做法：只处理「不是表格行、也不是标题」的行；把它们里面的半角 `|` 还原为全角 `｜`
（行内代码反引号内的内容不动）。表格行保持原样。

用法：python3 scripts/fix_blockquote_pipes.py <英文译稿.md> [--write]
"""
import io
import re
import sys


def fix_line(line):
    out = []
    for k, seg in enumerate(line.split("`")):
        if k % 2 == 1:          # 反引号内的行内代码，原样保留
            out.append(seg)
        else:
            out.append(seg.replace("\\|", "｜").replace("|", "｜"))
    return "`".join(out)


def main():
    path = sys.argv[1]
    write = "--write" in sys.argv
    lines = io.open(path, encoding="utf-8").read().split("\n")
    changed = 0
    samples = []
    # 跳过 front matter（首个 --- 到第二个 --- 之间）
    fm_end = 0
    if lines and lines[0].strip() == "---":
        try:
            fm_end = lines.index("---", 1)
        except ValueError:
            fm_end = 0
    for i, line in enumerate(lines):
        s = line.lstrip()
        if i <= fm_end:
            continue
        if s.startswith("|") or s.startswith("#"):
            continue
        if "|" not in line:
            continue
        new = fix_line(line)
        if new != line:
            if len(samples) < 5:
                samples.append((i + 1, line.strip()[:100]))
            lines[i] = new
            changed += 1
    print("%s: lines changed=%d" % (path.split("/")[-1], changed))
    for n, t in samples:
        print("  L%-5d %s" % (n, t))
    if write and changed:
        io.open(path, "w", encoding="utf-8").write("\n".join(lines))
        print("WROTE %s" % path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
