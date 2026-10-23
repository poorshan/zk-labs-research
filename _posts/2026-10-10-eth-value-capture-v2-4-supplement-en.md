---
layout: default
title: "Ethereum Value Capture v2.4 Supplement: Fix Hypotheses and Verification Paths"
permalink: /research/2026/10/10/eth-value-capture-v2-4-supplement-en.html
date: 2026-10-10
categories: research
author: 金戊乾坤2号
lang: en
translation_of: /research/2026/10/10/eth-value-capture-v2-4-supplement.html
parent_report: /research/2026/10/03/eth-value-capture-v2-en.html
data_cutoff: 2026-10-09
version: "English ed. 1.0 | corresponds to Chinese v2.4 supplement"
flagship: false
flagship_summary: "Building on the two breakpoints in v2.0: a three-layer root-cause framework (claim / transmission / premium) and seven fix hypotheses A-G, each with evidence status, economic constraint and failure condition · figures corrected per "v2.0 Errata 1"."
description: "ZK Labs Ethereum value capture special report, v2.4 supplement — building on the two breakpoints in v2.0, a three-layer root-cause framework (claim / transmission / premium) and seven fix hypotheses A-G, each tagged with evidence status, economic constraints and failure conditions; figures corrected per "v2.0 Errata 1"."
tags: [Ethereum, ValueCapture, ETH, IssuanceReform, Blob, Preconfirmation, NativeRollup, Staking, Falsifiability, Research]
---

*Testing potential repair mechanisms, economic constraints and falsification conditions for ETH value capture, built on the eight-segment transmission chain.*

**Institution**: ZK Labs Research ｜ **Version**: v2.4 supplement
**Data cutoff (UTC)**: 2026-10-09 (on-chain snapshot); recomputation definitions as of 2026-10-10 ｜ **Finalized (UTC)**: 2026-10-10
**Status**: `RESEARCH` ｜ no price target, no trading recommendation, no short-term forecast

This chapter supplements v2.0. Every repair proposal is a hypothesis yet to be tested; none of them implies that a fix is already feasible. Each proposal carries its evidence status and failure conditions.

> Note on definitions: figures follow the definitions disclosed in v2.0 and have been corrected per "v2.0 Errata 1". Anything labelled "estimate" is a rough calculation on top of those figures, used only for order-of-magnitude judgement and not as a price forecast.

## Contents {#toc}

