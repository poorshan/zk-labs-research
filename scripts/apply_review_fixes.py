#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""apply_review_fixes.py — 把两份独立复核报告里的 10 条意见落到英文稿

原则：只做「等价表达」层面的修正（术语统一、还原悬垂词、删译者注、补回元数据漏句），
不动任何数字、单位、证据标签、结论强度。
每条都断言替换次数，次数不符即报错退出（fail-closed）。
"""
import io
import re
import sys

R1 = "/Users/ivanwang/ZKLabs/zk-labs-research/_posts/2026-10-03-eth-value-capture-v2-en.md"
R2 = "/Users/ivanwang/ZKLabs/zk-labs-research/_posts/2026-10-10-eth-value-capture-v2-4-supplement-en.md"

errors = []


def sub(path, old, new, expect, label, regex=False):
    t = io.open(path, encoding="utf-8").read()
    if regex:
        t2, n = re.subn(old, new, t)
    else:
        n = t.count(old)
        t2 = t.replace(old, new)
    if n != expect:
        errors.append("%s: expected %d got %d" % (label, expect, n))
        return
    io.open(path, "w", encoding="utf-8").write(t2)
    print("OK  %-46s x%d" % (label, n))


# ---------- R1 ----------
# 1. 还原中文原文的悬垂词 Ethereum（不替原文补出归属断言）
sub(R1, "(post-4844 window average; current trailing 30 days 2.52%) on Ethereum)",
    "(post-4844 window average; current trailing 30 days 2.52%) Ethereum)",
    1, "R1-1 dangling Ethereum")

# 2. 量级比 → magnitude ratio（全文统一，原 14 处 scale ratio）
sub(R1, "scale ratios", "magnitude ratios", 2, "R1-2a scale ratios")
sub(R1, "scale ratio", "magnitude ratio", 12, "R1-2b scale ratio")

# 3. 4844 后窗口均值：window mean(s) → window average(s)
sub(R1, "window means", "window averages", 2, "R1-3a window means")
sub(R1, "window mean", "window average", 2, "R1-3b window mean")

# 4. 拆分口径 → split definition
sub(R1, "(decomposed definition)", "(split definition)", 1, "R1-4a decomposed (paren)")
sub(R1, "is a decomposed definition", "is a split definition", 1, "R1-4b decomposed (prose)")

# 5. 删掉正文里的译者注（移到 .en_chunks/QA_notes_en.md）
sub(R1, r" <!-- NOTE: source repeats the word \"measured\" here; rendered once\. -->", "", 1, "R1-5a NOTE measured")
sub(R1, r" <!-- NOTE: source cell is grammatically broken here \(\"…2\.52%） Ethereum\"\); structure preserved\. -->", "", 1, "R1-5b NOTE broken cell")
sub(R1, r" <!-- NOTE: source jumps from \"### 0\.\" to \"### 2\.\" with no §1 present; numbering preserved\. -->", "", 1, "R1-5c NOTE numbering")

# 6. 量词 two channels
sub(R1, 'split "stablecoins transmit nothing" into issuer / on-chain channels',
    'split "stablecoins transmit nothing" into two channels, issuer / on-chain',
    1, "R1-6 two channels")

# 7. 「支付链」中性化，不替原文断言方向
sub(R1, "builder / searcher payments to the chain", "builder / searcher payment path", 1, "R1-7 payment path")

# ---------- R2 ----------
# 8. 状态标签回到系列受控词表
sub(R2, "| 4 Protocol-layer fee capture | Partially holds |",
    "| 4 Protocol-layer fee capture | Partially demonstrated |", 1, "R2-8a tag seg4")
sub(R2, "| 5 Token utility and demand | Partially holds |",
    "| 5 Token utility and demand | Partially demonstrated |", 1, "R2-8b tag seg5")

# 9. flagship_summary 补回勘误披露
sub(R2, "each with evidence status, economic constraint and failure condition.\"",
    "each with evidence status, economic constraint and failure condition · figures corrected per \"v2.0 Errata 1\".\"",
    1, "R2-9 summary errata")

# 10. description 补回「承接两处断点」+ 失败条件用词
sub(R2, "special report, v2.4 supplement — a three-layer root-cause framework and seven fix hypotheses A-G, each tagged with evidence status, economic constraints and falsification conditions.",
    "special report, v2.4 supplement — building on the two breakpoints in v2.0, a three-layer root-cause framework (claim / transmission / premium) and seven fix hypotheses A-G, each tagged with evidence status, economic constraints and failure conditions; figures corrected per \"v2.0 Errata 1\".",
    1, "R2-10 description")

if errors:
    print("\nFAILED:")
    for e in errors:
        print("  " + e)
    sys.exit(1)
print("\nALL FIXES APPLIED")
