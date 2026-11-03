---
layout: default
title: 杂谈
permalink: /musings.html
---

<p style="max-width: 640px; margin-bottom: 2em;">
不拘形式的随笔：研究之外的思考、行业见闻与方法札记。
与「旗舰深度研究」追求完整投研框架不同，也与「市场观察」追短期信号不同，
本栏目想到哪写到哪，但每篇仍以事实为底。
</p>

---

{% if site.categories.musings %}
{% for post in site.categories.musings %}
- **{{ post.date | date: "%Y-%m-%d" }}** — [{{ post.title }}]({{ post.url | relative_url }})
  {% if post.description %}*{{ post.description }}*{% endif %}
{% endfor %}
{% else %}
*尚未发布杂谈。*
{% endif %}

---

<p style="margin-top: 3em; padding-top: 1.5em; border-top: 1px solid rgba(255,255,255,.08); text-align: center; color: #94a3b8; font-size: 0.82em;">
  <a href="{{ '/' | relative_url }}" style="color: #38bdf8;">← 返回主页</a>
  &nbsp;·&nbsp;
  © {{ site.time | date: '%Y' }} ZK-Labs Research
</p>
