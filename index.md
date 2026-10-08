---
layout: default
title: ZK-Labs Research
hero_image: /assets/images/hero-lab.jpg
hide_header_text: true
---



<div class="zk-intro">
  <span class="zk-pill"><span class="zk-pill-dot"></span>EVIDENCE FIRST · MARKET STRUCTURE · DIGITAL ASSETS</span>
  <p>由旗下「金戊乾坤2号」投研团队运营，专注期权波动率、加密货币及宏观市场的深度研究。所有结论均可回溯至一手数据与可复算证据链。</p>
  <div class="zk-cta-row">
    <a class="zk-btn zk-btn-primary" href="{{ '/observations.html' | relative_url }}">浏览市场观察</a>
    <a class="zk-btn zk-btn-ghost" href="{{ '/about.html' | relative_url }}">关于我们</a>
  </div>
</div>

## 🏴‍☠️ 旗舰深度研究

- **2026-10-03** — [《论 ETH 的价值捕获》v2.0：从协议现金流到网络价值传导]({{ '/research/2026/10/03/eth-value-capture-v2.html' | relative_url }})  
  *八段传导链 + 四层捕获框架 + 五条通道 · 反证登记册与监控看板 · 承重数字全部可复算 · UNKNOWN 保留为研究结论的一部分*
- **2026-10-01** — [Open USD (OUSD) 月度深度分析报告 — 2026年10月号（v7.1）]({{ '/research/2026/10/01/open-usd-ousd-monthly-deep-analysis.html' | relative_url }})  
  *五层证据标注（FACT / ATTRIBUTED FACT / INFERENCE / HYPOTHESIS / FORECAST）· 发行方 API + 链分布 + 交易所 API + 监管文书四路一手复跑 · Tempo 集中度的可证伪假说 · 伙伴证据阶梯 Level 0–6 · GENIUS Act 许可路径与生效日追踪*
- **2026-09-30** — [MSTR vs BMNR：两种 Digital Asset Treasury 模型的资本结构比较]({{ '/research/2026/09/30/mstr-vs-bmnr-digital-asset-treasury.html' | relative_url }})  
  *资本结构 × mNAV × 每股敞口 × Carry × 融资飞轮 · 一手 8-K/10-Q 逐周复算 · 机械 NAV 压力测试（假设股价不变）· 附录含核心数字审计表与可证伪条件*
- **2026-09-20** — [Circle × Coinbase 分销经济学：合同、GENIUS 法案与下一美元 USDC 的归属]({{ '/research/2026/09/20/circle-coinbase-distribution-economics.html' | relative_url }})  
  *四变量框架（规模×收益率×渠道×监管）· Marginal USDC Economics · GENIUS 四层法律拆解 + 六情景 · K2b 监控线 · CRCL Research Dashboard*
- **2026-09-20** — [blob 扩容、Quick Slots、账户抽象、快速最终性：Ethlabs Week 13 四题与我们的答案]({{ '/research/2026/09/20/ethlabs-week13-four-questions.html' | relative_url }})  
  *四问逐条核验 · 链上实测 + EIP 一手文本 + EF 官方文件 · 三处口径校正 + 一次自我更正留痕 · 五条可证伪的推翻条件*
- **2026-10-08** — [CRCL (Circle) v2.7：论点更新与勘误版（**评级复核中**）]({{ '/research/2026/10/08/crcl-circle-v2-7-0.html' | relative_url }})  
  *取代 v2.6.1 · KPI K6/K7 双触发 · 七处原文勘误（含 CPN 收入单位错 10 倍）· 利率叙事重写 · Q3 预登记阈值表公开 · **本版不提供评级与目标价**（估值留待 v2.8）*
- **2026-07-25** — [CRCL (Circle) v2.6.1：从货币基金到金融互联网 — 完整财务模型、市场定价诊断与投资框架]({{ '/research/2026/07/25/crcl-circle-v2-5-1.html' | relative_url }})  
  *⚠️ **已被 v2.7 取代**（BUY 评级与目标价失效）· DCF/SOTP 估值框架 · Investment Mosaic 75.9/100 · 附 Companion Document*
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

<div class="zk-page-nav">
  <a href="{{ '/observations.html' | relative_url }}">市场观察</a>
  <span class="zk-nav-sep">·</span>
  <a href="{{ '/about.html' | relative_url }}">关于我们</a>
</div>