---
layout: default
title: ZK-Labs Research
hero_image: /assets/images/hero-lab.jpg
hide_header_text: true
---



<div class="zk-intro">
  <span class="zk-pill"><span class="zk-pill-dot"></span>EVIDENCE FIRST · MARKET STRUCTURE · DIGITAL ASSETS</span>
  <p>由旗下「金戊乾坤2号」投研团队运营，专注期权波动率、加密货币及宏观市场的深度研究。所有结论均可回溯至一手数据与可复算证据链。</p>
</div>

## 🏴‍☠️ 旗舰深度研究

{%- comment -%}
自动生成——请勿手工编辑本列表。
新文章加入本栏：在该文 front matter 写 flagship: true 与 flagship_summary: "…"。
排序由 site.posts（Jekyll 默认按日期倒序）保证，不会错位。
{%- endcomment -%}
{%- assign flagship_posts = site.posts | where: "flagship", true %}
{% for post in flagship_posts %}
- **{{ post.date | date: "%Y-%m-%d" }}** — [{{ post.title }}]({{ post.url | relative_url }})  
  *{{ post.flagship_summary }}*
{% endfor %}
---

## 📡 市场观察

<p style="color: #606060; max-width: 640px;">
实时追踪机构资金流向、ETF 流量分化及大类资产配置信号。与深度研究不同，本专栏聚焦<b>短期可验证的信号</b>。
</p>

{% if site.categories.observation %}
{% for post in site.categories.observation limit:3 %}
- **{{ post.date | date: "%Y-%m-%d" }}** — [{{ post.title }}]({{ post.url | relative_url }})
  {% if post.description %}*{{ post.description }}*{% endif %}
{% endfor %}
{% endif %}

[→ 查看全部市场观察]({{ '/observations.html' | relative_url }})

---

## 全部报告

{% for post in site.posts %}
{% unless post.categories contains 'observation' %}
- **{{ post.date | date: "%Y-%m-%d" }}** — [{{ post.title }}]({{ post.url | relative_url }})
{% endunless %}
{% endfor %}

<div class="zk-page-nav">
  <a href="{{ '/observations.html' | relative_url }}">市场观察</a>
  <span class="zk-nav-sep">·</span>
  <a href="{{ '/about.html' | relative_url }}">关于我们</a>
</div>