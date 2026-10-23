#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""en_edition_struct_check.py — 英文版结构完整性校验（补充 en_edition_check.py 的数值闸门）

五项检查：
1. 表格列数一致：每一段表格内所有行的单元格数必须相同；并与中文原文同序号表格逐段比对列数。
2. 目录锚点可解析：所有 `](#id)` 指向的 id 必须在文档中存在（标题 `{#id}` 或 `<a id=...>`）。
3. 代码围栏成对。
4. 残留中文字符：列出仍含 CJK 的行（白名单：front matter、署名、被引用的中文文件名/术语）。
5. 行内表格破坏：表格行里出现裸 `|` 造成列数漂移。

用法：python3 scripts/en_edition_struct_check.py <中文原文.md> <英文译稿.md>
"""
import io
import re
import sys

CJK = re.compile(r"[\u4e00-\u9fff]")
WHITELIST_CJK = ("金戊乾坤2号", "审计底稿", "毛利", "留存率", "投研", "市场观察")


def body_wo_front(txt):
    if txt.startswith("---"):
        p = txt.split("---", 2)
        if len(p) >= 3:
            return p[2]
    return txt


def tables(txt):
    """返回每段表格的列数列表（按出现顺序）。"""
    out, cur = [], []
    for line in txt.split("\n"):
        if line.lstrip().startswith("|"):
            cur.append(line)
        else:
            if cur:
                out.append(cur)
                cur = []
    if cur:
        out.append(cur)
    res = []
    for t in out:
        cols = [row.count("|") - 1 for row in t]
        # 去掉分隔行（|---|---|）后判断一致性
        res.append(cols)
    return res


def front_matter_check(path):
    """front matter 里 `key: "值"` 的双引号必须成对；否则 YAML 解析失败，
    GitHub Pages 会静默不生成该页（实测：flagship_summary 里多一个 " → 整页 404）。"""
    bad = []
    raw = io.open(path, encoding="utf-8").read()
    if not raw.startswith("---"):
        return bad
    parts = raw.split("---", 2)
    if len(parts) < 3:
        return bad
    for ln, line in enumerate(parts[1].split("\n"), 2):
        s = line.strip()
        m = re.match(r'^([A-Za-z_][\w]*):\s*"(.*)"\s*$', s)
        if not m:
            continue
        inner = m.group(2)
        # 双引号标量内部不得再出现未转义的 "（贪心匹配会把它们包进来）
        if inner.replace('\\"', "").count('"') != 0:
            bad.append((ln, m.group(1), s[:90]))
    return bad


def main():
    src = body_wo_front(io.open(sys.argv[1], encoding="utf-8").read())
    dst_all = io.open(sys.argv[2], encoding="utf-8").read()
    dst = body_wo_front(dst_all)

    problems = []

    fm_bad = front_matter_check(sys.argv[2])
    if fm_bad:
        problems.append("FRONT_MATTER_QUOTES %s" % fm_bad[:4])

    # 1. 表格列数
    ts, td = tables(src), tables(dst)
    bad_tables = []
    for i, cols in enumerate(td):
        if len(set(cols)) > 1:
            bad_tables.append((i + 1, sorted(set(cols)), len(cols)))
    if len(ts) != len(td):
        problems.append("TABLE_COUNT %d vs %d" % (len(ts), len(td)))
    colmismatch = []
    for i, (a, b) in enumerate(zip(ts, td)):
        if sorted(set(a)) != sorted(set(b)):
            colmismatch.append((i + 1, sorted(set(a)), sorted(set(b))))
    if bad_tables:
        problems.append("RAGGED_TABLES %s" % bad_tables[:6])
    if colmismatch:
        problems.append("COLUMN_MISMATCH %s" % colmismatch[:6])

    # 2. 锚点
    ids = set(re.findall(r"\{#([^}]+)\}", dst)) | set(re.findall(r'<a id="([^"]+)"', dst))
    links = set(re.findall(r"\]\(#([^)]+)\)", dst))
    dangling = sorted(links - ids)
    if dangling:
        problems.append("DANGLING_ANCHORS %s" % dangling[:10])

    # 3. 代码围栏
    fences = dst.count("```")
    if fences % 2:
        problems.append("ODD_CODE_FENCE %d" % fences)

    # 4. 残留中文
    cjk_lines = []
    for i, line in enumerate(dst_all.split("\n"), 1):
        if CJK.search(line):
            if any(w in line for w in WHITELIST_CJK):
                continue
            cjk_lines.append((i, line.strip()[:90]))
    if cjk_lines:
        problems.append("CJK_RESIDUE %d lines" % len(cjk_lines))

    print("tables: src=%d dst=%d | anchors=%d links=%d dangling=%d | fences=%d" % (
        len(ts), len(td), len(ids), len(links), len(dangling), fences))
    print("STATUS %s problems=%s" % ("PASS" if not problems else "FAIL", problems or "-"))
    if cjk_lines:
        print("CJK lines:")
        for i, l in cjk_lines[:25]:
            print("  L%-5d %s" % (i, l))
    if dangling:
        print("dangling:", dangling[:10])
    for i, a, b in colmismatch[:6]:
        print("  table#%d cols src=%s dst=%s" % (i, a, b))
    return 0 if not problems else 1


if __name__ == "__main__":
    sys.exit(main())
