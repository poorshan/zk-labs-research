#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""verify_live_en_pages.py — 线上英文页部署验证（发布后最后一道闸门）

检查每页：
1. HTTP 200 且字节数与本地渲染量级相当（防「200 但内容空」）；
2. <title> 与 front matter title 一致；
3. 关键承重句/标题存在；
4. 表格数、行数、目录锚点零悬空；
5. 页内不出现 {#id} 字面量（kramdown 未解析会漏出）。
"""
import re
import subprocess
import sys

PAGES = [
    ("https://www.zklabsresearch.com/research/2026/10/03/eth-value-capture-v2-en.html",
     "Ethereum Value Capture v2.0", "From Protocol Cash Flow to Network Value Transmission",
     ["Eight-segment", "Part II", "disconfirmation register"], 92, 676),
    ("https://www.zklabsresearch.com/research/2026/10/10/eth-value-capture-v2-4-supplement-en.html",
     "Ethereum Value Capture v2.4 Supplement", "Fix Hypotheses and Verification Paths",
     ["three-layer root-cause", "Proposal A", "Partially demonstrated"], 8, 49),
]


def fetch(url):
    for _ in range(3):
        r = subprocess.run(["curl", "-s", "-w", "\n%{http_code}", "--max-time", "30", url],
                           capture_output=True, text=True)
        if r.returncode == 0 and r.stdout.strip():
            body, _, code = r.stdout.rpartition("\n")
            if code.strip() == "200":
                return body, 200
    return "", 0


def main():
    ok = True
    for url, title_part, sub_part, musts, min_tables, min_rows in PAGES:
        html, code = fetch(url)
        print("=" * 70)
        print(url)
        if code != 200:
            print("  FAIL http=%s" % code)
            ok = False
            continue
        ids = set(re.findall(r'id="([^"]+)"', html))
        hrefs = set(re.findall(r'href="#([^"]+)"', html))
        tables = len(re.findall(r"<table", html))
        rows = len(re.findall(r"<tr", html))
        title = re.search(r"<title>(.*?)</title>", html, re.S)
        title = title.group(1).strip() if title else ""
        checks = [
            ("bytes>100k" if min_tables > 50 else "bytes>20k",
             len(html) > (100000 if min_tables > 50 else 20000)),
            ("title", title_part in title),
            ("subtitle", sub_part in html[:6000] or sub_part in title),
            ("tables>=%d" % min_tables, tables >= min_tables),
            ("tr>=%d" % min_rows, rows >= min_rows),
            ("anchors_resolve", len(hrefs - ids) == 0),
            ("no_literal_id", html.count("{#") == 0),
        ]
        print("  bytes=%d tables=%d tr=%d ids=%d anchors=%d dangling=%d" % (
            len(html), tables, rows, len(ids), len(hrefs), len(hrefs - ids)))
        print("  title=%s" % title[:90])
        for name, cond in checks:
            print("  %-16s %s" % (name, "OK" if cond else "FAIL"))
            ok &= cond
        for m in musts:
            c = m in html
            print("  %-16s %s" % ("text:" + m[:12], "OK" if c else "FAIL"))
            ok &= c
    print("=" * 70)
    print("RESULT", "PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
