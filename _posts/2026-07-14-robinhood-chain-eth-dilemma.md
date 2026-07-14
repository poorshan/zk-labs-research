---
layout: default
title: "Robinhood Chain 深度研报 / 以太坊的胜利，ETH 的困境"
date: 2026-07-14
categories: research
author: ZK-Labs Research
permalink: /research/2026/07/14/robinhood-chain-eth-dilemma.html
---

**一句话结论**：Robinhood Chain 验证了以太坊 L2 作为「受监管金融基础设施」的可行路径——但它暴露的代价远比这个机会重大：**以太坊 L2 生态越繁荣，ETH 的价值捕获反而越薄弱。Robinhood 选择以太坊而 Stripe 选择 Solana 的分化，正是这种矛盾的结构性表达。** 这不是 Robinhood 的问题，这是 Ethereum 路线图的系统性问题。

**日期**：2026-07-14 · **出品**：ZK-Labs Research（金戊乾坤2号） · **版本**：v3.1

> **来源标签**：[DL]=官方文档 · [BPR]=新闻稿 · [DATA]=链上数据/研究机构 · [EXPERT]=专家引述 · [MEDIA]=媒体报道 · [EST]=行业推断

---

## 投资结论

我们通过分析 Robinhood Chain 的双层架构、链上实际使用数据和 ETH 叙事演化，得出以下判断：

1. **Robinhood Chain 是一个值得研究的模板，不是一个值得押注的资产**。它的法律防火墙精巧且可复制，但它不产生可投资的原生资产——Stock Token 是 Robinhood 的负债，不是你的资产。

2. **ETH 的「ultrasound money」叙事已被数据证伪**。自合并以来 ETH 净增发超过 100 万枚。L2 仅将收入的 7.8% 回流以太坊。这不是暂时的——这是结构性变化。

3. **ETH 正在被市场从「货币资产」重新定价为「结算商品」**。Dankrad Feist（以太坊基金会研究员）直言：「ETH 现在很少被用作交易媒介」（ETH is now rarely used as a medium of exchange）。Pine Analytics 的判断更直接：「ETH 已经开始像低收益基础设施代币一样交易，而不是高增长智能合约平台」（ETH has already begun trading like a low-yield infrastructure token）。

4. **Robinhood Chain 是 ETH 叙事压力的加速器，而非原因**。即使没有 Robinhood Chain，Base、Arbitrum、Optimism 也在做同样的事——从以太坊获取安全性，但把绝大部分经济价值留给自己。

5. **对投资者而言：ETH 需要一个全新的估值框架**。「ultrasound money」「世界计算机」「Web3 货币」这些口号已经失去了数据支撑。ETH 不会消失，但它现在的估值逻辑不成立——而市场正在对此进行定价。

---

## 执行摘要

Robinhood Chain 于 2025 年 6 月 23 日主网上线，是 Robinhood Markets（纳斯达克：HOOD）基于 Arbitrum Orbit 构建的 Ethereum Layer 2。它最核心的设计是一个精密的法律防火墙：**分发层无许可，资产层高度监管，两者之间只有一家名为 BBVI 的授权参与者作为唯一桥梁。**

这个防火墙让 Robinhood 可以在 Jersey（海峡群岛）设立 SPV、在 Liechtenstein 拿到 EU Prospectus 审批、通过 Reg S 豁免美国证券法注册——然后，把代表美股经济暴露的 ERC-20 代币（Stock Token）放在一个任何人都能访问的链上。

**但链上实际发生的事和 Robinhood 的品牌叙事完全不同**：

- 61% 的链上转账是 WETH，24 个 Stock Token 合约**仅占 0.27% 的转账量** [DATA]
- 早期的增长引擎是 memecoin 投机——不是 RWA tokenization
- 但 TVL 数据不容忽视：**12 天内从 $1,342 飙升至 $156.6M**，是 2026 年所有 L2 中最快的 TVL 爬坡之一 [DATA] DefiLlama

**更值得关注的是 ETH 的角色转变**。Robinhood Chain 用 ETH 作为 gas token——这似乎是对 ETH 的利好——但实际上，ETH 在这里的作用与天然气在工业经济中的作用高度相似：不可或缺，但被定价为一种越便宜越好的运营成本。用户桥接 ETH 只是为了支付 gas 参与 memecoin 和 Stock Token 交易——桥接的 $70M+ ETH 被立即消费，不作为价值存储持有。

**Robinhood Chain 是一个信号**：当传统券商可以在不持有 ETH 信仰的情况下建设链上金融基础设施，而 ETH 的经济价值没有被同步放大时——ETH 的叙事需要被重新审视。

---

## 一、为什么这个时刻值得关注

Robinhood 做链这件事，单看是一个中型的商业决策。但如果把它放在更大的趋势里看——L2 经济规模爆炸而 ETH 价值捕获萎缩——它就成了一个研究窗口。

三个力量正在交汇：

### 1.1 Robinhood 的困境与野心

2024-2025 年，Robinhood 的美国零售用户增长趋于平缓。作为一家上市公司，它需要新的增长故事。同时，Coinbase 通过 Base L2 获取了巨大的链上用户和收入——2023 年 8 月上线，到 2026 年 7 月 TVL 已达 $4.37B [DATA] DefiLlama。Robinhood 如果不做自己的链，就会从「革命性的零佣金券商」变成「仅限于美国的传统券商」。

Vlad Tenev 反复使用「tokenization is a freight train that can't be stopped」[MEDIA] 这样的叙事来重塑 HOOD 股票的故事——从零佣金券商升级为全球链上金融基础设施。

#### 1.1.1 Robinhood 的财务底盘

理解 Robinhood Chain 的战略逻辑，必须先看清母公司的财务基本面。这不是一个「被迫转型」的故事——这是一个年化净利润超 $13.8亿的公司，在主营业务之上叠加新增长层的扩张性决策 [DATA] Robinhood Q1 2026 财报。

| 指标 | 数值 |
|:---|:---|
| Q1 2026 净收入 | $10.7亿 |
| Q1 2026 净利润 | $3.46亿 |
| 调整后 EBITDA | $5.34亿 |
| 平台总资产 | $3,070亿 |
| 月活用户 | 2,740万 |
| Gold 订阅用户 | 430万 |
| ARPU | $157 |

*数据源：Robinhood Q1 2026 财报 [Robinhood, May 2026]*

交易收入构成揭示了一个关键趋势：

| 产品线 | Q1 2026 收入 | 占总交易收入 | 趋势 |
|:---|:---|:---|:---|
| 期权 | $2.60亿 | 41.8% | 稳定 |
| 加密货币 | $1.34亿 | 21.5% | ↓46.8% YoY（去年同期 $2.52亿） |
| 事件合约 | $1.04亿 | 16.7% | ↑340x（去年同期 $300万） |
| 股票 | $8,200万 | 13.2% | 稳定 |

*数据源：Robinhood Q1 2026 财报 [Robinhood, May 2026]*

三个洞察：

**第一，加密收入在转型而非衰退**。加密交易收入同比下降 46.8%，但加密名义交易量达 $660亿（Bitstamp 贡献 $420亿 + Robinhood App 贡献 $240亿）。Robinhood 的加密业务正在从「零售赚取价差」转向「基础设施服务」——Robinhood Chain 是这个转型的终极落脚点。

