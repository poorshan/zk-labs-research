---
layout: default
title: ZK-Labs Research
---

<div class="zk-intro">
  <span class="zk-pill"><span class="zk-pill-dot"></span>EVIDENCE FIRST · MARKET STRUCTURE · DIGITAL ASSETS</span>
  <p>由旗下「金戊乾坤2号 / 金戊乾坤3号」投研团队运营，专注期权波动率、加密货币及宏观市场的深度研究。所有结论均可回溯至一手数据与可复算证据链。</p>
</div>

<section class="zk-stats" aria-label="站点数据">
  <div class="zk-stat"><span class="zk-stat-n" data-n="{{ site.posts | size }}">0</span><span class="zk-stat-l">深度报告</span></div>
  <div class="zk-stat"><span class="zk-stat-n" data-n="{{ site.posts | where: 'flagship', true | size }}">0</span><span class="zk-stat-l">旗舰研究</span></div>
  <div class="zk-stat"><span class="zk-stat-n" data-n="5" data-suffix="级">0</span><span class="zk-stat-l">证据标签体系</span></div>
  <div class="zk-stat"><span class="zk-stat-t">持续更新</span></div>
</section>

## 🏴‍☠️ 旗舰深度研究
{: #flagship }

<div class="zk-flag-grid">
{%- assign flagship_posts = site.posts | where: "flagship", true %}
{% for post in flagship_posts limit:6 %}
<a class="zk-flag-card" href="{{ post.url | relative_url }}">
  <span class="zk-flag-date">{{ post.date | date: "%Y-%m-%d" }}</span>
  <h3>{{ post.title }}</h3>
  <p>{{ post.flagship_summary }}</p>
  <span class="zk-flag-go">阅读报告 →</span>
</a>
{% endfor %}
</div>
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
  <span class="zk-nav-sep">·</span>
  <a class="zk-nav-ext" href="https://vix.zklabsresearch.com" target="_blank" rel="noopener">VIX 量化交易训练站 ↗</a>
</div>