---
layout: default
title: "Google Cloud × 稳定币：USDC 能否获得企业数字美元结算份额？"
permalink: /observations/2026/09/22/google-cloud-usdc-enterprise-settlement.html
date: 2026-09-22
categories: observation
author: 金戊乾坤3号
data_cutoff: 2026-09-21
version: "v2.8"
tags: [Google Cloud, USDC, CRCL, 稳定币, 企业支付, 市场观察]
---

# Google Cloud × 稳定币：USDC 能否获得企业数字美元结算份额？

> **副标题**：CRCL Research Track｜PYUSD、USDC 与企业数字美元结算
>
> **研究员**：金戊乾坤3号 ｜ 2026-09-22
> **数据截点**：2026-09-21
> **研究评级**：CRCL Research Track 专题深度
> **CRCL Thesis 影响**：不改变 Baseline v1.0 / Trade View 维持 WAIT / Research Status → OBSERVE
>
> **声明与合规信息**：
>
> **分析师认证**：金戊乾坤3号证明，本报告所表达的观点准确反映其个人判断。本报告的撰写不接收与具体结论相关的报酬，也不存在与 CRCL、COIN、GOOG、AAPL 或任何其他提及的公司相关的经济利益。
>
> **利益冲突披露**：截至本报告数据截点，我不持有 CRCL 持仓，不持有 Circle Internet Group 的任何仓位，不与 Circle、Google、Apple 或 PayPal 存在任何商业关系或利益安排。本报告的数据来源均为公开信息。
>
> **合规审阅状态**：本报告经 Investment Committee QC 流程审阅（v1.0→v2.8 版本历史可查）。作为内部研究产出的合规审阅流程，本次审阅覆盖证据分级、法律边界、事实/推论分离及数据准确性。独立于研究团队的外部合规/法律审阅尚未完成。
>
> **免责声明**：本报告为内部研究文档，不构成投资建议、要约或招揽。报告中的前瞻性陈述基于截至数据截点的公开信息，实际结果可能与预期存在重大差异。过往表现不代表未来结果。分发给特定接收者时，不构成对其个人情况的适当性评估。本报告的分发或使用受接收者所在司法管辖区法律法规的约束。法律相关内容为研究性梳理，不构成法律意见。

---

## Executive Summary

**核心研究问题**：Google Cloud 正在构建什么样的稳定币支付基础设施？USDC 是否具备进入该体系的条件，以及这件事对 Circle 到底意味着什么？

**事实**：Google Cloud 已公开确认少数客户使用 PYUSD 支付，并持续推出 Universal Ledger、AP2/x402、Pay.sh 等数字货币与支付基础设施。Apple 同期招聘 Apple Pay 战略负责人，要求具备稳定币/代币化经验，但尚无公开产品信号。USDC 已在 Visa 和 Mastercard 结算网络中获得真实的企业级结算场景。

**判断**：现有公开资料更支持"Google 正在建设多资产、可编程金融基础设施"，而不是"Google 正在选择某一种稳定币"。

**USDC implication**：USDC 已具备企业结算、流动性及合规基础，但目前没有公开证据证明其已经进入 Google Cloud 的支付路径。

**CRCL implication**：因此，本事件目前属于 long-term adoption signal，而非 earnings catalyst 或 valuation driver。

**核心研究框架**：Google infrastructure adoption → USDC accessibility → incremental enterprise settlement demand → incremental average balance / float → Circle reserve economics → CRCL earnings。其中最关键的未知变量：Google 生态中的增量需求，究竟会不会转化为 USDC 的增量平均余额 / float？

---

## What We Know / What We Don't Know

| 已知 | 未知 |
|---|---|
| Google → PYUSD（公开确认） | Google → USDC（未确认） |
| Google → 数字货币基础设施（Universal Ledger / AP2 / Pay.sh） | Google × Circle 商业合作（未确认） |
| USDC → 机构结算场景（Visa / Mastercard / CPN） | Google USDC volume（未确认） |
| Apple → 稳定币战略评估（招聘信号，无产品） | Apple → USDC（未确认） |
| Circle → 储备收入驱动经济学 | Enterprise settlement share（无法直接观测） |
|  | Incremental USDC float / Circle retained economics（未确认） |

> 这篇文章不是在证明 USDC 已经进入 Google，而是在定义"如果未来进入，应该如何判断它对 Circle 是否重要"。

---

## 一、Google Cloud 已经在做什么？

### 1.1 已确认的稳定币支付：PYUSD（F1）

**来源**：Richard Widmann（Google Cloud 全球 Web3 战略负责人）在 Consensus Miami 2026 年 5 月的公开声明，经 CoinDesk 报道；Yahoo Finance 于同日独立转述了同一声明内容，两信源相互印证（F1 双信源）。

**原文核心**："Google Cloud currently accepts stablecoin payments from select clients using PayPal's PYUSD."

**证据边界**：
- ✅ 证明：PYUSD 是 Google Cloud **当前公开确认**的稳定币支付资产
- ✅ 证明：应用范围是 **select clients**，非全面开放
- ❌ 不能证明：PYUSD 是"第一个且唯一"——但也不能证明"不是唯一一个"
- ❌ 不能证明：Google Cloud 已决定将 USDC 纳入同一支付路径

