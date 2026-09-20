---
layout: default
title: "blob 扩容、Quick Slots、账户抽象、快速最终性：Ethlabs Week 13 四题与我们的答案"
permalink: /research/2026/09/20/ethlabs-week13-four-questions.html
date: 2026-09-20
categories: research
author: 金戊乾坤2号
data_cutoff: 2026-09-20
version: "v1.1"
tags: [Ethereum, Hegota, Blob, EIP-8198, QuickSlots, AccountAbstraction, EIP-8141, FCR, Finality, 投研]
---

# blob 扩容、Quick Slots、账户抽象、快速最终性：Ethlabs Week 13 四题与我们的答案

**投研文章｜ZK Labs Research**
作者：金戊乾坤2号｜日期：2026-09-20｜标的：ETH / 以太坊 L1 升级路径

> 本文是对 Ethlabs 周报 **Week 13（2026-09-20）** 提出的四个议题（含其引用的 Week 12）的独立研究与回答。
> 关键数字来自**链上实测、EIP 一手文本、EF 官方文件**；**未取得公开出处者已在第九节集中列出**，且不参与支撑结论。
> 本文为公开研究文稿，**只收录机制与市场结构层面的判断，不构成交易信号或投资建议**。

---

## 导语：这件事在路线图上的位置，以及一个容易被读错的排序

Hegotá 是 Fusaka 之后的一场合成分叉（预计 2027 Q2），EF 已经把它拆成若干个**可以分别推进**的议题。Ethlabs 的 Week 13 是生态侧第一次把其中四个放进同一份周报 —— blob 扩容、Quick Slots、原生账户抽象、快速最终性 —— 并给出自己的取舍与语气。

这份周报值得一次性回答四个问题，因为它把四件看起来无关的事摆在了一起：blob 扩容是**容量**问题，Quick Slots 是**延迟**问题，账户抽象是**钱包**问题，快速最终性是**确认时间**问题。我们的核验结论是：**这四件事在 fork 机制里并不平权。**

**中心判断（本文唯一的主论点）**：这一个 fork 的裁决顺序是 **「后量子通道 > 延迟改善 > 容量扩张」**。它不是我们的偏好排序，而是从 fork 机制里读出来的 —— 依据、以及一个必须先掐掉的误读，都在第七节。

**术语约定**：`slot` = 时隙，当前约 12 秒一个出块周期｜`target` = blob 费用曲线的目标值（长期平均应达到的 blob 数）｜`max` = 每块 blob 硬上限｜`headroom` = 性能优化腾出的余量｜`headliner` = 升级主推项｜`tier list` = EF 对 EIP 的分级清单｜`justification` = FFG 两阶段的第一阶段，先 justification 再 finalization｜`retuning` = 重调参数，客户端要重做性能调优。

**证据标注**：〔A〕一手规范 / 官方文件 / 链上实测｜〔B〕具名媒体报道 / 独立数据商｜〔C〕周报自述（未检索到公开一手出处）。

---

## 一、摘要：一条中心判断，六条支撑

### 中心判断

**后量子通道 > 延迟改善 > 容量扩张。**〔A〕

依据不是 EF 的优先级声明 —— 那份清单（Week 12 引用的 EF/团队优先级）的顺序是**抗审查 > 更快 > 性能工程 > 原生 AA**，原生 AA 排在最后 —— 而是**fork 机制**：FOCIL（EIP-7805）与 EIP-8141 是官方文件里的 locked-in headliner（共识层与执行层各一），8198 则是 B 档 + 四项前置。**投入顺序 ≠ 可延后性**：8141 在投入顺序上靠后，在可延后性上是不可延后的；8198 恰好相反。

### 六条支撑判断

**1｜这个 Fork 的主题不只是「更快」，还有「为后量子时代重写地基」。**〔A〕

EF Protocol 官方文件（2026-09-07）把 Hegotá 的两个 headliner 写定为 **EIP-7805 FOCIL**（"Locked-in **CL** headliner"）与 **EIP-8141 Frame Transactions**（原文 "Locked-in **EL** headliner"），后者被明确以**安全理由**推上 S 档：「为 PQ 签名方案提供路径而无需为每个方案分叉、用聚合让 PQ 验证可以被定价、以及退役 k1 密钥的路径。」Quick Slots、blob 扩容、FCR 属于性能与体验议题；原生 AA 与 PQ 密钥退役属于安全议题。**周报把两者放在同一层级叙述，会让读者低估后者的分量。**

**2｜blob 扩容的真正瓶颈不是容量，是「同一份 headroom 的竞争性用途」。**〔A〕

Ethlabs 自己在 Week 12 写得很清楚：性能工程带来的 headroom「可以支持**更多容量、更短的 slot、更低的节点要求**，或其中若干组合」。这三个用途互相争抢同一份预算。而 EIP-8198 文本要求：**缩短 slot 时，gas limit 与 blob 参数按比例缩放，以维持单位时间吞吐不变**。也就是说 —— **Quick Slots 是延迟升级，不是容量升级；每一秒的吞吐不变**。12→10 秒后，每块 gas limit 从 60,000,000 降到 50,000,000、每块 blob 上限从 21 降到 17。

**3｜当前 blob 市场：容量用了三成半，价格是零钱的零钱。**〔A〕

自采实测（2026-09-20，511 块窗口）：**平均 4.93 blobs/块 vs target 14（使用率 35.2%）、vs 上限 21（23.5%）**；空块占 17.5%，打到上限的块占 0.4%。价格方面 `eth_blobBaseFee` = 3,428,867 wei/blob gas，即**每个 128 KB blob 约 0.00000045 ETH（≈$0.00116）**。全部 L2 在 7 天内为 blobspace 支付 **$1,047（$149.58/天）**，约等于**用户实付 L1 费用的 0.03%（万分之三）**。**结论：今天继续扩 blob，在收入上找不到理由。**

**4｜但「收入为零」不等于「不该扩」——这是一道关于预期与承诺的题。**〔A〕〔C〕

@adietrichs 的框定是准确的：未必受限于当下容量，而是**受限于对未来的容量预期不清**。我们要补一层：这个问题的上游还有一个更硬的约束 —— **DA 机制选择本身要被 PQ 路线约束**。EF 已把 **EIP-8142（Block-in-Blobs）**列入 **D 档（declined）**，理由原文是它会「加深对 KZG 结构的依赖，与通往 J\* 的路径相冲突」；而 EF 的 DA 路线表里写着 **leanVM → PQ blobs**。所以「要不要继续扩 blob」的正解不是 yes/no，而是：**用 BPO 节奏把 target 路径写清楚，同时不要用当下的设计锁死未来的承诺机制。**

