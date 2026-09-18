# LeadUX Content Strategist

Open-source, universal, evidence-first **strategy formulation system** between verified market research and downstream content creation.

It is designed to answer a harder question than “what should we post?”:

> Given verified market evidence, confirmed business/founder context, real constraints, and multiple plausible directions — **which strategy should we choose, why this one, what are we deliberately not doing, and what evidence would make us change course?**

## Architecture

```text
LeadUX Competitor Research
        ↓ verified strategy handoff
Identity / Business Context
        ↓
Audience / ICP Fit
        ↓
Customer Journey / Funnel Intent
        ↓
Positioning / Offer Fit
        ↓
Channel / Distribution Fit
        ↓
Founder / Brand Context
        +
Strategy Memory / First-party Performance
        +
Validated Strategy Patterns
        ↓
Objective Mapping
        ↓
STRATEGY DIAGNOSIS
        ↓
2–4 MATERIAL STRATEGIC THESES
        +
STATUS-QUO BASELINE
        ↓
NON-COMPENSATORY HARD GATES
        ↓
ONE PRIMARY STRATEGIC THESIS
        ↓
STRATEGY CHALLENGER
        ↓
STRATEGY VALIDATION
        ↓
Strategic Wedge
        ↓
Content Pillars / Opportunities / Portfolio
        ↓
Experiments / Creator Briefs
        ↓
Performance Learning ↺
```

## v0.9 — Strategy Formulation Engine

The central change in v0.9 is that **pillars are no longer treated as strategy**.

A full strategy now requires:

- a `strategy-diagnosis`;
- 2–4 materially different candidate theses;
- exactly one `STATUS_QUO` baseline;
- five hard gates per thesis;
- exactly one selected primary thesis;
- a strongest alternative;
- explicit trade-offs / `will_not_do`;
- strategic bets and critical assumptions;
- challenger review;
- pre-mortem and reversal triggers;
- thesis-linked downstream content decisions.

### Strategic Thesis

Each thesis states:

```text
OBJECTIVE
WHERE TO PLAY
HOW TO WIN
ADVANTAGE SOURCE
ECONOMIC LOGIC
CONTENT / TRUST MECHANISM
DISTRIBUTION LOGIC
STRATEGIC BETS
TRADE-OFFS
CAPABILITIES REQUIRED
CRITICAL ASSUMPTIONS
EVIDENCE LINEAGE
REVERSAL CONDITIONS
TIME HORIZON
```

### Hard gates

Before options are compared, each thesis must pass:

```text
EVIDENCE_VIABILITY
COMMERCIAL_FIT
CREDIBILITY_PROOF
CAPABILITY_CAPACITY
ETHICAL_LEGAL_FIT
```

A fatal weakness cannot be averaged away by a high score elsewhere.

### Material alternatives

Different wording is not a different strategy.

Options must differ in consequential choices such as:
- where to play;
- how to win;
- economic logic;
- proof mechanism;
- distribution logic;
- resource allocation;
- trade-offs.

Different hooks, topics, formats, cadence, or slogans do not qualify.

### Coherence

Every downstream decision should be able to state:

```text
THIS EXISTS BECAUSE OF THESIS [thesis_id]
```

The system also asks:

> Would this recommendation remain unchanged under the strongest alternative thesis?

If yes, it is likely generic.

## What this repository does not do

It does not:
- redo the companion competitor-research repository;
- invent missing identity/business/market facts;
- infer buyer intent from engagement;
- equate reach with revenue;
- recommend platforms because they are popular;
- let scores choose strategy automatically;
- treat a content calendar as strategy;
- write final posts/scripts by default.

## Core strategy flow

```text
identity-unpacking
→ business-context
→ research handoff
→ strategy-intake
→ audience-icp-fit
→ customer-journey-intent
→ positioning-offer-fit
→ channel-distribution-fit
→ founder-brand-context
→ strategy-memory
→ strategy-pattern-selection
→ objective-mapping
→ strategy-diagnosis
→ strategy-formulation
→ strategy-challenger
→ strategy-validation
→ strategic-wedge
→ content-pillars
→ content-opportunity-engine
→ portfolio-prioritization
→ experiment-design
→ content-briefing
→ synthesis
        ↺ performance-learning
```

## Deterministic validation

The Python layer validates more than JSON shape.

It checks, among other things:
- exactly one status-quo option;
- exactly one selected thesis;
- selected thesis ID consistency;
- strongest alternative validity;
- each hard gate appears exactly once;
- selected thesis has no `FAIL` or `UNKNOWN` hard gate;
- validation cannot `SURVIVE` a failed hard gate;
- final pillars/opportunities/briefs/decisions trace to the selected thesis.

## Install

```bash
pip install -e '.[dev]'
pytest
```

## Validate examples

```bash
leadux-strategist validate examples/strategy-diagnosis.example.json
leadux-strategist validate examples/strategy-formulation.example.json
leadux-strategist validate examples/strategy-validation.example.json
leadux-strategist validate examples/strategy-output.example.json --research examples/research-package.example.json
```

See:
- `SKILL.md`
- `AGENTS.md`
- `docs/SKILLS.md`
- `frameworks/quality-gates.md`
- `docs/STRATEGY_SOURCES.md`

## Companion research layer

The upstream research repository remains responsible for competitor/market/VOC/pricing/GTM/whitespace/signals/contradictions/evidence verification.

This repository starts from the **verified strategy handoff** and focuses on strategic choice.
