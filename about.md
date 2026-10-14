---
layout: default
title: 关于 ZK-Labs Research
permalink: /about.html
banner_image: /assets/images/about-banner.webp
banner_pill: 关于我们
description: 独立加密研究，始于波动率，不止于波动率。
---

<section class="zk-stats" aria-label="站点数据">
  <div class="zk-stat"><span class="zk-stat-n">{{ site.posts | size }}</span><span class="zk-stat-l">深度报告</span></div>
  <div class="zk-stat"><span class="zk-stat-n">{{ site.posts | where: 'flagship', true | size }}</span><span class="zk-stat-l">旗舰研究</span></div>
  <div class="zk-stat"><span class="zk-stat-n">{{ site.categories.observation | size }}</span><span class="zk-stat-l">市场观察</span></div>
  <div class="zk-stat"><span class="zk-stat-n">5级</span><span class="zk-stat-l">证据标签体系</span></div>
  <div class="zk-stat"><span class="zk-stat-l" style="font-size:1rem;color:var(--zk-text)">持续更新</span></div>
</section>

<div class="about-wrap">

<section class="about-sec">
  <div class="sec-head"><span class="sec-no">01</span><h2>我们是谁</h2></div>
  <p>ZK-Labs Research 是 <strong>ZK Capital</strong>（Singapore）旗下的独立加密研究机构。</p>
  <div class="pull">我们不卖数据，不接付费推广，不替任何项目方站台。每一篇报告的唯一客户，是我们自己的交易决策——以及未来选择信任我们判断的合作伙伴。</div>
  <p>在信息过载的加密世界里，我们专注于一个被大多数人忽视的维度：<strong>波动率</strong>。我们认为，理解波动率定价错误的深度，比预测价格方向更能持续创造 alpha。</p>
</section>

<section class="about-sec">
  <div class="sec-head"><span class="sec-no">02</span><h2>研究方法 · 四条铁律</h2></div>
  <div class="rules">
    <div class="rule"><span class="rule-no">01</span><div><h3>无来源，不落笔</h3><p>所有数据论断必须标注可验证来源（DeFiLlama、CoinGecko、Deribit、Glassnode 等），不依赖记忆或二手转述。</p></div></div>
    <div class="rule"><span class="rule-no">02</span><div><h3>时间戳不可篡改</h3><p>每一篇研报通过 GitHub commit 发布，commit hash 就是审计线索。不删不改，错了公开勘误。</p></div></div>
    <div class="rule"><span class="rule-no">03</span><div><h3>数据实时验证</h3><p>关键数字在撰写时通过 API 实时抓取，不引用过期快照。</p></div></div>
    <div class="rule"><span class="rule-no">04</span><div><h3>批判性独立</h3><p>不因为持仓而美化，不因为踏空而贬低。观点可能有错，立场不能有偏。</p></div></div>
  </div>
</section>

<section class="about-sec">
  <div class="sec-head"><span class="sec-no">03</span><h2>研究领域</h2></div>
  <div class="domains">
    <div class="domain"><h3>加密期权</h3><p>ETH/BTC 波动率曲面、期限结构、偏度异常、策略回测</p></div>
    <div class="domain"><h3>波动率宏观</h3><p>VIX 择时、跨资产波动率传导、波动率风险溢价</p></div>
    <div class="domain"><h3>协议基本面</h3><p>稳定币、L1/L2、MEV、流动性质押等赛道的深度分析</p></div>
    <div class="domain"><h3>量化交易系统</h3><p>期权策略引擎、波动率定价模型、风控框架</p></div>
  </div>
</section>

<section class="about-sec">
  <div class="sec-head"><span class="sec-no">04</span><h2>团队</h2></div>
  <p>ZK-Labs Research 由 <strong>金戊乾坤2号 / 金戊乾坤3号</strong> 投研团队运营。</p>
  <p>我们采用「人机协作」模式：量化系统负责数据采集、异常检测和策略信号生成，人工负责方向性判断、主题研究和最终决策。团队的核心竞争力不在算力，而在<strong>将波动率判断和仓位纪律编码为可执行系统的能力</strong>。</p>
</section>

<section class="about-sec">
  <div class="track">
    <span class="kicker">05 · TRACK RECORD</span>
    <blockquote>我们不要求你相信我们的判断——<br>我们要求你验证我们的记录。</blockquote>
    <p>ZK-Labs Research 的每一篇研报都是一个不可篡改的公开记录。</p>
    <p>所有历史报告在 <a href="https://github.com/poorshan/zk-labs-research">GitHub 仓库</a> 中完整保留，每篇报告的发布时间由 git commit 时间戳锁定。一年后、三年后，你仍然可以回溯验证：当时我们看到了什么，我们判断对了什么，我们错过了什么。</p>
    <p style="margin-bottom:0">这是 ZK Capital 最重要的资产。对未来的合作伙伴而言，这比任何回测曲线都更有说服力。</p>
  </div>
</section>

<section class="about-sec">
  <div class="sec-head"><span class="sec-no">06</span><h2>联系</h2></div>
  <p>ZK-Labs Research 是 ZK Capital（Singapore）的研究部门。</p>
  <div class="contacts">
    <a class="contact" href="https://www.zklabsresearch.com"><span class="ic">🌐</span><span><b>官方网站</b><span>www.zklabsresearch.com</span></span></a>
    <a class="contact" href="https://github.com/poorshan/zk-labs-research"><span class="ic">💻</span><span><b>GitHub 仓库</b><span>github.com/poorshan/zk-labs-research</span></span></a>
  </div>
</section>

<p class="outro">ZK-Labs Research — 独立加密研究，始于波动率，不止于波动率。</p>

</div>