**5｜周报最需要「对表」的一处：Quick Slots 的乐观程度。**〔A〕〔B〕〔C〕

周报引用的是**客户端团队各自的 tier list**（Teku S / Prysm & Lighthouse A / Lodestar C / Nimbus & Grandine 倾向不纳入），并据此说「生态支持强，两周后 ACDC 推动升级为 Consider for Inclusion」。这不是造假 —— 它连不利项都列了。问题在于**没有同置**同一体系的 **EF Protocol 统一评级**（2026-09-07）：EIP-8198 在那里是 **B 档、均分 2/6**，理由原文「S/A 的支持来自 R&D；**专注交付的工程团队给了它 D**，理由是任何 slot 时间改动都会带来 **retuning 级联**」；而且列出**四项前置条件**，其中第四条「证明它不会复杂化分权共识」**要等规格存在之后才能判定**。**两类评级口径不同、不能相加，读者应当两组都看。**

**6｜FCR 与「快速最终性」：真要分清两个 1/6。**〔A〕〔C〕

公开一手材料里的「1/6」是**安全阈值语义**：EF 官方博客原文说单轮投票「大致可以把最终性时间减半，但可能把对抗容忍度从 1/3 降到约 **1/5 或 1/6**」。而周报里的 1/6 是**时延改善语义**（每 slot 检查 2/3 阈值 → 时延 −1/6；重验证者先投票 → 再 −1/6；两项叠加再加提前 justification → 整体 >50%）。**两种 1/6 含义完全不同，混用会把「安全边界变弱」误读成「性能提升」。** 另外：1/6 与 1/6 复利只有 **30.6%** 的改善，要得出「>50%」还需要第三项贡献约 29%。

---

## 二、题面复述：Week 13 到底提出了什么

周报（作者 Mislav Javor / @ox_shaman）这一周的四个板块，加上其引用的 Week 12，构成四个待答问题：

**Q1 blob 扩容**：「我们是否应该继续扩容 blob？」触发点是本周启动的一项工作 —— 回顾**当前供应**并规划未来参与方式。@adietrichs 框定问题：*while we may not be limited by the current capacity, we may be limited by unclear expectations on future capacity.*（未必受限于当前容量，而是受限于对未来容量的预期不清。）@casparschwa、@decentrek、@fradamt 把它转成一份**对 L2 的「实际与预期 blob 需求」调查**，输出「target 应该走到哪里、什么时候走」的报告；Derek 负责外联。同期的 @fradamt 在做**blob 容量报告**，并提出**提高 PeerDAS custody threshold** 的提案。

**Q2 Quick Slots（EIP-8198）**：@binji_x 与 @barnabemonnot 发布生态文章（引用 20+ 团队），主张「在 Hegotá 里把必要的地基打好，以便尽快实现 slot 时间改动」，并解释 **12 秒 → 10 秒**对这些团队为什么重要。

**Q3 原生账户抽象**：从「调和两个提案（EIP-8130 / EIP-8141）」转向「账户实际要怎么迁移」——@ox_shaman 负责把迁移流画出来（存量账户迁入 Frames、通过 `SETCODEFROM` 委托、作废已泄露或已退役的 ECDSA 密钥），产出 personas-and-user-stories 草案供钱包对照。另加一项：**cosigner（共签者）**应该进入「跨 8130/8141 可移植账户」的新标准，还是单独并存。

**Q4 FCR 与新最终性提速**：(a) FCR 的采纳闸门在 **RPC 供给方**，@_julianma 在推动并写实现指引（如何与既有 `safe` tag 期望兼容）；(b) 研究侧发现**可以用简洁 zk 证明来证明「某区块已被快速确认」**；(c) @fradamt 的分权共识形式化验证：所有性质已通过；(d) 三个提速数字：每 slot 检查 2/3 → −1/6；重验证者先投票 → 再 −1/6；把 justification 也提前处理 → **整体 >50%**。

---

## 三、Q1：还要继续扩 blob 吗？—— 链上数据给出的答案

### 3.1 供应侧：容量参数与实测占用

**权威参数（EIP-7910 `eth_config` 直问节点）**：`target = 14 blobs/块`、`max = 21`、`fraction = 11,684,671`，生效于 **BPO2（2026-01-07）**。

**自采实测（2026-09-20，最近 511 块 / 102.2 分钟）**：

- blob 总数 2,367；**平均 4.93 blobs/块**；中位数 4.0；最大 21
- **空块占 17.5%**；**打到上限的块占 0.4%**
- 对 target(14) 的使用率 **35.2%**；对上限(21) 还有 **76.5% 余量**
- 分段均值（8 段）在 4.45–5.68 之间波动，无趋势性抬升
- **另两个 24 块窗口的复核**：平均 **4.54** 与 **5.83 blobs/块**（使用率 32%–42%），max 19 —— 说明「3.5–4 成」这个量级不是单窗口运气，但**日内波动确实存在**

**独立交叉验证**：growthepie 的 `blob_size_bytes`（近 7 天）合计 **34.31 GB = 4.902 GB/天**。按每 blob 128 KB 折算 ≈ **37.4k blobs/天**，与自采的 4.93 × 7200 = **35.5k blobs/天** 偏差约 **5%**（37.4k / 35.5k = 1.054）。**两个独立口径指向同一结论：全网每天约 3.5–3.7 万个 blob，占 target 容量（100,800/天）的约 35%。**

### 3.2 价格侧：blobspace 现在的真实价格

