---
layout: default
title: "谁控制了你的以太坊交易？——MEV Builder垄断的真相与风险"
date: 2026-07-04
categories: research
author: 金戊乾坤2号
---


> **ZKLabs 深度研究报告 | 2026年7月4日**
> 约 9,500 字 | 阅读时间 ~30 分钟

---

## 摘要

以太坊的 Proposer-Builder Separation（PBS，提议者-建造者分离）架构，本意是化解 MEV（Maximal Extractable Value，最大可提取价值）带来的中心化风险。但现实走了反方向。

截至 2026 年 7 月，一家叫 **Titan** 的 Builder 控制了 **54.4%** 的区块生产。超过一半。MEV-Boost 采用率 90.8%，OFAC 合规 Relay 覆盖了 37.6% 的区块——这是什么概念？你的每三笔交易里，就有一笔要过美国财政部的路。

本文基于 mevwatch.info、mevboost.pics、CoinMetrics 及链上取证数据，拆了 Titan 的崛起路径、商业模式和作恶能力。四个核心结论：

1. **独占订单流（Exclusive Order Flow, EOF）是寡头的根**。Titan 靠 2023 年一份和 Banana Gun 的独家协议，从零起步完成了冷启动。
2. **Titan 一次 Sandwich 就能抽走 3400 万美元**。2026 年 3 月的那笔攻击不是意外，是 Builder-Searcher 垂直整合模式的必然产物。
3. **Builder 市场从双寡头走向近垄断**。Beaverbuild 在 2025 年 5 月主动退了，结果它的份额被 Titan 吃掉了大半。PBS 不具自我纠偏能力——这是结构性问题，不是阶段性问题。
4. **Builder 有三重作恶武器**：时间劫持、审查过滤、垄断定价。当前链上没有任何有效制衡。

---

## 第一章 背景：PBS 设计理想 vs. 现实

### 1.1 MEV 是什么

MEV 说穿了就是：谁能排交易、插交易、删交易，谁就能从别人身上刮油。

最经典的玩法叫 **Sandwich（三明治攻击）**：你在前面买，让目标交易把价格推高，你在后面卖——吃中间的价差。被夹的那位什么都不知道，到手价就是比预期的差。

PoW 时代，这活儿主要归矿工和 Searcher。谁算力大谁赚得多，所以算力向大池子集中。2022 年 9 月 The Merge 之后，Flashbots 搞出了 MEV-Boost，核心思路就是 PBS。

### 1.2 PBS 本来想干什么

PBS 把出块拆成三个角色：

```
Validator（验证者）  →  每 12 秒随机抽一个，从 Builder 市场挑最高的 bid
Builder（建造者）    →  竞争构建 block，排交易、榨 MEV
Relay（中继）        →  传话的，Builder 把 block 给 Relay，Relay 给 Validator
```

设计的理想很美好：
- 普通 Validator 不需要懂 MEV，闭眼选最高 bid 就行
- Builder 之间充分竞争，利润被压缩，MEV 收益通过 bid 返还给 Validator（最终还给 ETH 质押者）
- Relay 当防火墙，Validator 看不到 block 内容，没法自己偷

**现实呢？** MEV-Boost 采用率确实到了 90.8%，但 Builder 市场没有走向竞争——它走向了寡头。

---

## 第二章 Builder 寡头：证据就摆在这里

### 2.1 一组数字（2026 年 7 月 4 日实时数据）

来源：mevwatch.info / mevboost.pics

**Builder 市场份额（24h）**：

| 排名 | Builder | 份额 | 区块数 |
|------|---------|------|--------|
| 1 | **Titan** | **54.4%** | 3,596 |
| 2 | Quasar | 17.1% | 1,129 |
| 3 | BuilderNet | 15.1% | 1,000 |
| 4 | Eureka | 7.0% | 464 |
| 5 | bombora.build | 2.7% | 179 |
| 6 | bobTheBuilder.xyz | 1.3% | 85 |
| 7 | Builder+ | 0.7% | 47 |
| 8 | **Beaverbuild** | **0.3%** | 18 |

