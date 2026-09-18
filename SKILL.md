---
name: leadux-content-strategist
description: >-
  Universal evidence-first content strategy system that turns verified research and confirmed
  business/founder context into a diagnosed strategic problem, materially distinct strategic
  theses, one validated primary choice, and thesis-linked content strategy and Creator briefs.
metadata:
  version: 0.9.0
  role: router
  evidence_mode: required
license: MIT
---

# LeadUX Content Strategist — Root Skill Router

## Purpose
Build a real strategy, not a decorated content plan.

The system must separate:
1. evidence/context;
2. diagnosis;
3. strategic alternatives;
4. strategic choice;
5. validation;
6. downstream content execution.

```text
IDENTITY / BUSINESS CONTEXT
        +
VERIFIED RESEARCH PACKAGE
        ↓
AUDIENCE / ICP FIT
        ↓
CUSTOMER JOURNEY / FUNNEL INTENT
        ↓
POSITIONING / OFFER FIT
        ↓
CHANNEL / DISTRIBUTION FIT
        ↓
FOUNDER / BRAND CONTEXT
        +
STRATEGY MEMORY / FIRST-PARTY PERFORMANCE
        +
VALIDATED STRATEGY PATTERNS
        ↓
OBJECTIVE MAPPING
        ↓
STRATEGY DIAGNOSIS
        ↓
2–4 MATERIAL STRATEGIC THESES
        +
STATUS-QUO BASELINE
        ↓
HARD GATES
        ↓
ONE PRIMARY STRATEGIC THESIS
        ↓
STRATEGY CHALLENGER
        ↓
STRATEGY VALIDATION
        ↓
STRATEGIC WEDGE
        ↓
CONTENT PILLARS / OPPORTUNITIES / PORTFOLIO
        ↓
EXPERIMENTS / CREATOR BRIEFS
        ↓
PERFORMANCE LEARNING
        ↺
```

## Non-negotiable principles
1. No material recommendation without lineage.
2. Never invent identity, business facts, audience, buyer state, proof, positioning, channel fit, economics, performance, or outcomes.
3. `UNKNOWN` remains unknown.
4. Market visibility is not demand; competitor activity is not success.
5. Engagement is not purchase intent; reach is not revenue.
6. Popular platforms are not automatically suitable channels.
7. Strategy patterns are mechanisms to adapt, not tactics to copy.
8. Historical performance is observational evidence unless causality was tested.
9. Strategy must create a **real choice** among materially different alternatives.
10. The status quo must be represented as a baseline option.
11. Hard-gate failures cannot be averaged away.
12. A full strategy has one primary Strategic Thesis.
13. Strategy must state what will not be done.
14. Pillars, channels, calendars, posts, and hooks are downstream of the thesis.
15. Every major downstream decision must be traceable to `thesis_id`.
16. High-impact strategy must survive challenger + validation.
17. Final scripts/posts belong to a downstream Creator.
18. Strategy memory and reversal logic must remain explicit and auditable.

Read and obey:
- `AGENTS.md`
- `frameworks/input-contract.md`
- `frameworks/evidence-lineage.md`
- `frameworks/quality-gates.md`
- `frameworks/output-contract.md`
- `frameworks/strategy-memory.md`
- `frameworks/performance-learning.md`
- `references/validated-strategy-patterns.json`

---

# Pre-strategy context

## Step 0 — Identity Unpacking
For founder-led brands use `skills/identity-unpacking/SKILL.md`.

Output: `schemas/identity-profile.schema.json`.

## Step 0.5 — Business Context
Use `skills/business-context/SKILL.md`.

Output: `schemas/business-context.schema.json`.

## Step 1 — Strategy Intake
Use `skills/strategy-intake/SKILL.md`.

Validate research integrity, context completeness, first-party history, and blocking gaps.

## Step 1.25 — Audience / ICP Fit
Use `skills/audience-icp-fit/SKILL.md`.

Keep CONTENT_AUDIENCE, PROBLEM_HOLDER, USER, BUYER, DECISION_MAKER, INFLUENCER, CHAMPION, BLOCKER and ICP separate.

Output: `schemas/audience-icp-fit.schema.json`.

## Step 1.4 — Customer Journey / Funnel Intent
Use `skills/customer-journey-intent/SKILL.md`.

Keep buying role and journey state separate. Do not infer purchase intent from engagement.

Output: `schemas/customer-journey-intent.schema.json`.

## Step 1.5 — Positioning / Offer Fit
Use `skills/positioning-offer-fit/SKILL.md`.

Select only supportable offers, promises, reasons-to-choose, proof boundaries, and gaps.

Output: `schemas/positioning-offer-fit.schema.json`.

## Step 1.75 — Channel / Distribution Fit
Use `skills/channel-distribution-fit/SKILL.md`.

Keep WHO / STATE / JOB / WHERE / FORMAT / ACTION / OUTCOME separate.

Output: `schemas/channel-distribution-fit.schema.json`.

## Step 2 — Founder / Brand Context
Use `skills/founder-brand-context/SKILL.md`.

Merge confirmed context without upgrading hypotheses.

## Step 3 — Strategy Memory / First-party Performance
Use `skills/strategy-memory/SKILL.md`.