- 直问节点：`eth_blobBaseFee` = **3,428,867 wei/blob gas**
- 每 blob = 131,072 blob gas → **0.0000004494 ETH ≈ $0.00116 / 128 KB**
- **一个可核验的机制细节**：`blob_base_fee = exp(excess / 11,684,671)` 与实测值在**5 位有效数字**上吻合（ln(3,428,867) = 15.0474；175,827,899 / 11,684,671 = 15.0473）。BPO2 把费率曲线的分母从 Fusaka 时代的 **3,338,477** 改为 **11,684,671（×3.5）** —— 这是**价格曲线陡度**的改动，与「改容量」是两件事。
- **这个改动的含义值得单独说**：同样一份 `excess` 增量，在 BPO2 之后带来的涨价幅度只有原来的约 **1/3.5** —— **价格曲线变平了**。对扩容的含义是双向的：把 target 抬上去，价格不容易立刻爆表；反过来，**要等到使用率明显偏离 target，价格信号才会出现**。所以本文的门槛 B 用 30 天均值，而不是瞬时值 —— 写作时 3,428,867 wei（≈0.0034 Gwei）的同一晚，实测已升到 **6,283,755 wei（≈0.0063 Gwei，+83%）**，日内弹性不小。
- 上游已经把「扩容」拆成了**容量（BPO target）**与**定价（fee curve）**两条独立的旋钮 —— 这是理解后面门槛体系的前提。

### 3.3 需求侧：谁在用、付了多少钱

**近 7 天（2026-09-13 → 09-19，growthepie）**：

- 全部 L2 的 **blob 费用合计 $1,047.04 = $149.58/天**
- blob 付费前五：**Robinhood Chain $46.82/天**、**Base $39.01/天**、MegaETH $16.44/天、Celo $12.33/天、Arbitrum $10.99/天
- blob 数据量前五：**Robinhood Chain 1.549 GB/天（31.6%）**、Base 1.263 GB/天（25.8%）、MegaETH 0.474 GB/天（9.7%）、Optimism 0.388 GB/天、Celo 0.355 GB/天
- 全部 L2 的 **L1 总成本（calldata + blobs + 验证）合计 $13,015.45 = $1,859.35/天**

**费用总量（同一时点，三种口径）**：

- **用户实付 L1 费用（直测 receipts，两个各 24 块的窗口）**：**247–253 ETH/天 ≈ $638K–654K/天**；其中**中位区块**的有效 gas 价 0.64–2.01 Gwei
- **独立口径**：CoinMetrics `FeeTotNtv` 近 5 日 **145.3–188.2 ETH/天**（均值 ≈176 ETH/天 ≈ $455K/天）—— 与我们上篇市场观察引用的「L1 每天总费用 ≈$46.5 万」一致
- **基础费销毁**：**95–147 ETH/天（≈$245K–380K/天）**（base fee 波动剧烈：本次 511 块窗口均值 0.05629 Gwei，最近两个窗口已升到 0.098–0.264 Gwei）

**费用结构（谁拿到钱、链上有多少空位）**：

- **小费占用户实付的 41%–66%**（两个窗口各自的中位占比），对应约 **100–167 ETH/天**流向验证者；**销毁只占实付的 34%–59%**
- **区块填充率**：511 块窗口均值 **50.2%**（gas limit 6,000 万）；最近窗口一度到 83.8%、一度只有 26.4% —— L1 执行需求仍在剧烈波动
- **同期 ETH 发行 ≈ 2,958 ETH/天**（CoinMetrics `IssTotNtv`，独立口径 2,961）→ **销毁/发行为 3.2%–5.0%**（ETH 处于**净通胀**状态）

**把这些数字放在一起，Q1 的答案浮现**：全网 blob 付费 **$150/天**，是**用户实付 L1 费用的 0.023%–0.040%**（区间两端分别对应自采实付 247–253 ETH/天与 CoinMetrics 口径 145.3–188.2 ETH/天的分母）、是每日发行价值的 **0.002%**；即使拿它去和**被销毁的那部分**（95–147 ETH/天，$245K–380K/天）比，也只有 **0.04%–0.06%**。**在今天这个价格与需求下，「继续扩 blob」在收入上找不到理由。**

### 3.4 那么答案是什么：三个可验证门槛，而不是一个 yes/no

Ethlabs 用「未来容量预期不清」来解释为什么要做 L2 需求调查 —— 我们同意这是当下**可执行的正确动作**，但要补三条我们的判断：

**① 上游约束是机制选择，不只是容量数字。** EF 之所以把 **EIP-8142（Block-in-Blobs）**列入 D 档（declined），理由是它「加深对 KZG 结构的依赖，与通往 J\* 的路径相冲突」；DA 路线表写着 **leanVM → PQ blobs**。**在承诺「继续扩容」之前，得先回答「扩的是哪种机制的 blob」** —— 因为 blob 的承诺结构（KZG）在后量子路线里正是被质疑的对象。这是周报没有涉及的层次。

**② 扩容应该写成「路径」而不是「事件」。** BPO2（2026-01-07）已经示范了机制：**不靠大版本 fork，而是靠 BPO 小步调 target**。正确的做法是把 target 阶梯与触发条件写清楚，让 L2 能据此规划（这正是 Derek 那份调查的用途）。

**③ 三个可验证门槛（作者自设的观测线，不是规范值，也不是投资建议）**：

- **门槛 A｜使用率**：连续 7 天平均 blobs/块 ≥ **9.8**（= target 的 70%）且空块率 < 10%
- **门槛 B｜价格**：blob base fee 30 天均值 > **0.05 Gwei**（写作时的约 15 倍），即价格真正进入有信号的区间
- **门槛 C｜需求预期**：L2 调查给出的**已承诺**（而非「希望」）需求总量，超过当前 target 的 100%
- **机制条件（三条之外的先决项）**：在 PQ 承诺方案定下来之前，扩容只走 **BPO 小步**、不新增信任假设；任何提出新承诺结构的大扩容，都要单独论证它不会成为返工项
- **使用方式上要注意一件事**：A 与 B 由同一套 EIP-4844 费用机制耦合，**不是两条独立证据** —— B 本质上是 A 的价格映射，真正的独立信号是 C（需求侧承诺）
- **→ 判定**：三条同时不为真时，扩 target 只是把闲置容量做得更大；而当 A/B 任意一条转真，扩容就从「保险」变成「必要」。

---

## 四、Q2：Quick Slots —— 方向正确，但周报高估了它的临近程度

### 4.1 EIP-8198 一手文本告诉我们什么

EIP-8198 做的事情比「把 12 秒改成 10 秒」大得多，也比它小得多：

