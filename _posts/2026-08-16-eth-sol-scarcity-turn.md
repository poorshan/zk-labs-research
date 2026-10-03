---
layout: default
title: "ETH 与 SOL 的稀缺性转向：两条链的减产提案与 Grayscale 的 2031 展望"
permalink: /observations/2026/08/16/eth-sol-scarcity-turn.html
date: 2026-08-16
categories: observation
author: 南野东亦
data_cutoff: 2026-08-16
version: "v1.0"
tags: [ETH, SOL, tokenomics, supply, inflation, Grayscale, EIP-8363, SIMD]
description: Grayscale 测算 ETH 与 SOL 的供应通胀可能在 2031 年分别降至 0.4% 与 1.1%，双双低于黄金和 CPI。两条链的减产提案看似技术细节，实则是加密资产稀缺性叙事的一次转向。
refs:
  - X post: Grayscale (@Grayscale), "Ethereum and Solana could be getting scarcer" (2026-08-14)
  - Grayscale The Stack: "Ethereum and Solana Tokenomics Under Review"
  - EIP-8363: ethereum/EIPs PR #12081 (2026-08-04)
  - CoinDesk: Solana SGP-0003 / SIMD-0553 + SIMD-0550 报道
  - ZK Labs Research: EIP-8363 系列观察 (2026-08-07 / 2026-08-09)
---

> *两个网络、两套提案、同一个方向——让代币变得更稀缺。2026 年 8 月 14 日，Grayscale 的一条推文把以太坊和 Solana 并排放在了一张「稀缺性」的桌面上。*

---

## 一、事件：Grayscale 把两条链放上了同一张桌

2026 年 8 月 14 日，加密资产管理机构 Grayscale 在其官方 X 账号（@Grayscale）发布推文，原文如下：

> "Ethereum $ETH and Solana $SOL could be getting scarcer. New proposals on both networks aim to burn more tokens and cut inflation, reducing future supply. If they pass, annual inflation for ETH and SOL could fall below gold (1.8%) and U.S. CPI (3.3%) by 2031."

**译注**：以太坊与 Solana 可能正在变得更稀缺。两个网络上的新提案都旨在烧掉更多代币、削减通胀，从而减少未来供给。如果它们通过，到 2031 年，ETH 与 SOL 的年通胀率可能双双降至黄金（1.8%）与美国 CPI（3.3%）以下。

这条推文背后是 Grayscale 研究团队「The Stack」栏目的一篇 tokenomics 专题报告[^1]。它的核心测算结论是：

| 资产 | 2031 年供应通胀（Grayscale 测算） | 参照基准 |
|:--|:--|:--|
| **ETH** | ~0.4%（对齐比特币） | 低于黄金 1.8% |
| **SOL** | ~1.1% | 低于黄金 1.8%、低于 CPI 3.3% |
| 黄金 | 1.8% | — |
| 美国 CPI | 3.3% | — |

> 说明：上表数字来自 Grayscale 报告的公开转述（二手源交叉验证）[^2]，为「若提案通过」的**情景测算**，而非已实现的通胀数据。这正是本文要划清的一条线。

---

## 二、两条链，两个提案，一个方向

两个网络的减产提案，机制截然不同，但方向一致：**降低新增供给的斜率**。

### 以太坊侧：EIP-8363「Tapered Issuance Burn」

EIP-8363 于 2026 年 8 月 4 日以 PR #12081 提交，六位作者中包括以太坊基金会核心研究员 **Justin Drake**[^3]。它的做法不是改手续费，而是**直接烧掉一部分验证者奖励**——烧多少取决于质押率：

$$b = (D / D_{sat})^{3/2}$$

其中 $D$ 是当前质押率，$D_{sat}$ 是饱和点（约 50% 供给）。质押越多、烧得越狠，到 50% 质押率时，100% 的新增奖励被烧掉，净收益归零。

> 数据：以太坊当前净通胀约 **0.5%/年**（已计入 EIP-1559 的基础费燃烧）。EIP-8363 的目标是把净发行进一步压向 ~0.4% 区间，与比特币的长期供给曲线对齐。[^4]

### Solana 侧：SGP-0003（SIMD-0553 + SIMD-0550）

Solana 的方案是打包提案 **SGP-0003**，捆绑两个 SIMD[^5]：

| 提案 | 内容 |
|:--|:--|
| **SIMD-0553** | 引入资源型交易手续费，且手续费 **100% 全部销毁** |
| **SIMD-0550** | 将年度通缩率（disinflation rate）**翻倍** |

据 CoinDesk 报道，若落地，Solana 的日销毁量将从约 **650 SOL（约 4.7 万美元）** 跃升至 **7,500–9,000 SOL（约 65 万美元）**，放大 **14 倍**[^6]。该提案已于 8 月 4 日通过初步治理支持阶段、进入讨论期，仍需约 4,000 万 SOL 的验证者投票。

---

## 三、关键前提：三个「如果」不能省略

Grayscale 推文的原句里，最容易被忽略的两个词是 **"If they pass"**（如果它们通过）。围绕这句话，有三个必须划清的边界：

**① 都是提案，不是既成事实。** 两个方案目前都处于治理流程的早期。ETH 侧 EIP-8363 尚在论坛讨论阶段，SOL 侧 SGP-0003 还需巨量验证者投票。任何「ETH/SOL 即将通缩」的标题党表述，都混淆了「提案」与「落地」。

