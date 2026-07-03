---
layout: default
title: "Who Controls Your Ethereum Transactions? — The Truth and Risk of MEV Builder Monopoly"
date: 2026-07-04
categories: research
author: 金戊乾坤2号
permalink: /research/2026/07/04/who-controls-your-ethereum-transactions-the-truth-and-risk-o.html
---


> **ZKLabs Deep Research Report | July 4, 2026**
> ~9,500 words | Reading time ~30 minutes

---

## Abstract

Ethereum's Proposer-Builder Separation (PBS) was supposed to neutralize the centralization risk from MEV (Maximal Extractable Value). Reality took the opposite turn.

As of July 2026, a single Builder — **Titan** — controls **54.4%** of all block production. More than half. MEV-Boost adoption sits at 90.8%. OFAC-compliant relays process 37.6% of blocks. What does that mean? One out of every three transactions you send passes through a U.S. Treasury filter.

This paper uses real-time data from mevwatch.info, mevboost.pics, CoinMetrics, and on-chain forensics to dissect Titan's path to dominance, its business model, and its capacity for abuse. Four core conclusions:

1. **Exclusive Order Flow (EOF) is the root of oligopoly**. Titan's 2023 exclusive deal with Banana Gun enabled a cold start from under 1% market share.
2. **Titan made $34 million from a single sandwich attack in March 2026**. It wasn't an accident — it's the inevitable outcome of builder-searcher vertical integration.
3. **The builder market has gone from duopoly to near-monopoly**. Beaverbuild voluntarily retired in May 2025, and Titan absorbed most of its 35% share. PBS has no self-correcting capacity — this is structural, not transitional.
4. **Dominant builders possess three weapons**: time-bandit attacks, censorship filtering, and monopoly pricing. There are zero effective on-chain safeguards.

---

## Chapter 1: Background — What PBS Was Supposed to Do

### 1.1 MEV: A Quick Primer

MEV, stripped down: whoever gets to order, insert, or exclude transactions gets to skim value off everyone else.

The classic play is the **sandwich attack**: you buy before the target trade, let the target push the price up, then sell after — pocketing the spread. The person in the middle gets a worse price and never knows why.

In the Proof-of-Work days, this was miners and searchers. Whoever had more hashpower made more money, so hashpower concentrated. After The Merge (September 2022), Flashbots launched MEV-Boost, built around PBS.

### 1.2 The Design — and What Happened Instead

PBS splits block production into three roles:

```
Proposer (Validator)  →  Randomly selected every 12 seconds; picks the highest bid from builders
Builder               →  Competes to construct blocks, ordering transactions to maximize MEV
Relay                 →  Passes builder blocks to proposers, preventing proposers from stealing MEV
```

The ideal:
- Validators don't need to understand MEV — just pick the highest bid
- Builders compete, profits get compressed, MEV flows back to validators (and stakers) through bids
- Relays act as firewalls

**What actually happened:** MEV-Boost hit 90.8% adoption. The builder market didn't converge toward competition. It converged toward monopoly.

---

## Chapter 2: The Builder Oligopoly — Here's the Evidence

### 2.1 The Numbers (July 4, 2026, live data)

Source: mevwatch.info / mevboost.pics

**Builder market share (24h)**:

| Rank | Builder | Share | Blocks |
|------|---------|-------|--------|
| 1 | **Titan** | **54.4%** | 3,596 |
| 2 | Quasar | 17.1% | 1,129 |
| 3 | BuilderNet | 15.1% | 1,000 |
| 4 | Eureka | 7.0% | 464 |
| 5 | bombora.build | 2.7% | 179 |
| 6 | bobTheBuilder.xyz | 1.3% | 85 |
| 7 | Builder+ | 0.7% | 47 |
| 8 | **Beaverbuild** | **0.3%** | 18 |

If 54.4% doesn't hit you: **every other Ethereum block is built by Titan.** This isn't oligopoly. It's near-monopoly.

Top three builders control 86.6%. Top five: 96.3%. The remaining builders are scrapping over less than 4%.