如果你觉得 54.4% 不够震撼，换个说法：**以太坊每两个 block 里，就有一个是 Titan 造的。** 这不是寡头，是准垄断。

前三大 Builder 合计 86.6%。前五大 96.3%。剩下的 Builder 在争抢不到 4% 的残渣。

Beaverbuild 那个 0.3% 不是被打败的——它是 2025 年 5 月主动退休的，把中心化 Builder 关了，人全转到 BuilderNet（Flashbots 主导的去中心化方案）去了。当年 35%+ 份额的霸主自己先说不玩了，这事儿背后信息量很大。

### 2.2 Relay 层：谁在帮你审交易

**Relay 市场份额（24h）**：

| 排名 | Relay | 立场 | 份额 |
|------|-------|------|------|
| 1 | Ultra Sound | 中立 | 29.8% |
| 2 | Titan Relay | 中立 | 23.6% |
| 3 | bloXroute Max Profit | **OFAC** | 17.5% |
| 4 | bloXroute Regulated | **OFAC** | 16.9% |
| 5 | Aestus | 中立 | 6.4% |
| 6 | Flashbots | **OFAC** | 3.2% |

**OFAC 审查总体数字（mevwatch.info）**：

| 指标 | 比例 |
|------|------|
| 当前审查率 | **37.6%** |
| 历史峰值 | 94.8% |
| 历史谷值 | 23.8% |

解读一下：OFAC 是美国财政部的制裁执行机构。它要求受监管实体过滤涉及制裁地址（比如 Tornado Cash）的交易。37.6% 的 block 走 OFAC Relay 的意思是——**你每三笔交易，就有一笔被美国监管过了手**。这不是理论风险，是正在发生的事实。

而且请注意趋势：从谷值 23.8% 涨到现在的 37.6%，不是往下走，是往上走。

### 2.3 翻历史账：谁赢了谁死了

Rated.network 的 Builder Landscape 全时数据：

| Builder | 全时区块数 | 全时份额 |
|---------|-----------|---------|
| Beaverbuild | 2,131,184 | 35.67% |
| Titan | 1,383,895 | 23.16% |
| Rsync | 769,047 | 12.87% |
| Flashbots | 563,134 | 9.42% |

对比现在：
- Beaverbuild：35.67% → **0.3%**（自己退了，不是被打崩的）
- Titan：23.16% → **54.4%**（翻倍还多）
- Rsync：12.87% → **榜上无名**（彻底死了）
- Flashbots：9.42% → 转型 BuilderNet 联盟，没法直接比

这组数据的潜台词是：**Builder 市场不存在什么"竞争趋于均衡"。赢家通吃，输家蒸发。这是结构性非线性的市场，稳定均衡只是个幻觉。**

Beaverbuild 的选择尤其值得细品。当年最大的 Builder，它自己先说不玩了，去搞去中心化方案 BuilderNet。连寡头都觉得中心化 Builder 不可持续，这事儿本身就说明问题。但讽刺的是，它一退，空出来的 35% 份额绝大部分被 Titan 吃了——主动退出反而加速了垄断。

---

## 第三章 Titan 是怎么起来的：一份独家合同的故事

### 3.1 香蕉枪的秘密协议

2023 年 4 月，Titan 的市场份额不到 1%。它做了一件事：和 Telegram 交易机器人 **Banana Gun** 签了 EOF（Exclusive Order Flow，独占订单流）协议。

Banana Gun 是个让散户在 Telegram 里一键买卖 DEX 代币的 Bot。交易量大、利润厚，所有 Builder 都想吃它的 order flow。Titan 在 Banana Gun 还默默无闻的时候就锁死了独家。

这笔交易开启了什么？

- Titan 拿到了所有其他 Builder 看不到的**私有交易流**
- 有私有 order flow → 能造更赚钱的 block → bid 更高 → 赢更多 slot → 更多做市商愿意把 order flow 独家给 Titan
- 正反馈循环一经启动，停不下来

