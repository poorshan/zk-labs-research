#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""assemble_r1_en.py — 把 .en_chunks/ 里的分块译稿拼成 R1 英文版单文件。

做四件事：
1. 按顺序拼接分块（自动补空行，防止标题粘连）；
2. 给每个标题补显式 kramdown id，并把目录锚点重写成英文 slug；
3. 写入 front matter（旗舰研究、英文路由、translation_of）；
4. 打印结构核对（h2/h3/h4 数、表格行数、总字符），供 en_edition_check.py 复核。
"""
import io
import os
import re
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(BASE)
CH = os.path.join(ROOT, ".en_chunks")
ORDER = [
    "AB_summary_part1.md",
    "CD_conclusion_audit.md",
    "EFG_framework_matrix_counterfactual.md",
    "GH_evidence_disconfirmation_dashboard.md",
    "IJ_dashboard_appendixAB.md",
    "KL_appendixCDE.md",
]
OUT = os.path.join(ROOT, "_posts", "2026-10-03-eth-value-capture-v2-en.md")

FRONT = """---
layout: default
title: "Ethereum Value Capture v2.0 — From Protocol Cash Flow to Network Value Transmission"
permalink: /research/2026/10/03/eth-value-capture-v2-en.html
date: 2026-10-03
categories: research
author: 金戊乾坤2号
lang: en
translation_of: /research/2026/10/03/eth-value-capture-v2.html
version: "v2.0 (English ed. 1.0)"
data_cutoff: 2026-10-02
flagship: false
flagship_summary: "Eight-segment transmission chain + four-layer capture framework + five channels · disconfirmation register and monitoring dashboard · every load-bearing figure independently recomputable · UNKNOWN retained as part of the research conclusion"
description: "ZK Labs Ethereum value capture special report v2.0 — reframing the question from 'can ETH capture value' to 'through what transmission mechanism does value reach ETH'; eight-segment transmission chain, four-layer capture framework, five channels, disconfirmation register, monitoring dashboard."
tags: [Ethereum, ValueCapture, ETH, L2, Blob, Stablecoin, Staking, Transmission, Counterfactual, Research]
---
"""

KEEP_ANCHOR = {"errata-1"}


def slugify(text):
    t = re.sub(r"`", "", text)
    t = re.sub(r"\*\*|__|\*|_", "", t)
    t = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", t)
    t = t.lower()
    t = re.sub(r"[^a-z0-9]+", "-", t)
    t = t.strip("-")[:80] or "sec"
    # kramdown 不接受以数字开头的 id（会把 {@...} 当正文），必须补字母前缀
    if not t[0].isalpha():
        t = "sec-" + t
    return t


def main():
    parts = []
    missing = []
    for name in ORDER:
        p = os.path.join(CH, name)
        if not os.path.exists(p):
            missing.append(name)
            continue
        parts.append(io.open(p, encoding="utf-8").read().strip("\n"))
    if missing:
        print("MISSING CHUNKS: %s" % missing)
        return 2
    body = "\n\n".join(parts)

    lines = body.split("\n")
    # 定位目录区
    try:
        toc_start = next(i for i, l in enumerate(lines) if l.strip().lower() in ("## table of contents", "## contents"))
    except StopIteration:
        print("NO TOC FOUND")
        return 3
    toc_end = toc_start + 1
    while toc_end < len(lines) and (lines[toc_end].startswith("- ") or lines[toc_end].startswith("  - ") or not lines[toc_end].strip()):
        toc_end += 1

    toc_idx = [i for i in range(toc_start + 1, toc_end) if lines[i].lstrip().startswith("- [")]
    headings = [i for i, l in enumerate(lines) if re.match(r"^##[^#]", l) and i > toc_end] + \
               [i for i, l in enumerate(lines) if l.startswith("### ")]
    headings = sorted(set(headings))

    used = set()
    j = 0
    rewritten = 0
    for ti in toc_idx:
        line = lines[ti]
        m = re.match(r"^(\s*- )\[(.+?)\]\(#(.+?)\)\s*$", line)
        if not m:
            continue
        indent, text, old = m.group(1), m.group(2), m.group(3)
        if old in KEEP_ANCHOR:
            continue
        # 找到与之匹配的标题：按顺序取下一个
        if j >= len(headings):
            print("TOC OVERRUN at: %s" % text)
            break
        hi = headings[j]
        j += 1
        htxt = re.sub(r"\s*\{#[^}]*\}", "", lines[hi]).lstrip("#").strip()
        sid = slugify(htxt)
        base_id = sid
        k = 2
        while sid in used:
            sid = "%s-%d" % (base_id, k)
            k += 1
        used.add(sid)
        lines[hi] = "%s {#%s}" % (lines[hi].rstrip(), sid)
        lines[ti] = "%s[%s](#%s)" % (indent, text, sid)
        rewritten += 1

    out = FRONT + "\n" + "\n".join(lines).strip("\n") + "\n"
    # 英文版内部交叉引用指向英文补充章
    out = out.replace("(/research/2026/10/10/eth-value-capture-v2-4-supplement.html)",
                      "(/research/2026/10/10/eth-value-capture-v2-4-supplement-en.html)")
    io.open(OUT, "w", encoding="utf-8").write(out)

    body_lines = out.split("\n")
    print("OUT %s" % OUT)
    print("chars=%d lines=%d" % (len(out), len(body_lines)))
    print("h2=%d h3=%d h4=%d table_rows=%d" % (
        sum(1 for l in body_lines if l.startswith("## ")),
        sum(1 for l in body_lines if l.startswith("### ")),
        sum(1 for l in body_lines if l.startswith("#### ")),
        sum(1 for l in body_lines if l.startswith("|"))))
    print("toc_entries=%d rewritten=%d headings_seen=%d" % (len(toc_idx), rewritten, j))
    return 0


if __name__ == "__main__":
    sys.exit(main())