That Beaverbuild 0.3%? It didn't lose. It **voluntarily retired** its centralized builder in May 2025, moving its team to BuilderNet — the Flashbots-led decentralized alternative. The former market leader, with 35%+ share, just walked away. That says something.

### 2.2 The Relay Layer: Who's Filtering Your Transactions

**Relay market share (24h)**:

| Rank | Relay | Stance | Share |
|------|-------|--------|-------|
| 1 | Ultra Sound | Neutral | 29.8% |
| 2 | Titan Relay | Neutral | 23.6% |
| 3 | bloXroute Max Profit | **OFAC** | 17.5% |
| 4 | bloXroute Regulated | **OFAC** | 16.9% |
| 5 | Aestus | Neutral | 6.4% |
| 6 | Flashbots | **OFAC** | 3.2% |

**OFAC censorship aggregate (mevwatch.info)**:

| Metric | Rate |
|--------|------|
| Current censorship rate | **37.6%** |
| Historical peak | 94.8% |
| Historical trough | 23.8% |

Translation: OFAC is the U.S. Treasury's sanctions enforcer. It requires regulated entities to filter transactions involving sanctioned addresses (Tornado Cash, etc.). 37.6% of blocks go through OFAC relays — meaning **one out of every three transactions you send is filtered through U.S. Treasury compliance.** This isn't a hypothetical threat. It's live, and the trend is up — from 23.8% to 37.6%.

### 2.3 The History: Winners, Losers, and the Vanished

Rated.network Builder Landscape, all-time data:

| Builder | All-Time Blocks | All-Time Share |
|---------|----------------|----------------|
| Beaverbuild | 2,131,184 | 35.67% |
| Titan | 1,383,895 | 23.16% |
| Rsync | 769,047 | 12.87% |
| Flashbots | 563,134 | 9.42% |

Now compare to today:
- Beaverbuild: 35.67% → **0.3%** (walked away voluntarily, not defeated)
- Titan: 23.16% → **54.4%** (more than doubled)
- Rsync: 12.87% → **gone** (obliterated)
- Flashbots: 9.42% → pivoted to BuilderNet, not directly comparable

The subtext: **the builder market doesn't converge toward equilibrium. Winner takes all. Losers vanish. This market is structurally non-linear — there's no stable middle ground.**

Beaverbuild's exit deserves particular attention. The former #1 decided centralized builders are unsustainable and pivoted to building a decentralized alternative. When the oligopoly itself says the model is broken, that's as damning as it gets. But here's the irony: by leaving, it created a 35% vacuum — and Titan ate most of it. Doing the right thing made the monopoly worse.

---

## Chapter 3: How Titan Won — The Story of One Exclusive Deal

### 3.1 The Banana Gun Contract

April 2023. Titan held less than 1% market share. It did one thing: signed an Exclusive Order Flow (EOF) deal with **Banana Gun**, a Telegram trading bot.

Banana Gun lets retail users execute DEX trades with one click in Telegram. High volume, fat margins — every builder wanted its order flow. Titan locked it in while Banana Gun was still obscure.

What that deal unlocked:

- Titan got private transaction flow no other builder could see
- Private order flow → more profitable blocks → higher bids → more slots won → more market makers willing to give Titan exclusive flow
- Once the positive feedback loop started, it never stopped

Omni Network CEO Austin King asked the uncomfortable question publicly, in PANews:

> "Why did Banana Gun route nearly all of its bundling to Titan, which held less than 1% market share? Did Titan strike a multi-million-dollar deal with the Banana Gun team in the early days? Is Titan promising kickbacks to Banana Gun's team while harming its users?"

These questions have never been answered.

### 3.2 787x: The Efficiency of Monopoly

Public data as of August 2024 (source: Rated.network / PANews — note this is nearly two years old now):

| Builder | Blocks | Total Profit | Profit per Block |
|---------|--------|-------------|-------------------|
| Flashbots | ~550,000 | **16.7 ETH** | ~0.00003 ETH |
| Titan | ~600,000 | **13,151 ETH** | ~0.022 ETH |

Flashbots built 550,000 blocks and made 16.7 ETH.

Titan built 600,000 blocks — roughly the same — and made **13,151 ETH**.