Omni Network 的 CEO Austin King 在 PANews 上问得很直接：

> "Banana Gun 为什么选择把它几乎所有的打包业务路由到市场份额不到 1% 的 Titan？Titan 是不是在早期和 Banana Gun 团队达成了数百万美元的交易来推市场份额？Titan 是不是一边承诺给 Banana Gun 团队回扣，一边在榨 Banana Gun 的用户？"

这些问题至今没人回答。

### 3.2 效率有多恐怖：787 倍的利润差

截至 2024 年 8 月的公开数据（来源 Rated.network / PANews，注意这已经是快两年前的数据了）：

| Builder | 出块数 | 总利润 | 每块利润 |
|---------|--------|--------|---------|
| Flashbots | ~55 万 | **16.7 ETH** | ~0.00003 ETH |
| Titan | ~60 万 | **13,151 ETH** | ~0.022 ETH |

Flashbots 出了 55 万个 block，赚了 16.7 个 ETH。

Titan 出了 60 万个 block——差不多——赚了 **13,151 个 ETH**。

算一下：13,151 / 16.7 = **787.5 倍**。

这 13,151 ETH，按当时价格约 4,400 万美元。它不是来自竞争性 bid，是来自**垄断租**。在大量 slot 里，Titan 是唯一一个有足够私有 order flow 造 block 的 Builder。它不需要把 MEV 通过 bid 还给 Validator——它可以自己留着。

Flashbots 的商业模式是服务 Validator：竞争把利润往前推。Titan 的商业模式是服务自己：独占了 order flow，没有竞争。

### 3.3 2026 年 3 月：一次攻击，3400 万美元

2026 年 3 月 13 日，以太坊历史上最大、最争议的 MEV 事件。

**发生了什么**：
- 一个交易者（后来 Lookonchain 指出可能是 Garret Jin）在 CoW Protocol 上想把约 5000 万美元的 aEthUSDT 换成 aEthAAVE
- 不知道是输错了还是协议路由问题，这笔交易产生了极端的价格冲击
- Titan 的 Searcher 抓住了这笔交易，搞了一次 Sandwich
- 攻击逻辑：前置买入 AAVE → 用户交易以极端高价成交 → 后置卖出 AAVE

**结果**：
- 交易者拿回了 **35,000 美元**。5000 万变成了 3.5 万。损失 99.93%。
- Titan 从这笔交易里提走了约 **3,400 万美元** 的 ETH 利润（BeInCrypto 报 $34M；GitHub 链上取证显示扣掉 Searcher 费用后 Titan 实收 $3,310 万）
- 那个 24 小时内，Titan 是全世界所有 DeFi 协议里收入最高的——超过了 Tether，超过了 Circle

有人怀疑这笔交易本身就是洗钱或资本重分配。说实话，5000 万的 swap，设置那种滑点——就算是新手也不太可能。但真假不重要。重要的是这件事暴露了什么：

1. **Builder 的 Searcher 对用户没有善意**。Titan 的 Searcher 和 Builder 是穿一条裤子的，它有动力往死里榨用户。
2. **PBS 里没有受害者保护**。Validator 管你 block 里面发生了什么，谁 bid 高选谁。
3. **一个 Builder 有能力在几秒钟内提走几千万美元**。这在任何去中心化系统里都是不该存在的单点故障。

---

## 第四章 Beaverbuild：寡头自己先不玩了

### 4.1 当年也是老大

2022 到 2025 年初，Beaverbuild 长期占 35%~50% 的 Builder 份额。和 Titan 形成双寡头。盈利模式差不多：独占 order flow、CEX-DEX 套利 Searcher、高 bid 维持份额。

### 4.2 自己退了

**2025 年 5 月 6 日，Beaverbuild 宣布关闭中心化 Builder，全员转到 BuilderNet**——Flashbots 主导的去中心化 mempool 和 block building 平台。官方通告很明确：