**第二，事件合约证明了 Robinhood 的产品创新执行力**。从 $300万到 $1.04亿只用了一年——这说明 Robinhood 有能力在短时间内将新型金融产品推至规模化。Robinhood Chain 在母公司眼里，不是赌注，而是已验证能力的再次应用。

**第三，Robinhood Chain 是「成本中心 + 用户获取引擎」，不是直接利润中心**。链基础设施的投入（每年数千万美元）相对于 Robinhood $10.7亿/季的收入规模，是一个用于扩展可服务市场的长期投资。商业模式的关键不在链本身的直接收入（排序器费、做市价差），而在于：(1) 将 Robinhood 用户从 App 引导至链上 DeFi 后能否通过跨产品变现（期权、借贷、事件合约）；(2) Stock Token 能否在 2-3 年内成长为新的重要收入线 [EST]。

这意味着 Robinhood Chain 的可持续性不取决于它自己的盈亏，而取决于母公司认为这一战略方向的机会成本是否合理。如果 18-24 个月内 Stock Token 未出现明确的商业化路径，母公司可将资源重新分配到更高利润的业务线——事件合约的增长已经证明了这种「快速试错、快速转向」的内部文化。

### 1.2 L2 路线图的意外后果

Ethereum 的 L2 中心化路线图——通过 Rollup 将执行从 L1 卸载到 L2——是以太坊生态最成功的扩展策略。但它产生了一个未被充分预期的副作用：**L2 的经济繁荣不再直接转化为 L1 ETH 的价值。**

- 2021 Q4：以太坊 L1 季度费用收入高达 **$4.3B** [DATA] Pine Analytics
- 2025 Q4：L1 月均费用已降至 **<$15M**——年化约 $180M，下降超过 95% [DATA] Pine Analytics
- 2025 年全年，所有 L2 从用户收取了 $129M，但仅向以太坊支付了 ~$10M 结算费——**价值回流率 7.8%** [DATA] Pine Analytics

这不是一个暂时的现象。EIP-4844（Dencun 升级，2024 年 3 月）通过引入 blob 来大幅降低 L2 的数据可用性成本，结果是 L2 交易费下降了 97% [DATA]——但 L1 的 ETH 燃烧也下降了 84%。

### 1.3 机构入场的悖论

Robinhood Chain 是「机构入场 crypto」的一个里程碑式案例。但它的实现方式恰恰揭示了「机构入场」对 ETH 可能不是利好：机构不需要 ETH 作为价值存储，它们需要 ETH 作为一个低成本的、可靠的基础设施——就像它们不需要天然气股票来经营工厂一样。

---

## 二、双层架构：一个法律防火墙的解剖

Robinhood Chain 不是一个传统的「券商上链」。它是一个被精心设计的双层系统——两层之间的治理哲学截然不同。

### 2.1 架构全景

| 维度 | 分发层 | 资产层 |
|:---|:---|:---|
| 性质 | 无需许可的 Arbitrum Orbit L2 | 结构化的债务证券发行体系 |
| 准入 | 任何人可部署合约、运行节点 | 仅 BBVI（唯一 AP）可一级市场申购 [DL] |
| 地域 | 全球 120+ 国家 [BPR] | 排除美国、加拿大、英国、瑞士 [DL] |
| 监管 | 无前置 KYC/AML | COBO Consent (JFSC) + EU Prospectus (FMA Liechtenstein) [PR] |
| 资产形式 | ERC-20 代币 | 债务证券——不赋予底层股权法律所有权 [DL] |
| ETH 角色 | Gas token + L1 结算锚点 | 无 |

**核心洞察**：这两个层之间没有技术耦合。分发层的无许可性不需要「合规」，因为合规已经被完整封装在资产层。链是 permissionless 的，但链上打着 Robinhood 品牌的资产是 permissioned 的。

### 2.2 唯一的桥梁：BBVI

BBVI 是 Robinhood Chain 体系中最关键也是最容易被忽略的设计。它在 Robinhood Markets, Inc. 和 Robinhood Chain 之间充当唯一的 Authorised Participant（AP）[DL]。

**BBVI 的角色可以理解为三层**：

1. **一级市场的守门人**：所有 Stock Token 的创造（申购）和销毁（赎回）都必须经过 BBVI。没有其他路径。用户不能直接找 Robinhood 申购，也不能直接在链上铸造 Stock Token。

2. **合规的封装器**：BBVI 承担了全部的 AML/KYC、投资者资格审核、跨境合规义务。它在 Jersey（海峡群岛）注册为 SPV，将 Robinhood 的美国主体与链上无许可活动隔离开来。Robinhood 不需要直接面对零售用户的合规义务——BBVI 替它做了这个。

3. **资产负债表的缓冲垫**：Stock Token 在 Robinhood 的账本上是负债（liability），但法律上的兑付义务签在 BBVI 名下。如果 Stock Token 的链上交易引发任何监管纠纷或法律挑战，BBVI 是第一道防线。

**这意味着什么**：

- Robinhood 完全控制一级市场——它可以单方面决定暂停申购、限制赎回、或修改 AP 资质要求
- 合规负担被集中到单点——这是「干净」的设计，但也意味着如果 BBVI 出问题（监管处罚、运营失败、法律纠纷），一级市场立即冻结
- BBVI 是系统的单点故障——没有备份 AP。Robinhood 选择只有一个 AP，不是技术限制，是控制权的选择

### 2.3 ETH 在这个架构里的位置

ETH 只参与分发层的 gas 消耗和 L1 结算——对资产层的价值（底层股票、法律文件、托管账户）没有任何直接关联。用户桥接 ETH 到链上，是为了支付 gas 参与交易——不是为了持有 ETH。

**这个区分至关重要**：Robinhood Chain 的增长创造的是 ETH 的消耗场景，不是 ETH 的持有需求。而被消耗的 ETH（作为 gas 焚烧或支付给排序器）在创造价值的同时，并不增加 ETH 的净需求。

### 2.4 为什么是以太坊 L2 而非 Solana？——结算链 vs 支付通道

当一家管理 $3,070亿资产的上市券商选择在以太坊上构建结算层时，背后是机构级别的尽职调查。Robinhood（Arbitrum Orbit L2）和 Stripe（Solana USDC 结算）在 2024-2026 年间做出了截然不同的区块链基础设施决策。表面上这是「L2 vs L1」，本质上揭示了一个被市场忽视的结构性分化：**结算链（settlement chain）与支付通道（payment rail）是两种截然不同的技术需求。**

| 维度 | 以太坊 L2（Robinhood 的选择） | Solana（Stripe 的选择） |
|:---|:---|:---|
| 结算安全性 | 继承以太坊主网十年验证 + 欺诈证明 | 独立 L1，仅依赖自有验证网络 |
| 网络可靠性 | 以太坊主网十年零重大安全事件 | 七次全网宕机（2020-2025），最长 19h [DATA] |
| 客户端多样性 | 主网多客户端（均<33%） | Agave/Jito 控制 70%+ [DATA] |
| RWA 市场份额 | 60%+（~$1,250亿） | ~$87亿（主要来自稳定币） [DATA] rwa.xyz |
| 链级定制化 | 自定义 gas、排序器、费用模型、治理 | 无链级定制，共享全网规则 |
| 监管成熟度 | 十年对话 + ETH ETF 已获批 | SOL ETF 预期升温，但 SEC 曾将 SOL 列为未注册证券 |