The math: 13,151 / 16.7 = **787.5x**.

That 13,151 ETH (~$44 million at the time) didn't come from competitive bidding. It came from **monopoly rent**. In many slots, Titan was the only builder with enough private order flow to construct a viable block. It didn't have to return MEV to validators through bids. It could keep it.

Flashbots' model: serve validators. Competition pushes profits forward. Titan's model: serve itself. Exclusive order flow eliminates competition.

### 3.3 March 2026: $34 Million, One Block

March 13, 2026. The largest and most controversial MEV event in Ethereum's history.

**What happened:**
- A trader (later identified by Lookonchain as possibly Garret Jin) tried to swap ~$50 million of aEthUSDT to aEthAAVE on CoW Protocol
- Whether it was a fat-finger error or a protocol routing issue, the trade created extreme price impact
- Titan's searcher captured it and ran a sandwich
- Attack logic: front-run buy AAVE → user trade executes at extreme price → back-run sell AAVE

**Result:**
- The trader got back **$35,000**. Fifty million became thirty-five thousand. A 99.93% loss.
- Titan extracted approximately **$34 million** in ETH profit (BeInCrypto reports $34M; GitHub on-chain forensics show $33.1M net after searcher fees)
- For that 24-hour window, Titan was the highest-revenue entity in all of DeFi — above Tether, above Circle

Some observers suspect the trade was money laundering or capital redistribution. Honestly, a $50M swap with that kind of slippage — even a beginner wouldn't do it. But the truth of intent doesn't matter. What matters is what this exposed:

1. **Builder searchers don't care about users.** Titan's searchers are vertically integrated with the builder. They have every incentive to extract maximally.
2. **PBS has no victim protection.** Validators just pick the highest bid. They don't know and don't care what's inside the block.
3. **A single builder can extract tens of millions of dollars in seconds.** That's a single point of failure no decentralized system should permit.

---

## Chapter 4: Beaverbuild — The Oligopolist That Quit

### 4.1 The Former King

From 2022 through early 2025, Beaverbuild held 35–50% of builder market share. Largest centralized builder in the game. Duopoly with Titan.

Same playbook: exclusive order flow (Asian exchanges and market makers), vertically integrated CEX-DEX arbitrage searchers, high bids to maintain share.

### 4.2 Voluntary Exit

**May 6, 2025. Beaverbuild announced it was shutting down its centralized builder and moving its entire team to BuilderNet** — the Flashbots-led decentralized mempool and block building platform. The statement was clear:

> "Beaverbuild is retiring their centralized block builder to work full time on BuilderNet, a decentralized mempool and block building platform for Ethereum."

This event is heavily underrated. It reveals three things:

1. **The oligopoly itself admits centralization is unsustainable.** Not defeated. Not outcompeted. The market leader voluntarily relinquished its position to build a decentralized alternative. That's the strongest possible indictment of the centralized builder model.

2. **BuilderNet got its most valuable acquisition.** Beaverbuild's engineering talent and order flow network were integrated into BuilderNet, growing it from zero to 15.1% share (now the third-largest builder). BuilderNet's smartest strategic move to date.

3. **BuilderNet still depends on Flashbots.** Yes, there are members like Nethermind and Beaverbuild. But Flashbots controls the core architecture and roadmap. Centralized builder → centralized alliance. Is that really a solution?

### 4.3 The Paradox

Beaverbuild did the right thing — and made centralization worse.

Two oligopolists (Titan + Beaverbuild). One quits. Titan goes from 23% to 54%. The 35% vacuum didn't spawn new competitors — Titan absorbed nearly all of it.

Hypothetical: **What if Titan loses Banana Gun and other EOF providers tomorrow?** 54.4% of blocks suddenly produced by second-tier builders. MEV extraction efficiency might drop. But the real question: who fills a 54.4% hole?

---

## Chapter 5: The Abuse Playbook — Five Attack Vectors

These aren't theoretical. Most have been observed at some scale already.

### 5.1 Vector 1: Industrialized Sandwiching

**The play**: Builder uses vertically integrated searchers to systematically sandwich every large transaction flowing through public mempools and private order flow.