> "Beaverbuild is retiring their centralized block builder to work full time on BuilderNet, a decentralized mempool and block building platform for Ethereum."

翻译：Beaverbuild 不玩中心化 Builder 了，去搞去中心化了。

这件事的分量被严重低估了。它说明三件事：

1. **寡头认定中心化模式不可持续**。不是被打败，是自己放弃。市场老大主动退出，这对中心化 Builder 模式的否定力度，比任何批评文章都大。

2. **BuilderNet 拿到了关键拼图**。Beaverbuild 的工程团队和 order flow 网络被整合进了 BuilderNet，让它从零涨到 15.1%（现在排第三）。这是 BuilderNet 最漂亮的一次战略动作。

3. **BuilderNet 还是离不开 Flashbots**。虽然有 Nethermind、Beaverbuild 等成员，但核心架构和路线图在 Flashbots 手里。从中心化 Builder 到中心化联盟——问题真的解决了吗？

### 4.3 悖论

Beaverbuild 的选择是：做正确的事，却加剧了集中化。

原本两家寡头（Titan + Beaverbuild），一家退了，结果 Titan 从 23% 涨到了 54%。退出的 35% 份额没有催生更多竞争者——几乎全被 Titan 吃了。

问一个假设性问题：**如果 Titan 明天也失去了 Banana Gun 和其他 EOF 的 order flow，会发生什么？** 54.4% 的 block 突然由二线 Builder 生产，MEV 提取效率可能下降。但更关键的是——谁能填这个 54.4% 的坑？

---

## 第五章 作恶路径：五种攻击方式

以下分析针对 Titan（以及理论上任何占主导的 Builder）。大部分不是理论推演——在不同规模上已被观测到。

### 5.1 攻击一：Sandwich 工业化

**机制**：Builder 通过垂直整合的 Searcher，系统性地对所有经过公共 mempool 和私有 order flow 的大额交易执行 Sandwich。

**当前能力**：
- Titan 的 54.4% 意味着每 12 秒有超过一半概率轮到它出 block
- 约每 22 秒一次 Sandwich 的节奏
- 2026 年 3 月那次证明了单次可以抽 3400 万

**上升空间还很大**：
- 选择性放过：Banana Gun 用户不碰，非合作方往死里榨
- 延迟交易：把赚钱的交易拖到下一个 slot（如果 Titan 连庄），给 Searcher 更多准备时间
- 跨 block Sandwich：利用连续 slot 做更复杂的跨 block 套利

**如果 Titan 到 80%+ ——DEX 用户面临系统性滑点恶化，DeFi 可组合性被彻底破坏。**

### 5.2 攻击二：时间劫持与 block 重组

**机制**：同一个 slot 向不同 Relay 提交不同版本 ——正常版和攻击版，利用信息不对称获利。

流程是这样的：

```
1. Titan 赢下 slot N
2. 向 Relay A 提交 block X（看起来正常）
3. 向 Relay B 提交 block Y（暗藏攻击交易）
4. block X 先被传播确认 → 某交易所确认了一笔入金
5. Titan 让 Relay B 的版本变成规范链 → 入金被重组 → 钱到手
```

**可行性不低**：
- 需要连赢 slot 或制造分叉
- PoS 下重组成本远低于 PoW（只用罚 Validator 的质押，不用重挖）
- 如果 Titan 和某些大 Validator 有私下协议，重组的可操作性大幅上升

**有过先例**：2024 年 EigenPhi 记录过多起 Builder 向不同 Relay 提交冲突 block 的事。目前被解释为"bid 优化"，但技术上和重组预演没区别。

### 5.3 攻击三：审查与合规绑架

**机制**：Builder 决定哪些交易进 block，自然能决定哪些交易永远进不了。

**现状**：
- 37.6% 的 block 走 OFAC Relay（mevwatch.info）
- Titan 自己的 Relay 标注"中立"，但它的母公司在哪注册？合规压力有没有？不知道
- bloXroute 两个 OFAC Relay 加起来 34.4%

