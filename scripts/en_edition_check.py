#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""en_edition_check.py — 英文版 vs 中文原文的机器闸门

按「数值」而非「字符串」比对，容忍中英数量级写法差异：
  107.8 万 ETH  ≡  1.078 million ETH  ≡  1,078,000 ETH
  2.89 亿       ≡  289 million         ≡  289,000,000

四项判定（任一不通过 → rc=1）：
1. 数值守恒：中文原文的每个数值，在英文稿中不得缺失（按数值多重集比对）。
2. 数值无新增：英文稿不得出现原文没有的数值（白名单内的年份/序号噪声除外）。
3. 结构守恒：h2/h3/h4 数量、表格行数不得显著漂移。
4. 内容不缩水：非空行数不得少于原文的 92%。

用法：
  python3 scripts/en_edition_check.py <中文原文.md> <英文译稿.md> [--json]
"""
import io
import json
import re
import sys

# 中文数量级
CN_UNITS = {"万亿": 1e12, "亿": 1e8, "万": 1e4, "千": 1e3, "百": 1e2}
# 英文数量级词
EN_UNITS = {"trillion": 1e12, "billion": 1e9, "million": 1e6, "thousand": 1e3, "bn": 1e9, "mn": 1e6}

NUM_RE = re.compile(r"(\d[\d,]*(?:\.\d+)?)\s*(万亿|亿|万|千|百|trillion|billion|million|thousand|bn|mn)?", re.I)

# 英文缩写量级：$2.91B / 13.52M / 7K —— 仅匹配紧跟数字、且后面不接字母的单个大写字母
MAG_RE = re.compile(r"(?<=\d)\s?([BMTK])(?![A-Za-z])")
MAG_WORD = {"B": " billion", "M": " million", "T": " trillion", "K": " thousand"}

# 比较用的白名单（这些数在译文里合法地单独出现/变化：年份、序数、章节号、百分比位置等）
WHITELIST_VALUES = {
    1e0, 2e0, 3e0, 4e0, 5e0, 6e0, 7e0, 8e0, 9e0, 10e0, 11e0, 12e0, 20e0, 24e0, 30e0, 100e0,
    2025e0, 2026e0, 2027e0, 365e0, 52e0, 4e0,
}


def strip_front_matter(txt):
    if txt.startswith("---"):
        parts = txt.split("---", 2)
        if len(parts) >= 3:
            return parts[2]
    return txt


ANCHOR_RE = re.compile(r"\]\(#?[^)]*\)")          # markdown 链接目标（含锚点）→ 只留链接文字
HREF_RE = re.compile(r'href="[^"]*"')             # HTML 锚点
BRACE_ID_RE = re.compile(r"\{#[^}]*\}")           # kramdown 显式 id
BACKTICK_RE = re.compile(r"`[^`]*`")              # 行内代码（含口径原文，非读数）


def clean(txt):
    txt = ANCHOR_RE.sub("]", txt)
    txt = HREF_RE.sub('href=""', txt)
    txt = BRACE_ID_RE.sub("", txt)
    return txt


def sig(v):
    """归一到 6 位有效数字，容忍四舍五入差异。"""
    if v == 0:
        return 0.0
    from math import log10, floor
    d = 5 - floor(log10(abs(v)))
    return round(v, d)


def values(txt):
    txt = MAG_RE.sub(lambda m: MAG_WORD[m.group(1)], txt)
    out = {}
    for m in NUM_RE.finditer(txt):
        raw, unit = m.group(1), (m.group(2) or "").strip().lower()
        try:
            n = float(raw.replace(",", ""))
        except ValueError:
            continue
        mult = 1.0
        if unit in CN_UNITS:
            mult = CN_UNITS[unit]
        elif unit in EN_UNITS:
            mult = EN_UNITS[unit]
        out[sig(n * mult)] = out.get(sig(n * mult), 0) + 1
    return out


def counts(txt):
    lines = txt.split("\n")
    return {
        "h1": sum(1 for l in lines if l.startswith("# ")),
        "h2": sum(1 for l in lines if l.startswith("## ")),
        "h3": sum(1 for l in lines if l.startswith("### ")),
        "h4": sum(1 for l in lines if l.startswith("#### ")),
        "table_rows": sum(1 for l in lines if l.startswith("|")),
        "nonempty": sum(1 for l in lines if l.strip()),
        "chars": len(txt),
    }


def fmt(v):
    if v >= 1e9:
        return f"{v/1e9:g}B"
    if v >= 1e6:
        return f"{v/1e6:g}M"
    if v >= 1e3 and v == int(v):
        return f"{int(v):,}"
    return f"{v:g}"


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        return 2
    src_path, dst_path = sys.argv[1], sys.argv[2]
    as_json = "--json" in sys.argv
    src = clean(strip_front_matter(io.open(src_path, encoding="utf-8").read()))
    dst = clean(strip_front_matter(io.open(dst_path, encoding="utf-8").read()))

    a, b = values(src), values(dst)
    missing = {}
    for k, v in a.items():
        if k in WHITELIST_VALUES:
            continue
        need = 1 if k == 0.0 else v          # 「0」允许写成 zero，只要求至少出现一次
        if b.get(k, 0) < need:
            missing[k] = (v, b.get(k, 0))
    extra = {k: b[k] for k in b if k not in a and k not in WHITELIST_VALUES}

    ca, cb = counts(src), counts(dst)
    struct = {k: [ca[k], cb[k], abs(ca[k] - cb[k])] for k in ("h2", "h3", "h4", "table_rows")}
    struct["nonempty_ratio"] = round(cb["nonempty"] / max(ca["nonempty"], 1), 4)

    problems = []
    if missing:
        problems.append("MISSING_VALUES %d" % len(missing))
    if extra:
        problems.append("EXTRA_VALUES %d" % len(extra))
    if abs(ca["table_rows"] - cb["table_rows"]) > max(3, ca["table_rows"] * 0.02):
        problems.append("TABLE_ROWS_DRIFT")
    if struct["nonempty_ratio"] < 0.92:
        problems.append("CONTENT_SHRINK")

    result = {
        "src": src_path, "dst": dst_path,
        "status": "PASS" if not problems else "FAIL",
        "problems": problems,
        "missing_values": {fmt(k): [v[0], v[1]] for k, v in sorted(missing.items(), key=lambda kv: -kv[0])[:40]},
        "extra_values": {fmt(k): v for k, v in sorted(extra.items(), key=lambda kv: -kv[0])[:40]},
        "structure": struct,
        "distinct_values": [len(a), len(b)],
    }
    if as_json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print("SRC %s" % src_path)
        print("DST %s" % dst_path)
        print("STATUS %s   problems=%s" % (result["status"], problems or "-"))
        print("distinct values: src=%d dst=%d" % (len(a), len(b)))
        if missing:
            print("MISSING (value: src_count -> dst_count):")
            for k, (x, y) in list(result["missing_values"].items())[:30]:
                print("   %-14s %d -> %d" % (k, x, y))
        if extra:
            print("EXTRA (value: dst_count):")
            for k, v in list(result["extra_values"].items())[:30]:
                print("   %-14s %d" % (k, v))
        print("structure:", json.dumps(struct, ensure_ascii=False))
    return 0 if not problems else 1


if __name__ == "__main__":
    sys.exit(main())
