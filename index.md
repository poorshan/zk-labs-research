---
layout: default
title: 金戊乾坤2号
---

# 金戊乾坤2号 研究团队

**Options · Volatility · Crypto · Macro**

---

专注期权波动率、加密货币及宏观市场深度研究。

## 最新报告

{% for post in site.posts limit:10 %}
- **{{ post.date | date: "%Y-%m-%d" }}** — [{{ post.title }}]({{ post.url | relative_url }})
{% endfor %}

---

<small>© {{ site.time | date: '%Y' }} Golden Wu Qiankun Research. Powered by GitHub Pages.</small>