Understand historical winners, losers, repetitions, experiments and evidence limits.

## Step 4 — Strategy Pattern Selection
Use `skills/strategy-pattern-selection/SKILL.md`.

Separate mechanism from tactic and claimed result.

## Step 5 — Objective Mapping
Use `skills/objective-mapping/SKILL.md`.

Choose one primary objective and only a small number of secondary objectives. Distinguish business outcomes, content outcomes and diagnostic metrics.

---

# Strategy Formulation Engine

## Step 6 — Strategy Diagnosis
Use `skills/strategy-diagnosis/SKILL.md`.

Diagnosis must compress evidence into:
- one decision statement;
- decisive facts;
- strategic tensions;
- constraints;
- opportunity signals;
- risks;
- uncertainties;
- 2–5 choice questions.

Do not generate the strategy yet.

Output: `schemas/strategy-diagnosis.schema.json`.

## Step 7 — Strategy Formulation
Use `skills/strategy-formulation/SKILL.md`.

Generate:
- 2–4 materially different strategic theses;
- one status-quo baseline.

Options must differ materially in choices such as:
- where to play;
- how to win;
- economic logic;
- proof mechanism;
- distribution logic;
- resource allocation;
- trade-offs.

Different wording, hooks, formats, topics or cadence are not different strategies.

Each thesis conforms to `schemas/strategic-thesis.schema.json`.

### Hard gates
Before comparison evaluate:
- `EVIDENCE_VIABILITY`
- `COMMERCIAL_FIT`
- `CREDIBILITY_PROOF`
- `CAPABILITY_CAPACITY`
- `ETHICAL_LEGAL_FIT`

A critical `FAIL` invalidates the option. A fatal weakness cannot be averaged away.

### Choice
Select exactly one primary thesis.

The selection must answer:

> Why this thesis instead of the strongest alternative?

Output: `schemas/strategy-formulation.schema.json`.

## Step 7.5 — Strategy Challenger
Use `skills/strategy-challenger/SKILL.md`.

Challenge:
- option distinctness;
- hard-gate assumptions;
- evidence lineage;
- strongest alternative;
- trade-offs;
- coherence;
- reversal logic.

## Step 7.75 — Strategy Validation
Use `skills/strategy-validation/SKILL.md`.

Run:
- hard-gate recheck;
- coherence test;
- strongest-alternative review;
- pre-mortem;
- reversal triggers;
- challenger integration.

Return:
- `SURVIVES`
- `NARROWED`
- `INVALIDATED`
- `BLOCKED`

If invalidated, return to Strategy Formulation.

Output: `schemas/strategy-validation.schema.json`.

---

# Downstream content strategy

## Step 8 — Strategic Wedge
Use `skills/strategic-wedge/SKILL.md`.

The wedge is derived from the validated thesis. It cannot invent a second strategy.

## Step 9 — Content Pillars
Use `skills/content-pillars/SKILL.md`.

Pillars are consequences of strategy. Every pillar must preserve `thesis_id`.

Coherence test:

> Would this pillar remain unchanged under the strongest alternative thesis?

If yes, narrow, experimentally justify, or reject it.

## Step 10 — Content Opportunities
Use `skills/content-opportunity-engine/SKILL.md`.

Each opportunity must state why it exists because of the selected thesis, which audience/state it serves, what proof it uses, and what would make it stop.

## Step 11 — Portfolio Prioritization
Use `skills/portfolio-prioritization/SKILL.md`.

Allocate to `CORE / RESPONSIVE / EXPERIMENT / DEFERRED / REJECTED`.

Protect thesis trade-offs. Do not reintroduce rejected strategic directions through the portfolio.

## Step 12 — Experiment Design
Use `skills/experiment-design/SKILL.md`.

Make critical assumptions testable without fabricated thresholds.

## Step 13 — Creator Briefs
Use `skills/content-briefing/SKILL.md`.

Briefs must preserve `strategic_thesis_id`, audience role, journey state, proof, channel role, claim boundaries, CTA and measurement level.

Do not write final content by default.

## Step 14 — Synthesis
Use `skills/synthesis/SKILL.md`.

The final artifact centers on:
- Strategy Diagnosis;
- all strategic options + status quo;
- selected Strategic Thesis;
- strongest alternative;
- hard gates;
- trade-offs;
- strategic bets;
- validation/challenger;
- reversal triggers;
- thesis-linked wedge, pillars, opportunities, experiments and briefs.

## Feedback — Performance Learning
Use `skills/performance-learning/SKILL.md`.

Performance may:
- strengthen the thesis;
- narrow it;
- invalidate an assumption;
- promote an alternative;
- trigger reformulation.

Do not confuse content response with business outcome.

---

# Strategy integrity status

End the final strategy with one of:

```text
READY
READY_WITH_GAPS
NEEDS_RESEARCH
BLOCKED
```

`READY` requires:
- sufficient upstream context;
- a valid diagnosis;
- materially distinct alternatives;
- a status-quo baseline;
- one selected thesis;
- no unresolved fatal hard-gate failure;
- explicit trade-offs;
- validation that is `SURVIVES` or accepted `NARROWED`;
- explicit reversal logic.

The goal is not more content ideas. The goal is a defensible strategic choice that causes downstream actions to be different.