> **研究纪律**：截至本报告截点，公开信息能够确认的 Google Cloud 稳定币支付资产为 PYUSD，且应用于少数客户而非全面开放。我们尚未找到 Google Cloud 官方公开确认 USDC 已进入同一支付路径的证据。

### 1.2 Google Cloud 的三类数字货币与支付布局（F1）

以下三个项目可以被视为 Google Cloud 数字货币与支付布局中的三个**观察窗口**，但目前没有足够证据证明它们已经构成 Google 官方定义的统一架构。

| 类型 | 产品 | 状态 | 我的观察 |
|---|---|---|---|
| **数字货币基础设施** | Universal Ledger（GCUL） | Pre-GA（2026 年文档更新） | 聚焦于商业银行货币、代币化资产及金融机构场景 |
| **代理支付协议** | AP2 + A2A x402 扩展 | 已发布（2025-09，x402 与 Coinbase / Ethereum Foundation / MetaMask 联合开发） | AP2 定位为 payment-agnostic 信任层/开放协议，x402 扩展支持稳定币支付 |
| **稳定币支付应用案例** | Pay.sh（× Solana 基金会） | 2026-05 发布 | AI 代理用 Solana 稳定币按次购买 Google Cloud API 的实验性接入点 |

**关键洞察**：这些产品的公开设计显示出一定的支付方式与资产中立特征，但不同产品的资产支持范围并不一致。AP2 官方定位为 payment-agnostic 框架，明确支持包括稳定币在内的多种支付方式；GCUL 则更直接聚焦于商业银行货币、代币化资产及金融机构基础设施，且目前标注为 Pre-GA Offering。

因此，我们认为 Google 的公开产品方向更接近多资产数字金融基础设施，而非围绕单一稳定币构建支付体系；这一判断仍属于结构性推论。

但这不等于"USDC 很容易接入"。中间至少还有：技术兼容 → 资产选择 → 客户需求 → 流动性 → 合规/风险管理 → 结算/会计/Treasury → 商业条款 → 产品上线。

> "协议可以支持 USDC" 和 "Google Cloud 会接受 USDC" 是两个完全不同的问题。

### 1.3 Google Cloud 招聘的真实意图（F1）

2026 年 8-9 月，Google Cloud 在香港招聘 **Industry Principal Architect, Web3**（Advanced 级别）。

**岗位要求（Google Careers 原文）**：
- 10 年系统架构/分布式系统/云基础设施经验
- 4 年生产级 Web3 系统/区块链协议/智能合约生态经验
- 熟悉机构 Web3 用例：RWA 代币化、稳定币支付、代币化存款、数字资产托管（在受监管金融环境中）
- 熟悉多方计算（MPC）、硬件安全模块（HSM）、交易签名架构、机密计算
- 熟悉香港金管局（HKMA）和证监会（SFC）规则

**岗位职责原文**：指导 C-level 高管、协议创始人和首席架构师通过高风险的技决策；通过识别行业共性架构摩擦点来编写可复用的参考架构；影响 Google 的 Web3 产品路线图。

**我们的判断**：
该岗位表明 Google Cloud 正在为 Web3、稳定币支付、代币化存款和机构数字资产等企业场景配置专门能力，并明确要求候选人参与客户架构、行业共性问题和产品路线图反馈。

**证据边界**：
- ✅ 该岗位强化了 Google Cloud 对该领域进行商业化探索的证据
- ❌ 不能单独证明具体产品已经形成规模化需求
- ❌ 招聘广告本身不能证明 Google Cloud **已经决定**扩大稳定币支付或新增某一种特定稳定币

**为什么是香港？一个需要拆解的反向信号**

岗位地点选在香港而非美国，且明确要求熟悉 HKMA（香港金管局）和 SFC（证监会）规则。这可能指向一个与 USDC 无关的解释：

- 香港《稳定币条例》（Cap. 566）于 2025-08-01 生效，HKMA 已于 2026-04-10 授予两个稳定币发行牌照（Anchorpoint Financial 和汇丰银行），港元稳定币预计 2026 年中推出
- Google 可能在为香港的**港元稳定币**或**代币化存款**基础设施做准备，而非为 USDC 进入 Google Cloud 做准备
- 如果是这样，这条招聘证据对"USDC 进入 Google Cloud"的支撑力度比本报告呈现的更弱

**我的判断**：香港招聘是一个**中性偏弱**的信号——它证明 Google 在亚太布局数字货币基础设施，但不能直接推导为 USDC 进入 Google Cloud 的前兆。该证据需要与 Google 美国侧的产品布局分开评估，不宜作为 USDC 采用假设的核心支撑。

### 1.4 Apple 的平行信号：战略评估阶段（F1）

Apple 于 2026 年 8 月发布 **Apple Pay Financial Product Strategy Lead** 招聘（jobs.apple.com，纽约/库比蒂诺），归属 Apple Card / Apple Cash 团队。

**岗位要求原文**：
- 6 年以上咨询、投行、公司战略或战略财务经验
- 2 年以上 P2P 支付或信用卡经验
- **"Understanding of stablecoins, tokenized deposits, and blockchain technology"**

