---
layout: default
title: "加密资产行业重大盗窃与安全事件时间线（截至 2026 年 10 月 30 日）"
description: "从创世区块到 2026 年 10 月币安约 63 亿美元事件：按时间梳理加密资产行业重大盗窃与安全事件，区分被盗、冻结、追回与最终损失；金额以币种数量为准，美元数仅为时点估值。"
date: 2026-10-31 09:45:00 +0800
categories: observation
author: 南野东亦
permalink: /observations/2026/10/31/crypto-major-thefts-timeline.html
version: "v1.0"
tags: [时间线, 盗窃, 安全事件, Binance, 市场观察]
data_cutoff: 2026-10-30
---

<!-- 渲染说明：相邻引用之间用 &nbsp; 分隔，防止 Markdown 将 [n] [m] 解析成单个引用链接；文末编号列表由文末定义生成，与正文引用一一对应。 -->


**最重要的判断：**重大损失已不再只是交易所在线托管钱包被攻破。案例显示，风险还扩展到智能合约逻辑、跨链桥验证和权限、预言机/外部调用、共享代码依赖、签名界面及供应链；但事件的可追回性和责任归因差异很大。金额应优先看被转走的币种和数量，美元数通常只是特定时点估值。特别是截至 2026 年 10 月 30 日，确有可证实的 Binance 重大安全事件：10 月 29 日发生、约 63 亿美元估值的多链未授权转账；其技术根因和最终归因仍在调查中。不能把它误说成“没有 2026 年 10 月事件”，也不能把初步取证推断写成定论。[88]&nbsp;[89]&nbsp;[90]&nbsp;[91]&nbsp;[92]

> **口径说明：**“被盗/转出”不等于最终净损失；冻结、追踪、追回、平台补足和用户获赔是不同状态。以下凡美元数字均为估值，币种数量或官方记录更明确时优先列出。法律指控、执法归因和分析机构归因均按其证据性质表述。

## 2009 年：比特币网络诞生

### 1 月 3 日：创世区块（Block 0）

比特币区块链从创世区块开始运行。创世区块的 coinbase 数据嵌入了当天《泰晤士报》头版标题，常被视为比特币诞生的时间标记。它不是一宗安全事件，但为后续“账本由谁维护、规则如何变更”的历史提供了起点。[95]

### 1 月 12 日：早期点对点转账

区块链记录显示，Satoshi Nakamoto 向早期测试者 Hal Finney 转出 10 BTC，常被记作第一笔已知的个人间比特币转账。此阶段尚无成熟交易所或托管生态；风险重点是客户端软件、共识规则和早期用户自行保管密钥，而非大型平台热钱包。[96]

## 2010 年：第一次重大协议危机

### 8 月 15 日：区块 74638 的价值溢出漏洞

**类别：**共识规则/交易金额验证漏洞；不是攻击者从他人钱包盗走 BTC。交易检查代码在汇总极大输出金额时发生整数溢出，导致一笔交易在区块 74638 中凭空创造约 **184,467,440,737 BTC**，其中两个地址各收到约 922 亿 BTC，远超 2,100 万枚供给上限。[93]&nbsp;[94]

开发者数小时内发布补丁，拒绝溢出交易；节点随后形成短暂分叉。修正后的链在区块 74691 超过包含异常交易的旧链，成为有效历史，凭空创造的 BTC 随之失效。它展示了公开审计供应量和快速协调修补的重要性，也暴露一项根本张力：协议声称规则稳定，但遇到共识漏洞时，社区仍须通过软件升级和链选择共同决定哪本账本继续有效。由于当时网络规模很小，这样的干预成本远低于今天。[93]&nbsp;[94]

## 2011 年：Mt. Gox 早期入侵与长期失窃指控

### 2011 年 6 月：账户入侵与价格闪崩

**类别：**账户入侵、异常交易；不是已证实的链上盗币事件。攻击者利用被攻陷的账户提交大额卖单，平台显示的比特币价格从约 32 美元跌至几美分。Guardian 报道称攻击者试图提走所得，但受每日 1,000 美元提现限额影响；WIRED 则报约 875 万美元。两者对实际兑现或损失程度并不一致，所查材料不能核实净损失额，闪崩价格也不能当成被盗金额。[1]&nbsp;[2]

常被混淆的 **25,000 BTC** 是个人用户 Allinvain 自己电脑遭入侵后的钱包失窃，并非 Mt. Gox 的损失。早期报道未能独立核实 Mt. Gox 6 月事件的攻击者身份或可核对的链上盗币数。[1]

### 2011 年 9 月至至少 2014 年 5 月：钱包与私钥服务器遭长期入侵（起诉指控）

**类别：**未授权访问托管服务器并持续转币。美国司法部转述起诉书指控称，嫌疑人及同伙约于 2011 年 9 月未经授权进入存有 Mt. Gox 钱包及私钥的日本服务器，其后把币转至其控制地址；指控称该期间至少约 **647,000 BTC** 被盗，部分经其控制的其他交易所账户洗钱。这是跨时段累计指控，公开材料没有逐笔拆分日期和金额，也不是终审裁定；被告依法推定无罪。[3]

## 2012 年：交易所托管、凭证与钱包备份失窃

### 2012 年 3 月 1 日：Bitcoinica 经 Linode 遭入侵

**类别：**托管商及服务器权限失守。同期报道指攻击者取得 Linode 客户支持权限，利用管理界面进入客户服务器并重置 root 密码；Bitcoinica 约损失 **43,000 BTC**，按当时币价约 **22 万美元**。平台当时称继续运营、用户余额不受影响。损失是平台服务器钱包资产，不是用户个人钱包被盗。[6]&nbsp;[7]

### 2012 年 5 月 11 日：Bitcoinica 生产服务器再遭入侵

**类别：**在线钱包资产失窃。同期报道记录约 **18,547 BTC**，当时估值约 8.7 万至 9 万美元；用户资料也可能泄露。报道对初始入口说法不一，一篇提及受损邮箱账户，另一篇只确认生产服务器和数据库遭入侵。因此不把某一种入口写作已独立证实。Bitcoinica 暂停运营并称会处理提款和索赔。[8]&nbsp;[9]

### 2012 年 7 月 13 日：Bitcoinica 在 Mt. Gox 账户资产被提走

**类别：**账户/API 凭证失窃，而非一般热钱包服务器盗款。同期报道称约 **40,000 BTC 加 40,000 美元**被从 Bitcoinica 存于 Mt. Gox 的账户提走；据报道的路径，源代码公开后，攻击者发现 Mt. Gox API 密钥，该密钥又被复用于 LastPass 密码，且没有二次验证。人员对密码责任有争议，攻击者身份未获可靠确认。[9]

三起事故按同期近似数合计约 **101,500 BTC**，另有第三起的 40,000 美元；数字经过取整，并非经审计的精确总账。用户诉讼所称索赔金额、Bitcoinica 清盘及其留在 Mt. Gox 破产程序中的约 2,900 万美元债权估值，都不是新的盗窃金额，也不能证明赃币已追回。BBC 对后续攻击间隔的说法与同期明确日期报道不同，此处采用具体日期来源。[3]&nbsp;[8]&nbsp;[9]&nbsp;[10]

### 2012 年 9 月前后：BitFloor 未加密钱包密钥备份失窃

**类别：**操作失误导致密钥备份暴露，继而盗币。报道日期相差一天，宜记为 **9 月 3–4 日前后**。攻击者进入服务器并利用遗留的未加密钱包密钥备份，转走约 **24,000 BTC**，按当时报价约 **24.96 万美元**。报道指备份是在创办人手动升级服务器软件时留在服务器上；交易所暂停交易，后来尝试偿付，但退款拖延。[11]&nbsp;[12]

BitFloor 于 2013 年再次停业的直接原因是美国银行账户将被关闭；客户等待美元退款是后续债务/银行问题，不是 2013 年又发生一笔黑客盗窃。[13]


## 2014 年：Mt. Gox 停业、资产缺口与清算

### 2–4 月：停业、初始资产缺口与清算

Mt. Gox 于 2014 年 2 月停止运营并申请破产保护，最初称约 **850,000 BTC** 不见，其中当时报道拆为约 750,000 BTC 客户币及近 100,000 BTC 公司币。WIRED 按当时币价折算约 **4.60 亿美元**，另报约 **2,740 万美元银行账户资金缺口**；后者是法币账户缺口，不是比特币盗窃额。850,000 BTC 是破产时的初始缺口估算，不代表在 2014 年某日一次被盗 85 万枚。[4]&nbsp;[5]

公司称于 2014 年 3 月 7 日在一只旧格式钱包发现约 **200,000 BTC**，并于 3 月 14–15 日转入离线钱包。BBC 报道缺口因此由 850,000 降至约 650,000 BTC；Reuters 后来记为 202,185 BTC。此为原以为已空的钱包余额，不是确认追回的赃币。以 850,000 减约 202,000 得约 648,000，与司法部指控的至少 647,000 BTC大致接近，但统计范围、四舍五入及法律性质不同，不能视为精确相等。[3]&nbsp;[4]

2014 年 4 月 24 日，东京地方法院命令 Mt. Gox 进入清算程序。约 24,750 名客户提出赔偿请求；客户债权、无法提币和破产分配，与链上被盗数量不是同一口径。**清算/破产是盗窃后果与资不抵债处置，不是另一宗黑客攻击。**[3]

## 2015 年：Bitstamp 运营钱包被攻陷

### 1 月 4 日：Bitstamp 运营钱包被攻陷

**类别：**热钱包与员工终端/凭证风险。Reuters 报道约 **19,000 BTC** 被盗，约值 500 万美元；Bitstamp 称主要储备在离线系统，客户事故前余额会全额保留，并于 1 月 9 日恢复交易。[14]&nbsp;[15]

一份真实性未获 Bitstamp 确认的泄露内部报告称，攻击者数周内钓鱼联系六名员工、感染系统管理员电脑，继而获得热钱包文件及口令；报告列出 18,866 BTC、按其取价约 526 万美元。由于交易所未确认报告真实性，详细攻击链和精确币数须标为“泄露报告所称”，不能覆盖公开确认的约 19,000 BTC口径。[16]

