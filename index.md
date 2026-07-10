---
layout: default
title: ZK Labs Research
---

<div style="text-align: center; margin: 2em 0 0.5em;">

# ⚡ ZK Labs Research

### 机构级加密与期权投研

*Institutional-Grade Crypto & Options Research*

</div>

---

**ZK Labs Research** 由旗下「金戊乾坤2号」投研团队运营，专注期权波动率、加密货币及宏观市场的深度研究。我们为机构投资者和高级交易者提供数据驱动、逻辑严密的独立分析。

---

## 最新报告

{% for post in site.posts limit:10 %}
- **{{ post.date | date: "%Y-%m-%d" }}** — [{{ post.title }}]({{ post.url | relative_url }})
{% endfor %}

---

<small>© {{ site.time | date: '%Y' }} ZK Labs Research. Powered by GitHub Pages.</small>