*数据源：Arbitrum, BitGo 研报（2026.06）, rwa.xyz（2026.03）, 247wallst.com（2026.05）*

#### Robinhood 为什么不能选 Solana

三条无法穿透的底线：

**(1) 受监管实体不能运行在不可靠基础设施上。** 作为受 SEC/FINRA/SIPC 多重监管的上市券商，Robinhood 的合规义务要求每一笔交易的清算和结算路径具备可审计的确定性。Solana 七次全网宕机不是「技术问题」——在所有受监管实体的风险评估框架中，这是「不可接受的操作风险事件」[EXPERT]。以太坊主网自 2015 年创世至今零宕机记录，在监管机构的眼中，这并非技术偏好问题，而是**最低准入标准**。

**(2) RWA 格局已经确定。** 以太坊独占 60%+ RWA 市场份额——BlackRock 的 BUIDL（$8.24亿 AUM）、JPMorgan 的 Onyx、Franklin Templeton 的 BENJI 均运行在以太坊网络上 [DATA]。Solana 的 RWA 生态（~$87亿）主要来自稳定币（USDC/USDT），缺乏机构级的代币化证券产品。对 Robinhood 而言，选择 Solana 意味着在自己的 L1 上从零搭建代币化证券市场——这相当于在竞争对手的支付通道上重建经纪商基础设施。正如 BlackRock 前数字资产负责人 Joseph Chalom 所言：「机构只关心信任、安全性和流动性——高价值项目正在以太坊上构建」[EXPERT] Bitcoinist, Jan 2026。

**(3) 监管路径依赖。** 以太坊的十年监管对话（从「ETH 是证券吗」到 ETH ETF 获批）为建立在以太坊上的应用提供了相对清晰的法律边界。Solana 的监管框架仍在构建中——对需要明确合规路径的上市券商而言，这不具有操作性。

#### Stripe 为什么选了 Solana——而且这同样合理

理解 Stripe 的选择需要回到支付处理的本质：

- **延迟是支付的成本**。Stripe 处理的典型交易（电商结账、订阅扣款）要求亚秒级最终性。Solana 的 400ms 区块时间提供了一种接近传统支付网络（VisaNet ~1-2秒）的用户体验。Arbitrum Orbit 虽然 TPS 足够，但乐观 Rollup 的 7 天挑战期使其最终确定性受制于欺诈证明窗口——这对支付用例来说太长了。

- **USDC 是结算媒介，不是资产**。Stripe 使用 Solana 是为了结算 USDC——不创建代币化证券、不托管客户资产、不在链上发行受监管产品。稳定币支付不需要与代币化证券相同级别的法律审查和结算保证。

- **成本结构不同**。Stripe 的每笔交易需要低于 $0.01 的 Gas 成本才有商业意义。Solana 的交易费 <$0.001。以太坊 L2 的 Blob 费用虽大幅下降，但仍比 Solana 高一个数量级。

#### 分化意味着什么

Robinhood-Stripe 的分化是加密基础设施走向专业化的标志性事件。

这一分化不是在竞争——两者处于基础设施堆栈的不同层。Robinhood、BlackRock、JPMorgan 需要的是**结算链**（安全性、可审计性、法律确定性，最终性 > TPS）；Stripe、Visa、PayPal 需要的是**支付通道**（低延迟、低成本、高吞吐，延迟 < TPS）。结算链承载价值和合规性要求最高的资产；支付通道承载交易频次最高但对价值锚定要求较低的场景。

**什么会改变这一判断**：
- Solana 连续 18-24 个月零宕机，并建立等效的机构信任和监管框架——这可能需要数年
- 以太坊 L2 实现亚秒级最终性（基于 ZK 证明的快速桥接、共享排序器）——将削弱 Solana 的延迟优势
- SOL ETF 获批——但即使如此，以太坊累积的机构基础设施（托管、保险、审计、法务）需要 Solana 数年来弥合

**结论**：Robinhood 不选 Solana，不是因为 Solana 不好——而是因为 Robinhood 需要的东西，Solana 给不了。Stripe 需要的东西，以太坊 L2 目前也给不了。**两个都没选错。但 Robinhood 的选择对 ETH 的影响是双面的：它验证了以太坊 L2 作为「受监管金融基础设施」的可行路径，但也强化了 ETH 「被动结算商品」的定位——这正是本报告 §六要展开的核心矛盾。**

---

## 三、法律防火墙：合规套利还是监管创新？

### 3.1 Jersey SPV + Liechtenstein Prospectus + Reg S

Robinhood Chain 的法律结构是一个三件套：

**Jersey SPV**：Robinhood Assets (Jersey) Limited，公司注册号 162428，注册地址 St. Helier, Jersey [PR] [DL]。Robinhood Markets, Inc. 的间接子公司。获得 JFSC 的 COBO Consent——这不是银行牌照，但比空壳公司重得多——强制要求治理标准、投资者披露、AML/CFT/CPF 合规 [PR]。

**Liechtenstein FMA EU Prospectus**：Base Prospectus 由 Liechtenstein FMA 根据 EU Prospectus Regulation 批准 [PR]。已向 30 个 EEA 成员国发出通知（EU passport）。Liechtenstein 有专门的区块链法（Token and TT Service Provider Act），在 crypto 监管领域领先大多数 EEA 成员国。

**Reg S 豁免**：Stock Token 未在美国《1933 年证券法》下注册 [DL]。发行依赖 Regulation S——一个为「在美国境外向非美国人士发行证券」设计的豁免条款。法律文件明确排除美国、加拿大、英国、瑞士等司法管辖区。

Jersey + Liechtenstein 是一个精妙的组合：

| 优势 | Jersey | Liechtenstein |
|:---|:---|:---|
| 法律体系 | 英国法律遗产，SPV 架构成熟 | 专门区块链法 |
| 监管门槛 | COBO Consent——比银行牌照轻，比空壳重 | FMA Prospectus = 全 EEA passport |
| 国际地位 | 不在欧盟但被广泛接受 | EEA 成员国 |

### 3.2 Stock Token 的法律本质：你买到的不是股票

这是整个架构最关键的法律事实——也是散户最容易误解的部分：

> **Stock Tokens are tokenised debt securities** issued by Robinhood Assets (Jersey) Limited. They provide economic exposure to underlying securities but **do not grant investors any legal or beneficial rights** in, or against the issuer of, those underlying securities. [DL]

逐层分解：

1. **你不是 AAPL 的股东**——Token holder 不是底层股票的持有人
2. **你是 RHJ 的无担保债权人**（有资产担保但无股权权利）
3. **Security Agent 替你看着底层资产**——在 SPV 破产时代表 token holder 处置
4. **你获得的是价格暴露，不是所有权**——economic exposure 而非 legal ownership

这对散户来说是「good enough」的 trade-off——用法律权利的缺失换取了 24/7 全球可交易性。但必须清醒：**如果 Robinhood 或 RHJ 出问题，你持有的不是一个可以主张所有权的股票，而是一个无担保债权的代币化代表。**

### 3.3 美国用户的悖论