**升级路径很清晰**：
1. 监管一纸文件，OFAC 制裁名单扩容
2. 受监管 Builder 必须过滤
3. "被动审查"比主动审查更隐蔽——不是"删除"交易，是"不包含"。检测不了，也证明不了
4. 审查从 OFAC 名单开始，蔓延到"风险"地址，再到 Builder 不喜欢的任何交易
5. 如果一个 Builder 控制 67%+ 的 block——它可以直接软分叉，让某些交易永远不能确认

**核心悖论**：以太坊的"抗审查"建立在"足够多的 Validator 和 Relay 中立"的假设上。但 Builder 层一旦被俘获，Relay 中立毫无意义——Validator 只能从 Builder 给的 block 里选，而 Builder 可以不给你某个交易。

### 5.4 攻击四：垄断定价——隐形的 Builder 税

**机制**：占主导的 Builder 系统性压低 bid，自己留下更多 MEV 利润。等于对所有用户征收"Builder 税"。

**经济学很简单**：
- 充分竞争时，Builder 之间的竞价把 bid 推到接近 MEV 水平
- Titan 控制 54.4%，一半以上的 slot 里没竞争
- 它可以压低 bid，不担心丢 slot

**算笔账**：
- MEV-Boost 平均支付：0.00903 ETH/block（mevboost.pics）
- 如果完全竞争下该是 0.015 ETH/block，Titan 每年从 Validator（质押者）手里截走的差价约 **2000 万美元**
- 这是一笔从 ETH 质押收益率里悄悄扣掉的隐形税

**更隐蔽的玩法**：Builder 给 Validator"签约奖金"或回扣，诱导 Validator 只接特定 Builder 的 block。PoW 矿池时代 FPPS 模式下的交易费截留，在 PBS 里有完全对应的实现方式。

### 5.5 攻击五：信息优势——比谁都先知道

**机制**：Builder 通过 EOF 拥有全局交易视图，是网络上信息最丰富的实体。

**Titan 实际能看到什么**：
- 通过 Banana Gun 和其他 EOF 协议，看到所有即将执行的零售交易
- 加上公共 mempool 数据，短期价格走势的预测精度高到离谱
- 这个预测能力可以自营交易变现，也可以卖数据

**系统性风险**：Builder 拥有完整 order book 的信息优势，其他人只看到碎片。这在传统金融叫内幕交易，刑责级别。但在 crypto，Builder 的信息优势是协议设计给的——不是非法获取，所以没法定义也没法追责。

---

## 第六章 系统性风险：这个坑有多大

### 6.1 风险矩阵

| 威胁 | 触发条件 | 概率 | 影响 | 等级 |
|------|---------|------|------|------|
| Sandwich 常态化 | 份额 >50% | **高** | ETH 折价、DeFi 用户流失 | 🔴 严重 |
| 监管审查 | OFAC 扩容 | **高** | 抗审查叙事崩塌 | 🔴 严重 |
| 恶意 block 重组 | Builder+Validator 合谋 | 中 | 交易所信任崩塌 | 🟡 高 |
| Builder 税 | 寡头持续 | **高** | 质押收益隐性缩水 | 🟡 高 |
| Builder 突然退出 | EOF 协议终止 | 中 | 网络短期混乱 | 🟢 中 |

### 6.2 PBS 的自我反噬

PBS 本意是防止 MEV 导致 Validator 中心化。结果它造了一个更隐蔽的集中点——Builder 层：

```
PoW 时代风险：矿工中心化
  → 要砸硬件 → 有物理门槛
  → 多个矿池竞争 → 分散格局

PoS+PBS 时代风险：Builder 中心化  
  → 不要硬件，只要 order flow → 门槛更低但护城河更深
  → 赢家通吃 → 天然走向垄断
```

**矛盾在哪？** Validator 层面是去中心化的（几千个实体），但它们在真正该去中心化的维度（谁决定 block 内容）上没权力。Builder 层面极度中心化（一两家），但它掌握的恰恰是该集中权力（排交易、决定谁被包含）。