**与 Google 的关键差异**：

| 维度 | Google | Apple |
|---|---|---|
| 阶段 | 基础设施阶段——已发布 GCUL/AP2/Pay.sh，PYUSD 已接入 | 战略评估阶段——招聘战略负责人，无公开产品信号 |
| 面向 | 企业/机构客户（Google Cloud） | 消费者支付（Apple Card / Apple Cash / P2P） |
| 信号强度 | 较强——有产品布局 + 客户采用 + 招聘 | 较弱——仅有招聘信号 |
| 对 Circle 的含义 | USDC 可能进入企业支付分发渠道 | USDC 可能进入消费者 P2P/卡支付场景，但证据更弱 |

**我的判断**：Apple 的信号比 Google 弱，但方向一致——大型支付平台正在把稳定币从"交易所出入金工具"重新分类为"支付基础设施的战略选项"。这强化了 USDC 作为合规稳定币在机构/企业侧的 narrative，但 Apple 侧目前没有可验证的产品或合作证据。

**证据边界**：
- ✅ Apple 正在招聘具备稳定币/代币化经验的战略人才
- ❌ 不能证明 Apple 已经决定采用 USDC 或任何特定稳定币
- ❌ 不能证明 Apple × Circle 存在商业合作
- ❌ 招聘广告本身不能证明具体产品已经形成规模化需求

---

## 二、Google 真正构建的可能不是"稳定币支付"，而是"数字货币基础设施"

这是本报告最重要的一个洞察。

Google Cloud 自己对 Universal Ledger 的官方描述（cloud.google.com/application/web3/universal-ledger）中强调的概念是：

> "multi-asset" / "commercial bank money" / "tokenized assets" / "atomic settlement" / "24/7 movement" / "programmable financial infrastructure"

这不只是"需要稳定币"——它描述的是一个**允许多种数字货币和代币化资产参与企业支付与结算的基础设施层**。

这不是 Google 已公开宣布的路线图，而是我们基于其当前产品架构做出的结构性推论。

### 2.1 三种可能的"货币"形态

| 类型 | 当前状态 | Google Cloud 的关系 |
|---|---|---|
| **第三方稳定币**（USDC/PYUSD） | 已存在（PYUSD 已接入） | 作为支付通道资产 |
| **代币化存款 / 商业银行货币**（Tokenized Deposits / Commercial Bank Money） | GCUL 已支持 | Google 自己描述的核心用例 |
| **代币化资产 / RWA**（Tokenized Assets） | 广泛的机构资产代币化生态（包括银行货币、基金份额及其他证券化资产） | Circle 的 Arc 试图向该方向延伸；BlackRock BUIDL 和 DTCC 并非 Circle 的产品 |

**推论**：未来的竞争未必是"USDC vs PYUSD 谁赢"，而可能是**谁能够获得更大的企业数字美元结算份额**。甚至更复杂——USDC + 代币化存款 + GCUL 可能共同存在。

### 2.2 这对 CRCL 意味着什么

如果 Google 的答案是"多资产并存"，那么 Circle 的竞争重点**不是"Google 是否接受 USDC"**，而是：

> USDC 是否能够成为 Google Cloud 企业支付生态中**具有重要流动性、合规可用性和企业采用基础**的美元结算资产？

这是一个更高维度的竞争——不是零和博弈，而是"谁获得更多 settlement share"。

---

## 三、USDC 有没有进入这个体系的条件？

### 3.1 优势（F1 + F2）

| 条件 | 已观察证据 | 证据状态 |
|---|---|---|
| **流动性** | ~$74B 市值（2026-09），占稳定币市场 ~24% | Confirmed |
| **合规** | GENIUS Act 已立法（2025-07-18 签署）；Circle National Trust 获 OCC 最终批准（2026-07-10）；MiCA 合规 | Confirmed |
| **企业采用** | Visa 美国结算网络（2025-12，年化 $3.5B run-rate）、Mastercard EEMEA（2025-08）、CPN 年化 $23B | Corroborated |
| **多链可用性** | Ethereum / Solana / Arc / Base 等主要生态 | Confirmed |
| **分发网络** | Coinbase 深度集成 | Confirmed |

> 这些因素构成 USDC 的潜在进入条件，但不等同于 Google-specific qualification。

**合规维度的细分**：

| 维度 | 事实 | 对 Google 的意义 |
|---|---|---|
| 美国联邦稳定币监管框架 | GENIUS Act 已成法 | ↑ 法规确定性 |
| Circle 监管基础设施 | National Trust 等 | ↑ 机构合作条件 |
| 欧洲 | MiCA framework | ↑ 跨境可用性 |
| **Google-specific approval** | **未确认** | **仍是缺口** |

**多链可用性的研究含义**：降低不同客户和结算场景下的资产迁移成本。

### 3.2 障碍