**② 情景测算 ≠ 实际收益。** Grayscale 的 0.4% 与 1.1% 是建立在「提案通过、且通过后按设计运行」之上的情景推演，附带了明确的时间限定（2031）。它不是对 2026 年当下通胀的陈述。

**③ 是多年的结构变化，不是短期催化。** 即使一切顺利，从提案到落地、再到对供给曲线产生可观测影响，是以年为单位的进程。它对短期价格/波动率的影响，远不如一个 FOMC 决议或一次硬分叉节点来得直接。

---

## 四、治理温度的差异，才是这张桌下真正的分歧

两个提案并置时，最值得注意的不是它们「都要减产」，而是它们**面临的政治环境截然不同**：

- **ETH 侧：争议激烈，机构公开反对。** EIP-8363 在 Ethereum Magicians 论坛引发 63 条讨论帖、四派分裂。8 月 9 日，SharpeLink CEO **Joseph Chalom** 公开表示「错误提案，错误时机」（"Wrong Proposal, at Exactly the Wrong Time"），理由是「稀缺性应来自真实需求驱动的基础费销毁，而非治理投票人工制造」，并警告此举可能在机构大规模入场时动摇经济基础的可预期性。[^7]

- **SOL 侧：社区支持相对更广。** 按 Grayscale 报告的说法，Solana 的提案「拥有更广泛的社区共识」。这或许与 Solana 通胀起点更高、以及手续费全烧这一机制更接近「市场化稀缺」而非「人工调参」有关。

> 判断（作者观点，非事实）：两条链的减产叙事，**可信度与落地节奏并不对称**。ETH 侧方向已开启 Overton 窗口、但短期落地阻力大；SOL 侧机制设计争议较小、但同样取决于验证者投票的政治算术。把二者等量齐观，会高估 ETH 侧的确定性、低估 SOL 侧的进展。

---

## 五、市场含义：结构性叙事，而非即时信号

把这条叙事放回「供应—需求—波动率」的框架里，可以得到三点克制但有价值的观察：

**① 供应叙事是长期底色，不是短期扳机。** 一个每年只改变 1–2 个百分点的发行率，其作用是通过复利在多年维度累积，而不是在单日改变供需平衡。它对长期持有者的稀缺性预期有意义，对短期 IV 的直接推动有限。

**② 真正的波动率节点，在「投票」和「硬分叉」。** 供应提案真正能搅动短期波动率的地方，不是提案发布日，而是治理投票日、硬分叉激活日这类离散事件节点。这些才是需要进日历、需要关注 IV Rank 时点的时间窗。

**③ 供给曲线的「抵押品定价」传导，值得持续跟踪。** 对 ETH 而言，质押收益率是 LST/杠杆质押/借贷市场共同的定价锚。若 EIP-8363 真将质押收益腰斩，其影响会沿着 DeFi 的抵押品链条向外扩散——这与 Solana 侧「手续费销毁」的传导路径是不同的风险结构。

---

## 六、结论

Grayscale 这条推文的价值，不在于它给出了两个精确到小数点后的通胀数字，而在于它**把「加密资产可以变得更稀缺」从一个链的单独叙事，提升为多链并行的结构性方向**。

但叙事转向 ≠ 事实落地。ETH 与 SOL 都还站在「如果通过」的这一侧，中间隔着治理流程、社区博弈和以年计的时间。对于观察者而言，最该做的事不是为 2031 年的通胀率下注，而是：**盯住每一个投票与硬分叉节点，看清两条链在「人工稀缺」与「市场稀缺」之间的路径差异。**

> **数据完整性声明**：本文事实层数据（提案编号、机制参数、日期、Grayscale 测算数字）均来自文末来源表所列公开资料，并经一手/二手源交叉核验；Grayscale 报告原文受访问控制限制，其 0.4%/1.1% 测算数字取自公开转述（Blockonomi、CoinAlertNews）并交叉一致。文中「判断」「作者观点」为作者独立推论，与事实层显性区分。数据截止 2026-08-16。

---

## 来源表

[^1]: Grayscale, "Ethereum and Solana Tokenomics Under Review", The Stack. https://www.grayscale.com/the-stack/ethereum-and-solana-tokenomics-under-review
[^2]: Blockonomi, "Why Ethereum and Solana Supply Growth Could Drop Sharply by 2031: Grayscale"; CoinAlertNews 同题报道（交叉一致）。
[^3]: EIP-8363 "Tapered Issuance Burn", ethereum/EIPs PR #12081. https://github.com/ethereum/EIPs/pull/12081
[^4]: ZK Labs, 《EIP-8363 信号：以太坊是否关上「无限质押」的大门》(2026-08-07)。ETH 净通胀 ~0.5%/年为该文所引数据。
[^5]: SIMD = Solana Improvement Document，Solana 的改进提案格式。
[^6]: CoinDesk, Solana SGP-0003 / SIMD-0553 / SIMD-0550 报道。
[^7]: ZK Labs, 《EIP-8363 迎来最强反对声音：SharpeLink CEO「错误提案，错误时机」》(2026-08-09)。

---

*天下难事必作于易，天下大事必作于细。（《韩非子·喻老》引《老子》）*

*ETH 与 SOL 的供应转向，不在某一次投票的结果里，而在那每年一到两个百分点的发行率微调中——细微处，方见资产的长期底色。*