- [I. Redefining the core question](#s1)
  - [1.1 Terms, evidence status and shared review criteria](#s1-1)
- [II. Root-cause diagnosis](#s2)
  - [2.0 The three-layer root-cause framework](#s2-0)
  - [2.1 Root cause of breakpoint one: misaligned pricing power + decoupling of issuance from usage](#s2-1)
  - [2.2 Root cause of breakpoint two: absence of institutionally necessary demand](#s2-2)
  - [2.3 The nature of the vacuum period](#s2-3)
  - [2.4 Causal diagram (transmission hypothesis to be tested)](#s2-4)
- [III. Proposal matrix](#s3)
  - [3.1 Proposal A: issuance reform](#s3-1)
  - [3.2 Proposal B: blob fee mechanism and dependency-based tiered pricing](#s3-2)
  - [3.3 Proposal C: preconfirmations and ETH collateral](#s3-3)
  - [3.4 Proposal D: native rollups and built-in verification billing](#s3-4)
  - [3.5 Proposal E: institutional ETH demand](#s3-5)
  - [3.6 Proposal F: price-independent measurement system](#s3-6)
  - [3.7 Proposal G: return of direct L1 activity](#s3-7)
- [IV. Integrated economic assessment](#s4)
  - [4.1 Falsification matrix](#s4-1)
  - [4.2 Settlement share comparison against competing chains](#s4-2)
- [V. Transmission-chain improvement metrics (price-independent)](#s5)
  - [5.1 Five accounts](#s5-1)
  - [5.2 Transmission-chain metrics](#s5-2)
  - [5.3 Competing explanations and disconfirmations](#s5-3)
- [VI. Roadmap and scenario mapping](#s6)
- [VII. Risks and research limitations](#s7)
- [VIII. Conclusion](#s8)
- [Appendix: value capture repair experiments (research plan)](#s9)

---

## I. Redefining the core question {#s1}

The conclusion of v2.0 is that economic value is already created and distributed (segments 1-3 demonstrated), but two disconnects exist between protocol cash flow and eventual token value:

- **Breakpoint one (segment 4→5)**: the fee side is actively compressed by scaling, while demand on the holding side (staking) is not driven by cash flow.
- **Breakpoint two (segment 6→7)**: accumulation of the native collateral asset has yet to show a verifiable monetary or network premium transmission.

This chapter answers three things: what the **root causes** of these two disconnects are; which **mechanism designs** could repair them; and whether those proposals are **economically feasible**.

### 1.1 Terms, evidence status and shared review criteria {#s1-1}

**Terms.** Segment 4 of v2.0 used the term "cash-flow capture". This chapter renames it uniformly to **protocol-layer fee capture** and splits it into three sub-accounts: fee payment (who paid how much), fee burn (how much ETH was burned), and validator fee revenue (priority fees, MEV, preconfirmations, etc.). Base Fee and blob fees are both burned and do not flow into a protocol treasury that can be freely allocated; burn, validator revenue and holder returns therefore cannot be treated as the same thing.

**Evidence-status tags.** Deployed; adopted pending deployment; under research; mechanism inference; external adoption hypothesis. Any unverified claim is tagged "pending verification".

**Note on data reconciliation.** The v2.0 figures cited in this chapter have been independently reconciled; the item-by-item record is in the pre-publication reconciliation checklist and the recomputation log. Three definitional issues were corrected in "v2.0 Errata 1". Readers should note three points: validator execution-layer revenue has been recalculated on the basis of amounts actually received by proposers (the original used a gas priority-fee approximation), with issuance accounting for about 94%; the share of L2 payments to L1 in September 2026 is affected by a single new chain and must be presented both with and without it, alongside the recent-month trend; and every USD figure must state the conversion price and date.

**Shared review criteria (applying to all proposals A-G).** Value capture is not a matter of "the more the better"; it means forming sustainable ETH economic demand without undermining security, decentralization or user competitiveness. Each proposal must answer:

1. How much security cost does the system pay to capture this value?
2. Whose behaviour does the mechanism change?
3. Do users, developers and L2s have cheaper alternatives?
4. Can the new demand persist after subsidies are withdrawn?

## II. Root-cause diagnosis {#s2}

### 2.0 The three-layer root-cause framework {#s2-0}

The two breakpoints are placed in one framework below: which layer each proposal repairs must be stated explicitly.

1. **Claim layer: value creation separated from protocol claims.** Ethereum provides security, DA and settlement, but the commercial value created by those capabilities does not automatically belong to protocol revenue. The question is: who creates value, and who has the right to charge for it?
2. **Transmission layer: protocol revenue separated from ETH economic rights.** Even if the protocol collects fees, it must still be asked whether they are burned, paid to validators, or converted into new staking demand.
3. **Premium layer: ETH demand separated from a sustainable premium.** Demand driven by temporary lockups and issuance subsidies must be distinguished from net demand generated by real economic activity. The question is: why must this demand be met by ETH rather than by another asset?

Two clarifications. First, security and finality have public-good characteristics, but "valuable" does not equal "the protocol has the right to charge by value": the right to charge also depends on protocol design, substitutes, user elasticity and participants' exit options. Second, the "misaligned pricing power" below summarizes a phenomenon; it is not the single, separately identified root cause. Substitute competition, demand elasticity and the value-distribution structure also need to be examined.

Third, **L2 is a spectrum, not a uniform tenant.** Since February 2026, Vitalik Buterin has publicly stated that the earlier vision of L2s as "branded shards" of Ethereum no longer holds: L2 decentralization has progressed more slowly than expected while L1 itself is scaling. He argues for viewing L2s as a continuous spectrum, from being fully secured by Ethereum to having looser trust assumptions; an L2 that manages ETH or Ethereum-based assets should reach at least Stage 1, otherwise it should be regarded as an independent chain. The implication for this paper is that L2s differ greatly in how much they depend on L1 security, so charging them uniformly is conceptually unsound, and judgements about "value leakage" must be layered by dependency; only the part of value that genuinely depends on L1 security and settlement can be discussed in terms of a protocol claim.

### 2.1 Root cause of breakpoint one: misaligned pricing power + decoupling of issuance from usage {#s2-1}

1. **The issuance curve is unrelated to usage.** Under the current mechanism, Ethereum issuance varies mainly with the scale of active staking and protocol parameters, not directly with network usage. When usage fees fall, issuance does not adjust accordingly, so on the basis of amounts actually received by proposers (window 2025-10 to 2026-10), issuance accounts for about 94% of validator revenue (range approximately 93.4%-95.3%).
2. **Staking yield is redistribution, not newly created value.** When yield comes mainly from issuance, stakers' returns equal the dilution borne by non-staking holders. The staking ratio rising to about 36% (total beacon-chain balance about 44.2M ETH, 2026-10-09 snapshot, including pending activations and exits) reflects defensive "anti-dilution" demand rather than an inflow of external value.
3. **L1's public-good attributes lack a charging point.** L1 provides security, DA and finality, yet sells them at close to marginal cost: L2s pay L1 about $2,400-2,600 per day (two definitions), roughly 0.15-0.16% of L2 user fees (September 2026 alone; that month's denominator is inflated by a single new chain, and is about 0.56-0.61% once that chain is excluded). Value is priced at the L2 and application layers; L1 has no exclusive charging mechanism.

### 2.2 Root cause of breakpoint two: absence of institutionally necessary demand {#s2-2}

1. **The unit of account and settlement is not ETH.** Stablecoins (reserves above $311 billion) and RWA are denominated in USD equivalents; ETH is merely an optional collateral asset, not a necessary condition for settlement.
2. **L2 fee revenue is not tied to ETH.** L2 sequencers and operators earn about $1.63 million per day in fees (on a user-paid fee definition), with no obligation to stake, buy back, or hold in ETH.
3. **The premium lacks a verifiable measure.** Without price-independent metrics, the "monetary premium" can only be tagged Unknown, which itself impedes mechanism optimization and verification.

### 2.3 The nature of the vacuum period {#s2-3}

The cost of the old model (platform tolls) has already been realized: mainnet fees contracted by about 79% (rolling 365 days versus the prior 365 days; the window choice changes the magnitude), and deflation has paused. Wholesale revenue under the new model (sovereign settlement base) has yet to take shape. The vacuum between them lies in **not having converted "security and finality" into a service that can be priced and measured**.

### 2.4 Causal diagram (transmission hypothesis to be tested) {#s2-4}

```
Ecosystem economic activity (user demand, settlement, DA, applications)
   ↓ [B · D · G]
Protocol-layer fee capture (usage × unit price; separated into payment / burn / validator revenue)
   ↓ [A · C]
Validator economics and security budget (issuance, usage fees, MEV, preconfirmations)
   ↓ [C · E]
Net new ETH economic demand (new holdings, necessary collateral, persistent lockups)
   ↓ [F runs through the whole chain]
Verifiable monetary and network premium (price-independent metrics first)

Feedback:
① A falling security budget → weakens ecosystem activity and collateral demand
② Rising fees → lower usage or migration of activity
③ ETH price and volatility → changes staking, collateral and margin demand
```

This is a transmission hypothesis to be tested; it does not mean that causal relationships have been established at any link. The scope of A-G is not mutually exclusive, and combined effects cannot simply be added together.

## III. Proposal matrix {#s3}

| ID | Proposal | Breakpoint targeted | Technical feasibility | Economic feasibility | Governance feasibility | Transmission strength | Evidence status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| A | Issuance reform | Breakpoint one | High | Medium (requires a security model) | Medium-low (requires community consensus) | Medium (changes distribution, does not create value) | Under research |
| B | Blob fee mechanism and dependency-based tiered pricing | Breakpoint one | blob fee reserve-price mechanism (EIP-7918) deployed; tiered pricing is mechanism inference | Medium-low (must verify actual fees, usage response and migration risk) | Medium | Weak (significant value capture cannot be derived directly from the reserve-price mechanism) | EIP-7918 deployed (EIP page Final, EF announcement); tiered pricing is mechanism inference |
| C | Preconfirmations and ETH collateral | Breakpoints one and two | Medium-low | Medium | Medium | Medium-high (if revenue is real and collateral is non-substitutable) | Under research / mechanism inference; direction consistent with the based rollup discussed publicly by the founder |
| D | Native rollups and built-in verification billing | Breakpoint one | Low to medium | Medium (revenue effect must be modelled separately) | Medium-low | Medium | Under research; publicly supported by the founder, roadmap progress pending verification |
| E | Institutional ETH demand | Breakpoint two | No protocol change required | Low to medium (substitute assets exist) | External (regulators and institutions) | High but uncertain | External adoption hypothesis |
| F | Price-independent measurement system | Whole chain | High | High (lowest cost) | High | Indirect (used to verify A-E and G) | Research method; no protocol change required |
| G | Return of direct L1 activity | Breakpoint one | High (part of the L1 scaling roadmap is deployed, e.g. EIP-7935 default gas limit of 60M, a default rather than a consensus mandate) | Medium (usage must grow faster than unit price falls) | High | Medium (fees follow usage rather than unit price) | Scaling part deployed; usage return is mechanism inference pending on-chain verification |

See 1.1 for the definition of the status tags. The status of key mechanisms has been checked against primary sources wherever possible; content for which no primary source was obtained is tagged "pending verification" (for example, some of the founder's views are currently drawn mainly from secondary reporting). Mechanisms at the research or design stage should not be read as existing protocol capabilities.

### 3.1 Proposal A: issuance reform {#s3-1}

**Mechanism.** Flatten the relationship between issuance and staking ratio, or set an upper bound on a target staking ratio (the specific range is determined by the security model; this paper does not preset a value), so that issuance scale expands with security needs rather than unconditionally.

**Economic logic (two layers).** On the v2.0 definition, annual validator revenue is about $2.89 billion (converted at the 2026-10-01 spot price; it moves with price; after the correction, about 1.078 million ETH, about $2.91 billion), of which about 94% comes from issuance (proposer-received basis, range 93.4%-95.3%). Issuance is both a security incentive and a distribution mechanism among holders; reducing issuance does not mean reducing social cost by the same amount, nor does it mean increasing the intrinsic value of ETH by the same amount.

- **Static distribution effect**: directly measurable given a staking ratio and issuance volume. The direct effect of lower issuance is mainly a reduction in the dilution borne by non-staking holders; stakers may also benefit from lower dilution, but their nominal yield falls accordingly, and the net effect depends on stakers' cost of capital and holding structure. The staking and non-staking split (about 36% and 64%) cannot be used to derive directly where the value gains accrue.
- **Dynamic equilibrium effect**: issuance reform changes staking participation, validator distribution, attack cost, market equilibrium and the security budget, all of which must be verified with models and cannot be extrapolated from static ratios.

All modelling starts from ETH quantities (issuance, burn, net supply); USD figures are an auxiliary view only, because price changes move the USD value of both issuance and burn.

**Estimate (static scenario, not a forecast).** Issuance reform does not itself create value; it changes the dilution split among holders and the cost of security, so it should be compared across three scenarios with explicit definitions of ETH quantity, USD price assumption, net issuance and validator revenue:

| Scenario | Issuance assumption (ETH/year) | Model inputs | Main research purpose |
| --- | --- | --- | --- |
| Baseline | Current issuance mechanism maintained | Current staking ratio, issuance curve, validator costs, net supply | Establish a baseline for the security budget, net issuance and real revenue |
| Moderate reform | Slower issuance growth | Issuance-curve parameters, staking-ratio response function, validator exit thresholds | Measure changes in dilution distribution and staking behaviour |
| Deep reform | Large issuance cut | Same as above plus attack-cost thresholds and concentration metrics | Test the minimum security budget, validator exits and centralization risk |

The key is not to calculate "how much money is saved" but to find how the economic cost of issuance and the marginal security benefit change under the security constraint.

**Risk.** Lower staking yield will reduce the staking ratio; the impact on decentralization (LST concentration) and the minimum security threshold must be assessed.

### 3.2 Proposal B: blob fee mechanism and dependency-based tiered pricing {#s3-2}

**Mechanism.** Ethereum has already introduced, via EIP-7918, a blob fee reserve price linked to execution-layer prices (the EIP text states its purpose is to make the blob fee market function properly and to have blob users bear at least part of the verification cost they impose on nodes, not to raise rent from L2s). This proposal therefore no longer treats "setting a blob fee floor" as a new recommendation, but instead studies whether differentiated charges can be designed according to how much an L2 actually depends on L1 data availability and settlement. The latter remains a mechanism hypothesis to be tested, and its net impact on L2 costs, usage, alternative DA choices and ETH fee burn must be assessed. Note: a deployed mechanism does not mean the economic effect is verified; actual blob fee changes and burn contribution require separate checks.

**Estimate (scenario assumption, not a forecast).** On the v2.0 definition, L2 daily fee revenue (user-paid fees, per the official growthepie definition, before deducting L1 costs, subsidies and operating costs) is about $1.63 million, or about $595 million annualized. Assuming new charges eventually reach 10% of that scale, about $59.5 million per year; compare with L1's current annual burn of about $65.3 million (monthly $5.44 million × 12). This is an order-of-magnitude comparison only: L2 fee revenue is not the same as the market L1 can charge, since sequencing, proving and infrastructure costs must be deducted and subsidies and differing trust models are embedded, and "10%" is not a derived equilibrium outcome. New capture should be split into unit-price change, usage change and migration effects, which interact and cannot simply be added; USD conversion and statistical windows must be harmonized before comparison.

**Key conclusion.** Even so, this is still far below annual issuance (about $2.89 billion). The **fee route alone therefore cannot restore net deflation**; it can only serve as supplementary revenue and as the establishment of "pricing power", and should not be treated as the main means of value capture.

**Constraint.** The price increase must be smaller than the security loss an L2 incurs by migrating to Alt-DA, otherwise it will amplify the centrifugal force in scenario two.

**Tiering by security dependency.** If L2s sit at different points on the spectrum, a uniform fee is both unfair and likely to trigger migration. It is more reasonable to let fees vary with dependency: L2s that use native verification, reach a higher Stage, and genuinely depend on L1 data availability and settlement should bear matching fees, while weakly dependent L2s should not be regarded as tenants in the first place. At the same time, L1's own scaling (higher gas limits, progressing data scaling) increases block-space supply and lowers unit prices, which further lowers the revenue ceiling of this proposal; and keeping L1 fees sufficiently low is itself a precondition for censorship resistance, so the wholesale price offered to L2s and the retail price paid by users must be designed separately.

### 3.3 Proposal C: preconfirmations and ETH collateral {#s3-3}

**Mechanism.** Based rollups are sequenced by L1 validators, so preconfirmation tips become real validator revenue, and the higher their share, the less validator revenue depends on issuance. At the same time, L2 sequencers would be required or incentivized to post ETH as economic collateral, tying sequencing profit to ETH demand.

**Economic logic.** This is the most direct channel for reconnecting "L2 fee revenue" to ETH: sequencing rights must be acquired through ETH staking, so L2 commercial success translates into structural demand for ETH.

**Risk.** It raises L2 capital costs and operational complexity, and some L2s may choose centralized sequencing to avoid it.

**Evidence level.** Preconfirmation and collateral mechanisms are currently at the design and early pilot stage; the revenue and demand described above are mechanism inference, not observed phenomena.

**External signal.** In early 2026 the founder publicly discussed combining based rollups with low-latency sequencing, and the synchronous composability of L2s and L1, a direction consistent with this proposal. But this is only a design preference; it does not mean the protocol has adopted it, nor that preconfirmation revenue has appeared.

### 3.4 Proposal D: native rollups and built-in verification billing {#s3-4}

**Mechanism.** Provide protocol-level built-in execution verification (such as precompiles), so that L2s do not need to deploy verification contracts themselves and L1 bills by verification workload.

**Economic logic.** For L2s this lowers verification and upgrade costs; for L1 it creates predictable wholesale revenue. This is the mechanism closest to "wholesale pricing" within model B (settlement base).

**Risk.** It depends on the protocol roadmap and engineering cycles; early revenue would be limited.

**Evidence level.** Native rollups and built-in verification are at the research/design stage; whether and when they enter the protocol roadmap must be judged by the latest proposals and implementation progress.

**External signal and tension.** In January 2026 the founder said he was more supportive of native rollups than before, and in February continued to push precompiles for zkEVM proof verification, which raises the priority of this proposal. But the main purpose of native rollups is to make L2s safer and more composable; "billing by verification" is this paper's design choice, not part of that proposal. If verification were made into a near-free public good, L2 costs would fall while L1 revenue might not rise, so the revenue effect must be modelled separately and must not be assumed positive by default.

### 3.5 Proposal E: institutional ETH demand {#s3-5}

**Mechanism.** Encourage stablecoin issuers, RWA platforms and institutional settlement to use ETH staking or "finality insurance" as settlement collateral, with institutions paying for finality; increase the share of ETH-denominated collateral and yield-bearing assets.

**Economic logic.** The key to breakpoint two is "necessity": only when some class of large-scale settlement activity institutionally requires a native collateral asset free of counterparty risk does ETH's network monetary premium have a verifiable source.

**Risk.** It relies entirely on external adoption, with uncontrollable timing and scale; some RWA initiatives are exploring other high-performance chains.

**External signal.** The claim that L2s managing ETH or Ethereum-based assets should reach at least Stage 1 raises the trust threshold for such L2s and is mildly positive for ETH as trusted collateral, but it is only a threshold increase and does not constitute mandatory demand.

**Layering of demand.** Using ETH as collateral does not equal being denominated in ETH, and being denominated in ETH does not equal requiring large ETH holdings for final settlement. Split "structural demand" into four levels of strength:

| Level | Demand type | What it can prove |
| --- | --- | --- |
| D1 | Optional use | ETH is one of the available assets |
| D2 | Operational holding | Participants hold ETH for trading, collateral or liquidity needs |
| D3 | Institutional lockup | Rules or protocols require ETH to be locked continuously |
| D4 | Hard-to-substitute settlement demand | Large-scale activity continuously requires ETH and substitution costs are high |

D4 comes closest to strong structural demand, but it still does not automatically equal a quantifiable monetary premium. Test: when ETH price, collateral ratio or opportunity cost changes, does the demand persist, and can participants switch quickly to substitute assets.

### 3.6 Proposal F: price-independent measurement system {#s3-6}

See chapter V. This proposal has the lowest cost and is the precondition for testing whether A-E work.

### 3.7 Proposal G: return of direct L1 activity {#s3-7}

**Mechanism.** The founder's new positioning is that L1 scales itself and L2s compete on value-add rather than pure scaling. Along this path, more applications and users transact and settle directly on L1. A verified case: the ENS official blog (February 2026) announced that ENSv2 would be deployed on L1 only and that development of Namechain would stop; its claim of an approximately 99% reduction in registration gas costs, and the attribution, are ENS's own statements. L1 fees come from usage growth, not from charging L2s a higher unit price.

**Economic logic.** Fees equal unit price multiplied by usage. Scaling lowers the unit price, so protocol-layer fee capture increases only if demand grows faster than the unit price falls. Low fees are also a precondition for censorship resistance (users must be able to afford L1 fees in order to bypass L2 censorship), so revenue should not be sought by raising prices.

**Relationship to other proposals.** If direct L1 activity rises substantially, proposal B becomes less important; but higher capacity increases state growth and node burden, imposing decentralization costs.

**Evidence and risk.** Some reports say L1 active users are rising while L2 usage falls, but the definitions differ and must be verified with on-chain data. Main risks: the return of users may be short-term migration caused by low prices rather than persistent demand; higher capacity raises node thresholds; and relations with the L2 ecosystem may become strained, possibly accelerating centrifugal force (scenario two).

## IV. Integrated economic assessment {#s4}

| Path | Effect on net supply | Effect on real revenue | Effect on structural demand | Quantifiability |
| --- | --- | --- | --- | --- |
| A Issuance reform | Large (lowers issuance) | Medium (share rises, absolute level falls) | Weak | High |
| B Reserve price and tiered pricing | Small (incremental burn) | Medium | Weak | High |
| C Preconfirmation / collateral | Small | Large (share of real revenue rises) | Medium-large | Medium |
| D Native rollup | Small | Medium | Weak | Medium |
| E Institutional demand | None | None | Large | Low |
| F Measurement system | No direct effect | No direct effect | No direct effect (verification tool) | High |
| G Return of direct L1 activity | Depends on usage and unit price | Medium | Weak to medium | High |

**Three conclusions:**

1. **The leverage on the supply side (A) is far greater than on the fee side (B).** By order of magnitude, cutting issuance changes net supply more than raising fees.
2. **Real revenue (C, D) determines the quality of staking demand.** Shifting validator revenue from issuance towards usage fees is the core of repairing breakpoint one.
3. **The premium (E) is the largest but least certain variable.** Without institutional demand, breakpoint two cannot be closed by protocol-internal mechanisms alone.

### 4.1 Falsification matrix {#s4-1}

Every proposal must define its failure conditions; otherwise it is only an idea, not a research proposal.

| Proposal | Direct effect | Transmission to be verified | Failure signal |
| --- | --- | --- | --- |
| A Issuance reform | Lower issuance and dilution | Security remains acceptable, overall economic cost falls | Validator exits, rising concentration or worsening security margin |
| B Blob pricing and tiered fees | Higher charge per unit of resource | Net fee capture rises, L2 dependency not materially damaged | L2 usage falls, migration rises, net fees do not improve |
| C Preconfirmation and collateral | Generates service fees and ETH lockup demand | Revenue persists, new ETH demand is economically necessary | Revenue driven mainly by subsidies, collateral easily substituted |
| D Native rollup | Improves verification cost and billing | Cost advantage converts into protocol fees or usage growth | Savings stay at the L2, L1 fees do not improve |
| E Institutional demand | Institutions adopt ETH collateral or guarantees | Persistent and hard-to-substitute ETH demand forms | Institutions only use the network without holding or locking ETH |
| F Measurement system | Unified measurement and disconfirmation standards | Mechanism effects can be identified, not merely correlations observed | Metric changes cannot distinguish real demand from subsidies, prices or definitional changes |
| G Return of direct L1 activity | Higher direct L1 usage | Total gas usage grows faster than unit price falls, protocol-layer fee capture rises net | Usage growth is only short-term migration from low prices, fees fall, or rising node requirements drive concentration |

### 4.2 Settlement share comparison against competing chains {#s4-2}

Any charging or tiering proposal must be compared with alternatives, otherwise migration risk is ignored. Comparison questions: how does the settlement share of new institutional, stablecoin and RWA assets change on other high-performance chains or other DA layers; and what are the costs and security losses of migrating an L2 or application off Ethereum. Migration decisions also depend on security assumptions, development costs, liquidity, user experience and operational risk, so "negative net benefit after migration" cannot be treated as a directly observable certainty. Only when the incremental capture from charging is enough to cover the fall in usage, migration and competitive response can a price increase improve net capture; otherwise the higher the charge, the less is captured. Specific data must be collected separately; this chapter does not preset a conclusion.

## V. Transmission-chain improvement metrics (price-independent) {#s5}

### 5.1 Five accounts {#s5-1}

First separate several categories of numbers so that burn, validator revenue and holder returns are not conflated. Base Fee and blob fees are burned: they are neither treasury cash nor validator revenue; priority fees, MEV and preconfirmation revenue accrue to validators; issuance rewards are new supply and create dilution. MEV and preconfirmation revenue must also be labelled separately with source, persistence, and whether they are merely value transfers between participants.

| Account | What is recorded | What must not be mixed in |
| --- | --- | --- |
| Fee payment | Base Fee, blob fees, priority fees and preconfirmation fees actually paid by users, applications and L2s | Application-layer operating revenue, L2 retained profit |
| Fee burn | Quantity of ETH burned | Not treasury cash, and not validator revenue |
| Validator fee revenue | Attributable revenue such as priority fees, MEV and preconfirmations; in MEV-Boost blocks priority fees are collected by the builder and what the proposer actually receives is the builder's bid, so it must be counted on a received basis | Issuance rewards; also not equal to returns for all holders |
| Issuance and dilution | Quantity of newly issued ETH, change in net supply (in ETH quantity first) | USD value (which moves with price) |
| Net new ETH demand | New holdings or collateral still identifiable after deducting stock migration, changes in substitute assets and reward-rule-driven changes | Increases in locked value, increases in USD market cap |

### 5.2 Transmission-chain metrics {#s5-2}

| Transmission link | v2.0 status | Suggested metrics to track |
| --- | --- | --- |
| 4 Protocol-layer fee capture | Partially demonstrated | Three accounts: fee payment, burn (ETH), validator fee revenue; L2's L1 cost share (grouped by Stage level and whether native verification is used, with the rent\_paid definition presented alongside, plus a version excluding the single new chain and the recent-month trend); blob fees as a share of L2 fee revenue; scale of preconfirmation tips; direct L1 usage, split into "per-unit gas fee × total gas usage" |
| 5 Token utility and demand | Partially demonstrated | Actual staking yield (net of issuance dilution), usage fees as a share of validator revenue (on a proposer-received basis, not a gas priority-fee approximation), staking ratio versus deviation from the target range |
| 6 Native asset accumulation | Weak evidence | ETH's share of total DeFi collateral; share of ETH-denominated stablecoins/RWA (counted separately for ETH-denominated, ETH-collateralized and ETH-settled); distribution of coin age of locked assets |
| 7 Monetary and network premium | Unknown | Share of ETH-denominated trading pairs in settlement volume, scale of institutional ETH settlement guarantees, coin-age destruction and holding periods; output of "cannot identify" is permitted |
| 8 Eventual token value | Unknown | Maintain discipline: do not back out from spot price, only record the trends of the metrics above |

### 5.3 Competing explanations and disconfirmations {#s5-3}

Price-independent does not mean causality-independent. Every metric must have its competing explanation stated, together with the conditions under which it should not be believed:

- **Rising staking volume**: may stem from changes in reward rules rather than growth in settlement demand.
- **Rising ETH collateral share**: may stem from shrinking competing assets rather than absolute growth in ETH demand.
- **More ETH-denominated trading pairs**: may stem from exchange product restructuring rather than ETH becoming a more important settlement currency.
- **Longer holding periods**: may stem from lower liquidity or a change in holder structure, and does not necessarily indicate a stronger monetary premium.

This paper does not promise strict causal identification with existing on-chain data, but does promise to list competing explanations and to state honestly in the conclusion which metrics cannot yet rule them out.

The metric system permits the output "cannot identify". Net new ETH demand involves off-exchange collateral, institutional motives and substitute-asset choices, which public on-chain data may not fully identify; in that case it should be labelled honestly rather than forced into a conclusion.

## VI. Roadmap and scenario mapping {#s6}

| Phase | Content | Corresponding scenario |
| --- | --- | --- |
| Near term | Proposal F (measurement), evaluation and discussion of proposal A | Mitigate scenario one (weak transmission persists) |
| Medium term | Proposal B (moderate reserve price), proposal C (preconfirmation and collateral pilots), proposal D | Guard against scenario two (centrifugal force), advance scenario three |
| Long term | Proposal E (institutional demand) | Scenario three (a settlement return channel is established) |

**Note.** L1's own scaling and the spectralization of L2s make the divergence between scenario two (centrifugal force) and scenario three (settlement return) depend more on "the distribution of L2 dependency on L1". The roadmap should add continuous tracking of L2 Stage levels, native verification adoption and based rollup share, and place on-chain verification of proposal G in the near term.

## VII. Risks and research limitations {#s7}

- **Security budget and incentive compatibility:** issuance reform must be subjected to attack-cost analysis and cannot be driven by token economics alone.
- **Migration risk:** adjusting fees too quickly may push L2s to Alt-DA and weaken L1 instead.
- **Data limitations:** estimates are based on the monthly and daily definitions in v2.0; the statistical treatment of L2 retained value (including subsidized chains) significantly affects conclusions and must be rechecked by definition in later versions.
- **Externalities:** proposal E depends on regulation, institutional adoption and competing-chain developments, beyond the protocol's own control.
- **Discipline statement:** this chapter contains no price forecast; any improvement in a metric only represents verification of a transmission mechanism, not a conclusion about price.

* **Sources and timeliness:** information about the founder's views comes mainly from secondary media reports between February and April 2026; the original posts must be checked and any updated statements reviewed before publication. Those views are roadmap preferences, not protocol decisions, and do not mean the related mechanisms are in place.

- **Definitional limits:** validator execution-layer revenue is estimated on the basis of amounts actually received by proposers: relay payments 59,056 ETH (±9.4%, covering 83.6% of blocks, a lower bound), self-built blocks 2,113 ETH; total execution-layer revenue 61,169 ETH; issuance share about 94% (93.4%-95.3%). This estimate is incompletely covered and is a sampled value, usable for directional judgement but not to be cited as a precise figure; the earlier gas priority-fee definition has been superseded.

## VIII. Conclusion {#s8}

Repairing Ethereum value capture should not hinge on a single "raise fees" measure. This chapter only offers testable repair hypotheses, together with their respective economic constraints and failure conditions; they do not mean a repair is already feasible. The more prudent sequence is: first make transmission verifiable through a measurement system with unified definitions, then study the relationship between issuance and the security budget, while testing the net effects of wholesale pricing, preconfirmations and the return of direct L1 activity, and finally observe whether institutional ETH demand emerges. Any mechanism that sacrifices security, decentralization or long-term competitiveness, even if it improves a metric in the short term, should not be regarded as an improvement in value capture.

## Appendix: value capture repair experiments (research plan) {#s9}

Below, proposals A-G are turned into a stepwise verifiable research plan. Principle: test each mechanism independently first, then test combined effects. Combined results cannot be obtained by summing individual estimates, because real fee revenue changes validator behaviour, which in turn affects the staking ratio and the security budget.

1. **Phase one, establish a baseline (proposal F).** Fix the data definitions, measure protocol cash flow, validator revenue, issuance and burn, staking and collateral demand, and distinguish subsidy-driven from non-subsidy-driven changes; at the same time split L1 fees into unit price and usage, and group L2s by Stage level.
2. **Phase two, model the security budget (proposal A).** Build a joint model of the issuance mechanism and security cost, and compare the impact of different issuance curves on dilution, staking ratio, concentration and attack cost.
3. **Phase three, test fee and revenue mechanisms (proposals B, C, D, G).** Test blob tiered pricing, preconfirmation fees, collateral, built-in verification billing and the return of direct L1 activity separately, identifying individual effects first and then assessing combined effects.
4. **Phase four, test structural demand (proposal E).** Investigate which businesses genuinely require ETH collateral or guarantees, quantify the real constraints of substitute assets, capital costs and institutional adoption, and explain one by one why it must be ETH, whether demand would fall sharply with price, and whether participants have an incentive to hold persistently.

**Scope note.** This chapter does not add new repair mechanisms. The estimation templates for A-G (baseline, sensitivity, combined effects) and the pre-publication reconciliation checklist (figures, EIP status, primary sources, deployment progress, terminology consistency, with unverified items tagged "pending verification") are maintained as separate files and are not expanded here.
