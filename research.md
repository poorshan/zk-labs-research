---
layout: default
title: 旗舰深度研究
permalink: /research.html
banner_pill: 旗舰研究
description: 完整的机构级投研框架 — 每一篇都可回溯验证。
---

<p style="max-width: 680px; margin-bottom: 2em;">
旗舰深度研究是 ZK-Labs Research 的核心产出：完整投研框架、五级证据标签、一手数据复算。
每一篇报告都通过 GitHub commit 发布，发布时间由 commit 时间戳锁定，不删不改。
</p>

<div class="zk-flag-grid">
{%- assign flagship_posts = site.posts | where: "flagship", true %}
{% for post in flagship_posts %}
<a class="zk-flag-card" href="{{ post.url | relative_url }}">
  <span class="zk-flag-date">{{ post.date | date: "%Y-%m-%d" }}</span>
  <h3>{{ post.title }}</h3>
  <p>{{ post.flagship_summary }}</p>
  <span class="zk-flag-go">阅读报告 →</span>
</a>
{% endfor %}
</div>

---

<p style="margin-top: 3em; padding-top: 1.5em; border-top: 1px solid rgba(255,255,255,.08); text-align: center; color: #94a3b8; font-size: 0.82em;">
  <a href="{{ '/' | relative_url }}" style="color: #38bdf8;">← 返回主页</a>
  &nbsp;·&nbsp;
  © {{ site.time | date: '%Y' }} ZK-Labs Research
</p>