| 障碍 | 级别 | 说明 |
|---|---|---|
| **合规认证周期** | 🟡 中 | 公开资料尚不足以确定 Google 对第三方稳定币的合规、风险、储备及运营审查流程的具体周期；这可能构成新增准入门槛 |
| **PayPal/Paxos 的竞争关系** | 🟡 中 | PYUSD 是 Google Cloud 已确认的稳定币；Google 不想"选边站" |
| **Google 优先级** | 🟢 低 | AI 是核心战略，Web3 是基础设施层——不影响方向，影响速度 |
| **发行方风险** | 🟡 中 | 若 Circle 出现储备/监管问题，Google 承担声誉风险 |

---

## 四、为什么 Google 可能同时支持 PYUSD 与 USDC？

不要写成二选一。

**多稳定币并存可能比赢家通吃更符合基础设施提供商的利益。**

理由：
1. **资产中立 = 降低对单一发行方的依赖风险**
2. **客户需求多元**：不同客户（银行 vs 加密原生 vs 传统企业）需要不同的结算资产
3. **监管合规**：美国部分州/国家可能对特定稳定币有偏好；多资产支持是合规覆盖最广的路径
4. **GCUL 的设计哲学**：从一开始就不是"选一种稳定币"，而是"支持所有合规数字资产"

**三种可能的演进路径**：

| 路径 | 描述 |
|---|---|
| **Path A — Multi-stablecoin** | PYUSD + USDC + 其他合规稳定币并行 |
| **Path B — Payment-agnostic rail** | Google 将稳定币支持抽象为底层 payment rail，稳定币只是其中一种结算方式 |
| **Path C — Bank-money-centric** | GCUL / 代币化存款成为主要机构结算轨道 |

USDC 是否进入 Google Cloud，不是一个已经开始倒计时的"阶段 2"，而是上述不同路径下的一个待验证变量。

---

## 五、对 Circle 到底意味着什么？

### 5.1 Direct Revenue：目前难以证明具有重要性

**我们无法用公开数据证明 Google Cloud 对 Circle 的储备收入形成重要贡献。**

Google Cloud 的云收入规模很大，但"云收入"不能直接转换成"稳定币支付余额"。企业客户可能通过银行账户、卡、ACH、电汇等方式支付，稳定币只是其中一种结算方式。

因此，本报告不采用"Google Cloud revenue × stablecoin penetration"估算 Circle 收入，而将其视为一个待观察的 USDC float / settlement balance 问题。Circle 的经济模型核心是**平均 USDC 流通量 × 储备资产收益率 × Circle 经济留存份额**，而非"支付流水 × 费率"。

**Google → USDC → CRCL 财务传导链**

| 环节 | 当前证据 | 状态 |
|---|---|---|
| Google 数字货币基础设施 | Universal Ledger / AP2 / Pay.sh | Confirmed |
| Google → PYUSD | 公开确认接受少数客户使用 | Confirmed |
| Google → USDC | 未确认 | Unconfirmed |
| USDC → 企业结算 | Visa/Mastercard 真实场景 | Corroborated |
| Google → USDC volume | 未确认 | Unconfirmed |
| Google adoption → incremental USDC demand | 理论关系 | Inference |
| incremental USDC demand → incremental average balance / float | 理论关系 | Inference |
| incremental float → Circle reserve income | 已知商业机制 | Confirmed |
| Google → CRCL earnings | 尚未建立 | Unproven |

**注意**：Incremental float ≠ circulating supply。Google 生态增加 USDC 使用不一定意味着 USDC circulating supply 增加——可能只是已有 USDC 被更频繁地使用。真正的财务传导核心是 **incremental average balance / float**，而非 circulating supply。

**需要未来观察的真正财务变量**：
1. Google Cloud 通过 USDC 产生的**增量平均 USDC 余额 / float**
2. Circle 在该增量余额中的**经济留存份额**
3. USDC 在 Google 生态中的**结算频率**
4. Google Cloud 生态带来的**增量 USDC 流通量**（超出 Google 生态本身的网络效应）

**结论**：我们将其视为**待观察的 USDC float / settlement balance 问题**。

### 5.2 情景量级测算（假设性推演）

**方法**：以 PYUSD 市值（~$2.8B）和 Visa/Mastercard 结算 run-rate（$3.5B/$23B年化）为锚点，构造三档情景。**以下测算纯属假设性推演，用于框架化思考，不构成预测或投资建议。**

| 情景 | 假设增量 USDC 结算规模 | 对应增量平均余额（假设 50% 停留率）* | 储备收入（按当前 Fed 利率 3.88%） | Circle 留存（按 Q2'26 RLDC margin ~41%） | 对 CRCL 年化的潜在影响 |
|---|---|---|---|---|---|
| **Bear** | ~$3.5B（Visa 级别年化结算） | ~$1.75B | ~$68M | ~$28M | 极小——占 Circle 年储备收入（~$2.7B）不到 1% |
| **Base** | ~$23B（CPN 级别年化结算） | ~$11.5B | ~$447M | ~$183M | 中等——占 Circle 年储备收入 ~7% |
| **Bull** | ~$50B（假设 Google 生态大规模采用） | ~$25B | ~$970M | ~$398M | 显著——占 Circle 年储备收入 ~15% |

> *停留率假设：结算需求不等于平均余额。如果 USDC 在 Google 生态中按次结算后立即换出，平均余额可能远低于结算规模。此处假设 50% 为简化处理，实际比例取决于结算频率和资金停留时间。