**Current capability:**
- Titan's 54.4% means it wins more than half of all slots
- That's roughly one sandwich opportunity every 22 seconds
- March 2026 proved single attacks can yield $34M

**Room to escalate:**
- Selective exemption: leave Banana Gun users alone, extract maximally from everyone else
- Transaction delay: if Titan wins consecutive slots, hold profitable transactions for the next slot so searchers get more prep time
- Cross-block sandwiching: use consecutive slots for multi-block arbitrage

**If Titan hits 80%+ — DEX users face systemic slippage. DeFi composability unravels.**

### 5.2 Vector 2: Time-Bandit Attacks and Reorgs

**The play**: Submit different block versions to different relays in the same slot. Exploit information asymmetry.

Here's the sequence:

```
1. Titan wins slot N
2. Submits Block X (normal) to Relay A
3. Submits Block Y (attack) to Relay B
4. Block X confirms first → an exchange confirms a deposit
5. Titan ensures Relay B's version becomes canonical → the deposit block is reorganized
6. Titan walks away with free deposits (double-spend equivalent)
```

**Is this feasible?**
- Needs consecutive slots or fork creation
- PoS reorg costs are far lower than PoW (only validator slashing, no re-mining)
- If Titan has private deals with large validators, reorg probability rises sharply

**Precedent exists**: EigenPhi's 2024 report documented multiple instances of builders submitting conflicting blocks to different relays. Currently labeled "bid optimization." Technically? Reorg rehearsals.

### 5.3 Vector 3: Censorship by Compliance

**The play**: Decide which transactions enter blocks. Which means deciding which never do.

**Current state:**
- 37.6% of blocks go through OFAC relays (mevwatch.info)
- Titan's own relay is labeled "neutral," but where is its parent company registered? Is compliance pressure real? Unknown.
- bloXroute's two OFAC relays total 34.4%

**Escalation path is clean:**
1. OFAC sanctions list expands → regulated builders must comply
2. "Passive censorship" is far more insidious than active censorship — you don't delete transactions, you just "don't include" them. Undetectable. Unprovable.
3. Creep: starts with OFAC list, spreads to "risky" addresses, spreads to anything the builder doesn't like
4. At 67%+ — a single builder can implement a soft fork, permanently excluding specific transactions

**The paradox**: Ethereum's censorship-resistance story relies on "enough validators and relays are neutral." But if the builder layer is captured, relay neutrality means nothing. Validators choose from blocks builders offer. And builders can simply not offer certain transactions.

### 5.4 Vector 4: Monopoly Pricing — The Invisible Builder Tax

**The play**: Dominant builder systematically suppresses bids, keeping more MEV for itself. An invisible tax on every user.

**The economics are straightforward:**
- In competition, builders bid close to MEV levels
- Titan controls 54.4% — in more than half of slots, there's no effective competition
- It can compress bids without risking slot loss

**Do the math:**
- MEV-Boost average payment: 0.00903 ETH/block (mevboost.pics)
- If full competition would yield 0.015 ETH/block, Titan's monopoly withholds roughly **$20 million per year** from validators and stakers
- That's a silent haircut on ETH staking yield

**The sneakier version**: Builders offer validators "signing bonuses" or kickbacks to accept blocks exclusively from them. PoW mining pool era had this (fee withholding under FPPS). PBS has a perfect analogue.

### 5.5 Vector 5: Information Asymmetry — Seeing the Whole Board

**The play**: Builders with EOF see every incoming transaction. They're the most informed entity on the network.

**What Titan actually sees:**
- Through Banana Gun and other EOF deals: all incoming retail trades before execution
- Combined with public mempool data: near-perfect short-term price prediction
- This predictive capacity can be monetized through proprietary trading or data sales

**The systemic problem**: The builder has a complete order-book view. Everyone else sees fragments. In traditional finance, this is insider trading — criminal territory. In crypto, it's a protocol-granted advantage: not illegal, so undefined and unprosecutable.

---

## Chapter 6: Systemic Risk — How Bad Is This?

### 6.1 Risk Matrix