## 2016 年：The DAO 代码漏洞与 Bitfinex 凭证/网络入侵

### 2016 年 6 月 17 日：The DAO 重入漏洞

**类别：**智能合约漏洞利用，不是私钥被盗，也不是以太坊网络本身遭攻破。攻击者利用 The DAO 的 `split` 函数在内部余额状态更新前递归调用，使同一笔交易反复取得 ETH 并转入攻击者控制的 child DAO。以太坊基金会当时明确说漏洞影响 The DAO，而非 Ethereum 网络；转入 child DAO 的资金约 27 天不能提取。[17]

常用数量概数为约 **360 万 ETH**，约占 The DAO 资金三分之一；同期美元估值约 **5,000 万至 6,000 万美元**。这是当时币价换算，不是最终净损失；同期报道对募资总额也有约 1.5 亿至 1.68 亿美元等不同数字，不应与攻击金额混用。[18]&nbsp;[19]

### 2016 年 7 月 20 日：硬分叉恢复机制引发治理争议

以太坊硬分叉在区块 1,920,000 执行“非正常状态变更”，将 Dark DAO 与 Whitehat DAO 合约约 **1,200 万 ETH** 转入 WithdrawDAO 恢复合约。这是两类合约余额的转移总量，不等于攻击者盗走的数量；公告时约 450 万 ETH 已返还 DAO 代币持有人，另约 46.3 万 ETH 由 curator 控制，其他处理仍在审查，不能说所有持有人已全额获赔。基金会称其方案不是回滚区块或交易。此次处置凸显账本不可篡改原则与保护受害者的治理张力。[20]

### 2016 年 8 月 2 日：Bitfinex 约 119,754 BTC 被盗

**类别：**交易所网络入侵及未经授权转账；不是已确认的协议漏洞，也不能简单归结为“多签失效”。司法部材料称 Ilya Lichtenstein 进入 Bitfinex 网络，实施逾 2,000 笔未经授权交易，将约 **119,754 BTC** 转走，并删除访问凭证和日志。Reuters 同期报道称 BitGo 表示未发现其服务器被攻破；现有公开材料没有确定完整初始入侵点或证明某项具体漏洞。[21]&nbsp;[22]

各来源记载 **119,754–119,756 BTC**，宜以司法部的 119,754 BTC为主并说明差异。按盗窃时价格约 **7,100 万至 7,200 万美元**；客户余额削减 36.06% 是平台损失分摊方案，不等于每位用户丢失 36% 原始 BTC。Bitfinex发行 BFX债权代币，后按面值赎回或换股并销毁；这是负债/补偿安排，不是被盗 BTC 原物归还，也不是平台破产。[21]&nbsp;[22]&nbsp;[23]

执法部门 2022 年取得收币钱包私钥并扣押超过 **94,000 BTC**，扣押时价值约 36 亿美元；Bitfinex 官方另记 2019 年追回约 27.66 BTC、2021 年追回约 6.51 BTC。被扣押、后来法院返还安排与实际归还受害者需分别表述。2025 年政府主张将约 94,643 BTC按原币返还 Bitfinex；2026 年 3 月媒体称法院已下令返还，但所给研究未提供法院命令原文，故不据此断言具体执行或最终客户分配。36 亿美元及更高的后来市值是币价升值后的估值，不是 2016 年损失额。[21]&nbsp;[24]&nbsp;[25]&nbsp;[26]

Lichtenstein 与 Heather Morgan 于 2023 年就洗钱共谋认罪；Lichtenstein 于 2024 年被判刑。其认罪与司法部案情支持高可信归因，但定罪罪名是洗钱共谋，并非单独的黑客入侵罪。[22]&nbsp;[27]

## 2017 年：Parity 多签钱包的盗币与资产冻结

### 2017 年 7 月 18–19 日：Parity 多签初始化漏洞遭利用

**类别：**智能合约权限/初始化漏洞。攻击者调用特定旧版钱包的 `initWallet` 将自己设为唯一所有者，再调用 `execute` 转走资产。链上重建记录三笔主要转账，合计 **153,037 ETH**；按 2017 年 7 月 20 日价格约 **3,274 万美元**，媒体常写约 3,000 万美元。[28]&nbsp;[29]

这是项目多签钱包中的 ETH被转出，不是以太坊底层协议漏洞或用户私钥被盗。其后 White Hat Group 也利用同一漏洞，将其他易受影响钱包的 ETH 与代币转入保管地址；研究者估算救援资产约 1.64 亿美元（含 ETH 和代币），不可与黑帽盗币额混为一谈。所查来源不足以确认被盗资金最终全部追回。[29]

### 2017 年 11 月 6 日：共享库自毁，513,774 ETH 无法访问

**类别：**合约库操作/部署权限错误造成资产冻结，不是被盗。Parity 官方事后报告称，未初始化的共享库被调用者取得所有权后执行遗留 `selfdestruct`；依赖该库的 **587 个钱包**因此无法执行转账，涉及 **513,774.16 ETH**及代币。资产仍在合约中不可访问，不能算攻击者拿走的币。[30]

同期 2.8 亿美元是早期估算；Parity审计的约 1.62 亿美元按不同时间币价计值。EIP-999 提议恢复代码并引发是否应改变链状态的争论，曾有非正式签名投票但无决定效力。所查材料未显示提案最终实施。操作者身份与其究竟蓄意破坏或误操作均不确定。[30]&nbsp;[31]&nbsp;[32]

## 2018 年：Coincheck 的 NEM 热钱包盗窃

### 2018 年 1 月 26 日：约 5.23 亿 XEM 从热钱包转出

**类别：**交易所客户资产被盗。Coincheck称约 **523,000,000 XEM** 于日本时间 02:57 转出，直到约 11:25 才发现；事发时估值约 **580 亿日元**，媒体美元换算约 5.30 亿至 5.34 亿美元。平台承认资产保存在联网热钱包，且未用多重签名这一额外保护；公开材料未确认攻击者如何取得签名权限或具体漏洞，不能直接写成已证实的私钥盗窃。[33]&nbsp;[34]&nbsp;[35]

约 26 万名客户受影响。Coincheck 承诺以自有资金按每枚 88.549 日元赔付，合计约 **463 亿日元**，并于 2018 年 3 月启动偿付；这是平台赔付而非被盗 XEM 追回。NEM 基金会追踪并标记地址提供了资金流线索，但不能单方面冻结或返币。后续研究称 2021 年有 30 余人因涉嫌明知币源而兑换相关 NEM 被起诉；该研究并未确认黑客主谋身份，亦不能据此称款项已返还。[34]&nbsp;[35]&nbsp;[36]

## 2019 年：Binance 与 Upbit 的热钱包事件

### 2019 年 5 月 7 日：Binance 单笔提款约 7,000 BTC

**类别：**账户/API 凭证滥用与未经授权的热钱包提款。Binance称攻击者取得大量用户 API 密钥、双重验证代码及可能的其他资料，通过多个账户协同构造看似通过安全检查的提款；约 **7,000 BTC** 在一笔交易中从热钱包转出，官方估值约 **4,000 万美元**（其他同期报道约 4,100 万美元）。热钱包约占其 BTC持有量 2%，不是损失比例。[37]&nbsp;[38]

平台暂停充提并承诺由 SAFU 承担损失，用户资金不受影响；这是平台补偿承诺，不是链上追回。Chainalysis 2019 年 5 月 17 日报告称资金已转至多个地址且当时仍未移动；该状态只截至报告发布时，所查来源不能确认后来追回情况。未确认私钥泄露、具体初始入口或内部人员参与。[37]&nbsp;[38]&nbsp;[39]

### 2019 年 11 月 27 日：Upbit 热钱包 342,000 ETH 被盗

**类别：**交易所热钱包未经授权转出；攻击技术未公开确认。Upbit公告记录约 **342,000 ETH** 转往未知地址，估值约 **580 亿韩元**。媒体按当时价格和汇率估为约 4,150 万至 5,000 万美元；以 ETH 数量及韩元公告为主。Upbit说明其后其他大额转账是迁移剩余热钱包资产至冷钱包，不是更多盗窃。[40]&nbsp;[41]

平台称以公司资产补足、用户资产不受损，并暂停充提。韩国国家警察厅 2024 年 11 月称调查确认攻击者与朝鲜有关，依据包括 IP 与资金流线索；警方官员拒绝确认具体组织，Lazarus 与 Andariel 是韩国媒体报道的身份，不能写成警方正式点名。警方还称追回约 4.8 BTC并返还，远非 342,000 ETH全数追回。后续市值超过 10 亿美元是币价变化后的估值，不是 2019 年损失额。[41]

## 2020 年：KuCoin 热钱包私钥失窃

### 2020 年 9 月 25–26 日：多资产热钱包被盗

**类别：**内部网络遭入侵并获取热钱包私钥。9 月 26 日 UTC+8（UTC 日期仍为 9 月 25 日），KuCoin 检测到异常大额提现；官方早期称热钱包私钥泄露，冷钱包未受影响。事后平台称攻击者长期侵入内部网络，影响 **154 种代币**；Chainalysis观察到部分 ERC-20 代币经 Uniswap、Kyber 等去中心化交易平台换成 ETH。[42]&nbsp;[43]

总损失常见估值为 **2.75 亿至 2.85 亿美元**：Chainalysis早期链上清单超过 2.75 亿美元，联合国专家报告约 2.81 亿美元，KuCoin事后按事发日价格计约 2.85 亿美元。这是不同估值/统计快照，不是多笔损失。KuCoin称约 84% 资产通过链上追踪、合约升级和执法等方式追回；最终事后拆分为伙伴追回约 2.22 亿美元（78%）、执法与安全机构追回约 1,745 万美元（6%），余下约 4,555 万美元（16%）由平台和保险基金承担。此为平台事后自述，追回与平台承担并非同一概念；平台称用户最终未承担损失。[42]&nbsp;[43]&nbsp;[44]

联合国专家称洗钱模式强烈暗示朝鲜关联，Chainalysis归因为 Lazarus Group；属于有分析依据的机构归因，不是公开司法定罪。另一起约 2,300 万美元的 2020 年盗窃在联合国报告中被认为链上相关，但受害方未确认，不计入 KuCoin 数额。[43]&nbsp;[44]