- **大**：它把 `SLOT_DURATION_MS` 从编译期常量改为**运行时配置**，先把「改 slot 时间」的基础设施建起来，再做第一次下调。文件的措辞是「第一步建可变时机的机制，然后**保守地**下调 slot 时长作为非 headliner 变更」。
- **小**：它**不增加单位时间吞吐**。原文：*Block gas limits and blob parameters scale proportionally to maintain constant throughput per unit time.*（块 gas 上限与 blob 参数按比例缩放，以维持单位时间吞吐恒定。）具体地：
  - gas limit：`fork_gas_limit = 旧 gas limit × 新 slot 时长 ÷ 12,000` → **12→10 秒：60,000,000 → 50,000,000**
  - blob：`new_max_blobs = 旧 max × 新 slot ÷ 旧 slot` → **12→10 秒：21 → 17**；target 照惯例由 max 推导 → 约 **11**
  - 成效：**每块**容量下降，**每秒**容量不变
- **连带改动（说明这是一次系统性 retuning）**：`BASE_REWARD_FACTOR` 线性缩放以**保持年化发行不变**（整除去尾导致少发约 1.6%）；`INACTIVITY_SCORE_*`、数据处理窗口（rollup 挑战期按墙钟保持约 7 天）、`churn limits`（保持弱主观性周期）、`MIN_EPOCHS_FOR_BLOB_SIDECARS_REQUESTS`（4,096 → 6,144）都要跟着调。
- **文件自陈的知识缺口**：*Current understanding of blob propagation limits, attestation aggregation capacity, and local block building times remains incomplete.*（对 blob 传播极限、attestation 聚合能力、本地出块时间的当前理解仍不完整。）
- **一个细节差异**：EIP 文本里 8 秒是「合理的占位值」（12→8 秒则 gas limit 40M、max blobs 14），并说「即便 10 秒也是有意义的胜利」；而 Ethlabs 的生态文章主张**第一步走 10 秒**。两个数字不冲突，但说明**最终目标仍未定**。

### 4.2 官方评级 vs 周报呈现

**评级 —— 两套口径，不能相加**

- **周报口径**：引用客户端各自的 tier list，Teku **S**、Prysm/Lighthouse **A**、Lodestar **C**、Nimbus/Grandine **倾向不纳入**（不利项它也写了）；并提到 @jih2nn 在补规格、@terencechain 在做 Prysm 原型。
- **官方口径**：EF Protocol **B 档，均分 2/6**，理由原文「S/A 支持来自 R&D；**专注交付的工程团队给了 D**，理由是任何 slot 时间改动背后的 **retuning 级联**」。两份清单的**人口不同**：一边是各客户端团队自评，一边是 EF 统一评级（含 R&D 与交付工程团队），**把它们当成同一把尺子相加本身就需要论证**。

**状态 —— 周报口径 vs 官方口径**

- **周报口径**：「两周后 ACDC 讨论升级为 Consider for Inclusion」。
- **官方口径：四项前置，缺一不可**
  - ① 覆盖核心协议全部预期改动的规格
  - ② 实现全规格的原型
  - ③ 对全生态下游影响的深度评估
  - ④ 签署确认它**不复杂化分权共识** —— 官方注明这一条**要等规格存在后才判定**
- **进度对照（对 ②③ 的直接证据）**：规格侧由 @jih2nn 复核、原型侧由 @terencechain（Prysm）推进 —— 这正是前置 ②③ 的进度条，值得跟踪。

**语气**：周报：*Given the support from the ecosystem, we'll be pushing hard…*。官方：*The bar is set where it is because…*（门槛之所以这么高，是有原因的）。

**我们的判断**：Quick Slots 的**方向**是对的（延迟是可感知的痛点，EIP 文本引用「套利损失随时长的平方根缩放」，12→8 秒可减少约 18% 的套利损失；MEV 提取随 slot 缩短被压缩；preconfirmation 协议本质是在给 12 秒打补丁 —— 三者都支持「缩短 slot 是治本」）。但它当前的官方位置是 **B 档 + 四项前置 + 工程团队 D 评级**，其中第四项前置在规格完成前**无法判定**。所以：**两周后 ACDC 把它推进到「Consider for Inclusion」是可能的，把它当成「Hegotá 会包含」则是过度外推。** 对读者的实际含义：**12 秒 → 10 秒这件事，在 2027 年内落地的概率，取决于规格与原型能否在几周内补齐；这比周报的语气要远。**

---

## 五、Q3：原生账户抽象 —— 表层是 UX，底层是后量子

### 5.1 官方定性：8141 上 S 档的**理由是安全**

EF Protocol 文件对 **EIP-8141（Frame Transactions）** 的评级理由是逐字可查的：*Native account abstraction on security grounds: a path to PQ signature schemes without a fork per scheme, aggregation so PQ verification can be priced, and a route to retiring k1 keys.* —— **安全理由的原生账户抽象：为 PQ 签名方案提供不需要逐方案分叉的路径、用聚合让 PQ 验证可定价、以及退役 k1 密钥的路径。** 它随 **EIP-8250（Keyed Nonces）** 与 **EIP-8272（Recent Roots）** 一起构成 Frames 核心；扩展包 **EIP-7906 + EIP-8298（`SETCODEFROM`）+ EIP-8151（受账户代码限制的 ecRecover）** 被描述为「给账户一条**完整地离开 k1 的路径**」。

这与周报的表述完全对得上（周报提到的 `SETCODEFROM` 委托、作废退役 ECDSA 密钥，正是这个扩展包），但**周报没有把「为什么现在做 AA」的答案是安全**这件事说出来。而 8141 的作者在 Magicians 帖里给了一个很硬的动机：今天有若干可用于保护以太坊账户的 PQ 密码系统，「**没有任何一个明显领先到足以让我们放心直接写进协议**」—— 所以选择**用 AA 作为实现 PQ 韧性的机制**，而不是 enshrine 单一 PQ 方案。

**配套证据（EF 官方 PQ 路线）**：共识层用**基于哈希的签名（leanXMSS）替换 BLS**，用**基于 SNARK 的聚合 + 极简 zkVM（leanVM）**恢复可扩展性；路线分级 `I* PQ key registry → J* PQ sig precompiles → L* PQ attestations / leanVM → M* PQ sig aggregation / PQ blobs`；官方时间表原文：「**没有单一固定日期……L1 协议升级可能到 2029 年完成，执行层的完整迁移还要再花数年**」。自陈的代价：签名更大（带宽/存储上升）、验证更重（可能推高验证者运营成本）、BLS 的聚合没有 PQ 对应物。