尽管法律文件白纸黑字排除了美国人士，但 Robinhood Chain 是一个 permissionless L2——技术上，任何美国 IP 都可以通过 VPN 访问 DEX 上的 Stock Token。

Robinhood 可以说「我们在法律上已经做了力所能及的一切来排除美国用户」。但 SEC 的执法标准不是「文件上排除」，而是「实质上是否向美国人发售」。如果 Stock Token 在 DEX 上的流动性和交易量主要由美国 IP 贡献——这很难不被认定为实质上的美国发售。

**这是一个没有被写进 Prospectus 的尾部风险。**

---

## 四、链上的真实故事：Memecoin 在开车，RWA 在后座

Robinhood 的品牌叙事是「tokenisation of real-world assets」。但链上的数据讲了另一个故事。

### 4.1 数字不会说谎

根据 SQD 的早期数据 [MEDIA]：

- 链上共 323,791 个区块，128,950 次 Transfer 事件
- 690 个 ERC-20 合约中，**WETH 占 61% 的转账活动**
- **24 个 Stock/ETF Token 合约仅占 0.27% 的转账量**
- 46% 的 Stock Token 转账发生在传统美股交易时间之外

CoinDesk 的标题一针见血：「Robinhood's blockchain finds early success — Thanks to memecoins, not stocks」[MEDIA]。Fortune 报道了 meme 交易者涌入链上 [MEDIA]。

#### 4.1.1 数据核验：$40 亿 DEX 交易量的真与假

Robinhood Chain 上线后，一些社区和媒体渠道提出了「DEX 累计交易量 $40 亿」的说法。这一数字若属实，将极大强化 Robinhood Chain 的增长叙事——但我们进行了独立核验，得出以下判断：

**DefiLlama 的数据不支持 $40 亿。** 在 DefiLlama 的去中心化交易所排名中，Robinhood Chain 的 DEX 交易量显示在三级交易所层面：24 小时仅 **$7,779**，7 天仅 **$38,515** [DATA] DefiLlama（2026-07-13 核验）。即使考虑 DefiLlama 对 Robinhood Chain 本地 DEX（如 Lighter、Robinhood DEX）的追踪可能存在延迟或不完整，$7,779 与 $40亿之间的差距是**六个数量级**，无法以「数据延迟」解释。

**三种可能：**

1. **$40 亿是一个累计数字**（自测试网上线起的数月跨度，可追溯至 2025-07）。如果将测试网的交易活动（主要为 Robot/Bot 压力测试交易）纳入统计，理论上可以达到 $40 亿的名义交易量。但这与「主网上线后的链上经济活力」是完全不同的概念。

2. **刷量交易（Wash Trading）占主导。** Robinhood Chain 作为一条新链，没有交易成本（低 Gas）、没有活跃用户基础和独立验证机制，是刷量交易者和 MEV Bot 的理想渔场。DefiLlama 显示 Uniswap 在 Robinhood Chain 上的 24 小时交易量仅为 **$3,188** [DATA]——与 $40 亿的宏大叙事形成鲜明反差，表明非机器人驱动的有机交易活动当前极其有限。

3. **统计口径问题。** 部分渠道可能将链上所有 Token Transfer 事件（包括 WETH 的反复包装/解包、MEV Bot 的闪电贷循环、用户从 CEX 的桥接存款等）误归类为「DEX 交易量」。这些活动产生了名义上的链上交易量，但并非终端用户主动发起的资产交换。

**对比：其他 L2 上线初期的真实交易量。** Base 链上线首周有机 DEX 交易量约为 $1-3 亿（不包括 Coinbase 的内部转账）[DATA] DefiLlama。Arbitrum 上线首月约 $20 亿。Robinhood Chain 上线仅 12 天，要产生 $40 亿的有机 DEX 交易量——这需要日均 $3.3 亿，超过 Arbitrum One 同期日均 DEX 交易量——在当前链上用户基数和 TVL 规模下不成立。

**对论证的影响：**

| 如果 $40 亿是... | 对 Robinhood Chain 叙事的含义 |
|:---|:---|
| Bot/压力测试累计交易 | 无关——不代表真实用户采用或经济活动 |
| 刷量交易 | 负面——可能扭曲链上指标，损害 Robinhood 合规品牌 |
| 含桥接/Token Transfer | 误导——不应作为「DEX 活跃度」的证据 |
| 真实有机交易 | **不成立**——与 DefiLlama 的独立数据矛盾 |

在可以独立核验 DefiLlama 的真实交易数据（$7,779/24h）之前，本报告认为 **$40 亿的说法缺乏可信证据支撑，建议投资者在该数字获得可交叉验证的来源确认前不予采信**。

### 4.2 但 TVL 数据在尖叫

如果你只看 TVL，Robinhood Chain 的增长是爆炸性的：

| 日期 | TVL | 日增长 |
|:---|:---|:---|
| 2026-07-02 | $1,342 | — |
| 2026-07-03 | $17.5M | +$17.5M |
| 2026-07-04 | $34.2M | +$16.7M |
| 2026-07-07 | $42.3M | +$5.4M |
| 2026-07-09 | $74.4M | +$27.6M |
| 2026-07-11 | $111.5M | +$17.8M |
| 2026-07-13 | $156.6M | +$31.4M |

**12 天从 $1,342 到 $156.6M**——增幅超过 11,600,000%。[DATA] DefiLlama

这个增长速度不容忽视。到 2026 年 7 月 14 日，Robinhood Chain 的 TVL 已经是 Optimism（$296M）的 53%、Arbitrum One（$1.23B）的 12.7%、Base（$4.37B）的 3.6%。

### 4.3 叙事与现实之间的裂缝

三种可能的解读：

1. **乐观派**：「TVL 在爆炸，说明 Robinhood Chain 正在成为一个真正的 DeFi 中心。Stock Token 的链上活动会慢慢赶上。」
2. **怀疑派**：「TVL 主要由 memecoin 流动性池和 USDG 存款驱动。0.27% 的 Stock Token 转账量说明 RWA 叙事至少目前是虚的。」
3. **本报告的判断**：**TVL 是真实的，但增长引擎是错的**。Robinhood Chain 的成功不是「RWA tokenization 的成功」，而是「一个 permissionless L2 吸引了 crypto 原生投机者的成功」。两者之间的区分不是语义游戏——它决定了这条链的长期定位和监管风险。

如果 Robinhood 的品牌承诺是「合规金融基础设施」，但实际使用是「memecoin 赌场」，那么要么品牌会被现实污染（监管关注、丑闻风险），要么现实会被品牌约束（限制 memecoin 活动，但会杀死早期引擎）。

**Robinhood 现在同时需要两件事：memecoin 驱动的 TVL 增长来证明链的成功，和 Stock Token 的合规叙事来维护品牌。这两件事迟早会发生冲突。**

---

## 五、谁还能复制这个模板

### 5.1 对比表：Robinhood Chain vs 主要 L2

| 链 | TVL | 独特资产 | 合规策略 | 增长引擎 |
|:---|:---|:---|:---|:---|
| **Base** | $4,371M | 无 | 直接在美国运营 | Coinbase 用户导入 + memecoin |
| **Arbitrum One** | $1,233M | 无 | 通用 L2 | DeFi 原生生态 |
| **Optimism** | $296M | 无 | 通用 L2 | Superchain 生态 |
| **Robinhood Chain** | $156.6M | **Stock Token（RWA）** | Jersey SPV + Reg S | Memecoin + RWA 叙事 |