## 2021 年：Poly Network 跨链管理权限漏洞

### 2021 年 8 月 10 日：跨链资产被转走，随后分批回返

**类别：**跨链消息验证与特权调用组合漏洞，不是 Keeper 私钥被盗。SlowMist分析称攻击者构造跨链请求，利用目标链调用逻辑改写 Keeper公钥，随后以伪造的验证者身份通过验证并调用资产管理合约。约 **6.10 亿至 6.13 亿美元**各为攻击时币种组合的估值，不是几起不同攻击。[45]&nbsp;[46]

资产分布在 Ethereum、当时的 Binance Smart Chain（现 BNB Chain）及 Polygon，涵盖十余种代币。8 月 11 日时约 2.60 亿美元回流、约 3.53 亿待返，Tether冻结约 3,300 万美元 USDT；8 月 12 日各来源的回流统计又不同。8 月 23 日 Poly称除被冻结 USDT外已重新控制其他资产；8 月 27 日 Tether释放冻结资产后，Poly称全数追回。追回的是资产/控制权处置，不代表攻击者主动返还全部资金；所称 50 万美元漏洞赏金也不是追回金额。匿名攻击者自述的白帽动机未能独立核验。[45]&nbsp;[46]&nbsp;[47]&nbsp;[48]&nbsp;[49]

## 2022 年：桥接验证风险、签名门槛与合约默认值

### 2022 年 2 月 2 日：Wormhole 跨链桥漏洞

**类别：**Solana桥程序验证漏洞。攻击者伪造验证流程依赖的 sysvar账户，令桥把假存款证明当成真，在 Solana 上铸造约 **120,000 枚无足额以太坊支持的桥接 ETH**；不是从用户钱包盗走原生 ETH。攻击时估值略高于 **3.2 亿美元**。[50]&nbsp;[51]&nbsp;[52]

约 93,750 ETH随后桥回 Ethereum，其余转为 SOL等；这些是资金流向，不是追回。2 月 3 日 Jump Crypto补入超过 3.2 亿美元 ETH，使资金支持恢复；这是第三方补足而非赃款追回。所查材料未确认攻击者身份或悬赏成功。[50]&nbsp;[51]&nbsp;[52]

### 2022 年 3 月 23 日：Ronin Bridge 5/9 验证者密钥失陷

**类别：**验证者凭证/权限集中风险。攻击者取得 9 个验证者中 5 个签名密钥，批准两笔提现：**173,600 ETH 和 25.5 million USDC**。Sky Mavis控制其中四个验证者；第五个 Axie DAO 验证者曾临时授权代签，任务结束后权限未撤销。攻击于 3 月 23 日发生，3 月 29 日因用户无法提现而发现。[53]&nbsp;[54]&nbsp;[55]

攻击时估值约 **5.4 亿美元**，披露时约 6.15 亿美元；6.2 亿或 6.24 亿美元是其他取价口径，不是额外损失。FBI于 2022 年 4 月将攻击归因 Lazarus Group 与 APT38（朝鲜关联），为执法机构归因，非针对具体个人的法院判决。[53]&nbsp;[56]

Ronin 于 2022 年 6 月重开桥，称用户资产 1:1 获支持；Sky Mavis以公司资产和融资补足用户损失。Chainalysis称执法与业界协作扣押超过 3,000 万美元，但不等于大部分盗币已追回。重开后增加独立验证者、大额提现熔断、额外签名审核与限额，直接回应已暴露的门槛和监控问题。[54]&nbsp;[55]&nbsp;[57]

### 2022 年 8 月 1 日：Nomad Bridge 零值根哈希漏洞与“跟进式”掏空

**类别：**合约验证漏洞。升级把零值根哈希登记为可信根，使未使用消息的零值映射被当作有效证明；攻击者通过 `process()` 处理伪造消息并更改收款地址。首笔成功交易提走 **100 WBTC**（当时约 230 万美元），随后大量地址复制相似交易，在数小时内形成同一漏洞的连续攻击波。[58]&nbsp;[59]

Nomad官方称损失超过 **1.86 亿美元**，多家同期/取证来源以约 **1.90 亿美元**计。追回阶段性数字包括 8 月 5 日超过 2,000 万美元，官方后来称超过 3,700 万美元（约 20%）；Mandiant记载约 3,600 万美元返还。数字是不同日期和估值口径，不能相加；当时官方仍将桥重启与资产分配列为待办。2026 年 10 月报道，Alexander Blok（又名 Gurevich）已被引渡美国受审，被指为最初利用漏洞并提取约 280 万美元者；这是起诉/引渡阶段指控，不等于定罪，更不能把全案 1.86 亿美元归于一人。[58]&nbsp;[60]&nbsp;[61]&nbsp;[62]&nbsp;[63]

### 2022 年 8 月 1 日：Nomad 以外的后续归因不应混算

Nomad攻击持续波及不同持币地址，但资料未支持将其拆成多个独立事件。媒体报道的单一嫌疑人约 280 万美元是全案的一部分，不应另加在 1.86 亿美元总额之上。地址聚类只能支持对部分行为者的分析判断，不等同于全案现实身份归因。[60]&nbsp;[61]&nbsp;[62]&nbsp;[63]

## 2023 年：借贷合约、个人钱包、云数据库与热钱包

### 2023 年 3 月 13 日：Euler Finance 闪电贷辅助的合约漏洞

**类别：**智能合约记账与健康度检查缺陷。攻击者借助闪电贷循环存借，调用 `DonateToReserve` 捐赠抵押品并自我清算；关键路径缺少健康度检查，抵押与债务记账失衡。闪电贷是攻击工具，不是根因。[64]&nbsp;[65]&nbsp;[66]

攻击时估值约 **1.97 亿至 1.99 亿美元**，涉及 stETH、USDC、WBTC、DAI等。Euler称数千名用户受影响，Angle、Balancer、Idle、Yield等协议也有存款风险；Angle稳定币曾脱锚。攻击后存款降至不足 1,000 万美元，不等于盗款金额，也不等于平台破产。[64]&nbsp;[65]&nbsp;[66]&nbsp;[67]

3 月至 4 月，攻击者分批返还 ETH和稳定币；Euler于 2024 年回顾称被盗资产 100%追回。其称归还资产按返还时价格约值 2.4 亿美元，差额主要是价格变化，不是比攻击时多追回额外币。攻击者真实身份及是否被捕未确认；有 100 ETH转往 Lazarus关联地址不构成归因证据，分析机构称可能是误导。[64]&nbsp;[65]&nbsp;[66]

### 2023 年 6 月 2 日：Atomic Wallet 用户钱包失窃

**类别：**非托管钱包用户资产盗窃；具体入侵机制未公开确认。FBI称约 **1 亿美元**失窃，并归因 TraderTraitor（又称 Lazarus Group、APT38）关联行为者；Reuters转述链上分析称逾 5,500 个钱包受影响。不同阶段估值有差异，所查来源未确认具体是漏洞、密钥失窃、钓鱼或用户误操作，也未确认已向用户追回或赔付。[68]&nbsp;[69]

### 2023 年 9 月 23 日：Mixin 云服务商数据库遭攻击

**类别：**第三方云数据库安全事件。Mixin称主网资产损失约 **2 亿美元**，涉及用户钱包内 BTC、ETH与稳定币；这是平台初步估值，链上追踪识别约 1.41 亿美元资产不等于追回。平台暂停存取款，后来提出以未来利润回购债券型代币等补偿方案；方案不是已兑现赔款。攻击者身份和进入数据库的具体方式未确认。[70]&nbsp;[71]&nbsp;[72]

### 2023 年 11 月 10 日：Poloniex 热钱包异常转出

**类别：**热钱包私钥失陷的链上分析判断。ETH、Tron、BTC等链钱包资产被转出；CertiK估值约 **1.32 亿美元**，同期报道常写逾 1 亿至 1.2 亿美元，差异来自资产范围、取价和统计时间。攻击者把资金转至多个地址；约 1,050 万枚 GLM误入代币合约且在报告时滞留，并非已返还。[73]&nbsp;[74]

Justin Sun提出若 7 天内返还可获 5% 白帽赏金，并称会承担受影响资金、系统恢复后逐步重开充提。所查资料未确认赃款返还、赏金成功或用户损失实际补齐；私钥如何被取得及攻击者身份亦未知。[74]&nbsp;[75]

## 2024 年：DMM Bitcoin 供应链社工与 WazirX 多签交易授权欺骗

### 2024 年 5 月 31 日：DMM Bitcoin 4,502.9 BTC 被盗

**类别：**供应商员工遭社工及终端入侵后滥用交易授权。美国 FBI、美国国防部网络犯罪中心与日本警察厅联合公告称，朝鲜关联 TraderTraitor行为者通过 LinkedIn假招聘接触 Ginco钱包软件公司员工，诱使其运行恶意 Python代码；其后冒用员工会话并很可能篡改 DMM员工发出的合法交易请求，转走 **4,502.9 BTC**。[76]

按当时价格约 **482 亿日元 / 3.05 亿至 3.08 亿美元**；美元差异是估值口径。DMM称会补足客户存款，Chainalysis称客户存款获全额覆盖，这是补偿而非被盗 BTC追回。公司后来停止交易所业务并将客户账户及资产迁往 SBI VC Trade，属于后续业务处置，不是另一笔盗窃。[76]&nbsp;[77]

### 2024 年 7 月 18 日：WazirX 多签钱包攻击

**类别：**多签交易授权流程遭欺骗，伴随恶意合约升级；根因仍有争议。多种代币损失估值约 **2.3 亿至 2.35 亿美元**。WazirX称其多签流程中界面显示与实际待签负载不一致；Liminal称涉事为客户自托管钱包且其基础设施未遭攻破。Cobo分析支持 4-of-6 Safe钱包恶意合约升级机制，但具体界面或中间人攻击路径仍未定论，不宜简写为“私钥被盗”或已证实的 Liminal漏洞。[78]&nbsp;[79]&nbsp;[80]