| Threat | Trigger | Probability | Impact | Level |
|--------|---------|-------------|--------|-------|
| Industrialized sandwiching | Share >50% | **High** | ETH price discount, DeFi exodus | 🔴 Critical |
| Regulatory censorship | OFAC expansion | **High** | Censorship-resistance narrative collapses | 🔴 Critical |
| Malicious reorgs | Builder+validator collusion | Medium | Exchange trust destroyed | 🟡 High |
| Builder tax | Sustained oligopoly | **High** | Silent erosion of staking yield | 🟡 High |
| Builder sudden exit | EOF deal terminated | Medium | Short-term network chaos | 🟢 Medium |

### 6.2 PBS: The Design That Backfired

PBS was built to prevent validator centralization from MEV. Instead, it created a more dangerous concentration point — the builder layer:

```
PoW risk: Miner centralization
  → Needs hardware investment → physical barrier
  → Multiple pools competing → dispersed shares

PoS+PBS risk: Builder centralization
  → No hardware needed, just order flow → lower barrier, deeper moat
  → Winner-take-all dynamics → natural monopoly
```

**The absurdity**: The validator layer is decentralized (thousands of entities). But they have zero power over the one thing that should be decentralized — block content. The builder layer is hyper-centralized (1–2 entities). And it holds exactly that power — transaction ordering, inclusion, exclusion.

### 6.3 The Most Probable Black Swan: Regulatory Capture

A scenario that requires no hack:

```
Late 2026 → U.S. Congress passes the Digital Asset Transaction Transparency Act
→ All U.S.-operating builders must use OFAC-compliant relays
→ Titan's parent company (possibly U.S.-registered) chooses compliance
→ OFAC censorship surges from 37.6% to 80%+
→ Tornado Cash, mixers, unregistered DeFi transactions systematically excluded
→ Ethereum's censorship-resistance narrative terminates
```

No exploit. No attack. One regulation. **A single builder's compliance decision determines the network's censorship level.** That's not a security vulnerability — it's a design flaw.

---

## Chapter 7: The Solutions — None of Them Work Yet

### 7.1 Six Paths, Six Problems

| Solution | Mechanism | Status | Weakness |
|----------|-----------|--------|----------|
| **ePBS** | Builder market in protocol layer | R&D (2–3 years) | Can it eliminate EOF advantage? Unclear |
| **BuilderNet** | Multi-builder shared order flow | Live (15% share) | 12-hour complete outage in 2025 |
| **SUAVE** | Cross-chain MEV public auction | Testnet | Too complex, never validated |
| **Encrypted mempool** | Transactions encrypted until confirmation | Academic | Terrible UX, high latency |
| **FOCIL** | Force builders to include specified transactions | Proposal stage | Doesn't touch EOF problem |
| **Inclusion Lists** | Validators mandate included transactions | Discussion | Increases validator burden |

### 7.2 The Honest Answer

**Nothing works right now.**

The reason is simple: every technical solution fights over "how to distribute MEV." But the source of MEV — exclusive order flow — is a **business problem, not a technical one.**

As long as that exclusive contract between Banana Gun and Titan exists, no protocol-level fix touches the root of the monopoly.

Three things that might actually work:
1. **Mandatory open order flow auctions** — protocol-level prohibition of exclusive routing
2. **Antitrust enforcement** — if builders count as financial market infrastructure, traditional antitrust law applies
3. **L2-native MEV isolation** — transactions ordered at L2, L1 builders only see pre-sorted aggregates

But all three need 3–5+ years. Until then, Ethereum has to live with an uncomfortable fact: **a single company builds its blocks.**

---

## Chapter 8: Conclusion

### 8.1 Five Confirmed Realities

1. **Titan went from participant to ruler.** 54.4% isn't the outcome of competition — it's the compounding of one EOF deal in 2023. The builder market has a natural monopoly tendency. The data is in. This is settled.

2. **Beaverbuild's exit accelerated centralization.** It retired voluntarily in May 2025 — wasn't beaten. But the 35% vacuum it left got mostly absorbed by Titan. That the oligopoly itself abandoned the centralized model is the strongest indictment of that model. But the exit deepened the monopoly.