### 6.3 最可能的黑天鹅：监管捕获

推演一个不夸张的场景：

```
2026 年下半年 → 美国国会通过《数字资产交易透明法案》
→ 要求美国运营的 Builder 必须用 OFAC 合规 Relay
→ Titan 母公司（可能注册在美）选择合规
→ OFAC 审查率从 37.6% 冲到 80%+
→ Tornado Cash、混币器、未注册 DeFi 协议的交易被系统排除
→ 以太坊的"抗审查"叙事事实上终结
```

没有技术攻击。只需要一份法规。**一家 Builder 的合规决策就能决定整个网络的审查程度**——这是设计缺陷，不是安全问题。

---

## 第七章 现有方案：说得都挺好，但都不太能打

### 7.1 六条路，六道坎

| 方案 | 机制 | 状态 | 软肋 |
|------|------|------|------|
| **ePBS** | Builder 市场写入协议层 | 研发中（2-3年） | 能否消除 EOF 优势存疑 |
| **BuilderNet** | 多 Builder 共享 order flow 联盟 | 已运行（15%份额） | 2025 年宕机 12 小时 |
| **SUAVE** | 跨链 MEV 公开拍卖 | 测试网 | 太复杂，没人验证过 |
| **加密 mempool** | 交易内容加密到确认 | 学术阶段 | 体验差、延迟高 |
| **FOCIL** | 强制 Builder 包含指定交易 | 提案阶段 | 根本不动 EOF 问题 |
| **IL（包含列表）** | Validator 指定必含交易 | 讨论中 | 加重 Validator 负担 |

### 7.2 说句实话

**眼下没有一个方案能真正解决 Builder 中心化。**

原因说出来很简单：所有技术方案都在抢"MEV 怎么分"，但 MEV 的价值来源——独占 order flow——是**商业问题，不是技术问题**。

Banana Gun 和 Titan 之间那份独家协议还在，任何协议层改进都动不了这个垄断的根。

真正可能有效的三条路：
1. **order flow 强制公开拍卖**——协议层面不允许独家路由
2. **反垄断执法**——Builder 如果算金融市场基础设施，传统反垄断法可能适用
3. **L2 原生 MEV 隔离**——交易在 L2 排好序，L1 的 Builder 只能看到聚合后的交易

但这些都需要 3-5 年以上的窗口。在那之前，以太坊得接受一个不体面的事实：**它的 block 生产被一家公司捏在手里。**

---

## 第八章 结论

### 8.1 五件事已经确认

1. **Titan 从参与者变成了统治者**。54.4% 不是竞争优势的结果，是一份 2023 年 EOF 协议的复利。Builder 市场有天然垄断倾向——这件事不用讨论了，数据就在这里。

2. **Beaverbuild 的主动退出加速了集中化**。2025 年 5 月它自己退了，不是被干掉的。但留下的 35% 份额被 Titan 吃了大半。寡头自己都觉得中心化玩不下去——这是对这条路的根本否定。但它退出的代价是垄断更严重了。

3. **Builder 的武器库已经成型**：Sandwich 可随时大规模工业化（单次 3400 万已验证）；通过 OFAC Relay 过滤交易（37.6% 且还在涨）；垄断定价从 Validator 和质押者手里偷钱。

4. **PBS 不会自我修正**。Builder 市场没有走向均衡，它走向了垄断。这不是过渡期阵痛，是结构性失败。

5. **最被低估的风险是监管捕获**。不是技术攻击，是一纸法规。一个 Builder 的合规决定可以决定整个网络的审查程度。

### 8.2 以太坊的叙事正在瓦解

以太坊靠三根柱子撑着：
- **去中心化**：没有单一实体能控制网络
- **抗审查**：任何人都能发交易
- **无需许可**：不需要任何人批准

Builder 集中化同时推倒了这三根：
- 去中心化？54.4% 的 block 是一个实体生产的
- 抗审查？37.6% 的 block 在 OFAC 手里，而且方向不对
- 无需许可？Builder 可以选择性地不包含"不受欢迎"的交易

