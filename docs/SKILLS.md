# Skills architecture

LeadUX Content Strategist separates evidence/context, strategy formulation, validation, and downstream content execution.

| Skill | Responsibility | Must not do |
|---|---|---|
| identity-unpacking | Build confirmed identity profile | Infer personality/values/expertise |
| business-context | Capture commercial reality | Invent economics/audience/priorities |
| strategy-intake | Validate readiness | Repair gaps by invention |
| audience-icp-fit | Separate audience, user, buyer, decision-maker, ICP | Fabricate personas |
| customer-journey-intent | Map evidence-backed buying states | Infer intent from engagement |
| positioning-offer-fit | Establish supportable offer/promise/reason-to-choose | Invent USP |
| channel-distribution-fit | Establish supportable distribution roles | Recommend channels by popularity |
| founder-brand-context | Merge confirmed strategy context | Upgrade hypotheses |
| strategy-memory | Load auditable history | Treat memory as market proof |
| strategy-pattern-selection | Adapt reusable mechanisms | Copy tactics/results blindly |
| objective-mapping | Set the decision objective | Default to vanity metrics |
| **strategy-diagnosis** | Compress evidence into the strategic problem/tensions | Recommend a solution prematurely |
| **strategy-formulation** | Generate distinct theses, hard-gate them, choose one | Treat wording variants as alternatives or let scores decide |
| strategy-challenger | Attack the selected thesis | Protect the narrative |
| **strategy-validation** | Recheck gates, coherence, alternatives, pre-mortem, reversals | Quietly invent a replacement strategy |
| strategic-wedge | Derive content-facing wedge from thesis | Create a second strategy |
| content-pillars | Derive bounded strategic territories | Treat pillars as strategy |
| content-opportunity-engine | Generate thesis-linked opportunities | Produce generic ideas |
| portfolio-prioritization | Allocate scarce resources | Reintroduce rejected directions |
| experiment-design | Test uncertainty | Fabricate precision |
| content-briefing | Preserve strategy into Creator handoff | Write final content |
| synthesis | Compile the auditable strategy | Hide gaps/alternatives |
| performance-learning | Update assumptions from outcomes | Claim causality from correlation |
| research-gap-router | Request missing evidence | Fill research gaps with intuition |

## Strategy formulation pipeline

```text
VERIFIED INPUTS
    ↓
strategy-diagnosis
    ↓
2–4 candidate theses + STATUS_QUO
    ↓
hard gates
    ↓
strategy-formulation
    ↓ one selected thesis + strongest alternative + trade-offs
strategy-challenger
    ↓
strategy-validation
    ↓ SURVIVES / NARROWED
strategic-wedge
    ↓
content-pillars
    ↓
content-opportunity-engine
    ↓
portfolio / experiments / briefs
```

## What makes two strategies different?

At least two consequential dimensions should change:
- where to play;
- how to win;
- economic logic;
- proof mechanism;
- distribution logic;
- resource allocation;
- trade-offs.

Changing topic names, hooks, formats, cadence, or slogans is not enough.

## Non-compensatory hard gates

```text
EVIDENCE_VIABILITY
COMMERCIAL_FIT
CREDIBILITY_PROOF
CAPABILITY_CAPACITY
ETHICAL_LEGAL_FIT
```

A critical fail invalidates the thesis. Scores are sorting aids, not a way to average away fatal weaknesses.

## Coherence contract

Downstream objects preserve `strategic_thesis_id`.

The standard counterfactual test is:

> Would this recommendation remain unchanged if the strongest alternative thesis were selected?

If yes, classify it as generic/weakly linked unless explicitly justified.

## Upstream bridge

`integrations/leadux-competitor-research/skills/strategy-handoff/SKILL.md` is the bridge from the companion Research Agent.

The Strategist does not redo competitor research by default.