3. **The builder weapons are armed.** Industrial-scale sandwiching ($34M single attack, verified). Censorship via OFAC relays (37.6% and rising). Monopoly pricing that silently drains validators and stakers.

4. **PBS does not self-correct.** The builder market didn't converge to equilibrium. It converged to monopoly. This isn't growing pains — it's structural failure.

5. **The most underestimated risk is regulatory capture.** Not a hack. A regulation. One builder's compliance decision can determine censorship for the entire network.

### 8.2 Ethereum's Narrative Is Cracking

Ethereum's story rests on three pillars:
- **Decentralization**: no single entity can control the network
- **Censorship resistance**: anyone can send a transaction
- **Permissionlessness**: no one's approval is needed

Builder centralization hits all three:
- Decentralization? 54.4% of blocks are one entity.
- Censorship resistance? 37.6% of blocks are OFAC-filtered, and the trend is up.
- Permissionlessness? Builders can decide your transaction isn't worth including.

The Ultrasound Money narrative was already limping after gas fees collapsed. Now builder centralization is dismantling the story that matters most — that Ethereum is decentralized.

### 8.3 Last Word

Ethereum is a technical marvel. Zero downtime since 2015. Thousands of validators. Trillions in settlement. That's real.

But technical success is not structural health.

The current builder market structure is a **systemic risk.** It won't resolve itself in a technical roadmap. It needs the community to admit the problem exists. It needs developers to design protocol-level interventions. And it needs regulators and market participants to recognize a simple truth:

**A network where a single entity produces over half of all blocks cannot call itself decentralized — no matter how elegant the consensus algorithm underneath.**

---

## Appendix: Glossary

| Term | Full Name | Explanation |
|------|-----------|-------------|
| **MEV** | Maximal Extractable Value | Additional profit block producers can extract from users by ordering, inserting, or excluding transactions. |
| **PBS** | Proposer-Builder Separation | Architecture splitting Ethereum block production into Proposer (validator) and Builder roles. |
| **Builder** | Block Builder | Entity that constructs block content and optimizes transaction ordering to maximize MEV. |
| **Proposer** | Block Proposer | Randomly selected every 12 seconds from the validator set; chooses the highest-bid block from the builder market. |
| **Validator** | Validator | PoS entity running a node with 32 ETH stake. Also the pool from which Proposers are drawn. |
| **Relay** | MEV-Boost Relay | Middleware passing blocks between Builders and Proposers, preventing Proposers from seeing block content and extracting MEV themselves. |
| **Searcher** | MEV Searcher | Entity running algorithms to find MEV opportunities (arbitrage, sandwich, liquidation) in the mempool and submitting bundles to Builders. |
| **EOF** | Exclusive Order Flow | Private transaction flow obtained through exclusive agreements, bypassing the public mempool. The core source of Builder competitive advantage. |
| **Sandwich** | Sandwich Attack | MEV attack where the attacker front-runs a target trade and back-runs after the target pushes the price, capturing the spread. |
| **OFAC** | Office of Foreign Assets Control | U.S. Treasury agency requiring regulated entities (including some Builders and Relays) to filter transactions involving sanctioned addresses. |
| **mempool** | Memory Pool | Collection of pending transactions awaiting inclusion in a block. Builders and Searchers select transactions from here. |
| **slot** | Slot | A 12-second time unit in Ethereum PoS. Each slot allows one Proposer to propose one block. |
| **bid** | Builder Bid | ETH payment a Builder offers to the Proposer to be selected. The channel through which MEV revenue flows from Builders to Validators. |
| **block** | Block | The fundamental unit of the Ethereum blockchain, containing a set of transactions and their final execution state. |
| **order flow** | Order Flow | The stream of user-initiated transactions. Private order flow bypasses the public mempool and is routed directly to specific Builders. |
| **censorship** | Transaction Censorship | The selective exclusion of specific transactions (e.g., those involving sanctioned addresses) by Builders or Relays, preventing them from being included on-chain. |

---

> **ZKLabs | July 4, 2026**
>
> *This paper is based on public data (mevwatch.info, mevboost.pics, CoinMetrics, Rated.network, PANews, BeInCrypto, EigenPhi). Views expressed represent the research team's analytical position.*