美国与韩国政府声明依据行业分析将事件归因朝鲜；所查材料中没有同等详细的公开技术取证披露。WazirX于 2025 年冻结首批约 300 万美元 USDT，但冻结不等于返还。新加坡法院批准债权重组后，平台称 2025 年重启首批分配约为合资格用户核准债权参考价值的 85%，并提供与未来利润或追回资产挂钩的 Recovery Tokens；这不是“追回 85%被盗币”，也不是最终全额偿还保证。平台债权总额约 5.46 亿美元是债权基数，不是被盗额。[81]&nbsp;[82]

## 2025 年：Bybit 冷钱包在签名界面/供应链攻击中失窃

### 2025 年 2 月 21 日：Bybit 一只以太坊冷钱包被控制

**类别：**钱包服务供应链、开发者终端及签名界面攻击。攻击者转移 **401,347 ETH、90,375 stETH、15,000 cmETH、8,000 mETH**；Bybit公布估值约 **14.6 亿美元**，FBI及媒体常取整约 15 亿美元。各分项估值取整后相加与总额略有差异，应以币种数量为准。[83]&nbsp;[84]

Safe与Mandiant初步调查指向开发者 Mac终端遭入侵及 AWS会话令牌被劫持；Sygnia进一步描述钱包网页资源中的恶意 JavaScript篡改，使签署者看到正常转账，却实际签署调用恶意合约的 `delegatecall`。这些是调查发现而非法院认定，具体细节仍有证据强弱差异。FBI于 2 月 26 日正式归因朝鲜关联 TraderTraitor；该执法归因并非公开法院判决。[84]&nbsp;[85]&nbsp;[86]

Bybit称客户资产维持 1:1支持，并在约 72 小时内用合作方融资、存款与场外采购补足储备；这是资产负债表补足，不等于赃币追回。冻结、协议方取回与追踪资金也须分开；所查截至 2025 年 3 月资料没有证明被盗总额全数追回。[83]&nbsp;[87]

## 2026 年：Binance 十链未授权提款——有重大事件，根因仍属初步调查

### 2026 年 10 月 29–30 日：约 63 亿美元估值的多链安全事件

**类别：**热钱包与签名权限遭攻击导致未授权转账；不是平台破产或用户集体资产损失的证据。Binance于 10 月 30 日初步公告称，调查可能从一名 DevOps工程师的笔记本遭入侵开始，攻击者进入 service container 并提交未授权提款；Binance称当时没有钱包私钥泄露证据，调查未完成。TRM观察到 Ethereum上有 EIP-7702授权与扫款代码，其他链呈标准签名转账；TRM据跨链签名行为推断更可能是签名基础设施遭攻破，但这是分析机构推断，不能写成Binance已确认根因。[88]&nbsp;[89]&nbsp;[90]

TRM称攻击自 10 月 29 日约 20:05 UTC起，大部分转账在约 20 分钟内发生，涉及约十条链；按转账时价格估值约 **63.6 亿美元**，按其报告撰写时价格重估约 62.3 亿美元。Binance官方称影响约 63 亿美元，Chainalysis约 64 亿美元，Reuters亦概括约 63 亿美元。金额差异反映估值时点、取整和统计口径，并非多起事件或几笔独立损失。[88]&nbsp;[89]&nbsp;[90]&nbsp;[91]

TRM估算已冻结约 27 亿美元，Chainalysis约 28 亿美元，Binance最新公告称约 30 亿美元已在链上冻结；冻结不等于依法返还或最终追回。TRM称仍有约 24 亿美元处于发行方无法直接冻结的资产中。Binance暂时暂停提款，存款和其他未受影响的平台服务仍正常运行，并撤销受影响地址授权，承诺由 SAFU与公司资金承担损失、用户资金安全；这些是处置措施与补偿承诺，不等于赃款追回。取证公司高置信度指向朝鲜关联 TraderTraitor，但 Binance未将责任归于特定个人，未见执法机构对此案正式归因或起诉，因此应保留“分析机构归因”的限定。[88]&nbsp;[89]&nbsp;[90]&nbsp;[91]&nbsp;[92]&nbsp;[97]

**截至 2026 年 10 月 30 日的核验结论：**“2026 年 10 月 Binance 事件”不是无根据传言；研究结果所列 Binance官方公告、TRM、Chainalysis及 Reuters/CNBC报道相互印证，支持确有一宗重大多链未授权转账事件。可以确认的是事件日期、规模约 63 亿美元估值及部分资金被冻结/定位；尚未证实的是完整技术根因、最终损失净额、资金最终返还情况及司法责任。故不能称其“没有发生”，也不能把工程师笔记本入侵或朝鲜归因当作已最终裁定事实。[88]&nbsp;[89]&nbsp;[90]&nbsp;[91]&nbsp;[92]

## 这些事件改变了什么

1. **风险从单点托管外溢到权限链与供应链，但不是旧风险消失。** Mt. Gox、Bitcoinica、BitFloor、Coincheck、Binance 2019与 KuCoin等，显示服务器、凭证、密钥备份和热钱包仍是高影响目标。[3]&nbsp;[6]&nbsp;[7]&nbsp;[8]&nbsp;[9]&nbsp;[10]&nbsp;[11]&nbsp;[12]&nbsp;[13]&nbsp;[14]&nbsp;[15]&nbsp;[16]&nbsp;[33]&nbsp;[34]&nbsp;[35]&nbsp;[36]&nbsp;[37]&nbsp;[38]&nbsp;[39]&nbsp;[40]&nbsp;[41]&nbsp;[42]&nbsp;[43]&nbsp;[44] 后续 DMM与 Bybit则说明，供应商员工、开发者终端、云会话及签名界面也可能成为控制资产的入口；DMM官方调查描述社工冒用供应商员工会话，Bybit调查描述界面资源被篡改。[76]&nbsp;[84]&nbsp;[85]&nbsp;[86] 这支持“风险边界扩展”，不支持“托管风险已被取代”。

2. **代码正确性与密钥安全是两类不能互相替代的防线。** The DAO、Parity、Poly、Wormhole、Nomad和 Euler的损失来自代码逻辑、初始化、验证或状态记账缺陷；Ronin、BitFloor、KuCoin等则突出签名密钥、权限门槛、热钱包及备份风险。[17]&nbsp;[18]&nbsp;[19]&nbsp;[20]&nbsp;[28]&nbsp;[29]&nbsp;[30]&nbsp;[31]&nbsp;[32]&nbsp;[45]&nbsp;[46]&nbsp;[47]&nbsp;[48]&nbsp;[49]&nbsp;[50]&nbsp;[51]&nbsp;[52]&nbsp;[53]&nbsp;[54]&nbsp;[55]&nbsp;[56]&nbsp;[57]&nbsp;[58]&nbsp;[59]&nbsp;[60]&nbsp;[61]&nbsp;[62]&nbsp;[63]&nbsp;[64]&nbsp;[65]&nbsp;[66] 安全评估不能仅问“私钥是否离线”，也要检查合约如何验证调用、共享依赖是否可被初始化/销毁、签名者实际批准的调用与屏幕显示是否一致。案例证明的是这些具体失守路径，不是审计或多签必然无效。

3. **跨链桥把验证错误变成可跨协议传递的资产风险。** Wormhole的伪造存款证明铸出无抵押桥接资产，Ronin的 5/9门槛被集中控制与遗留授权满足，Poly的跨链请求触发特权 Keeper更新，Nomad的零值根哈希令伪造消息被接受。[45]&nbsp;[46]&nbsp;[47]&nbsp;[48]&nbsp;[49]&nbsp;[50]&nbsp;[51]&nbsp;[52]&nbsp;[53]&nbsp;[54]&nbsp;[55]&nbsp;[56]&nbsp;[57]&nbsp;[58]&nbsp;[59]&nbsp;[60]&nbsp;[61]&nbsp;[62]&nbsp;[63] 这些案例支持桥接系统要分别约束消息证明、目标调用、特权更新和签名独立性；Wormhole事件还说明，接受桥接资产作抵押的其他协议可能面临传染风险，但不能据此断言相关协议实际资不抵债。[50]&nbsp;[51]&nbsp;[52]&nbsp;[53]&nbsp;[54]&nbsp;[55]

4. **追回并非纯技术问题，且与去中心化治理存在张力。** Poly事件中稳定币发行方冻结资产，后来解冻使 Poly 宣布追回全部资金；Euler通过谈判收到资产，KuCoin通过合作与合约机制追回部分资产。[45]&nbsp;[46]&nbsp;[47]&nbsp;[48]&nbsp;[49]&nbsp;[42]&nbsp;[43]&nbsp;[44]&nbsp;[64]&nbsp;[65]&nbsp;[66] 相反，DAO硬分叉与 Parity恢复提案引发“保护受害者是否应改变链状态”的争论。[20]&nbsp;[30]&nbsp;[31]&nbsp;[32] 因此链上可追踪并不等于能追回；冻结、追回与补偿依赖发行方、平台、执法和治理选择，甚至可能与抗审查/不可逆原则冲突。

5. **平台补足可保护用户，但不能冒充赃款追回或无损。** Bitfinex以BFX重组负债，Coincheck以自有资金赔付，Binance承诺SAFU覆盖，KuCoin称平台承担未追回余额，Ronin与 Bybit以公司或外部资金补足储备；这些都是赔付/补足机制，不是攻击者交还原币。[21]&nbsp;[22]&nbsp;[23]&nbsp;[24]&nbsp;[25]&nbsp;[34]&nbsp;[35]&nbsp;[37]&nbsp;[38]&nbsp;[42]&nbsp;[43]&nbsp;[44]&nbsp;[53]&nbsp;[54]&nbsp;[55]&nbsp;[56]&nbsp;[57]&nbsp;[83] 对外报告应分别列出被盗资产、冻结/扣押、实际返还、平台承担和债权分配，避免把一种数字写成另一种。

