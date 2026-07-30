---
layout: default
title: 市场观察
permalink: /observations.html
---

# 市场观察

<p style="color: #606060; max-width: 640px; margin-bottom: 2em;">
实时追踪加密市场的机构资金流向、波动率异动、ETF 流量分化及大类资产配置信号。
与「旗舰深度研究」追求完整投研框架不同，本专栏聚焦<b>短期可验证的信号</b> — 数据驱动、迅速反应、持续追踪。
</p>

---

{% if site.categories.observation %}
{% for post in site.categories.observation %}
- **{{ post.date | date: "%Y-%m-%d" }}** — [{{ post.title }}]({{ post.url | relative_url }})
  {% if post.description %}*{{ post.description }}*{% endif %}
{% endfor %}
{% else %}
*尚未发布观察报告。*
{% endif %}

---

<p style="margin-top: 3em; padding-top: 1.5em; border-top: 1px solid #e1e4e8; text-align: center; color: #999; font-size: 0.82em;">
  <a href="{{ '/' | relative_url }}" style="color: #666;">← 返回主页</a>
  &nbsp;·&nbsp;
  © {{ site.time | date: '%Y' }} ZK-Labs Research
</p>