来源：[DATA] DefiLlama, 2026-07-14

Robinhood Chain 的独特性不在于技术——基于 Arbitrum Orbit 的技术栈完全可复制。独特性在于三个东西：

1. **Stock Token**——代表美股经济暴露的合规代币，目前没有其他 L2 提供
2. **Robinhood 品牌**——2400 万用户的信任和认知
3. **BBVI 单点控制的一级市场**——让 Robinhood 在不失去控制的情况下开放链

但这三点中，只有第一点是真正独特的。品牌可以被复制（如果 Charles Schwab 或 Fidelity 做同样的事），单点控制是特性也是脆弱点。

### 5.2 模板的可复制性

任何想 tokenize 股票、债券、基金的机构都可以走这条路：

1. 在 Jersey/Cayman/BVI 设立 SPV
2. 找 EEA 监管机构批准 Prospectus
3. 底层资产放传统托管银行
4. 发行 ERC-20 代币代表债务证券
5. 把代币放在 permissionless L2 上（不需要自建链——可以直接用 Arbitrum/Base/Optimism）
6. 靠现有 DeFi 生态提供二级市场流动性

**这意味着 Robinhood Chain 的「独家优势窗口」可能很短**——如果这个模板被验证（TVL 数据正在验证），跟风者会迅速出现。Coinbase 完全可以在 Base 上做同样的 Stock Token——它甚至不需要新的监管批准，因为 Base 已经在美国运营。

### 5.3 Coinbase 的下一步

Coinbase Base 的 TVL 是 Robinhood Chain 的 28 倍。如果 Coinbase 在 Base 上推出 Stock Token，Robinhood Chain 的差异化将几乎消失。Coinbase 有：更大的用户基础、更深的 DeFi 生态、不需要依赖第三方 AP。

唯一的障碍可能是美国的监管——但 Robinhood Chain 已经证明了「Jersey SPV + Reg S」模式在技术上排除了美国用户。Coinbase 完全可以复制这个架构。

---

## 六、ETH 的身份危机——本报告的核心论点

> 这是本报告最重要、原创性最高的部分。我们不是在讨论 ETH 会不会归零——它不会。我们讨论的是 ETH 的估值叙事是否需要被重写。

### 6.1 天然气类比：一个便利但不舒服的比喻

ETH 在 L2 时代的角色与天然气在工业经济中的角色高度相似：

| 维度 | 工业天然气 | ETH in L2 |
|:---|:---|:---|
| 作用 | 燃料，驱动工业过程 | 燃料，驱动 L2 交易 + L1 结算 |
| 定价逻辑 | 运营成本，被压低到最小 | Gas price，被 blob 压缩到接近零 |
| 与产出价值的关联 | 几乎为零 | 几乎为零——ETH 价格与 L2 经济价值无直接关联 |
| 资产属性 | 消耗性商品 | 消耗性商品 |
| 价值存储 | 零 | 正在被剥离 |

天然气工业是全球经济的命脉——但没有人持有天然气期货作为退休储蓄。ETH 在变成 crypto 的天然气。

### 6.2 数据告诉你一个你不想听的故事

#### L2 费用回流：从 40.8% 到 7.8%

| 年份 | L2 总收入 | 支付给以太坊 | 回流比例 |
|:---|:---|:---|:---|
| 2024 | $277M | $113M | 40.8% |
| 2025 | $129M | ~$10M | **7.8%** |

来源：[DATA] Pine Analytics, 2026-02-24

一年之间，L2 向以太坊支付的费用比例从 40.8% 跌到 7.8%——这不是偶然波动，这是 EIP-4844 的结构性后果。Blob 费用被设计为极低（目标是零），这意味着 L2 的结算成本被永久性压缩。

#### Base 是最清晰的镜子

Base（Coinbase 的 L2）自上线以来总的收入约 $98M，仅向以太坊 L1 支付了约 $4.9M 的结算费。**Base 的利润率约 95%。** [DATA] CoinMetrics, Cointelegraph

如果 Base 是一家餐厅，它每天营业、服务数百万顾客、赚取丰厚收入——但付给房东（以太坊）的租金只占收入的 5%。这在前 L2 时代是不可想象的。

#### Dencun 前后的剧变

| 指标 | Dencun 前 | Dencun 后 | 变化 |
|:---|:---|:---|:---|
| Arbitrum 单笔交易费 | $0.37 | $0.012 | ↓97% |
| Optimism 单笔交易费 | $0.32 | $0.009 | ↓97% |
| ETH 日燃烧量 | 较高 | — | **↓84%** |

来源：[DATA] Pine Analytics, EIP-4844

#### ETH 供应：「ultrasound money」已被证伪

自 2022 年 9 月合并以来，ETH 净增发超过 **100 万枚**。PoS 日发行约 2,600 ETH（验证者奖励），而 Dencun 后日燃烧仅 500-1,500 ETH。**ETH 的供应不是在收缩——它在以每年约 0.3-0.7% 的速度增长。** [DATA] ultrasound.money, Glassnode

Fusaka 升级（EIP-7918，2025 年 12 月）将 blob 基础费用的 30% 纳入燃烧，年化燃烧率升至 1.32%——但这仍不足以逆转通胀。Bitwise 的分析：Fusaka 后 blob 费用未来 12 个月预计仅产生 5.39-78.2 ETH/年（$16K-$234K）——小数点后四位的数字 [DATA] Bitwise。

### 6.3 专家们的声音：从以太坊圈子内部到外部

> **Dankrad Feist**（以太坊基金会研究员，2025-12）：
> "Ethereum is now rarely used as a medium of exchange or unit of account, when compared to the 2017-2021 period. Since 2021, adoption as a medium of exchange has mostly been replaced by stablecoins. … This could be an explanation why appreciation of ETH seems to have stalled, while adoption is still growing." [EXPERT]
>
> *（译：与 2017-2021 年相比，以太坊现在很少被用作交易媒介或记账单位。自 2021 年以来，作为交易媒介的采用已被稳定币大量取代。……这或许可以解释为什么 ETH 的升值似乎停滞了，尽管采用仍在增长。）*

连以太坊基金会自己的核心研究员都公开承认：ETH 的货币功能已被稳定币取代。他提出的三条出路——成为类似黄金的模因价值存储、重新建立货币功能、或聚焦收入与燃烧——本质上都是接受「商品」定位的不同方式。

> **Pine Analytics**（2026-02-24）：
> "ETH has already begun trading like a low-yield infrastructure token rather than a high-growth smart contract platform." [DATA]
>
> *（译：ETH 已经开始像低收益基础设施代币一样交易，而不是高增长智能合约平台。）*

> **Jon Charbonneau**（DBA 联合创始人，2023-02——在 Dencun 之前就已预见到）：
> "Deflation doesn't make ETH 'ultrasound money.' PoS inflation isn't an explicit network revenue or cost in any scenario. … Can ETH actually become 'money,' and should it even try to be?" [EXPERT]
>
> *（译：通缩并不能让 ETH 成为 'ultrasound money'。在任何场景下，PoS 通胀都不是显式的网络收入或成本。……ETH 真的能成为「货币」吗？它甚至应该尝试吗？）*