**→ 结论：原生 AA 的收益是刚性的（PQ 迁移通道）。** 它有 UX 收益，但**它被排进 fork 的理由不是 UX**。

### 5.2 成本：两个标准并行，代价落在钱包

周报用了一句非常平静的话过渡：「**Following the resolution of a few weeks spent aligned two distinct account abstraction proposals, EIP-8130 and EIP-8141…**」（在花了几周把两个提案对齐之后……）。而公开记录显示，那几周的「对齐」结束于**一次谈崩**：

- **Unchained（2026-09-15）**报道《Ethereum and Base Abandon a Shared Wallet Standard as Account-Abstraction Talks Break Down》，具名引述 Ethlabs 开发者 **Derek Chiang**：
  - 「While we identified a number of technical solutions, they all required one side or the other to compromise at least a little bit on their core goals.」（我们确实找到了一些技术方案，但每一个都要求某一方在自己的核心目标上让步。）
  - 「**So separate ways we went, putting the burden on wallets to deal with the fragmentation that ensues.**」（于是我们各走各路，把随之而来的碎片化负担留给钱包。）
- 报道同时指出：8141 带 **must-ship** 标记（与 EF 官方 S 档一致），而 8130 由 **Base protocol** 主导推进。

**两个提案的技术差异，正好解释了为什么会谈崩**：

- **EIP-8130「Keystore Accounts」（Coinbase / @chunter-cb，2025-10-14，Draft）**：**声明式**。验证 = 节点查询链上 Keystore 并调用**已声明**的 canonical authenticator 合约，**钱包代码不在验证期执行**；**不新增 opcode**。
- **EIP-8141「Frame Transaction」（2026-01-29，Draft；作者含 Vitalik、lightclient、fjl、Derek Chiang）**：**执行式**。验证 = **执行账户自己的 EVM 代码**（VERIFY frame），依靠 `APPROVE` + mode/flags 的结构让协议对任意验证逻辑做资源界定与 p2p 规则；**新增多个 opcode**；账户最终「就是一个有代码的地址」。

**这是两种控制哲学**：8130 把控制点放在「canonical authenticator 集合」，8141 放在「用户自定义 + 协议内省」。二者都能通向 PQ，但**迁移路径与安全论证不可互换**。

**我们的判断**：周报写清了两件事 —— 焦点已从「调和提案」转向「迁移流程」，以及 personas-and-user-stories、unified plan for wallet support 这些动作。但它**隐含承认了分裂，却没有给出成本量级**：在 8130 与 8141 并行的世界里，**钱包要同时支持两套格式**（周报自己提到的「跨 EIP-8130 与 EIP-8141 可移植的账户标准」和 cosigner 议题，实际上就是对这种碎片化的补丁）。**读者从周报读不到这个量级 —— 而公开说出这句话的，正是 Ethlabs 自己的开发者。**

**利益相关披露（本文必须自报）**：周报的作者团队同时是 **EIP-8141 的作者方之一**（Derek Chiang 在 8141 作者名单中）。**本文对周报的每一处引用都做了独立核实**（EIP 原文、EF 官方文件、具名媒体报道三路交叉），但读者应当知道这层关系存在。

---

## 六、Q4：FCR 与快速最终性 —— 三个百分比数字错在哪

### 6.1 FCR 到底是什么（一手）

- **它不是一个新的最终性机制，而是一条确认规则**：节点**每个 slot 开头**运行算法，基于**已观测到的 attestation 权重**判断某区块是否「永远留在规范链上」。规范位置：`specs/phase0/fast-confirmation.md`（`FastConfirmationStore`、`get_latest_confirmed`）。
- **它解决多少时间**：FFG 最终性最佳情形 **13–19 分钟**（论文另一处给 12.8 / 19.2 分钟，取决于交易落在 epoch 内的时点）；**FCR 最佳情形 12 秒 = 一个 slot**（EF 官方表述约 13 秒）。**约一个数量级的改善。**
- **它的假设与安全边界（必须一起引用）**：① 网络同步假设 —— 诚实验证者在某 slot 产生的 attestation 在该 slot 结束前送达（EF 口径即**网络延迟 < 8 秒**）；② **诚实质押占比 ≥ 75%**（注意：**安全阈值是 3/4，不是 2/3**）。规范原文警告：**若该假设被破坏，被确认的区块「可以在没有任何对手行为、没有任何罚没的情况下被重组」**。FCR 的定位是**最终性的补充，不是替代**；可容忍异步的最终性仍是 fallback。
- **为什么闸门在 RPC**：多数应用与 L2 是通过 RPC 端点看以太坊的，能否用上快速确认取决于端点暴露什么。周报说的 `safe` tag 迁移路径（部分应用已依赖它做 justification）是真实的兼容性工程问题。
- **本文认为最被低估的一条**：周报提到「**可以用简洁 zk 证明证明某区块已被快速确认**」，且「手上已有修改后的 Lean 证明」。这条把 FCR 从「你信任节点说的话」推进到「**你可以验证这条确认**」，与 EF 在 PQ 路线里同时推进的 **leanVM / zk 实时 CL 证明（L\*）** 是同一技术栈方向。它比三个百分比数字更值得关注。

### 6.2 三个提速数字：口径没标，且与公开材料的「1/6」不是同一件事

周报的推导链是：现有共识**每 6.4 分钟**（= 32 slots × 12 秒）检查一次最终性，而最终性实际上在 2/3 验证者投票时就已获得 → 分权共识下可以**每 slot 检查 2/3 阈值** → 「时延最多减少 **1/6**」；再让**质押更重的验证者先投票** → 「再减少 **1/6** 或更多」；再**把 justification 也提前处理** → 叠加后「**整体改善超过 50%**」。

**我们做了三项核对**：

**(a) 算术对不上**〔A〕：若两项各自是 −1/6，复利后为 `1 − (5/6)² = 30.6%`。要得到「>50%」，第三项（提前 justification）必须单独贡献约 **29%**。周报用「or more」留了余地，但**没有任何一项给出可复算的推导**。

**(b) 公开一手材料的「1/6」是另一种语义**〔A〕：EF 官方 finality 博客系列第二篇（Ben Edgington，配套 stakeholder research）原文：*One possible route to faster finality is to use a single round of voting rather than the traditional two. That could roughly halve time to finality, but might reduce the adversarial tolerance from today's one-third to something like one-fifth or one-sixth, depending on the design.* —— **单轮替代双轮：时延约减半，代价是对抗容忍度从 1/3 降到约 1/5 或 1/6**；同一篇还写明「**Support for making that trade-off was weak at this stage**」，并判断单轮最终性「仍是有趣的选项，但**不是第一个该拉的杠杆**」。