**关键观察**：
- 即使 Bull 情景（$50B 年化结算），对 Circle 的年化收入影响约为 $1B 量级——这仍然不是 CRCL 估值的主要驱动因素。
- 真正重要的是 **settlement share 的增量**和 **资金停留时间**，而非结算规模本身。
- 利率敏感性：如果 Fed 进入降息周期（当前 3.88% → 假设降至 2.5%），同样 $25B 平均余额对应的储备收入将从 ~$970M 降至 ~$625M，减少 ~36%。利率路径与 float 增量同等重要。

### 5.3 利率敏感性：被忽略的宏观变量

Circle 储备收入的核心公式：**USDC 平均余额 × 短端利率 × Circle 经济留存比例**。

**当前利率环境**（2026-09-22）：
- Fed 于 2026-09-16 加息 25bps 至 3.75%-4.00%，为 2023 年以来首次加息
- 有效联邦基金利率 ~3.88%
- 如果通胀持续，短端利率可能维持高位；如果经济走弱，降息周期可能开启

**利率对增量 float 收入的影响**：

| 假设增量平均余额 | 利率 4.00%（当前） | 利率 3.00% | 利率 2.00% | 利率 1.00% |
|---|---|---|---|---|
| $5B | ~$200M | ~$150M | ~$100M | ~$50M |
| $10B | ~$400M | ~$300M | ~$200M | ~$100M |
| $25B | ~$1.0B | ~$750M | ~$500M | ~$250M |

**结论**：在降息周期中，即使 Google adoption 带来增量 float，对 Circle earnings 的实际贡献也会被利率压缩。利率路径与 float 增量是 CRCL thesis 的两个同等重要的未知变量。

### 5.4 Distribution Economics：潜在重要

如果 USDC 被纳入 Google Cloud 的计费 / AI 代理商务 / API 市场：

> Google Cloud → 企业客户 → USDC 支付需求 → **潜在的 USDC B2B 分发渠道**

这不是"Google 给 Circle 带来一点收入"——而是"USDC 进入一个拥有庞大企业客户基础的云平台，可能形成持续的结算余额需求"。

量级尚无法估计。分发渠道扩大可能增加 USDC 的可用场景和结算需求，但对 Circle 财务的实际贡献取决于新增 USDC 流通量、平均余额、资金停留时间以及 Circle 对相关经济收益的留存比例。**因此，distribution expansion 是 adoption signal，而非天然的 earnings signal。**

### 5.5 市场是否已经 price in？

**检验问题**：PYUSD 声明（5月）、Apple/Google 招聘（8-9月）这些信号出来后，CRCL 股价有没有反应？

**已知事实**：
- CRCL 在 2026-05-04 CLARITY Act 妥协后单日涨近 20%（监管驱动，非稳定币 adoption 驱动）
- CRCL 在 2026-06-30 竞争对手推出稳定币后单日跌 17.55%（竞争格局驱动）
- CRCL 在 2026-09-16 Fed 加息后市场整体走强，股价 ~$94.49（截至 2026-09-22）
- **未观察到**因 Google PYUSD 声明或 Apple/Google 稳定币招聘导致的 CRCL 异常波动

**我的判断**：市场**尚未 price in** Google/USDC adoption 信号。CRCL 近期的股价驱动因素是监管（CLARITY）、竞争（Tether/银行系稳定币）和利率预期，而非企业支付基础设施 adoption。这意味着：
- 如果 Google 正式确认 USDC 支付，CRCL 可能有**正向重新定价**空间
- 但也意味着当前"OBSERVE"状态的**边际信息价值尚未被市场消化**——这是一个被低估的 monitoring item

**证据边界**：
- ✅ 上述股价事实来自公开行情数据
- ❌ 无法排除"市场已部分定价但未反映在短期股价中"的可能
- ❌ 期权隐含波动率数据未纳入本次分析

### 5.6 Bear case 补强

**原有下行因素**（已在 §6.2 Competitive Architecture 中讨论）：
- Path C：代币化银行存款成为主要机构结算轨道，USDC 被边缘化

**新增两个更直接的下行因子**：

**① GENIUS Act 禁止稳定币付息 → 削弱企业"生息现金管理工具"动机**

GENIUS Act §4(a)(11) 禁止稳定币发行方向持有人支付利息或收益。这意味着：
- 企业持有 USDC **无法直接获得储备收益**（收益归发行方 Circle 或分销渠道）
- USDC 对企业 Treasury 的吸引力主要来自**结算效率**，而非**收益**
- 如果企业主要用 USDC 做"过路资金"（结算后立即换出），平均余额和资金停留时间可能远低于预期
- 这压低了 USDC 作为"企业现金管理工具"的需求上限，从而压低了 settlement share 的天花板

**② 竞争格局：USDT 体量远大于 USDC，且正在机构化**

| 稳定币 | 市值（2026-09） | 份额 | 机构化程度 |
|---|---|---|---|
| **USDT（Tether）** | ~$183B | ~52%（Stablecoin Insider Q2'26；部分信源如 Glassnode 年内高点曾达 ~58-60%） | 正在推进合规化、审计透明化，已获多项监管进展 |
| **USDC（Circle）** | ~$74B | ~24% | 合规优势明显（GENIUS、OCC、MiCA），但体量仅为 USDT 的 ~40% |