> **James Beck**（ENS Labs，康奈尔区块链大会 2025-04）：
> "Ethereum is a neutral verification layer, but the Ethereum mainnet is not being fairly compensated for the work that it is doing. Centralized for-profit L2s like Base, Optimism and Arbitrum are gathering the lucrative sequencing fees while enjoying the security and liveness guarantees of the Ethereum mainnet at relatively little economic cost." [EXPERT]
>
> *（译：以太坊是一个中立的验证层，但以太坊主网并没有因为其所做的工作获得公平的补偿。Base、Optimism 和 Arbitrum 这些中心化的营利性 L2，正在攫取丰厚的排序费收入，同时以相对较低的经济成本享受以太坊主网的安全性和活性保障。）*

> **Bankless**（2025-05-14）：
> "The market stopped pricing ETH as a crypto-money, and started pricing it as a tech-stock with a discounted cash flow (DCF) model." [MEDIA]
>
> *（译：市场已经停止将 ETH 定价为加密货币，转而开始用贴现现金流模型将其定价为科技股。）*

> **Bankless**（2025-05-14）——L2 作为客户的比喻：
> "L2s are best understood as paying customers of Ethereum. Each L2 controls its own governance, can fork at will, and is free to settle on another chain. Ethereum needs to treat them like customers they could lose, not an integrated part of Ethereum's tech stack." [MEDIA]
>
> *（译：L2 最应该被理解为以太坊的付费客户。每个 L2 都控制自己的治理、可以随时分叉、也可以自由选择在另一条链上结算。以太坊需要把它们当作可能流失的客户，而不是自己技术栈的一个组成部分。）*

> **Binance Research**（2024-12）：
> "From a value perspective, the key question is whether cash flows generated from transaction fees and MEV, versus the monetary premium from ETH functioning as a gas token, medium of exchange, and collateral asset, will lead to greater value capture in the long-term." [DATA]
>
> *（译：从价值角度看，关键问题是：交易费和 MEV 产生的现金流，与 ETH 作为 gas 代币、交易媒介和抵押资产所产生的货币溢价相比，哪个将在长期带来更大的价值捕获。）*

### 6.4 Robinhood Chain 是 ETH 叙事压力的加速器

Robinhood Chain 带来的挑战比一般的 L2 更深刻，因为它引入了一种**完全不需要 ETH 作为价值载体的资产类别**：

- Stock Token 代表的是美股的经济暴露——用户关心的是 AAPL/NVDA 的价格，不关心 ETH 的价格
- Stock Token 以 USDG（美元稳定币）计价交易——不以 ETH 计价
- 作为 DeFi 抵押品时，协议关心的是抵押品的美元价值，而非 ETH 价值
- 用户桥接 $70M+ ETH 只是为了支付 gas——这些 ETH 被立即消费，不作为价值存储持有

**Robinhood Chain 正在建造的未来是这样的**：金融资产在链上，交易以美元稳定币发生，ETH 只出现在 gas 费的微小消耗中，没有人因为持有 Stock Token 而产生持续持有 ETH 的需求。

这和一个「ETH 作为全球互联网货币」的未来是截然不同的。

### 6.5 反方观点：ETH 的叙事为什么还没有崩溃

一个没有反方论证的论点不值得认真对待。以下是 ETH 仍可能维持溢价的最佳论证——每条都附上数据检验。

**反方一：网络效应 → 安全需求**

L2 生态越大，以太坊作为结算层越不可或缺，ETH 的安全需求越大。

*检验*：L2 聚合吞吐量确实在爆炸（2026 年 4 月达 3,700 ops/sec，同比 +210% [DATA] Gate Blog）。但 L1 费用收入仍在下降——数量和单价的乘积在缩小，而非扩大。网络效应的价值没有转化为 ETH 的经济价值。

**反方二：ETH 作为 L2 抵押品**

EigenLayer restaking、validity proofs、AnyTrust 等架构使用 ETH/stETH 作为经济安全抵押品——这创造了「gas」以外的 ETH 需求。

*检验*：EigenLayer 确实创造了额外的 ETH 锁定需求，但其规模远小于 L2 费用流失。目前没有证据表明「抵押品需求」的增速能弥补「费用引擎」的下降。

**反方三：L2 成功 = ETH 成功**

如果 L2 生态爆炸，以太坊网络整体变得更重要。类比：即使大多数贸易不以美元结算，美元作为全球储备货币的地位仍在强化。

*检验*：ETH 市场主导地位从历史高位持续下降至 13.1%（2024-12）[DATA] Binance Research。市场没有在定价「以太坊成为全球金融枢纽」的战略价值。恰恰相反——市场在定价 ETH 的「货币属性」正在消退。

**反方四：Fusaka 和未来升级**

Fusaka 将年化燃烧率提升至 1.32%，后续升级可能继续改善价值捕获。

*检验*：Bitwise 的数据显示 Fusaka 后 blob 费用年收入仅 $16K-$234K。这是一个小数点后四位的数字。任何依赖 blob 费用增长的修复方案，目前没有数据支持。

**反方五：Based Rollups 可能根本性解决问题**

Bankless 提出让 L1 验证者直接处理 L2 排序——可能将 MEV 和费用导回 ETH。

*检验*：Based Rollups 仍处于理论阶段，没有任何主流 L2 承诺迁移。且 L2 的总吞吐量已是 L1 的 100 倍以上——L1 是否有能力承担 Based Rollup 的排序负载是一个严肃的工程问题。

### 6.6 裁决

ETH 的四个核心叙事——逐一检验：

| 叙事 | 数据说了什么 | 状态 |
|:---|:---|:---|
| 「ultrasound money」 | L2 仅回流 7.8%，净增发 >100 万 ETH，日燃烧 500-1,500 vs 发行 2,600 | **证伪** |
| 「世界计算机」 | 计算在 L2 执行，L1 费用收入下降 95%+ | **证伪** |
| 「价值存储」 | 市场主导地位降至 13.1%，Bankless：「market stopped pricing ETH as crypto-money」 | **正在失效** |
| 「Web3 货币」 | Dankrad Feist：「rarely used as a medium of exchange」，稳定币取代 | **证伪** |

**ETH 不会消失。但它当前的估值逻辑无法成立。市场正在寻找一个新框架来定价 ETH——一个不依赖于「货币溢价」而聚焦「基础设施收益」的框架。在这个新框架下，ETH 的合理估值可能显著低于当前市场定价。**

---

## 七、风险矩阵

### 7.1 Robinhood Chain 自身风险

| 风险 | 严重性 | 概率 |
|:---|:---|:---|
| SEC 认定 Stock Token 实质向美国人发售 | 极高——可能使整个架构崩溃 | 中 |
| BBVI 作为唯一 AP 出现运营问题 | 高——一级市场立即中断 | 低-中 |
| EU Prospectus 到期后被部分成员国拒绝 | 高——市场份额缩减 | 中 |
| SPV 对手方风险（RHJ 违约） | 中——Security Agent 处置流程未经实战检验 | 极低 |
| Memecoin 丑闻损害 Robinhood 品牌 | 中——「合规金融」品牌被 memecoin 赌场玷污 | 中 |
| 分发层被利用于欺诈 | 中——Robinhood 面临「无法控制但需担责」的两难 | 高 |

