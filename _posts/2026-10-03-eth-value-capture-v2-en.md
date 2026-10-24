---
layout: default
title: "Ethereum Value Capture v2.0 — From Protocol Cash Flow to Network Value Transmission"
permalink: /research/2026/10/03/eth-value-capture-v2-en.html
date: 2026-10-03
categories: research
author: 金戊乾坤2号
lang: en
translation_of: /research/2026/10/03/eth-value-capture-v2.html
version: "v2.0 (English ed. 1.0)"
data_cutoff: 2026-10-02
flagship: false
flagship_summary: "Eight-segment transmission chain + four-layer capture framework + five channels · disconfirmation register and monitoring dashboard · every load-bearing figure independently recomputable · UNKNOWN retained as part of the research conclusion"
description: "ZK Labs Ethereum value capture special report v2.0 — reframing the question from 'can ETH capture value' to 'through what transmission mechanism does value reach ETH'; eight-segment transmission chain, four-layer capture framework, five channels, disconfirmation register, monitoring dashboard."
tags: [Ethereum, ValueCapture, ETH, L2, Blob, Stablecoin, Staking, Transmission, Counterfactual, Research]
---

## Ethereum Value Capture v2.0 | From Protocol Cash Flow to Network Value Transmission

<a id="errata-1"></a>

> **"On the Value Capture of ETH" v2.0 Errata 1** ｜ **Version label**: v2.0 Errata 1 ｜ **Publication date**: 2026-10-10 (UTC)
>
> During pre-publication review we found three definitional points in v2.0 that require correction. The original figures are left unchanged; the corrections are set out below. The remaining figures can be reproduced from the same-source data during review; reproduction does not mean the definition has been officially verified, and individual items (such as the `costs_l1_usd` definition for L2 payments to L1, and the active staking set) still await first-hand confirmation.
>
> **Errata 1｜USD conversion price of validator revenue**
>
> The original text converted approximately 1.069M ETH of annual validator revenue into approximately $2.89B using the 2026-10-01 spot price ($2,703.60), not the 365-day average price ($2,514.02). After recomputation per Errata 3, validator revenue is approximately 1.078M ETH (issuance of approximately 1,016,345 ETH plus execution-layer revenue of 61,169 ETH); at the same spot price this is approximately $2.91B, and at the 365-day average price approximately $2.71B.
>
> **Errata 2｜The definition and source of ">11.1% of ETH is locked as collateral/custody"**
>
> The actual meaning of this ratio is: US spot ETF holdings plus listed-company treasury holdings total approximately 13.52M ETH, about 11.1% of 2026-10-01 supply (122,113,302 ETH) (11.07%; range approximately 10.7%–11.4%, since the ETF portion is converted by price and is an estimate). It is **not** a collateral or custody ratio, and it does not include on-chain collateral protocols. Accordingly, the statement in Link 6 of the transmission chain that uses this figure as "sedimentation" evidence should read "institutional holdings", and that link's rating is being re-reviewed separately. Composition and sources:
>
> - US spot ETF holdings of approximately 6.63M ETH (estimated by price conversion);
> - BitMine Immersion (BMNR) 6,001,302 ETH: company press release, published 2026-09-28 (US Eastern time), figure as of 2026-09-27 15:00 (US Eastern time) — original link: [BitMine Immersion Technologies (BMNR) announces ETH holdings reach over 6 million tokens…](https://www.prnewswire.com/news-releases/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-over-6-million-tokens-with-total-crypto-cash--marketable-securities-holdings-of-17-2-billion-302891056.html);
> - SharpLink Gaming (SBET) 888,938 ETH: company 8-K exhibit filed with the US SEC, filed 2026-08-10 (US Eastern time), figure as of 2026-08-03 — original link: [SEC 8-K ex99-1 (CIK 0001981535, accession 0001493152-26-036741)](https://www.sec.gov/Archives/edgar/data/1981535/000149315226036741/ex99-1.htm).
>
> The SharpLink figure used in the original text (892,127 ETH) came from reporting by the on-chain monitoring firm Lookonchain (2026-09-29), not from company disclosure; the disclosed figure is now used instead. The two differ by 3,189 ETH, about 0.003 percentage points, which does not affect the 11.1% conclusion.
>
> **Errata 3｜The definition and value of proposer execution-layer revenue**
>
> The original text stated that "execution-layer tips already include all MEV payments, so 4.96% is an upper bound on usage fees". That statement is **withdrawn**.
>
> **1. Definition correction.** The "tips" in the original text equal total fees minus burn, i.e. the block's gas priority fee, approximately 53,049 ETH from 2025-10-02 to 2026-10-01; issuance over the same period was approximately 1,016,345 ETH. Per public relay data and on-chain checks, in MEV-Boost blocks the gas priority fee is taken by the block's `block.miner` (the builder), and the proposer (validator) receives the bid (`value`) paid by the builder via transfer. Treating the gas priority fee in its entirety as proposer execution-layer revenue therefore does not hold by definition: it both omits the builder's payment and counts the priority fee retained by the builder as proposer revenue.
>
> **2. On-chain check.** Across 132 sampled blocks, the balance of the proposer fee recipient address (`proposer_fee_recipient`) increased by exactly `value` in the corresponding block, with 131 matching within ±1%. The payment channel varies over time: the 2025-10 and 2026-03 samples were direct in-block transfers (43/43 and 49/49 matched transaction by transaction), while the 2026-09 sample shifted to intra-contract transfers (balance differences matched 40/40).
>
> **3. Recomputed result.** 2025-10-02 to 2026-10-01:
>
> - Proposer payments recorded by relays total approximately 59,056 ETH (systematic sampling estimate, standard error approximately 9.4% of the mean, 95% range approximately 48,200–69,900 ETH);
> - Priority fees from self-built blocks (non-MEV-Boost) of approximately 2,113 ETH;
> - Total proposer execution-layer revenue of 61,169 ETH;
> - Corresponding issuance share of approximately **94.3%** (range approximately 93.4%–95.3%), with execution-layer revenue at approximately 5.7%.
>
> **4. How to read it.** The point estimate of 94.3% is below the original 95.04%, but the range contains 95.04%, so one can only say the point estimate is slightly lower, not that the original figure has been overturned. Incomplete relay coverage causes revenue to be understated and the share to be overstated. The direction is unchanged: validator revenue remains predominantly issuance.
>
> **5. Method and limits.** The relay side covers delivery records from 6 relays (flashbots, ultrasound, agnostic, titan, aestus, bloxroute.regulated), sampled as 1 day out of every 5 days with full pagination for that day, covering approximately 83.6% of blocks; some relay endpoints were unreachable, so total revenue is a lower bound and the share is correspondingly high. The mechanistic reading that "priority fees accrue to the builder" comes from the 132-block sample described above and was not verified block by block for the full year. The foregoing is the available evidence as of 2026-10-10; it does not constitute a conclusion about future values, nor investment advice.
>
> **Supplementary notes**
>
> 1. "Average burn/issuance of 19.7% after 4844" covers 2024-03-13 to 2026-10-01. Broken into periods, 4844 to Fusaka (2025-12-03) is 28.58%, and after Fusaka 2.47%. The latter is closer to the current state; this note only describes the periods and does not imply a judgment about causes.
> 2. The 0.146% L2-to-L1 payment share in the text is a single-month value for September 2026, a month in which the denominator was inflated by a single new chain; under the same definition, August was approximately 0.42%. That single-month value should not be treated as a typical level.
>
> **Related**: for the repair mechanisms and verification paths involved in this correction, see the v2.4 supplement chapter of "On the Value Capture of ETH" published the same day — [Repair Hypotheses and Verification Paths](/research/2026/10/10/eth-value-capture-v2-4-supplement-en.html).


**Topic**: Ethereum Value Capture ｜ **Version**: **v2.0**  
**Reference date (UTC)**: 2026-10-02 ｜ **Data cutoff (UTC)**: daily 2026-10-01 / on-chain real-time 2026-10-02 (**all retaining the v1.0 first-hand evidence set; not re-pulled this round**)  
**Status**: `RESEARCH` ｜ no price targets, no trading recommendations, no short-term forecasts  
**Publication Freeze discipline (Publication Freeze ｜ set by research review 2026-10-04)**: once this version enters **final freeze**, **no new data, new metrics, new frameworks, or tier adjustments will be accepted except for P1 hard definitional errors**. **A retained UNKNOWN is itself part of the research output**; "eliminating UNKNOWNs" is not the delivery standard.  
**Author**: ZK Labs ｜ Jinwu Qiankun No. 2 ｜ **This version (v2.0) finalized**: **2026-10-03 16:00 UTC** ｜ **Time definition**: throughout, **always UTC**

> **v2.0 change summary**: **full inheritance of v1.5** + **all 7 P0 audit items landed** + **7 second-round dispositions per the research review directive of 2026-10-03**: **#1 two-column presentation layer ｜ #3 Layer 4 self-limitation ｜ #4 thresholds changed to historical percentiles ｜ #7 EIP-7918 90-day block-by-block evidence ｜ #8 L2 chain-set redefinition ｜ #9 weighted mean and percentile shown side by side ｜ #11 B5 observation item**; **#5 split into "external version + audit working papers"**. **Zero tier changes**; the A3 floor and the A2/B2 thresholds had their **wording and values** adjusted per directives **#12/#13/#14** (not tier changes); "institutional blocking" was changed to "institutional anchoring" per **#15**. **The full version-history narrative (v1.0→v1.5) has been moved into the companion Audit Working Papers**

> **Document-form note**: this file is the **single-file self-contained report** for **v2.0** (single-file form since v1.3). **The companion Audit Working Papers are a separate file** (`ETH_Value_Capture_v2.0_审计底稿.md`), carrying **the version-history narrative, item-by-item disposition records, the load-bearing figure register, self-check corrections, and the recomputation asset index** — **citing this report does not require opening it** — the main text, supporting analysis, evidence and disconfirmation register, monitoring dashboard, and version trail are **all within the same document**; reading this file requires opening no other file. The original 13 split deliverables have been **folded in verbatim** to the sections below (only three pure-pointer paragraphs were deleted and cross-references rewritten; see Appendix C). The original split version is archived byte-for-byte at `../_archive/v1.3_13files/`. The mapping between original files and these sections, reading paths, and terminology conventions are in **Appendix D**.
>
> **Definition reminder**: "this round" always refers to **the logical tightening and elevation round after v1.0 (v1.1→v1.5)**, not the present moment; "mandate brief" refers to the mandate brief for this topic (external input); "§X" in cross-references denotes an internal section of this file.

---

<a id="errata-4"></a>

> **Ethereum Value Capture v2.0 — Errata 4** | **Version label**: v2.0 Errata 4 | **Published**: 2026-10-24 (UTC)
>
> **Erratum 4 | Item count in the v1.3 additions list**
>
> The Chinese source (the "v1.3 additions" bullet) reads "**v1.3 新增八项** (this version's self-check + research review)" — eight new items — while the list that follows actually contains ten items, ①–⑩. Items ⑨ "Originated" and ⑩ "earliest verifiable implementation" were appended later without updating the heading's count. The heading is now corrected to "ten new items"; all other text and every figure are unchanged. This English page follows the corrected source; it previously read "Eight new items in v1.3", which was a faithful translation of the then-uncorrected source.
>
> How to verify: count the item numbers ①–⑩ in the list.

## Table of Contents

- [v2.0 Errata 1 (published 2026-10-10)](#errata-1)
- [v2.0 Errata 4 (published 2026-10-24)](#errata-4)
- [Executive Summary](#executive-summary)
  - [00 Executive Summary](#sec-00-executive-summary)
- [Part I ｜ Main Report (v2.0 body)](#part-i-main-report-v2-0-body)
  - [01 Value Creation — What Does Ethereum Create?](#sec-01-value-creation-what-does-ethereum-create)
  - [02 Value Distribution — Who Captures the Value?](#sec-02-value-distribution-who-captures-the-value)
  - [03 ETH Value Capture Framework v2.0 (Four Layers)](#sec-03-eth-value-capture-framework-v2-0-four-layers)
  - [04 L2: Value Retention vs Network Expansion (Mandate Brief §8)](#sec-04-l2-value-retention-vs-network-expansion-mandate-brief-8)
  - [05 Blob / DA Economics](#sec-05-blob-da-economics)
  - [06 Staking / Security Economics](#sec-06-staking-security-economics)
  - [07 ETH Collateral / Asset Demand](#sec-07-eth-collateral-asset-demand)
  - [08 Stablecoin / RWA Transmission](#sec-08-stablecoin-rwa-transmission)
  - [09 Value Not Captured by ETH](#sec-09-value-not-captured-by-eth)
  - [10 Counterfactual Value Capture](#sec-10-counterfactual-value-capture)
  - [11 Evidence Matrix](#sec-11-evidence-matrix)
  - [12 What Is Proven / What Is Not Proven](#sec-12-what-is-proven-what-is-not-proven)
  - [13 3–5 Year Value Capture Scenarios](#sec-13-3-5-year-value-capture-scenarios)
- [Part II ｜ Final Conclusions (v2.0 final)](#part-ii-final-conclusions-v2-0-final)
  - [I. Answer to the Mandate Brief's Ultimate Question](#sec-1-the-answer-to-the-mandate-brief-s-ultimate-question)
  - [II. Link-by-Link Chain Annotation (Mandate Brief §23 mandatory format)](#sec-2-segment-by-segment-chain-annotation-mandate-brief-23-mandatory-format)
  - [III. Mandate Brief §17: Structural Migration — "Observable Mechanism-Composition Tilt" Must Be Separated from "Value Capture Migration"](#sec-3-mandate-brief-17-structural-migration-the-observed-mechanism-mix-tilts-and-val)
  - [IV. Core Conclusions (against the draft framework in Mandate Brief §18, rewritten sentence by sentence according to the evidence)](#sec-4-core-conclusion-against-the-18-draft-framework-in-the-mandate-brief-rewritten-)
  - [V. Value Capture Transmission Status (Replaces v1.0's "0/4")](#sec-5-value-capture-transmission-status-replacing-v1-0-s-0-4)
  - [VI. The Largest Unknown Variables (Inherited + Update Priority)](#sec-6-the-largest-unknown-variables-carried-forward-updated-priorities)
  - [VII. Research Discipline Statement](#sec-7-research-discipline-statement)
  - [VIII. Closing Status](#sec-8-closing-status)
- [Part III ｜ Criteria and Conceptual Audit](#part-iii-criteria-and-concept-audit)
  - [I. Adjudication Principles of the Audit](#sec-1-judgment-principles-of-the-audit)
  - [II. Item-by-Item Conceptual Audit](#sec-2-concept-by-concept-audit)
  - [III. Item-by-Item Re-Examination of the Mandate Brief §16 Strong Conclusions](#sec-3-item-by-item-re-review-of-the-mandate-brief-16-strong-conclusions)
  - [IV. List of Statements Deleted/Replaced in This Round (substitute directly when writing)](#sec-4-list-of-phrasings-deleted-replaced-this-round-substitute-directly-when-writing)
  - [V. The Audit's Own Boundaries (what this round does not resolve)](#sec-5-the-audit-s-own-boundaries-what-this-round-does-not-resolve)
- [Part IV ｜ Transmission Framework (eight-stage chain / four layers / 2×2)](#part-four-transmission-framework-eight-segment-chain-four-layers-2-2)
  - [I. Positioning of the Framework (why it can extend beyond the ETH topic)](#sec-1-positioning-of-the-framework-why-it-extends-beyond-the-eth-topic)
  - [II. The Trichotomy: Value Creation ≠ Value Capture ≠ Cash Flow (Mandate Brief §15)](#sec-2-the-trichotomy-value-creation-value-capture-cash-flow-brief-15)
  - [III. The Eight-Stage Transmission Chain and Per-Link Status (Mandate Brief §2 / §23)](#sec-3-the-eight-segment-transmission-chain-and-per-segment-status-brief-2-23)
  - [IV. The Four-Layer Value Capture Framework v2.0 (Mandate Brief §4)](#sec-4-the-four-layer-value-capture-framework-v2-0-brief-4)
  - [VI. ETH Demand-Supply Absorption Framework (Mandate Brief §5)](#sec-6-eth-demand-supply-absorption-framework-brief-5)
  - [VII. Transmission Mechanism Four-Question Criteria (mandatory throughout)](#sec-7-the-four-question-criterion-for-transmission-mechanism-mandatory-throughout)
  - [VIII. Application Boundaries of the Framework](#sec-8-application-boundaries-of-the-framework)
  - [IX. Version Discipline](#sec-9-version-discipline)
- [Part V ｜ Value Distribution Matrix](#part-five-value-distribution-matrix)
  - [I. Three-Part Framework (replaces v1.0's "Value Creation → Leakage")](#sec-1-three-stage-framework-replacing-v1-0-s-value-creation-leakage)
  - [II. Value Distribution Matrix ｜ 2026-09/10 definition (all retaining v1.0 first-hand data)](#sec-2-value-distribution-matrix-2026-09-10-definition-all-reusing-v1-0-primary-data)
  - [III. "Which Values Are Not Captured by ETH?" — Strict Adjudication](#sec-3-which-value-was-not-captured-by-eth-strict-adjudication)
  - [IV. Mandate Brief §8: Value Retention vs Network Expansion (L2 upgrade)](#sec-4-brief-8-value-retention-vs-network-expansion-the-l2-upgrade)
  - [V. The Second Case of the Trichotomy: Stablecoin (Mandate Brief §10 + §15)](#sec-5-the-second-case-of-the-trichotomy-stablecoin-brief-10-15)
  - [VI. Uncertainties in This Section (must not be omitted)](#sec-6-uncertainties-in-this-section-not-to-be-omitted)
- [Part VI ｜ Counterfactual (absent Ethereum, where would the value go)](#part-six-counterfactual-absent-ethereum-where-would-the-value-go)
  - [I. Methodology: Three-Part Counterfactual Adjudication](#sec-1-methodology-three-tier-adjudication-of-counterfactuals)
  - [II. Stablecoin: Ethereum vs Tron vs Solana vs Other rails](#sec-2-stablecoin-ethereum-vs-tron-vs-solana-vs-other-rails)
  - [III. L2: Ethereum settlement vs Alternative DA vs Independent L1](#sec-3-l2-ethereum-settlement-vs-alternative-da-vs-independent-l1)
  - [IV. Collateral: ETH vs BTC vs Stablecoin vs Tokenized Treasury](#sec-4-collateral-eth-vs-btc-vs-stablecoin-vs-tokenized-treasury)
  - [V. Settlement: Ethereum vs Alternative blockchain vs Traditional financial rails](#sec-5-settlement-ethereum-vs-alternative-blockchain-vs-traditional-financial-rails)
  - [VI. Summary of the Four Adjudications](#sec-6-summary-of-the-four-adjudications)
  - [VII. Three Self-Limitations of This Module](#sec-7-three-self-limitations-of-this-module)
- [Part VII ｜ Evidence Register](#part-vii-evidence-register)
  - [0. Explicit "No Re-Search" Declaration](#sec-0-explicit-no-re-search-declaration)
  - [1. New Evidence (N1–N5)](#sec-1-new-evidence-n1-n5)
  - [2. Items in v1.0 That Require "Re-Labelling" Because of This Round's Conceptual Corrections (not new evidence, but a definition upgrade)](#sec-2-v1-0-entries-that-require-relabeling-because-of-this-round-s-conceptual-correc)
  - [3. Volume Reconciliation of First-Hand Data on Machine (proving "retention" rather than "redo")](#sec-3-volume-reconciliation-of-first-hand-data-on-this-machine-evidence-of-retention)
- [Part VIII ｜ Disconfirmation Register](#part-viii-disconfirmation-register)
  - [I. Remapping of v1.0 Disconfirmations (old conclusions → v1.1–v1.4 status)](#i-remapping-of-v1-0-disconfirmations-old-conclusions-v1-1-v1-4-status)
  - [II. Inherited Items (still valid among v1.0 disconfirmations, not weakened this round)](#ii-carry-over-items-still-valid-among-v1-0-disconfirmations-not-weakened-this-ro)
  - [III. Disconfirmations of New Load-Bearing Judgments in v1.1–v1.5 (CE-1…CE-12 newly added in this register)](#iii-disconfirmations-against-the-new-load-bearing-judgments-of-v1-1-v1-5-ce-1-ce)
  - [IV. This Report's Own Methodological Errors (deliberately logged, new in v1.1–v1.5)](#iv-this-report-s-own-methodological-errors-proactively-traced-new-in-v1-1-v1-5)
  - [V. Distribution of Conclusion Confidence (re-sorted by v1.1–v1.4 status labels)](#v-distribution-of-conclusion-confidence-re-sorted-by-v1-1-v1-4-status-label)
- [Part IX ｜ Monitoring Dashboard](#part-ix-monitoring-dashboard)
  - [Differences from the v1.0 Dashboard (version change log)](#differences-from-the-v1-0-dashboard-version-change-record)
  - [Above-the-Fold Summary ｜ 4 Core Readings (new in v1.4)](#front-screen-summary-4-core-readings-new-in-v1-4)
  - [Group A ｜ Protocol Capture (protocol cash flow)](#group-a-protocol-capture-protocol-cash-flow)
  - [Threshold Calibration Method: Historical Percentiles (new in v2.0 ｜ research review directive #4)](#threshold-calibration-method-historical-percentiles-new-in-v2-0-research-review-)
  - [Group B ｜ Settlement Capture (settlement and DA)](#group-b-settlement-capture-settlement-and-da)
  - [L2 Chain-Set Redefinition: By "Whether It Settles to Ethereum" (new in v2.0 ｜ research review directive #8)](#l2-chain-set-redefinition-by-whether-it-settles-to-ethereum-new-in-v2-0-research)
  - [Group C ｜ Asset Capture (assets and collateral)](#group-c-asset-capture-assets-and-collateral)
  - [Group D ｜ Monetary Capture (currency and network position)](#group-d-monetary-capture-money-and-network-position)
  - [Event-Driven Observations (no scheduled runs required)](#event-driven-observations-no-need-to-run-periodically)
  - [Two-Column Presentation of Evidence: Fundamental / Market-implied (new in v2.0 ｜ research review directive #1)](#presenting-evidence-in-two-columns-fundamental-market-implied-new-in-v2-0-resear)
  - [\[UNKNOWN\] Closure Roadmap (by cost-effectiveness)](#unknown-gap-closing-roadmap-by-cost-effectiveness)
  - [Recheck Protocol (four items per round)](#re-check-procedure-four-items-per-round)
  - [One-Click Recheck Script (inherited from v1.0, unchanged)](#one-command-re-check-script-inherited-from-v1-0-unchanged)
- [Appendix A ｜ v1.0 Research Status Inventory](#appendix-a-v1-0-research-status-inventory)
  - [I. Facts Already Demonstrated](#i-facts-already-demonstrated-demonstrated)
  - [II. Facts Partially Demonstrated](#ii-facts-partially-demonstrated-partially-demonstrated)
  - [III. Hypotheses Not Demonstrated](#iii-hypotheses-not-yet-demonstrated-not-demonstrated)
  - [IV. Inferences in the Research (Inference, not Fact)](#iv-inferences-in-the-research-inference-not-fact)
  - [V. Definitional Problems in the Research (the root cause this round must audit)](#v-definitional-problems-in-the-research-root-causes-that-must-be-audited-this-ro)
  - [VI. Load-bearing Conclusions to Revise](#vi-load-bearing-conclusions-to-revise-this-round)
  - [VII. Parts of v1.0 That Should Not Be Changed (to prevent erroneous edits this round)](#vii-parts-of-v1-0-that-must-not-be-changed-to-prevent-mistaken-edits-this-round)
- [Appendix B ｜ Preparation Discipline and Mandate Premises](#appendix-b-drafting-discipline-and-task-premises)
  - [0. This Round's Task Discipline (hard constraints, fixed per the research review instruction of 2026-10-02)](#sec-0-task-discipline-for-this-round-hard-constraints-fixed-in-writing-per-research-)
  - [2. This Round's Research Discipline (Mandate Brief §22)](#sec-2-research-discipline-for-this-round-task-brief-22-note-source-jumps-from-0-to-2)
  - [3. The Three Wording Disciplines of This Round](#sec-3-three-expression-disciplines-for-this-round)
  - [4. Conclusion Discipline (the definition adjudicated by research review, continuing this round)](#sec-4-conclusion-discipline-the-definition-ruled-by-research-review-still-in-force-t)
  - [5. What This Round Does Not Do](#sec-5-what-this-round-does-not-do)
  - [6. Version History and Version Discipline](#sec-6-version-lineage-and-version-discipline)
- [Appendix C ｜ Version History and Revision Trail](#appendix-c-version-history-and-revision-trail)
  - [v1.5 → v2.0 (UTC 2026-10-03) ｜ Audit Landing + Directive Handling + Errata](#v1-5-v2-0-utc-2026-10-03-audit-landing-directive-disposition-errata)
  - [Patch-Level Alignment ｜ In-Report Time Definition Changed from "Beijing Time" to "Always UTC" ｜ 2026-10-03 09:16 UTC](#patch-level-unification-in-report-time-definition-changed-from-beijing-time-to-a)
  - [v1.4 → v1.5 (UTC 2026-10-03) ｜ Conceptual Elevation (originally labelled "final candidate" → superseded by v2.0)](#v1-4-v1-5-utc-2026-10-03-conceptual-elevation-originally-labeled-final-draft-can)
  - [v1.3 → v1.4 (UTC 2026-10-03) ｜ Layer 4 Tier Re-Labelling + Three Content Additions](#v1-3-v1-4-utc-2026-10-03-layer-4-status-re-labeling-three-content-increments)
  - [Structural Change ｜ 13 Split Versions → 1 Single-File Self-Contained Version ｜ 2026-10-03 (UTC)](#structural-change-13-split-versions-1-single-file-self-contained-version-2026-10)
  - [v1.2 → v1.3 (UTC 2026-10-02) ｜ Final Logic Audit](#v1-2-v1-3-utc-2026-10-02-final-logic-audit)
  - [v1.1 → v1.2 (UTC 2026-10-02) ｜ 2×2 Capture Matrix Elevated to First-Class Framework Component](#v1-1-v1-2-utc-2026-10-02-the-2-2-capture-matrix-elevated-to-a-first-class-framew)
  - [I. What Changed](#sec-1-what-changed)
  - [II. What Did Not Change (crucial)](#sec-2-what-did-not-change-key)
  - [III. Guidance for Subsequent Citers](#sec-3-guidance-for-subsequent-citers)
  - [Attachment: In-v1.3 Corrections (patch level, no version bump) ｜ 2026-10-03 (UTC)](#appendix-corrections-within-v1-3-patch-level-no-version-number-increase-2026-10-)
  - [1. First, the Parts That Were Checked and Found Correct (positive verification)](#sec-1-parts-first-reported-as-checked-and-error-free-positive-verification)
  - [2. Hard Errors Fixed (all of the "reads fine, does not recompute" type)](#sec-2-hard-errors-already-fixed-all-of-the-reads-fine-does-not-recompute-kind)
  - [3. Verification Results (re-run after revision)](#sec-3-verification-results-re-run-after-revision)
  - [4. Comments Registered but Not Changed / Rejected (with reasons)](#sec-4-opinions-registered-but-not-changed-rejected-with-reasons)
  - [5. Note on Version Semantics](#sec-5-explanation-of-version-semantics)
  - [6. v1.2 Framework Delta QA (2×2 capture matrix elevated to first-class framework component)](#sec-6-v1-2-framework-delta-qa-2-2-capture-matrix-elevated-to-a-first-class-framework)
  - [7. v1.3 Final Logic Audit QA (6 P0 logic tightenings)](#sec-7-v1-3-final-logic-audit-qa-6-p0-logic-tightenings)
  - [8. v1.3 Source Labelling Correction (the provenance of the load-bearing figure $521.6M/month) ｜ 2026-10-03 (UTC)](#sec-8-v1-3-source-label-correction-the-provenance-of-the-load-bearing-figure-521-6m-)
- [Appendix D ｜ File Mapping, Reading Paths, and Terminology Conventions](#appendix-d-file-mapping-reading-path-and-terminology-conventions)
  - [D1 ｜ Original file → this section](#d1-original-file-this-section)
  - [D2 ｜ Mandate Brief §21 Deliverable Coverage](#d2-coverage-of-task-brief-21-deliverables)
  - [D3 ｜ Suggested Reading Paths](#d3-suggested-reading-path)
  - [D4 ｜ Terminology and Coordinate Conventions](#d4-terminology-and-coordinate-conventions)
- [Appendix E ｜ 2026 Key Events and Temporal Discontinuities (new in v2.0)](#appendix-e-key-events-of-2026-and-timing-breaks-new-in-v2-0)
  - [E1 ｜ Event Register](#e1-event-register)
  - [E2 ｜ Temporal Discontinuities (unmarked in v1.5, marked in v2.0)](#e2-timing-breaks-unmarked-in-v1-5-marked-in-v2-0)
  - [E3 ｜ Adjudication Impact (item by item; all chains already supplied above)](#e3-impact-on-judgments-item-by-item-all-supplemented-above)

---

## Executive Summary {#executive-summary}

### 00 Executive Summary {#sec-00-executive-summary}

**Question escalation**: from "Can ETH capture Ethereum's economic value" → "**Through what** transmission mechanism (Transmission Mechanism: who pays / pays in what currency / into whose account / whether burned or locked) **does the economic value Ethereum creates transmit to ETH**".

**Five core conclusions**

1. **Value capture ≠ cash-flow capture.** Cash-flow capture is a **proper subset** of value capture. v1.0 treated it as the whole, which led to "cash flow compressed" being read as "capture weakening". This round splits it into four layers: Protocol Cash Flow ｜ Security / Settlement ｜ Asset / Collateral ｜ Monetary / Network.
2. **Deflation is not a necessary condition.** The correct logic is **Supply Growth vs Demand Growth**; burn / issuance is a **Monetary Supply Indicator**, not a Value Capture Indicator.
3. **L1 execution demand is not the only channel.** The five channels (A execution fees / B L2 settlement / C security staking / D ecosystem collateral / E monetary position) have different preconditions; A is the most effective one, **but not a necessary condition for the other four**.
4. **The chain's breakpoints have been located.** Stages 1–3 (activity, creation, distribution) 🟢 hold; stages 4–5 (protocol capture, demand) 🟡 partially hold, **stage 6 (assets) 🟠 weak evidence** (missing share denominator); **stage 7 (monetary premium) ⚪️ undeterminable** (the only proxy is derived from ETH price → no valid measurement tool); stage 8 is not adjudicated. The breakpoints are specifically in two places: **stages 4→5 are not co-sourced** (capture↓ while demand↑), **and the 6→7 transmission is unconfirmed** (no verifiable transmission has yet been observed between asset accumulation and monetary / network premium).
5. **Mechanism composition is tilting; value capture migration is unproven.** Fee-side compression (burn/issuance 138.7% (2022-09-15→2024-03-12 average) → 19.7% (2024-03-13→2026-10-01 average; ⚠️ both values are window averages for "pre-/post-4844", not current values — current last-30-day 2.52%, last-365-day 2.60%, last-90-day 1.81%) and holding-side growth (staking rate 9.73%→36.09%) are both **measurable facts**; **but a tilt in observable mechanism composition ≠ a completed value capture migration** — as of the current evidence, a verifiable "holding-side growth → ETH economic value" transmission has not formed.


> **【New in v2.0 ｜ P0-1】Four-window comparison of burn ÷ issuance** — the original report gave only "138.7% → 19.7%" without labelling the windows, which is easily read as the current state. Measured (CoinMetrics daily series; script `v2.0/scripts/recompute_burn_issuance_windows.py`):

| Window | Start–end (UTC) | Issuance (ETH) | Burn (ETH) | Burn ÷ Issuance |
|:--|:--|--:|--:|--:|
| Pre-4844 average (post-Merge) | 2022-09-15 → 2024-03-12 (545d) | 1,104,762 | 1,532,286 | **138.698%** |
| Post-4844 average | 2024-03-13 → 2026-10-01 (933d) | 2,492,115 | 491,906 | **19.738%** |
| Last 365 days | 2025-10-02 → 2026-10-01 (365d) | 1,016,345 | 26,469 | **2.604%** |
| Last 180 days | 2026-04-05 → 2026-10-01 (180d) | 516,841 | 13,313 | **2.576%** |
| Last 90 days | 2026-07-04 → 2026-10-01 (90d) | 262,851 | 4,759 | **1.810%** |
| Last 30 days | 2026-09-02 → 2026-10-01 (30d) | 88,728 | 2,236 | **2.520%** |

> **Definition reminder**: 19.7% is a 933-day cumulative average, inflated by the early post-4844 period (when burn was still higher); the current compression is **about 7.8× deeper** than 19.7% suggests. Wherever 19.7% is cited, at least one current-period figure must be given alongside it.

**In one sentence**: **Between Ethereum's value creation and ETH's value capture there is a Transmission Layer that can be located but has not yet been bridged.**

**This round's most important audit outcome**: deleted v1.0's "four necessary conditions 0/4" (fabricated premises + artificial scoring), strictly defined "L2 99.77% retention" as `L1 cost share / gross economic retention`, split "stablecoins transmit nothing" into two channels, issuer / on-chain, downgraded "institutional demand has been disconfirmed" to "transmission not yet demonstrated", and added a **Counterfactual Value Capture** comparison set.

---

## Part I | Main Report (v2.0 body) {#part-i-main-report-v2-0-body}

### 01 Value Creation — What Does Ethereum Create? {#sec-01-value-creation-what-does-ethereum-create}

| Layer | Scale of economic activity | Data |
|:--|:--|:--|
| Transaction activity | L2 **988.3M tx/month (94.6%)**; L1 56.9M tx/month | growthepie / l2beat |
| Gross value of economic activity | **$586.7M/month** (**split definition, includes cross-layer double counting, read as order of magnitude**; all percentages below derived by comparison with L1 fees are **magnitude ratios**) | growthepie |
| Application-layer fees | **$521.6M/month** (**L2 application-layer** fee definition; 2026-09, 26 chains, growthepie 90-day window) | growthepie (⚠️ separately, DefiLlama "2025 chain-level fees" ranks Ethereum 4th = $523.17M, **a different definition from this cell; the close value is pure coincidence and the two do not corroborate each other**) |
| DA usage | blob **154.7 GB/month**; measured 6.35 blobs/block | growthepie / blobscan |
| Security spending | **1,069,394 ETH/year ≈ $2,891M (= $2.891B)** (0.876% of market cap) | CM + on-chain |
| Settlement scale | L2 processes 94.6% of transactions, security re-anchors to L1 | l2beat |

**Adjudication (🟢)**: **Value creation is real, large, and growing.** This layer is not in dispute — the entire dispute is over "who gets it".

#### The Qualitative Shift in the Business Model: From "Platform Toll" to "Sovereign Settlement Base" (v1.5 elevation)

> **All content in this section is an `[INTERPRETATION]` interpretive framework.** It explains what the following set of **already observed facts** means; it **adds no new evidence, changes no tier, and does not speculate about Ethereum's objective function**.

**Observed facts (load-bearing for this report)**: declining unit protocol rent (L1 fees trailing-365d year-on-year **−79.6%**; burn ÷ issuance **138.7% (2022-09-15→2024-03-12 average) → 19.7% (2024-03-13→2026-10-01 average; ⚠️ both values are window averages for "pre-/post-4844", not current values — current last-30-day 2.52%, last-365-day 2.60%, last-90-day 1.81%**) and network scale expansion (L2 carries **94.6%** of transactions, blob **154.7 GB/month**, DA capacity **4.7×**) **occurred in the same period**.

**Interpretive framework ｜ Two business models compared**:

| Dimension | Model A: Platform toll (App Store type) | Model B: Sovereign settlement base (wholesale finality type) |
|:--|:--|:--|
| Revenue object | Levied per instance on **high-frequency end-user interaction** | Levied in bulk on **institutional-scale wholesale settlement and final state confirmation** |
| Pricing philosophy | The **auction price** of scarce block space | The **wholesale / commoditized price** of the clearing base |
| Unit rent | High | Low |
| Source of network effects | Application-layer lock-in (whoever comes, stays) | **Non-substitutability of settlement finality and collateral** |
| Corresponding reading in this report | 1559 boom period (burn ÷ issuance > 100%) | EIP-7918 relative reserve price (measured ratio **0.931**) + L2 settlement anchored to L1 |

**What this framework can and cannot explain**:
1. **Within the on-machine evidence set, the relationship between high fee rates and "application-layer network effects" admits two readings that cannot be distinguished** — see **CE-10** in "Part VIII". This report **does not adopt a single causal statement** ("high fee rates killed the application layer").
2. blob scaling and price reduction (4844 / BPO / EIP-7918) **can be read as evolution under commoditization competition in infrastructure**: when DA supply is substitutable across multiple rails, the window for collecting rent from scarcity alone closes, **and competition shifts to reserve price and finality**. This is `[INTERPRETATION]`; **"inevitability" is retrospective narrative and must not be written as forecast**.
3. **Definition of the so-called "qualitative shift"**: the definition of where ETH value capture is centered is being ceded from "**direct cash-flow sharing** (Protocol Cash Flow)" to "**an irreplaceable underlying base for credit clearing and risk collateral** (Sovereign Collateral)" — that is, from "**how much money do we get**" to "**can anything else replace it**".

**⚠️ Three boundaries (must be read together with the framework)**:
- **"Deliberate shift" cannot be written or inferred**: this report explicitly forbids speculating about the objective function (v1.3 P0-3 ruling). All that may be written is the **observed architectural trade-off**; **whether it is a conscious economic strategy must be proven by governance documents / roadmap**; **v2.0**: the roadmap record can now be named (see "Appendix E"), but **there is still no first-hand basis for answering "intent"**.
- **"Fedwire / Treasury settlement" is an analogy, not an observation**: "Part VI" of this report has already adjudicated that **incremental institutional settlement is landing on other chains** (leading products BUIDL / USYC chose other chains), and that **there is no first-hand data at all on the traditional financial rails side**. The analogy describes a **directional institutional imagination**, **not an achieved position**.
- **Model B revenue has not appeared within the on-machine evidence set**: L1 capture of **$16.0M/month** (magnitude ratio **2.73%**), settlement return flow **$2,387/day** (**0.146% (0.550% after excluding Robinhood)**) — **"base position" currently cannot be exchanged for an observable cash-flow return**. This is another way of stating this report's core open question (the Transmission Layer).

> **⚠️ A tension that must be read against "L1 marginalization" (v1.5 note ｜ not hidden by this report's opponents either)**: the "**upgrade to clearing base**" in this section and the "**L1 marginalization**" observation hypothesis in "Part IX" describe **the same architectural displacement, but are assigned opposite signs** —
> - The former reads it as **moving up**: the execution layer yields, and **finality and security** become the core good being wholesaled;
> - The latter reads it as **moving down**: L1 degrades from "value settlement layer" to "DA / security layer".
> **This report does not choose between these signs** (both layers lack measurable readings). **Only one discriminating quantity can distinguish them: whether finality / security is actually priced** — i.e. whether Group A (L1 fees) can recover structurally. **Until then, "upgrade" and "degradation" are two narratives of the same set of facts, and only one may not be taken**; this report registers them **side by side** precisely so that neither narrative gains default status.

---

### 02 Value Distribution — Who Captures the Value? {#sec-02-value-distribution-who-captures-the-value}

Full attribution across the 11 categories of actors is in `Part V (Value Distribution Matrix)`. Core distribution facts:

| Actor | Receives | Magnitude | Relation to ETH |
|:--|:--|--:|:--|
| Ethereum protocol (L1) | base fee burn + priority fee + blob + settlement gas | **$16.0M/month** (= L1 protocol fees ÷ reported ecosystem gross-value proxy ≈ **2.73%, a magnitude ratio, not a capture rate**) | ✅ Directly collected |
| ETH (all holders) | proportional scarcity from burn | burn **$5.44M/month** | ⚠️ Asymmetric benefit |
| Validators | issuance + tips (including all MEV tips) | **≈ $2,891M/year** (95.04% issuance) | ✅ Composition problem |
| L2 / Sequencers | user fees − L1 cost | **$1,630,763/day gross** | ❌ No return mechanism |
| Applications | own fee revenue (**L2 application-layer** definition) | **$521.6M/month** | ❌ Value outside the protocol |
| Stablecoin issuers | interest on Treasury reserves | reserves $311.18B | ❌ Channel A does not transmit |
| MEV (searcher/builder) | extracted value | `[UNKNOWN]` (validator-side upper bound $143M) | ⚠️ Unmeasurable |
| Users | benefit of lower costs | per transaction $13.21 (2024Q1) → $0.275 (2026Q2) | — |
| Other networks | incremental share | Tron stablecoins 30.0%, Solana 5.3% | ❌ |

**Key conceptual correction (Mandate Brief §7)**: **do not default "not captured by ETH" to "leakage".** Only value that "**could in theory have been captured by ETH through protocol mechanisms but in fact was not**" qualifies as **Value Leakage**. On that basis:
- Application-layer $521.6M/month → **Structurally outside protocol capture** (the protocol never designed a claim)
- L2 retention → **Discretionary non-capture** (collectable but deliberately priced low)
- Net supply dilution → **Monetary supply effect** (not leakage)
- **Conclusion of this round: under the strict definition, no single value flow can be identified as qualifying as Value Leakage**; within the observation set available on machine, the only candidates are the MEV split and the blob opportunity cost, **and neither is measurable**.

---

### 03 ETH Value Capture Framework v2.0 (Four Layers) {#sec-03-eth-value-capture-framework-v2-0-four-layers}

The full seven fields for each layer are in `Part IV (Transmission Framework)` §IV. Summary:

| Layer | Capture mechanism | Key magnitude | Status |
|:--|:--|:--|:--|
| **Layer 1 Protocol Cash Flow** | base fee burn; priority fee → validators; blob burn; L2 settlement gas | $16.0M/month (burn $5.44M) | 🟡 **Partially demonstrated** |
| **Layer 2 Security / Settlement** | settlement anchoring; DA; validator security | settlement $2,387/day (0.146% (0.550% after excluding Robinhood)); blob $234/day | 🟡 **Partially demonstrated** |
| **Layer 3 Asset / Collateral Demand** | native collateral; LST/LRT; ETF/DAT | staking **44,061,701 ETH (36.09%)**; locked **≈13.52M (11.1% of circulating)**; Lido $26.76B | 🟠 **Weak evidence** (missing share definition) |
| **Layer 4 Monetary / Network Premium** | settlement asset; reserve asset; unit of account activity | **ETH-to-Stablecoin Market-Cap Ratio = 1.077** (definition: ETH market cap ÷ all-chain stablecoins; 2.543→1.778→1.182→1.077, four points declining monotonically; on an Ethereum on-chain basis 2.28, same direction). **⚠️ This ratio is a proxy for monetary / network premium, not the premium itself** (affected by ETH price, stablecoin supply, circulating supply, market structure and other factors). **⚠️ v1.4 tier re-labelling: the numerator of this proxy is ETH market cap (= price), so using it to measure premium is proving the point via price and conflicts with No Price Shortcut; this layer's direct evidence (ETH-denominated economic activity) does not even have an indicator definition ⇒ the report has no valid measurement tool, hence changed from 🔴 Not demonstrated to ⚪️ Unknown** | ⚪️ **Unknown** (no valid measurement tool) |

**The criterion running through the whole report (Transmission's four questions)**: who pays? in what currency? into whose account? burned/locked or not? **Inability to answer = Not demonstrated, not "weak".**

---

### 04 L2: Value Retention vs Network Expansion (Mandate Brief §8) {#sec-04-l2-value-retention-vs-network-expansion-mandate-brief-8}

**Two directions, evidence presented side by side, no forced choice:**

**Direction 1 ｜ Network Expansion**  
`L2 Growth → Lower L1 marginal cost → More activity → More settlement/DA → Potential ETH demand`  
Evidence: L2 94.6% of transactions; blob 154.7 GB/month; capacity 4.7×; L2 DA cost per transaction $3.6e-6; L1 block utilization ≈100% of target (30M); **EIP-7918 sets a relative reserve price = `L1 base fee / 16` (a soft lower bound, pulled back dynamically via excess_blob_gas, with multi-block lag)** (measured/reserve price 0.931).

**Direction 2 ｜ Rent Sacrifice**  
`L2 Growth → Sequencer captures economics → L1 fee compression → Lower ETH cash-flow capture`  
Evidence: L1 cost share **0.146% (0.550% after excluding Robinhood)**; L1 fees year-on-year **−79.6%**; burn/issuance **138.7% (2022-09-15→2024-03-12 average) → 19.7% (2024-03-13→2026-10-01 average; ⚠️ both values are window averages for "pre-/post-4844", not current values — current last-30-day 2.52%, last-365-day 2.60%, last-90-day 1.81%**; Coinbase SEC first-hand (Base activity +7× while `Other transaction revenue` −11%).

**Answer: one of three — C, but an "asymmetric C":**

| Option | Adjudication |
|:--|:--|
| Unit protocol rent (originally A, "Maximizing Protocol Rent") | 🟢 **Decline observed** — expansion executed through its own upgrades (4844/Fusaka/BPO1/BPO2) + EIP-7918 price cap + a 0.146% take (0.550% after excluding Robinhood); **objective function not inferred** (v1.3 correction: the original "falsified" wording is void) |
| B. Maximizing Economic Network | **Partially demonstrated** — activity, DA, and settlement anchoring do remain within the ecosystem |
| C. Dynamic balance | **Partially demonstrated, and asymmetric** |

**Where the asymmetry lies**: **the rent-decline side has been observed**, **the return side has not** (network expansion → ETH transmission is at a magnitude ratio of 2.73% in stage 4, and the observable proxy in stage 7 points the opposite way). → **"Ethereum's current architecture exhibits an economic trade-off in which unit protocol rent declines while L2 / DA / settlement activity expands; but as of the current evidence, a verifiable, proportional return of value to ETH has not formed."** This is an **observed trade-off, not a confirmed design objective**, and not a judgment about the future.

#### 04b | What This Trade-Off Means for the Business Model (v1.5 elevation)

**The observed asymmetry**: **the rent-decline side is realized** (L1 fees −79.6%, burn ÷ issuance 138.7% (2022-09-15→2024-03-12 average) → 19.7% (2024-03-13→2026-10-01 average; ⚠️ both values are window averages for "pre-/post-4844", not current values — current last-30-day 2.52%, last-365-day 2.60%, last-90-day 1.81%, L1 cost share 0.146% (0.550% after excluding Robinhood)); **the return side is not realized** (stage 4 magnitude ratio 2.73%, stage 7 has no usable valid measurement tool).

**Interpretive framework (`[INTERPRETATION]`)**: Ethereum's current architecture can be read as shifting from "**levying a platform toll on retail users and high-frequency interaction**" to "**a clearing base wholesaling security and final state confirmation**" — the former collects rent per instance from end-user interaction, the latter prices institutional-scale settlement and finality in bulk. **That shift shows up at the observation layer precisely as the asymmetry above**: **unit rent (the toll) falls first, while wholesale revenue (the base fee) has not yet appeared**.

**⚠️ Three boundaries**:
1. This is an **interpretive framework**, not an adjudication; it **does not infer the objective function** (P0-3 explicitly forbids it).
2. "Wholesale revenue has not yet appeared" **does not equal** "will not appear" — this report is bound to "the current observation window + evidence set + threshold levels" and **does not conclude about the future**.
3. **The direct readings of base position (ETH-denominated economic activity / institutional settlement share) are currently `[UNKNOWN]`** ⇒ the shift **can be neither proven nor disproven**, and this report **registers the direction only, without adjudicating success or failure**.

---

### 05 Blob / DA Economics {#sec-05-blob-da-economics}

| Item | Value |
|:--|:--|
| Parameters (BPO2) | target **14** / max **21**; capacity **4.7×** larger than at 4844 |
| Measured usage | **6.35 blobs/block** (utilization 45% vs target); September definition 39% |
| Unit price | **$0.003015/blob** (10,122,972 wei/blob-gas) |
| **EIP-7918 anchoring** | reserve price = `base_fee_per_gas / 16`; measured/reserve price **mean 0.931**, median 0.928, range [0.741, 1.087] |
| blob revenue | **$143–234/day = 0.026%–0.043% of L1 fees** |
| DA cost allocated per L2 transaction | **$3.6e-6** |

**Mechanism adjudication (🟢)**: **the blob price is no longer determined by blob demand; it is anchored at 1/16 of the L1 execution base fee.** There are two implications: ① **the current rule already establishes a relative reserve price** (= `base_fee_per_gas / 16`, pulled back dynamically via excess_blob_gas), so that "blob charging capacity spiralling down to 1 wei through mechanical reduction" is **no longer triggered by blob demand alone within execution-fee-led intervals** — but this is a **soft lower bound**: the EIP text itself states there is **multi-block lag**, and `MIN_BASE_FEE_PER_BLOB_GAS` remains 1 wei, so the bound is **relative rather than absolute** (**v2.0 correction**; originally written as "price floor / hard floor / guaranteed never to reach zero"); ② **blob revenue is a claim proportional to the L1 execution base fee** (coefficient 1/16 < 1, **not leverage**; **v2.0 correction** of the earlier phrase "leveraged claim") — the currently small value reflects a low base fee regime, **not the strength of the mechanism** (this is `[SCENARIO]` and does not enter the load-bearing conclusions).

---

### 06 Staking / Security Economics {#sec-06-staking-security-economics}

| Item | Value | Implication |
|:--|:--|:--|
| Beacon chain total balance | **44,061,701 ETH (36.09%)** | first-hand, 2,376,110 records in full |
| Effective staking | **43.02M (35.23%)** | the two definitions differ by 2.4% (total balance includes the queue) |
| Active validators | **877,233** | ⚠️ **must no longer be ×32** (Pectra/EIP-7251) |
| Consolidated accounts | **12,092 (1.36%) holding 16,081,362 ETH = 36.49%** | **validator concentration**, not entity concentration |
| CL nominal yield | **2.53%** (4.85% at the Merge) | yield↓ while staking rate↑ → **not yield-driven** |
| security budget | **1,069,394 ETH/year ≈ $2,891M** | 0.876% of market cap, 2.43% of staked market cap ※[Errata ①](#errata-1) |
| **Revenue composition** | **issuance 95.04% / usage 4.96%** | **Nature: dilution protection, not external value capture** |

**Adjudication**: **staking demand is real holding demand, but what it buys is "dilution protection" (a hedge against +0.862%/yr dilution), not external cash flow.** → the **security component** of Layer 2 has status **Demonstrated (composition determines nature)**.

---

### 07 ETH Collateral / Asset Demand {#sec-07-eth-collateral-asset-demand}

| Channel | Magnitude | Strength |
|:--|:--|:--|
| Staking | **44,061,701 ETH (36.09%)** | on-chain first-hand |
| ETF | **≈6.63M ETH (5.43%, estimate ±3–5%)**; cumulative net inflow **+$13.87B** (561 days) | inflow first-hand |
| DAT (BitMine + SharpLink) | 6,001,302 + 892,127 = **6.89M** | company announcements / secondary |
| **Total locked** | **≈13.52M = 11.1% of circulating** | ⚠️ overlaps with staking, **must not be added together** |
| Collateral protocols | Lido $26.76B (≈9.84M stETH = 22.5% of active stake); Aave v3 $18.36B; Morpho $11.25B; EigenCloud $7.10B; ether.fi $5.23B; Kelp $1.14B | DefiLlama |
| Comparison: BTC-side tokenization | **≈$13–14B** (WBTC $9.96B etc.) → ETH side about **4–5×** | new in this round's Counterfactual, reusing landed `raw/` ("Part VII (Evidence Register)" N2, **no re-search**) |
| Comparison: Tokenized Treasury | **$4.65B** (BUIDL $2.25B, 43% on Solana; USYC $2.40B, only 1.7% on Ethereum) | a rounding error in magnitude |

**Adjudication (🟠 Weak evidence)**: ETH exhibits a **structural difference** from BTC at the **on-chain collateral** layer (native vs tokenized/wrapped, whose Transmission Mechanisms differ) and a **magnitude difference** from Tokenized Treasury (~15×) — **difference ≠ advantage** (relative position is an evaluative inference); **but the "share denominator" is missing** — ETH's share of lending collateral is `[UNKNOWN]`, so a rising relative position cannot be demonstrated. **This is probably the most conservative point in this report** ("Part VIII (Disconfirmation Register)" CE-2): once Aave/Morpho collateral composition is obtained, it will **most likely be upgraded to Partially demonstrated**.

---

### 08 Stablecoin / RWA Transmission {#sec-08-stablecoin-rwa-transmission}

**The two channels must be separated (Mandate Brief §10):**

| Channel | Path | Adjudication |
|:--|:--|:--|
| **A: issuer reserve economics** | reserves → **Treasury interest** → issuer | **usually does not transmit to ETH directly** |
| **B: on-chain activity** | transactions → settlement → Ethereum / L2 → **potential ETH demand** | **transmission mechanism exists, magnitude unproven** |

**Four layers must be stated separately**: Issuer economics ｜ On-chain economic activity ｜ Ethereum settlement economics ｜ ETH demand.

| Data | Value |
|:--|:--|
| All-chain stablecoins | **$311.18B** (+1.5% YTD) |
| Ethereum L1 | **$147.08B (47.3%)**, **YTD −10.7% (−$17.66B)** |
| Tron / Solana | $93.99B (30.0%) / ≈$16.5B (5.3%) |
| Share change | **53.7% (2026-01) → 47.3% (2026-10) = −6.4pp** |
| RWA | all categories **$4.69B / 181 protocols**; BUIDL 43% on Solana > 19.7% (post-4844 window average; current last-30-day 2.52%) Ethereum; USYC only 1.7% on Ethereum |

**Prohibited wording**: `Stablecoin growth has no transmission to ETH`.  
**Wording to use**: "whether stablecoin growth **forms a sufficiently large ETH value capture through Ethereum settlement activity has not yet been demonstrated as of the current evidence**."

---

### 09 Value Not Captured by ETH {#sec-09-value-not-captured-by-eth}

**Strict adjudication table (full version in "Part V (Value Distribution Matrix)" §III):**

| Value flow | Amount | Characterization | Leakage? |
|:--|--:|:--|:--|
| Application-layer fees | $521.6M/month | Structurally outside protocol capture | ❌ Does not meet the threshold |
| L2 gross retention | $1,630,763/day | Discretionary non-capture | ❌ Does not meet the threshold |
| Net supply dilution | +1,052,326 ETH/year | Monetary supply effect | ❌ Does not meet the threshold |
| MEV searcher/builder share | `[UNKNOWN]` | Unmeasured | ⚠️ May qualify but unmeasurable |
| blob opportunity cost (under low base fee) | `[SCENARIO]` | Potential non-capture (conditional, **not counted as Leakage**) | ⚠️ Counterfactual unmeasurable |
| Stablecoin reserve interest | not quantified | Channel A, a non-ETH path | ❌ Does not meet the threshold |

**Conclusion**: **this round cannot, in a strict sense, identify a single instance of "Value Leakage"** — that is itself a research conclusion, not an evasion.

---

### 10 Counterfactual Value Capture {#sec-10-counterfactual-value-capture}

**Core question**: absent Ethereum, where would this economic activity go? (full version in `Part VI (Counterfactual)`)

| Comparison set | (a) Created | (b) Share | (c) Bearing | Status |
|:--|:--|:--|:--|:--|
| **Stablecoin** | settlement paradigm ✅ | 47.3%, **direction downward** ⚠️ | reserve value (Treasury interest) ✅ | Partially demonstrated |
| **L2** | shared security and settlement anchor ✅ | DA share ✅ (pricing locked by EIP-7918) | sequencer economics ✅ | Partially demonstrated |
| **Collateral** | native collateral ✅ | structural difference vs BTC ✅ | — | Weak evidence |
| **Settlement** | open programmable settlement ✅ | institutional settlement increment ❌ | — | Weak evidence |

**Answer**: **"What Ethereum scaled first was the infrastructure paradigm, not the value of the assets it bears; and that paradigm is now being reused by other chains at lower cost (alternative DA, independent L1s, Tron payment rails). Whether Ethereum is thereby harmed depends on whether paradigm reuse also brings settlement demand back — as of the current evidence, no verifiable transmission has formed on this point."**

---

### 11 Evidence Matrix {#sec-11-evidence-matrix}

| Mechanism | Layer / chain stage | Evidence status | First-hand basis | Disconfirmation location |
|:--|:--|:--|:--|:--|
| Protocol Cash Flow | 1 | Partially demonstrated | $16.0M/month; burn/issuance 19.7% (post-4844 window average; current last-30-day 2.52%) | "Part VIII (Disconfirmation Register)" CE-1 |
| L2 / Settlement | 2 | Partially demonstrated | 0.146% (0.550% after excluding Robinhood); EIP-7918 0.931 | "Part VIII (Disconfirmation Register)" CE-5 |
| Staking / Security | 2 | Demonstrated (composition determines nature) | 95.04% issuance | "Part VIII (Disconfirmation Register)" K1 |
| Collateral Demand | 3 | Weak evidence | locked 11.1%; ETH side ≈4–5× BTC side | "Part VIII (Disconfirmation Register)" CE-2 |
| Monetary Premium (proxy: ETH/stablecoin market-cap ratio) | 4 | Unknown | the only proxy, 1.077, is price-derived and constitutes no measurement | "Part VIII (Disconfirmation Register)" CE-3 |
| Application Revenue → ETH | — | Not demonstrated | $521.6M/month with no return flow | "Part VIII (Disconfirmation Register)" CE-4 |
| MEV → ETH holders | — | Weak evidence | upper bound $143M (0.043% of market cap) | "Part VIII (Disconfirmation Register)" K1 |
| ETH Economic Value | chain stage 8 | Unknown | not adjudicated this round | — |

---

### 12 What Is Proven / What Is Not Proven {#sec-12-what-is-proven-what-is-not-proven}

#### ✅ Proven (🟢)
1. The scale and growth of value creation (ecosystem gross value on the order of $586.7M/month);
2. The layer-by-layer attribution of value distribution is measurable;
3. The EIP-7918 anchoring mechanism (measured/reserve price 0.931);
4. The 4844 phase change (burn/issuance 138.7% (2022-09-15→2024-03-12 average) → 19.7% (2024-03-13→2026-10-01 average; ⚠️ both values are window averages for "pre-/post-4844", not current values — current last-30-day 2.52%, last-365-day 2.60%, last-90-day 1.81%);
5. Staking scale and validator-set consolidation (44,061,701 ETH; 12,092 holding 36.49%);
6. Listed-company-level circumstantial evidence of "scale decoupled from capture" (Coinbase SEC first-hand);
7. **L2 fees highly concentrated within the window** (Robinhood 83.2%, full month of 2026-09) — **v2.0 downgrade: from "proven" to "observed within the window"**. Reason: that window (2026-07-03→09-30) **coincides exactly** with the Robinhood Chain mainnet launch (**2026-07-01**) and its approximately **90-day gas subsidy period (07-01→09-29, later extended to 12-31)**, making it a **launch-period phenomenon** that must not be written as a stable fact (see the P0-2 special block).

#### ❌ Not Proven (🔴)
1. **Transmission from application-layer revenue → ETH** (no mechanism in force);
2. **Non-cash-flow capture → ETH economic premium** (this report's core open question).

#### ⚠️ Partially Proven (🟡/🟠)
Protocol cash flow (mechanism strong, magnitude compressed) ｜ L2 settlement (mechanism thin, 0.146% (0.550% after excluding Robinhood)) ｜ staking (composition problem) ｜ collateral (missing share denominator) ｜ MEV (mechanism holds, magnitude does not).

#### ⚪️ Unknown
**the monetary premium itself** (v1.4 moved this from 🔴 into this tier: this layer's only proxy is price-derived, and the report has no valid measurement tool) ｜ **scale of ETH-denominated economic activity** (the direct evidence for layer 4; the indicator is not yet defined) ｜ exchange ETH balances ｜ lending collateral composition ｜ MEV split ｜ alternative DA pricing ｜ traditional financial rails ｜ full-industry DAT scale ｜ corporate / institutional settlement share (new in v1.4).

---

### 13 3–5 Year Value Capture Scenarios {#sec-13-3-5-year-value-capture-scenarios}

> **Value capture scenarios only, no ETH price targets.** This report **assigns no probabilities to scenarios** (a probability without first-hand basis is false precision).

#### S1 | Rent Sacrifice Continues
- **Shape**: L1 base fee stays low for an extended period; capture continues shifting nominally to Layer 3/4; the bridge is not built.
- **Trigger observations**: A1/A2 show no improvement; B3 holds at the 0.1% order of magnitude; no L2-based governance change.
- **What happens to ETH capture**: Layer 1 stays 🟡 but the magnitude trends to zero; Layer 3 holds 🟠 on locked volume; **Layer 4 stays ⚪️**.
- **Criterion**: "Part IX (Monitoring Dashboard)" Group A shows no confirmation, Group C grows, Group D shows no improvement.
- **Unknown**: the direction of exchange balances remains a blank.

#### S2 | Expansion Reverses
- **Shape**: L2 economics compress further (Coinbase first-hand already shows "activity up, revenue down" for a single chain), L2 shifts to alternative DA or becomes an independent L1; Ethereum's settlement share declines.
- **Trigger observations**: B1/B3 turn down; D2 breaks below 45%; a scaled alternative-DA migration appears.
- **What happens to ETH capture**: Layer 2 drops from 🟡 to 🟠/🔴; **this is currently the only scenario within this framework that meets the conditions for two-way disproof**.
- **Criterion**: "Part IX (Monitoring Dashboard)" Group B disconfirmation and D2 disconfirmation trigger simultaneously.
- **Unknown**: alternative DA pricing (currently `[UNKNOWN]`) — **this is precisely why S2 cannot be quantified**.

#### S3 | Bridge Built
- **Shape**: based/native rollup scales (a **second** Taiko-level case appears), L2's L1 cost share rises from <0.5% toward the 60% order of magnitude; or a mandatory return mechanism appears.
- **Trigger observations**: B3's share of L2 fees rises markedly; B4 shows governance action; A2 base fee recovers structurally.
- **What happens to ETH capture**: Layer 1/2 rise from 🟡 toward 🟢; channel B becomes the main channel; **Layer 4 acquires measurable conditions for the first time**.
- **Criterion**: the "second based/native rollup case" event-driven item in "Part IX (Monitoring Dashboard)" triggers.
- **Unknown**: whether the n=1 Taiko case is reproducible.

**Premise common to all three scenarios**: **Layer 4 (Monetary Premium) lacks direct observation indicators under all three scenarios** — this is the framework's largest structural gap, and the reason S1/S2/S3 cannot be distinguished using on-chain data alone.

---

> **The original §14 Monitoring Dashboard and §15 Final Conclusion have been merged into this file**: the full monitoring dashboard is in "Part IX (Monitoring Dashboard)"; the final conclusions (worded more strictly than this section, and superseding it) are in "Part II (Final Conclusions)".

**ZK Labs ｜ Jinwu Qiankun No. 2 ｜ 2026-10-02 (UTC)**

---

## Part II | Final Conclusions (v2.0 Final) {#part-ii-final-conclusions-v2-0-final}

### 1. The answer to the mandate brief's ultimate question {#sec-1-the-answer-to-the-mandate-brief-s-ultimate-question}

> **Through what mechanism does the value Ethereum creates actually transmit to ETH; which parts have already been proven by evidence, which are merely theoretical possibilities, and which are currently not happening at all?**

**Answered in three layers (not to be merged):**

#### Transmission already proven by evidence at the mechanism layer (mechanism 🟢; **status strength** counted separately, see §5)

| Mechanism | Transmission path | Magnitude |
|:--|:--|:--|
| **Direct pricing of L1 blockspace** | Users/L2s → pay gas in ETH → base fee unit is burned + priority fee to validator fee recipient | L1 collects **$16.0M/month**; of which permanently burned **$5.44M/month** |
| **Unit pricing of DA (relative to reserve price, soft lower bound)** | L2 → blob → **100% burned**; EIP-7918 sets relative reserve price = `L1 base fee / 16` (pulled back dynamically via excess_blob_gas, **with multi-block lag**, not a per-block hard guarantee) | blob revenue **$143–234/day**; realized/reserve price **0.931** |
| **Deterministic flow-back at the settlement layer** | L2 → L1 execution gas (settlement/proof verification) | **$2,387/day (0.146% of L2 fees (0.550% excluding Robinhood))** |
| **Locking of security collateral** | Validators → must lock ETH to participate in consensus | Locked **44,061,701 ETH (36.09% of supply)** |

**Common feature**: all four satisfy the **four Transmission questions** (who pays / pays in what token / into whose account / whether burned or locked). **They are real.**

#### Merely theoretical possibilities, not yet demonstrated (🟡/🟠/⚪️)

| Mechanism | Why it only reaches "possible" |
|:--|:--|
| **L2 growth → ETH demand** | Activity does stay within the ecosystem (94.6% of transactions, 154.7 GB/month), but **no in-force mechanism** is currently observed converting it into ETH demand |
| **Ecosystem scale → collateral demand → ETH demand** | 11.1% of circulating supply locked and staking up 3.6× over 4 years are **measurable facts**; but **the collateral share definition is missing** → cannot prove "net new and rising in relative position" |
| **Network position → monetary premium** | A theoretical path exists; **the only observable proxy available today is this single one, and it is price-derived** (ETH/stablecoin market-cap ratio 1.077, monotonically falling across four points); this proxy carries a known mechanical bias and is not premium itself → **neither can it be established, nor is it sufficient to falsify ⇒ ⚪️ Unknown (v1.4 explicit: no valid measurement instrument at this layer)** |
| **ETH Economic Value (final segment)** | **Not judged this round** (No Price Shortcut) |

#### What can currently be identified as "not happening" (🔴)

| Mechanism | Evidence |
|:--|:--|
| **Application-layer economic value flowing back to ETH** | Application layer **$521.6M/month**; **no in-force mandatory flow-back mechanism is currently observed** (the only known voluntary give-back today is the OP Superchain 2.5%/15% share, flowing to the OP Collective) |

> **v1.4 removal note**: the row "monetary premium realization" previously in the table has been **moved to the ⚪️ unknown tier** — the only proxy at that layer is price-derived and there is no second indicator, which makes it **undecidable** rather than "identifiably not happening".

---

### 2. Segment-by-segment chain annotation (mandate brief §23 mandatory format) {#sec-2-segment-by-segment-chain-annotation-mandate-brief-23-mandatory-format}

```
Economic Activity                        🟢 Demonstrated
      ↓
Value Creation                           🟢 Demonstrated
      ↓
Value Distribution                       🟢 Demonstrated
      ↓
Ethereum Capture                         🟡 Partially Demonstrated
      ↓
ETH Demand                               🟡 Partially Demonstrated
      ↓
ETH Asset Value                          🟠 Weak Evidence (share definition missing)
      ↓
Monetary Premium                         ⚪️ Unknown (v1.4: no valid measurement instrument)
      ↓
ETH Economic Value                       ⚪️ Unknown (not judged this round)
```

| Segment | Status | One-line basis |
|:--|:--|:--|
| Economic Activity | 🟢 | L2 988.3M transactions/month (94.6%), L1 block utilization ≈100% of target, blob 154.7 GB/month |
| Value Creation | 🟢 | Ecosystem gross value $586.7M/month (split definition); application-layer fees $521.6M/month |
| Value Distribution | 🟢 | Attribution per layer is measurable: applications $521.6M/month｜L2 $1,630,763/day｜L1 $16.0M/month |
| Ethereum Capture | 🟡 | All mechanisms hold, magnitude ratio **2.73% (not a capture rate)**, and compressed by its own scaling (−79.6%) |
| ETH Demand | 🟡 | Staking 36.09% and rising, but validator revenue **95.04% from issuance** → in nature it is dilution protection |
| ETH Asset Value | 🟠 | 11.1% locked, collateral position clear; **share denominator missing** |
| Monetary Premium | ⚪️ | **No valid measurement instrument available** (the only proxy, 1.077, is price-derived); the stablecoin share −6.4pp is an **input-side** reading |
| ETH Economic Value | ⚪️ | Only observations registered (price 2025-10→2026-10 −36.9%), not treated as evidence under No Price Shortcut |

**Chain breakpoints**: **segments 4→5 are not same-source** (capture ↓ while demand ↑); **the transmission in segments 6→7 is unproven** (between asset accumulation and monetary/network premium, no verifiable transmission has yet been observed). **These two are the specific locations of the "Transmission Layer" the mandate brief asked us to find.**

---

### 3. Mandate brief §17: structural migration — "the observed mechanism mix tilts" and "value capture migrates" must be kept separate {#sec-3-mandate-brief-17-structural-migration-the-observed-mechanism-mix-tilts-and-val}

> The mandate brief requires: **the evidence must decide.**

#### The migration must be split into five independent propositions (no merging, no tier-skipping)

| # | Proposition | Status | Evidence / criteria |
|:--|:--|:--|:--|
| ① | The fee side is compressed | 🟢 **Has happened (measurable fact)** | burn/issuance **138.7% (2022-09-15→2024-03-12 average) → 19.7% (2024-03-13→2026-10-01 average; ⚠️ both values are window averages "before/after 4844", not current values — current last 30 days 2.52%, last 365 days 2.60%, last 90 days 1.81%**; net supply **−0.238%/yr → +0.652%/yr**; L1 fees YoY **−79.6%** |
| ② | The holding side is growing | 🟢 **Has happened (measurable fact)** | staking ratio **9.73% → 36.09%** (3.6× over 4 years); ETF+DAT locked **11.1% of circulating supply** |
| ③ | The **composition** of the two has changed | 🟡 **Evidence supports a composition change** | ① and ② occur in the same period and the same direction; and ① was executed by Ethereum's own upgrades (4844 / Fusaka / BPO / EIP-7918) |
| ④ | Capture **migrated from the fee side to the holding side** | 🟡 **This is interpretation, not observation** | ①↓ and ②↑ can only prove **simultaneous occurrence**; the report itself shows the two are **not same-source** (§2, segments 4→5) → a causal migration cannot be inferred |
| ⑤ | The holding side has **successfully captured ETH economic value** | 🔴 **Verifiable evidence has not yet formed** (⚠️ **only as to the measurable part**) | validator revenue **95.04% from issuance** (= lock-up utility, not incremental value); collateral share denominator missing; price is not evidence (No Price Shortcut). **v1.4 correction: the basis previously listed, "the observable proxy moves in the opposite direction", no longer holds** — the monetary premium sub-channel has been re-labeled ⚪️ because there is **no valid measurement instrument** (see "Part IV" Layer 4); **the 🔴 in this row does not depend on that proxy** |

#### Verdict (strict wording)

> **Evidence as of 2026-10-02:**
> - "**Fee side declining, holding side growing**" — **two measurable facts** (🟢);
> - "**The observed mechanism mix is tilting from the fee side toward the holding/lock-up side**" — **supported by evidence** (🟡);
> - "**Value capture has migrated from the fee side to the holding side**" — **interpretation rather than observation** (🟡 Interpretation): two facts occurring simultaneously is not sufficient to prove a causal migration;
> - "**The holding side has successfully captured ETH economic value**" — **verifiable evidence has not yet formed** (🔴 Not Demonstrated, **only as to the measurable part**: validator revenue 95.04% from issuance, no mandatory flow-back mechanism at the application layer). **⚠️ The "monetary premium" sub-channel within it has been re-labeled ⚪️ Unknown per v1.4 (no valid measurement instrument) — the 🔴 in this row does not cover that sub-channel.**
>
> **v1.3's precise formulation**: judged by the observed mechanism mix, ETH's economic transmission is tilting from "fee-type mechanisms" toward "holding/lock-up-type mechanisms"; **but it cannot yet be proven that this is a completed value capture migration, let alone that it has already been realized as ETH's economic value.** This is not "the migration does not hold", but rather **"composition change" is supported by evidence, while "value capture migration" and its realization are not yet proven**.

#### Three counter-constraints that must be stated alongside (not to be omitted)

1. **Coinbase SEC primary source**: Base stablecoin transfer volume **+7× YoY**, while `Other transaction revenue` **−11%** → **the decoupling of scale growth from capture is independently corroborated at the listed-company disclosure layer**, but it simultaneously weakens the narrative that "L2s get rich by withholding".
2. **Taiko n=1**: based-ification can raise the L1 cost share from <0.5% to **61.7%** → the **bridge** for migration exists technically, but **if it is not reproducible it does not hold**.
3. **EIP-7918 is a "reserve price", not a "fee rate"**: it guarantees "will not go to zero", and **does not guarantee** a rebound.

---

### 4. Core conclusion (against the §18 draft framework in the mandate brief, rewritten sentence by sentence per the evidence) {#sec-4-core-conclusion-against-the-18-draft-framework-in-the-mandate-brief-rewritten-}

> §18 states explicitly: *The above is only a research direction. Do not copy it directly. The final wording must be decided by the Evidence.*
> The left column below is the **direction** given by the mandate brief; the right column is the wording **the evidence permits us to write**.

| Mandate brief §18 direction | Wording permitted by the evidence (v1.3 final) |
|:--|:--|
| "Ethereum is creating large amounts of application-layer and L2 economic activity, but this activity is not converted proportionally into L1 protocol cash flow or ETH burn" | **Holds and is proven**: ecosystem gross value $586.7M/month → L1 protocol fees $16.0M/month (**≈2.73%, a magnitude ratio, not a capture rate**); burn $5.44M/month (**≈0.93%**) |
| "Ethereum ecosystem growth ≠ ETH cash-flow growth" | **Holds** (🟢). **But must not be escalated to** "ecosystem growth ≠ ETH value capture" — because Value Capture ⊋ Cash-Flow Capture (CA-02) |
| "ETH may still capture network value through settlement / security / staking / collateral / liquidity / monetary" | **Partially holds**: the settlement and security mechanisms are **both proven** (magnitudes 0.146% (0.550% excluding Robinhood) and 95% funded by issuance respectively); collateral **evidence exists but the share definition is missing**; liquidity / monetary **no supporting readings observed** |
| "What is genuinely under-proven today is whether these non-cash-flow forms of Value Capture can form a sufficiently strong, sustainable, observable ETH economic premium" | **Holds, and is this report's core open question**. **Precise formulation**: *as of current evidence, a verifiable "non-cash-flow capture → ETH economic premium" transmission has not yet formed.* |

#### One-sentence version (ZK Labs v2.0 core conclusion)

> **Between Ethereum's value creation and ETH's economic value there is a Transmission Layer that can already be located but has not yet been sufficiently verified.**
>
> **What has been proven is that Ethereum has four clear ETH transmission mechanisms** — L1 blockspace pricing, DA burn, settlement flow-back, security lock-up; the four Transmission questions can be answered and the mechanisms hold. **But "a transmission mechanism exists" does not equal "that mechanism has been proven to generate incremental ETH economic value"**: the aggregate of the four is extremely small (L1 protocol fees ÷ the report's ecosystem gross value proxy ≈ **2.73%, a magnitude ratio, not a capture rate**; settlement flow-back **0.146% (0.550% excluding Robinhood)**); and the largest of them, security lock-up, has its economic cost paid mainly by ETH issuance (validator revenue **95.04% from issuance**) — so what it proves is **that the security mechanism exists** and **that ETH lock-up utility exists**, not **incremental ETH economic value brought by external economic activity**.
>
> **The observed mechanism mix is indeed tilting**: fee-side compression (burn/issuance **138.7% (2022-09-15→2024-03-12 average) → 19.7% (2024-03-13→2026-10-01 average; ⚠️ both values are window averages "before/after 4844", not current values — current last 30 days 2.52%, last 365 days 2.60%, last 90 days 1.81%**) and the rise of the holding/lock-up side (staking ratio **9.73% → 36.09%**) are both measurable facts. **But "composition has changed" does not equal "value capture has already migrated"**, and still less "the holding side has already successfully captured ETH economic value" — as of 2026-10-02, no verifiable transmission from asset/holding-side growth to Monetary / Network Premium has been observed (the observable proxy is a single item, price-derived, and carries a known mechanical bias → that layer has been re-labeled from 🔴 Not demonstrated to **⚪️ Unknown**).
>
> **This round therefore gives no binary answer to "has ETH captured Ethereum's value"**, but gives the segment-by-segment status of the chain: segments 1–3 hold, segments 4–5 partially hold, segment 6 is weak evidence, segment 7 is undecidable, segment 8 is not judged.
>
> **Condensed into one sentence**: Ethereum has proven that it can create economic activity, and has proven that it has multiple mechanisms transmitting economic activity to ETH; but as of 2026-10-02 the evidence is not yet sufficient to prove that these mechanisms have formed an ETH economic value capture that matches the scale of the Ethereum ecosystem, is sustainable, and is observable. **The clearest fact today is not "ETH has no value capture", but rather: between Ethereum's economic expansion and ETH's economic value there remains a Transmission Layer that has not yet been sufficiently verified.**

---

#### Whole-chain compression (what we know / what we do not know)

Compressing the eight-segment chain into a single table — this is the **preferred summary** when citing this study after v1.3:

| Layer | What we know | What we do not know |
|:--|:--|:--|
| **Economic Activity** | Ethereum / L2 have huge and real economic activity (94.6% of transactions stay within the ecosystem, 154.7 GB/month DA usage) | **how the economic value of this activity is attributed** to each party |
| **Value Creation** | large amounts of economic activity do occur (ecosystem gross value on the order of $586.7M/month) | **how much of it is created uniquely by Ethereum** (with no substitute implementation) |
| **Value Distribution** | **where each layer's money flows is measurable** (**L2 applications** $521.6M/month, L2 $1,630,763/day, L1 $16.0M/month) | which parts are **long-term economic rent** and which are cyclical flows |
| **Protocol Capture** | L1 has **clear and enforceable fee mechanisms** (base fee burn, priority fee, blob, settlement gas) | **whether the captured magnitude is sufficient** (magnitude ratio only 2.73%, and not a capture rate) |
| **ETH Demand** | the three demand types staking / gas / collateral **do exist and are growing** (staking 9.73%→36.09%) | whether this constitutes **net new external demand** (or stock reshuffling / issuance-driven) |
| **ETH Asset Capture** | lock-up scale is large and measurable (13.52M locked, staking 36.09% of supply) | ETH's **share relative to other collateral** (denominator missing, lending collateral share `[UNKNOWN]`) |
| **Monetary Premium** | **a theoretical mechanism exists**; **the only proxy available is derived from ETH's price and does not constitute a measurement of premium** (ETH/stablecoin market-cap ratio 1.077); the stablecoin share −6.4pp is an **input-side** reading | a **price-independent** measurement instrument is needed (scale of ETH-denominated economic activity / share of reserve usage) — **neither currently exists** |
| **ETH Economic Value** | — (**not judged** this round, No Price Shortcut) | **whether long-term economic value is ultimately produced** |

**How to read this table**: the left column is **the existence facts that already stand**, the right column is **what genuinely needs filling in next round**. **Do not read the existence facts in the left column as the right column already holding** — this is precisely the common theme of all the logic tightening in this version.

### 5. Value Capture Transmission Status (replacing v1.0's "0/4") {#sec-5-value-capture-transmission-status-replacing-v1-0-s-0-4}

| Mechanism | Evidence Status | Nature |
|:--|:--|:--|
| Protocol Cash Flow | **Partially demonstrated** | mechanism holds; magnitude compressed by its own upgrades |
| L2 / Settlement | **Partially demonstrated** | mechanism holds; magnitude 0.146% (0.550% excluding Robinhood) |
| Staking / Security | **Demonstrated (composition determines nature)** | 95.04% from issuance |
| Collateral Demand | **Weak evidence** | share definition missing |
| Monetary Premium | **Unknown** | **no valid measurement instrument available**: the only proxy is price-derived (proxy ≠ premium itself) and no second indicator exists ⇒ **the conditions for a negative judgment are not met** (re-judged from Not demonstrated in v1.4) |
| Application Revenue → ETH | **Not demonstrated** | no in-force flow-back mechanism |
| MEV → ETH holders | **Weak evidence** | mechanism holds; magnitude 0.043% of market cap |
| ETH Economic Value | **Unknown** | not judged this round |

**Prohibited**: `0/4`, `1/4`, `Score`, `Bull/Bear score` (mandate brief §12).

---

### 6. The largest unknown variables (carried forward + updated priorities) {#sec-6-the-largest-unknown-variables-carried-forward-updated-priorities}

1. **Exchange ETH holdings** — determines whether "lock-up = net new or custody relocation"; the single-point key for layer 3 (the payment source).
2. **Scale of ETH-denominated economic activity** — the **only direct evidence** identified so far for layer 4, and currently **not even an indicator definition exists**.
3. **ETH/LST collateral share in lending protocols** — **can be filled at zero cost**, and **may directly raise the layer 3 status** ("Part VIII (disconfirmation register)" CE-2).
4. **MEV generated / extracted / paid split** — the largest global UNKNOWN; this round gives only the validator-side upper bound **53,049 ETH/365d**. **v2.0 strengthening**: Glamsterdam (SFI 18) includes **EIP-7732 ePBS** and **EIP-7928 BALs** — landing ePBS will change the builder/relay structure, **and the MEV attribution definition will change with it**, so this item's "unmeasurable" status may be **partially lifted** at that point; the monitoring dashboard has it listed as a trigger (no pre-emptive parameter tuning). **Any number claiming to know what share of MEV is captured by ETH cannot be verified on this machine.** ※[Errata ③](#errata-1)
5. **Alternative DA pricing / comparison against traditional-finance rails** — the two blank faces of the Counterfactual module.

---

### 7. Research discipline statement {#sec-7-research-discipline-statement}

- This conclusion **contains no** price target, **no** trading recommendation, **no** short-term forecast;
- It is **bound** to "current observation window + evidence set + threshold gate", and **does not conclude about the future**; "has not yet formed" ≠ "will not form";
- Where data-source quality is insufficient, this is labeled a **data-infrastructure limitation** (e.g. no primary source for MEV), and **no market conclusion is inferred from it**;
- **No load-bearing figure was re-fetched this round** (mandate brief §24: do not redo completed data collection);
- **Self-errors voluntarily put on record**: six items in v1.1–v1.2 ("Part VIII (disconfirmation register)" §4) — the 0/4 score, the 99.77% naming, the institutional-demand counter-evidence, the absolute stablecoin sentence, "only" ×4, ×32 understatement of staking volume;
- **Ten new items in v1.3** (this version's self-check + research review) ※[Errata ④](#errata-4): ① "the four channels really capture value" (mechanism→capture slippage); ② "the capture center of gravity has already migrated" (observation→interpretation slippage); ③ "A has been falsified" (inferring the objective function); ④ "2.73% as a capture rate" (numerator and denominator at different layers); ⑤ the Counterfactual "Created" (unfalsifiable counterfactual); ⑥ "segments 6→7 conversion fails" (failure ≠ unverified); ⑦ "ETH has a structural advantage over BTC" (evaluative inference); ⑧ directly naming monetary premium (proxy ≠ premium); **⑨ "Originated" (requires denying that others implemented it earlier, still unfalsifiable — "Part VI (counterfactuals)" §2 has been changed to `Scaled First`)**; **⑩ "earliest verifiable implementation" (factual error; colored coins / Mastercoin / Counterparty all predate Ethereum mainnet)**.
- All load-bearing figures are independently recomputable: `notes/T1|T2|T3` + `data/`, `raw/`, `scripts/`.

---

### 8. Closing status {#sec-8-closing-status}

**v1.3–v1.5 three-round evolution** (Final Logic Audit → tier re-labeling → four thought-elevation items): the complete narrative, per-round deliverables and tier-change records **have been moved, per research review instruction #5, into the companion audit working paper** (`ETH_Value_Capture_v2.0_审计底稿.md` §A). **None of the three rounds changes the study's frozen status, and none alters any criterion.**  
**v2.0 round = all 7 P0 items landed ＋ 7 dispositions from the second review of the instructions**: **zero tier changes**; the A3 lower bound and the A2/B2 thresholds were adjusted in **wording and values** per instructions **#12/#13/#14** (**not tier changes**); "institutional blockading" was changed to "institutional anchoring" per **#15** (judgment strength reduced to phenomenological). Item-by-item dispositions are in the audit working paper §B.
- Deliverables (v2.0): **1 external version ＋ 1 audit working paper**. v1.5 and all earlier versions are frozen in their respective directories;
- **Publication Freeze (set by research review 2026-10-04, written into research discipline)**: **apart from P1 hard-definition errors, no new data, new indicators, new frameworks, or new tier adjustments will be accepted**. A P1 hard-definition error = a verifiable defect a reader hits on first check (e.g. a cited recomputation script does not exist, a definition label does not match the reading, the chain count/window is not reproducible); for such errors **only reproducibility and labeling are fixed, without changing load-bearing figures**. This round's **F-7a (missing recomputation script)** was handled on exactly this basis, **with no load-bearing figure changed**;
- **No new automation tasks, no external publication** (external publication requires separate confirmation);
- **Incremental trigger conditions for the next round** (carried from v1.0 and updated):
  ① obtaining **lending collateral composition** (zero cost, best value for effort, may change the layer 3 judgment);  
  ② obtaining **exchange ETH holdings** or **any MEV source from Dune/relayscan**;  
  ③ an **ETH-denominated economic activity** indicator being defined and measurable (currently the only identified path for layer 4 to move from ⚪️ to 🟡);  
  ④ L1 execution base fee structurally returning to **> p90 (≈0.46 Gwei, 90-day daily-average definition)** (triggering a simultaneous lift of the A/B group) — the original "> 5 Gwei" = p100, 0 triggers in 90 days, **abolished in v2.0 per instruction #13**;  
  ⑤ a **second** measurable case of based/native rollup;  
  ⑥ the next blob parameter adjustment (all blob conclusions must be recomputed).

---

## Part III | Criteria and Concept Audit {#part-iii-criteria-and-concept-audit}

### 1. Judgment principles of the audit {#sec-1-judgment-principles-of-the-audit}

1. **Concepts must be operationalizable**: if a concept cannot be written as "numerator / denominator / time window / data source", it cannot enter the conclusion.
2. **Causality must be explicit**: `the data supports A` cannot automatically imply `B` unless there is a **nameable Transmission Mechanism** (who pays, pays what, into whose account, whether burned or locked).
3. **Strength must match the evidence**: the vocabulary has only five tiers (Demonstrated / Partially demonstrated / Weak evidence / Not demonstrated / Unknown), **there is no scoring**.
4. **No negative judgment without an instrument (added v1.4, load-bearing; v2.0 adds a self-imposed limit clause)**: **this report's self-imposed limit** — when a layer lacks a valid price-independent observation instrument, its tier **can only stay at ⚪️**; ⚪️ **is neither a negation nor an affirmation**. **Any upward move of a layer from ⚪️ requires two independent price-independent indicators simultaneously** (a first plus a second), both indispensable. **🔴 Not demonstrated requires "a usable observation instrument exists and its reading points to non-occurrence"**; if **no usable valid observation instrument exists**, the correct tier is **⚪️ Unknown**, and **🔴 must not be assigned** — a negative judgment with no measurable instrument cannot be supported by evidence. **Discriminant test**: can this judgment be falsified by some set of observables? If not ⇒ ⚪️. **Application in this report**: **Layer 4 (Monetary / Network Premium), because its only proxy is price-derived and a direct-evidence indicator is undefined, is re-labeled ⚪️ Unknown under this rule** (see "Appendix C", v1.3 → v1.4).

---

### 2. Concept-by-concept audit {#sec-2-concept-by-concept-audit}

#### CA-01 | Value capture narrowed to protocol cash flow

- **Old Concept**: Value Capture = protocol revenue / fees / burn / cash flow. The six-segment chain [3]–[6] in v1.0 used fees and burn throughout as its definition, and only at the conclusion layer was "mechanism 1 = holding demand" added, forming a binary "cash flow vs non-cash-flow" contrast.
- **Problem**: it treated **one** form of capture as **all** of it. The consequence: when the cash-flow side is deliberately compressed (post-4844 burn/issuance 138.7% (2022-09-15→2024-03-12 average) → 19.7% (2024-03-13→2026-10-01 average; ⚠️ both values are window averages "before/after 4844", not current values — current last 30 days 2.52%, last 365 days 2.60%, last 90 days 1.81%), the report could only conclude "capture is weakening" and **could not answer** "is any other layer strengthening". This is precisely the potential problem identified in mandate brief §3.
- **New Concept**: Value Capture falls into four categories, **existing in parallel with independent definitions**:
  - **A. Protocol Cash-Flow Capture** (gas / base fee / burn / priority fee / validator revenue / MEV-related protocol economics)
  - **B. Security / Settlement Capture** (settlement role / DA / blob / validator security / staking demand)
  - **C. Asset / Collateral Capture** (ETH as collateral / DeFi collateral / lending / stablecoin collateral / institutional holdings / ETF / DAT / reserve-asset use)
  - **D. Monetary / Network Capture** (settlement asset / reserve asset / monetary premium / network liquidity / ETH-denominated economic activity / global crypto-collateral role)
- **Reason**: the four categories have **different observation definitions** — A looks at USD/ETH flows, B at the security budget and degree of anchoring, C at lock-up and collateral share, D at relative denomination and share. Only by separating them can one answer "which layer is strengthening and which is weakening".

#### CA-02 | `ETH Value Capture ≠ ETH Cash-Flow Capture`

- **Old Concept**: implicitly equating "capture" with "some fee comes in".
- **Problem**: this led v1.0 into an **asymmetric evidence standard** — numbers for the cash-flow side ($16.0M/month) versus a list for the holding side ($26.76B TVL etc.), the two incomparable.
- **New Concept**: **Cash-flow capture ⊂ Value capture, a proper subset, not the whole.** Stated explicitly: *Cash-flow capture is a subset of Value Capture, not the whole of it.*
- **Reason**: a value capture mechanism can hold at **zero dollar revenue** (e.g. collateral status, settlement anchoring), and can fail to hold at **high dollar revenue** (e.g. revenue entirely from issuance transfer). The subset relation is a logical fact, not rhetoric.

#### CA-03 | Deleting "deflation = necessary condition"

- **Old Concept**: condition ③ of the four conditions in the main report, "net supply must return to neutral or deflationary" (criterion threshold: burn/issuance ≥ 100%).
- **Problem**: **this is a pseudo-necessary condition.** The direction of net supply is determined by "issuance vs burn" and has nothing to do with "whether value is captured by ETH" — issuance can be absorbed by demand growth, and burn can be zero while capture still holds (categories C/D). Setting it as a necessary condition amounts to **using a monetary-policy indicator to veto non-monetary capture**.
- **New Concept**: *Net deflation is NOT a necessary condition for ETH value capture.* The correct logic is **ETH Supply Growth vs ETH Demand Growth**; burn / issuance are defined as a **Monetary Supply Indicator**, not a Value Capture Indicator.
- **Reason**: v1.0's own evidence already supports this correction — staking up 3.6× over 4 years (9.73% → 36.09%) and 11.1% of circulating supply locked all occurred in the same period of **positive net issuance**. If deflation were a necessary condition, these observations would contradict each other.

#### CA-04 | Deleting "L1 execution demand must recover"

- **Old Concept**: condition ① "L1 execution demand **must** structurally recover (base fee > 5 Gwei)", described as "the **only** variable that can simultaneously amplify all three channels".
- **Problem**: it wrote **the single most effective channel** as a **necessary condition**. If L1 execution demand stays low for a long time (reality: 0.12–0.15 Gwei), then under the old wording "all capture fails to hold" — which simultaneously **kills categories B/C/D** (settlement anchoring, collateral status and monetary status do not presuppose high L1 gas).
- **New Concept**: *L1 execution demand is one major value-capture channel, not a necessary condition for all forms of ETH value capture.* Five channels are established:

| Channel | Path | Capture type |
|:--|:--|:--|
| A | L1 Execution → Fees → Burn → ETH | Direct (cash flow) |
| B | L2 → DA / Settlement → Ethereum → ETH | Indirect (cash flow + security) |
| C | Ethereum Security → Staking → ETH demand | Asset-demand |
| D | Ethereum ecosystem → ETH collateral → ETH demand | Asset-demand |
| E | Ethereum network → Monetary / reserve role → ETH premium | Monetary |

- **Reason**: the five channels have **different preconditions**. A needs L1 demand, C/D need ecosystem scale, E needs relative position. Binding them into one shared necessary condition amounts to using A's threshold to veto C/D/E.

#### CA-05 | Redefining value leakage

- **Old Concept**: the main report's ranking of "the biggest value leakage": ① net supply dilution +1,052,326 ETH/year; ② L2 cost-savings withholding (99.77%); ③ application-layer fees not flowing back at all.
- **Problem**: **it presupposed that "Ethereum should have taken back all economic value".** Under that definition any value not in the protocol's hands becomes a "leak", and the conclusion is biased negative by construction; moreover the word "leak" implies **fault**, whereas 4844/Fusaka/BPO1/BPO2/EIP-7918 were **all deliberate decisions**.
- **New Concept**: changed to a three-stage **Value Creation → Value Distribution → Value Retention**, with a **single admission condition** for "Leakage":

> "Value Leakage" may be used only when **some economic value could originally, in theory, have been captured by ETH through a protocol mechanism, but in fact was not**.

On this basis the re-judgment (details in `Part V (value distribution matrix)`):

| Value flow | v1.0 definition | v1.1–v1.4 definition | Rationale |
|:--|:--|:--|:--|
| Application layer $521.6M/month | leakage | **Structurally outside protocol capture** (value outside the protocol) | the protocol **never designed** a claim on application revenue → the Leakage admission condition is not met |
| L2 retention $48.92M/month (gross) | leakage | **Discretionary non-capture** (deliberate waiver / pricing choice) | mechanically "it could be collected, or not" (EIP-7918 has established a floor); this is a **policy choice**, not a leak |
| Net supply dilution +0.862%/yr | leakage #1 | **Monetary supply effect** (not a leak) | dilution is a transfer between holders, not "value that could have been captured and was not" |
| blob revenue under EIP-7918 anchoring | — | **Potential non-capture (conditional, not counted as Leakage)** | only when "L1 execution base fee stays low for long" does blob revenue sit systematically below the potential value under demand-based pricing; **the counterfactual is unmeasurable and must be labeled [SCENARIO]** |

- **Reason**: separating "did not get it" from "could have gotten it but did not" is one of the most important conceptual corrections of this round — it simultaneously avoids two errors: reading deliberate design as failure, and reading a market division of labor as fault.

#### CA-06 | Strict definition and renaming of L2's "99.77%"

- **Old Concept**: the main report and the conclusion uniformly said "L2 retention rate 99.77%" and "L2 gross profit $1,630,763/day".
- **Problem**: `毛利` and `留存率` are extremely easy to read as **profit margin** in a Chinese context. The actual data is only **`L2 user fees − cost paid to L1`**, **without deducting** sequencer servers, team, infrastructure, airdrops/incentives. v1.0 itself noted in disconfirmation register §10 that it "must not be treated as net profit", **but the naming in the body did not carry that restriction through**.
- **New Concept**: fixed as

  > **L1 cost share / gross economic retention**
  > = (L2 user fees − L1 settlement cost) ÷ L2 user fees
  > 2026-09 monthly average: L2 user fees $1,634,574/day, paid to L1 $2,387/day → **L1 cost share = 0.146% (0.550% excluding Robinhood)**, **gross economic retention = 99.854% (L1-only definition) / 99.77% (definition including other costs $1,424/day)**

  **Prohibited**: calling it profit margin; **prohibited**: inferring L2 net profitability from it.
- **Reason**: Base's counter-evidence already proves this restriction is not formalism — Coinbase SEC primary source: Base stablecoin transfer volume **+7× YoY**, while `Other transaction revenue` **−11%** → at the single-chain level "activity surges while revenue falls", and **industry gross retention ≠ single-chain net profitability**.

#### CA-07 | Splitting stablecoin into two Channels

- **Old Concept**: the conclusion sentence "stablecoins do not transmit to ETH"; disconfirmation register "the transmission chain breaks at step 1 (issuer revenue = Treasury interest)".
- **Problem**: **it kneaded two different economic chains into one sentence.** The issuer's reserve yield (Treasury interest) and on-chain settlement activity are two different value flows; the former not transmitting **does not mean** the latter does not transmit.
- **New Concept**:

  - **Channel A ｜ Stablecoin issuer reserve economics** → Treasury yield → **Issuer** (**usually does not transmit to ETH directly**)
  - **Channel B ｜ Stablecoin on-chain activity** → Transactions → Settlement → Ethereum / L2 → **Potential ETH demand** (**an ETH transmission mechanism still exists**)

  Four layers must be stated separately: **Issuer economics ｜ On-chain economic activity ｜ Ethereum settlement economics ｜ ETH demand**.  
  The question to research is: **does stablecoin growth, through Ethereum settlement activity, form a sufficiently large ETH value capture?**
- **Reason**: sentences like "Stablecoin growth has no transmission to ETH" are prohibited — it writes a **magnitude question** (is it big enough) as an **existence question** (is there any).

#### CA-08 | Causal downgrade of institutional demand

- **Old Concept**: "institutions buy ETH but the price falls, therefore the demand is falsified"; main report "the proposition 'institutional balance-sheet demand = price support' is **directly falsified**".
- **Problem**: **three layers conflated** — Demand (there are purchases), Value (there is economic value transmission), Price (price response). Rising purchase volume and falling price **can both be true at the same time**, and price is governed by macro liquidity, regulation and risk appetite, **which does not falsify the reality of demand**.
- **New Concept**:

  > *Institutional accumulation does not by itself demonstrate sufficient price support or economic value capture.*
  > Rigorous form: *Institutional accumulation has not yet provided sufficient evidence that this demand translates into persistent ETH economic value or price support.*

  Stated explicitly: **Price ≠ Value Capture**; **Institutional demand ≠ Guaranteed price appreciation**. The DAT/ETF research is **retained** but **downgraded** to the **Institutional ETH Demand** section, and **not listed** as a core Value Capture mechanism.
- **Reason**: what v1.0's original wording committed is exactly the **No Price Shortcut** of mandate brief §22 — using price direction to falsify value capture.

#### CA-09 | Deleting "0/4 of the four necessary conditions"

- **Old Concept**: main report "**0** of the four conditions hold today"; framework criterion 5 "① ❌ ② ❌ ③ ❌ ④ ❓ → **0/4 hold**".
- **Problem**: **artificial scoring**. The four conditions themselves have already been judged by CA-03/CA-04 to be **fabricated necessary conditions**; combining them into a score again is producing a wrong conclusion from wrong premises, and the score carries a strong conclusion hint ("0/4" reads like a verdict).
- **New Concept**: delete the scoring. Replace with the **Value Capture Transmission Status** table (mechanism × five-tier status labels), and **prohibit** `0/4`, `1/4`, `Score`, `Bull/Bear score`.
- **Reason**: status labels preserve the same information content (which layer is weak, which is strong) but **do not manufacture a composite score** and do not induce a "total negation" reading.

#### CA-10 | Binary table "validated as invalid/reversed" changed to five tiers

- **Old Concept**: conclusion §2 three-tier table: ✅ validated / ❌ validated as invalid or reversed / ❓ cannot be validated.
- **Problem**: **the binary erases differences in degree**. "burn ≠ value capture" (a composition problem), "stablecoins do not transmit" (a magnitude problem) and "MEV is an important return" (a magnitude problem) were all put into the same ❌, and readers cannot distinguish **which one is a mechanism failure and which is merely insufficient magnitude**.
- **New Concept**: five status tiers, with each tier stating **whether it is a mechanism problem or a magnitude problem**:

| Mechanism | v1.0 | v1.1–v1.4 status | Nature |
|:--|:--|:--|:--|
| Protocol Cash Flow | ✅ | **Partially demonstrated** | mechanism holds, magnitude deliberately compressed |
| L2 / Settlement | ✅ | **Partially demonstrated** | mechanism holds, magnitude extremely small (0.146% (0.550% excluding Robinhood)) |
| Staking / Security | ✅ | **Demonstrated (composition determines nature)** | mechanism holds; nature determined by 95.04% from issuance |
| Collateral Demand | ❓/✅ | **Weak evidence** (observables exist, share definition missing) | magnitude problem |
| Monetary Premium | ❌ | **Unknown** (re-judged from Not demonstrated in v1.4) | **instrument problem** (no valid measurement instrument: the only proxy is price-derived, proxy ≠ premium itself) |
| Application Revenue → ETH | ❌ | **Not demonstrated** | mechanism absent (no flow-back path) |
| MEV → ETH holders | ❌ | **Weak evidence** (mechanism holds, magnitude does not) | magnitude problem |

- **Reason**: distinguishing "the mechanism does not exist" from "the magnitude is insufficient" is the most valuable layer of information this report offers readers — the policy implications of the two are entirely different.

#### CA-11 | Six-segment chain → eight-segment value transmission chain

- **Old Concept**: v1.0 framework six segments: ecosystem economic activity → revenue formation at each layer → revenue attribution judgment → ETH capture mechanism → capture volume measurement → comparison with supply.
- **Problem**: segments [5][6] put "capture volume" and "comparison with supply" at the **end of the chain**, so that **non-cash-flow capture had nowhere to sit** (collateral and monetary premium have no "volume" to measure) and could only be pushed into footnotes. The chain's endpoint was also set as "comparison with supply" — precisely the fabricated condition of CA-03.
- **New Concept**: changed to the eight-segment chain of mandate brief §2, **allowing any link to break**, with each link independently labeled:

```
Economic Activity → Economic Value Creation → Value Distribution
→ Ethereum Protocol Capture → ETH Demand/Utility → ETH Asset Capture
→ ETH Monetary/Network Premium → ETH Economic Value
```

- **Reason**: only by splitting **Demand**, **Asset Capture** and **Monetary Premium** into three segments can each be given evidence and labeled separately — exactly what v1.0 could not do (details in `Part IV (transmission framework)`).

#### CA-12 | Downgrading "only"-type absolute words

- **Old Concept**: "[the **only** mechanism that is strengthening]", "the **only** field evidence, Taiko 61.7%", "the **only** 'structural hole' in ETH's value capture system", "the **only** flow-back".
- **Problem**: under the four-category capture framework, "only" is **unsupportable on the evidence** — with measurable definitions available for only a few protocols (Lido/Aave/Morpho/EigenLayer etc.), claiming "only" exceeds observational capability.
- **New Concept**: uniformly changed to "**the strongest under current evidence / the most worth tracking / no alternative path observed yet**", with the **observation that could overturn it** attached at each site.
- **Reason**: mandate brief §16 explicitly requires item-by-item review of "only"; where evidence is insufficient, downgrade.

#### CA-13 | Mixed subjects: ETH / ETH holders / protocol / validators must be separated

- **Old Concept**: the whole text used "ETH captures" generically, while in different paragraphs it actually referred to different subjects (protocol fees, validator revenue, token holders).
- **Problem**: it caused two substantive errors — ① counting validator revenue as "ETH capture" (validators ≠ all holders); ② counting "burn" as "holder capture" (burn **benefits all holders pro rata**, a different nature from validator revenue).
- **New Concept**: four subjects — **Protocol (the protocol itself) ｜ Validators ｜ ETH holders (all holders, including pro-rata benefit from burn) ｜ ETH as asset (collateral/settlement/reserve use)**. Every capture volume must state the beneficiary subject.
- **Reason**: v1.0 itself already had the correct criterion ("it is captured by stakers, not by non-staking ETH holders, and not by the protocol"), but did not elevate it into a **definition for the whole text**.

#### CA-14 | "Transmission" must be observable (Transmission Mechanism definition)

- **Old Concept**: v1.0 already required segment [4] to give "a concrete, observable settlement path", but did not formalize it as a **criterion for the whole text**.
- **Problem**: this let sentences that are **correct but non-operational**, such as "Ethereum remains the security and settlement anchor for L2s", be taken as capture evidence.
- **New Concept**: any "transmission" claim must answer four questions: **who pays? pays in what token? into whose account? whether burned/locked?** If it cannot answer them = `Not demonstrated` (rather than "weak").
- **Reason**: this is the operationalized form of mandate brief §22 **No Conceptual Overreach**, and the criterion basis for the `04` matrix and the `08` Dashboard.

---

### 3. Item-by-item re-review of the mandate brief §16 strong conclusions {#sec-3-item-by-item-re-review-of-the-mandate-brief-16-strong-conclusions}

| Original sentence (v1.0) | Trigger word | Problem | v1.1–v1.4 revised |
|:--|:--|:--|:--|
| "**0** of the four conditions hold today" | 0/4 | fabricated premise + artificial scoring | deleted; replaced by the mechanism status table (CA-09) |
| "[the **only** mechanism that is strengthening] balance-sheet asset status" | only | exceeds observational capability | "under current evidence, the asset side is **the layer with the strongest observed growth** (🟡), but realization is unproven" |
| "This is the **only** 'structural hole' in ETH's value capture system" | only | as above | "the application layer→ETH flow-back path **has no in-force mechanism observed at present** (🔴)" |
| "Taiko 61.7% is the **only** field evidence" | only | a single case is insufficient to claim "only" | "**this is the only identified measurable field case** (n=1); **if it is not reproducible it does not hold**" |
| "'Institutional balance-sheet demand = price support' is **directly falsified**" | directly falsified | three layers conflated (CA-08) | "institutional accumulation **has not yet provided sufficient evidence** that this demand translates into persistent economic value or price support" |
| "**Stablecoins have no transmission to ETH**" | none/absolute | existence vs magnitude (CA-07) | "issuer reserve economics usually does not transmit to ETH; on-chain activity has a transmission mechanism, **magnitude not yet proven**" |
| "'burn = value capture' is validated as **invalid or reversed**" | invalid/reversed | binary | "burn is a **Monetary Supply Indicator** and **does not constitute** a Value Capture indicator (mechanism-layer judgment)" |
| "L1 execution demand **must** structurally recover" | must | fabricated necessary condition (CA-04) | "L1 execution demand **is one of the main channels, not a necessary condition for all forms of capture**" |
| "net supply **must** return to neutral or deflationary" | must | fabricated necessary condition (CA-03) | deleted; changed to Supply Growth vs Demand Growth |
| "At the L2 level **no** mainstream mechanism exists to buy ETH with profits or burn ETH" | no/none | insufficient evidence (the OP share exists) | "**no in-force mandatory flow-back mechanism has been observed to date**; the only known voluntary give-back today is the OP Superchain 2.5%/15% share, flowing to the OP Collective" |
| "issuance is **40×** burn", "40×" | — | the number is correct, but the wording served the "burn is ineffective" conclusion | number retained, use changed: only as a **monetary supply structure** description |
| "the **only** flow-back" | only | as above | "L1 cost is currently the **only mechanism-certain** L2→ETH channel, magnitude 0.146% (0.550% excluding Robinhood)" |
| "a system with **missing negative feedback**" | judgmental | descriptive inference | "issuance ∝ √stake → staking increases accompanied by issuance increases; **this is a mechanism description, not a judgment on outcomes**" |
| "**biggest risk**" | biggest risk | risk definition undefined | "**single-point uncertainty**: mNAV / exchange holdings (`[UNKNOWN]`)" |
| "**inevitably**"-type phrasing | inevitably | none | removed throughout; changed to "holds under … conditions / not observed" |

---

### 4. List of phrasings deleted/replaced this round (substitute directly when writing) {#sec-4-list-of-phrasings-deleted-replaced-this-round-substitute-directly-when-writing}

| Delete | Replace with |
|:--|:--|
| Value Leakage (referring to application-layer/L2 retention) | Structurally outside protocol capture / Discretionary non-capture |
| L2 profit margin / `毛利` / `留存率` (used alone) | **gross economic retention** + **L1 cost share** |
| "stablecoins do not transmit" | Channel A / Channel B stated separately |
| "demand is falsified" | "has not yet provided sufficient evidence that … transmits" |
| four necessary conditions / 0/4 | Value Capture Transmission Status (five-tier labels) |
| "validated as invalid or reversed" | Not demonstrated / Weak evidence (noting the mechanism layer or the magnitude layer) |
| "must", "only", "none", "inevitably", "certainly" | "current evidence supports / partially supports / not yet proven / no sufficient evidence yet / to be observed" |
| "only deflation shows capture" | "Supply Growth vs Demand Growth" |

---

### 5. The audit's own boundaries (what this round does not resolve) {#sec-5-the-audit-s-own-boundaries-what-this-round-does-not-resolve}

1. **Does not resolve the magnitude gaps**: the MEV split, exchange holdings, lending collateral share, historical blob price series, and DAT industry-wide scale **remain `[UNKNOWN]`** (see `Part IX (monitoring dashboard)` §7 `[UNKNOWN]` fill-in roadmap). Conceptual corrections **cannot substitute for** this data.
2. **Does not change any v1.0 number**: no load-bearing figure was re-fetched this round.
3. **Makes no price judgment**: the `ETH Economic Value` segment only registers observations (price, monetary premium ratio), and **does not read price as** proof or disproof of capture (No Price Shortcut).
4. **Does not set a conclusion direction**: the strength of this round's conclusions is decided by the evidence, not by "hoping v1.1–v1.4 looks better" (last sentence of mandate brief §24).

---

## Part Four | Transmission Framework (eight-segment chain / four layers / 2×2) {#part-four-transmission-framework-eight-segment-chain-four-layers-2-2}

### 1. Positioning of the framework (why it extends beyond the ETH topic) {#sec-1-positioning-of-the-framework-why-it-extends-beyond-the-eth-topic}

The question this framework answers has been upgraded from "how much of Ethereum's economic value can ETH capture" to:

> **Through what Transmission Mechanism does the economic value created by Ethereum ultimately transmit to ETH?**

**Portability**: replace "Ethereum / ETH" with any "network / token" and the chain and criteria still hold. It is therefore also the base framework for ZK Labs' subsequent research on **L2 / Stablecoin / RWA / DeFi / Solana vs Ethereum**:

| Subsequent topic | Which part of this framework is used directly |
|:--|:--|
| L2 | Chain segments 3→4 (Value Distribution → Protocol Capture) + five channels B |
| Stablecoin | eight-segment chain (Channel A/B separated) + counterfactual matrix §Stablecoin |
| RWA | segments 4→5 (Capture → Demand) + counterfactual §Collateral |
| DeFi | segment 5 (Asset Capture) + collateral share definition |
| ETH | the full chain |
| Solana vs Ethereum | eight-segment chain side by side + counterfactual §Settlement |

---

### 2. The trichotomy: Value Creation ≠ Value Capture ≠ Cash Flow (brief §15) {#sec-2-the-trichotomy-value-creation-value-capture-cash-flow-brief-15}

| Concept | Question answered | Observation definition | Why it cannot be conflated |
|:--|:--|:--|:--|
| **Value Creation** | Where does economic activity occur? | Transaction volume, total fees, user count, settlement value | It measures **scale**, it does not answer attribution |
| **Value Capture** | Who obtains the economic value? | attribution determination (who receives the money, who benefits) | Attribution ≠ scale; scale can rise while attribution is unchanged |
| **Cash Flow Capture** | Who obtains **distributable cash flow**? | actual cash inflow to a given entity | It is a **proper subset** of Value Capture |

#### The separation of the three must be proven with one complete case (hard requirement of the brief §15)

**Case: user transactions on L2 (2026-09 definition)**

| Layer | Value | Entity |
|:--|:--|:--|
| Value Creation | **L2 processes 94.6% of transactions** (L2 988.3M transactions vs L1 56.9M); L2 user fees **$1,634,574/day (2026-09 monthly average)** | economic activity occurs on L2 |
| Value Capture | applications / sequencing layer take **$1,630,763/day gross**; L1 takes only **$2,387/day (0.146% (0.550% excluding Robinhood))** | value accrues to L2 operators |
| Cash Flow Capture | **ETH-side cash flow = blob $234/day (100% burned) + L1 execution gas ≈$2,153/day** | only this part enters ETH |

**What the separation proves**: `Value Creation ↑` (L2 transactions and fees at record scale) **while simultaneously** `ETH Cash Flow Capture` is minimal (0.146% (0.550% excluding Robinhood)). **And even so, ETH Asset / Monetary Capture may still exist independently** — because ETH remains the security anchor and largest collateral of L2 (Chain segments 5–6). **That the three move in different directions is the core fact of this framework.**

---

### 3. The eight-segment transmission chain and per-segment status (brief §2 / §23) {#sec-3-the-eight-segment-transmission-chain-and-per-segment-status-brief-2-23}

```
Economic Activity
   ↓  ?
Economic Value Creation
   ↓  ?
Value Distribution
   ↓  ?
Ethereum Protocol Capture
   ↓  ?
ETH Demand / Utility
   ↓  ?
ETH Asset Capture
   ↓  ?
ETH Monetary / Network Premium
   ↓  ?
ETH Economic Value
```

| # | Segment | Status | Evidence (primary) | Break-point note |
|:--|:--|:--|:--|:--|
| 1 | **Economic Activity** | 🟢 Demonstrated | L2 988.3M transactions/month, L1 56.9M; L1 block utilization ≈100% of target (v2.0 correction); blob 154.7 GB/month | — |
| 2 | **Economic Value Creation** | 🟢 Demonstrated | ecosystem gross value **$586.7M/month** (split definition); application-layer fees $521.6M/month | definition caveat: cross-layer stacking, read as order of magnitude |
| 3 | **Value Distribution** | 🟢 Demonstrated | attribution by layer is measurable: applications $521.6M/month, L2 **$1,630,763/day**, L1 $16.0M/month | — |
| 4 | **Ethereum Protocol Capture** | 🟡 **Partially demonstrated** | L1 protocol fees $16.0M/month; **÷ reported ecosystem gross-value proxy ≈ 2.73% (a magnitude ratio, not a strict capture rate)**; of which permanently burned **$5.44M/month (≈ 0.93% on the same definition)**; L1 fees trailing-365d YoY **−79.6%** | **the mechanism holds but the magnitude is minimal, and it is compressed by the protocol's own scaling** |
| 5 | **ETH Demand / Utility** | 🟡 **Partially demonstrated** | staking 44,061,701 ETH (36.09%); validator revenue **95.04% from issuance**; gas must be paid in ETH | **demand exists, but its composition determines that it is not external value acquisition** (it is dilution protection) |
| 6 | **ETH Asset Capture** | 🟠 **Weak evidence** (share definition missing) | ETF+DAT locked ≈13.52M (11.1% of circulating); Lido $26.76B, Aave v3 $18.36B, Morpho $11.25B, EigenLayer $7.10B with ETH at the core | **the quantity exists; ETH's share of lending collateral is `[UNKNOWN]`** ※[Errata ②](#errata-1) |
| 7 | **ETH Monetary / Network Premium** | ⚪️ **Unknown** | ① **input-side readings (definite facts)**: Ethereum stablecoin share **53.7% → 47.3% (−6.4pp)**, YTD −10.7% (all chains +1.5% over the same period) → readings on network / unit-of-account standing **weakening**; ② **the only proxy**: ETH/stablecoin market-cap ratio **2.543 → 1.778 → 1.182 → 1.077**, **but that ratio is derived from price** | **v1.4 re-rating (🔴→⚪️)**: the numerator of the proxy is ETH market cap (= price) ⇒ using it to measure premium amounts to **testifying via a detour through price**, which conflicts with No Price Shortcut; for this layer the direct evidence **does not even have a metric definition** ⇒ **the report has no valid measurement instrument and is not in a position to issue the negative judgment "Not demonstrated"** |
| 8 | **ETH Economic Value** | ⚪️ **Unknown (not adjudicated this round)** | price 2025-10→2026-10 **−36.9%**; 2026 YTD −9.91% | **under No Price Shortcut, price is not evidence for this segment**; this segment registers observations only, **it draws no conclusion** |

> **Term mapping (chain segment ↔ layer ↔ label)**: chain segment 6 `ETH Asset Capture` = **Layer 3 `Asset / Collateral Demand`** of the four-layer framework; the two share the same evidence set and **the same tier conclusion** (🟠 Weak evidence) — segment 6 measures "quantity of assets accumulated" (13.52M locked, 36.09% staked), while Layer 3 additionally requires a "collateral share denominator"; **the same gap (missing share definition) prevents either from being upgraded to Partially demonstrated**. Segment 8 `ETH Economic Value` has no corresponding layer (⚪️ not adjudicated this round).

#### Locating the break points in the chain (core output of this framework)

- **Between segments 4 and 5**: `Protocol Capture` is minimal and falling → yet `ETH Demand` rises (staking 3.6× over 4 years) ⇒ **the two do not share a source**: demand is not driven by protocol cash flow.
- **Between segments 6 and 7**: the quantity in `Asset Capture` is growing (13.52M locked, 36.09% staked) → the **input-side readings** of `Monetary Premium` **weaken** (stablecoin share −6.4pp) ⇒ **current evidence does not show that growth on the asset / holder side has already transmitted into an observable monetary / network premium** (**Transmission not demonstrated**, not "transmission failed"). **v1.4 addition: the output side of segment 7 has itself been re-labeled ⚪️ (no valid measurement instrument), so this sentence is confined to "input-side readings weakening" and must not be upgraded to "the premium has fallen".** This is the **key break point** for the question the brief §17 requires adjudicating: whether a "structural migration has actually occurred".
- **Conclusion (strict wording)**: **on evidence as of 2026-10-02, the chain holds 🟢 in segments 1–3 (activity, creation, distribution); 🟡 partially holds in segments 4–5, with 🟠 weak evidence in segment 6; ⚪️ undecidable in segment 7 (no valid measurement instrument); ⚪️ not adjudicated in segment 8.** Changes in **the composition of the mechanism** are observable; **the migration of value capture** is an interpretation; **the realization of that migration** has not yet formed verifiable evidence.

---

### 4. The four-layer Value Capture Framework v2.0 (brief §4) {#sec-4-the-four-layer-value-capture-framework-v2-0-brief-4}

Each layer answers seven items: Value Creation ｜ Capture Mechanism ｜ Transmission Mechanism ｜ Evidence ｜ Evidence Against ｜ Current Status ｜ Unknown.

#### Capture matrix (2×2): putting "non-cash-flow capture" back inside the framework

The four layers are cut by **mechanism domain**; the 2×2 below is cut by **whether cash flow is formed** and **whether transmission is direct** — it is used to answer the most substantive gap in v1.0: captures of the kind that have **no measurable "quantity"**, such as collateral and monetary premium, previously had no place to sit.

| | **Direct (goes directly to the protocol / holder)** | **Indirect (via demand and asset standing)** |
|:--|:--|:--|
| **Cash-Flow Capture** | gas / base fee burn / priority fee / blob burn / L2 settlement gas (= Layer 1) | MEV-related demand (builder / searcher payment path) |
| **Non-Cash-Flow Capture** | ETH settlement utility and validator security lock-up (= the security component of Layer 2) | collateral / asset demand / monetary premium / ecosystem capture (= Layer 3, Layer 4) |

**How to read it**: ETH's **Cash-Flow Capture is currently very weak** (L1 protocol fees ÷ ecosystem gross-value proxy ≈ 2.73% magnitude ratio, settlement flow-back 0.146% (0.550% excluding Robinhood)), but **Non-Cash-Flow Capture still exists** — "the mechanism exists" and "it has been realized as ETH economic value" are two different things, and the break point lies between segments 6→7 of the chain in §3. This matrix has been a **first-class framework component since v1.2** (retained in v1.3) (a second coordinate system standing alongside the four layers, see `Appendix C (version history and revision trail)`); it adds no new criteria and changes no four-layer classification definitions, so all v1.1 status conclusions remain valid as written.


#### Layer 1 — Protocol Cash Flow: does Ethereum directly obtain economic rent?

| Field | Content |
|:--|:--|
| **Value Creation** | L1 block-space demand (execution gas) + blob data-space demand (DA) |
| **Capture Mechanism** | base fee burn (100% to all holders); priority fee / MEV tip → validator fee recipient; blob fee burn; L2 pays L1 execution gas (burn + validator) |
| **Transmission Mechanism** | the mechanism is **explicit and observable**: gas must be paid in ETH → base fee units are burned → priority fees enter validator accounts. **All four questions are answerable** (who pays: users/L2; in what currency: ETH; into whose account: burn + fee recipient; whether burned: base fee and blob fee burned 100%; priority fee not burned, enters validator accounts) |
| **Evidence** | L1 collects **$16.0M/month**; permanently burned **$5.44M/month**; blob revenue **$143–234/day** (0.026%–0.043% of L1 fees); security budget 1,069,394 ETH/year |
| **Evidence Against** | the 4844 phase change: burn/issuance **138.7% (2022-09-15→2024-03-12 average) → 19.7% (2024-03-13→2026-10-01 average; ⚠️ both values are window averages for "before/after 4844", not current values — current trailing 30 days 2.52%, trailing 365 days 2.60%, trailing 90 days 1.81%**; net supply **−0.238%/yr → +0.652%/yr**; L1 fees trailing-365d YoY **−79.6%**; 365d burn 26,469 ETH = **2.5%** of security spending |
| **Current Status** | 🟡 **Partially demonstrated** (the mechanism holds completely; the magnitude was compressed by **deliberate scaling**, not defeated) |
| **Unknown** | whether `FeeTotNtv` includes blob fees; the standalone blob burn amount (the `fake_exponential` bug); attribution of the 8.7% error in daily burn |

#### Layer 2 — Security / Settlement: does Ethereum capture economic value through settlement / DA / security / staking?

| Field | Content |
|:--|:--|
| **Value Creation** | L2 activity requires **final settlement and a security anchor**; rollups require DA; cross-chain assets require a trusted settlement layer |
| **Capture Mechanism** | ① L2 → L1 settlement / proof-verification fees; ② blob DA fees; ③ the validator security budget denominated in ETH and locking up 36.09% of supply |
| **Transmission Mechanism** | settlement layer: **exists but is extremely thin** — L2 pays L1 **$2,387/day (0.146% of its fees (0.550% excluding Robinhood))**. Security layer: **exists and is explicit** — validators must lock ETH to participate, 44,061,701 ETH are locked; but **95.04% of revenue comes from issuance** |
| **Evidence** | Ethereum is the security anchor for **94.6%** of L2 transactions; blob carries 154.7 GB/month; EIP-7918 anchors the blob price to the L1 base fee (measured ratio **0.931**, range [0.741, 1.087]); staking rate 36.09% |
| **Evidence Against** | settlement rent share 0.146% (0.550% excluding Robinhood); blob unit price $0.003015 (DA allocated per L2 transaction **$3.6e-6**); 95.04% of validator revenue is an issuance transfer (**not external value**) |
| **Current Status** | 🟡 **Partially demonstrated**; the security component within it is **Demonstrated (composition determines the nature)** |
| **Unknown** | the actual appeal of non-Ethereum DA (Celestia / EigenDA) to L2s (no L2-side breakdown of DA sources); the official definition of L2 settlement / proof fees (growthepie `labels` 403) |

#### Layer 3 — Asset / Collateral Demand: does ecosystem growth increase asset/collateral demand for ETH?

| Field | Content |
|:--|:--|
| **Value Creation** | DeFi lending / derivatives / restaking require high-quality collateral; institutions require a custodiable, auditable, compliance-ready reserve asset |
| **Capture Mechanism** | ETH as native collateral (no bridging, no counterparty issuance); derivative demand for LSTs/LRTs; ETF/DAT balance-sheet holdings |
| **Transmission Mechanism** | **a nameable path**: collateral demand → ETH locked → reduced circulating supply + persistent borrowing demand. But **one link is missing**: ETH's **share** of lending collateral (vs BTC / stablecoins / RWA) is **not measurable** |
| **Evidence** | staking rate **9.73% → 36.09%** (3.6× over 4 years); ETF+BitMine+SharpLink **≈13.52M = 11.1% of circulating**; Lido $26.76B (≈9.84M stETH = 22.5% of active stake), Aave v3 $18.36B, Morpho $11.25B, EigenLayer $7.10B (≈2.59M ETH); Aave v3 Ethereum-chain borrows $10.31B |
| **Evidence Against** | ETH price over the same period **−36.9%** (**under No Price Shortcut this item may not serve as counter-evidence on capture; it is a co-existence observation only**); **exchange balances unavailable** → cannot distinguish net new inflow from custody migration; all-category RWA only **$4.69B** (BUIDL 43% on Solana > 19.7% (post-4844 window average; current trailing 30 days 2.52%) Ethereum) |
| **Current Status** | 🟠 **Weak evidence** (observables are plentiful, but the **share definition is missing**, making comparison with BTC/stablecoins/Treasury impossible, hence not classified as Partially demonstrated) |
| **Unknown** | ETH/LST share of collateral in lending protocols (Aave/Morpho APIs not retrieved); exchange ETH balances; whole-industry DAT scale; validator entity attribution |

#### Layer 4 — Monetary / Network Premium: does network standing strengthen ETH's monetary premium?

| Field | Content |
|:--|:--|
| **Value Creation** | a need for a **neutral, counterparty-free, composable** on-chain unit of account and settlement; stablecoins/RWA/derivatives need a unit of account and margin asset |
| **Capture Mechanism** | ETH as settlement asset / reserve asset / global crypto collateral; economic activity denominated in ETH |
| **Transmission Mechanism** | **theoretically sound but currently unmeasurable**: network standing → unit-of-account demand → premium. **This layer has no usable measurement instrument** (no aggregator source on this machine, see Unknown); the only available relative metric is **derived from price**, and its denominator has separate drivers ⇒ **it does not constitute a measurement of premium**. **Only the input-side readings are falsifiable** (stablecoin share, chain-level fees ranking) |
| **Evidence** | ETH remains the largest on-chain collateral and the L2 security anchor (see Layer 2/3) |
| **Evidence Against** | monetary premium proxy (ETH/stablecoin market-cap ratio) **2.543 → 1.778 → 1.182 → 1.077** (four points, monotonically declining); Ethereum stablecoin share **53.7% → 47.3%** (−6.4pp; **v2.0 definition limitation: L1-only**); Ethereum-side stablecoins YTD **−10.7%** (all chains +1.5%); 2025 chain-level fees ranking Ethereum 4th |
| **Current Status** | ⚪️ **Unknown** (**no usable valid measurement instrument**). **Reclassified from 🔴 Not demonstrated in v1.4**. **⚠️ v2.0 (research review directive #3): this ⚪️ tier is the report's self-imposed limit** — the criterion requires that "a usable observation instrument exists and its readings point to non-occurrence" before 🔴 may be assigned; this layer has **no valid price-independent measurement instrument at all**, so it **can only remain at ⚪️, which constitutes neither evidence of "not captured" nor evidence of "captured"**. **The necessary and sufficient condition for upgrading to a higher tier = obtaining a second, independent, price-independent metric** (the first candidate = the scale of ETH-denominated economic activity, whose metric definition has not yet been established, see D4 / roadmap). **Until the second independent metric is in place, this layer must not be upgraded on the basis of any indirect reasoning, mechanism narrative, or price-derived quantity**: the only proxy is price-derived ⇒ using it to measure premium conflicts with No Price Shortcut; for the direct evidence (ETH-denominated economic activity) the metric is undefined; **with no measurable instrument, "Not demonstrated" is a negative conclusion that cannot be supported by evidence**. **The definite facts registered are confined to the input side: stablecoin share 53.7% → 47.3%, Ethereum side YTD −10.7% (all chains +1.5%)** |
| **Unknown** | the scale of ETH-denominated economic activity (no aggregator source); institutional definition of "reserve asset" use; ETH's share of cross-chain collateral |

#### Mechanism exposition for Layer 4: **Composability Premium** (elevated in v1.5 | **tier unchanged: ⚪️ Unknown**)

> **Premise**: the tier of this section **remains ⚪️ Unknown** — this section **adds mechanism reasoning (a hypothesis), not readings**. Because no usable valid measurement instrument exists, **no matter how complete the mechanism story, the tier cannot be upgraded** (decision principle 4).

**Why "composability" may constitute a genuine bid / lock-up channel (transmission hypothesis)**:
1. **The current pain point is fragmented liquidity**: ecosystem transaction volume is already carried by multiple heterogeneous L2s (this report's definition: **26 chains** within growthepie's 90-day window; L2 accounts for **94.6%** of transactions). The coexistence of multiple domains means **a single cross-domain interaction needs one adjudicator**.
2. **Candidate mechanisms for atomic interoperability** (**all are roadmap candidates, none is an already-effective mechanism**): based rollup (sequencing returned to L1), shared sequencers, cross-chain intent standards (candidates such as ERC-7683). The common structure of these mechanisms is: **the more cross-domain interaction, the deeper the dependence on a "unified state adjudication court"**.
3. **ETH's position in this structure**: **within the observed set of crypto assets identified in this report**, ETH is **the only asset that serves as collateral in native form and has no issuing entity and no counterparty** (cross-chain versions of other assets require bridges or wrapping entities). **This step is a judgment about "property attributes", not about "value capture".**
4. **The hypothesis derived from this (this step must remain a hypothesis)**: if atomic interoperability becomes the dominant mode of interaction, then **the native collateral of the unified adjudication court** would gain structural demand — its strength depends on "total cross-domain interaction × dependence on the unified adjudication court × whether collateral must be a native asset", and **none of the three variables has any quantified reading within this machine's evidence set**.

**Why it "has no dashboard" (the direct reason it stays ⚪️)**:
- the premium manifests as **"having to hold"**, not as a bookable cash flow — **no fee, no burn, no flow-back**, therefore **any cash-flow-type observation point (Group A / Group B) is inherently blind to it**;
- the direct readings would be "**the scale of ETH-denominated economic activity**" and "**ETH's share of cross-domain collateral**" — **neither even has a metric definition** (see D3 / D4 and the roadmap in "Part Nine");
- therefore: **this mechanism can explain "why the standing may persist", but it cannot prove "value has been captured".**

**Statement of theoretical standing (`[INTERPRETATION]`, strictly bounded)**:
> **Among the architectural differences identified, composability / counterparty-free collateral is the most fundamental structural difference between Ethereum and a monolithic chain.** That difference **explains only "difficulty of substitution"**, **not "revenue"** — high switching difficulty ≠ someone pays for it, and still less ≠ that payment flows to ETH holders. **This report does not treat "moat" as a synonym for "capture"** (this is the same theme as P0-1: "the mechanism exists ≠ value capture has occurred").


| Channel | Path | Type | Current magnitude | Status |
|:--|:--|:--|:--|:--|
| **A** | L1 Execution → Fees → Burn → ETH | **Direct** | $16.0M/month (of which burn $5.44M) | 🟡 partial (magnitude compressed by its own upgrades) |
| **B** | L2 → DA / Settlement → Ethereum → ETH | **Indirect** | $2,387/day (0.146% (0.550% excluding Robinhood)) + blob $234/day | 🟡 partial (thin mechanism, tiny magnitude) |
| **C** | Ethereum Security → Staking → ETH demand | **Asset-demand** | 44,061,701 ETH locked; 95.04% of revenue from issuance | 🟡 partial (composition problem) |
| **D** | Ethereum ecosystem → ETH collateral → ETH demand | **Asset-demand** | ≈13.52M locked; collateral standing (share definition missing) | 🟠 weak |
| **E** | Ethereum network → Monetary / reserve role → ETH premium | **Monetary** | no primary magnitude metric; the only relative metric is **derived from price** (does not constitute measurement) | ⚪️ **Unknown** (changed from 🔴 in v1.4: no valid measurement instrument) |

**Key criterion**: **A is not a precondition for the other four.** v1.0 wrote "a recovery in L1 execution demand" as "the only variable that can simultaneously enlarge all three channels" and treated it as a necessary condition; v1.1–v1.4 correct this to: **A is the channel with the highest amplification efficiency, but whether C/D/E hold does not depend on A.**

---

### 6. ETH Demand-Supply Absorption Framework (brief §5) {#sec-6-eth-demand-supply-absorption-framework-brief-5}

Replaces v1.0's "deflation = necessary condition".

```
Value Creation / Capture
        ↓
   ETH Demand Growth        ← staking demand + collateral demand + settlement/unit-of-account demand + institutional allocation
        vs
   ETH Supply Growth        ← issuance (∝ √effective stake) − burn (∝ L1 execution demand)
        ↓
   Absorbed?  → demand growth > supply growth ⇒ absorption holds
```

| Element | Current reading | Note |
|:--|:--|:--|
| Supply Growth | **+1,052,326 ETH/year (+0.862%)**; daily issuance 2,986.6 ETH/day | **∝ √effective stake**: more staking → more issuance (mechanism description) |
| Supply Growth components | 365d issuance 1,016,345 ETH vs burn 26,469 ETH (**issuance is 38.4× the burn**) | burn is a **monetary supply indicator**, not a capture indicator |
| Demand Growth | staking 9.73% → 36.09% (4 years); 11.1% of circulating locked | measurable, but **composition unproven** (issuance dilution transfer vs external demand) |
| **Absorption verdict** | **cannot yet be adjudicated** | because the **composition** of demand is unproven (Layer 3 Unknown) — this is not "not absorbed", it is **an unreliable denominator** |

**Framework discipline**: `Burn > Issuance` **must not** be read as `ETH value capture ↑`; `Issuance > Burn` **must not** be read as `ETH value capture ↓`. Both are **Monetary Supply Indicators**.

---

### 7. The four-question criterion for Transmission Mechanism (mandatory throughout) {#sec-7-the-four-question-criterion-for-transmission-mechanism-mandatory-throughout}

Any claim that "transmission holds" must be able to answer:

1. **Who pays?** (users / L2 / institutions / applications)
2. **In what currency?** (ETH / stablecoins / fiat / their own token)
3. **Into whose account?** (burn / validators / protocol treasury / application operators / issuers)
4. **Is it burned or locked?**

| Criterion outcome | Status |
|:--|:--|
| All four answered ∧ magnitude measurable | Demonstrated |
| All four answered ∧ magnitude unmeasurable or minimal | Partially demonstrated |
| Not all four answerable (one link missing) | Weak evidence |
| Unanswerable (no observable path) | Not demonstrated |
| No data | Unknown |

**Application examples**: application-layer $521.6M/month → question 3 "into whose account" = application operators, **not** ETH → **Not demonstrated** (rather than "leakage"). Stablecoin issuer Treasury interest → question 3 = issuer → **Not demonstrated** (Channel A). L2 → L1 execution gas → all four answered, magnitude 0.146% (0.550% excluding Robinhood) → **Partially demonstrated**.

---

### 8. Application boundaries of the framework {#sec-8-application-boundaries-of-the-framework}

1. **No price forecasting**: chain segment 8 (ETH Economic Value) is **not adjudicated this round**; price and capture are neither sufficient nor necessary for each other.
2. **No TVL as a value proxy** (it entails double counting and price effects).
3. **No treating correlation as causation**; no writing "coexistence" as "proof" or "counter-evidence".
4. **No load-bearing conclusions from a single source**; single sources are marked `[UNKNOWN]` or downgraded to "reference".
5. **No treating gross as net** (for L2, gross economic retention is used throughout).

### 9. Version discipline {#sec-9-version-discipline}

- Changes to **criteria / classification / label definitions** = **a framework version change**, and must be logged in `Part Three (criteria and concept audit)` and `Appendix C (version history and revision trail)`.
- **v1.2 is a framework version change** — the 2×2 capture matrix is elevated to a first-class framework component; the decision criteria are unchanged, so status conclusions are unchanged.
- **v1.3 is a logic tightening (Final Logic Audit)** — the decision discipline "the mechanism exists ≠ value capture has occurred", splitting migration into five propositions, changing the objective function to observed trade-off, downgrading 2.73% to a magnitude ratio, four counterfactual tiers (Created abolished), and the monetary premium switched to a proxy definition. **Criterion definitions and status labels are unchanged, so the tier conclusions of the four layers and chain segments are preserved**, with only the strength of wording and naming tightened.
- **Pure data updates** (running the Dashboard) **do not change the version number**.
- The list of changes in this version relative to v1.0 is in the full text of `Part Three (criteria and concept audit)` (CA-01…CA-14 + §16 table).

---

## Part Five | Value Distribution Matrix {#part-five-value-distribution-matrix}

### 1. Three-stage framework (replacing v1.0's "Value Creation → Leakage") {#sec-1-three-stage-framework-replacing-v1-0-s-value-creation-leakage}

```
 Value Creation          Value Distribution              Value Retention
 scale of economic    →  who gets it (protocol/validators/ →  how much of it ultimately
 activity and total      L2/applications/issuers/            settles inside the ETH
 fees                    users/other chains)                 system (burn/lock/unit of account)
                          ↑ observable: attribution           ↑ basis: the four Transmission questions
```

**The problem with v1.0**: it jumped straight from "creation" to "leakage", skipping "distribution". The result was **reading a distribution fact (who gets it) as a moral judgment (who should not get it)**.

---

### 2. Value Distribution Matrix | 2026-09/10 definition (all reusing v1.0 primary data) {#sec-2-value-distribution-matrix-2026-09-10-definition-all-reusing-v1-0-primary-data}

| # | Entity | What it obtains | Value | Data strength | Relation to ETH |
|:--|:--|:--|:--|:--|:--|
| 1 | **Ethereum protocol (L1)** | base fee burn + priority fee/MEV tip + blob fees + L2 settlement gas | **$16.0M/month** (÷ reported ecosystem gross-value proxy ≈ **2.73%, a magnitude ratio, not a capture rate**); of which permanently burned **$5.44M/month (≈ 0.93% on the same definition)**; blob $143–234/day | strong (CM + DefiLlama dual source, 0.12% difference) | ✅ **collected directly** (Layer 1), but the magnitude is compressed by its own upgrades |
| 2 | **ETH (all holders)** | ① proportional scarcity from burning ② the issuance share available to stakers | burn $5.44M/month; **non-staking holders diluted +0.862%/yr** | strong | ⚠️ **asymmetric benefit**: burning benefits all; issuance is a transfer **from non-stakers → stakers** |
| 3 | **Validators** | consensus-layer issuance + execution-layer tips (including all MEV tips) | **1,069,394 ETH/year ≈ $2,891M**; composition **95.04% issuance / 4.96% usage**; = **0.876%** of market cap, **2.43%** of staked market cap | strong | ✅ capture (the security component of Layer 2), but **composition determines the nature** |
| 4 | **L2 (operators / DAOs)** | user fees − L1 costs − other costs | **$1,630,763/day gross** (≈$595M/year); L1 takes only 0.146% (0.550% excluding Robinhood) | medium-high (**gross definition**) | ❌ **no flow-back mechanism** (Discretionary non-capture) |
| 5 | **Sequencers** | L2 user fees (extremely concentrated) | Robinhood Chain **$1,359,679/day (83.2%)**; Base **$157,859/day (9.7%)**; two chains **92.8%** | medium-high (**2026-09 monthly average; source has only a 90-day window**) | ❌ same as above; moreover **concentrated in two TradFi listed-company chains** |
| 6 | **Applications** | the applications' own fees and revenue | **$521.6M/month** (**L2 application layer** fee definition; 2026-09, 26 chains, growthepie 90-day window); Uniswap 2025 fees $1,054.26M, fee-switch protocol revenue $28.55M | medium-high | ❌ **Structurally outside protocol capture** (the protocol holds no claim) |
| 7 | **Stablecoin issuers** | **Treasury interest** on reserve assets | reserve scale: all chains **$311.18B** / Ethereum side $147.08B | strong (scale) / **weak (profit)** | ❌ **Channel A: usually does not transmit to ETH directly** |
| 8 | **Infrastructure** | node/RPC/MEV infrastructure service fees | `[UNKNOWN]` (no aggregator source) | — | ⚪️ unknown |
| 9 | **MEV (searcher / builder)** | extractable value captured | **`[UNKNOWN]`**; validator-side upper bound **53,049 ETH/year ≈ $143M (0.043% of market cap)** | mechanism strong / **no source for the breakdown** | ⚠️ part of the upper bound reaches validators; **the remaining share is unmeasurable** |
| 10 | **Users** | the dividend of falling costs | average per-transaction fee on the same definition: **2024Q1 $13.21 → 2026Q2 $0.275** (−97.9%); DA allocated per L2 transaction **$3.6e-6** | medium-high (definition annotated) | — (users are beneficiaries of value distribution, not a capture) |
| 11 | **Other networks** | the **increment** in stablecoin and settlement share | Tron $93.99B (30.0%), Solana ≈$16.5B (5.3%); 2025 chain-level fees: Hyperliquid $971.67M(1) / Solana $645.22M(2) / Tron $579.33M(3) / Ethereum $523.17M(4) | strong (share) / medium (fees ranking definition caveat) | ❌ the increment occurs outside Ethereum |

---

### 3. "Which value was not captured by ETH?" — strict adjudication {#sec-3-which-value-was-not-captured-by-eth-strict-adjudication}

> Brief §7: **"Value Leakage" may be used only where the Leakage admission conditions are met.**

| Value flow | Amount | Meets Leakage admission conditions? | v1.1–v1.4 characterization | Reason |
|:--|:--|:--|:--|:--|
| Application-layer fees | $521.6M/month | **No** | **Structurally outside protocol capture** | the protocol **never designed** a claim on application-layer revenue; and there is no existing mechanism by which it "could in theory be captured by the protocol" (unless a sequencer revenue tax-grade redesign appears) |
| L2 gross retention | $1,630,763/day | **No (it is a policy choice)** | **Discretionary non-capture** | mechanically "could be collected or not"; EIP-7918 already establishes a blob floor → showing the protocol **is able** to price but **chooses** to price low |
| L2 → other chains / other DA | not decomposed | **Unknown** | `[UNKNOWN]` | missing decomposition of L2-side DA sources and settlement destinations |
| Stablecoin reserve interest | not quantified | **No** | **Channel A: not an ETH transmission path** | this value is created by issuers and the Treasury market and **never passes through Ethereum's mechanism** |
| Net supply dilution | +1,052,326 ETH/year | **No** | **Monetary supply effect** | dilution is a transfer between holders, not "capturable but not captured" |
| Searcher/builder share of MEV | `[UNKNOWN]` | **Possibly yes, but unmeasurable** | **Unmeasured (not Leakage)** | if it were confirmed that "priority fees the protocol could have captured are being taken externally", it could be upgraded to Leakage; **there is currently no data** |
| Opportunity cost of blob revenue under a low base fee | `[SCENARIO]` | **Conditionally yes** | **Potential non-capture (conditional, not counted as Leakage)** | only where the L1 execution base fee stays low for long does blob revenue sit systematically below its potential under demand-based pricing. **The counterfactual is unmeasurable** and can only be a scenario |
| 8.7% error in daily burn | ~6.5 ETH/day | **No** | **Measurement gap** | a measurement issue, not a value-flow issue |

**Conclusion**: **under strict definitions, none of the three major "leaks" listed in v1.0 strictly meets the definition of Value Leakage.** They are, respectively: value outside the protocol (application layer), voluntary non-collection (L2), and a monetary policy effect (dilution). **Given the observation set available on this machine, the only things that could constitute Leakage are the MEV breakdown and the blob opportunity cost, and both are currently unmeasurable** — which is itself a research conclusion: **this round cannot, in a strict sense, identify a single instance of "Value Leakage".**

---

### 4. Brief §8: Value Retention vs Network Expansion (the L2 upgrade) {#sec-4-brief-8-value-retention-vs-network-expansion-the-l2-upgrade}

**Core question**: > **Is Ethereum sacrificing unit protocol rent in exchange for a larger economic network?**

#### Direction 1 | Network Expansion path (positive)

```
L2 Growth → Lower L1 marginal cost → More economic activity
→ More settlement / DA → Potential ETH demand
```

| Evidence | Value |
|:--|:--|
| activity does stay inside the ecosystem | L2 processes **94.6%** of transactions (988.3M/month); blob carries **154.7 GB/month** |
| costs are indeed pressed down | capacity **4.7×** (target 3→14); DA allocated per L2 transaction **$3.6e-6** |
| L1 is not left idle | L1 block gasUsed ≈**30.2M/block ≈ 100% of EIP-1559 target (30M)**, about **50% of gas limit (60M)** (**v2.0 correction**: the earlier "84% full (30.2M vs target 36M)" mistook the pre-EIP-7935 old gas limit for the target) |
| pricing has not been zeroed | EIP-7918 measured ratio **0.931**, range [0.741, 1.087] → **blob price anchored at 1/16 of the L1 execution base fee** |

**What this reads as**: scaling is **an accomplished fact**, and it is institutionally protected (EIP-7918 sets a relative reserve price, suppressing the mechanical downward spiral to 1 wei; but it is a **soft floor**, with multi-block lag). **Yet the segment "More settlement / DA → Potential ETH demand" is still labeled "Potential"** — corresponding in the chain to segment 4 🟡 and segment 7 ⚪️ (re-labeled in v1.4).

#### Direction 2 | Rent Sacrifice path (negative)

```
L2 Growth → Sequencer captures economics → L1 fee compression → Lower ETH cash-flow capture
```

| Evidence | Value |
|:--|:--|
| sequencers take the overwhelming majority | L2 gross retention **99.77%**; L1 cost share **0.146% (0.550% excluding Robinhood)** |
| L1-side fees compressed | L1 fees trailing-365d **$552,414/day (annualized ≈$201.6M)**, YoY **−79.6%** |
| institutional phase change | burn/issuance **138.7% (2022-09-15→2024-03-12 average) → 19.7% (2024-03-13→2026-10-01 average; ⚠️ both values are window averages for "before/after 4844", not current values — current trailing 30 days 2.52%, trailing 365 days 2.60%, trailing 90 days 1.81%**; net supply **−0.238%/yr → +0.652%/yr** |
| listed-company corroboration | Base stablecoin transfer volume **+7× YoY** while Coinbase `Other transaction revenue` **YoY −11%** |

**What this reads as**: the decline in unit protocol rent is **an accomplished fact**, and **it was executed by Ethereum's own upgrades** (4844 / Fusaka / BPO1 / BPO2 / EIP-7918 are all scaling or price-capping). **⚠️ But this only shows "what happened", not "what Ethereum wants" — the objective function belongs to governance / design intent and is not inferred this round.**

#### From "choose one of three objective functions" to "observed economic design orientation"

> The brief's original question: **Is Ethereum currently: A. Maximizing Protocol Rent / B. Maximizing Economic Network / C. a dynamic balance between the two?**
> **v1.3 correction**: Ethereum's **objective function** is a governance / design-intent question, and public data **can neither confirm nor refute** it. This round answers an **observable** question instead: **what economic design orientation does Ethereum actually exhibit at present (Observed Economic Design)?**

**No objective-function inference is made; what follows states only the observable trade-off:**

| Observation item | Evidence status | Verdict |
|:--|:--|:--|
| **Unit protocol rent** | measurable decline (−79.6%; burn/issuance 138.7% (2022-09-15→2024-03-12 average) → 19.7% (2024-03-13→2026-10-01 average; ⚠️ both values are window averages for "before/after 4844", not current values — current trailing 30 days 2.52%, trailing 365 days 2.60%, trailing 90 days 1.81%); executed by its own upgrades (scaling + EIP-7918 price cap + L2 cost share 0.146% (0.550% excluding Robinhood))) | 🟢 **decline observed** |
| **Economic network scale** | activity, DA usage, and settlement anchoring stay within the Ethereum ecosystem (94.6% of transactions, 154.7 GB/month) | 🟡 **partially realized** |
| **Relation between the two** | the current architecture exhibits both "declining unit rent" and "expanding network scale" | 🟡 **observed trade-off** |
| **Objective function** (whether deliberately maximizing the network, or balancing the two) | **no primary governance document answering the "objective function"**; but **nameable roadmap and EIP records exist** (Glamsterdam SFI 18 includes ePBS/BALs/gas repricing; EIP-8363 Tapered Issuance Burn is **Draft only, not in SFI**) — **these records are observable but do not answer the objective-function question** (v2.0 reinforcement, see "Appendix E") | ⚪️ **not inferred this round** |

**Where the asymmetry of this trade-off lies**:
- **the cost side is realized**: the decline in unit protocol rent is **already occurred and measurable** (−79.6%, 138.7% (2022-09-15→2024-03-12 average) → 19.7% (2024-03-13→2026-10-01 average; ⚠️ both values are window averages for "before/after 4844", not current values — current trailing 30 days 2.52%, trailing 365 days 2.60%, trailing 90 days 1.81%);
- **the return side is unrealized**: the transmission from a larger economic network → ETH capture stands at a 2.73% magnitude ratio in segment 4, and **no usable valid measurement instrument** in segment 7 (re-labeled ⚪️ in v1.4);
- the accurate formulation is therefore: **"Ethereum's current architecture exhibits an economic trade-off in which unit protocol rent declines while L2 / DA / settlement activity expands; but on the evidence to date, no verifiable, proportional ETH value return has yet formed."**
- **this is an observed trade-off, not a confirmed design objective** — whether it is a conscious long-term economic strategy must be further established by governance documents / roadmaps / longer-horizon data. **v2.0 reinforcement**: roadmap records **are now nameable** (Glamsterdam SFI 18, EIP-8363 Draft, see "Appendix E"), so the wording is tightened from "no primary basis" to "**no primary basis that answers the objective function / intent**"; **the ⚪️ tier is unchanged**.
- **this is not a judgment about the future**, nor does it presuppose that the future will not deliver (brief §24, closing sentence: let the evidence determine the conclusion).

#### 04c | Sustainability of sequencer rent (elevated in v1.5)

**Observed facts**: L2 gross economic retention **99.854%** (L1-only definition; **99.450% excluding Robinhood**) / **99.77%** (including other costs); L1 cost share **0.146% (0.550% excluding Robinhood)**; Coinbase SEC primary source: Base stablecoin transfer volume **+7× YoY** while `Other transaction revenue` **−11%**.

> **【v2.0 addition ｜ P0-2】L2 definitions must be read both ways: with / without Robinhood Chain**

| Definition | L2 fees (USD/day, **2026-09 monthly average**) | L1 cost paid (USD/day, **2026-09 monthly average**) | L1 cost share |
|:--|--:|--:|--:|
| with Robinhood (25 chains, report definition) | 1,634,574 | 2,367 | **0.146%** (report value; v2.0 recomputation 0.145%, the $20/day gap being a snapshot difference) |
| **excluding Robinhood (24 chains)** | **274,894** | 1,512 | **0.550%** |

> **⚠️ Window-definition note (v2.0 second-round self-check correction ｜ F-1)**: the fee readings in the table above are **2026-09 full-month (30 days)** averages, **not** growthepie's 90-day window values. Measured on the same definition over 90 days (2026-07-03→09-30), Σ = **$786,267/day**, **less than half the value in this table** — because Robinhood Chain only launched on **2026-07-01** and had not yet ramped in July–August. **Wherever this report cites "the growthepie 90-day window", it refers to the upper bound of the window available from the data source; the reading itself is the 2026-09 full month** (this version has corrected the relevant wording accordingly).

**Distribution of L1 cost share by chain** (n=23, excluding items without data): **median 10.476%**, p25 0.444%, p75 **30.539%**, max 167.5% (manta), min 0.063% (Robinhood).

> **How to read it**: 0.146% is **a weighted average dominated by a single chain**; it represents neither a "typical L2" nor L2 as a whole — on the same definition, **excluding that chain gives 0.550% (3.8×)**, while the cross-chain median is **10.5%**. Wherever L1 cost share / gross retention is cited, the ex-Robinhood definition must be given alongside.

> **Three external facts (v2.0 primary verification, see `EXTERNAL_FACTS_VERIFIED.md`)**:
> ① Robinhood Chain mainnet launched **2026-07-01** (four sources agree: Robinhood official newsroom / Arbitrum official blog / PR Newswire);
> ② its gas subsidy is **official policy**: on 2026-08-07 the official X account lowered the gas sponsorship threshold from $5 to $0.50 (through 09-29), and on 2026-09-29 announced an extension to **2026-12-31**. **07-01→09-29 is about 90 days; the fee readings in this group take the 2026-09 full month (30 days), falling inside the subsidy period** (source window upper bound 90 days, see the definition note above);
> ③ **growthepie's own official documentation states**: `fees_paid_usd` (display name Revenue) is "the gross on-chain gas total paid by users to the sequencer", and in "How can Chain Revenue be gamed?" it states explicitly that "**chains can introduce fee incentives or subsidies** (e.g. gas credits) to encourage use, **which temporarily inflates revenue readings**" — **subsidies are not deducted**. ⇒ readings during the subsidy period are on a "**generated on-chain**" definition and equal neither "users' net outlay" nor sustainable revenue.


**What this set of readings shows (three layers, tightened layer by layer)**:
1. **Fact layer**: current gross margin remains largely on the L2 side (centralized sequencer structure) — this is **an observed distributional outcome**, not speculation.
2. **But this does not equal "sequencing rights constitute an impregnable monopoly moat"**: Coinbase provides **evidence in the opposite direction** — **volume is surging while revenue contracts**. If traffic growth cannot convert into revenue, the **sustainability of "retaining fees through information asymmetry and single-point sequencing" is weakened**. **The observable constraint comes from competition among L2s, not from Ethereum's will** (this is the same evidence set as **CE-5** in "Part Eight").
3. **Taiko's 61.7% is field evidence (n=1) that "sequencing rights can return to L1"**: after based rollup returns sequencing to L1 validators, **L1 cost as a share of its fees jumps from <0.5% under OP Stack to 61.7%** ⇒ **the L1 claim can be reactivated architecturally** (**technical feasibility has been proven by a single case; economic feasibility has not**).

**Conditional judgment (strictly not to be written as a forecast)**:
> **Conditional form**: **if** decentralized sequencing and censorship resistance become a **compliance necessity** for enterprise-grade chains, **and** a **second** measurable based / native rollup case appears, **then** the economics of the "sequencing rights return to L1" path will have adjudicable conditions — at which point **this report will on that basis revisit the magnitude of segment 4 (🟡) and channel B**.
> **Must not be written as**: "sequencing rights will be returned to L1", "the L1 claim will be reactivated" — **"will" is a forecast**, and this report contains no short-term forecasts and draws no conclusions about the future; moreover Taiko is **n=1, and unreproducible means it does not hold** (CE-4).

**⚠️ Three boundaries**: ① the readings above **do not include** a complete breakdown of L2s' own cost structures (Coinbase's line item is a consolidated definition and **cannot be used as Base's standalone P&L**); ② "enterprise-grade compliance necessity" **currently has no primary basis** (the regulatory path is undetermined) ⇒ **the antecedent of the conditional sentence is itself `[SCENARIO]`**; ③ this section **changes no tier** — it explains only "why 0.146% (0.550% excluding Robinhood) is **a quantity that can be repriced**", not "it has already been repriced".

---

### 5. The second case of the trichotomy: Stablecoin (brief §10 + §15) {#sec-5-the-second-case-of-the-trichotomy-stablecoin-brief-10-15}

Used to show that `Value Creation ≠ Value Capture ≠ Cash Flow` also holds **within a single economic phenomenon**:

| Layer | Stablecoin scenario | Conclusion |
|:--|:--|:--|
| **Value Creation** | on-chain stablecoin transfer activity (all-chain supply **$311.18B**); settlement volume and count | the activity genuinely exists |
| **Value Capture (Channel A)** | issuer reserves → Treasury interest → **issuer** | **does not pass through Ethereum's mechanism** → `Not demonstrated` for ETH |
| **Value Capture (Channel B)** | on-chain settlement → Ethereum/L2 gas and blob → **potential ETH demand** | **the transmission mechanism exists**, but magnitude unproven (Ethereum-side stock YTD **−10.7%**) |
| **Cash Flow Capture** | stablecoin-related gas that Ethereum obtains | **not decomposed** `[UNKNOWN]` (this determines "how much gas stablecoins contribute to ETH") |

**Key discipline**: **do not** write "Stablecoin growth has no transmission to ETH".
**Write instead**: "whether stablecoin growth **forms ETH value capture large enough through Ethereum settlement activity has not yet been proven on current evidence**; and issuer economics and on-chain economics must be stated separately."

---

### 6. Uncertainties in this section (not to be omitted) {#sec-6-uncertainties-in-this-section-not-to-be-omitted}

1. **Ecosystem gross value of $586.7M/month is a split definition**, the denominator includes cross-layer stacking and is **not entirely on the same layer** as L1 fees → 2.73% / 0.93% should be read as **the magnitude ratio of L1 protocol fees ÷ reported ecosystem gross-value proxy**, **not a clean economic capture rate**.
2. **growthepie's window upper bound is 90 days** (readings take the 2026-09 full month) → L2 concentration and the +296% month-over-month figure **have no cross-year validity**. **v2.0 reinforcement**: that window **coincides entirely** with Robinhood Chain's mainnet launch (2026-07-01) and the roughly 90-day gas subsidy period, and growthepie's official documentation states that "subsidies inflate readings and **are not deducted**" ⇒ these fees are on a **generated on-chain** definition and equal neither "users' net outlay".
3. **L2 gross retention does not deduct** sequencer servers, teams, or incentives → it must not be read as net profit; Coinbase's SEC primary source already shows that at the single-chain level "activity up, revenue down" is possible.
4. **The 2025 chain-level fees ranking has mixed definitions** (application fees of the Hyperliquid type are counted into the chain page, biasing it upward) → the ranking is not strong evidence.
5. **Exchange ETH balances are unavailable** → neither direction of "lock-up = net new inflow or custody migration" has been falsified.

---

## Part Six | Counterfactual (absent Ethereum, where would the value go) {#part-six-counterfactual-absent-ethereum-where-would-the-value-go}

### 1. Methodology: three-tier adjudication of counterfactuals {#sec-1-methodology-three-tier-adjudication-of-counterfactuals}

Counterfactuals **cannot be observed directly**. This framework permits only triangular inference from "**existence of substitutes + relative pricing + share change**", and confines conclusions to three tiers. **v1.3 correction**: the former (a) `Created` ("absent Ethereum this economic value would not exist") requires proving "the paradigm is irreplaceable + no competing implementation", which is an **unobservable counterfactual** — almost no historical technology can satisfy it. It has been split into **(a) Scaled First** (first to scale) and **(c) Hosted** (same-round self-check then tightened further, see the factual correction in §2):

| Verdict | Definition | Evidence requirement |
|:--|:--|:--|
| **(a) Scaled First** (first to scale) | Ethereum is **the first party to push the paradigm to scale** | requires **a verifiable scaling timeline + share history**; **must not** claim "earliest implementation" or "first invention"; **must not** be phrased as "absent Ethereum it would not exist" |
| **(b) Captured a share** | the economic activity **can exist on multiple networks**, and Ethereum obtains part of it | requires the share and the direction of the share |
| **(c) Hosted** | Ethereum **hosted the activity**, but **there is no evidence that** Ethereum created the corresponding economic value | requires proof that the value-creation mechanism is unrelated to Ethereum |
| **(a′) Created** (old tier) | ~~absent Ethereum this economic value would not exist~~ | **abolished in v1.3**: unobservable counterfactual, unfalsifiable |

**Mandatory limits**: ① a counterfactual proportion **must not** be treated as "money that can be taken away"; ② counterfactuals **must not** be used to infer price; ③ where substitute pricing data is absent, mark `[UNKNOWN]` and **do not infer**; ④ **do not** use unfalsifiable counterfactual historical judgments such as "absent Ethereum this value would not exist" — only the three tiers (a) Scaled First, (b) Captured a share, (c) Hosted are permitted. **Test: if a label requires you to deny someone else's earlier implementation, it is outside the falsifiable range.**

---

### 2. Stablecoin: Ethereum vs Tron vs Solana vs Other rails {#sec-2-stablecoin-ethereum-vs-tron-vs-solana-vs-other-rails}

#### Data (DefiLlama primary, 2026-10-02)

| Rail | Supply | Share | Direction |
|:--|--:|--:|:--|
| **Ethereum L1** | **$147.08B** | **47.3%** | **2026 YTD −10.7% (−$17.66B)**, share down from 53.7% |
| Tron | $93.99B | 30.0% | rising |
| Solana | ≈$16.5B | 5.3% | rising |
| remainder (incl. L2) | ≈$53.6B | 17.4% | — |
| all chains | **$311.18B** | 100% | **+1.5%** (all chains rising) |

#### Counterfactual decomposition (three layers must be kept separate)

| Layer | Substitution path (observable competing implementation) | Verdict |
|:--|:--|:--|
| **Reserve value** (Treasury interest) | stablecoin issuers' balance sheets and the Treasury market are **unrelated to Ethereum**; issuers earn interest regardless | **(c) Incidentally hosted** — Ethereum never participates in creating this value |
| **Settlement paradigm** (programmable, permissionless, 24/7 stablecoin transfers) | observable evidence: Ethereum is **the party that first pushed the paradigm to scale** (ERC-20 since 2015, DeFi peaking 2020–2021), share history observable; current competing implementations are Tron (cheaper) and Solana (faster) | **(a) Scaled First** (first to scale) — **claims neither "earliest implementation" nor "first invention"** (earlier implementations in the factual correction below); **asserts nothing about "absent Ethereum it would not exist"** |
| **Current increment** | all chains +1.5% while Ethereum **−10.7%** → the increment clearly falls to Tron/Solana | **(b) losing share** |

**Verdict**: **"Ethereum is the party that first pushed on-chain programmable stablecoin settlement to scale (a. Scaled First), but it does not create the reserve value of stablecoins (c); and it is currently ceding share to cheaper / faster rails (b, reversed)."** (The former "Created" formulation was abolished in v1.3: unobservable counterfactual; "first invention" was also abolished in the same self-check, for the reason below.)

> **⚠️ Factual correction (found in the v1.3 self-check, voluntarily withdrawn)**: an earlier draft of this version wrote that "Ethereum completed the **earliest verifiable implementation** of this paradigm in 2015–2017" — **that sentence is wrong and has been withdrawn**. **Earlier verifiable implementations** of programmable tokens / permissionless settlement:
> - **colored coins** (2012–2013): marking specific satoshis on Bitcoin to represent off-chain assets;
> - **Mastercoin** (whitepaper 2012-01; **launched 2013-08**): implemented token issuance on Bitcoin ("smart properties / user currencies");
> - **Counterparty** (**launched 2014-01-02**): token issuance + decentralized exchange + contracts for difference + native oracles.
>
> **All three predate the Ethereum mainnet (2015-07)**. Harder primary material comes from **the Ethereum Foundation's own blog** (2014-11-13): the original conception of Ethereum — "the first true seed of the Ethereum idea" — originated from a proposal Vitalik submitted to the Mastercoin team; the post also says that "if history had gone differently, we might have chosen to build on top of Bitcoin from the start".
>
> **Disposition accordingly**: "first invention" is unusable (it requires denying others' earlier implementations = unfalsifiable); "**first to scale**" is usable — Ethereum was the first to push programmable settlement to scale (ERC-20 since 2015, DeFi peaking 2020–2021), and its **share history is observable**. The label is tightened from `Originated / Pioneered` to **`Scaled First`**.
**Key qualification**: stablecoin activity on Tron/Solana **produces no ETH burn**, but it **equally produces no "monetary premium" equivalent for the corresponding chain** — the direct consequence of share loss is a reduction in Ethereum-side settlement activity and gas demand, **not** the symmetric statement that "value was captured by Tron".
`[UNKNOWN]`: the fee share of stablecoin-related transactions on Ethereum is not decomposed → **the actual loss to ETH capture from share loss cannot be quantified**.

> **【v2.0 addition ｜ P0-5】Stablecoin share must be shown in three columns: L1-only / L1+rollups / all chains**

| Definition | USD | Share of all chains | Difference vs L1-only |
|:--|--:|--:|--:|
| all-chain total (213 chains) | $313.21B | 100% | — |
| **Ethereum L1 only** | **$147.66B** | **47.14%** | baseline |
| Ethereum + Ethereum-settled rollups (**20 chains incl. Ethereum L1**) | $158.78B | **50.69%** | **+3.55pp** ($11.12B) |
| + remaining Ethereum-hosted L2s (incl. Ethereum-family sidechains) (**48 chains incl. Ethereum L1**) | $164.19B | 52.42% | +5.27pp |

> **Chain set and reproducibility (v2.0 final errata ｜ F-7)**:
> ① **the chain-set definition follows the L2BEAT primary-source classification** — `hostChain = Ethereum` ∩ `category ∈ {Optimistic Rollup, ZK Rollup, Validium, Optimium}` yields **19 Ethereum-settled rollups**; the remaining Ethereum-hosted L2s with `category = Other` number **28**; **together 47 (excluding Ethereum L1 itself)**. **Counting Ethereum L1 itself in**, the two columns total **20 chains** (=1+19) and **48 chains** (=1+19+28) respectively.
> ② neither column above **includes Robinhood Chain** — that chain only launched 2026-07-01 and is within a roughly 90-day gas subsidy period; the main text P0-2 already handles it with dual readings "with / without Robinhood", and this is kept consistent with the rest of the report. **The sensitivity including that chain is 51.06% / 52.75%** (see the recomputation script output).
> ③ **one-click recomputation**: `scripts/recompute_stablecoin_columns.py` (uses only data already on disk in this directory, no network, no new fetching; adding `--verify` runs consistency assertions against the chain list and the L2BEAT primary-source rule).
> ④ **recomputation error**: L1-only **+0.003pp**, rollup column **+0.024pp**, all-inclusive column **−0.014pp**, **maximum 0.024pp ⇒ the published values in this table are declared with a ≤0.03pp tolerance** (published values remain unchanged).

**Top5 on the rollup side**: Base $5.12B (1.64%) ｜ Arbitrum $4.30B (1.37%) ｜ OP Mainnet $0.59B (0.19%) ｜ Mantle $0.55B (0.17%) ｜ Ink $0.17B (0.06%).

> **Why three columns are necessary**: when stablecoins migrate from L1 to rollups such as Base, **the L1-only share falls while the combined share is unchanged or even rises** — the two do not measure the same thing. The "Ethereum stablecoin share 53.7% → 47.3%" of v1.5 (and v1.0–v1.4) **counted L1 only**, with L2 folded into "remainder".

> **v2.0 definition discipline (three items)**:
> ① the −6.4pp **may only be stated as** "**the stablecoin share carried by Ethereum L1** declined", and **must not** be stated as "the Ethereum ecosystem's share declined";
> ② **the current stock on the combined definition** has been added (50.69%), but **the time series on the combined definition was not obtained in v2.0** (it requires per-chain history), so **the trend direction on the combined definition is `[UNKNOWN]`** — one cannot assume that "because it migrated to L2 it actually did not decline";
> ③ the report's original conclusion (share loss = weakening input-side readings of the mechanism) **is not overturned by this**: the L1-carried share and YTD −10.7% (all chains +1.5%) remain valid readings; only the **boundary of the statement** changes.

> **Data source and definition**: DefiLlama `stablecoins.llama.fi/stablecoinchains` (snapshot 2026-10-02 saved as `raw/stablecoins_llama_20261002.json`), recomputation script **`scripts/recompute_stablecoin_columns.py`** (actually present in this directory; registered in the Audit Working Papers §H recomputation asset index). ⚠️ the difference from the main text's 47.3%/$147.08B (0.16pp / $0.58B) comes from **a different snapshot time** and changes no conclusion.


#### Resilience and physical-layer decentralization: a framework for comparing asymmetries (added in v1.5)

> **Evidence-status statement (read this first)**: this section is **a structural argument at the architectural layer** (`[INTERPRETATION]`). **Within this machine's evidence set there are no quantified readings of validator geographic distribution, ASN concentration, client diversity, or outage history for Solana / Tron** ⇒ this section **constitutes no magnitude comparison and changes no tier**. Its role is to put **the share readings back into the risk structure**.

**Observed share readings (load-bearing)**: Ethereum L1 **$147.08B (47.3%**, down from 53.7%); Tron **$93.99B (30.0%**, rising); Solana **≈$16.5B (5.3%**, rising); all chains **+1.5%** while the Ethereum side is **−10.7%**.

**Where the asymmetry lies (three structural differences)**:

1. **Physical-layer "reuse" vs physical-layer "redundancy"**: the performance advantage of high-throughput chains comes from **validators' physical reuse of high-performance data centers and a small number of network operators (ASNs)** — the higher the reuse, the lower the unit cost and **the larger the shared failure domain**. The corresponding Ethereum-side structure is **877,233 active validators, beacon-chain total balance 44,061,701 ETH (36.09%)** plus **multi-client redundancy**: the cost is an execution side that is "**expensive and unwieldy**", the benefit is **liveness that does not depend on a single physical facility or a single network operator remaining available**.
2. **The shape of tail risk differs**: the failure mode of reuse-type architectures is **correlated failure** (one facility event / one network event hitting many validators at once → cascading outage); the failure mode of redundancy-type architectures is **throughput and cost** (slow, expensive), **not everyone going offline simultaneously**. **A different shape ≠ better or worse** — this is **a choice of risk preference**, not a free lunch.
3. **What institutional trust is buying**: institutional-grade settlement is more sensitive to "**can it be shut down at a single point**" than to "how many transactions per second". Hence "application-layer traffic spilling onto cheaper chains" and "whether the standing of highest settlement finality and largest collateral pool has been lost" **are two different questions** and cannot be answered with the same set of share readings.

**Conclusion tightened (strict wording)**:
> **Application-layer traffic spilling onto cheaper rails does not constitute evidence for the proposition that Ethereum's standing as "highest settlement finality + largest collateral pool" has been lost.**
> **But the converse holds equally**: **"a more redundant physical layer" also does not constitute evidence that "ETH therefore obtains value capture"** — the report's core unresolved question (observable mechanisms cannot be redeemed into verifiable ETH economic value) **is unchanged by this comparison**.
> **Correct use**: explaining "why share loss and loss of standing are not the same proposition" ｜ **incorrect use**: citing it as an argument that "Ethereum necessarily prevails" (that statement is **unfalsifiable** and is not adopted by this report).

`[UNKNOWN]` (gap added in this section): **validator geography / ASN concentration, client diversity, historical outage duration and scope** for each chain — no primary source on this machine; **until filled, any comparison in this section can only be structural and must not be quantified**.

---

### 3. L2: Ethereum settlement vs Alternative DA vs Independent L1 {#sec-3-l2-ethereum-settlement-vs-alternative-da-vs-independent-l1}

#### Data (already on this machine)

| Item | Value | Source |
|:--|--:|:--|
| L2 user fees (all L2) | $1,634,574/day (**2026-09 monthly average**) | growthepie |
| L2 pays L1 (settlement+proof+blob) | **$2,387/day (0.146% of its fees (0.550% excluding Robinhood))** | same as above |
| — of which blob publication | $234/day | same as above |
| — of which L1 execution gas | ≈$2,153/day | same as above |
| L2 share of transactions processed | **94.6%** (988.3M/month) | growthepie/l2beat |
| blob capacity (BPO2) | target 14 / max 21; measured 6.35 blobs/block (utilization 45%) | blobscan / EIP-7607 |
| **based rollup field evidence** | **Taiko's L1 cost is 61.7% of its fees** vs OP Stack chains **<0.5%** | v1.0 T1 |
| alternative DA pricing (Celestia / EigenDA / Avail) | **`[UNKNOWN]`** — this machine's `raw/llama_chain_fees.json` contains only L2 chains (ethereum/base/arbitrum/op-mainnet/starknet/zksync-era/linea/scroll), **no DA layer at all** | confirmed by measurement this round |

#### Counterfactual decomposition

| Layer | Substitution path (observable competing implementation) | Verdict |
|:--|:--|:--|
| **DA (data availability)** | L2s can switch to alternative DA such as Celestia/EigenDA → **DA is a layer with substitutes** | **(b) share** — Ethereum obtains DA share via blob, but the share **depends on relative pricing**, and the blob price is anchored by EIP-7918 at `L1 base fee / 16` (measured ratio 0.931), **no longer determined by blob demand** |
| **Settlement and security anchor** | alternatives = independent L1 (abandoning shared security) or alt-settlement layers; **currently no scaled alternative implementation** | **(a) Scaled First + (b) share lead** — shared security + final settlement anchor; "currently no scaled substitute" is **a current state**, not "absent Ethereum it would not exist" |
| **Sequencing and fee capture** | were an L2 not to build on Ethereum but to run its own independent L1, all fees would accrue to itself | **(c) attributed to L2** — this part was never on the Ethereum side |

**Verdict**: **what Ethereum creates on L2 is "shared security and the settlement anchor" (a); it obtains a DA share (b, with pricing locked down by itself), while sequencer economics never belonged to Ethereum (c).**
**This yields the framework's only identified "non-capture" candidate conclusion for L2 today (conditional, not counted as Leakage)**:
- if some economic value "**could in theory be captured by ETH through a protocol mechanism**" — EIP-7918 already establishes a blob price floor, **proving the protocol has pricing power**;
- then "**having pricing power yet choosing to collect only 0.146% (0.550% excluding Robinhood)**" can, under a strict definition, be read as **Discretionary non-capture** (voluntary non-collection), **not** Value Leakage (because the price level at which it "could have been captured" is itself indeterminate);
- **the counterfactual opportunity cost (how much demand-based pricing could collect) is unmeasurable** → it can only be `[SCENARIO]` and **does not enter the conclusions**.

---

### 4. Collateral: ETH vs BTC vs Stablecoin vs Tokenized Treasury {#sec-4-collateral-eth-vs-btc-vs-stablecoin-vs-tokenized-treasury}

#### Data (this machine's `raw/llama_protocols_all.json` primary, 2026-10-02; **not additive**)

| Asset side | Protocols (TVL) | Side total (indicative, **not summed**) |
|:--|:--|:--|
| **ETH side** | Lido $26.76B; Aave v3 $18.36B (Ethereum chain $15.47B, borrows $10.31B); Morpho Blue $11.25B; EigenCloud $7.10B; ether.fi Stake $5.23B; Sky Lending $5.85B; Kelp $1.14B; Compound v3 $1.53B | **order of magnitude $70B+, but heavily overlapping** (stETH counted simultaneously in Lido/Aave/EigenLayer) |
| **BTC side (tokenized)** | WBTC $9.96B; Function FBTC $0.71B; Lombard LBTC $0.69B; SolvBTC $0.55B; Lorenzo enzoBTC $0.52B; Bedrock uniBTC $0.38B; tBTC $0.37B; GTBTC $0.30B; Nexus BTC $0.26B; Stacks sBTC $0.21B etc. | **≈$13–14B** (and most sits on the Bitcoin chain or cross-chain, **not Ethereum-native collateral**) |
| **Tokenized Treasury** | BlackRock BUIDL **$2.25B** (**Solana 43% > Ethereum 19.7% (post-4844 window average; current trailing 30 days 2.52%)**); Circle USYC **$2.40B** (**Ethereum only 1.7%**); all-category RWA **$4.69B / 181 protocols** | **$4.65B order of magnitude** |
| **Stablecoin (as collateral)** | supply $311.18B (all chains); **of which the share used as lending collateral is `[UNKNOWN]`** | cannot be adjudicated |

#### Counterfactual decomposition

- **The structural difference between ETH and BTC**: ETH is Ethereum's **native asset** and can be used directly for gas, staking and collateral without bridging; BTC on Ethereum usually must enter in **tokenized / wrapped form** (WBTC/LBTC/tBTC etc.), and **those wrapped versions are themselves ERC-20s on Ethereum**. **This means the Transmission Mechanism of the two differs** — and not that ETH has an "advantage" over BTC (advantage is an evaluative inference, not evidence). (`[INTERPRETATION]`) **⚠️ Qualification: hosting ≠ capture** — this activity produces no cash-flow or state-layer capture for ETH (see §6).
- **Substitution path (observable)**: the observable substitute host for BTC collateral is the Bitcoin ecosystem itself (sBTC/exSat etc.) and other chains, **an order of magnitude smaller** (as seen: most Bitcoin-chain-side protocols sit in the $0.1–1B range). **Note: this is "the currently observable substitute host", not a counterfactual inference about "what would happen absent Ethereum".**
- **Stablecoin as collateral**: this requires debt markets **denominated in ETH or stablecoins**, and those markets **run on Ethereum and its L2s** → on this point Ethereum is simultaneously host and rule provider.
- **Tokenized Treasury**: the magnitude **remains a rounding error** ($4.65B vs ETH market cap $335B), and **the leading products are largely not on Ethereum** → at this stage it cannot serve as evidence of ETH collateral demand.

**Verdict**: **at the on-chain collateral layer ETH is a mixture of "(a) Scaled First + (b) share"; there is a structural difference vs BTC (native vs tokenized/wrapped) and a magnitude difference vs Tokenized Treasury (about 15×) — the two are "differences", not "advantages", and the two have different Transmission Mechanisms.** (Relative standing is an evaluative inference, and the share denominator is missing.)
**But**: **ETH's share of lending collateral is unmeasurable** (Aave/Morpho collateral composition not retrieved) → this verdict can only stop at `Weak evidence`, **consistent with the status of Layer 3**.
`[UNKNOWN]`: ETH/LST collateral share in lending protocols; attribution of BTC-side tokenized assets by **custody chain**; stablecoin collateral share.

---

### 5. Settlement: Ethereum vs Alternative blockchain vs Traditional financial rails {#sec-5-settlement-ethereum-vs-alternative-blockchain-vs-traditional-financial-rails}

#### Data

| Layer | Available readings | Strength |
|:--|:--|:--|
| **vs alternative chains** | Ethereum stablecoin share **47.3% (−6.4pp)**; 2025 chain-level fees ranking 4th (Hyperliquid $971.67M / Solana $645.22M / Tron $579.33M / Ethereum $523.17M); leading RWA products **largely not on Ethereum** | medium-high (fees ranking has a definition caveat) |
| **vs traditional financial rails** | **`[UNKNOWN]`** — v1.0 already labeled Visa's "$7.0B/$3.5B", SWIFT's "17 banks" and the like all as **grade C (second-hand and internally inconsistent), not admissible into load-bearing conclusions**. This round **adds no** such data | none |

#### Counterfactual decomposition

- **Observable substitute hosts**: the on-chain portion of institutional settlement already has substitute implementations — Solana (BUIDL 43%), Tron (payments), or private permissioned chains; **the traditional-rails side is unmeasurable** (no primary source).
- **What Ethereum created**: **a permissionless, composable, programmable settlement layer** — a native product of Ethereum, of which the L2 ecosystem (94.6% of transactions) is an extension.
- **What Ethereum did not obtain**: **the increment in institutional settlement** — leading institutional products (BUIDL/USYC) **chose other chains**.

**Verdict**: **Ethereum is the party that first pushed the "open settlement" paradigm to scale (a. Scaled First); in the incremental scenario of "institutional settlement" it is losing share (b, reversed).**
**Key limitation**: **there is no primary data at all on the traditional financial rails side**, so "whether Ethereum is competing with traditional rails" **is not adjudicated this round** (brief §22: no strong judgment without evidence).

---

### 6. Summary of the four adjudications {#sec-6-summary-of-the-four-adjudications}

| Comparison group | (a) Scaled First | (b) Captured a share | (c) Hosted | Status label |
|:--|:--|:--|:--|:--|
| **Stablecoin** | settlement paradigm **first to scale** ✅ | share 47.3%, **direction downward** ⚠️ | reserve value (Treasury interest) ✅ | **Partially demonstrated** |
| **L2** | shared security and settlement anchor ✅ | DA share ✅ (pricing locked by EIP-7918) | sequencer economics ✅ | **Partially demonstrated** |
| **Collateral** | native collateral standing ✅ | structural **difference** vs BTC ✅ (not an "advantage") | — | **Weak evidence** (share definition missing) |
| **Settlement** | open programmable settlement ✅ | institutional settlement increment ❌ | — | **Weak evidence** (no data on traditional rails) |

#### Answer to the brief's core question

> **Did Ethereum really "create" this economic value, or did it merely obtain a share of the market from other networks / financial infrastructure?**

**The answer must be given in three layers and cannot be merged into one sentence:**

1. **Paradigm layer (programmable settlement, shared security, native collateral)**: **Ethereum is the party that first pushed these paradigms to scale (Scaled First)**. It **claims no "first invention" and asserts nothing about "absent Ethereum these paradigms would not exist"** — both are unfalsifiable (for earlier implementations see the factual correction in §2).
2. **Value layer of the hosted assets (stablecoin reserve interest, RWA asset yield)**: **not created by Ethereum** — Ethereum is only the hosting channel; this value **never enters ETH's capture mechanism**.
3. **Current increment layer (new stablecoins, new RWA, institutional settlement pilots)**: **Ethereum is losing share** — the increment clearly falls to Tron / Solana / the Bitcoin ecosystem / other chains.

**The most accurate formulation is therefore**:
> **"What Ethereum scaled first (Scaled First) is an infrastructure paradigm, not the value of the assets hosted; and that paradigm is currently being reused at lower cost by other chains (alternative DA, independent L1s, Tron payment rails). Whether Ethereum is harmed by this depends on whether paradigm reuse simultaneously brings settlement demand back — on the evidence to date, this has not yet formed a verifiable transmission."**

---

### 7. Three self-limitations of this module {#sec-7-three-self-limitations-of-this-module}

1. **Counterfactual ≠ attribution**: this module answers only "do substitutes exist, where is the share moving", and **does not answer** "what the world would be like without Ethereum".
2. **Not to be used to infer price**: any reasoning of the form "if Ethereum loses X share it should be worth Y" is **prohibited** (No Price Shortcut).
3. **Leave a blank wherever there is no data**: alternative DA pricing, lending collateral share, traditional financial rails — all three are `[UNKNOWN]` and have been listed as items to be filled in `Part Nine (monitoring dashboard)` §7.

---

## Part VII | Evidence Register {#part-vii-evidence-register}

### 0. Explicit "No Re-Search" Declaration {#sec-0-explicit-no-re-search-declaration}

| Data layer | Action this round |
|:--|:--|
| Coin Metrics (supply / issuance / burn / staking APY) | **Not re-fetched**; carried over from the v1.0 full-history landing |
| Beacon chain full validator balances (88.6 MB / 2,376,110 records) | **Not re-fetched** |
| growthepie (L2 fundamentals, 90-day window) | **Not re-fetched** |
| DefiLlama (stablecoin chain distribution / chain-level fees / protocol TVL) | **Not re-fetched** (only **re-parsed the already-landed `raw/llama_protocols_all.json`**, see N2) |
| Farside (ETF daily) | **Not re-fetched** |
| blobscan / eth_feeHistory / RPC per-block | **Not re-fetched** |
| SEC EDGAR (Coinbase 10-K/10-Q) | **Not re-fetched** |
| **Control set required by the Counterfactual module** | **Only reused the `raw/` already landed on this machine**; no new fetch was initiated |

**Conclusion: 5 new entries this round, all of them from "re-parsing the already-landed `raw/`" or "recomputing existing figures under a revised definition"; zero new external requests.**

---

### 1. New evidence (N1–N5) {#sec-1-new-evidence-n1-n5}

| # | Source | Date | Metric | Definition | Period | Original source | Our interpretation |
|:--|:--|:--|:--|:--|:--|:--|:--|
| **N1** | DefiLlama `api.llama.fi/overview/fees` landed file | Parsed this round, 2026-10-02 | Chain-level fees **coverage** | The set of chains returned by this endpoint | Instantaneous | `raw/llama_chain_fees.json` | **Contains only 8 L2 chains** (ethereum / base / arbitrum / op-mainnet / starknet / zksync-era / linea / scroll) → **contains no DA layer whatsoever (Celestia / EigenDA / Avail)**. **→ Counterfactual §III "alternative DA pricing" must be marked `[UNKNOWN]`; alternative values must not be used to fill it.** |
| **N2** | DefiLlama `api.llama.fi/protocols` landed file | Parsed this round, 2026-10-02 | Protocol TVL on the collateral / reserve side | TVL of each protocol (USD) | Instantaneous | `raw/llama_protocols_all.json` (8,459 protocols) | **First quantification of BTC-side tokenized assets**: WBTC **$9.96B**; Function FBTC $0.71B; Lombard LBTC $0.69B; SolvBTC $0.55B; Lorenzo enzoBTC $0.52B; Bedrock uniBTC $0.38B; tBTC $0.37B; GTBTC $0.30B; Nexus BTC $0.26B; Stacks sBTC $0.21B; exSat $0.18B; Lombard BTC.b $0.18B; Bitget bgBTC $0.12B → **BTC side total ≈$13–14B** (vs ETH side Lido $26.76B / Aave v3 $18.36B / Morpho $11.25B / EigenCloud $7.10B / ether.fi Stake **$5.23B** / Kelp **$1.14B** / Aave V4 $0.66B / Aave Horizon RWA $0.26B). **⚠️ Not additive**: stETH is counted simultaneously in Lido / Aave / EigenCloud |
| **N3** | [CALC] Definition split of L2 retention | 2026-10-02 | `L1 cost share` and `gross economic retention` | (L2 user fees − L1 costs paid) ÷ L2 user fees | 2026-09 | v1.0 `deliverables/CORE_DATA_TABLES.md` table 6 inputs | **L1-only definition: L1 cost share = 0.146% (0.550% after excluding Robinhood) → retention = 99.854%**; **definition including other costs ($1,424/day): retention = 99.77%**. → The two figures **are not in conflict**; they use **different denominator definitions**; **neither may be called profit margin** (CA-06) |
| **N4** | [CALC] Supply structure ratio | 2026-10-02 | Issuance ÷ burn (365d) | Annual issuance ÷ annual burn | 2025-10-02→2026-10-01 | v1.0 A2/A3/B8 | **1,016,345 ÷ 26,469 = 38.4×** (v1.0 phrased it as "40×"; the exact ratio is given here). **Use restriction**: solely a **Monetary Supply Indicator** description; **must not** be used to judge value capture (CA-03) |
| **N5** | [CALC] Staking efficiency ratio | 2026-10-02 | Beacon chain total balance ÷ effective stake | Ratio of total balance (including pending activation / exiting) to effective stake | 2026-10-02 | v1.0 B1/B6 | **44,061,701 ÷ 43.02M = 1.0242** → the two definitions differ by **2.4%**, and the direction is reasonable (total balance includes the queue). **Purpose**: to fix the explanation of why the report shows both 36.09% and 35.23% staking rates, so that they are not read as a data conflict |

---

### 2. v1.0 entries that require "relabeling" because of this round's conceptual corrections (not new evidence; a definition upgrade) {#sec-2-v1-0-entries-that-require-relabeling-because-of-this-round-s-conceptual-correc}

| v1.0 # | Original label | v1.1–v1.4 labeling requirement |
|:--|:--|:--|
| C1/C2 (L2 fees and retention) | "retention rate / gross margin" | Always use **L1 cost share / gross economic retention** instead; citations must carry "not net of servers / team / incentives" |
| C4 (L1 fees, trailing-365d) | A single year-on-year reading | Citations **must** be labeled **separately** from the quarterly year-on-year figure (−48.7%); mixing is prohibited (v1.0 already self-flagged this; this round upgrades it to mandatory) |
| D6/D7 (stablecoins) | "no transmission" | Split into **Channel A (issuer reserve, no transmission)** / **Channel B (on-chain activity, mechanism exists, magnitude to be demonstrated)** |
| D1–D5 (ETF/DAT locking) | "institutional demand" | Classify under **Institutional ETH Demand**; **not** as a core Value Capture mechanism |
| A3/A7 (burn / net supply) | "largest leakage point / dilution" | Relabel as **Monetary supply effect**; **must not** be entered into the leakage ranking |
| E1/E2 (Coinbase SEC) | External submission cross-check | Upgraded to **load-bearing corroboration for v1.1–v1.4** (official-disclosure grade, accession verified): Base activity **+7× YoY** while `Other transaction revenue` **−11%** |

---

### 3. Volume reconciliation of first-hand data on this machine (evidence of "retention", not "redo") {#sec-3-volume-reconciliation-of-first-hand-data-on-this-machine-evidence-of-retention}

| Asset | Status | Location |
|:--|:--|:--|
| Data endpoint inventory (12 available / 9 unavailable) | Carried over | `_SHARED_BRIEF.md` §3 |
| Load-bearing figure register (A1–E4, 46 entries in total) | Carried over | `deliverables/EVIDENCE_REGISTER.md` |
| Raw landings | Carried over | `raw/` (including the 88.6 MB beacon response, 3.8 MB growthepie) |
| Independently recomputable scripts | Carried over | `scripts/` (T2_fetch_cm.py, T2_analyze_supply.py, t1_blob_anchors.py, etc.) |
| Charts | Carried over | `charts/` (6 charts) |
| External submission review | Carried over | `notes/AUDIT_external_submission_v1.md` (7 hard defects / 1 mechanism read backwards / 13 internal contradictions) |

**v1.3 round**: 13 files (including gatekeeping records and change records), **zero new external requests**, **5** new register entries; after that round the deliverable form converged, within the same day, into **1 single-file self-contained document** (see "Appendix C (Version History and Revision Traces)"). **v1.4 round**: **zero new external requests, zero new data**; 1 new disconfirmation entry **(CE-9)**, 1 observational hypothesis **(L1 marginalization)**, 1 UNKNOWN roadmap item **(enterprise / institutional settlement share)**.

---

## Part VIII | Disconfirmation Register {#part-viii-disconfirmation-register}

### I. Remapping of v1.0 disconfirmations (old conclusions → v1.1–v1.4 status) {#i-remapping-of-v1-0-disconfirmations-old-conclusions-v1-1-v1-4-status}

| v1.0 # | Original registered object | v1.1–v1.4 disposition | Result |
|:--|:--|:--|:--|
| §1 | "burn = value capture" | Direction of the conclusion retained, **tier changed** | Still **Not demonstrated (as a Value Capture metric)**; but demoted to "does not constitute a sufficient condition", no longer called "invalid / reversed" |
| §2 | "staking demand = value capture" | **Tier changed** (Layer 2 security) | **Demonstrated (constitutive in nature)** (95.04% comes from issuance) |
| §4 | "institutional demand = price support" | **Causal strength changed** | "Institutional accumulation has not yet provided sufficient evidence that this demand converts into sustained economic value or price support" (**"disconfirmation" no longer used**) |
| §5 | "stablecoins transmit to ETH" | **Split into two Channels** | Channel A (issuer reserve) → Not demonstrated; Channel B (on-chain) → mechanism exists, magnitude to be demonstrated |
| §7 | "ecosystem growth → ETH capture" | **Upgraded to an eight-segment chain + five channels** | No longer a single negative conclusion; replaced by segment-by-segment status (1–3 🟢 / 4–6 🟡 / **7 ⚪️ (changed from 🔴 in v1.4)** / 8 ⚪️) |
| §3, §6, §8–§13 | MEV / L2 / competing chains / RWA / L2 business characteristics / own methodological errors / definition risk | **All remain valid** | See §II Carry-over items below |

---

### II. Carry-over items (still valid among v1.0 disconfirmations, not weakened this round) {#ii-carry-over-items-still-valid-among-v1-0-disconfirmations-not-weakened-this-ro}

| # | Disconfirmation point | Strength | Key figures |
|:--|:--|:--|:--|
| K1 | **MEV split not obtainable** | Strong (capability boundary) | Validator-side upper bound 53,049 ETH/365d (**0.043%** of market cap); no first-hand source for searcher/builder share; zero hits for `mev` in the CM catalog; relayscan DNS failure |
| K2 | **ETH held on exchanges not obtainable** | Strong (single largest uncertainty) | Cannot distinguish "net new" from "custody relocation" |
| K3 | **ETH share within lending collateral not obtainable** | Strong | DefiLlama `tokens` field measured as incomplete (sum $3M vs TVL $15.47B) |
| K4 | **Long series of blob base fee not obtainable** | Medium-high | publicnode returns 403 for 2024 blocks; CM blob metrics require credentials → the exact path of the "collapse period" cannot be quantified |
| K5 | **growthepie window capped at 90 days** | Medium-high | Readings taken for the full month of 2026-09 → L2 conclusions **have no cross-year validity** (see P0-2 definition note F-1) |
| K6 | **L2 is on a gross definition** | Medium-high | Not net of servers / team / incentives / airdrops |
| K7 | **Chain-level fees ranking mixes definitions** | Medium | Application fees of the Hyperliquid type are counted into the chain page and inflate it → the ranking is not used as strong evidence |
| K8 | **Daily burn precision has been partly falsified** | Medium | RPC per-block 2026-09-30 = **68.3626 ETH** vs identity 74.9 ETH (**−8.7%**); the gap is not fully attributed |
| K9 | **Validator entity attribution not obtainable** | Medium | 36.49% is **validator concentration**; it **cannot** be translated into entity concentration |
| K10 | **Ecosystem gross value denominator contains cross-layer double counting and sits at a different layer from L1 fees** | Medium | 2.73% / 0.93% are **magnitude ratios, not clean economic capture rates** |

---

### III. Disconfirmations against the new load-bearing judgments of v1.1–v1.5 (CE-1…CE-12, new in this register) {#iii-disconfirmations-against-the-new-load-bearing-judgments-of-v1-1-v1-5-ce-1-ce}

#### CE-1 | Against the Layer 1 status "🟡 Partially demonstrated (magnitude actively compressed, not defeated)"

- **Evidence**: L1 fees trailing-365d **−79.6%**; burn/issuance **138.7% (2022-09-15→2024-03-12 mean) → 19.7% (2024-03-13→2026-10-01 mean; ⚠️ both values are window averages of "pre/post-4844", not current values — the current period is 2.52% over the last 30 days, 2.60% over the last 365 days, 1.81% over the last 90 days**); base fee **0.12–0.15 Gwei**.
- **Supports**: L1 block gasUsed ≈**30.2M/block ≈ 100% of target (30M)**, about 50% of limit (60M) → usage **has not exceeded target capacity**. **(v2.0 correction: the earlier "84% full" definition was wrong — 36M was the old gas limit, not the target.)** Under EIP-1559, usage not exceeding target **does not constitute "price being held down by capacity"**, so this column **no longer supports** the reading that "capacity was expanded too far".
- **Contradicts**: **"usage near target + 0.12–0.15 Gwei" can equally be read as "the price users are willing to pay has collapsed"** — utilization near target does not equal healthy demand; and Ethereum ranking 4th in 2025 chain-level fees is corroboration that **demand is being diverted on the demand side**. **"Active expansion" is an institutional fact; "not defeated" is an interpretation** — the two have different evidential strength.
- **Strength**: Medium (institutional fact strong / interpretation weak).
- **Remaining uncertainty**: **Demand-side decomposition data for L1 does not exist** → cannot distinguish "capacity effect" from "demand loss". **Therefore, in formal statements, "active compression" must be listed alongside "possible demand diversion" and must not be written as a single cause.**

#### CE-2 | Against the Layer 3 status "🟠 Weak evidence"

- **Evidence**: The magnitude of ETH-side collateral protocols (Lido $26.76B / Aave v3 $18.36B / Morpho $11.25B / EigenCloud $7.10B / ether.fi $5.23B) is **about 4–5× the BTC-side tokenized assets (≈$13–14B)**; ETF+DAT locking equals 11.1% of circulating supply. (The BTC-side data are new in this round's Counterfactual, reusing the already-landed `raw/`; see "Part VI (Counterfactual)" §IV / "Part VII (Evidence Register)" N2 — **not a re-search**)
- **Supports**: The judgment that "ETH is the largest on-chain collateral" has **sufficient evidence**; by this it should be rated **Partially demonstrated**.
- **Contradicts**: ① There is no **share denominator** (ETH's proportion within lending collateral is unknown) → cannot rule out "a rising tide lifting all boats"; ② stETH is counted repeatedly across layers → magnitudes are not additive; ③ exchange holdings are unknown → cannot confirm net new.
- **Strength**: Medium.
- **Remaining uncertainty**: **This is the point in this register where our own judgment is most likely too conservative.** If the collateral composition of Aave/Morpho were obtained, it would **very likely be upgraded to Partially demonstrated**. Already listed in `Part IX (Monitoring Dashboard)` as a **P1 backfill item (zero cost)**.

#### CE-3 | Against the Layer 4 status "⚪️ Unknown" (**this Contradicts paragraph is itself the trigger for the v1.4 tier change**; previously aimed at 🔴 Not demonstrated)

- **Evidence**: Currency premium **proxy** (ETH/stablecoin market cap ratio) **2.543 → 1.778 → 1.182 → 1.077**, four points declining monotonically; Ethereum stablecoin share **53.7% → 47.3%** (**v2.0: L1-only definition**). **Note: the proxy ≠ the premium itself** (see "Part II (Final Conclusion)" §IV).
- **Supports**: The ratio is monotonic and the share is falling; the directions agree, and both are first-hand.
- **Contradicts**: **This metric carries a mechanical bias** — the denominator (stablecoin supply) is driven by USD liquidity, regulatory progress, and emerging-market payment demand, and **can keep growing while ETH is completely unchanged**, thereby **mechanically depressing the ratio**. In other words, **a falling ratio need not mean "a falling currency premium"**. Also: switching to the Ethereum on-chain definition gives **2.28** (different level, same direction), showing that the metric is sensitive to the denominator definition.
- **Strength**: Medium (the metric bias is real; but **apart from this metric, this machine has no second observable currency-premium proxy**).
- **Remaining uncertainty (v1.4 disposition)**: This Contradicts paragraph ("the numerator is the price, which conflicts with the No Price Shortcut", "apart from this metric there is no second observable proxy", "the direct-evidence metric is undefined") **constitutes the basis for the reclassification** ⇒ Layer 4 was changed from 🔴 Not demonstrated to **⚪️ Unknown**. **It is still not upgraded to 🟡/🟠**: an upgrade would require **a second independent metric** (scale of ETH-denominated economic activity / share of reserve use), both of which are `[UNKNOWN]`. **Formal statement**: the input-side readings are weakening (fact); the output side has no instrument (no determination).

#### CE-4 | Against "application-layer revenue → ETH: Not demonstrated"

- **Evidence**: OP Superchain's **2.5%/15% revenue share** already exists (flowing to the OP Collective); **Taiko's L1 costs are 61.7% of its fees** (vs OP Stack **<0.5%**).
- **Supports**: There genuinely is no **mandatory** return flow mechanism → Not demonstrated holds.
- **Contradicts**: **"Absence of a mechanism" may only be a point-in-time judgment** — if based/native rollups scale, the return flow could jump from "<0.5%" to ">60%" (Taiko has already shown technical feasibility).
- **Strength**: Medium (n=1 case).
- **Remaining uncertainty**: **Taiko's single case does not hold if it cannot be reproduced**; but if a second case appears, this status must be re-examined immediately.

#### CE-5 | Against "L2 Discretionary non-capture (the protocol has pricing power but chooses not to charge)"

- **Evidence**: EIP-7918 makes measured/reserve price = **0.931** → the protocol **does set a relative reserve price**; but the EIP text itself states there is a **multi-block lag**, and `MIN_BASE_FEE_PER_BLOB_GAS` is still 1 wei ⇒ **it is a soft lower bound, not an absolute price floor** (**v2.0 correction** of the original "does set a price floor").
- **Supports**: The protocol possesses a pricing instrument.
- **Contradicts**: **Coinbase's SEC filing provides first-hand evidence in the opposite direction** — Base stablecoin transfer volume **+7× YoY**, while `Other transaction revenue` **−11% YoY**. If L2 own revenue is contracting, the judgment that "pricing power exists" is weakened: **pricing power may be constrained by competition among L2s, not by Ethereum's willingness.** Also: EIP-7918 sets a **floor**, **not a rate**.
- **Strength**: Strong (SEC primary text).
- **Remaining uncertainty**: That Coinbase line item is on a **consolidated definition** (including Base but not limited to it) and **cannot be treated as Base's standalone P&L**.

#### CE-6 | Against the **over-interpretation risk** in "Layer 1 magnitude is small → weak capture"

- **Evidence**: blob revenue **$143–234/day** (0.026%–0.043% of L1 fees).
- **Contradicts**: Under EIP-7918, **blob revenue = a function of the L1 execution base fee (1/16)** → it is **a claim proportional to the L1 execution base fee** (coefficient < 1, **not leverage**; v2.0 correction). The current small value reflects **a low-base-fee regime**, **not the strength of the mechanism**.
- **Strength**: Strong at the mechanism level / `[SCENARIO]` at the numerical level.
- **Remaining uncertainty**: If the base fee recovers 40–160×, blob revenue rises linearly (**$6k–23k/day**). **This scenario must not enter any load-bearing conclusion**; it may only be a `[SCENARIO]`.

#### CE-7 | Against the Counterfactual module itself ("Part VI (Counterfactual)")

- **Contradicts**: ① **Counterfactuals are unobservable** — "without Ethereum" cannot be falsified; ② **the existence of substitutes ≠ substitutability** (liquidity network effects, audit/compliance inertia, bridge risk); ③ a change in share **does not equal** Ethereum being harmed (the stock is still the largest: $147.08B > Tron $93.99B).
- **Strength**: Strong (methodological level).
- **Remaining uncertainty**: Alternative DA pricing, lending collateral share, and the traditional-finance rail **all lack first-hand data** → of the 4 groups of determinations in this module, **2 can only stop at Weak evidence**.

#### CE-8 | Against "stablecoin share loss = Ethereum harmed"

- **Contradicts**: ① Ethereum **is still first in absolute stock** ($147.08B); ② **bridging out ≠ not settling on Ethereum** (some cross-chain stablecoins still re-anchor to Ethereum); ③ part of the share decline comes from **user behavior changes after Ethereum itself pushed costs down**; ④ the gas share attributable to stablecoins is `[UNKNOWN]` → **the magnitude of the loss is unquantified**.
- **Strength**: Medium.
- **Remaining uncertainty**: Net outflow vs share dilution cannot be distinguished.

#### CE-9 | Against the **systemic resonance fragility of Restaking** in Layer 2 / Layer 3 "locked utility" (new in v1.4)

> **v2.0 reinforcement ｜ Upgraded from "structural risk" to "structural risk + a case already realized within the year"**: The **KelpDAO rsETH cross-chain bridge attack** occurred at **2026-04-18 17:35:35 UTC (block 24,908,285)**, involving 116,500 rsETH ≈ **$292M**; root cause was a **1-of-1 DVN** single-point configuration, and LayerZero attributed it to **DPRK Lazarus**. **Aave's official incident report (2026-04-20)** gives bad-debt scenarios of **$123.7M–$230.1M** (the attacker deposited 89,567 rsETH = $221.39M and borrowed 82,650 WETH = $190.86M). **⇒ "the resonance fragility of restaking / cross-chain receipt assets" already has a realized case within the report year and is no longer a pure hypothesis.** However, CE-9's **disposition conclusion is unchanged** (it remains supporting disconfirmation): because the "scale → loss" mapping still has no magnitude definition, and this event occurred **before CE-9 was registered**, it does not constitute direct disconfirmation of this round's tier.

- **Evidence**: ETH-centric staking/restaking **stacks multiple layers of claims on the same asset**, and the scale has reached observable magnitude — EigenLayer **$7.10B**, ether.fi **$5.23B**, alongside Lido $26.76B, Aave v3 $18.36B, Morpho $11.25B, all belonging to the "ETH-centric" collateral system; the same batch of ETH is **counted repeatedly across layers** along the `staking → LST → LRT → AVS` chain (CE-2 has already registered the multi-layer counting of stETH).
- **Supports**: "ETH is the largest on-chain collateral" and the locked scale (**≈13.52M**, **11.1%** of circulating, **36.09%** staked) are **measurable facts**; this entry does not dispute them.
- **Contradicts (the core of this entry)**: **"More locked" and "more risk exposure" are co-sourced.** Restaking extends the **slashing risk of the same ETH from one layer to multiple layers**: ① the same batch of ETH can be **simultaneously committed to multiple AVSs** via an LRT ⇒ **correlated slashing**; ② **liquidity mismatch** — LST/LRT receipts are transferable while the underlying stake is constrained by the exit queue, so in a stress scenario the receipts de-peg from the underlying; ③ once multi-layer slashing occurs, what is damaged is **the same batch of ETH**, which **simultaneously** hits (a) collateral value, (b) ETH-denominated lending and liquidation chains, and (c) L2 security costs. **Therefore, the "locked utility" recorded by Layer 2 / Layer 3 can, in a stress scenario, turn into a "chain-liquidation channel" in reverse; and in the existing observation set this situation has been neither priced nor measured.**
- **Strength**: Medium (**the structural risk is an established mechanism, but the "scale → loss" mapping has no magnitude evidence**).
- **Remaining uncertainty**: ① The **exact multiple** of repeated counting is `[UNKNOWN]` (no aggregating source); ② the sample of actual AVS slashing events is **nearly zero** ⇒ this risk is **currently neither confirmable nor falsifiable**, and therefore **is registered only as structural fragility and must not enter any magnitude judgment or tier change**; ③ if a first-hand definition of the scale of "multiple commitments of the same ETH" is obtained (this machine has no source), this entry could be upgraded to a quantitative determination.
- **Relationship to CE-2 (must not be read as a contradiction)**: CE-2 holds that Layer 3's 🟠 may be **too conservative** (positive magnitude evidence is sufficient); this entry points out that the same body of evidence contains **an unaccounted downside risk**. **Magnitude (positive) and fragility (negative) are two sides of the same phenomenon** — their coexistence precisely shows that the "locked scale" reading **is insufficient on its own to support a tier upgrade**.

---

#### CE-10 | Against the narrative that "the business model has shifted from a platform tax to a sovereign settlement base" (new in v1.5)

- **Evidence**: The rent-decline side is realized (L1 fees **−79.6%**, burn ÷ issuance **138.7% (2022-09-15→2024-03-12 mean) → 19.7% (2024-03-13→2026-10-01 mean; ⚠️ both values are window averages of "pre/post-4844", not current values — the current period is 2.52% over the last 30 days, 2.60% over the last 365 days, 1.81% over the last 90 days**, L1 cost share **0.146% (0.550% after excluding Robinhood)**); the scale-expansion side is realized (L2 **94.6%** of transactions, blob **154.7 GB/month**).
- **Supports**: The two things occurred **in the same period**, and both can be re-measured within this report's observation window.
- **Contradicts (three)**:
  ① **"Active shift" is unobservable** — "turning into a base layer" would require proving "this is a chosen strategy", and this machine has **no first-hand governance basis that answers "whether such an intent exists"** (a nameable roadmap record is in "Appendix E", but it does not answer intent); the report already explicitly prohibits speculating about the objective function (P0-3);  
  ② **"High fees killed application-layer network effects" is a single-cause reading** — demand-side decomposition data for L1 does not exist; **the two readings "capacity effect" and "demand loss" coexist and cannot be distinguished** (CE-1); writing it as a single cause is precisely the formulation CE-1 prohibits;  
  ③ **The core predictive part of the narrative is unfalsifiable** — "wholesale revenue (base-layer fees) will eventually appear" **has no measurable reading within the current observation window** (the ETH-denominated economic activity metric is undefined).
- **Strength**: Medium (the structural framework has explanatory power, but **explanatory power ≠ evidence**).
- **Remaining uncertainty**: **Can this narrative be given a falsifiable reading?** Not at present ⇒ disposition: **the framework is retained at the `[INTERPRETATION]` level, with zero effect on the tier level**; **if** either "the scale of ETH-denominated economic activity" or "institutional settlement share" becomes defined and measurable, **then** the narrative would acquire, for the first time, the conditions for a determination (already entered into the "Part IX" UNKNOWN roadmap).

#### CE-11 | Against the claim that "resilience and physical-layer decentralization constitute an asymmetric advantage" (new in v1.5)

- **Evidence (the part for which this machine has first-hand data)**: structural readings on the Ethereum side — **877,233 active validators**, beacon chain total balance **44,061,701 ETH (36.09%)**, consolidated-account concentration **12,092 accounts holding 36.49%**, multiple client implementations.
- **Supports**: The structural judgment that Ethereum's **liveness does not depend on a single physical facility** is consistent in magnitude with its validator count / client diversity.
- **Contradicts (three)**:
  ① **The other side of the comparison has no first-hand readings on this machine** — the validator geographic distribution, ASN concentration, client diversity, and downtime history of Solana / Tron are **all `[UNKNOWN]`** ⇒ the comparison **can only remain a structural claim and must not be quantified**;  
  ② **"More redundancy ⇒ better" is not a general conclusion** — the cost of redundancy is throughput and expense, and reuse-type architectures are **objectively ahead** on the "unit cost" dimension; **this is a choice of risk preference, not a free advantage**;  
  ③ **This report has already refuted the simplification that "more nodes = lower concentration"** — the consolidated accounts **12,092 holding 36.49%** suggest that **validator entity concentration** is far higher than the node count implies (entity attribution `[UNKNOWN]`).
- **Strength**: Medium-weak (**the structural judgment holds; the comparative conclusion has no evidence on this machine**).
- **Remaining uncertainty**: **This is the entry in this round most likely to be read as "defending Ethereum"** ⇒ the main text has added a **two-way qualification** — "more redundant at the physical layer" **neither proves that its position is not being lost, nor proves that ETH attains value capture**; this entry **must not be used to support any tier**.

#### CE-12 | Against the judgment that "ordering rights will return to L1 and L1 claims will be activated" (new in v1.5)

- **Evidence**: Taiko's **L1 costs are 61.7% of its fees** (vs OP Stack **<0.5%**); Coinbase SEC first-hand: volume **+7× YoY** while revenue **−11%**.
- **Supports**: **A technical path exists** (based rollups have already implemented returning ordering to L1); **competition among L2s is indeed compressing the withholding space of centralized sequencers**.
- **Contradicts (three)**:
  ① **n=1** — Taiko's single case **does not hold if it cannot be reproduced**, and a second measurable case has not yet appeared;  
  ② **"Enterprise-grade compliance necessity" has no first-hand basis** — the regulatory path is undetermined ⇒ the **antecedent of the conditional itself is `[SCENARIO]`**;  
  ③ **"Will" cannot be written** — writing a conditional as a prediction violates the discipline of "no short-term forecasts, no conclusions about the future" (this round has rewritten it as a conditional).
- **Strength**: Medium (technical feasibility has on-site evidence; **neither economic feasibility nor timing does**).
- **Remaining uncertainty**: The **trigger observation for this entry is explicit** (a second based / native rollup case + its L1 cost share); **should one appear, paragraph 4 and Channel B must be re-examined immediately**. Until then, **no tier is changed**.

---

### IV. This report's own methodological errors (proactively traced, new in v1.1–v1.5) {#iv-this-report-s-own-methodological-errors-proactively-traced-new-in-v1-1-v1-5}

| # | Error | Nature | Disposition |
|:--|:--|:--|:--|
| E1 | **"four necessary conditions 0/4"** — the premises were themselves fabricated necessary conditions (deflation, L1 demand recovery), and a score was then synthesized | **Conceptual error + scoring error** | Deleted from the whole round; replaced by a mechanism status table. **This error has been corrected and traced.** |
| E2 | **Naming "L2 retention/gross margin 99.77%"** — the self-warning "must not be called profit margin" was not carried through the whole text | **Formulation error** | Renamed to `L1 cost share / gross economic retention`; definition split added (N3) |
| E3 | **"institutional demand is directly disconfirmed"** — violates the No Price Shortcut, conflates three layers | **Causal error** | Changed to "has not yet provided sufficient evidence of transmission"; Demand→Value→Price three layers separated |
| E4 | **"stablecoins do not transmit to ETH"** — wrote a magnitude question as an existence question | **Conceptual error** | Split into Channel A/B |
| E5 | **"only/sole" type statements ×4** — beyond observational capability | **Strength error** | All demoted (CA-12); all other "only" usages in v1.1–v1.4 have been given observation-set qualifiers (current / as available on this machine / identified) |
| E6 | **"validator count × 32" understated staked amount by 36%** | Methodological error (already self-traced in v1.0) | Carried over and retained, see K9 |
| E7 | **v1.3 internal tier inconsistency** — "Part II" §VIII trigger condition ③ was already written on the basis of "Layer 4 = ⚪️", while the four-layer table and the chain table marked 🔴 | **Consistency error** (not a judgment error) | Unified to ⚪️ in v1.4 and traced in "Appendix C". **That inconsistency was itself one of the clues for the v1.4 tier relabeling.** |
| E8 | **Three formulations in the v1.4 → v1.5 task instruction conflict with existing criteria** ("active shift" = inferring the objective function; "will" = prediction; "only" without qualifier = beyond the observation set) | **Disciplinary risk** (following them literally would roll back the P0 corrections of v1.3) | Rewritten per the existing criteria and traced: converted to the `[INTERPRETATION]` framework + conditional phrasing + **observation-set qualifiers**; see "Appendix C" v1.4 → v1.5. **This is not a content error but a level error — a C-level claim was placed in an A-level position.** |

---

### V. Distribution of conclusion confidence (re-sorted by v1.1–v1.4 status label) {#v-distribution-of-conclusion-confidence-re-sorted-by-v1-1-v1-4-status-label}

- **Demonstrated (🟢)**: the chain's segments 1–3 (activity / creation / distribution); the EIP-7918 anchoring mechanism; L2's DA pricing lower-bound mechanism; the merger of staking scale and the validator set; the Coinbase SEC corroboration of "scale decoupled from capture"
- **Partially demonstrated (🟡)**: protocol cash flow (mechanism strong, magnitude compressed); L2 settlement (mechanism thin); Staking/Security (**Layer 2 as a whole**; its security component is Demonstrated at the mechanism level (constitutive in nature)); L2 counterfactual (shared security)
- **Weak evidence (🟠)**: Collateral Demand (lacks a share definition); share competition for institutional Settlement; MEV → ETH holders (mechanism holds, magnitude does not)
- **Not demonstrated (🔴)**: application-layer revenue → ETH (no mechanism in effect)
- **Unknown (⚪️)**: ETH Economic Value (no determination this round); **Monetary Premium (moved in from 🔴 in v1.4: no valid measuring instrument)**; MEV split; exchange holdings; lending collateral share; alternative DA pricing; traditional-finance rail; DAT industry-wide scale; enterprise / institutional settlement share

**Global UNKNOWN (carried over from v1.0)**: MEV decomposition, ETH held on exchanges, ETH collateral share, historical blob price series, quantitative impact of based/native rollups, DAT industry-wide scale.

---

## Part IX | Monitoring Dashboard {#part-ix-monitoring-dashboard}

### Differences from the v1.0 Dashboard (version change record) {#differences-from-the-v1-0-dashboard-version-change-record}

| Item | v1.0 | v1.1–v1.4 | Rationale |
|:--|:--|:--|:--|
| Organizing principle | Primary metrics = "gatekeeping metrics for the four necessary conditions" | **Four groups of capture metrics A/B/C/D** | The four necessary conditions have been judged to be fabricated premises (CA-03/CA-04/CA-09) |
| `burn ÷ issuance ≥ 100%` | **Listed as the flip line for condition 3** | **Demoted to one supply-structure reading within Group A** | Task brief §20 explicitly prohibits treating it as a Value Capture Trigger |
| Default state | "holds / does not hold" | **Five-tier status labels** (Demonstrated / Partially / Weak / Not / Unknown) | Task brief §12 |
| New | — | **Group D Monetary Capture** (v1.0 had only scattered metrics) | Task brief §20 |
| **Front-screen summary (v1.4)** | — | **4 core readings placed at the top** | Brings the 4 numbers that "fit on one screen" to the front; **does not replace the observation points below** |

---

### Front-screen summary | 4 core readings (new in v1.4) {#front-screen-summary-4-core-readings-new-in-v1-4}

> **Does not replace the observation points below**; it only moves "the 4 numbers that fit on one screen" to the front. **All are taken from existing readings in Groups A / B, with zero new data**; the definitions are fully consistent with the entries below, and in case of conflict **the entries below prevail**.

1. **DA demand**: blob **6.35 blobs/block** (utilization **45%**, vs target 14); **154.7 GB/month** (growthepie September definition 39%) → **capacity has not yet been pushed to its limit**
2. **DA pricing**: measured ÷ reserve price **0.931** (range [0.741, 1.087], anchored to **1/16** of the L1 base fee); unit price **$0.003015/blob**; revenue **$143–234/day (= 0.026%–0.043% of L1 fees)** → **pricing is determined by L1 demand, not by blob demand**
3. **L2 settlement economics**: L2 → L1 **$2,387/day = 0.146% of L2 fees (0.550% after excluding Robinhood)**; gross economic retention **99.854%** (L1-only definition; 99.450% after excluding Robinhood) / **99.77%** (definition including other costs); L2 gross ÷ L1 fees **≈3.0×** → **the return flow is three orders of magnitude lower than L2's own gross retention**
4. **Supply structure (net issuance)**: 30d burn **74.5 ETH/day** (365d **26,469 ETH**); post-4844 burn ÷ issuance **19.7% (post-4844 window average; current period 2.52% over the last 30 days)**; **365d issuance ÷ burn = 38.4×**; 30d annualized net issuance rate **+0.862%** → **issuance is still the main component of net supply** (⚠️ burn is a **monetary supply indicator**, not capture strength, see A3)

> **How to read**: Together these 4 items say "**the network is expanding, the return flow is extremely thin, supply still relies on issuance**" — **they are observations, not determinations**.

---

### Group A | Protocol Capture (protocol cash flow) {#group-a-protocol-capture-protocol-cash-flow}

#### A1. L1 network-wide fees

- **What it measures**: the **price paid × usage** of L1 block space (excluding blob; for blob usage and pricing see B1 / B2)
- **Why it matters**: it is the **common upstream** of Channel A and of the blob reserve price (Channel B)
- **Confirmation**: trailing-365d year-on-year **turns positive**, and the 90-day daily-mean base fee stands at **> p90 (≈0.4615 Gwei)** [the original "> 5 Gwei for 30 consecutive days" = p100, **triggered 0 times in 90 days, repealed as v2.0 Research Review Directive #13**]
- **Disconfirmation**: year-on-year keeps falling (currently **−79.6%**); the 90-day daily-mean base fee stays ≤ **p75 (≈0.1993 Gwei; currently 0.0735 Gwei = p15.4)**
- **Sample interval**: 2026-07-05 → 2026-10-03 (about 90 days, per-block aggregation to daily mean, n=91) ｜ **periodic recalibration** (quarterly recommended)
- **Current state**: **trailing-365d $552,414/day (annualized ≈$201.6M)**, year-on-year **−79.6%**; trailing-30d $561,068/day. ⚠️ Must not be mixed with the quarterly year-on-year **−48.7%** (2026Q2 $52.47M)

- **[New in v2.0 ｜ P0-7] Dual denomination and price/quantity effect decomposition**: the year-on-year **−79.6%** is a **USD-denominated** reading; it must be presented alongside the **ETH-denominated** reading, with the price effect decomposed. Measured (`v2.0/scripts/recompute_fee_decomposition.py`):

| Reading | Prior year 2024-10-02→2025-10-01 | Latest year 2025-10-02→2026-10-01 | YoY |
|:--|--:|--:|--:|
| L1 protocol fees (ETH-denominated) | 322,798 ETH | 79,518 ETH | **−75.4%** |
| L1 protocol fees (USD-denominated) | $985.2M | $204.3M | **−79.3%** |
| Window average price (USD) | $2,982.3 | $2,514.0 | **−15.7%** |

> **Log decomposition**: Δln(USD fees) = −1.5734 = **quantity effect −1.4010 (89.0% of the decline)** + **price effect −0.1708 (10.9%)**.
> **How to read**: the **bulk of the year-on-year fee decline is a real quantity contraction** (ETH-denominated −75.4%); the price effect is only about one sixth. ⚠️ The comparison quantity is the **window average price** ($2,982.3→$2,514.0, −15.7%), **not the year-on-year spot price** — the spot definition would inflate the price effect to about −38%, which is not directly mixable with the flow definition.

### Threshold calibration method: historical percentiles (new in v2.0 | Research Review Directive #4) {#threshold-calibration-method-historical-percentiles-new-in-v2-0-research-review-}

> **Change**: from this version on, monitoring thresholds **are no longer expressed as integer cut-offs but as historical percentiles**, and **the sample length must be stated**. Integer cut-offs distort easily after a mechanism change (e.g., after Glamsterdam raises the gas limit target to 200M, every absolute threshold tied to gas must be recalibrated).

| Metric | Original threshold (integer) | New formulation (historical percentile) | Sample length | Limitation |
|:--|:--|:--|:--|:--|
| A2 base fee | > 5 Gwei | **90d daily-mean measured percentiles: p50 0.1342; p75 0.1993; p90 0.4615; p95 0.8127; max 1.2139 Gwei**. ⚠️ **The original 5 Gwei threshold = p100 (0 triggered in 90 days) ⇒ no longer valid**; **per Research Review Directive #13 it has been changed to > p90 ≈ 0.4615 Gwei** (currently **0.0735 = p15.4**) | **Sample interval 2026-07-05 → 2026-10-03 (about 90 days)**, per-block aggregation to daily mean, n=91 | The whole sample sits in **the same low-fee environment** and **cannot be treated as a "structural" percentile**; a long series back to the launch of 1559 is needed; **periodic recalibration** |
| A3 burn (30d mean) | > 500 ETH/day | **> p42.4** (post-Merge 30d rolling distribution, n=1,449; median **1,012.0**, p25 143.3, p75 2,276.0 ETH/day) | **2022-09-15 → 2026-10-01 (about 4 years)** | The series spans two institutional breaks (4844 / Fusaka), so **the percentiles are not internally homogeneous**; **periodic recalibration** (annually or after each institutional upgrade) |
| A3 burn (lower bound) | ~~< 100 ETH/day~~ | **Per Research Review Directive #12, raised to < p10 = 46.4 ETH/day** (the original lower bound of 100 ETH/day = **p20.3**, which has already been breached **20.3% of the time** since the Merge ⇒ it has lost discriminating power) | **Same as above (about 4 years)** | Recomputable series: `data/burn_percentiles.json` (CM burn series); **periodic recalibration** |
| A3 current value | — | Current 30d mean **74.5 ETH/day = p15.7** (low percentile; p25=143.3, p50=1,012.0, p75=2,276.0) | Same as above | Compared with "post-4844 mean 19.7%": **the percentile view is more intuitive than the ratio view**; **the series has been unified into the recomputable CM burn series** |
| B2 measured/reserve price | > 1.5 / < 0.8 | **Full 90d measurement: per-block p05 0.754; median 0.923; p95 1.046; 24h rolling mean range [0.797, 0.961]; median 0.913**. The original **> 1.5** was measured in only **0.06%** of blocks (= above p99.9) ⇒ the percentile formulation should be **> p99.9**; the original **< 0.8** covered **9.42%** of blocks, but under the 24h rolling definition **only 1 of 2,161 hours** ⇒ **per Research Review Directive #14, all of it has been switched to the 24h rolling mean**: **> p90 ≈ 0.9379 / < p10 ≈ 0.8895** | **Sample interval 2026-07-05 → 2026-10-03 (about 90 days)**, per-block across 645,424 blocks → **2,161 rolling hours** | The per-block ratio **oscillates at high frequency around 1** (the median continuous run below 1 is only 4 blocks ≈ 48 seconds) ⇒ per-block "sustained" thresholds are almost never triggerable; **periodic recalibration** |
| B3 / B4 L1 cost share | rising / < 0.2% | **Weighted mean 0.1448%; cross-chain median 4.38% (p50), p25 0.27%, p75 27.60%** (0.1428% / median 7.43% after the chain set was redrawn) | **Sample interval the full month of 2026-09 (30 days); source window capped at 90 days** | ⚠️ **Sample length is seriously insufficient** — **cannot distinguish a structural level from a launch-phase phenomenon**, so this group **is registered only, with no hard thresholds set**; **periodic recalibration** |
| C1 staking rate | > 45% | **To be backfilled** (no historical series on this machine) | — | Requires third-party staking history; **periodic recalibration** (once the series is in place) |
| D2 stablecoin share | > 55% / < 45% | **To be backfilled** (currently only a single-point snapshot) | **Single point (sample interval = 1 point in time)** | ⚠️ **No historical series ⇒ percentiles cannot be set**; and whether the denominator includes L2 changes the reading (P0-5); **periodic recalibration** |

> **Four disciplines**: ① Any threshold **must be cited together with its sample interval**; ② **a threshold with a sample < 1 year must not be used for "structural" judgments** (B3/B4 and D2 fall in this category); ③ a threshold change = a Dashboard version change, and the rationale and affected conclusions must be recorded; ④ **all thresholds must be recalibrated periodically** — A2/B2 quarterly, A3 annually or after each institutional upgrade, with recalibration results recorded in the version change log. This table **changes no existing tier** (the changes to the A3 lower bound and to the A2/B2 formulations are Research Review Directives #12/#13/#14 of 2026-10-03, and **constitute threshold formulation and numerical changes, not tier changes**).


#### A2. Base fee level

- **What it measures**: the **marginal clearing price** of the L1 execution layer
- **Why it matters**: under EIP-7918 it **simultaneously determines the blob relative reserve price** (`base_fee_per_gas / 16`) → one variable drives two channels
- **Confirmation**: **90-day daily-mean base fee > p90 (≈0.4615 Gwei)** [the original "> 5 Gwei for 30 consecutive days" = p100, **0 triggers in 90 days, repealed per Research Review Directive #13**] → Channels A and B rise together
- **Disconfirmation**: **90-day daily-mean base fee persistently ≤ p75 (≈0.1993 Gwei)** (currently **0.0735 Gwei = p15.4**; intraday definition **0.12–0.15 Gwei**)
- **Sample interval**: 2026-07-05 → 2026-10-03 (about 90 days, per-block aggregation to daily mean, n=91) ｜ **periodic recalibration** (quarterly recommended)
- **Current state**: **0.12–0.15 Gwei**; L1 block gasUsed ≈**30.2M/block ≈ 100% of target (30M)**, about 50% of limit (60M) → **the two readings "capacity effect" and "demand loss" coexist** (see "Part VIII (Disconfirmation Register)" CE-1; the earlier "84% full" definition has been corrected)

#### A3. Burn

- **What it measures**: the amount of **monetary supply contraction**, not capture strength
- **Why it matters**: it is a **Monetary Supply Indicator**; task brief §20 prohibits using it as a Value Capture Trigger
- **Confirmation (with respect to "a change in supply structure", not to capture)**: 30d burn back to **> p42.4 (≈500 ETH/day)** = a signal that the base fee structure is recovering
- **Disconfirmation**: **30d burn < p10 = 46.4 ETH/day** [**Research Review Directive #12**: the original lower bound of 100 ETH/day = p20.3, breached 20.3% of the time since the Merge and thus without discriminating power, so it was raised to p10]
- **Sample interval**: 2022-09-15 → 2026-10-01 (about 4 years, post-Merge 30d rolling n=1,449) ｜ **periodic recalibration** (annually or after each institutional upgrade)
- **Current state**: **30d mean 74.5 ETH/day (= p15.7, low percentile)**; 365d **26,469 ETH**; cumulative since 1559 **4,648,477 ETH**; post-4844 burn/issuance **19.7% (post-4844 window average; current period 2.52% over the last 30 days)**; 365d issuance ÷ burn = **38.4×**

#### A4. Priority fee / MEV tip

- **What it measures**: price competition over the non-base-fee portion (bidding for inclusion)
- **Why it matters**: within the observation set available on this machine, this is the **only measurable upper bound** for MEV flowing back to validators (builder payments must pass through this path)
- **Confirmation**: the tip share of validator revenue **rises**
- **Disconfirmation**: the share keeps falling
- **Current state**: **53,049 ETH/365d ≈ $143M (0.043% of market cap)**; **4.96%** of validator revenue. `[UNKNOWN]` searcher/builder share

#### A5. Validator revenue (security budget)

- **What it measures**: the total consideration paid for consensus security
- **Why it matters**: its **composition** (issuance vs usage) determines the nature of staking demand (Layer 2 determination)
- **Confirmation**: "**the issuance share of validator revenue falls below 90%**" = real usage begins to matter
- **Disconfirmation**: the share keeps rising or stays flat at 95%
- **Current state**: **1,069,394 ETH/year ≈ $2,891M** (**0.876%** of market cap, **2.43%** of staked market cap); **95.04% comes from issuance**

---

### Group B | Settlement Capture (settlement and DA) {#group-b-settlement-capture-settlement-and-da}

#### B1. Blob demand (DA usage)

- **What it measures**: L2's **actual consumption** of Ethereum data space
- **Why it matters**: it is the **quantity** of Channel B; together with the **price** in B2 it determines blob revenue
- **Confirmation**: utilization **> 80% sustained** (set by this report) → demand genuinely approaching capacity
- **Disconfirmation**: utilization persistently < 30%
- **Current state**: measured **6.35 blobs/block (utilization 45% vs target 14)**; growthepie September definition **39%**; **154.7 GB/month**

#### B2. Blob fees (DA pricing)

- **What it measures**: the unit price of DA and the degree to which it is anchored
- **Why it matters**: **EIP-7918 anchors the price to 1/16 of the L1 base fee** → pricing is no longer determined by blob demand (**v2.0 Directive #15**: here we may only say "anchored" — the evidence on the phenomenon side is sufficient, while the **causal side has not been confirmed by evidence**, see the reassessment of determination strength below)
- **Confirmation**: the **24h rolling mean of the measured/reserve price > p90 (≈0.9379)** = blob demand is genuinely picking up (forming an independent premium) [the original "sustained > 1.5" covered only 0.06% of blocks at block level, and **triggered 0 of 2,161 hours** on the 24h rolling basis ⇒ per Research Review Directive #14 it has been switched to rolling-mean percentiles]
- **Sample interval**: 2026-07-05 → 2026-10-03 (about 90 days) ｜ **periodic recalibration** (quarterly recommended)
- **Disconfirmation**: **24h rolling mean < p10 (≈0.8895)** = fully dominated by the L1 base fee [the original "sustained < 0.8" covered 9.42% at block level and only **1 of 2,161 hours** on the 24h rolling basis ⇒ per Directive #14 the definition was changed]. The original reading **0.931** (range [0.741, 1.087]) came from a sample of **only 256 blocks (≈51 minutes)**; **v2.0 has expanded it to 90 days × 645,424 blocks** (block-level median **0.9231**, 24h rolling-mean median **0.913**) — **the small-sample reading is confirmed by the full dataset** (see the next section). **⚠️ The thresholds of this group (>1.5 / <0.8) must, after the mechanism was re-understood, be expressed as percentiles bound to a time definition**: see proposals #4 / #7 / #14
- **Current state**: unit price **$0.003015/blob** (10,122,972 wei/blob-gas); revenue **$143–234/day = 0.026%–0.043% of L1 fees**; DA allocated per L2 transaction **$3.6e-6**

#### B2 supplement | EIP-7918 per-block evidence (90 days, 645,424 blocks) [new in v2.0 | Research Review Directive #7]

> **Method**: Blockscout v2 was queried per block for `base_fee_per_gas` and `excess_blob_gas`; the blob base fee was rebuilt block by block and then divided by the reserve price (`base_fee_per_gas / 16`) to obtain the per-block ratio.
> **Parameters not from memory**: the update fraction of the blob base fee was **reverse-solved and calibrated = 11,684,671 from 1,000 known blocks (blobscan `blobGasPrice` for the same blocks), hitting exactly on 1,000/1,000 blocks** (⇒ EIP-4844's 3,338,477 no longer applies in this window).
> **Coverage**: heights 25,464,382 → 26,112,381, spanning **90.35 days**; 647,932/648,000 blocks (**99.99%**). 68 numbered blocks are missing (not returned by Blockscout, 0.011%), **treated as missing and not counted on either side**.

| Window | Blocks | **Share with ratio < 1** | Median ratio | p05 | p95 | Longest continuous run below 1 |
|:--|:--|:--|:--|:--|:--|:--|
| Last 30 days | 214,996 | **81.50%** | 0.9343 | 0.7812 | 1.0522 | **253 blocks ≈ 50.6 minutes** |
| Last 90 days | 645,424 | **84.09%** | 0.9231 | 0.7536 | 1.0460 | **253 blocks ≈ 50.6 minutes** |

**Three readings**

1. **The ratio sits stably below the reserve price, and over 90 days it never crosses the line on a rolling basis**: block-level < 1 accounts for **84.09%**; **the 24h rolling mean ranges [0.797, 0.961] with a median of 0.913** — of the 2,161 rolling hours, **not a single hour has a mean > 1**, and only 1 hour is < 0.8. ⇒ "the blob price is anchored by the reserve price" is **sufficient on the phenomenon side**.
2. **The oscillation is high-frequency, not "pinned down"**: runs below 1 at block level total **87,043 runs, with a median of only 4 blocks (≈48 seconds)**; runs above 1 have a median of 1 block. ⇒ any statement of "being suppressed for a long time" **does not hold at the block scale**, and only holds **on the rolling definition**.
3. **Excess was never cleared**: within 90 days `excess_blob_gas` was still at least **166,099,710**, and **returned to zero 0 times**; the blob price returned to the 1 wei floor **0 times**. ⇒ structural excess has been suspended for a long period.

**Reassessment of determination strength: "institutional blocking" → "institutional anchoring" (approved and implemented per Research Review Directive #15)**

- **Phenomenon side: maintained and strengthened** — the sample expanded from 256 blocks to **645,424 blocks × 90 days**; the direction is unchanged and more stable.
- **Causal side: not upgraded** — reverse-inferring the excess update rule block by block: **68.72%** of blocks show `excess += blob_gas_used / 3`, **13.01%** show excess **declining** (by an integer multiple of blob), and **15.48%** show no change; yet comparing "reserve price > blob price" against the update direction block by block, **the agreement rate is only 31.36% (close to random)**. ⇒ **the observable update rule does not take the reserve price as an input**, so **one cannot assert that "the reserve price is actively suppressing price discovery"**.
- **Conclusion wording (implemented)**: "**institutional anchoring**" is retained (the price sits persistently below the reserve price, and the rolling mean never crossed the line over 90 days); **assertions of the "mechanism failure / blocking" type have been withdrawn throughout**; **the determination strength is downgraded from "mechanistic" to "phenomenological"** — that is, "the price is anchored" is an **observed phenomenon**, not a **causal conclusion** that "some mechanism is executing a block". **No tier change** (this item changes no tier).

> `[UNKNOWN]` the trigger conditions of the two branches in the excess update rule — 13.01% "declining" and 2.79% "declining with no blob usage": the data on this machine are insufficient to determine them (the specification text or node implementation would be required); **no inference is made**.

#### B3. L2 → L1 payment (return-flow scale)

- **What it measures**: the money L2 actually pays L1 for "settlement + security + DA"
- **Why it matters**: within the observation set available on this machine, this is the **only deterministic cash flow** of Channel B
- **Confirmation**: its share of L2 fees **rises from 0.146%** (currently 0.146%; 0.550% after excluding Robinhood). **v2.0 (Directive #9): the conclusions of this group must always present "weighted mean + cross-chain median/p25/p75" side by side** — weighted mean **0.1448%** ｜ **cross-chain median 4.38% ｜ p25 0.27% ｜ p75 27.60%** (median **7.43%** after excluding Polygon PoS)
- **Disconfirmation**: it stays at the 0.1% order of magnitude
- **Current state**: **$2,387/day** (of which blob $234/day, L1 execution gas ≈$2,153/day); = **0.146% of L2 fees (0.550% after excluding Robinhood)**; L2→L1 equals **0.438%** of total L1 revenue

#### B4. L2 settlement economics

- **What it measures**: **gross retention** at the L2 layer (not net profit)
- **Why it matters**: it determines "whether L2 has the ability and the willingness to pay L1 more"
- **Confirmation**: **L1 cost share rises** / a mandatory return-flow mechanism appears (based, sequencer tax, mandatory ETH denomination). **v2.0 (Directive #9)**: always give "weighted mean + median/p25/p75", **never the weighted mean alone** — currently **0.1448% (weighted) ｜ median 4.38% ｜ p25 0.27% ｜ p75 27.60%**
- **Disconfirmation**: L1 cost share persistently < 0.2%, with no governance action
- **Current state**: **L1 cost share 0.146% (0.550% after excluding Robinhood)**; **gross economic retention 99.854% (L1-only definition; 99.450% after excluding Robinhood) / 99.77% (definition including other costs)**; L2 gross ÷ L1 fees **≈3.0×**. ⚠️ **Must not be called profit margin**; Coinbase's SEC filing shows first-hand that **at the single-chain level "activity up, revenue down" is possible**

---

### L2 chain-set redefinition: by "whether it settles to Ethereum" (new in v2.0 | Research Review Directive #8) {#l2-chain-set-redefinition-by-whether-it-settles-to-ethereum-new-in-v2-0-research}

**Old definition**: all **25 chains** returned by growthepie for 2026-09 were counted in the denominator — including non-Ethereum-settling chains such as **Polygon PoS** (which L2BEAT explicitly designates as a **sidechain**, with Ethereum acting only as notary rather than judge).  
**New definition**: only **chains whose settlement layer is Ethereum L1** are counted (rollups whose state roots / proofs are submitted directly to L1).

| Definition | Chains | Σ fees (USD/day) | **L1 cost share** | Concentration, max | Cross-chain **median** | p25 | p75 |
|:--|--:|--:|--:|--:|--:|--:|--:|
| **Old** (all chains) | 25 | 1,634,574 | **0.1448%** | 83.18% | 4.38% | 0.27% | 27.60% |
| **New A** (excluding Polygon PoS) | 24 | 1,560,406 | **0.1428%** | 83.18% | **7.43%** | 0.32% | 29.07% |
| New B (excluding pending Orbit confirmation) | 22 | 1,560,326 | 0.1420% | 83.18% | 3.80% | 0.27% | 36.51% |

> **⚠️ Window definition (F-1)**: the three rows of **Σ fees** in the table above (1,634,574 / 1,560,406 / 1,560,326) are **all monthly averages for the full month of 2026-09 (30 days)**, consistent with the definition used throughout the report; they are **not** the mean of the data source's 90-day window (the measured 90-day figure under the same definition is $786,267/day, see the P0-2 block).

**How the readings change, and why**:
1. **The weighted mean barely moves** (0.1448% → 0.1428%, −0.002pp): the excluded Polygon PoS accounts for only 4.5% of fees, and **its own L1 cost share is only 0.19%**, the same order of magnitude as the whole ⇒ numerator and denominator shrink in the same direction.
2. **What actually changes is the distribution**: the cross-chain **median rises from 4.38% to 7.43% (+70%)**. This is precisely positive evidence that "a single weighted mean cannot represent a typical L2" — **weighted mean 0.14%, typical chain 7.4%, p75 29%**, three figures spanning two orders of magnitude.
3. **Concentration is unchanged (83.18%)**: the excluded chains are not the largest chain, so the concentration conclusion **is unaffected by the chain-set definition**.
4. **Plume / Gravity pending confirmation**: both are Arbitrum Orbit chains, and **no first-hand evidence on their settlement layer has been obtained**; their combined fee share is **<0.01%**, with an impact on the readings of **<0.001pp** (definition B already gives the upper bound).

> **⚠️ One existing assumption that must be corrected**: the audit file speculated that Robinhood Chain should be removed from the new chain set. **Measurement contradicts the official documentation** — Robinhood Chain's **official documentation explicitly states that it is an Arbitrum Nitro Layer-2, settling to Ethereum, using Ethereum blobs for DA** (`docs.robinhood.com/chain/`). ⇒ **It remains in the new chain set**.
>
> **A related new observation (registered in v2.0; changes no tier)**: under the terms of the **Arbitrum Expansion Program (AEP)**, Robinhood Chain pays **a portion of its net protocol revenue to the Arbitrum ecosystem**; while over the same period **Ethereum's L1 settlement cost from it is only $855/day (0.063% of its fees)**. ⇒ **For a chain that uses Ethereum as its settlement layer, the licensing fee it pays to another L1 ecosystem is far larger in magnitude than the settlement cost it pays to Ethereum.** This observation has, per **Research Review Directive #11**, been raised to a Group B observation item (see **B5** below); it **sets no threshold and affects no tier**.
>
> **Data and definitions**: growthepie `fees_paid_usd` / `costs_l1_usd` (2026-09-01→30); chain metadata from growthepie `master.json` (`chain_type`/`bucket`/`stack`/`da_layer`); settlement-layer facts from each chain's official documentation and L2BEAT (Polygon PoS is a sidechain). Recompute script `v2.0/scripts/recompute_chain_set.py`, results `v2.0/data/l2_chainset_redefinition.json`.

#### B5 (observational item, no threshold) | Settlement-layer capture vs. ecosystem license-fee capture 〔new in v2.0 | research review directive #11〕

- **What it measures**: for a chain that uses **Ethereum as its settlement layer**, the ratio of the amount of its net protocol revenue claimed by **another L1 ecosystem** to the **settlement cost** Ethereum obtains from that same chain.
- **Why it matters**: it tests whether "**settling to Ethereum**" and "**paying Ethereum**" are the same thing. If the two differ by orders of magnitude, then "settlement-layer capture" cannot be equated with "value flowing back".
- **First-hand facts (verified)**:
  1. **The AEP license terms** require Arbitrum chains **other than Arbitrum One / Nova** to pay the Arbitrum Foundation **10% of net protocol revenue** (official Arbitrum docs `docs.arbitrum.io/launch-arbitrum-chain/chain-config/costs/aep-overview`, which also link the AEP license terms PDF).
  2. **Split definition**: of that 10%, **8% flows to the ArbitrumDAO treasury and 2% to the Arbitrum Developer Guild** (official ArbitrumDAO factsheet "Robinhood Chain Mainnet Launch", 2026-07).
  3. **Billing base**: `AEP_FEES = [(l2BaseFee + l2SurplusFee + l1BaseFee + l1SurplusFee) − (l1BaseFee)] × 10%` (official Arbitrum `docs.arbitrum.foundation/calculate-aep-fees`) — **the Ethereum-side settlement cost (l1BaseFee) has already been deducted before billing**.
  4. The same factsheet also states explicitly: **Robinhood Chain settles to Ethereum and therefore falls within the scope of the AEP license** — **independent corroboration of this paper's redrawing of the chain set by "whether it settles to Ethereum" (#8)**.
- **Unverified part (kept at grade C)**: the **actual license-fee amount paid** by Robinhood Chain has not been obtained from a primary source; "$855/day (0.063%)" is **our own reading**, estimated from growthepie `costs_l1_usd` (full month of 2026-09).
- **Reading (provisional, not used for any determination)**: under the above definition, the license fee this chain pays to the Arbitrum ecosystem is **expected to be higher than** the settlement cost Ethereum obtains over the same period; **the order-of-magnitude gap cannot be settled until the actual payment amount is verified**.
- **Two disciplines**: ① **no threshold, no effect on any tier, no entry into any determination** (this item is observational); ② **must not be written as "Ethereum is having value extracted from it"** — the AEP billing base **has already deducted the settlement cost**, so the "license fee" and "L1 settlement revenue" **are not the same money and are not double-charged**; they are **two parallel claim paths**.

> **Data and definitions**: official Arbitrum documentation ×2 (AEP overview, AEP fee formula) + official ArbitrumDAO factsheet ×1; chain fees and L1 costs from growthepie (full month of 2026-09).

### Group C | Asset Capture (assets and collateral) {#group-c-asset-capture-assets-and-collateral}

#### C1. ETH staking (staking scale)

- **What it measures**: **security-collateral demand** denominated in ETH
- **Why it matters**: it reflects holding demand, and also **automatically raises issuance** (∝ √effective stake) → a two-way effect
- **Confirmation**: staking ratio **> 45%** (float materially tightening); **> 50%** requires re-estimating the yield structure
- **Disconfirmation**: staking ratio peaks and rolls over
- **Current state**: beacon chain total balance **44,061,701 ETH (36.09%)**; effective stake **43.02M (35.23%)**; active validators **877,233** (⚠️ **must no longer be multiplied by 32**); consolidated-account concentration **12,092 accounts (1.36%) hold 36.49%**; CL nominal yield **2.53%**

#### C2. ETH collateral share (collateral share)

- **What it measures**: **ETH's share of lending collateral** (vs BTC / stablecoins / RWA)
- **Why it matters**: for the observable set available on this machine, this is the **only key** that lifts Layer 3 from `Weak evidence` to `Partially demonstrated`
- **Confirmation**: once a share definition is obtained, ETH's share **rises or holds first place**
- **Disconfirmation**: ETH's share is eroded by wrapped BTC or tokenized treasury
- **Current state**: **`[UNKNOWN]`**. Side evidence: Lido $26.76B (**≈9.84M stETH = 22.5% of active stake**); tokenized BTC side ≈**$13–14B** (WBTC $9.96B etc.); Tokenized Treasury **$4.65B**. **⚠️ Must not be summed (stETH is counted at multiple layers)** (the BTC side is newly added in this round's Counterfactual, reusing already-landed `raw/`; "Part VI (Counterfactual)" §IV / "Part VII (Evidence Register)" N2)

#### C3. ETH lending (lending demand)

- **What it measures**: credit expansion collateralized by ETH/LST
- **Why it matters**: it turns staking's "single lock-up" into a "composable collateral base"
- **Confirmation**: ETH-collateralized debt on Aave/Morpho **grows and its share rises**
- **Disconfirmation**: collateral structure migrates toward stablecoins/RWA
- **Current state**: Aave v3 **$18.36B** (Ethereum chain $15.47B, borrows $10.31B); Morpho Blue **$11.25B**; Compound v3 $1.53B; Sky Lending $5.85B

#### C4. ETF / ETP

- **What it measures**: **accumulation of holdings** through regulated channels
- **Why it matters**: for the observable set available on this machine, it is the only daily primary series for **Institutional ETH Demand** (**not** a core capture mechanism)
- **Confirmation**: net inflows are **sustained** **and** C2's share improvement appears **at the same time** (otherwise it is merely custody relocation)
- **Disconfirmation**: a shift to sustained net outflows
- **Current state**: cumulative net inflow **+$13.87B (561 trading days)**; holdings **≈6.63M ETH = 5.43%** (**estimate ±3–5%**); 2026 YTD +$1.58B; net selling over the last 5 days

#### C5. Institutional holdings (DAT / treasuries)

- **What it measures**: ETH exposure on listed companies' balance sheets
- **Why it matters**: this is where **single-point reversal risk** sits — if the issuance channel closes, net buying may become net selling
- **Confirmation**: holdings grow **and** mNAV ≥ 1
- **Disconfirmation**: **mNAV < 1 = issuance channel closed → net buying turns to net selling**
- **Current state**: BitMine **6,001,302** (staked 5,067,309); SharpLink 892,127 → **DAT total 6.89M**; including ETFs (≈6.63M), **total locked ≈13.52M = 11.1% of float** (overlaps with staking, must not be summed). **mNAV `[UNKNOWN]`**

---

### Group D | Monetary Capture (money and network position) {#group-d-monetary-capture-money-and-network-position}

#### D1. ETH liquidity share

- **What it measures**: ETH's **unit-of-account position** relative to other stores of value
- **Why it matters**: the observable proxy for Layer 4
- **Confirmation**: the proxy metric **recovers**
- **Disconfirmation**: continues to decline
- **Current state**: **ETH-to-Stablecoin Market-Cap Ratio = 1.077** (2.543 → 1.778 → 1.182 → 1.077); Ethereum on-chain definition **2.28**. ⚠️ **This metric is a proxy for the monetary / network premium, not the premium itself**; and it carries mechanical bias (the denominator is driven by USD liquidity) → see "Part VIII (Disconfirmation Register)" CE-3, **a single metric is not sufficient to conclude**

#### D2. ETH settlement share

- **What it measures**: Ethereum's share of **on-chain settlement**
- **Why it matters**: share is the central observable of the counterfactual framework ("Part VI (Counterfactual)")
- **Confirmation**: share **recovers above 55%**
- **Disconfirmation**: **falls below 45%**
- **Current state**: stablecoins **47.3%** (from 53.7%); Ethereum side YTD **−10.7%**; 2025 chain-level fees ranking **#4**; leading RWA products sit mainly on **other chains**

#### D3. ETH reserve usage

- **What it measures**: the degree to which ETH is held as a **reserve/settlement asset** by institutions or protocols
- **Why it matters**: this is the precondition for Layer 4 to move from "no data" to "decidable"
- **Confirmation / Disconfirmation**: **to be set once the metric is defined** — ⚠️ **currently unfalsifiable: not included in this round's trigger execution**
- **Current state**: **`[UNKNOWN]`** (no aggregate source; the industry-wide size of DATs is also unknown)

#### D4. ETH-denominated economic activity

- **What it measures**: the scale of economic activity priced/settled in ETH
- **Why it matters**: direct evidence of the "monetary premium", not a proxy
- **Confirmation / Disconfirmation**: **to be set once the metric is defined** — ⚠️ **currently unfalsifiable: not included in this round's trigger execution**
- **Current state**: **`[UNKNOWN]`** (no source on this machine) → **this is the largest gap in Group D and in Layer 4 overall**

---

### Event-driven observations (no need to run periodically) {#event-driven-observations-no-need-to-run-periodically}

| Event | What is observed | Impact |
|:--|:--|:--|
| **Next blob parameter adjustment (BPO / Fusaka+)** | changes in target / max | **recompute all blob conclusions** (capacity ↑ → unit price ↓, but EIP-7918 preserves a floor) |
| **Second measurable case of based / native rollup** | L1 cost as a share of its fees | verify whether Taiko's **61.7%** is reproducible (currently n=1) |
| **BMNR / SBET quarterly reports** | ETH per share, mNAV, funding method | determination of a locked-holdings trend reversal (the single-point risk in C5) |
| **Coinbase 10-Q/10-K** | `Other transaction revenue` | whether "scale decoupled from capture" persists (FY2025 $252.888M → 2026Q2 $47.413M, −11%) |
| **Aave / Morpho collateral-composition API** | ETH/LST collateral share | **closes C2 (P1, zero cost) → may upgrade Layer 3 status** |
| **Major L1 upgrade (Glamsterdam)** | changes in the execution-layer fee mechanism; **official gas limit target 200M** (test reference 150M) ⇒ the gas dimension of current Group A thresholds must be recalibrated | rerun Group A + B2 threshold recalibration |
| **Major stablecoin migration (issuer/regulation)** | Ethereum share | D2 |
| **L1 marginalization signals (new observational hypothesis in v1.4)** | ① L1 fees trailing-365d YoY **negative for two consecutive quarters**; ② base fee persistently **≤ 0.2 Gwei**; ③ L1 block **utilization declining relative to target** (currently gasUsed ≈30.2M ÷ target 30M ≈ 100%) | **observe only, no determination** — all three deteriorating in the same direction = the **observable form** of "L1 degrading from a value-settlement layer to a DA/security layer"; its qualitative part is unfalsifiable and **must not be written into conclusions** |
| **Corporate/institutional settlement disclosure (new in v1.4)** | enterprise-level breakdowns in stablecoin issuers' transparency reports, RWA platform disclosures, on-chain settlement sections of listed companies' 10-Ks | closes D3; **define the definition before pulling data**; before the definition exists, **no input to tier determinations** |

> **On the definition of "L1 marginalization" (new in v1.4, must be read together with the readings)**: "marginalization" is a **retrospective narrative**, and its **qualitative part is unfalsifiable under the No Price Shortcut rule** (neither price nor qualitative judgment can serve as evidence). **Only the three readings in the table above are falsifiable.** Therefore this report **only registers readings and directions and draws no conclusion on "whether L1 is being marginalized"**; once all three readings deteriorate in the same direction and **persist for ≥ 2 quarters**, they will be submitted as a **trigger condition** for the next round of re-review, **with no tier changed this round**.

---

### Presenting evidence in two columns: Fundamental / Market-implied (new in v2.0 | research review directive #1) {#presenting-evidence-in-two-columns-fundamental-market-implied-new-in-v2-0-resear}

> **Nature: a pure presentation layer. This table changes no tier, rewrites no criterion, and alters no weight.** It has exactly one purpose — to let the reader see at a glance **which readings are price-independent (fundamental) and which are price-derived (market-implied)**, so that the error of "using a price-derived quantity as capture evidence" is not repeated (No Price Shortcut).

| Reading | Category | Why |
|:--|:--|:--|
| L1 protocol fees (ETH-denominated) | **Fundamental** | amount of ETH on-chain, independent of price |
| Burn / issuance (ETH-denominated) | **Fundamental** | same as above |
| **Burn ÷ issuance (ratio)** | **Fundamental** | numerator and denominator are both ETH; the price term cancels |
| blob usage / utilization / transaction count | **Fundamental** | physical quantities |
| L1 cost share, gross economic retention | **Fundamental** | numerator and denominator are both USD and from the same source; price approximately cancels |
| staking ratio, validator count, locked ETH | **Fundamental** | on-chain ETH definition |
| Ethereum stablecoin **share** | **Fundamental** | a ratio, insensitive to price; but **whether the denominator includes L2s changes the reading** (see P0-5) |
| L1 protocol fees / L2 fees / ecosystem fee pool (**USD-denominated**) | **Market-implied** | contains a price factor; **YoY comparisons must be decomposed into price/quantity** (see P0-7) |
| ETH price, market cap | **Market-implied** | purely price-derived |
| ETH-to-Stablecoin Market-Cap Ratio | **Market-implied** | the numerator is a price-derived quantity ⇒ **not a measurement of the premium** (the direct reason Layer 4 is ⚪️) |
| 2.73% order-of-magnitude ratio, gross ÷ L1 fees 3.0× | **Market-implied (same-source ratio)** | contains price on both sides; **usable only as an order-of-magnitude ratio** |

> **Three usage disciplines**: ① **market-implied readings must not on their own carry a "capture holds / does not hold" determination** (they may be used for magnitude, direction, decomposition); ② any **YoY** reference to a market-implied figure must be accompanied by the fundamental definition or its decomposition (already landed in P0-7); ③ this table **does not change** a single word of the "No Price Shortcut" rule text.

### `[UNKNOWN]` gap-closing roadmap (by cost-effectiveness) {#unknown-gap-closing-roadmap-by-cost-effectiveness}

| Priority | Gap | How to close it | Cost | Impact |
|:--|:--|:--|:--|:--|
| **P0** | Exchange ETH balances | Glassnode / CryptoQuant subscription | paid | determines whether "locked = net new or custody relocation" (Layer 3) |
| **P0** | Scale of ETH-denominated economic activity | requires defining the metric first | research | the only direct evidence identified so far for Layer 4 (D4) |
| **P1** | ETH/LST collateral share on lending protocols | Aave `api.aave.com/data/markets` + Morpho `blue-api.morpho.org/graphql` | **zero cost** | **may upgrade Layer 3 status** (C2) |
| **P1** | MEV generated / extracted / paid split | Dune (relay data queryable on the free tier) | key required | removes the largest global UNKNOWN |
| **P1** | Historical blob base fee series (2024-03→2025-12) | archive RPC (`eth.merkle.io` / `rpc.ankr.com/eth`) for anchor points | **zero cost** | fills in the precise path of the "collapse period" |
| **P2** | Alternative DA pricing (Celestia / EigenDA / Avail) | each DA layer's official/on-chain data | low | fills Counterfactual §III (currently `[UNKNOWN]`) |
| **P2** | Standalone blob burn amount | fix the `fake_exponential(1, excessBlobGas, 3338477)` bug (returns an absurd value of 1.88e18) | **zero cost** | explains the 8.7% daily-frequency error |
| **P2** | Stablecoin-related gas share | requires defining the definition first | research | quantifies the loss from D2 share attrition |
| **P3** | Entity attribution of validators | third-party label libraries | paid | converts 36.49% from "validator concentration" into "entity concentration" |
| **P3** | Industry-wide DAT size / mNAV | scrape SEC 13F / announcements company by company | manual | closes C5 |
| **P3** | Traditional-finance rail comparison (settlement) | requires reliable primary sources (the v1.0 Visa/SWIFT data is grade C and must not be used) | high | fills Counterfactual §V |
| **P1** | **Corporate/institutional settlement share (new in v1.4)** | **define the definition first** (numerator = the portion of enterprise-level settlement value settled via Ethereum; denominator = total enterprise-level on-chain settlement) → then pull data: enterprise-level breakdowns in stablecoin issuers' transparency reports, RWA platform disclosures, on-chain settlement sections of listed companies' 10-Ks (SEC EDGAR **readable on this machine**) | research (**zero procurement cost**) | closes D3 / Counterfactual §V; **before the definition exists, no input to any tier determination** |

---

### Re-check procedure (four items per round) {#re-check-procedure-four-items-per-round}

1. **Run groups A/B/C/D** and compare item by item with this period's values; **if any item triggers confirmation or disconfirmation → rerun the corresponding layer determination** and flag it in the report.
2. **Any change exceeding 20% must be root-caused** (distinguishing "a real change" from "a definition change").
3. **Check the event-driven items**; begin incremental analysis as soon as one occurs.
4. **Update the `[UNKNOWN]` list** and record the data sources newly obtained this round.

**Prohibited actions (observation-period procedure)**

- ❌ Do not adjust any threshold, parameter, or textual-level conclusion judgment because of a single-day/single-week reading;
- ❌ Do not treat Dashboard thresholds as trading signals;
- ❌ Do not fill load-bearing figures with second-hand aggregates;
- ❌ **Do not treat `Burn / Issuance > 100%` as a Value Capture Trigger** (task brief §20);
- ❌ Do not add automated tasks and do not publish externally.

**Version discipline**: changes to thresholds/indicators/grouping = **a Dashboard version change**, and the reason and affected historical conclusions must be recorded. Pure data updates do not change the version number.

---

### One-command re-check script (inherited from v1.0, unchanged) {#one-command-re-check-script-inherited-from-v1-0-unchanged}

```bash
cd ~/ZKLabs/research/eth-value-capture-2026-10

python3 scripts/T2_fetch_cm.py && python3 scripts/T2_analyze_supply.py   # supply/issuance/burn
python3 scripts/T2_derive_stake_history.py                                # back out staking scale
python3 scripts/T2_hist_and_trailing.py                                   # run-rate
python3 scripts/report_charts.py                                          # charts
```

**Known limitations**: the free CM tier returns **403** for `SplyBurntNtv / FeePrioTotNtv / StakingAPYNominal / FeeMevRevPct` → burn still goes through identity back-derivation; MEV / staking APY still have no source.

---

## Appendix A | v1.0 research status inventory {#appendix-a-v1-0-research-status-inventory}

### I. Facts already demonstrated (Demonstrated) {#i-facts-already-demonstrated-demonstrated}

Criterion: primary source independently recomputable ∧ ≥2 sources cross-checked, or direct on-chain measurement.

| # | Fact | Value | Evidence strength |
|:--|:--|:--|:--|
| F1 | Phased structure of ETH supply (four architectural periods) | annualized net issuance **+10.41% (pre-1559) → +2.57% (1559→Merge) → −0.238% (Merge→4844) → +0.652% (post-4844)** | strong (CM daily full history + ultrasound cross-check; cumulative burn deviation **+0.18%**) |
| F2 | Current run-rate | 30d (2026-09-02→10-01): issuance 88,729 / burn 2,236 / **net +86,493 → annualized +1,052,326 (+0.862%)**; daily issuance **2,986.6 ETH/day** | strong |
| F3 | Cumulative burn | **4,648,477 ETH** since 1559; 2,024,192 since Merge; **net increase +1,572,685 ETH** since Merge | strong (identity + ultrasound) |
| F4 | Staking scale (primary full on-chain set) | beacon chain total balance **44,061,701 ETH** (sum over 2,376,110 per-validator records) = **36.09%** of supply; active validators **877,233**; ultrasound definition 43,740,862 (0.73% difference) | strong (maximum spread across the three definitions 2.4%) |
| F5 | Validator consolidation (Pectra / EIP-7251) | **12,092 accounts (1.36%) hold 16,081,362 ETH = 36.49% of the beacon chain**; "validator count × 32" **understates staked amount by roughly 36%** | strong (bucketing of 2,376,110 primary balance records) |
| F6 | Validator revenue structure (365d) | consensus issuance **1,016,345 ETH (95.04%)** + execution-layer tips (including all MEV tips) **53,049 ETH (4.96%)** = security budget **1,069,394 ETH ≈ $2,891M = 0.876% of market cap** | strong (primary issuance + on-chain balance cross-verification) |
| F7 | EIP-7918 anchors the blob price to the L1 execution base fee | reserve = `base_fee_per_gas / 16` (EIP text: `BLOB_BASE_COST=2^13`, `GAS_PER_BLOB=2^17`); 256-block measurement: measured/reserve price **mean 0.931, median 0.928, range [0.741, 1.087]** | strong (direct on-chain measurement + EIP text) |
| F8 | Current state of blob economics | parameters **target 14 / max 21 (BPO2)**; measured **6.35 blobs/block (45% utilization)**; unit price **$0.003015/blob**; blob revenue **$143–234/day = 0.026%–0.043% of total L1 network fees** | strong |
| F9 | L2 value distribution (2026-09) | user fees **$1,634,574/day (2026-09 monthly average)** → paid to L1 **$2,387/day (0.146% (0.550% excluding Robinhood))** + other costs $1,424/day → retained **$1,630,763/day** | strong (growthepie primary + two-source check against DefiLlama's L1 side at 0.12%) |
| F10 | Concentration of L2 fees | Robinhood Chain **$1,359,679/day = 83.2% of all L2s**; Base $157,859 (9.7%); the two chains **92.8%**; 2026-09 MoM **+296%**, of which 83% came from a single chain | strong (but **the reading is a 2026-09 monthly average and the growthepie source has only a 90-day window**; and that window coincides exactly with the chain's launch plus subsidy period ⇒ **observation within the window**, not a stable fact. See the P0-2 dedicated block) |
| F11 | Stablecoin chain distribution and flows | all chains **$311.18B**; Ethereum L1 **$147.08B (47.3%, 2026 YTD −10.7%)**; Tron $93.99B (30.0%); Solana ≈$16.5B (5.3%); all chains over the same period **+1.5%** | strong (DefiLlama daily series) |
| F12 | The monetary-premium ratio weakens monotonically | ETH market cap ÷ all-chain stablecoins: **2.543 (2024-07) → 1.778 (2025-10) → 1.182 (2026-01) → 1.077 (2026-10)** | strong (using the Ethereum on-chain definition, 2.28, same direction) |
| F13 | L1 fee level and direction | trailing-365d **$552,414/day (annualized ≈$201.6M)**, YoY **−79.6%**; 2026Q2 quarter $52.47M (YoY −48.7%) | strong (CM back-derivation + DefiLlama, two sources, 0.12% difference) |
| F14 | Listed-company-level evidence of "scale decoupled from capture" | Coinbase SEC primary source: `Other transaction revenue` (definition *primarily comprises Base sequencer revenue*) FY2025 **$252.888M (+20%)** → 2026Q2 **$47,413 thousand (YoY −11%)**; over the same period Base stablecoin transfer volume **+7× YoY** | strong (SEC text; accession number verified) |
| F15 | Locked holdings on balance sheets | ETFs **≈6.63M ETH (5.43%, estimate ±3–5%)** + BitMine **6,001,302** (staked 5,067,309) + SharpLink 892,127 = **≈13.52M = 11.1% of float** | medium-high (ETF figure is an estimate; SBET is second-hand) |
| F16 | Chain-level fees competitive landscape (2025) | Hyperliquid $971.67M(1) / Solana $645.22M(2) / Tron $579.33M(3) / **Ethereum $523.17M(4)** | medium (definition caveat: including app fees on chain pages biases the figure upward) |
| F17 | Daily-frequency precision of the burn has been partially falsified | block-by-block RPC measurement of the 2026-09-30 base fee burn: **68.3626 ETH** vs 74.9 ETH from identity back-derivation, **8.7% lower** | strong (we proactively falsified our own method) |

**Four primary findings added in v1.0** (Core Data Tables, Table 13): ① validator consolidation 36.49%; ② EIP-7918 measured ratio 0.931; ③ concentration of L2 fees (Robinhood 83%/90-day window); ④ scale decoupled from capture (Base stablecoin volume +7× while revenue −11%).

---

### II. Facts partially demonstrated (Partially demonstrated) {#ii-facts-partially-demonstrated-partially-demonstrated}

| # | Claim | Part demonstrated | Part not demonstrated |
|:--|:--|:--|:--|
| P1 | "Institutional/balance-sheet demand forms long-term ETH demand" | locked holdings and staking ratio are measurable from primary sources (13.52M / 36.09%) | **net new versus custody relocation is inseparable** (exchange ETH balances `[UNKNOWN]`); and price over the same period was YoY −36.9% |
| P2 | "L2 growth weakens ETH value capture" | retention rate and the L1 take are measurable (0.146% (0.550% excluding Robinhood)) | "monetization capacity keeps falling" is **institutionally anchored by the EIP-7918 reserve price** (**#15: wording changed from "closed off" to "anchored", determination strength = phenomenal**); and the growthepie window caps at 90 days → no cross-year validity |
| P3 | "Ethereum has been beaten by competing chains" | stablecoin share −6.4pp, chain-level fees rank #4 | cannot distinguish **proactive scaling** from **demand being driven away** (no demand-side decomposition for L1) |
| P4 | "MEV returns to ETH holders" | mechanism holds: MEV-Boost payments must pass through the priority fee → fee recipient; settled in ETH terms | **the MEV generated / extracted / paid split is entirely unavailable** (no primary source for searcher/builder shares) |
| P5 | "RWA / institutional settlement has not transmitted to ETH" | magnitudes from primary sources (RWA $4.69B vs ETH market cap $335B); BUIDL 43% on Solana > 19.7% (post-4844 window average; latest 30 days 2.52%) Ethereum | DefiLlama's RWA taxonomy has not been verified; the chain choices of institutional settlement pilots have not been systematically mapped |
| P6 | "Application-layer revenue flows back to ETH zero" | there is indeed no mandatory flow-back mechanism at the protocol layer | an OP Superchain 2.5%/15% split **does exist** (flowing to the OP Collective, not to ETH); based/native rollup has only Taiko as a single live case |
| P7 | "blob changed the L2 business model" | capacity 4.7×, DA cost $3.6e-6/tx are measurable | the long-run price path lacks a 2024-03→2025-12 series (publicnode 403 / CM requires credentials) |

---

### III. Hypotheses not yet demonstrated (Not demonstrated) {#iii-hypotheses-not-yet-demonstrated-not-demonstrated}

| # | Hypothesis | Why it is not yet demonstrated |
|:--|:--|:--|
| A1 | Non-cash-flow forms of value capture (settlement / security / collateral / liquidity / monetary) can form a **sufficiently strong, sustainable, observable ETH economic premium** | the mechanism exists but **has never been measured for realization**; the monetary premium **has no usable valid measurement tool** (v1.4: the only proxy is price-derived); the input-side reading (stablecoin share) is weakening |
| A2 | L2 growth → ETH demand | there is only a "potential" path (settlement/DA); not one mandatory transmission is in force |
| A3 | The driver of staking growth is **net new holding demand** | yield 4.85%→2.53% while staking ratio 9.73%→35.23% → "not yield-driven" **holds**, but "compliance/custody/LST liquidity" is an inference, and motives are unobservable |
| A4 | based / native rollup can move L2 gross margin back to L1 | the only live evidence is Taiko's L1 cost at 61.7% of fees (vs OP Stack <0.5%); **not reproducible means not established** |
| A5 | Stablecoin on-chain activity → sufficiently large ETH value capture | the Ethereum-side stock is **declining in absolute terms**; and the fee share of stablecoin-related transactions has not been split out |

---

### IV. Inferences in the research (Inference, not Fact) {#iv-inferences-in-the-research-inference-not-fact}

| # | Inference | Depends on | Risk |
|:--|:--|:--|:--|
| I1 | "Staking demand is holding demand, not yield demand" | the inverse observation of yield versus staked amount | only proves "not yield-driven", does not prove "net new holding" |
| I2 | "ETH's capture center of gravity is shifting from the fee side to the holding side" | the 4844 phase change (an institutional fact) + rising staking/locked holdings | tightened in v1.3 to three layers: **"tilt in mechanism composition" demonstrated; "value-capture migration" is interpretation; "realization" not demonstrated** |
| I3 | "The decline in fees was actively caused by Ethereum itself" | 4844/Fusaka/BPO1/BPO2/EIP-7918 were all active decisions | "active" is an institutional fact; "not taken away" is interpretation |
| I4 | "MEV upper bound = total fees − burn" | MEV-Boost payments must pass through the priority fee | the precision of that bound depends on the already partially falsified 8.7% daily-frequency error |
| I5 | "The rise in the lock-up ratio may only be custody relocation" | competing explanation | exchange balances `[UNKNOWN]`, **neither direction has been falsified** |
| I6 | "Over-scaling rather than demand being driven away" | base fee 0.12–0.15 Gwei + L1 block utilization ≈100% of target (**v2.0 correction**: the earlier "84% full" treated the old gas limit as the target) | no demand-side decomposition data |

---

### V. Definitional problems in the research (root causes that must be audited this round) {#v-definitional-problems-in-the-research-root-causes-that-must-be-audited-this-ro}

> This section is the **root-cause list** for v1.1–v1.4. `Part III (Criteria and Concept Audit)` addresses each item.

| # | Definitional problem | Where it appears in v1.0 |
|:--|:--|:--|
| D-1 | **Value Capture was narrowed to protocol cash flow / fee / burn** | the six-part chain [3]–[6] all use "fees/revenue/burn" as the definition; the conclusion "mechanism 1 = holding demand" was written as a contrast to "not fees" |
| D-2 | **Fabricated "necessary conditions"**: writing "deflation" and "L1 execution demand recovery" as indispensable prerequisites | main report §"four conditions" ③, framework criterion 5 ①③ |
| D-3 | **The usage of Value Leakage presupposes "everything due must be collected"** | the main report's "largest value leakage" ranking lists application layer $521.6M/month and L2 gross margin $48.92M/month as leaks |
| D-4 | **The naming of 99.77% is close to profit margin** | the main report and conclusions uniformly call it "retention rate / gross margin", and write "gross margin ÷ fees" in the risk section |
| D-5 | **Mixed definitions**: quarterly YoY (−48.7%) and daily-frequency trailing-365d YoY (−79.6%) | main report §appendix definitions table item 8 (already flagged internally in v1.0, but the body still uses both in many places) |
| D-6 | **Stablecoin logic kneads issuer economics and on-chain economics into one sentence** | conclusion sentence 6 "stablecoins have not transmitted to ETH"; disconfirmation register §5 "the transmission chain breaks at step 1" |
| D-7 | **Institutional demand conflates the three layers Demand / Value / Price** | main report §"institutional balance-sheet demand = price support directly disproven"; conclusion table "❌ verified invalid/inverse" |
| D-8 | **Arbitrary scoring 0/4** | main report "0 of the current four conditions hold"; conclusions §VII; framework criterion 5 |
| D-9 | **Proliferation of absolute words**: "the only one strengthening", "the only live evidence", "the only structural hole", "verified invalid/inverse" | main report mechanism ranking, conclusions §II, §IV |
| D-10 | **Coexisting single-point price definitions** ($2,703.60 / $2,734.24 / $2,744.16) | already registered in disconfirmation register §13 |
| D-11 | **"Transmission" and "capture" not layered**: reading "Ethereum has a settlement role" directly as "ETH captures" | six-part chain [4] segment design (requires an "observable settlement path") — direction correct but not carried through the whole text |

---

### VI. Load-bearing conclusions to revise this round {#vi-load-bearing-conclusions-to-revise-this-round}

| # | v1.0 load-bearing conclusion | Disposition in v1.1–v1.4 |
|:--|:--|:--|
| R1 | "Four necessary conditions, **0** currently hold" | **Deleted.** Replaced with `Value Capture Transmission Status` (five-grade label); no scoring is established |
| R2 | "burn = value capture" was "verified invalid/inverse" | conclusion direction retained, **wording changed**: burn is a **Monetary Supply Indicator**, not a Value Capture Indicator (§5) |
| R3 | "staking yield = ETH return" was overturned | component conclusion retained (95.04% from issuance), **level changed**: it belongs to Layer 2 Security/Settlement and **constitutes a determinant property** (dilution transfer vs. external value acquisition) |
| R4 | "stablecoins have not transmitted to ETH" | **split into two Channels**: issuer reserve economics (no direct transmission) vs on-chain activity (transmission mechanism exists, magnitude to be demonstrated); writing "no transmission" is prohibited |
| R5 | "institutional balance-sheet demand = price support **directly disproven**" | **causal strength changed**: *Institutional accumulation does not by itself demonstrate sufficient price support or economic value capture*; Price ≠ Value Capture; Demand→Value→Price separated into three layers |
| R6 | "L2 retention 99.77% (gross margin/retention rate)" | **strictly defined and renamed**: = **gross economic retention** of `L2 user fees − L1 settlement cost` (L1 cost share 0.146% (0.550% excluding Robinhood)); **must not be called profit margin**, and must not imply L2 net profitability |
| R7 | "L1 execution demand must recover structurally" | **changed**: *L1 execution demand is one major value-capture channel, not a necessary condition for all forms of ETH value capture*; Channels A–E established |
| R8 | "net supply must return to neutral or deflationary" | **deleted**. *Net deflation is NOT a necessary condition*; a Demand-Supply Absorption Framework is established |
| R9 | "verified / verified invalid-inverse / unverifiable" three-way table | **changed to five-grade status labels** (Demonstrated / Partially / Weak / Not / Unknown) |
| R10 | "[the only mechanism strengthening]" "[the only live evidence]" "the only 'structural hole'" | **all downgraded** to "strongest / most worth tracking under current evidence"; the absoluteness of "only" is removed |
| R11 | "Ethereum holds on the fee side, does not yet hold on the holding side; the bridge between the two is broken" | **retained as the accurate form of the structural migration**; tightened further in v1.3: **tilt in mechanism composition demonstrated; value-capture migration is interpretation; realization not demonstrated** (L5→L6 segment) |
| R12 | "$0.027 to the protocol / $0.0093 burned" (33:1 leakage ratio) | figures retained, **renamed and downgraded**: `gross economic retention ratio`, flagged with the caveat that the denominator stacks across layers, **read as an order of magnitude**; and **must not** be called leakage |

---

### VII. Parts of v1.0 that must not be changed (to prevent mistaken edits this round) {#vii-parts-of-v1-0-that-must-not-be-changed-to-prevent-mistaken-edits-this-round}

1. **All F1–F17 figures** (primary and recomputable, and F17 has already self-falsified the daily-frequency precision);
2. **The five methodological red lines**: Fees ≠ Revenue ｜ TVL ≠ Economic Value ｜ Burn ≠ Value Capture ｜ Ecosystem ≠ Token ｜ Usage ≠ ETH Demand;
3. **The self-documentation of our own error in disconfirmation register §12** (×32 understated staked amount by 36%) — this is an asset, not a defect;
4. **The UNKNOWN list and the gap-closing roadmap** ("Part IX (Monitoring Dashboard)" §VII `[UNKNOWN]` gap-closing roadmap);
5. **The conclusions' disciplines of "not taking sides" and "not re-tuning parameters for short-term readings"**;
6. **AUDIT's review conclusions on external submissions** (7 hard errors, 1 mechanism read backwards) — figures from external drafts must never enter load-bearing conclusions under any circumstances.

---

## Appendix B | Drafting discipline and task premises {#appendix-b-drafting-discipline-and-task-premises}

### 0. Task discipline for this round (hard constraints, fixed in writing per research review instructions of 2026-10-02) {#sec-0-task-discipline-for-this-round-hard-constraints-fixed-in-writing-per-research-}

> **No tearing down and rebuilding.** The most valuable asset of v1.0 is not the numbers but the **mechanism determinations nailed down by primary evidence**. Searching everything again would not be better; it would only contaminate what is already nailed down by changing sources or time points.

This round is therefore **zero re-search + concept rebuild + transmission-chain layering**:

1. **Retain** all of v1.0's load-bearing evidence (no changed numbers, no swapped sources, no rerunning of completed collection);
2. **Correct** the three places Concept / Causality / Conclusion (§2 concept audit, recorded item by item);
3. **The "first landing and evidence archiving" of newly added empirical data is permitted only in `Part VI (Counterfactual)`** (the comparison frame whose absence was a structural gap in the previous version) — **v1.3 wording correction: what is restricted is "source uniqueness", not citation**. Reuse already-landed primary sources by preference; **new entries are registered uniformly in `Part VII (Evidence Register)` (N1–N5)**. Where other files cite that comparison frame, it must appear as a **cross-reference with attribution** (marked "Part VI (Counterfactual)" §IV / "Part VII (Evidence Register)" N2) and **does not constitute an independent evidence source**;
4. **`06_EVIDENCE_REGISTER_v1.3` registers only genuinely new evidence**; existing entries must not be duplicated for the sake of "updating" (§21 Deliverable 6 explicitly requires this).


### 2. Research discipline for this round (task brief §22) {#sec-2-research-discipline-for-this-round-task-brief-22-note-source-jumps-from-0-to-2}

| Discipline | Meaning |
|:--|:--|
| Evidence First | conclusions start from evidence |
| No Evidence, No Strong Claim | no evidence, no strong judgment |
| **No Conceptual Overreach** | data supporting A **cannot** automatically imply B unless an explicit Transmission Mechanism exists |
| **No Narrative Substitution** | "ETH is the native asset" is **not** a reason that Ethereum growth accrues to ETH |
| **No Price Shortcut** | price **cannot alone prove or disprove** value capture |
| **No Revenue Shortcut** | protocol revenue **cannot alone prove or disprove** value capture |
| **No Deflation Shortcut** | burn/issuance **cannot alone prove or disprove** value capture |
| **No Ecosystem Shortcut** | ecosystem activity **cannot alone prove or disprove** value capture |

### 3. Three expression disciplines for this round {#sec-3-three-expression-disciplines-for-this-round}

1. **Status-label system (replacing scoring)**: only `Demonstrated` / `Partially demonstrated` / `Weak evidence` / `Not demonstrated` / `Unknown` may be used.
   **Prohibited**: `0/4`, `1/4`, `Score`, `Bull/Bear score` (task brief §12).
2. **Transmission-chain status symbols** (task brief §23): 🟢 Demonstrated｜🟡 Partially Demonstrated｜🟠 Weak Evidence｜🔴 Not Demonstrated｜⚪️ Unknown.
3. **Downgrade table for strong conclusion words** (task brief §16): "must" / "only" / "directly prove" / "directly disprove" / "none whatsoever" / "inevitably" / "certainly" / "the only mechanism" / "greatest risk" / "0/4" are reviewed item by item, and those with insufficient evidence are downgraded to "supported by current evidence" / "partially supported" / "not yet demonstrated" / "no sufficient evidence yet" / "to be observed".

### 4. Conclusion discipline (the definition ruled by research review, still in force this round) {#sec-4-conclusion-discipline-the-definition-ruled-by-research-review-still-in-force-t}

- A determination is **bound to** "the current observation window + evidence set + threshold bar" and **does not constitute a judgment about future developments**; write "**as of current evidence, no verifiable X has formed yet**", not "X does not hold".
- Ratios borrowed across markets must be flagged with a caveat (called an `indicative spread`, and must not be written as a net profit margin).
- Poor data-source quality counts only as **data-infrastructure weakness**, not as evidence of market failure.
- Our own errors are retracted with documentation and reported proactively.

### 5. What this round does not do {#sec-5-what-this-round-does-not-do}

- ❌ Do not redo completed collection (results from CM / growthepie / DefiLlama / Farside / beacon node / blobscan are all carried over);
- ❌ Do not set ETH price targets and do not make trading recommendations;
- ❌ Do not retain `0/4`-style scoring;
- ❌ Do not adjust v1.0's frozen thresholds because of short-term readings (if a threshold changes, it goes through the Dashboard version-change record);
- ❌ Do not add automated tasks and do not publish externally (external publication requires separate confirmation).

### 6. Version lineage and version discipline {#sec-6-version-lineage-and-version-discipline}

| Version | Location | Status | Notes |
|:--|:--|:--|:--|
| v1.0 | topic root directory | **frozen** (read-only baseline) | first round of research: main report + 7 Deliverables + T1/T2/T3 working papers + `raw/` |
| v1.1 | `../v1.1/` | **frozen** (read-only) | Conceptual Audit + Value Transmission Framework Upgrade: zero re-search, concept rebuild, transmission-chain layering |
| v1.2 | `../v1.2/` | **frozen** (read-only) | full inheritance from v1.1 + **the 2×2 capture matrix promoted to a first-class framework component** |
| v1.3 | `../v1.3/` | **frozen** (read-only) | full inheritance from v1.2 + **Final Logic Audit logical tightening** (mechanism existence ≠ value capture has occurred; migration split into five propositions; no inference about the objective function; 2.73% downgraded to an order-of-magnitude ratio; Counterfactual four grades; monetary premium switched to a proxy definition); **tier conclusions unchanged**. After that round's delivery, it was consolidated the same day into 1 self-contained document per the "single-file-first" requirement |
| v1.4 | `../v1.4/` | **frozen** (read-only) | full inheritance from v1.3 + **① Layer 4 tier re-labeled 🔴→⚪️ (tier-level, decided by research review)**; **② new disconfirmation CE-9 (Restaking systemic resonance fragility)**; **③ first-screen summary (4 items) + the "L1 marginalization" observational hypothesis + corporate settlement share added to the UNKNOWN roadmap**. **Zero new data collection**; conclusions changed in only one tier, Layer 4 |
| v1.5 | `../v1.5/` | **superseded by v2.0** (previously labeled "final-draft candidate") | full inheritance from v1.4 + **four conceptual elevations**: ① the explanatory framework "platform tax → sovereign settlement substrate" (§01 / §04); ② an exposition of Layer 4's **composability premium** mechanism (**tier remains ⚪️**); ③ a comparative framework for the **asymmetry between resilience and physical-layer decentralization** (Part VI); ④ **sequencer rent sustainability** and the conditional clause on the return of ordering rights (Part V). Plus disconfirmations **CE-10／11／12**, four terminology items, E8 documentation. **Zero new data, zero tier changes, criteria unchanged** |
| **v2.0** | **this directory** | **current final** (frozen with research review approval 2026-10-03) | full inheritance from v1.5 + **all 7 audit P0 items landed** + **disposition of research review directives #1–#15**; **zero tier changes** (the A3 floor and the A2/B2 thresholds are **wording/value changes**, and "closed off→anchored" is a **determination-strength wording change**); **deliverables: 1 external version + 1 audit working paper (2 files in total)**. For the detailed narrative see "Audit Working Paper" §A/§B |

**Version discipline**: any change to a **criterion / classification / label definition** = **a framework version change**, and must be recorded in `Part III (Criteria and Concept Audit)` and `Appendix C (Version Lineage and Revision Log)`.
**The full differences, basis and impact assessment of the four changes v1.1 → v1.2, v1.2 → v1.3, v1.3 → v1.4, v1.4 → v1.5** are in `Appendix C (Version Lineage and Revision Log)`.

---

## Appendix C | Version History and Revision Trail {#appendix-c-version-history-and-revision-trail}

### v1.5 → v2.0 (UTC 2026-10-03) | Audit landing + directive disposition + errata {#v1-5-v2-0-utc-2026-10-03-audit-landing-directive-disposition-errata}

**Content**: Audit **all 7 P0 items fully landed** (P0-1 four-window ｜ P0-2 L2 dual readings ｜ P0-3 blob soft lower bound ｜ P0-4 gas/target definition ｜ P0-5 stablecoin three-column ｜ P0-6 Appendix E events ｜ P0-7 dual-denomination decomposition) + **disposition of research review directives #1–#15** (#1 two-column presentation layer ｜ #3 Layer 4 self-imposed limit ｜ #4 thresholds changed to quantiles ｜ #7 90-day block-by-block evidence ｜ #8 chain-set re-drawing ｜ #9 weighted mean + quantile ｜ #11 B5 observation item ｜ #12 A3 lower bound ｜ #13 A2 threshold ｜ #14 B2 time definition ｜ #15 blocking→anchoring ｜ #5 split external version + working papers).  
**Level**: **zero status-tier changes**; the A3 lower bound and the A2/B2 thresholds are **wording and value changes**; "blocking→anchoring" is a **change in the wording of judgment strength** (mechanistic → phenomenological).  
**Errata (this round)**: ① the B2 rolling hour count is **unified to 2,161** from the mixed use of 2,161 / 2,170 (= the 90-day window subset, the same source as the block-level table), and p10 is accordingly corrected from 0.8892 to **0.8895**; ② the status of v1.5 in the appendix version table is changed from "current (final-draft candidate)" to "superseded by v2.0", and a v2.0 row is added.  
**Detailed narrative**: **the version history, the item-by-item disposition, the load-bearing figure register, the fact verification, and the self-audit corrections are all moved into the Audit Working Papers §A/§B/§C/§D** (research review directive #5).

### Patch-level unification | In-report time definition changed from "Beijing time" to "always UTC" | 2026-10-03 09:16 UTC {#patch-level-unification-in-report-time-definition-changed-from-beijing-time-to-a}

**Trigger**: the research review pointed out that phrasings such as the document header's "single-file version produced: Beijing 2026-10-03 ｜ v1.4 content increment finalized: Beijing 2026-10-03" do not conform to the definition, and required that **all times in the report document follow UTC**.

**Scope of change**: the status block at the head of the document (baseline date / data cutoff / finalization time), the version signatures in the body, **all version entries and dates in Appendix C**, and the time-definition clause in Appendix D4 — **19 places in total**.

**Honesty check on the date conversion (important)**: this round **does not "change only the label without doing the conversion"** — every date that was changed is traced back item by item to the actual time point involved, with the following results:

| Original label (Beijing time) | Actual time range (traced back) | After conversion (UTC) | Did the date shift |
|:--|:--|:--|:--|
| Beijing 2026-10-02 (v1.1→v1.2, v1.2→v1.3, "Part 2" signature) | From Beijing 12:52 (same day) | **2026-10-02** | **No** |
| Beijing 2026-10-03 ($521.6M source correction, 13→1 structural change, v1.3→v1.4, v1.4→v1.5) | Beijing 16:31 → 17:16 | **2026-10-03** | **No** |

**That is: after conversion, all 19 dates remain unchanged** (a date can shift by one day only if the event falls in the Beijing 00:00–08:00 range, and none of this report's entries falls in that range).

**⚠️ Reminder for subsequent citers (already written into D4)**: **v1.4 and earlier versions are labeled in Beijing time**; when citing their dates, note that the two **may differ by 1 day**.

**Level**: **patch level, no version-number increase** — a change in definition labeling, with no change to numbers / criteria / status tiers (the same handling as the $521.6M source correction).

**ZK Labs ｜ Jinwu Qiankun No.2 ｜ 2026-10-03 (UTC)**

---

### v1.4 → v1.5 (UTC 2026-10-03) | Conceptual elevation (originally labeled "final-draft candidate" → **superseded by v2.0**) {#v1-4-v1-5-utc-2026-10-03-conceptual-elevation-originally-labeled-final-draft-can}

**Trigger**: the research review issued a special-topic revision directive — the theme is unchanged (**"Where is value created, and how much of it accrues to ETH"**) — requiring **conceptual elevation and textual refinement** on four items: **① the qualitative change in the business model (platform tax → sovereign settlement base), ② the Layer 4 composability premium, ③ the asymmetry in physical-layer resilience against external competition, ④ the sequencer rent game**; it also explicitly stated three prohibitions: **strictly no overturning load-bearing figures, strictly no re-searching external data, strictly no rewriting the architecture**.

**Zero-change declaration (nature of this round)**:
- **0 status-tier changes**: Paragraphs 1–3 🟢 / Paragraphs 4–5 🟡 / Paragraph 6 🟠 / Paragraphs 7–8 ⚪️ **all untouched**; **Layer 4 remains ⚪️ Unknown**;
- **0 load-bearing figure changes**: all citations come from evidence already archived in v1.0 (`raw/`, `notes/T1|T2|T3`), with **zero new external requests**;
- **0 criteria changes**: the five-tier labeling scheme, the four Transmission questions, No Price Shortcut, and Article 4 of the judgment principles are **all retained**;
- **All new content falls in the interpretive layer**: explicitly labeled as `[INTERPRETATION]` / `[SCENARIO]` / `[UNKNOWN]`, and **enters no status-tier judgment input**.

**Line-level change description (five body locations + four supporting places)**:

| # | Location | Change | Nature |
|:--|:--|:--|:--|
| 1 | "Part 1" §01 (after the Value Creation judgment) | Adds "The qualitative change in the business model: from platform toll to sovereign settlement base" — a two-model comparison table (revenue object / pricing philosophy / unit rent / source of network effects / corresponding reading in this report) + three boundaries | `[INTERPRETATION]` framework |
| 2 | "Part 1" §04 (after the trade-off conclusion) | Adds "04b What this trade-off means for the business model" — **the asymmetric observational signature = unit rent falls first, wholesale revenue not yet observed** | `[INTERPRETATION]` framework |
| 3 | "Part 4" §4 (after the Layer 4 detail section) | Adds a mechanism exposition of the "**composability premium**" — fragmentation pain point → candidate atomic-interoperability mechanism → unified adjudication court → **native collateral demand hypothesis**; also explains **why it has no dashboard** | Mechanism hypothesis (**status tier unchanged ⚪️**) |
| 4 | "Part 6" §2 (after the stablecoin counterfactual) | Adds "resilience versus physical-layer decentralization asymmetry" — physical reuse vs. physical redundancy, the form of tail risk, the object of institutional trust; **two-sided qualification** | Structural claim (no local quantitative reading) |
| 5 | "Part 5" §4 (after the trade-off conclusion) | Adds "04c The sustainability of sequencer rent" — three-layer tightening + **conditional phrasing** (strictly forbidden to write as a forecast) | Conditional judgment + `[SCENARIO]` antecedent |
| 6 | "Part 8" §3 | Adds counter-evidence **CE-10 / CE-11 / CE-12** | Counter-evidence registration |
| 7 | "Part 8" §4 | Adds **E8** (trail of how this round handled three phrasings that conflict with existing criteria) | Self-audit trail |
| 8 | "Appendix D" D4 | Adds five terms: platform tax / sovereign settlement base, sovereign collateral, composability premium, sequencing rights, **the boundary between the interpretive layer and the judgment layer** | Terminology conventions |
| 9 | "Appendix B" | v1.4 turned frozen, v1.5 row added; version discipline changed to "four changes" | Version discipline |

**The three "hold-back" phrasings (the most important disciplinary act of this round)**:
1. **"Active shift" → not writable**: inferring the objective function violates v1.3 P0-3. The body text is rewritten as **observed architectural trade-off**, and the question of "whether it is a conscious strategy" is explicitly left to governance documents / the roadmap.
2. **"Sequencing rights will return to L1" → rewritten as a conditional**: **"will" is a forecast**, violating "contains no short-term forecasts, draws no conclusions about the future"; it has been changed to "**if** X **and** Y, **then** Z has decidable conditions", with the **antecedent itself labeled `[SCENARIO]`**.
3. **"ETH is the only asset without counterparty risk" → observational-set qualification added**: the original statement exceeded observational capability (the same problem as CA-12 / E5); it has been changed to "**within the set of crypto assets identified in this report**, ETH is the only asset that serves as collateral in native form and has no issuing entity and no counterparty", **immediately followed by "this is a property-attribute judgment, not a value capture judgment"**.

**Two other factual tightenings**: ① **"50+ heterogeneous L2s" has no local first-hand source** → replaced with this report's definition "**26 chains within growthepie's 90-day window**"; ② **"validators in the millions" → replaced with the load-bearing readings** **877,233 active validators / 44,061,701 ETH staked (36.09%)** (**×32 forbidden**, see K9/C1).

**Verification**: `zk_style_lint --kind report` → **error=0 warning=0 style=0**; zero table breaks; all load-bearing figures in place; **status-tier intersection scan: 0 residue**.

**ZK Labs ｜ Jinwu Qiankun No.2 ｜ 2026-10-03 (UTC)**

---

### v1.3 → v1.4 (UTC 2026-10-03) | Layer 4 status re-labeling + three content increments {#v1-3-v1-4-utc-2026-10-03-layer-4-status-re-labeling-three-content-increments}

**Basis**: the research review approved the v1.4 content increments on 2026-10-03 (UTC). This round has **zero new data collection**; all changes trace back to the raw evidence set already saved in v1.0 (`raw/`, `notes/T1|T2|T3`, `scripts/`).

#### 1. Status-tier-level change: Layer 4 "Monetary / Network Premium" 🔴 Not demonstrated → ⚪️ Unknown

**Original status tier**: 🔴 **Not demonstrated** (v1.3 and earlier; the original reason being "only one observable proxy, and it points in the opposite direction").

**Grounds for the change (all three hold simultaneously)**:

1. **The only available proxy for this layer is price-derived** — the **numerator of the ETH/stablecoin market-cap ratio is ETH market cap (= price)**, and the four-point series 2.543 → 1.778 → 1.182 → 1.077 is isomorphic to the ETH price path. **Using it to measure the premium = taking a detour through price to serve as evidence**, which directly conflicts with the report-wide criterion **No Price Shortcut** (price may not serve as evidence).
2. **Direct evidence for this layer is zero** — the only direct evidence, "the scale of ETH-denominated economic activity", **does not even have an indicator definition** (see "Part 9" D4) ⇒ the report has **no valid measurement instrument whatsoever**.
3. **No negative judgment without an instrument** — absent a measurable instrument, **"Not demonstrated" is itself a negative conclusion that cannot be supported by evidence**, contradicting this report's consistent definition (we want "as of current evidence, a verifiable X has not yet formed", not "X does not hold").

**Retained real readings (must not be discarded along with the status tier)**: Ethereum stablecoin share **53.7% → 47.3% (−6.4pp)**; Ethereum side YTD **−10.7%** (all chains **+1.5%**). **This is a non-price-derived reading of network position, and its direction is negative** — but it measures **the input side of the mechanism** (⚠️ **v2.0 definition qualification**: this −6.4pp is on an **Ethereum L1-only definition**; under the combined definition the current figure is 50.69%, see the P0-5 special block) (network / unit-of-account position), **not the output side (the premium) itself**. **Conclusion wording: input-side readings are weakening (fact); the output side has no instrument (no judgment).**

**Associated self-consistency fix**: v1.3 contained one internal inconsistency — "Part 2" §8 trigger condition ③ already said "**Layer 4 moves from ⚪️ to 🟡**" (treating Layer 4 as ⚪️), while the four-layer table and the chain table labeled it 🔴. This round unifies it as ⚪️.

**Blast radius (35 places synchronized)**: head-of-document executive summary §00 item 4 ｜ "Part 1" §03 four-layer table, §11 evidence matrix, §12 demonstrated / not demonstrated, §13 S1 scenario ｜ "Part 2" §1 judgment table and four-layer summary table, §1 chain-segment status code block, §2 segment-by-segment labeling, §4 proposition table item ⑤ and the judgment sentence, §4 compression table and one-sentence version, §5 five-tier distribution, §8 closing status ｜ "Part 3" §1 judgment principles (new Article 4), §2 item-by-item conceptual audit comparison table, chain segment 7, breakpoint location, strict-wording conclusion ｜ "Part 4" Layer 4 detail section (Current Status and Transmission Mechanism), five-channel table row E, 2×2 footnote, §6 trade-off ｜ "Part 7" evidence total reconciliation ｜ "Part 8" §1 v1.0 remapping table, CE-3, §3 heading, §5 confidence distribution ｜ "Appendix A" A1 ｜ "Appendix B" version table, version discipline ｜ "Appendix D" D4 terminology conventions.

**Counter-evidence remapping**: **CE-3 changes from "the strongest self-objection against 🔴" to "supporting counter-evidence for ⚪️ and the trigger condition for this status change"** (the Contradicts section of the original CE-3 is the main basis for the change); **CE-9 is added** (Restaking systemic resonance fragility).

**Nature of change**: **a conclusion status-tier change = framework level**, raised from v1.3 to **v1.4** per version discipline (not patch level).

#### 2. Content increments (other than Layer 4, no other status tier is changed)

1. **New counter-evidence CE-9 ｜ Restaking systemic resonance fragility** ("Part 8" §3) — registers "increased locked stake" and "increased risk exposure" as **same-origin**; three structural risks: multi-layer double counting, correlated slashing, liquidity mismatch; because **the "scale → loss" mapping has no order-of-magnitude evidence**, **only structural fragility is registered, and no magnitude judgment is written in**.
2. **Three additions to "Part 9"** — ① **first-screen summary (4 core readings placed at the top)**: DA demand / DA pricing / L2 settlement economics / supply structure (net issuance), **all taken from existing Group A and Group B readings, with zero new data, and not replacing the original observation points**; ② **the "L1 marginalization" observation hypothesis** — **observe only, do not judge** (its qualitative part is not falsifiable under No Price Shortcut; only the three falsifiable readings enter the event-driven observation table); ③ **enterprise / institutional settlement share added to the UNKNOWN roadmap** — **no local source**, **define the definition first, then take data**, and **before the definition is defined it enters no status-tier judgment input**.
3. **Two items explicitly not written in (trail kept)** — ① counterfactual-type **consequence sentences** (e.g., "the narrative of a million validators' decentralization collapses", not falsifiable); ② the **qualitative judgment** of "L1 marginalization". Both are observation registrations only.

#### 3. Verification and boundaries

- **Zero new data**: this round **re-took no load-bearing figure**;
- **Zero number changes**: apart from the status-tier label (🔴→⚪️, synchronized in 35 places), all load-bearing figures, definitions, and criteria are unchanged;
- **Disallowed phrasings**: new entries in this round **contain no** `0/4`, `1/4`, `Score`, `Bull/Bear score`; they contain no price targets, trading recommendations, or short-term forecasts.

**ZK Labs ｜ Jinwu Qiankun No.2 ｜ 2026-10-03 (UTC)**

---

### Structural change | 13 split versions → 1 single-file self-contained version | 2026-10-03 (UTC) {#structural-change-13-split-versions-1-single-file-self-contained-version-2026-10}

**Basis**: research review format directive of 2026-10-03 — did not like a report assembled from many files; "it would be best if one standalone research report document could solve the problem".

**Change**: the delivery form of this special topic's v1.3 changed from **13 split files** (`00_`–`11_` + README) to **1 single-file self-contained report** (this file). The original 13 files are **folded in verbatim** to this file's body and appendices; the original split version is archived byte-for-byte at `../_archive/v1.3_13files/`, and the original delivery zip is archived at `../_archive/ETH_Value_Capture_v1.3_13files.zip`. The folding map is in **Appendix D**.

**The only 3 deletions (all pure pointer paragraphs or duplicate paragraphs, all with replacement locations)**:
1. **The files' file-level meta-information lines** (H1 title, file-level "version / baseline date / status" lines) — now carried uniformly by this file's head-of-document status block;
2. **Main report §14 Monitoring Dashboard** — the original text was a pointer paragraph pointing to the dashboard; re-pointed to "Part 9 (Monitoring Dashboard)";
3. **Main report §15 Final Conclusion** — duplicates "Part 2 (Final Conclusion)" and is superseded by the latter; an annotation has been added in the file.

**Content verification (mechanical, not self-reported)**:
- **Load-bearing figure reconciliation**: 43 items compared item by item; single-file count = 13-file merged count − 3 deliberately deleted lines + new head-of-document status block; **every difference has been located to a specific line, with zero unexplained discrepancies**;
- **Line-by-line multiset reconciliation**: apart from heading-level downgrades and cross-reference rewrites, **no content lines lost**;
- **Table integrity**: all table blocks in the document have **zero breaks**;
- **Style self-check**: `zk_style_lint --kind report` → **error=0 warning=0 style=0**;
- **Cross-references**: old filenames remaining in the body: **0** (only the mapping table in Appendix D retains the original filenames by design).

**Conclusion**: **0 content changes, 0 number changes, 0 criteria changes, 0 status-label changes** — this is only a **delivery-form change** and does not constitute a version-number change.

**ZK Labs ｜ Jinwu Qiankun No.2 ｜ 2026-10-03 (UTC)**


### v1.2 → v1.3 (UTC 2026-10-02) | Final Logic Audit {#v1-2-v1-3-utc-2026-10-02-final-logic-audit}

**Change type**: **logic tightening + naming correction** (no change to criteria definitions, no change to status tiers)  
**Basis**: research review, 2026-10-02, review point nineteen — "v1.3 — Final Logic Audit, fix only the 6 P0s"  
**Upstream predecessor**: `../v1.2/` (frozen, read-only)

#### 1. What changed

| # | Change | Location | Nature |
|:--|:--|:--|:--|
| P0-1 | "The four channels **genuinely capture value**" → "four **transmission mechanisms** exist; mechanism existence ≠ incremental ETH economic value already produced"; Security split into three layers | "Part 2 (Final Conclusion)" §4, "Part 1 (Main Report)" §conclusion | Causal discipline |
| P0-2 | Migration changed from 3 lines to **five independent propositions** (including "capture migration is interpretation" and "realization not demonstrated"); the summary sentence changes from "migration happened" to "the mechanism composition is tilting; value capture migration not demonstrated" | "Part 2 (Final Conclusion)" §3, "Part 1 (Main Report)" abstract, "Appendix A (v1.0 Research State Inventory)" I2/R11, "Part 4 (Transmission Framework)" §3 | Observation / interpretation separation |
| P0-3 | "A. Maximizing Protocol Rent is **falsified**" → **Observed Economic Design**: state only the observed trade-off, **do not infer the objective function**; delete "rent paid in exchange for the economic network" | "Part 5 (Value Distribution Matrix)" §, "Part 1 (Main Report)" §03 | No speculation about design intent |
| P0-4 | "Protocol captures 2.73%" → "L1 protocol fees ÷ reported ecosystem gross-value proxy ≈ 2.73%, **an order-of-magnitude ratio, not a capture rate**" (10 places document-wide) | "Part 1 (Main Report)" / "Part 4 (Transmission Framework)" / "Part 5 (Value Distribution Matrix)" / "Part 8 (Counter-Evidence Register)" / "Part 2 (Final Conclusion)" | Definition level |
| P0-5 | Counterfactual (a) **Created** ("without Ethereum it would not exist") **abolished**, replaced by three tiers **Scaled First**, Captured a Share, Hosted | "Part 6 (Counterfactual)" full text, "Part 1 (Main Report)" § | Remove unfalsifiable counterfactuals |
| **P0-5′** | **Self-audit second correction**: the first draft followed the directive and wrote `Originated / Pioneered`, which **is still not falsifiable** (colored coins 2012–13 / Mastercoin 2013-08 / Counterparty 2014-01 all predate the Ethereum mainnet 2015-07; an Ethereum Foundation post of 2014-11-13 itself states that the concept originated in a proposal submitted to Mastercoin) → the label is tightened again to **`Scaled First` (first to scale)**, and the "earliest verifiable implementation" phrasing is withdrawn | "Part 6 (Counterfactual)" §2 + fact-correction block, "Part 1 (Main Report)" § | **Correcting a factual error introduced by the assistant itself** |
| P0-6 | "Segments 6→7 **transformation failed**" → "**Transmission not demonstrated**" | "Part 2 (Final Conclusion)" / "Part 4 (Transmission Framework)" / "Part 1 (Main Report)" | Failure ≠ not verified |
| Supp-1 | "ETH has a structural **advantage** over BTC" → structural **difference** (different Transmission Mechanism) | "Part 6 (Counterfactual)" / "Part 1 (Main Report)" | Remove evaluative inference |
| Supp-2 | "monetary premium 1.077" → **ETH-to-Stablecoin Market-Cap Ratio** (a **proxy** for the premium, not the premium itself) | "Part 1 (Main Report)" / "Part 3 (Criteria and Conceptual Audit)" / "Part 4 (Transmission Framework)" / "Part 8 (Counter-Evidence Register)" / "Part 9 (Monitoring Dashboard)" / "Part 2 (Final Conclusion)" | Indicator naming |
| Supp-3 | Adds an **eight-layer compression table** (what we know / what we do not know) | "Part 2 (Final Conclusion)" §4 | Framework summary |
| Supp-4 | README data discipline changed to "**new data has a single source of origin archived in "Part 6 (Counterfactual)"; other files may cite it but must state the source**" | "Appendix B (Compilation Discipline)" §0 | Audit principle |
| Supp-5 | QA record adds two sections: v1.2 Framework Delta QA and v1.3 Final Logic Audit QA | "Appendix C (Version History and Revision Trail)" §6/§7 | Audit chain completeness |
| Supp-6 | Version number v1.2 → v1.3; version history table, file titles, and cross-references synchronized | whole directory | Version identification |

#### 2. What did not change (key)

**Status tiers are uniformly unchanged.** Therefore the following conclusions remain valid as-is in v1.3:

- Four layers: Layer 1 Partially demonstrated ｜ Layer 2 Demonstrated (composition determines nature) ｜ Layer 3 Weak evidence ｜ Layer 4 Not demonstrated;
- Eight-segment chain: segments 1–3 🟢, segments 4–5 🟡, segment 6 🟠, segment 7 🔴, segment 8 ⚪️;
- All load-bearing figures (**zero re-takes**), the "Part 5 (Value Distribution Matrix)" value distribution table, "Part 7 (Evidence Register)" N1–N5, "Part 8 (Counter-Evidence Register)" CE-1…CE-8, and K1…K10.

**Why only tighten the wording and not touch the tiers**: the 6 P0 fixes address the **inferential leap from "the mechanism exists" to "value capture has occurred"**, and **the indicator naming and the order-of-magnitude-ratio definition** — both are **wording-strength** issues, not evidence-judgment issues. After tightening, the **evidential basis of every tier conclusion is unchanged**, so re-running the judgment is neither necessary nor appropriate.

#### 3. Guidance for subsequent citers

- Citing **judgment conclusions**: use v1.3 (tiers identical to v1.2, but the wording is more stable).
- Citing **version history**: v1.0 (root directory, frozen) → v1.1 (`../v1.1/`, frozen) → v1.2 (`../v1.2/`, frozen) → v1.3 (this directory, current). [**This line is a verbatim trail from the v1.3 round**; **the current version is v2.0**]
- Citing the **summary**: use the **eight-layer compression table** in "Part 2 (Final Conclusion)" §4 — it is the preferred condensation for this special topic.
- Any subsequent **criteria / classification / label definition** change is still appended, per version discipline, in `Part 3 (Criteria and Conceptual Audit)` and in this file.

---

### v1.1 → v1.2 (UTC 2026-10-02) | The 2×2 capture matrix elevated to a first-class framework component {#v1-1-v1-2-utc-2026-10-02-the-2-2-capture-matrix-elevated-to-a-first-class-framew}


**Change date**: 2026-10-02 (UTC)  
**Change type**: **framework version change**, not revision level  
**Basis**: research review ruling on 2026-10-02 — "if you regard the newly added 2×2 matrix as a framework-level addition, it should go to v1.2; do it"  
**Upstream predecessor**: `../v1.1/` (frozen, read-only)

---

### 1. What changed {#sec-1-what-changed}

| # | Change | Location | Nature |
|:--|:--|:--|:--|
| 1 | The **2×2 capture matrix** (Cash-Flow / Non-Cash-Flow × Direct / Indirect) elevated from "presentation layer" to **first-class framework component** | `Part 4 (Transmission Framework)` §4 | Framework component addition |
| 2 | Version number v1.1 → v1.2; version history table and version discipline rewritten; version labels and cross-references in each file synchronized | `Appendix B (Compilation Discipline)` §6, "Part 1 (Main Report)" / "Part 4 (Transmission Framework)" / "Part 7 (Evidence Register)" / "Part 8 (Counter-Evidence Register)" / "Part 9 (Monitoring Dashboard)" / "Part 2 (Final Conclusion)" titles and table headers | Version identification |
| 3 | This file added; the original judgment in `Appendix C (Version History and Revision Trail)` §5 ("does not trigger a version change") is overridden by this ruling, with a trail kept | `Appendix C (Version History and Revision Trail)`, `10_...md` §5 | Record trail |

### 2. What did not change (key) {#sec-2-what-did-not-change-key}

**The judgment criteria, the four-layer classification definitions, the five-tier status label definitions, all load-bearing figures, and all status conclusions — uniformly unchanged.**

Therefore the following v1.1 conclusions remain valid as-is in v1.2:

- "Part 4 (Transmission Framework)" chain segments 1–3 🟢, segments 4–5 🟡, segment 6 🟠, segment 7 🔴, segment 8 ⚪️;
- Four-layer status: Layer 1 Partially demonstrated ｜ Layer 2 Demonstrated (composition determines nature) ｜ Layer 3 Weak evidence ｜ Layer 4 Not demonstrated;
- The finalized conclusions of "Part 2 (Final Conclusion)", plus the 24 revisions and all verification conclusions recorded in "Appendix C (Version History and Revision Trail)".

**Measured difference (mechanical check, not self-reported)**: a line-by-line diff of the 13 files shows **144 changed lines** versus v1.1; after line-by-line inspection, **all fall into three categories** — ① version labels and titles; ② cross-referenced filenames (`_v1.1.md` → `_v1.3.md`); ③ the three intentional rewrites listed in this document (03 matrix positioning and version discipline, 10 §5 ruling trail, README version history). **No line touches judgment criteria, status labels, load-bearing figures, or conclusion wording.**

**Why changing the slicing dimension does not require re-running the judgment**: the 2×2 matrix **re-presents the existing four layers along a different dimension** (by "whether cash flow is formed" × "whether transmission is direct"), introducing no new criteria, thresholds, or evidence. Its role is to give captures that **have no single measurable value**, such as "collateral / monetary premium", an explicit coordinate within the framework, filling the structural gap in v1.0. **Changing the slicing dimension ≠ changing the criteria.**

### 3. Guidance for subsequent citers {#sec-3-guidance-for-subsequent-citers}

- Citing **judgment conclusions**: use v1.2 (consistent with v1.1).
- Citing **version history**: v1.0 (special-topic root directory, frozen) → v1.1 (`../v1.1/`, frozen) → v1.2 (this directory, current). [**This line is a verbatim trail from the v1.1 round**; **the current version is v2.0**]
- Citing the **framework component list**: v1.2 governs — four layers (by mechanism domain) × 2×2 (by cash flow / transmission directness); the two have different coordinates and the same source of conclusions.
- Any subsequent **criteria / classification / label definition** change is still appended, per version discipline, in `Part 3 (Criteria and Conceptual Audit)` and in this file.

---

### Appendix: corrections within v1.3 (patch level, no version-number increase) | 2026-10-03 (UTC) {#appendix-corrections-within-v1-3-patch-level-no-version-number-increase-2026-10-}

**Source-label correction**: in "Part 1 (Main Report)" and "Part 5 (Value Distribution Matrix)", the source column for "application-layer fees $521.6M/month" is corrected from **DefiLlama** to **growthepie** (the real first-hand source being `raw/probe_growthepie_fundamentals.json`), and the **"L2 application layer"** definition qualifier is restored; the "Ethereum 2025 chain-level fees $523.17M" previously placed inside the value cell belongs to **a different definition** (DefiLlama 2025 chain-level fees ranking, correctly cited in "Part 5 (Value Distribution Matrix)" row 11), and has been moved out and explicitly marked as **a different definition, not mutually corroborating**. The "L2 application" qualifier in the "Part 1 (Main Report)" §02 table and in the "Part 2 (Final Conclusion)" compression table has also been synchronized.

**Blast radius**: 0 number changes; 0 criteria changes; 0 status-label changes; 0 conclusion changes. The full trail is in `Appendix C (Version History and Revision Trail)` §8.

**ZK Labs ｜ Jinwu Qiankun No.2 ｜ 2026-10-03 (UTC)**

---

### 1. Parts first reported as "checked and error-free" (positive verification) {#sec-1-parts-first-reported-as-checked-and-error-free-positive-verification}

| Check item | Result |
|:--|:--|
| Traceability of load-bearing figures | **Pass**. All load-bearing figures in v1.1–v1.3 can be traced to sources in the evidence files saved in v1.0; the 5 classes of figures marked "new" are either `[CALC]` recomputations with the formulas listed alongside, or register entries N1–N5 in "Part 7 (Evidence Register)" |
| N2 data sources | **Pass**. All 10 BTC-side tokenization readings **hit the already-landed `raw/llama_protocols_all.json`**, with **zero new external requests** |
| Disallowed counting/scoring expressions | **Pass**. Every occurrence of `0/4` / `Score` in the document is either ① a prohibition clause or ② an explicit trail of a deprecated phrasing; **none is used as a judgment** |
| Four-layer seven-field completeness | **Pass**. Layers 1–4 all contain Value Creation / Capture Mechanism / Transmission Mechanism / Evidence / Evidence Against / Current Status / Unknown |
| Leakage substantive determination | **Pass**. Among the eight candidates, **none is mislabeled Leakage**; application layer = Structurally outside, L2 = Discretionary non-capture, dilution = Monetary supply effect, MEV = Unmeasured, 8.7% error = Measurement gap, stablecoin = Channel A |
| Table structure | **Pass**. 68 tables, **zero breaks** |
| Numbering continuity | **Pass**. CA-01…CA-14, N1–N5, CE-1…CE-8, K1…K10, §1–§9 — no skipped numbers |
| Chinese writing standard | **Pass**. `zk_style_lint.py` error=0 warning=0 style=0 |

---

### 2. Hard errors already fixed (all of the "reads fine, does not recompute" kind) {#sec-2-hard-errors-already-fixed-all-of-the-reads-fine-does-not-recompute-kind}

| # | Location | Problem | Fix | Status |
|:--|:--|:--|:--|:--|
| 1 | "Part 9 (Monitoring Dashboard)" L141 | **Total does not match the listed numbers**: the two items sum to 6.89M, yet the text says "total ≈13.52M" (the difference being an unlisted ETF ≈6.63M) | Split into "DAT total 6.89M" and "total locked including ETF 13.52M" | ✅ |
| 2 | "Part 2 (Final Conclusion)" §2 | **The chart and table list only 7 segments, but the body cites "segment 8"** | Segment 8 added to the chart, `ETH Economic Value` row added to the table | ✅ |
| 3 | "Part 4 (Transmission Framework)" L102 | **The four questions contradict themselves**: "whether burned: partially 100% burned" | Changed to "base fee and blob fee 100% burned; priority fee not burned, goes to the validator account" | ✅ |
| 4 | "Part 1 (Main Report)" L38 | **Unit ambiguity**: `$2.891M×10³` (literally read as $2.89 million, actually $2.891 billion) | Unified to `≈ $2,891M (= $2.891B)`; in the same batch `$252,888 thousand` → `$252.888M` | ✅ |
| 5 | "Part 4 (Transmission Framework)" L127 / "Part 8 (Counter-Evidence Register)" L50 | **Color–label mismatch**: `Weak evidence` uses 🟠 in 01 and 🟡 in 03/07, violating this version's legend | Unified to 🟠 | ✅ |
| 6 | `01/02/03/07/09`, 6 places in total | **Sixth-tier label**: `Demonstrated but composition matters` exceeds the five-tier definition | Changed to the base label + parenthetical qualifier `Demonstrated (composition determines nature)` | ✅ |
| 7 | "Part 1 (Main Report)" L135 | **Scope error**: writes Layer 2's overall status as the status of the security component | Changed to "the status of Layer 2's **security component** is Demonstrated (composition determines nature)" | ✅ |
| 8 | "Part 2 (Final Conclusion)" §1 | **Self-contradiction**: the §1 heading says "proven by evidence (🟢)", while §5 gives the same batch of mechanisms as Partially demonstrated | Heading changed to "the mechanism layer is proven by evidence (mechanism 🟢; status strength counted separately)" | ✅ |
| 9 | `01/03/09`, 8 places in total | **Chain segment 6 status inconsistent in four places** (three writings: 🟡 / 🟠 / "🟡→🟠") | Unified to **🟠 Weak evidence**, with a terminology mapping anchor added in "Part 4 (Transmission Framework)" §3 | ✅ |
| 10 | `00/02/05`, 3 places in total | **Dangling reference**: "see "Part 9 (Monitoring Dashboard)" §4" but §4 is Group C, the actual target being §7 | Unified to ""Part 9 (Monitoring Dashboard)" §7 `[UNKNOWN]` completion roadmap" | ✅ |
| 11 | "Part 9 (Monitoring Dashboard)" L25 | Dangling reference to "Group A note" (no such note exists in the document) | Changed to "see B1 / B2 for blob usage and pricing" | ✅ |
| 12 | "Appendix B (Compilation Discipline)" L41 / "Appendix A (v1.0 Research State Inventory)" L118 | **Count does not match content**: the heading says "six items", the content has 5 | Heading no longer claims a count; "Appendix A (v1.0 Research State Inventory)" changed to "five methodological red lines" | ✅ |
| 13 | "Part 1 (Main Report)" L119 | **Coined term + over-assertion**: "the bearish thesis… has been institutionally blocked" (the term is undefined in either the v1.0 or the v1.1 draft) | Changed to the neutral wording "current rules set a price floor, so that… cannot be triggered by blob demand alone" | ✅ |
| 14 | "Part 4 (Transmission Framework)" L136 / "Part 2 (Final Conclusion)" L30 | **Absolute terms not downgraded**: "no first-hand indicator shows…" | Changed to "no observable indicator is currently observed (no local aggregation source)" | ✅ |
| 15 | 15 places document-wide | **The "only" discipline not carried through** ("Part 8 (Counter-Evidence Register)" had itself kept a trail saying "all downgraded", yet residues remained) | Observational-set qualifiers added place by place (currently / as available locally / identified) | ✅ |
| 16 | `01/04/05`, 3 places in total | **Leakage naming overreach**: unmeasurable counterfactual items still called `Potential leakage` | Renamed to `Potential non-capture (conditional, not counted as Leakage)` | ✅ |
| 17 | "Part 1 (Main Report)" L213 | **Layer/chain-segment mixing**: the same column first gives four-layer numbers 1–4, and the last row gives chain segment number 8 | Header changed to "Layer / Chain segment", last row changed to "Chain segment 8" | ✅ |
| 18 | "Part 1 (Main Report)" L78 | **Core negative conclusion lacks a definition**: monetary premium 1.077 first appears without a definition | Added "ETH market cap ÷ all-chain stablecoins; 2.543→1.778→1.182→1.077; on the Ethereum on-chain definition 2.28, same direction" | ✅ |
| 19 | "Part 1 (Main Report)" L14 | **Key term first appears without Chinese**: `Transmission Mechanism` | Chinese added along with the four-question criterion | ✅ |
| 20 | "Part 6 (Counterfactual)" L94 | **Causal extrapolation**: wrapped BTC is an ERC-20 → "partially converted into Ethereum-hosted activity" without a type label | Added `[INTERPRETATION]` + the "hosting ≠ capture" qualifier | ✅ |
| 21 | "Part 9 (Monitoring Dashboard)" D3/D4 | **Unfalsifiable indicators not marked** | Explicitly marked "currently unfalsifiable: not included in this round's trigger execution" | ✅ |
| 22 | "Appendix B (Compilation Discipline)" §1 | **Delivery index lacks guidance** (answers only "which file corresponds to which item of the task brief", not "which to read first") | Added a suggested reading order + a one-sentence purpose for each file | ✅ |
| 24 | "Part 3 (Criteria and Conceptual Audit)" L168 / "Part 6 (Counterfactual)" L76 | **Chinese content uses ASCII straight quotes** (quote domain mismatch) | Changed to corner brackets (「」) | ✅ |
| 23 | "Part 4 (Transmission Framework)" §4 | **Item named by the original review missing**: the 2×2 capture matrix (Cash-Flow / Non-Cash-Flow × Direct / Indirect) did not exist as an artifact | Added that matrix (**elevated to a first-class framework component since v1.2**, adding no criteria and changing no four-layer classification) | ✅ |

---

### 3. Verification results (re-run after revision) {#sec-3-verification-results-re-run-after-revision}

| Item | Result |
|:--|:--|
| Table column count | 68 tables, breaks **0** |
| Style self-check | error=0 / warning=0 / style=0 |
| Residue scan | `composition matters` / `🟡 Weak evidence` / `Potential leakage` / absolute terms / ambiguous-unit phrasings — **all 0 hits** |
| Change-landing review | For 64 changes, **the asserted hit count = 1 item by item**; written only after the dry run was fully green |

---

### 4. Opinions registered but not changed / rejected (with reasons) {#sec-4-opinions-registered-but-not-changed-rejected-with-reasons}

| Opinion source | Opinion | Disposition | Reason |
|:--|:--|:--|:--|
| Logic line F-1 | The newly added empirical data falls outside the "Part 6 (Counterfactual)" module; suggests **removing the values** from `01/07/08` | **Partially adopted**: source cross-reference labels added at all three places + boundary clarification in "Appendix B (Compilation Discipline)"; **removal of the values rejected** | ① the data is **not a re-search** (it reuses the already-landed `raw/`, with zero new external requests) and does not touch the substantive prohibition in §21; ② the value at "Part 1 (Main Report)" L148 sits in a load-bearing cell of the "comparison" table, and removing it would leave a dangling qualitative judgment; ③ it is already explicit in "Appendix B (Compilation Discipline)" §0 that appearances in other files are always cross-references with sources and **do not constitute an independent evidence source** |
| Language line F49/F50/F52/F54 | Core conclusion sentences, the mechanism×status table, and key numbers repeated in 6 places | **Registered, not changed** | This is a design trade-off of a multi-file deliverable: the 11 files must each be **independently readable** and citable on their own as a framework for later use (L2 / Stablecoin / RWA / DeFi / Solana). Unified compression would break the self-containedness of individual files |
| Language line F27/F32/F35/F37/F39/F40/F41 | Mixed Chinese and English terminology, three sets of eight-segment names, three numbering systems | **Partially adopted** (a terminology mapping anchor added in "Part 4 (Transmission Framework)" unifying chain segment ↔ layer ↔ label); the rest registered | The three numbering systems correspond respectively to "task brief chapter / directory file number / section within a file", i.e., different coordinate systems; forced unification would instead increase ambiguity |
| Language line long-sentence category (13 items) | >40 characters without a break | **Registered, not changed** | Mostly judgment sentences and qualifier sentences; breaking them would sever the "condition—conclusion" binding; this category does not affect the readability of judgments |

---

### 5. Explanation of version semantics {#sec-5-explanation-of-version-semantics}

All 24 revisions recorded here are **revision level** (fixing errors, unifying definitions, adding labels and guidance), and **change no criteria / classification / label definitions**.

**But this delivery subsequently underwent one framework-level change**: on 2026-10-02 the research review ruled that the newly added **2×2 capture matrix** (Cash-Flow / Non-Cash-Flow × Direct / Indirect) is a **framework-level component addition**, and on that basis raised the version **v1.1 → v1.2**.

That matrix was labeled "presentation layer" in the v1.1 manuscript (the original judgment at the time being "does not trigger a version change"); in v1.2 it is elevated to a **first-class framework component**. **The judgment criteria, the four-layer classification, the five-tier label definitions, and all load-bearing figures are unchanged**, so the verification conclusions in §1–§4 of this record remain valid as-is in v1.2. The full diff is in `Appendix C (Version History and Revision Trail)`.

---

### 6. v1.2 Framework Delta QA (2×2 capture matrix elevated to a first-class framework component) {#sec-6-v1-2-framework-delta-qa-2-2-capture-matrix-elevated-to-a-first-class-framework}

Although the v1.2 change does not touch the criteria, it is still run through once more as a framework-level change:

| Check item | Result |
|:--|:--|
| Mapping from the 2×2 matrix → the four layers | **Pass**: the correspondence between the matrix's four cells and the four categories is verifiable one by one, with no attribution conflict |
| Status labels | **Pass**: the five-tier definitions are unchanged, and no layer / chain-segment tier was re-judged because of the matrix addition |
| Cross-references | **Pass**: all 13 `_v1.2.md` references are reachable |
| Consistency with conclusions | **Pass**: a line-by-line diff against v1.1 shows 144 changed lines, **all falling into the three categories of version labels / cross-references / intentional rewrites**, with zero judgment-content change |

**Conclusion**: v1.2 introduces no new logic risk; **no** status conclusion needs re-running.

---

### 7. v1.3 Final Logic Audit QA (6 P0 logic tightenings) {#sec-7-v1-3-final-logic-audit-qa-6-p0-logic-tightenings}

This round is **logic tightening**, not new research. Review method: locate the original sentence for each of the 6 P0s item by item → mechanical recomputation → landing → post-hoc assertion review.

| # | P0 | Original wording | v1.3 wording | Review |
|:--|:--|:--|:--|:--|
| P0-1 | Mechanism existence ≠ capture has occurred | "the four channels **genuinely capture value**" | "four explicit **transmission mechanisms** exist; **mechanism existence ≠ incremental ETH economic value already produced**"; Security split into "mechanism 🟢 / lock-in utility 🟢 / incremental economic value 🔴" | ✅ |
| P0-2 | Migration must not skip tiers | "**migration happened**, realization did not" | Split into five independent propositions: fee side ↓🟢, holding side ↑🟢, composition change 🟡, capture migration 🟡 (**interpretive**), realization 🔴 | ✅ |
| P0-3 | Do not infer the objective function | "A is **falsified**", "has **paid** the rent cost of acquiring the network" | Changed to **Observed Economic Design**: state only the observed trade-off; the objective function is marked ⚪️ **not inferred** | ✅ |
| P0-4 | 2.73% may not be called a capture rate | "protocol captures 2.73%" | "L1 protocol fees ÷ reported ecosystem gross-value proxy ≈ 2.73%, **an order-of-magnitude ratio, not a capture rate**" | ✅ |
| P0-5 | Counterfactuals must not be unfalsifiable | (a) **Created** = "without Ethereum it would not exist" | Three tiers: **Scaled First**, Captured a Share, Hosted; the old tier **explicitly abolished with a trail kept**. **⚠️ Same-round self-audit correction**: the first draft followed the original directive and wrote `Originated / Pioneered`, but that label would require denying colored coins (2012–13), Mastercoin (2013-08), Counterparty (2014-01), and other implementations **predating the Ethereum mainnet** → **still unfalsifiable**, so it is tightened again to `Scaled First` (details in "Part 6 (Counterfactual)" §2 fact correction and the end of this section) | ✅ (including the self-audit second correction) |
| P0-6 | Failure ≠ not verified | "segments 6→7 **transformation failed**" | "**Transmission not demonstrated** (no verifiable transmission observed yet)" | ✅ |

**Six other fixes** (supplementary opinions from the research review): Counterfactual "ETH has a structural advantage over BTC" → structural **difference** (noting that the two have different Transmission Mechanisms); monetary premium 1.077 → **ETH-to-Stablecoin Market-Cap Ratio (a proxy for the premium, not the premium itself)**, with the "only" at that place deleted; the segment 6→7 downgrade synchronized to "Part 4 (Transmission Framework)"; a new eight-layer "what we know / what we do not know" compression table added ("Part 2 (Final Conclusion)" §4); this section added to the QA record; README data discipline changed to "**single source of origin, citations with sources permitted**".

**Review method**: all changes in this round were written only after **the asserted hit count = 1 item by item** (including 1 place with an expected 2 hits); then four re-checks were run: full diff, table column count, style self-check, and residue scan.

**Conclusion**: v1.3 **changes no tier conclusion**; it only tightens **wording strength and naming**.

---

### 8. v1.3 source-label correction (the provenance of the load-bearing figure $521.6M/month) | 2026-10-03 (UTC) {#sec-8-v1-3-source-label-correction-the-provenance-of-the-load-bearing-figure-521-6m-}

**Trigger**: during an in-depth external institutional review (IC perspective), the assistant's self-audit found one **source-label drift**.

| Item | Content |
|:--|:--|
| Figure involved | Application-layer fees **$521.6M/month** (appearing in the "Part 1 (Main Report)" §01 table, the "Part 1 (Main Report)" §02 table, "Part 5 (Value Distribution Matrix)" row 6, and the "Part 2 (Final Conclusion)" compression table — 4 places in total) |
| The true first-hand source of this figure | **growthepie** (`raw/probe_growthepie_fundamentals.json`, 3.84 MB, field `fees_paid_usd`; definition = **L2 application layer** fees, 2026-09, **26 chains**, 90-day window) |
| The erroneous label in v1.3 | The source column of the "Part 1 (Main Report)" §01 table and of "Part 5 (Value Distribution Matrix)" row 6 wrote **DefiLlama**, and stuffed "(Ethereum 2025 chain-level fees $523.17M)" into the value cell |
| What was wrong | $523.17M is the Ethereum value in the **DefiLlama 2025 "chain-level fees" ranking** (correctly cited in "Part 5 (Value Distribution Matrix)" row 11), and is **not the same definition, not the same period, not the same object** as this cell; the two numbers only appeared to corroborate each other because they differ by 0.3% → constituting **false corroboration** |
| Another weakening | The original wording dropped the **"L2"** qualifier, making "L2 application-layer fees" read as "Ethereum network-wide application fees" — this figure is the **largest single component of the denominator ($586.7M/month)** of the 2.73% order-of-magnitude ratio, so the qualifier must be retained |

**Disposition**: all 4 places unified to **growthepie (L2 application-layer definition; 2026-09, 26 chains, 90-day window)**; the "Part 1 (Main Report)" §01 table retains $523.17M but **explicitly marks it as a different definition, not mutually corroborating**.

**Why this counts as patch level and does not raise the version number**: numbers, definitions, criteria, status labels, and all conclusions have **zero changes**; what changed are the **cited-source labels and qualifiers**; handled as an in-v1.3 correction trail (the same way as the P0-5 fact correction).

**Lesson (kept for reference)**: **close in value ≠ the same indicator.** The "source" column of a load-bearing figure may only name the producer of that figure itself; a cross-reference must be placed in a separate cell and explicitly declare a different definition.

**ZK Labs ｜ Jinwu Qiankun No.2 ｜ 2026-10-03 (UTC)**

---

## Appendix D | File Mapping, Reading Path, and Terminology Conventions {#appendix-d-file-mapping-reading-path-and-terminology-conventions}

**In one sentence**: this report is the **single-file self-contained version** of v1.3; the original 13 split deliverables are folded into the following sections by function, **preserved verbatim, with zero change to conclusions** (see the trail entries in Appendix C).

### D1 | Original file → this section {#d1-original-file-this-section}

| Original file | Folded into |
|:--|:--|
| `README.md` | Appendix B Compilation Discipline + this Appendix D |
| `00_PREVIOUS_RESEARCH_STATE.md` | Appendix A — v1.0 Research State Inventory |
| `01_ETH_VALUE_CAPTURE_REPORT_v1.3.md` | Executive Summary + Part 1 — Main Report |
| `02_CONCEPTUAL_AUDIT.md` | Part 3 — Criteria and Conceptual Audit |
| `03_VALUE_TRANSMISSION_FRAMEWORK_v1.3.md` | Part 4 — Transmission Framework |
| `04_VALUE_DISTRIBUTION_MATRIX.md` | Part 5 — Value Distribution Matrix |
| `05_COUNTERFACTUAL_VALUE_CAPTURE.md` | Part 6 — Counterfactual |
| `06_EVIDENCE_REGISTER_v1.3.md` | Part 7 — Evidence Register |
| `07_COUNTER_EVIDENCE_REGISTER_v1.3.md` | Part 8 — Counter-Evidence Register |
| `08_MONITORING_DASHBOARD_v1.3.md` | Part 9 — Monitoring Dashboard |
| `09_RESEARCH_CONCLUSION_v1.3.md` | Part 2 — Final Conclusion |
| `10_QA_AND_REVISION_RECORD.md` | Appendix C — Version History and Revision Trail |
| `11_CHANGELOG.md` | Appendix C — Version History and Revision Trail |

**Archiving**: the original 13 split files are saved byte-for-byte at `../_archive/v1.3_13files/` for line-level traceability.

### D2 | Coverage of task brief §21 deliverables {#d2-coverage-of-task-brief-21-deliverables}

| # | Task brief requirement | This section |
|:--|:--|:--|
| — | (§1 prerequisite artifact) Previous Research State | Appendix A |
| D1 | ETH Value Capture Research (main report) | Executive Summary + Part 1 |
| D2 | Conceptual Audit (Old → Problem → New → Reason) | Part 3 |
| D3 | ETH Value Transmission Framework | Part 4 |
| D4 | Value Distribution Matrix | Part 5 |
| D5 | Counterfactual Value Capture Framework | Part 6 |
| D6 | Updated Evidence Register (new evidence only) | Part 7 |
| D7 | Updated Counter-Evidence Register | Part 8 |
| D8 | Updated Monitoring Dashboard | Part 9 |
| D9 | Final Research Conclusion | Part 2 |
| — | (pre-delivery gatekeeping record) | Appendix C |
| — | (version change record) | Appendix C |

> Note: the "Task brief requirement" column retains **the version label of the task brief original text (v1.1)**; the actual content of this version is finalized as **v1.3**; see Appendix C for the evolution.

### D3 | Suggested reading path {#d3-suggested-reading-path}

1. **Conclusions only**: Executive Summary → Part 2 (Final Conclusion).
2. **Basis for judgments**: Part 1 (Main Report) → Part 4 (Transmission Framework: four layers + eight-segment chain + four-question criteria).
3. **Basis for conceptual changes**: Part 3 (item-by-item Old → Problem → New → Reason).
4. **Data provenance**: Part 7 (Evidence Register) / Part 8 (Counter-Evidence Register).
5. **Re-checks and next steps**: Part 9 (Monitoring Dashboard: four groups A/B/C/D + event-driven items + `[UNKNOWN]` completion roadmap).
6. **Tracing old conclusions**: Appendix A (v1.0 state inventory, not an entry path).
7. **Versions and trail**: Appendix C.

### D4 | Terminology and coordinate conventions {#d4-terminology-and-coordinate-conventions}

- **"This round"** = the **logic-tightening and conceptual-elevation rounds after v1.0 (v1.1→v1.5)**, not the present moment.
- **"Task brief"** = the task brief for this special topic (external input); `§N` in it refers to the task brief item number.
- **"v1.0"** = the previous research round, whose deliverables are in the special-topic root directory (`deliverables/`, `notes/`, `raw/`), and which is a **read-only baseline**.
- **"§X" without book-title marks** = an internal section number of this file.
- **Status labels** allow only five tiers: `Demonstrated` ｜ `Partially demonstrated` ｜ `Weak evidence` ｜ `Not demonstrated` ｜ `Unknown` (replacing the scoring system).
- **Chain status symbols**: 🟢 Demonstrated ｜ 🟡 Partially Demonstrated ｜ 🟠 Weak Evidence ｜ 🔴 Not Demonstrated ｜ ⚪️ Unknown.
- **Platform tax vs. sovereign settlement base (v1.5 terminology)**: an **interpretive contrast** between two business models — the former rents per transaction on high-frequency end-user interactions (App Store type), the latter prices institutional-grade settlement and finality in bulk (wholesale / clearing-base type). **The contrast is `[INTERPRETATION]`, not a judgment**; in this report it serves only to explain the already-observed asymmetry "**unit rent falls first, wholesale revenue not yet observed**".
- **Sovereign Collateral (v1.5 terminology)**: the asset property of serving as collateral **with no issuing entity, with no counterparty, and in native form**. **It is a property-attribute judgment, not a value capture judgment.**
- **Composability Premium (v1.5 terminology)**: the **hypothesis** that cross-domain interaction depends on a unified state adjudication court ⇒ **structural demand arises for the court's native collateral**. **No quantifiable dashboard** (no fees, no burns, no return flow) ⇒ Layer 4 **remains ⚪️**.
- **Sequencer Rights (v1.5 terminology)**: ownership of transaction ordering and fee retention. **Centralized sequencer = sequencing rights stay on the L2 side**; **based / native rollup = sequencing rights returned to L1** (Taiko is the field evidence, **n=1**).
- **The boundary between the interpretive layer and the judgment layer (established in v1.5, load-bearing)**: the `[INTERPRETATION]` framework **only explains the meaning of observed facts; it adds no judgments and changes no tiers**; no framework text **may enter the input of status-tier judgments**. **The persuasiveness of a framework ≠ the strength of the evidence.**
- **The boundary between 🔴 and ⚪️ (established in v1.4 as a load-bearing criterion)**: **🔴 Not Demonstrated = a usable observation instrument exists, and the readings point to "not occurring"**; **⚪️ Unknown = no usable, valid observation instrument** — in that case **🔴 must not be assigned** (a negative judgment made without a measurable instrument cannot be supported by evidence). Applied to this report: **Layer 4 = ⚪️** (the only proxy is price-derived, conflicting with No Price Shortcut).
- **Time definition (patch-level unification in v1.5, load-bearing)**: **all dates and times in this file are UTC** (the same applies to Deribit tape / on-chain readings / events / version trails). ⚠️ **v1.4 and earlier versions are labeled in Beijing time (CST = UTC+8)**; the two **may differ by 1 day** (Beijing 00:00–08:00 corresponds to the previous UTC day) — note this when citing dates from older versions.
- **All thresholds are analytical thresholds set by this report**; they are not market consensus and do not constitute forecasts.

---

**ZK Labs ｜ Jinwu Qiankun No.2 ｜ 2026-10-03 (UTC)**


---

## Appendix E | Key Events of 2026 and Timing Breaks (new in v2.0) {#appendix-e-key-events-of-2026-and-timing-breaks-new-in-v2-0}

**Why added**: versions up to v1.5 were absent on, or gave only one line to, **several events this year that bear directly on load-bearing judgments**. This appendix registers **first-hand verification results** and **the impact on the report's judgments** item by item.

- Verification date: **2026-10-03 (UTC)** ｜ Method: 3 independent parallel verification paths, first-hand sources prioritized
- Detail: `v2.0/EXTERNAL_FACTS_VERIFIED.md` ｜ `v2.0/data/external_verification.json`

### E1 | Event register {#e1-event-register}

| # | Event | Time (UTC) | First-hand fact | Which part of the report it touches | Handling in this version |
|:--|:--|:--|:--|:--|:--|
| 1 | **KelpDAO rsETH cross-chain bridge attack** | 2026-04-18 17:35:35 | 116,500 rsETH ≈ **$292M** (block 24,908,285); root cause **1-of-1 DVN**; LayerZero attribution **DPRK Lazarus**. **Aave official report (04-20)**: bad-debt scenario **$123.7M–$230.1M** (89,567 rsETH deposited / 82,650 WETH borrowed) | **CE-9** (Restaking systemic resonance fragility), the Layer 2/3 "lock-in utility" layer | Chain supplemented: CE-9 upgraded from "structural risk" to "**structural risk + a case realized within the year**"; **status tier unchanged** |
| 2 | **Glamsterdam upgrade** | Sepolia **2026-10-06 13:53:36** (3 days before activation as of this version's editing); Hoodi/Mainnet TBD | **18 SFI items**: **EIP-7732 ePBS**, **EIP-7928 BALs**, the gas repricing group (summarized in EIP-8007); **official gas limit target 200M** (test reference 150M) | **Group A thresholds** (gas dimension), **MEV definition**, **B2 threshold** | Chain supplemented to the monitoring dashboard triggers and the MEV UNKNOWN item; **no parameter changes in advance** |
| 3 | **EIP-8363 Tapered Issuance Burn** | Draft **2026-07-14**; EF Protocol **declined 2026-09-07**; author **withdrew 2026-10-01** | **No longer within Hegotá scope**: the EF Protocol tier list (2026-09-07) rated 62 proposals, and **EIP-8363 was judged DFI (Declined for Inclusion), unanimous**; **on 2026-10-01 the author formally withdrew it from Hegotá consideration on Ethereum Magicians** (thread title "Withdrawing EIP-8363 from consideration for Hegotá"), with progress moved to an independent issuance-policy process (the first Issuance Forum scheduled for Devcon 2026-11). The EIP **itself remains a Draft and has not been deleted** (listed on eips.ethereum.org); the Hegotá timeline is 2027 | The wording boundary of "**no governance basis**" | Wording tightened to "**no first-hand basis for answering the objective function / intent**"; **this row is a status correction (erratum E-6)**: corrected from "among Hegotá PFI candidates" to "**declined by EF Protocol on 2026-09-07 + withdrawn by the author on 2026-10-01**"; **no tier change, no threshold change, no change to any judgment** |
| 4 | **MetaMask exits Lido** | Disclosure date **2026-09-30** | **Official announcement** (MetaMask news + Lido research forum), confirmed to be due to an infrastructure compromise | The composition risk of the staking layer | The audit's original `[UNVERIFIED]` label **is withdrawn here**; no change to the staking-layer status tier |
| 5 | **Robinhood Chain launch + gas subsidy** | Launch 2026-07-01; subsidy 07-01→09-29 (later extended to 12-31) | Four sources agree on the mainnet; the subsidy is **an official act**; growthepie's official documentation explicitly states **subsidies are not deducted** | All L2 readings (concentration, L1 cost share, retention, +296%) | Chain supplemented: see the **P0-2 special block**; "fee uniformity" downgraded from "demonstrated" to "**observed within the window**" |

### E2 | Timing breaks (unmarked in v1.5, marked in v2.0) {#e2-timing-breaks-unmarked-in-v1-5-marked-in-v2-0}

1. **Cross-regime break**: the trailing-365d window (**2025-10-02 → 2026-10-01**) **spans the Fusaka / EIP-7918 activation date 2025-12-03**, while the preceding year's window (2024-10-02→2025-10-01) is **entirely before it** ⇒ the year-over-year comparison of blob and fees is a **cross-regime comparison**, not a year-over-year comparison within the same regime.
2. **Subsidy-period overlap**: the L2 fee reading takes the **full month of 2026-09 (30 days)**, which falls **within** the Robinhood Chain launch (07-01) and its gas subsidy period (07-01→09-29, later extended to 12-31) ⇒ the in-window reading carries the dual effect of **launch period + subsidy period**.
3. **Snapshot and window from different sources**: stablecoin share, TVL, and protocol balances are all **single-point snapshots**, from a different source than the 30/90/365d **rolling windows** of the fee class, and **must not be treated as readings at the same point in time**.

### E3 | Impact on judgments (item by item, all supplemented above) {#e3-impact-on-judgments-item-by-item-all-supplemented-above}

- **CE-9**: evidence grade upgraded (risk → risk + realized case); **the handling conclusion and status tier are unchanged**.
- **Group A / B2**: Glamsterdam's 200M gas target will **change the dimension** ⇒ thresholds must be **re-calibrated** after the upgrade lands; this version **only registers triggers and adjusts no parameters**.
- **MEV**: ePBS changes the builder/relay structure ⇒ the distribution definition changes, and the related UNKNOWN **may be partially resolved**.
- **"No governance basis"**: nameable roadmaps and EIP records **do exist**, but they **do not answer the objective function** ⇒ wording tightened, **judgment unchanged**.
- **Status tiers**: **this appendix changes no status tier and changes no threshold**.

> **⚠️ This appendix's net effect on the "v1.5 conclusions" is zero status-tier change**. Its role is to fill v1.5's "**absent facts**" **to a place where they can be read**, so that existing judgments **can be tested**, rather than being protected by implicit assumptions.