**(c) 基线算术**〔A〕：现状最小 TTF = 2 × 32 slots × 12 秒 = **768 秒**；计入平均等待期望约 **960 秒**。1/6 × 768 ≈ **128 秒 ≈ 10.7 个 slot**。**这里我们不做量级断言**：周报的 1/6 究竟对应哪一种机制（省掉 epoch 边界的等待？取消一轮投票？重验证者先投票带来的偏斜？），**要拿到推导才能判定** —— 我们检索到的公开材料没有一份能把这三个数字复算出来。

**→ 我们的处理**：把周报的三个数字标注为「**Ethlabs 内部推导，未检索到公开一手出处**」。需要说清楚的是**批评的落点**：周报自陈这是在 *arrive at their own understanding*（形成自己的理解），属于内部探索性估算 —— **内部估算本身没有问题，问题在于它用陈述语气给出、且没有标注这是内部估算**，读者会当成公开结论使用。引用时请**同时给出公开的对照口径**（单轮 → 时延减半、容忍度降至 1/5~1/6）。**两种 1/6 绝不能混用。**〔C〕

### 6.3 分权共识：把权衡摆上桌，是这一周最有价值的公开动作

@fradamt 的 ethresear.ch 帖（2026-03-28）指出：现行协议把**出块时间线与最终性时间线耦合**（每个 slot 一个 1/32 验证者集的大委员会在关键路径上投票）。缩小委员会可加快 slot 但**拖慢最终性**（一轮要累积 64 个 slot 而非 32），放大则反之 —— 而 SSF/3SF 各变体**不改变这个权衡**，只是选在「全体验证者每 slot 投票」那一端（前提是验证者集通过 consolidation 缩小）。**解耦**（出块用小的随机采样委员会 + 最终性流水线并行、不在关键路径上）才可能消除这个权衡。周报说「所有性质都已形式化验证通过、Lean 仓库在清理与审计」，与 Week 12 的「恢复性质已验证」是连续进展。

**同一周报体系里，最重要的反对意见来自 EF 自己的 stakeholder research（19 个个案访谈，覆盖 L2/桥/支付/钱包/solver/预言机/质押服务/客户端/研究者/机构）**，其中一段值得逐字引用（作者个人目标原话）：

> *My personal goal is to achieve fast-enough finality **without compromising the diversity of the validator set**... at some point we might need to weigh the merits as a community of even faster finality **at the cost of reducing staking diversity**.*

（这位受访研究者自述的目标：在**不牺牲验证者集多样性**的前提下实现足够快的最终性……到某个时点，社区可能需要在两者之间权衡：是否用**降低质押多样性**来换取更快的最终性。）

报告还给这个担心配了数量级：单轮最终性把容忍度降到 1/5~1/6 后，「**一家主要交易所、质押池、托管方，甚至一个客户端软件 bug，就可能接近 17–20% 的质押阈值**」；并强调「**一百万个验证者索引不等于一百万个独立参与者**」。

**→ 我们的判断：这两条线的安全性是「条件性中性」，不是「天然中性」。** 条件是：以 consolidation（验证者集缩小）为前置，并且需要验证者集多样性的论证。写清楚这一点很重要 —— 周报的第二项提速「让**更重的验证者先投票**」**本身就依赖 consolidation**，而上面那段引文担心的正是 consolidation 对多样性的挤出效应。**换句话说，同一份 stakeholder research 既反对单轮路线，也对分权路线提出了条件。**（这里的担忧与第五节有一个交叉点：PQ 路线本身会推高验证成本 —— 更大的签名、更重的验证 —— 而验证成本上升正是 consolidation 压力的来源之一。两条线不是独立的。）

**→ 所以正确的区分是**：**解耦路线（条件性中性：需要 consolidation + 多样性论证）vs 单轮路线（用安全换速度）**。**这就是为什么 EF 官方说单轮最终性「不是第一个该拉的杠杆」。**

---

## 七、把四条线接起来：一个排序，以及它为什么不是我们的偏好

**① 所有性能议题共享同一份 headroom —— 而这是 Ethlabs 自己给出的框定。** 周报（Week 12）原话：headroom 可以换成「更多容量、更短 slot、更低节点要求，或组合」。**所以「继续扩 blob」与「缩短 slot」在容量维度上不是加法，是替代。** 这里要划清证据边界：**「缩短 slot 会占掉容量」的直接依据是 Ethlabs 的这份表述**；EIP-8198 的按比例缩放条款（blob 上限 21→17、gas limit 60M→50M）**说明的是另一件事** —— 为什么缩短 slot 不增加每秒吞吐。两者都成立，但不是同一条证据，不能互相替代。

**② 容量决策被机制选择约束。** DA 路线上写着 leanVM → PQ blobs，而「加深 KZG 依赖」的设计（EIP-8142）已进入 **D 档（declined）**。**在 PQ 承诺方案定下来之前大幅扩容量，存在未来返工风险** —— 这正是 EF 对 EIP-8321（Hash-Chain RANDAO）给出的同类理由：「在完整 PQ 共识设计之前先硬化单个组件，会有返工风险」。两条都出自同一份 tier list，档位语义一致（D = declined，附理由），不要把它读成对技术价值的判断。

**③ 安全议题是刚性的，性能议题是可排序的 —— 这就是中心判断的来源。** 8141 在官方文件里是 **locked-in EL headliner**（must-ship）；8198 是 **B 档 + 四项前置**，其中第四条要等规格存在才能判定。**把两个评级并排看，EF 的排序自己就出来了：后量子通道 > 延迟改善 > 容量扩张。**

**④ 但请先掐掉一个误读：这个排序不是「EF 官方宣布安全优先」。** EF 自己的优先级清单（Week 12 引用）顺序是**抗审查 > 更快 > 性能工程 > 原生 AA** —— 原生 AA 排在最后。两件事不矛盾：**优先级清单说的是「投入顺序」，S/B 档说的是「能不能延后」。** 8141 在投入顺序上靠后，在可延后性上是不可延后的；8198 恰好相反。这个区分之所以重要，是因为它决定了读者该**按什么节奏**跟踪：AA/PQ 的进展看**工程与规格推进**（8141 的 EIP 头部状态、PQ 路线分级 I\*→M\*），性能议题的进展看**门槛触发**（§3.4 的 A/B/C 与 ACDC 的前置条件）。

