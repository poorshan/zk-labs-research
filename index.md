---
layout: default
title: ZK-Labs Research
---

<div style="text-align: center; margin: 3em 0 1.5em;">

# ZK-Labs Research

### 加密货币与期权深度研究

*Crypto & Options Research*

</div>

<p style="text-align: center; max-width: 560px; margin: 0 auto 3em; color: #606060; font-size: 0.95em; line-height: 1.75;">
由旗下「金戊乾坤2号」投研团队运营，专注期权波动率、加密货币及宏观市场的深度研究。
</p>

<div style="border-top: 1px solid #e1e4e8; margin: 0 auto 3em; max-width: 400px;"></div>

## 🏴‍☠️ 旗舰深度研究

- **2026-07-25** — [CRCL (Circle) v2.5.1：从货币基金到金融互联网 — 完整财务模型、市场定价诊断与投资框架]({{ '/research/2026/07/25/crcl-circle-v2-5-1.html' | relative_url }})  
  *DCF 目标价 $164 (+165%) · SOTP $158 · Investment Mosaic 75.9/100 · 附 Companion Document*
- **2026-07-25** — [CRCL Companion Document：研究路线图 & 监控仪表盘]({{ '/research/2026/07/25/crcl-companion-v2-5-1.html' | relative_url }})  
  *Research Roadmap R1–R6 + 完整 Dashboard + 指标详解*

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

<div style="margin-top: 4em; padding-top: 1.5em; border-top: 1px solid #e1e4e8; text-align: center; color: #999; font-size: 0.82em;">
  <a href="{{ '/observations.html' | relative_url }}" style="color: #666;">市场观察</a>
  &nbsp;·&nbsp;
  <a href="{{ '/about.html' | relative_url }}" style="color: #666;">关于我们</a>
  &nbsp;·&nbsp;
  © {{ site.time | date: '%Y' }} ZK-Labs Research
</div>