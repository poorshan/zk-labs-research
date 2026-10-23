#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""fix_table_pipes.py — 修复英文版表格列数漂移

成因：中文原文在单元格内用全角「｜」做并列分隔；英文译稿把它换成了半角「|」，
在 Markdown 里就变成额外的列分隔符，导致整张表错列。

做法：以中文原文为基准，逐表逐行对齐——
  原文该行有 N 个单元格，第 i 个单元格内含 k_i 个「｜」；
  译稿该行按「|」切出的记号数应为 N + Σk_i；
  若相等，则把每个单元格的 k_i+1 个记号用「; 」重新合并，恢复 N 列。
记号数不等的行原样保留并报告，供人工核对。

用法：python3 scripts/fix_table_pipes.py <中文原文.md> <英文译稿.md> [--write]
"""
import io
import re
import sys


def table_blocks(lines):
    blocks, cur = [], []
    for i, l in enumerate(lines):
        if l.lstrip().startswith("|"):
            cur.append(i)
        else:
            if cur:
                blocks.append(cur)
                cur = []
    if cur:
        blocks.append(cur)
    return blocks


def cells_of(line):
    s = line.strip()
    if s.startswith("|"):
        s = s[1:]
    if s.endswith("|"):
        s = s[:-1]
    return s.split("|")


def main():
    src_p, dst_p = sys.argv[1], sys.argv[2]
    write = "--write" in sys.argv
    src = io.open(src_p, encoding="utf-8").read().split("\n")
    dst = io.open(dst_p, encoding="utf-8").read().split("\n")

    sb, db = table_blocks(src), table_blocks(dst)
    print("tables src=%d dst=%d" % (len(sb), len(db)))
    fixed = 0
    unfixed = []
    for t, (s_idx, d_idx) in enumerate(zip(sb, db), 1):
        if len(s_idx) != len(d_idx):
            unfixed.append((t, "row-count %d vs %d" % (len(s_idx), len(d_idx))))
            continue
        for s_i, d_i in zip(s_idx, d_idx):
            s_cells = cells_of(src[s_i])
            n = len(s_cells)
            ks = [c.count("｜") for c in s_cells]
            d_cells = cells_of(dst[d_i])
            need = n + sum(ks)
            if len(d_cells) == n:
                continue                      # 已正常
            if len(d_cells) != need:
                unfixed.append((t, "line %d tokens %d != expected %d" % (d_i + 1, len(d_cells), need)))
                continue
            out, p = [], 0
            for i in range(n):
                take = ks[i] + 1
                out.append("; ".join(x.strip() for x in d_cells[p:p + take]).strip())
                p += take
            dst[d_i] = "| " + " | ".join(out) + " |"
            fixed += 1

    print("rows fixed=%d | unfixed=%d" % (fixed, len(unfixed)))
    for t, msg in unfixed[:15]:
        print("  table#%d: %s" % (t, msg))
    if write and fixed:
        io.open(dst_p, "w", encoding="utf-8").write("\n".join(dst))
        print("WROTE %s" % dst_p)
    return 0 if not unfixed else 1


if __name__ == "__main__":
    sys.exit(main())