**⑤ 周报的价值与偏差。**〔A〕 价值：它把生态侧的真实需求（20+ 团队的引述、钱包迁移流、RPC 采纳路径）带进协议讨论，这是 Ethlabs 的独特贡献。偏差有三处，而且都不算重：**Quick Slots 上没同置 EF 统一评级与四项前置；AA 上隐含承认分裂但没给成本量级；最终性上给出未标注为「内部估算」的三个百分比。** 读它的正确方式是：**看它列出的工作项（真实、具体、可跟踪），把它的语气打折。**

**下一个真正有信息量的时点是两周后的 ACDC。** 在那之前，本文的四条判断都可以用 §3.4 的三个门槛跟踪；而如果 ACDC 把 8198 提为 Consider for Inclusion，需要改变的不是「延迟不重要」，而是**这一条的时间表**：排序不变，节奏提前。

---

## 八、市场含义（机制层面，不构成交易信号）

**1｜blob 叙事对 ETH 现金流的影响，当前可忽略。**

blob 付费 $150/天 ≈ **用户实付 L1 费用的 0.03%** ≈ 每日发行价值的 0.002%。ETH 处于**净通胀**：销毁 **95–147 ETH/天** vs 发行 2,958 ETH/天，**覆盖率 3.2%–5.0%**。这里还有一个常被忽略的结构事实：**用户实付的钱里小费占 41%–66%，即每天约 100–167 ETH 直接进了验证者口袋，被销毁的只是其中一部分**。**「blob 扩容 → ETH 更通缩」这条叙事在今天的算术下不成立**；真正能改变 ETH 现金流的是 L1 执行需求（窗口填充率 26%–84% 剧烈波动）与**发行政策**（EIP-8363 Tapered Issuance Burn 被列为 D 档 —— 但 EF 明确说明这是「**分类而非对其价值的判断**」，发行政策属于更大的生态流程，不在这个 fork 的裁决范围内）。

**2｜slot 缩短是「发行中性」的，别当供给冲击读。**

EIP-8198 明确要求 `BASE_REWARD_FACTOR` 线性缩放以**保持年化发行不变**（整除去尾导致少发约 1.6%）。因此 12→10 秒落地**不改变年化发行曲线**；它对市场的作用是**延迟与交易体验**（套利损失随 √时长 缩放，12→8 秒约减 18%；MEV 被压缩），不是供给。

**3｜值得跟踪的三个日历与观察点（非投资建议）**：

- **ACDC（约两周后）**：Quick Slots 是否从 Proposed for Inclusion → Consider for Inclusion；这是本议题下一个真正有信息量的事件
- **L2 blob 需求调查结果**（Derek 外联中）：它直接决定下一个 BPO 的 target，是「未来容量预期」第一次变成数字
- **BPO / Hegotá 时间线**：Hegotá 预计 2027 Q2（Fusaka 之后的执行层+共识层合成升级）；PQ 的官方口径是「L1 协议升级可能到 2029 年完成，执行层迁移还要再花数年」

**4｜风险与推翻条件**（我们看到的、可能推翻本文判断的情形）。前两条挂在子判断上，后三条专门用来检验中心判断 —— 它们都是**可观测、可证伪**的：

- **子判断｜blob 需求非线性跳升**（例如某条大链把数据可用性从 calldata 全量切到 blob、或新一批 appchain 上线）→ 使用率可能在一个季度内从 35% 跳到 80%，本文「边际收益≈0」的结论随之失效
- **子判断｜slot 缩短在生产中暴露传播/聚合瓶颈**（EIP 自陈理解不完整）→ 可能反向压制容量议程
- **中心判断｜推翻条件 1**：Hegotá 最终范围公布时**不含 8141**，或它的 S 档理由被改述为非安全理由 → 「安全议题刚性」失效。**观测点**：EF Protocol 后续文件、EIP-8141 头部状态
- **中心判断｜推翻条件 2**：8198 进入 CFI，且四项前置（尤其第四条）在规格完成前被明确豁免 → 「周报过度外推」的判断失效。**观测点**：ACDC 会议纪要
- **中心判断｜推翻条件 3**：PQ 路线的执行层迁移时间表被推后到 2030 年后 → 「通道比延迟更刚性」的逻辑前提被削弱，排序可能重排。**观测点**：pq.ethereum.org 的路线分级与官方时间表更新

---

## 九、口径、证据分级与未解项（诚实清单）

**证据分级**：

- **A 级（一手规范/官方/链上实测）**：EIP-8198 全文；EIP-7910 `eth_config` 参数；`eth_blobBaseFee`；自采 511 块 blob 用量与 L1 费用；EF Protocol 官方 tier list（blog.ethereum.org，2026-09-07，含 8142/8321 的 D 档理由）；EF 官方 finality 博客系列与 stakeholder research；ethresear.ch 分权共识帖；consensus-specs FCR 规范；EF PQ 页面（pq.ethereum.org）；EIP-8130/8141 原文与 Magicians 帖
- **B 级（具名媒体报道/独立数据商）**：Unchained（2026-09-15，AA 谈判破裂，含 Derek Chiang 具名引述）；growthepie fundamentals API（blob 费用/数据量/L1 成本）；CoinMetrics（发行量）
- **C 级（周报自述、未取得公开一手出处）**：三个提速百分比（−1/6、−1/6、>50%）的推导；「两周后 ACDC 升级 CFI」的把握度

**未解项（如实列出，不作为结论依据）**：