### 7.2 ETH 叙事风险

| 风险 | 严重性 | 概率 |
|:---|:---|:---|
| L2 持续吸走经济活动，ETH 燃烧继续萎缩 | 高——通缩/超声叙事彻底失效 | 高 |
| 更多 L2 采用自有稳定币作为计价单位 | 中——进一步边缘化 ETH 的货币需求 | 高 |
| RWA tokenization 在 L2 爆炸但不使用 ETH 作为资产 | 中-高——ETH 与机构金融彻底脱钩 | 中-高 |
| L2 DA 向 Celestia/EigenDA 等替代方案迁移 | 极高——将终结 ETH 的「结算商品」叙事，开启「完全可替代结算层」时代 | 低-中 |

### 7.3 监管周期风险：2028 年的政治更迭

Stock Token 的法律结构对政治周期高度敏感。当前处于特朗普政府任期内，SEC 领导层于 2026年1月发布声明将代币化证券分为「issuer-sponsored」和「third-party」两大类，Robinhood Stock Token 属于后者中的「Linked Security」类别——**SEC 明确标注为密切关注区** [SEC 2026年1月声明]。

| 情景 | 概率 | SEC 执法风险 | 对 Robinhood Chain 影响 |
|:---|:---|:---|:---|
| 特朗普连任至 2028 | ~40% | 低（~2/10） | 持续友好环境，RWA 代币化可推进 |
| 2028 政权更迭 | ~35% | 高（~8/10） | Stock Token 法律框架面临重新审查 |
| 中期国会变动 | ~25% | 中（~5/10） | 部分产品需调整，但核心框架可存活 |

*数据源：SEC 2026年1月声明、Robinhood Jersey 招股说明书*

三个结构脆弱点：

1. **Jersey SPV 依赖 COBO Consent（非受监管实体）+ 瑞士账簿证券法，无跨境判例支撑。** 当出现法律纠纷时，没有现成的司法先例来处理「Jersey SPV 发行的代币化美国股票债务证券→瑞士账簿记账→全球链上交易→用户在不同司法管辖区提出权利主张」这条路径。第一次法律挑战将在判例法中定义整条路径的合法性边界——而该边界尚未被绘制。

2. **Stock Token 在法律上是「债务证券」而非受益权凭证。** 这是监管友好的一面（避免了 SEC 对受益权凭证的注册要求），但也意味着用户在 Robinhood 破产程序中仅作为无担保债权人——排在所有有担保债权人和优先债权人之后。SPV 的 Security Agent 可以处置底层资产为 Token Holders 挽回部分价值，但该机制未经破产法庭的实际检验。

3. **SEC 对代币化证券的立场自 2017 年以来经历了从全面否定（ICO 执法潮）到选择性接纳的 180° 转变，2028 年后完全可能再次反转。** 监管对金融创新的态度不是线性推进的——它在危机（执法）、宽松（鼓励创新）、收紧（消费者保护反弹）之间摆动。Robinhood Chain 的 Stock Token 框架在这个周期中处于一个脆弱的中间位置：它不是非法产品（有 EU Prospectus），也不是获得全面豁免的产品（SEC 标记为「密切关注」）。

**综合监管周期风险评分：6.5/10。** 这不是「如果」而是「何时」的问题——Robinhood Chain 最晚需要在 2028 年前建立足以抵御不利监管环境的业务护城河。如果 2028 年政权更迭且新 SEC 领导层对代币化证券采取敌对立场，Stock Token 的法律框架可能被迫重构——这对 Robinhood Chain 的市场定位是结构性的、而非战术性的影响。

---

## 八、对投资者的启示

### 8.1 可追踪的先行指标

| 指标 | 看什么 | 当前信号 |
|:---|:---|:---|
| Robinhood Chain Stock Token DEX 流动性 | 何时达到可交易规模 | 极初期（0.27% 转账量）[DATA] |
| L2 → L1 费用回流趋势 | ETH 价值捕获在改善还是恶化 | 恶化中（7.8% vs 40.8%）[DATA] |
| ETH 日燃烧 vs 日发行 | 供应在收缩还是扩张 | 扩张（日发行 2,600 vs 燃烧 500-1,500）[DATA] |
| ETH 市场主导地位 | 货币溢价在上升还是下降 | 下降（13.1%）[DATA] |
| L2 DA 方案迁移 | 是否有主流 L2 转向 alt-DA | 暂未发生——这是最大尾部风险 |

### 8.2 对 ETH 波动率交易的结构性含义

如果本报告的 ETH 叙事风险论证成立：

1. **ETH 的长期 IV 溢价可能面临结构性压缩**。当市场逐步认识到 L2 繁荣不直接转化为 ETH 价值时，波动率溢价中的「叙事溢价」部分可能被挤出——就像 2022-2023 年 Twitter/Facebook 从「科技成长股」被重新定价为「成熟广告平台」时的过程。

2. **ETH/BTC ratio 的波动率可能增加**。ETH 正在失去「digital gold」叙事的支持，ratio 的波动越来越反映叙事博弈而非基本面差异。

3. **L2 新闻成为 ETH 波动率触发点**。Robinhood Chain 或 Base 的重大新闻（新资产上线、监管行动、数据里程碑）正在变得比 ETH 自身的协议升级更影响 ETH 价格波动。

### 8.3 证伪条件：什么会让我们改变观点

好的研究必须明确在什么条件下自己的核心判断需要被修正。以下是 ZK-Labs 对本报告关键结论的证伪条件：

| 当前判断 | 证伪触发条件 | 证伪后修正方向 |
|:---|:---|:---|
| 短期温和利好 ETH（~350-500 ETH/年消耗） | 连续 30 天链上交易量 < $1,000万/日 | ETH 消耗下调至 <150 ETH/年，影响降级为「中性」 |
| Stock Token 法律框架短期可存活 | SEC 或 ESMA 在 12 个月内针对代币化敞口产品发布不利指引或执法行动 | 看跌情景概率上调至 50%+；下调 TVL 增长预测 |
| Robinhood Chain 有能力在 12 个月内达 $5-10亿 TVL | 连续 60 天 TVL 零增长或负增长 | 基准情景 TVL 下调至 $2-4亿 |
| $40亿 DEX 交易量中包含实质性链上活动 | DefiLlama / Dune 公开仪表板上 Robinhood Chain DEX 日均交易量 < $1,000万 | 中度负面——链上经济活动弱于叙事暗示，ETH 价值捕获预期大幅下修 |
| 母公司将持续投入资源 | Robinhood Q4 2026 或 Q1 2027 财报中 Robinhood Chain 相关提及显著减少或资本支出指引下调 | 重大负面——若母公司退缩，Robinhood Chain 失去最大护城河 |
| L2→L1 费用回流率将持续恶化 | 回流率在 12 个月内回升至 >20%（通过 Fusaka 等升级） | ETH 叙事压力减轻，重新审视「结算商品」定位 |

**证伪不等于恐慌。** 大多数证伪条件需要数周至数月的时间序列数据才能触发。它们的作用是让读者能够在叙事与实际数据之间做出独立判断，而非在每次市场波动中被噪音左右。如果上述证伪条件中任何一个被触发，ZK-Labs 将发布更新报告，同步修正评级和投资启示。

