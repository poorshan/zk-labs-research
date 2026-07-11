---
layout: default
title: ZK-Labs Research
---

<div style="text-align: center; margin: 3em 0 1.5em;">

# ZK-Labs Research

### 加密货币与期权深度研究

*Crypto & Options Research*

</div>

<p style="text-align: center; max-width: 560px; margin: 0 auto 1em; color: #606060; font-size: 0.95em; line-height: 1.75;">
由旗下「金戊乾坤2号」投研团队运营，专注期权波动率、加密货币及宏观市场的深度研究。
</p>

<p style="text-align: center; margin-bottom: 3em;">
  <a href="/zk-labs-research/about.html" style="color: #0366d6;">关于我们 →</a>
</p>

<div style="border-top: 1px solid #e1e4e8; margin: 0 auto 3em; max-width: 400px;"></div>

## 最新报告

{% for post in site.posts limit:10 %}
- **{{ post.date | date: "%Y-%m-%d" }}** — [{{ post.title }}]({{ post.url | relative_url }})
{% endfor %}

<div style="margin-top: 4em; padding-top: 1.5em; text-align: center; color: #999; font-size: 0.82em;">
© {{ site.time | date: '%Y' }} ZK-Labs Research
</div>