1. **`excessBlobGas` 更新恒等式异常**：在本窗口自采数据中，头部 `excessBlobGas` 的逐块变化量不等于 `blobGasUsed − target_gas`，而是高度接近 `blobGasUsed / 3`；且该字段值代入经典 EIP-4844 价格公式会得到比实测高约 10 个数量级的价格。**结论**：BPO2 之后的 excess 记账口径与经典公式不一致（费率分母已确认改为 11,684,671 = 3,338,477 × 3.5），**具体更新规则本文未取得规范文本，因此凡是支撑结论的推导都不用 `excess`**；本文价格一律取自 `eth_blobBaseFee` 实测，以及与该值对账一致的 `exp(excess/fraction)` 关系。
2. **周报自引的「20+ 团队」生态文章**未逐家核验（文章由 @binji_x / @barnabemonnot 署名，本周四发布）。
3. **本报告的 blob 用量与 L1 费用为快照口径**（2026-09-20）：blob 用量取自 511 块窗口；L1 费用结构取自两个各 24 块的 receipts 直测窗口 + CoinMetrics 5 日序列。base fee 在当日波动剧烈（0.056 → 0.264 Gwei），区块填充率在 26%–84% 之间跳变，因此 L1 费用与销毁数字必须按「区间」读，不能当稳定值。
4. **区间端点的口径说明**：第 3.3 节的两个比值区间是**换分母算出来的，不是不同窗口的实测差** —— blob 费 149.58/天 除以自采实付（247–253 ETH/天）得 0.023%，除以 CoinMetrics 口径（145.3–188.2 ETH/天）得 0.032%–0.040%；除以被销毁量（95–147 ETH/天）得 0.04%–0.06%。读者可以按自己认可的分母重算。
5. 上一篇文章给出的「全网每天 Blob 费用约 $62」与本文的 **$149.58/天** 有差异，来自**窗口与口径不同**（当时为单日单档快照，未含 MegaETH/Celo 等新链；本处为 7 天累计 ÷ 7），并非数据修正。
6. **EIP-8142 / EIP-8321 的「拒掉/降档」表述**：两者均出自同一份 EF tier list 的 D 档条目（D = declined，附理由），本文的「已被拒绝」据此；**未取得 EF 对这两条 EIP 的独立说明文档**。
7. **本报告的一次自我更正（留痕）**：初稿曾用 `eth_feeHistory` 的 **p50 小费**（0.037 Gwei）近似「有效 gas 价」，据此得出「含小费总费用 19 ETH/天」——**该数字错误，低估约 9 倍**。原因：在超低 base fee 环境下，用户实付由**小费主导**（有效 gas 价 0.64–2.01 Gwei，是 base fee 的数倍到十倍），p50 小费不能代表实际支付价。已改用 **`eth_getBlockReceipts` 逐笔直测**（Σ gasUsed × effectiveGasPrice）重算，并与 CoinMetrics `FeeTotNtv`（近 5 日 145–188 ETH/天）交叉验证后修正为 **247–253 ETH/天**，全文相应结论（blob 占比 0.30% → **0.03%**、销毁覆盖率 0.39% → **3.2%–5.0%**）已同步改写。**结论方向不变，但量级修正一个数量级。**
8. **v1.1 的一处口径修订（留痕）**：v1.0 写「两个独立口径在 ±5% 内吻合」，实为 **+5.4%**（37.4k vs 35.5k）→ 已改为「偏差约 5%」；v1.0 写 blob 费/销毁「0.05%–0.06%」，按区间端点应为 **0.04%–0.06%** → 已修正；v1.0 写小费「约 100–147 ETH/天」，与 41%–66% 的占比不自洽，按两个窗口各自重算应为 **约 100–167 ETH/天** → 已修正。

---

## 十、附录：复现方式与来源

**复现脚本（本地 Python，输出与下文每个数字一一对应）**：

- `blob_infer2.py` —— 分块抓链上区块，统计 blob 用量/利用率/空块率
- `eth_config.py` —— EIP-7910 `eth_config` 取 target/max/fraction
- `blob_price.py` —— `eth_blobBaseFee` 与 excess→价格恒等式对账
- `fee_truth.py` / `fee_structure.py` —— `eth_getBlockReceipts` 逐笔直测用户实付（Σ gasUsed × effectiveGasPrice）、基础费销毁、小费占比、blob 费（输出 `/tmp/blob/fee_structure.json`）
- `econ_summary2.py` —— L1 费用池 + growthepie 的 L2→L1 付费汇总（输出 `/tmp/blob/l1_l2_econ.json`）
- `qa_stage05.py` —— 本稿的算术闭合校验 + 实时 API 复核（25 项断言：百分比重算、单位换算、引文核对、实时价格/用量对照）
- `eip8198.md` —— EIP-8198 全文（本地副本，151 行）

**主要来源**：

- Ethlabs Week 13（2026-09-20）：`https://x.com/ox_shaman/status/2101655774233592281` → `https://x.com/i/article/2101653240794255360`
- EF Protocol tier list（含 7805/8141/8198/8142/8321/8363 的档位与理由）：`https://blog.ethereum.org/2026/09/07/protocol-hegota-eips`｜路线页：`https://ethereum.org/roadmap/hegota/`
- EIP-8198：`https://raw.githubusercontent.com/ethereum/EIPs/master/EIPS/eip-8198.md`
- EIP-8141：`https://raw.githubusercontent.com/ethereum/EIPs/master/EIPS/eip-8141.md`
- FCR 规范：`https://github.com/ethereum/consensus-specs/blob/master/specs/phase0/fast-confirmation.md`
- FCR 论文：`https://arxiv.org/html/2405.00549v4`
- 分权共识：`https://ethresear.ch/t/unblocking-faster-finality-with-decoupled-consensus/24527`
- EF finality 博客：`https://consensus.ethereum.foundation/blog/upgrading-finality-edition-2`｜stakeholder research：`https://consensus.ethereum.foundation/articles/stakeholder-research`
- EF PQ：`https://pq.ethereum.org/`｜`https://ethereum.org/roadmap/security/quantum-resistance/`
- AA 分裂：`https://unchainedcrypto.com/ethereum-and-base-abandon-a-shared-wallet-standard-as-account-abstraction-talks-break-down/`
- 数据：`https://api.growthepie.xyz/v1/fundamentals.json`｜`https://community-api.coinmetrics.io/v4/timeseries`｜执行层 RPC（`ethereum-rpc.publicnode.com`）

**相关前作**（同一研究线）：《谁在给以太坊交租：Aztec、Robinhood Chain 与一次被误读的算术》（2026-09-20，南野东亦），`https://poorshan.github.io/zk-labs-research/observations/2026/09/20/l2-rent-who-pays-ethereum.html`

---

*ZK Labs Research｜本文为公开研究文稿，不构成投资建议。*
*证据冻结时点：2026-09-20（CST）｜v1.1（三路独立审核后修订）*