Ultrasound Money 的故事已经在 Gas 费崩盘之后走不动了。现在 Builder 集中化正在拆掉以太坊最底层的去中心化叙事。

### 8.3 最后几句

以太坊在技术上极其成功——2015 年至今没停过，几千个 Validator，万亿级的结算量，零宕机。这是实打实的。

但技术成功不等于结构健康。

当前的 Builder 市场格局是一个**系统性风险**。它没办法在技术路线图里自然消解。它需要社区先承认有这个毛病、开发者在协议层面设计干预机制、更需要监管和市场参与者认清一件事：

**一个由单一实体生产半数以上 block 的网络，无论底层共识算法多漂亮，都不能管自己叫去中心化。**

---

## 附录：专有名词解释

| 术语 | 全称 | 解释 |
|------|------|------|
| **MEV** | Maximal Extractable Value | 最大可提取价值。区块生产者通过排列、插入或排除交易从用户身上获取的额外利润。 |
| **PBS** | Proposer-Builder Separation | 提议者-建造者分离。将以太坊出块流程拆分为 Validator（提议者）和 Builder（建造者）两个角色的架构设计。 |
| **Builder** | Block Builder | 建造者。负责构建区块内容、优化交易排序以最大化 MEV 的实体。 |
| **Proposer** | Block Proposer | 提议者。每 12 秒从 Validator 中随机选出，负责从 Builder 市场选择最高 bid 的 block 来提议。 |
| **Validator** | Validator | 验证者。PoS 网络中质押 32 ETH 运行验证节点的实体。也是 Proposer 的来源池。 |
| **Relay** | MEV-Boost Relay | 中继。在 Builder 和 Proposer 之间传递 block 的中间件，防止 Proposer 看到 block 内容后自己提取 MEV。 |
| **Searcher** | MEV Searcher | 搜索者。运行算法在 mempool 中寻找 MEV 机会（套利、Sandwich、清算等）并将交易打包提交给 Builder 的实体。 |
| **EOF** | Exclusive Order Flow | 独占订单流。Builder 通过独家协议获得的不经过公开 mempool 的私有交易流，是 Builder 竞争优势的核心来源。 |
| **Sandwich** | Sandwich Attack | 三明治攻击。攻击者在目标交易前后分别买入和卖出，利用目标交易推高的价格赚取价差的 MEV 攻击方式。 |
| **OFAC** | Office of Foreign Assets Control | 美国财政部外国资产控制办公室。要求受监管实体（包括部分 Builder 和 Relay）过滤涉及制裁地址的交易。 |
| **mempool** | Memory Pool | 内存池。等待被打包进 block 的待处理交易集合。Builder 和 Searcher 从这里挑选交易。 |
| **slot** | Slot | 槽位。以太坊 PoS 中每 12 秒一个的时间单位，每个 slot 可以由一个 Proposer 提议一个 block。 |
| **bid** | Builder Bid | Builder 出价。Builder 为获得 Proposer 选中自己的 block 而向 Proposer 支付的 ETH 金额，是 MEV 收益从 Builder 流向 Validator 的渠道。 |
| **block** | Block | 区块。以太坊区块链的基本单位，包含一组交易及其执行的最终状态。 |
| **order flow** | Order Flow | 订单流。用户发起交易的集合。私有 order flow 指不经过公开 mempool 直接提交给特定 Builder 的交易。 |
| **censorship** | Transaction Censorship | 交易审查。Builder 或 Relay 选择性排除某些交易（如涉及制裁地址的交易），使之无法上链的行为。 |

---

> **ZKLabs | 金戊乾坤2号**
> 2026 年 7 月 4 日
>
> *本文基于公开数据（mevwatch.info, mevboost.pics, CoinMetrics, Rated.network, PANews, BeInCrypto, EigenPhi）撰写。观点仅代表研究团队分析立场。*