- USDT 在**流通量**上仍然占据绝对主导地位（~52-60% vs ~24%，份额随信源和时点浮动，数据截至 2026-09）
- USDC 的优势在**合规性和机构分发**，但如果 USDT 持续推进合规化，USDC 的差异化优势可能被侵蚀
- 这进一步说明：USDC 的核心竞争不是"Google 选谁"，而是**能否在整体数字美元市场中维持/提升份额**

### 5.7 Institutional Validation：中长期信号

Google Cloud 使用 USDC 可以作为**大型企业对 USDC operational / compliance readiness 的市场信号**，但不能等同于监管认证。

> Google 接受 USDC ≠ SEC/Treasury/banking regulator 对 USDC 认证。但 Google 作为全球主要云服务提供商之一，其企业采用行为本身就是一个 institutional adoption signal。

### 5.8 Settlement Share：这才是 CRCL Thesis 真正值得观察的核心变量

**我的正式定义：Enterprise Settlement Share = USDC 在企业链上美元结算中的相对份额。竞争对象包括但不限于 PYUSD、代币化银行存款和其他受监管数字美元。**

> **Measurement caveat**：目前公开数据缺乏统一的 Enterprise Settlement Share 统计口径。链上交易量、稳定币流通量和支付交易量均可能包含交易所、DeFi、机器人及其他非企业活动。因此，该指标目前属于我的研究框架，而非可直接读取的市场数据。

从 CRCL 的长期视角看，Google Cloud 并不是终点，而是一个观察窗口。真正决定 Circle 长期经济价值的变量，是 USDC 在企业链上结算中的份额，而不是某一家大型客户是否接受 USDC。

如果未来以下组合成为现实：

> USDC（结算层） + AP2/x402（代理授权+支付协议）+ Arc（机构结算链） + GCUL（企业资产发行层）

Circle 获得的可能不是一次性的 payment volume，而是 **stablecoin infrastructure position**——成为互联网企业支付基础设施的重要结算层之一。

这更接近当前 CRCL 长期 thesis 所关注的基础设施价值捕获问题。

---

## 六、真正应该监控什么？

### 6.1 CRCL Research Dashboard（三层结构）

**A. Google / Payment Adoption（采用信号）**

| 指标 | 当前 | Signal 级别 | 触发条件 |
|---|---|---|---|
| Google Cloud USDC 支付公告 | 未触发 | 强 | 官方公告 |
| Google Cloud 计费支持 USDC | 未触发 | 强 | 技术文档/支持页面更新 |
| AP2/x402 USDC 使用量 | 极低 | 中 | 形成可观察规模* |
| Pay.sh USDC 交易量 | 未启动 | 中 | 出现持续可验证使用量* |
| Google Cloud 企业稳定币客户数 | 未公开 | 强 | 多家企业客户公开确认* |

> *具体数值阈值属于我的内部监控标准，并不代表行业公认的重要性门槛。

**B. USDC Institutional Adoption（行业验证）**

| 指标 | 当前 | Signal 级别 |
|---|---|---|
| Visa USDC 结算 | 已发生（美国，2025-12-16，年化 $3.5B run-rate） | 已确认 |
| Mastercard USDC/EURC 结算 | 已发生（EMEA，2025-08-26 扩展） | 已确认 |
| 银行结算量 | 未公开 | 强 |
| 企业 Treasury 采用 | 未公开 | 强 |
| USDC 跨境 B2B 量 | 未公开 | 强 |

**C. Circle Financial Transmission（CRCL 财务传导）**

这才是最重要的——形成完整证据链：

> Google infrastructure adoption → USDC accessibility → incremental enterprise settlement demand → incremental average balance / float → Circle reserve economics → CRCL earnings

| 指标 | 为什么重要 |
|---|---|
| **USDC average balance** | **核心**——Circle 储备收入的直接驱动因素 |
| USDC circulating supply | 旁证——上升不一定意味着增量需求，可能只是已有 USDC 被更频繁使用 |
| USDC velocity | 辅助 |
| Reserve income | 核心 |
| Distribution costs | 核心 |
| Other revenue | 辅助 |
| **USDC institutional / enterprise settlement share** | **核心**——防止把流通量上升错误归因为 Google adoption |

> **关键观察**：即使 USDC circulation 上升，也不能直接归因于 Google Cloud adoption。必须观察 USDC 在企业/机构结算中的相对份额变化，才能建立因果关系。

### 6.2 Competitive Architecture Framework

**不在各路径上赋予概率——当前证据不足以支撑概率判断。**

| 路径 | 描述 | 对 CRCL 的影响 |
|---|---|---|
| **Path A — Multi-stablecoin** | Google 支持 PYUSD + USDC + 其他合规稳定币 | 竞争从"谁被选中"变成"谁获得更多 settlement share" |
| **Path B — Payment-agnostic rail** | Google 将稳定币支持抽象为底层 payment rail | Circle 的竞争重点变成 USDC 是否能成为默认流动性资产 |
| **Path C — Bank-money-centric** | GCUL / 代币化存款成为主要机构结算轨道 | 对 CRCL 是竞争压力，但可能验证 Google 正在推动的基础设施方向 |
| **Path D — Hybrid institutional rail** | 代币化银行货币 + 稳定币 + 支付协议共存 | 现实世界可能不是单一路径；USDC 可能在混合轨道中获得增量份额。**证据等级：当前证据最不支持的路径，但现实世界可能是混合路径。** |