6. **攻击规模可能迅速放大，但“系统性传染”须逐案证明。** Nomad的首笔交易被大量地址复制，显示漏洞公开可见后利用门槛可骤降；Euler冲击波及多个存款协议，Wormhole无抵押铸币则可能威胁接受桥接资产的协议。[58]&nbsp;[59]&nbsp;[60]&nbsp;[61]&nbsp;[62]&nbsp;[63]&nbsp;[64]&nbsp;[65]&nbsp;[66]&nbsp;[67]&nbsp;[50]&nbsp;[51]&nbsp;[52] Bybit事件引发市场波动与平台暂时暂停部分提款，属于短期市场冲击的证据，但不能据此推断系统性危机或资不抵债。[88]&nbsp;[89]&nbsp;[90]&nbsp;[91]&nbsp;[92] 不能把每起重大盗窃都泛化为全行业传染。

## References

1. [The Guardian, “A history of bitcoin hacks.”](https://www.theguardian.com/technology/2014/mar/18/history-of-bitcoin-hacks-alternative-currency)
2. [WIRED, “The Inside Story of Mt. Gox, Bitcoin’s $460 Million Disaster.”](https://www.wired.com/2014/03/bitcoin-exchange/)
3. [U.S. Department of Justice, “Russian Nationals Charged With Hacking One Cryptocurrency Exchange and Illicitly Operating Another.”](https://www.justice.gov/archives/opa/pr/russian-nationals-charged-hacking-one-cryptocurrency-exchange-and-illicitly-operating-another)
4. [BBC News, “MtGox finds 200000 missing bitcoins in old wallet.”](https://www.bbc.com/news/technology-26677291)
5. [Reuters, “Twice burned - How Mt. Gox’s bitcoin customers could lose again.”](https://www.reuters.com/investigates/special-report/bitcoin-gox/)
6. [IEEE Spectrum, “Thousands of Bitcoins stolen in a hack on Linode.”](https://spectrum.ieee.org/thousands-of-bitcoins-stolen-in-a-hack-on-linode)
7. [Bitcoin Magazine, “The Bitcoinica Linode Theft And What It Means For Bitcoin.”](https://bitcoinmagazine.com/business/the-bitcoinica-linode-theft-and-what-it-means-for-bitcoin-1330805009)
8. [Threatpost, “Breach at Bitcoinica Exchange Nets $87,000 in Online Currency.”](https://threatpost.com/breach-bitcoinica-exchange-nets-87000-online-currency-051412/76559/)
9. [Bitcoin Magazine, “Bitcoinica Stolen From… Again.”](https://bitcoinmagazine.com/business/bitcoinica-stolen-from-again)
10. [BBC News, “Bitcoin users sue over funds lost in site attack.”](https://www.bbc.co.uk/news/technology-19244210)
11. [CNET, “Bitcoin exchange BitFloor shuttered after virtual heist.”](https://www.cnet.com/tech/services-and-software/bitcoin-exchange-bitfloor-shuttered-after-virtual-heist/)
12. [Ars Technica, “Hacker steals $250k in Bitcoins from online exchange Bitfloor.”](https://arstechnica.com/tech-policy/2012/09/hacker-steals-250k-in-bitcoins-from-online-exchange-bitfloor/)
13. [Finextra, “Bitcoin exchange Bitfloor shuts down.”](https://www.finextra.com/newsarticle/24738/bitcoin-exchange-bitfloor-shuts-down)
14. [Reuters, “Bitcoin exchange Bitstamp suspends service after security breach.”](https://www.reuters.com/article/business/bitcoin-exchange-bitstamp-suspends-service-after-security-breach-idUSKBN0KF0UH/)
15. [Reuters, “Bitcoin exchange Bitstamp says to resume trading on Friday.”](https://www.reuters.com/article/technology/bitcoin-exchange-bitstamp-says-to-resume-trading-on-friday-idUSL6N0UO1DC)
16. [CoinDesk, “Details of $5 Million Bitstamp Hack Revealed.”](https://www.coindesk.com/markets/2015/07/01/details-of-5-million-bitstamp-hack-revealed)
17. [Ethereum Foundation, “CRITICAL UPDATE Re: DAO Vulnerability.”](https://blog.ethereum.org/2016/06/17/critical-update-re-dao-vulnerability)
18. [BBC News, “Hack attack drains start-up investment fund.”](https://www.bbc.com/news/technology-36585930)
19. [The New York Times, “A Hacking of More Than $50 Million Dashes Hopes in the World of Virtual Currency.”](https://www.nytimes.com/2016/06/18/business/dealbook/hacker-may-have-removed-more-than-50-million-from-experimental-cybercurrency-project.html)
20. [Ethereum Foundation, “Hard Fork Completed.”](https://blog.ethereum.org/2016/07/20/hard-fork-completed)
21. [U.S. Department of Justice, “Two Arrested for Alleged Conspiracy to Launder $4.5 Billion in Stolen Cryptocurrency.”](https://www.justice.gov/archives/opa/pr/two-arrested-alleged-conspiracy-launder-45-billion-stolen-cryptocurrency)
22. [U.S. Department of Justice, “Bitfinex Hacker and Wife Plead Guilty to Money Laundering Conspiracy Involving Billions in Cryptocurrency.”](https://www.justice.gov/archives/opa/pr/bitfinex-hacker-and-wife-plead-guilty-money-laundering-conspiracy-involving-billions)
23. [Bitfinex, “2016 Security Breach Bitcoin Recovery Frequently Asked Questions (FAQ).”](https://support.bitfinex.com/hc/en-us/articles/4417401349657-2016-Security-Breach-Bitcoin-Recovery-Frequently-Asked-Questions-FAQ)
24. [The Block, “US government says stolen bitcoin from 2016 Bitfinex hack should be returned to the exchange 'in-kind'.”](https://www.theblock.co/news/markets/2025-01-15-us-government-says-stolen-bitcoin-from-2016-bitfinex-hack-should-be-returned-to-the-exchange-in-kind-334791)
25. [crypto.news, “Court-ordered BTC return to Bitfinex sets a precedent for crypto victim rights.”](https://crypto.news/court-ordered-btc-return-to-bitfinex-sets-a-precedent-for-crypto-victim-rights/)
26. [Reuters Legal News, “When stolen crypto is recovered, who is entitled to restitution?”](https://www.reuters.com/legal/legalindustry/when-stolen-crypto-is-recovered-who-is-entitled-restitution-2024-12-09/)
27. [U.S. Department of Justice, “Bitfinex Hacker Sentenced in Money Laundering Conspiracy Involving Billions in Stolen Cryptocurrency.”](https://www.justice.gov/archives/opa/pr/bitfinex-hacker-sentenced-money-laundering-conspiracy-involving-billions-stolen)
28. [OpenZeppelin, “The Parity Wallet Hack Explained.”](https://www.openzeppelin.com/news/on-the-parity-wallet-multisig-hack-405a8c12e8f7)
29. [GitHub (bokkypoobah), “Parity Multisig Vulnerability - White Hat Group Rescue Reconciliation.”](https://github.com/bokkypoobah/ParityMultisigRecoveryReconciliation)
30. [Parity Technologies, “A Postmortem on the Parity Multi-Sig Library Self-Destruct.”](https://medium.com/paritytech/a-postmortem-on-the-parity-multi-sig-library-self-destruct-63daca3a4cf7)
31. [Ethereum Improvement Proposals, “EIP-999: Restore Contract Code at 0x863DF6BFa4469f3ead0bE8f9F2AAE51c91A907b4.”](https://eips.ethereum.org/EIPS/eip-999)
32. [Bitcoin Magazine, “The Evolving Debate Over EIP-999: Can (or Should) Trapped Ether Be Freed?”](https://bitcoinmagazine.com/business/evolving-debate-over-eip-999-can-or-should-trapped-ether-be-freed)
33. [BBC News, “Coincheck: World's biggest ever digital currency 'theft'.”](https://www.bbc.com/news/world-asia-42845505)
34. [Reuters, “Japan raps Coincheck, orders broader checks after $530 million cryptocurrency theft.”](https://www.reuters.com/idUSKBN1FI073/)
35. [Reuters, “Japan's Coincheck to start repaying customers Monday after digital money heist.”](https://www.reuters.com/idUSKCN1GO0U5)
36. [Forensic Science International: Digital Investigation, “How cryptocurrency is laundered: Case study of Coincheck hacking incident.”](https://www.sciencedirect.com/science/article/pii/S2665910721000724)
37. [Binance, “Binance Security Breach Update.”](https://www.binance.com/en/support/announcement/detail/360028031711)
38. [CNBC, “Binance bitcoin hack: Over $40 million of cryptocurrency stolen.”](https://www.cnbc.com/2019/05/08/binance-bitcoin-hack-over-40-million-of-cryptocurrency-stolen.html)
39. [Chainalysis, “All Eyes on Binance Stolen Funds: Can the Thieves Cash Out?”](https://www.chainalysis.com/blog/all-eyes-on-binance-stolen-funds/)
40. [Upbit, “암호화폐 입출금 서비스 일시 중단 및 긴급 서버 점검 진행 사유에 대해 말씀드립니다.”](https://www.upbit.com/service_center/notice?id=1085)
41. [Reuters, “North Korea hackers behind 2019 $42 mln Ethereum heist, South Korea police say.”](https://www.reuters.com/world/asia-pacific/north-korea-hackers-behind-2019-42-mln-ethereum-heist-south-korea-police-say-2024-11-21/)
42. [KuCoin, “KuCoin Security Incident Update.”](https://www.kucoin.com/announcement/kucoin-security-incident-update)
43. [Chainalysis, “The KuCoin Hack: What We Know So Far and How the Hackers Are Laundering the Funds.”](https://www.chainalysis.com/blog/kucoin-hack-2020-defi-uniswap/)
44. [KuCoin, “A Letter from KuCoin CEO: 2020, 2021 and Beyond.”](https://www.kucoin.com/announcement/en-a-letter-from-kucoin-ceo-2020-2021-and-beyond)
45. [SlowMist, “The Analysis and Q&A Of Poly Network Being Hacked.”](https://slowmist.medium.com/the-analysis-and-q-a-of-poly-network-being-hacked-8112a35beb39)
46. [Chainalysis, “Poly Network Attacker Returning Funds After Pulling Off Biggest DeFi Theft Ever.”](https://www.chainalysis.com/blog/poly-network-hack-august-2021/)
47. [Reuters, “How hackers stole $613 million in crypto tokens from Poly Network.”](https://www.reuters.com/technology/how-hackers-stole-613-million-crypto-tokens-poly-network-2021-08-12/)
48. [Reuters, “Crypto platform Poly Network says hacked funds returned.”](https://www.reuters.com/technology/crypto-platform-poly-network-says-hacked-funds-returned-2021-08-23/)
49. [Business Insider, “Poly Network Hack: All $610 Million Returned As Tether Unfreezes Funds.”](https://markets.businessinsider.com/news/currencies/poly-network-hack-610-million-tether-mr-white-hat-defi-2021-8)
50. [CertiK, “Wormhole Bridge Exploit Incident Analysis.”](https://www.certik.com/blog/wormhole-bridge-exploit-incident-analysis)
51. [Reuters, “Jump Trading replaces stolen Wormhole funds after $320 million hack.”](https://www.reuters.com/technology/crypto-network-wormhole-hit-with-possible-320-mln-hack-2022-02-03/)
52. [Chainalysis, “Wormhole Hack: Lessons From The Wormhole Exploit.”](https://www.chainalysis.com/blog/wormhole-hack-february-2022/)
53. [Reuters, “Blockchain project Ronin hit by $615 million crypto heist.”](https://www.reuters.com/technology/blockchain-company-ronin-hit-by-615-million-crypto-heist-2022-03-29/)
54. [Sky Mavis / Axie Infinity, “Sky Mavis Raises $150M Led By Binance, Funds to be Used to Reimburse Users Affected by Ronin Validator Hack.”](https://blog.axieinfinity.com/p/funding)
55. [Ronin, “The Ronin Bridge Is Open.”](https://www.blog.roninchain.com/p/the-ronin-bridge-is-open-)
56. [FBI, “FBI Statement on Attribution of Malicious Cyber Activity Posed by the Democratic People's Republic of Korea.”](https://www.fbi.gov/news/press-releases/fbi-statement-on-attribution-of-malicious-cyber-activity-posed-by-the-democratic-peoples-republic-of-korea)
57. [Chainalysis, “Crypto Community Makes Profiting Hard for North Korean Hackers.”](https://www.chainalysis.com/blog/axie-infinity-ronin-bridge-dprk-hack-seizure/)
58. [Immunefi, “Hack Analysis: Nomad Bridge, August 2022.”](https://immunefi.com/blog/bug-fix-reviews/hack-analysis-nomad-bridge-august-2022/)
59. [Nomad, “The Road to Recovery: Where we are today.”](https://medium.com/nomad-xyz-blog/the-road-to-recovery-6abe5eec8ff1)
60. [Mandiant / Google Cloud, “Decentralized Robbery: Dissecting the Nomad Bridge Hack and Following the Money.”](https://cloud.google.com/blog/topics/threat-intelligence/dissecting-nomad-bridge-hack)
61. [Reuters, “U.S. crypto firm Nomad hit by $190 million theft.”](https://www.reuters.com/technology/us-crypto-firm-nomad-hit-by-190-million-theft-2022-08-02/)
62. [CTech, “Israeli crypto suspect extradited to U.S. over $186 million Nomad hack.”](https://www.calcalistech.com/ctechnews/article/bkskkjgtze)
63. [The Jerusalem Post, “Israel extradites suspect to US over alleged USD 2.8 million Nomad theft.”](https://www.jpost.com/israel-news/crime-in-israel/article-913280)
64. [Euler Finance, “War & Peace: Behind the Scenes of Euler’s $240M Exploit Recovery.”](https://www.euler.finance/blog/war-peace-behind-the-scenes-of-eulers-240m-exploit-recovery)
65. [Chainalysis, “Euler Finance Flash Loan Attack Explained.”](https://www.chainalysis.com/blog/euler-finance-flash-loan-attack/)
66. [Elliptic, “Euler Finance loses $199 million in flash loan attack.”](https://www.elliptic.co/insights/euler-finance-loses-199-million-in-flash-loan-attack/)
67. [DL News, “Euler Finance hacker returns stolen funds amid ongoing negotiations, reveals identity.”](https://www.dlnews.com/articles/defi/euler-finance-hacker-returns-stolen-funds-amid-ongoing-negotiations-reveals-identity/)
68. [FBI, “FBI Identifies Cryptocurrency Funds Stolen by DPRK.”](https://www.fbi.gov/news/press-releases/fbi-identifies-cryptocurrency-funds-stolen-by-dprk)
69. [Reuters, “North Korean hackers stole $100 million in recent cryptocurrency heist, analysts say.”](https://www.reuters.com/world/north-korean-hackers-stole-100-million-recent-cryptocurrency-heist-analysts-2023-06-13/)
70. [Reuters, “Hong Kong crypto firm hit by $200 million hack.”](https://www.reuters.com/technology/hong-kong-crypto-firm-hit-by-200-million-hack-2023-09-25/)
71. [Bitdefender, “Mixin Network Reports $200 Million Security Breach.”](https://www.bitdefender.com/en-us/blog/hotforsecurity/mixin-network-reports-200-million-security-breach)
72. [DL News, “Questions swirl around $200m hack as Mixin pledges to pay users back.”](https://www.dlnews.com/articles/defi/questions-swirl-around-hack-at-hong-kong-network-mixin/)
73. [CertiK, “Poloniex Incident Analysis.”](https://www.certik.com/blog/poloniex-incident-analysis)
74. [The Wall Street Journal, “Crypto Exchange Poloniex Hacked for More than $120 Million.”](https://www.wsj.com/livecoverage/stock-market-today-dow-jones-11-10-2023/card/crypto-exchange-poloniex-hacked-for-more-than-120-million-qjll0KyHGxBCEQzRz020)
75. [Justin Sun, public X statement on Poloniex system restoration.](https://x.com/justinsuntron/status/1723009018086527126)
76. [FBI / DC3 / Japan National Police Agency, “FBI, DC3, and NPA Identification of North Korean Cyber Actors, Tracked as TraderTraitor, Responsible for Theft of $308 Million USD from Bitcoin.DMM.com.”](https://www.fbi.gov/news/press-releases/fbi-dc3-and-npa-identification-of-north-korean-cyber-actors-tracked-as-tradertraitor-responsible-for-theft-of-308-million-from-bitcoindmmcom)
77. [Chainalysis, “$2.2 Billion Stolen in Crypto in 2024 but Hacked Volumes Slowed in Second Half.”](https://www.chainalysis.com/blog/crypto-hacking-stolen-funds-2025/)
78. [WazirX, “Preliminary Report: Cyber Attack on WazirX Multisig Wallet.”](https://wazirx.com/blog/preliminary-report-cyber-attack-on-wazirx-multisig-wallet/)
79. [Liminal Custody, “Liminal Remains Secure Amidst Sophisticated Attack.”](https://www.liminalcustody.com/blog/liminal-remains-secure-amidst-sophisticated-attack/)
80. [Cobo Security Team, “WazirX Hacking Incident Analysis By Cobo Security Team.”](https://www.cobo.com/post/wazirx-hack-incident-analysis)
81. [U.S. Department of State, “Joint Statement on Cryptocurrency Thefts by the Democratic People’s Republic of Korea and Public-Private Collaboration.”](https://2021-2025.state.gov/office-of-the-spokesperson/releases/2025/01/joint-statement-on-cryptocurrency-thefts-by-the-democratic-peoples-republic-of-korea-and-public-private-collaboration/)
82. [WazirX, “Update on WazirX Restructuring Scheme: Recovery Token Allocation Complete.”](https://wazirx.com/blog/recovery-tokens-explained/)
83. [Bybit, “Bybit Security Incident: Timeline of Events and FAQs.”](https://www.bybit.com/en/learn/this-week-in-bybit/bybit-security-incident-timeline)
84. [FBI, “North Korea Responsible for $1.5 Billion Bybit Hack.”](https://www.fbi.gov/investigate/cyber/alerts/2025/north-korea-responsible-for-1-5-billion-bybit-hack)
85. [Safe{Wallet}, “Investigation Updates and Community Call to Action.”](https://x.com/safe/status/1897663514975649938)
86. [Sygnia, “Sygnia's Investigation into the Bybit Hack: What We Know So Far.”](https://www.sygnia.co/blog/sygnia-investigation-bybit-hack/)
87. [BBC News, “North Korean hackers cash out hundreds of millions from $1.5bn ByBit hack.”](https://www.bbc.com/news/articles/c2kgndwwd7lo)
88. [Binance, “Security Incident Update,” 2026-10-30.](https://www.binance.com/en/support/announcement/detail/c5a8729a97ac486d963784d96c5642d7)
89. [TRM Labs, “North Korea Steals USD 6.36 Billion From Binance in the Largest Hack in History.”](https://www.trmlabs.com/resources/blog/north-korea-steals-usd-6-36-billion-from-binance-in-the-largest-hack-in-history)
90. [Chainalysis, “Binance Exploit: Latest Findings and Response.”](https://www.chainalysis.com/blog/binance-exploit-latest-findings-and-response/)
91. [Reuters, “Hackers steal $6.3 billion from Binance in world's biggest crypto theft.”](https://www.reuters.com/legal/transactional/tether-circle-freeze-238-billion-after-binance-reports-security-incident-2026-10-29/)
92. [CNBC, “Binance's $6.3 billion hack: What we know and what happens next.”](https://www.cnbc.com/2026/10/30/billions-in-crypto-frozen-in-binance-hack-heres-what-happens-next-.html)
93. [Bitcoin Wiki, “Value overflow incident.”](https://en.bitcoin.it/wiki/Value_overflow_incident)
94. [Bitcoin Core, “Fix for block 74638.”](https://github.com/bitcoin/bitcoin/commit/d4c6b90ca3f9b47adb1b2724a0c3514f80635c84)
95. [Blockstream, “Genesis Block.”](https://help.blockstream.com/education/glossary/genesis-block)
96. [Guinness World Records, “First Bitcoin transaction.”](https://www.guinnessworldrecords.com/world-records/696243-first-bitcoin-transaction)
97. [Binance, “Security Incident Update #2 (2026-10-30).”](https://www.binance.com/en/support/announcement/detail/d3306d9dca5243548c813b605e1d1751)

[1]: https://www.theguardian.com/technology/2014/mar/18/history-of-bitcoin-hacks-alternative-currency "The Guardian, “A history of bitcoin hacks.”"
[2]: https://www.wired.com/2014/03/bitcoin-exchange/ "WIRED, “The Inside Story of Mt. Gox, Bitcoin’s $460 Million Disaster.”"
[3]: https://www.justice.gov/archives/opa/pr/russian-nationals-charged-hacking-one-cryptocurrency-exchange-and-illicitly-operating-another "U.S. Department of Justice, “Russian Nationals Charged With Hacking One Cryptocurrency Exchange and Illicitly Operating Another.”"
[4]: https://www.bbc.com/news/technology-26677291 "BBC News, “MtGox finds 200000 missing bitcoins in old wallet.”"
[5]: https://www.reuters.com/investigates/special-report/bitcoin-gox/ "Reuters, “Twice burned - How Mt. Gox’s bitcoin customers could lose again.”"
[6]: https://spectrum.ieee.org/thousands-of-bitcoins-stolen-in-a-hack-on-linode "IEEE Spectrum, “Thousands of Bitcoins stolen in a hack on Linode.”"
[7]: https://bitcoinmagazine.com/business/the-bitcoinica-linode-theft-and-what-it-means-for-bitcoin-1330805009 "Bitcoin Magazine, “The Bitcoinica Linode Theft And What It Means For Bitcoin.”"
[8]: https://threatpost.com/breach-bitcoinica-exchange-nets-87000-online-currency-051412/76559/ "Threatpost, “Breach at Bitcoinica Exchange Nets $87,000 in Online Currency.”"
[9]: https://bitcoinmagazine.com/business/bitcoinica-stolen-from-again "Bitcoin Magazine, “Bitcoinica Stolen From… Again.”"
[10]: https://www.bbc.co.uk/news/technology-19244210 "BBC News, “Bitcoin users sue over funds lost in site attack.”"
[11]: https://www.cnet.com/tech/services-and-software/bitcoin-exchange-bitfloor-shuttered-after-virtual-heist/ "CNET, “Bitcoin exchange BitFloor shuttered after virtual heist.”"
[12]: https://arstechnica.com/tech-policy/2012/09/hacker-steals-250k-in-bitcoins-from-online-exchange-bitfloor/ "Ars Technica, “Hacker steals $250k in Bitcoins from online exchange Bitfloor.”"
[13]: https://www.finextra.com/newsarticle/24738/bitcoin-exchange-bitfloor-shuts-down "Finextra, “Bitcoin exchange Bitfloor shuts down.”"
[14]: https://www.reuters.com/article/business/bitcoin-exchange-bitstamp-suspends-service-after-security-breach-idUSKBN0KF0UH/ "Reuters, “Bitcoin exchange Bitstamp suspends service after security breach.”"
[15]: https://www.reuters.com/article/technology/bitcoin-exchange-bitstamp-says-to-resume-trading-on-friday-idUSL6N0UO1DC "Reuters, “Bitcoin exchange Bitstamp says to resume trading on Friday.”"
[16]: https://www.coindesk.com/markets/2015/07/01/details-of-5-million-bitstamp-hack-revealed "CoinDesk, “Details of $5 Million Bitstamp Hack Revealed.”"
[17]: https://blog.ethereum.org/2016/06/17/critical-update-re-dao-vulnerability "Ethereum Foundation, “CRITICAL UPDATE Re: DAO Vulnerability.”"
[18]: https://www.bbc.com/news/technology-36585930 "BBC News, “Hack attack drains start-up investment fund.”"
[19]: https://www.nytimes.com/2016/06/18/business/dealbook/hacker-may-have-removed-more-than-50-million-from-experimental-cybercurrency-project.html "The New York Times, “A Hacking of More Than $50 Million Dashes Hopes in the World of Virtual Currency.”"
[20]: https://blog.ethereum.org/2016/07/20/hard-fork-completed "Ethereum Foundation, “Hard Fork Completed.”"
[21]: https://www.justice.gov/archives/opa/pr/two-arrested-alleged-conspiracy-launder-45-billion-stolen-cryptocurrency "U.S. Department of Justice, “Two Arrested for Alleged Conspiracy to Launder $4.5 Billion in Stolen Cryptocurrency.”"
[22]: https://www.justice.gov/archives/opa/pr/bitfinex-hacker-and-wife-plead-guilty-money-laundering-conspiracy-involving-billions "U.S. Department of Justice, “Bitfinex Hacker and Wife Plead Guilty to Money Laundering Conspiracy Involving Billions in Cryptocurrency.”"
[23]: https://support.bitfinex.com/hc/en-us/articles/4417401349657-2016-Security-Breach-Bitcoin-Recovery-Frequently-Asked-Questions-FAQ "Bitfinex, “2016 Security Breach Bitcoin Recovery Frequently Asked Questions (FAQ).”"
[24]: https://www.theblock.co/news/markets/2025-01-15-us-government-says-stolen-bitcoin-from-2016-bitfinex-hack-should-be-returned-to-the-exchange-in-kind-334791 "The Block, “US government says stolen bitcoin from 2016 Bitfinex hack should be returned to the exchange 'in-kind'.”"
[25]: https://crypto.news/court-ordered-btc-return-to-bitfinex-sets-a-precedent-for-crypto-victim-rights/ "crypto.news, “Court-ordered BTC return to Bitfinex sets a precedent for crypto victim rights.”"
[26]: https://www.reuters.com/legal/legalindustry/when-stolen-crypto-is-recovered-who-is-entitled-restitution-2024-12-09/ "Reuters Legal News, “When stolen crypto is recovered, who is entitled to restitution?”"
[27]: https://www.justice.gov/archives/opa/pr/bitfinex-hacker-sentenced-money-laundering-conspiracy-involving-billions-stolen "U.S. Department of Justice, “Bitfinex Hacker Sentenced in Money Laundering Conspiracy Involving Billions in Stolen Cryptocurrency.”"
[28]: https://www.openzeppelin.com/news/on-the-parity-wallet-multisig-hack-405a8c12e8f7 "OpenZeppelin, “The Parity Wallet Hack Explained.”"
[29]: https://github.com/bokkypoobah/ParityMultisigRecoveryReconciliation "GitHub (bokkypoobah), “Parity Multisig Vulnerability - White Hat Group Rescue Reconciliation.”"
[30]: https://medium.com/paritytech/a-postmortem-on-the-parity-multi-sig-library-self-destruct-63daca3a4cf7 "Parity Technologies, “A Postmortem on the Parity Multi-Sig Library Self-Destruct.”"
[31]: https://eips.ethereum.org/EIPS/eip-999 "Ethereum Improvement Proposals, “EIP-999: Restore Contract Code at 0x863DF6BFa4469f3ead0bE8f9F2AAE51c91A907b4.”"
[32]: https://bitcoinmagazine.com/business/evolving-debate-over-eip-999-can-or-should-trapped-ether-be-freed "Bitcoin Magazine, “The Evolving Debate Over EIP-999: Can (or Should) Trapped Ether Be Freed?”"
[33]: https://www.bbc.com/news/world-asia-42845505 "BBC News, “Coincheck: World's biggest ever digital currency 'theft'.”"
[34]: https://www.reuters.com/idUSKBN1FI073/ "Reuters, “Japan raps Coincheck, orders broader checks after $530 million cryptocurrency theft.”"
[35]: https://www.reuters.com/idUSKCN1GO0U5 "Reuters, “Japan's Coincheck to start repaying customers Monday after digital money heist.”"
[36]: https://www.sciencedirect.com/science/article/pii/S2665910721000724 "Forensic Science International: Digital Investigation, “How cryptocurrency is laundered: Case study of Coincheck hacking incident.”"
[37]: https://www.binance.com/en/support/announcement/detail/360028031711 "Binance, “Binance Security Breach Update.”"
[38]: https://www.cnbc.com/2019/05/08/binance-bitcoin-hack-over-40-million-of-cryptocurrency-stolen.html "CNBC, “Binance bitcoin hack: Over $40 million of cryptocurrency stolen.”"
[39]: https://www.chainalysis.com/blog/all-eyes-on-binance-stolen-funds/ "Chainalysis, “All Eyes on Binance Stolen Funds: Can the Thieves Cash Out?”"
[40]: https://www.upbit.com/service_center/notice?id=1085 "Upbit, “암호화폐 입출금 서비스 일시 중단 및 긴급 서버 점검 진행 사유에 대해 말씀드립니다.”"
[41]: https://www.reuters.com/world/asia-pacific/north-korea-hackers-behind-2019-42-mln-ethereum-heist-south-korea-police-say-2024-11-21/ "Reuters, “North Korea hackers behind 2019 $42 mln Ethereum heist, South Korea police say.”"
[42]: https://www.kucoin.com/announcement/kucoin-security-incident-update "KuCoin, “KuCoin Security Incident Update.”"
[43]: https://www.chainalysis.com/blog/kucoin-hack-2020-defi-uniswap/ "Chainalysis, “The KuCoin Hack: What We Know So Far and How the Hackers Are Laundering the Funds.”"
[44]: https://www.kucoin.com/announcement/en-a-letter-from-kucoin-ceo-2020-2021-and-beyond "KuCoin, “A Letter from KuCoin CEO: 2020, 2021 and Beyond.”"
[45]: https://slowmist.medium.com/the-analysis-and-q-a-of-poly-network-being-hacked-8112a35beb39 "SlowMist, “The Analysis and Q&A Of Poly Network Being Hacked.”"
[46]: https://www.chainalysis.com/blog/poly-network-hack-august-2021/ "Chainalysis, “Poly Network Attacker Returning Funds After Pulling Off Biggest DeFi Theft Ever.”"
[47]: https://www.reuters.com/technology/how-hackers-stole-613-million-crypto-tokens-poly-network-2021-08-12/ "Reuters, “How hackers stole $613 million in crypto tokens from Poly Network.”"
[48]: https://www.reuters.com/technology/crypto-platform-poly-network-says-hacked-funds-returned-2021-08-23/ "Reuters, “Crypto platform Poly Network says hacked funds returned.”"
[49]: https://markets.businessinsider.com/news/currencies/poly-network-hack-610-million-tether-mr-white-hat-defi-2021-8 "Business Insider, “Poly Network Hack: All $610 Million Returned As Tether Unfreezes Funds.”"
[50]: https://www.certik.com/blog/wormhole-bridge-exploit-incident-analysis "CertiK, “Wormhole Bridge Exploit Incident Analysis.”"
[51]: https://www.reuters.com/technology/crypto-network-wormhole-hit-with-possible-320-mln-hack-2022-02-03/ "Reuters, “Jump Trading replaces stolen Wormhole funds after $320 million hack.”"
[52]: https://www.chainalysis.com/blog/wormhole-hack-february-2022/ "Chainalysis, “Wormhole Hack: Lessons From The Wormhole Exploit.”"
[53]: https://www.reuters.com/technology/blockchain-company-ronin-hit-by-615-million-crypto-heist-2022-03-29/ "Reuters, “Blockchain project Ronin hit by $615 million crypto heist.”"
[54]: https://blog.axieinfinity.com/p/funding "Sky Mavis / Axie Infinity, “Sky Mavis Raises $150M Led By Binance, Funds to be Used to Reimburse Users Affected by Ronin Validator Hack.”"
[55]: https://www.blog.roninchain.com/p/the-ronin-bridge-is-open- "Ronin, “The Ronin Bridge Is Open.”"
[56]: https://www.fbi.gov/news/press-releases/fbi-statement-on-attribution-of-malicious-cyber-activity-posed-by-the-democratic-peoples-republic-of-korea "FBI, “FBI Statement on Attribution of Malicious Cyber Activity Posed by the Democratic People's Republic of Korea.”"
[57]: https://www.chainalysis.com/blog/axie-infinity-ronin-bridge-dprk-hack-seizure/ "Chainalysis, “Crypto Community Makes Profiting Hard for North Korean Hackers.”"
[58]: https://immunefi.com/blog/bug-fix-reviews/hack-analysis-nomad-bridge-august-2022/ "Immunefi, “Hack Analysis: Nomad Bridge, August 2022.”"
[59]: https://medium.com/nomad-xyz-blog/the-road-to-recovery-6abe5eec8ff1 "Nomad, “The Road to Recovery: Where we are today.”"
[60]: https://cloud.google.com/blog/topics/threat-intelligence/dissecting-nomad-bridge-hack "Mandiant / Google Cloud, “Decentralized Robbery: Dissecting the Nomad Bridge Hack and Following the Money.”"
[61]: https://www.reuters.com/technology/us-crypto-firm-nomad-hit-by-190-million-theft-2022-08-02/ "Reuters, “U.S. crypto firm Nomad hit by $190 million theft.”"
[62]: https://www.calcalistech.com/ctechnews/article/bkskkjgtze "CTech, “Israeli crypto suspect extradited to U.S. over $186 million Nomad hack.”"
[63]: https://www.jpost.com/israel-news/crime-in-israel/article-913280 "The Jerusalem Post, “Israel extradites suspect to US over alleged USD 2.8 million Nomad theft.”"
[64]: https://www.euler.finance/blog/war-peace-behind-the-scenes-of-eulers-240m-exploit-recovery "Euler Finance, “War & Peace: Behind the Scenes of Euler’s $240M Exploit Recovery.”"
[65]: https://www.chainalysis.com/blog/euler-finance-flash-loan-attack/ "Chainalysis, “Euler Finance Flash Loan Attack Explained.”"
[66]: https://www.elliptic.co/insights/euler-finance-loses-199-million-in-flash-loan-attack/ "Elliptic, “Euler Finance loses $199 million in flash loan attack.”"
[67]: https://www.dlnews.com/articles/defi/euler-finance-hacker-returns-stolen-funds-amid-ongoing-negotiations-reveals-identity/ "DL News, “Euler Finance hacker returns stolen funds amid ongoing negotiations, reveals identity.”"
[68]: https://www.fbi.gov/news/press-releases/fbi-identifies-cryptocurrency-funds-stolen-by-dprk "FBI, “FBI Identifies Cryptocurrency Funds Stolen by DPRK.”"
[69]: https://www.reuters.com/world/north-korean-hackers-stole-100-million-recent-cryptocurrency-heist-analysts-2023-06-13/ "Reuters, “North Korean hackers stole $100 million in recent cryptocurrency heist, analysts say.”"
[70]: https://www.reuters.com/technology/hong-kong-crypto-firm-hit-by-200-million-hack-2023-09-25/ "Reuters, “Hong Kong crypto firm hit by $200 million hack.”"
[71]: https://www.bitdefender.com/en-us/blog/hotforsecurity/mixin-network-reports-200-million-security-breach "Bitdefender, “Mixin Network Reports $200 Million Security Breach.”"
[72]: https://www.dlnews.com/articles/defi/questions-swirl-around-hack-at-hong-kong-network-mixin/ "DL News, “Questions swirl around $200m hack as Mixin pledges to pay users back.”"
[73]: https://www.certik.com/blog/poloniex-incident-analysis "CertiK, “Poloniex Incident Analysis.”"
[74]: https://www.wsj.com/livecoverage/stock-market-today-dow-jones-11-10-2023/card/crypto-exchange-poloniex-hacked-for-more-than-120-million-qjll0KyHGxBCEQzRz020 "The Wall Street Journal, “Crypto Exchange Poloniex Hacked for More than $120 Million.”"
[75]: https://x.com/justinsuntron/status/1723009018086527126 "Justin Sun, public X statement on Poloniex system restoration."
[76]: https://www.fbi.gov/news/press-releases/fbi-dc3-and-npa-identification-of-north-korean-cyber-actors-tracked-as-tradertraitor-responsible-for-theft-of-308-million-from-bitcoindmmcom "FBI / DC3 / Japan National Police Agency, “FBI, DC3, and NPA Identification of North Korean Cyber Actors, Tracked as TraderTraitor, Responsible for Theft of $308 Million USD from Bitcoin.DMM.com.”"
[77]: https://www.chainalysis.com/blog/crypto-hacking-stolen-funds-2025/ "Chainalysis, “$2.2 Billion Stolen in Crypto in 2024 but Hacked Volumes Slowed in Second Half.”"
[78]: https://wazirx.com/blog/preliminary-report-cyber-attack-on-wazirx-multisig-wallet/ "WazirX, “Preliminary Report: Cyber Attack on WazirX Multisig Wallet.”"
[79]: https://www.liminalcustody.com/blog/liminal-remains-secure-amidst-sophisticated-attack/ "Liminal Custody, “Liminal Remains Secure Amidst Sophisticated Attack.”"
[80]: https://www.cobo.com/post/wazirx-hack-incident-analysis "Cobo Security Team, “WazirX Hacking Incident Analysis By Cobo Security Team.”"
[81]: https://2021-2025.state.gov/office-of-the-spokesperson/releases/2025/01/joint-statement-on-cryptocurrency-thefts-by-the-democratic-peoples-republic-of-korea-and-public-private-collaboration/ "U.S. Department of State, “Joint Statement on Cryptocurrency Thefts by the Democratic People’s Republic of Korea and Public-Private Collaboration.”"
[82]: https://wazirx.com/blog/recovery-tokens-explained/ "WazirX, “Update on WazirX Restructuring Scheme: Recovery Token Allocation Complete.”"
[83]: https://www.bybit.com/en/learn/this-week-in-bybit/bybit-security-incident-timeline "Bybit, “Bybit Security Incident: Timeline of Events and FAQs.”"
[84]: https://www.fbi.gov/investigate/cyber/alerts/2025/north-korea-responsible-for-1-5-billion-bybit-hack "FBI, “North Korea Responsible for $1.5 Billion Bybit Hack.”"
[85]: https://x.com/safe/status/1897663514975649938 "Safe{Wallet}, “Investigation Updates and Community Call to Action.”"
[86]: https://www.sygnia.co/blog/sygnia-investigation-bybit-hack/ "Sygnia, “Sygnia's Investigation into the Bybit Hack: What We Know So Far.”"
[87]: https://www.bbc.com/news/articles/c2kgndwwd7lo "BBC News, “North Korean hackers cash out hundreds of millions from $1.5bn ByBit hack.”"
[88]: https://www.binance.com/en/support/announcement/detail/c5a8729a97ac486d963784d96c5642d7 "Binance, “Security Incident Update,” 2026-10-30."
[89]: https://www.trmlabs.com/resources/blog/north-korea-steals-usd-6-36-billion-from-binance-in-the-largest-hack-in-history "TRM Labs, “North Korea Steals USD 6.36 Billion From Binance in the Largest Hack in History.”"
[90]: https://www.chainalysis.com/blog/binance-exploit-latest-findings-and-response/ "Chainalysis, “Binance Exploit: Latest Findings and Response.”"
[91]: https://www.reuters.com/legal/transactional/tether-circle-freeze-238-billion-after-binance-reports-security-incident-2026-10-29/ "Reuters, “Hackers steal $6.3 billion from Binance in world's biggest crypto theft.”"
[92]: https://www.cnbc.com/2026/10/30/billions-in-crypto-frozen-in-binance-hack-heres-what-happens-next-.html "CNBC, “Binance's $6.3 billion hack: What we know and what happens next.”"
[93]: https://en.bitcoin.it/wiki/Value_overflow_incident "Bitcoin Wiki, “Value overflow incident.”"
[94]: https://github.com/bitcoin/bitcoin/commit/d4c6b90ca3f9b47adb1b2724a0c3514f80635c84 "Bitcoin Core, “Fix for block 74638.”"
[95]: https://help.blockstream.com/education/glossary/genesis-block "Blockstream, “Genesis Block.”"
[96]: https://www.guinnessworldrecords.com/world-records/696243-first-bitcoin-transaction "Guinness World Records, “First Bitcoin transaction.”"
[97]: https://www.binance.com/en/support/announcement/detail/d3306d9dca5243548c813b605e1d1751 "Binance, “Security Incident Update #2 (2026-10-30).”"