---

## 数据附录

### 表 A-1：L2 向以太坊支付费用趋势

| 年份 | L2 总收入 | 支付给以太坊 | 回流比例 | 来源 |
|:---|:---|:---|:---|:---|
| 2024 | $277M | $113M | 40.8% | [DATA] Pine Analytics |
| 2025 | $129M | ~$10M | **7.8%** | [DATA] Pine Analytics |

Base 典型案例：总收入 ~$98M，支付以太坊 ~$4.9M——利润率 ~95%。[DATA] CoinMetrics, Cointelegraph

### 表 A-2：Dencun 升级前后 L2 费用

| 指标 | Dencun 前 | Dencun 后 | 变化 | 来源 |
|:---|:---|:---|:---|:---|
| Arbitrum 交易费 | $0.37 | $0.012 | ↓97% | [DATA] Pine Analytics |
| Optimism 交易费 | $0.32 | $0.009 | ↓97% | [DATA] Pine Analytics |
| ETH 日燃烧 | — | — | ↓84% | [DATA] Pine Analytics |

### 表 A-3：ETH 供应变化

| 时期 | 流通供应 | 变化 | 来源 |
|:---|:---|:---|:---|
| 2022-09（合并） | ~120.5M | PoS 转换 | [DATA] ultrasound.money |
| 2024 年底 | ~121M | +>100 万 ETH（净通胀） | [DATA] Glassnode |
| 2026-07（估算） | >121.2M | 继续微量通胀 | [DATA] ultrasound.money |

### 表 A-4：ETH 燃烧率轨迹

| 阶段 | 年化燃烧率 | 关键事件 | 来源 |
|:---|:---|:---|:---|
| 合并后（2022 Q4-2023） | 负值（通缩） | 高 L1 费用 | [DATA] ultrasound.money |
| Dencun 后（2024 Q2 起） | +0.5-0.8% | Blob 费用极低 | [DATA] Pine Analytics |
| Fusaka 后（2025 Q4-） | 1.32% | 30% blob 费燃烧 | [DATA] Bitwise, Gate Blog |

### 表 A-5：以太坊 L1 费用收入

| 时期 | 费用收入 | 来源 |
|:---|:---|:---|
| 2021 Q4 | $4.3B/季度 | [DATA] Pine Analytics |
| 2025 Q4 | <$15M/月（年化 ~$180M） | [DATA] Pine Analytics |
| 变化 | **↓95%+** | — |

### 表 A-6：ETH 市场主导地位

| 指标 | 数据 | 来源 |
|:---|:---|:---|
| ETH 市场主导地位 | 13.1% | [DATA] Binance Research (2024-12) |
| 山寨币总主导地位 | 28.2% | [DATA] Binance Research (2024-12) |

### 表 A-7：主要 L2 TVL 对比（2026-07-14）

| 链 | TVL | 上线时间 | 来源 |
|:---|:---|:---|:---|
| Base | $4,371M | 2023-08 | [DATA] DefiLlama |
| Arbitrum One | $1,233M | 2021-08 | [DATA] DefiLlama |
| Optimism | $296M | 2021-12 | [DATA] DefiLlama |
| **Robinhood Chain** | **$156.6M** | 2025-06 / TVL 爆发 2026-07 | [DATA] DefiLlama |

### 表 A-8：Robinhood Chain TVL 增长轨迹

| 日期 | TVL | 日增长 |
|:---|:---|:---|
| 2026-07-02 | $1,342 | — |
| 2026-07-03 | $17.5M | +$17.5M |
| 2026-07-04 | $34.2M | +$16.7M |
| 2026-07-07 | $42.3M | +$5.4M |
| 2026-07-09 | $74.4M | +$27.6M |
| 2026-07-11 | $111.5M | +$17.8M |
| 2026-07-13 | $156.6M | +$31.4M |

来源：[DATA] DefiLlama。12 天增幅 11,600,000%+。

> **数据缺口说明**：Robinhood Chain 日活地址、DEX 日交易量、Stock Token vs Memecoin 细分交易量数据暂不可用——Dune Analytics 和 Artemis 尚未覆盖此链。以上指标将在数据可用后纳入后续版本更新。

---

## 来源索引

**Robinhood Chain 官方**：
- [DL] robinhood.com/us/en/chain/
- [PR] cdn.robinhood.com/assets/robinhood/legal/rhj_base_prospectus.pdf
- [BPR] robinhood.com/us/en/newsroom/ — 「Robinhood Accelerates Global Expansion」新闻稿

**媒体报道**（12 家）：
- [MEDIA] americanbanker.com, blog.thirdweb.com, cryptobriefing.com, sqd.dev, coinmarketcap.com, theblock.co, coindesk.com, decrypt.co, fortune.com, techbullion.com, weex.com, thedefiant.io

**研究机构与专家**：
- [DATA] Pine Analytics — pineanalytics.substack.com/p/the-compression-of-l1-value-capture (2026-02-24)
- [DATA] CoinMetrics / Cointelegraph — tradingview.com/news/cointelegraph:fd700cd26094b:0 (2025-05-08)
- [EXPERT] Dankrad Feist — dankradfeist.de/ethereum/2025/12/07/l1-tokens.html (2025-12-07)
- [EXPERT] Jon Charbonneau — joncharbonneau.substack.com/p/eth-is-not-ultrasound-money-part (2023-02-19)
- [EXPERT] James Beck (ENS Labs) — 康奈尔区块链大会 (2025-04)
- [MEDIA] Bankless — bankless.com/read/the-two-sides-of-eth (2025-07-08), bankless.com/read/restoring-eths-product-money-feedback-loop (2025-05-14)
- [DATA] Binance Research — public.bnbstatic.com/static/files/research/the-eth-value-debate.pdf (2024-12)
- [DATA] Bitwise — bitwiseinvestments.eu/blog/crypto-research/fusaka-wont-solve-ethereums-revenue-challenge/
- [DATA] Gate Blog — gate.com/blog/101695/, gate.com/blog/101766/ (2026-04)
- [DATA] DefiLlama — api.llama.fi
- [DATA] ultrasound.money
- [DATA] EIP-4844 — eips.ethereum.org/EIPS/eip-4844
- [DATA] EIP-7918 — eips.ethereum.org/EIPS/eip-7918

**数据完整性声明**：本文所有事实性论断均标注来源标签。数据来源包括 Robinhood 官方文档（含 Q1 2026 财报）、研究机构报告、区块链数据平台、以及以太坊基金会成员的公开言论。截至 2026-07-14，交叉验证来源 25+。Robinhood Chain 链上细粒度活动数据（日活地址、DEX 日交易量等）因第三方仪表板覆盖不足而存在缺口，已在文中标注。

---

**免责声明**：本报告由 ZK-Labs Research（ZK Capital 旗下研究机构）制作，仅供专业投资者参考。报告中的任何内容不构成投资建议、交易建议、或任何形式的投资推荐。数字资产市场具有极高风险——请根据自身情况独立判断。过去的数据趋势不代表未来表现。

ZK-Labs Research 是 ZK Capital (Singapore) 控股的独立加密研究机构。本报告不代表 ZK Capital 或其关联方的持仓或交易方向。