---

## 七、CRCL Investment Implication

### 7.1 对 Thesis 的影响

**不改变 Thesis Baseline v1.0**。

本事件不足以改变现有 CRCL Thesis，也不足以形成独立交易催化剂。

### 7.2 对 Trade View 的影响

**维持 WAIT**。

### 7.3 Investment Implication 五层判断

| 层级 | 当前判断 |
|---|---|
| **Thesis** | 不变——Google Cloud 是 long-term adoption signal，非当前估值驱动因素 |
| **Earnings** | 暂无可量化影响——Google → USDC → CRCL earnings 传导链尚未建立。即使 Google 宣布 USDC billing，也仍需观察 incremental float 是否真正增长，才能判断对 Circle 财务的实际影响 |
| **Valuation** | 暂无重新估值依据——缺乏 incremental float 和 settlement share 数据 |
| **Catalyst** | 尚未形成——Tier 1/2/3 触发器未触发 |
| **Monitoring** | 提升 Google / enterprise settlement 权重——Tier 1/2/3 触发器已就位 |

### 7.4 Research Status：OBSERVE

后续仅在以下事实出现时升级判断：

| Tier | 触发事件 | 动作 |
|---|---|---|
| **Tier 1** | Google Cloud 官方确认 USDC 支付 | 重新评估 direct revenue + distribution 假设 |
| | Circle × Google 正式商业合作 | 同上 |
| **Tier 2** | AP2/x402 出现可验证的 USDC 使用量 | 跟踪 adoption signal |
| | Google Cloud 企业客户稳定coin adoption 公开数据 | 跟踪 |
| **Tier 3** | USDC circulating supply / average balance 出现与企业支付相对应的结构性增长 | 财务模型更新 |
| | Circle 财务披露能够观察到相关收入传导 | 财务模型更新 |

---

## 八、结论

**Google Cloud 是否最终采用 USDC 还没有被证明；但 Google 的产品布局提供了一个值得关注的信号：企业支付基础设施正在开始为 programmable dollars 留出原生位置。**

对 Circle 而言，真正值得观察的不是 Google 会贡献多少收入，而是 USDC 能否获得更大的企业数字美元结算份额。

**最终判断**：
本报告将 Google Cloud USDC adoption 定义为 CRCL 的**长期 adoption signal**，而非当前 valuation driver。

---

## What Would Change Our Mind?

**Bullish evidence**
- Google 官方确认 USDC billing/payment
- Circle × Google commercial partnership
- Google enterprise customers publicly using USDC
- AP2/x402 出现持续可验证的 USDC settlement
- USDC enterprise settlement share 持续提升
- Circle 财务数据开始出现对应 transmission

**Neutral evidence**
- Google 继续支持 PYUSD
- AP2 支持稳定币但没有 USDC usage
- GCUL 支持 tokenized bank money

**Thesis-negative evidence**
- 即使 Google 扩大数字货币基础设施，企业结算价值捕获持续向 tokenized bank money / bank-controlled rails 转移，而 USDC 的 enterprise settlement share 没有同步提升。
- **这是真正的 kill condition**：企业数字美元市场增长，但 USDC 在其中的价值捕获能力没有增长。
- Google 不选 USDC ≠ Circle thesis 被证伪。真正能证伪的是：企业数字美元市场增长，但 USDC 在其中的价值捕获能力没有增长。

**Evidence → 改变的假设**

| Evidence | 改变的假设 |
|---|---|
| Google USDC billing announcement | Distribution hypothesis |
| Circle × Google commercial partnership | Commercial relationship hypothesis |
| Google enterprise customers using USDC | Adoption hypothesis |
| Incremental average USDC balance growth | Float hypothesis |
| Circle disclosed economics transmission | Earnings hypothesis |

> 关键纪律：Google announcement → 只更新 distribution hypothesis。不允许直接跳到 CRCL bullish。

---

## 附录：数据来源

**F1 — Primary / Company / Regulatory**
- Richard Widmann 声明（Consensus Miami 2026，CoinDesk 2026-05-10）
- Google Cloud Universal Ledger 官方文档（2026 年更新）
- Google Cloud AP2 官方博客（2025-09）
- Solana Foundation × Google Cloud Pay.sh 公告（2026-05）
- Google Careers：Industry Principal Architect, Web3（香港，2026-08/09 发布）
- Visa USDC 结算上线公告（2025-12-16）
- Mastercard USDC/EURC 结算扩展公告（2025-08-26）
- SEC Innovation Exemption（SEC Press Release 2026-90，2026-09-17）
- Circle Q2'26 财报（Arc/DTCC/BlackRock/CPN 数据）
- HKMA 稳定币发行牌照公告（2026-04-10，Cap. 566）
- Fed FOMC 2026-09-16 利率决议（3.75%-4.00%）

**F2 — High-quality secondary**
- Sullivan & Cromwell 备忘录（2026-09）：豁免令法律拆解
- Galaxy Research（Alex Thorn）：第三方包装 vs 发行人自办模式分析
- Davis Polk：香港稳定币条例概览（2026-09）
- TIKR：CRCL 股价分析（2026-09）
- Goldman Sachs 报告（2026-09-18，James Yaro）——**F3 转述**：经 techflowpost 转述，非原文核实，信源等级降为 F3

**F3 — Market data / aggregator**
- CoinDesk（2026-05-10）：Consensus Miami 报道
- Yahoo Finance（2026-09-18）："Google Adds Stablecoin Support to AI Payment System"
- Yahoo Finance（2026-05）：Richard Widmann 声明独立转述（第二信源）
- CryptoRank / CoinStats：PYUSD 市值 ~$2.8B，USDC ~$74B（截至 2026-09）
- Stablecoin Insider：PYUSD Q2 2026 报告
- DefiLlama：USDT ~$183B / USDC ~$74B 市值数据（2026-09）
- CNBC / Forbes：Fed 利率决议报道（2026-09）
- Bitcoin Foundation / CoinDesk（2026-09）：Apple/Google 稳定币招聘报道

---

## Version History

| 版本 | 日期 | 变更 |
|---|---|---|
| v1.0 | 2026-09-21 | 初稿（"PYUSD 之后，USDC 会不会进？"） |
| v2.0 | 2026-09-22 | Research-grade 升级 |
| v2.1 | 2026-09-22 | Publication Ready 最终修订 |
| v2.2 | 2026-09-22 | Investment Committee QC：①Visa 日期修正为 2025-12-16 + 补 $3.5B run-rate②"三层架构" → "三类布局/观察窗口"③asset-agnostic 收紧为"较强资产中立特征"+ Pre-GA 标注④删除"6-12个月"无来源数字⑤Arc/BUIDL/DTCC 归属修正⑥删除 Binance distribution 细节⑦Dashboard 阈值加内部标注⑧新增 financial 传导链表⑨删除阶段表，改为 Path A/B/C⑩Scenario D 改为"gains meaningful share"⑪"downside" → "竞争/价值捕获风险"⑫新增 Enterprise Settlement Share 正式定义⑬新增 What Would Change Our Mind 章⑭合规维度细分行⑮distribution "正向影响"改为 adoption signal 表述⑯数据来源按 F1 Primary / F2 Secondary / F3 Aggregator 分类 |
| v2.3 | 2026-09-22 | Publication QC + Apple 平行信号：①Financial Transmission 改为 incremental demand → incremental average balance / float → reserve income → Circle economics②Enterprise Settlement Share 加 measurement caveat③优势表"评级"改为 Evidence Status④asset-neutral 收紧为"一定的支付方式与资产中立特征"⑤招聘措辞收紧⑥ES 去重 + 新增 Apple 信号 + 核心研究框架段⑦Investment Implication 五层判断⑧Scenario 改为 Competitive Architecture + Path D Hybrid⑨What Would Change Our Mind 证伪速度表⑩标题升维为"USDC 能否获得企业数字美元结算份额"⑪删除媒体化表述⑫新增 §1.4 Apple 平行信号⑬Dashboard C 同步 incremental 传导链⑭Earnings 层补 incremental float 观察⑮Path D 加证据等级标注 |
| v2.4 | 2026-09-22 | Final QC：①修复 Evidence → 改变的假设表笔误（Google × Google → Circle × Google）②§5.4 删除两处重复表述③SEC 引用编号修正为 SEC Press Release 2026-90 |
| v2.5 | 2026-09-22 | 机构合规补项：①新增分析师认证声明②新增利益冲突/持仓披露（我不持有 CRCL 仓位）③新增合规审阅状态声明（经 Investment Committee QC，外部合规审阅尚未完成）④免责声明扩展（前瞻性陈述、过往表现、司法管辖区、分发限制）⑤Richard Widmann 声明补第二信源（Yahoo Finance，F1 双信源）⑥高盛报告信源等级从 F2 降为 F3 转述（经 techflowpost 转述，非原文核实） |
| v2.6 | 2026-09-22 | 五项加深：①新增情景量级测算表（Bear/Base/Bull 三档）②新增利率敏感性分析（Fed 3.88% 当前利率）③香港招聘反向解读④市场 price-in 检验⑤Bear case 补强（GENIUS Act 付息禁令 + USDT 竞争格局） |
| v2.7 | 2026-09-22 | 事实修正：①Cap. 656 → Cap. 566（香港稳定币条例章节编号）②USDT 份额标注改为 ~52%（Stablecoin Insider Q2'26），并注明部分信源年内高点曾达 ~58-60% |
| v2.8 | 2026-09-22 | 人称统一：全文"ZK Labs"改为"我"，"ZK Labs 判断"改为"我的判断"，落款保持金戊乾坤3号署名 |

---

*本文是「市场观察」系列 Google Cloud × 稳定币专题，v2.8 Publication Ready，署名金戊乾坤3号。符合 No Evidence, No Change 纪律。*
