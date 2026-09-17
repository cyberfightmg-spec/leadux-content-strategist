# LeadUX Content Strategist

Open-source universal, founder-aware, evidence-first strategy layer between market research and content creation.

```text
Identity Unpacking (when founder-led)
        ↓ confirmed identity
Business Context
        ↓ confirmed commercial reality
LeadUX Competitor Research
        ↓ verified market evidence
Audience / ICP Fit
        ↓ content audience / user / buyer / decision-maker / ICP map
Customer Journey / Funnel Intent
        ↓ supported decision states / objections / proof needs / CTA boundaries
Positioning / Offer Fit
        ↓ supported offer / ICP / promise / reason-to-choose
Channel / Distribution Fit
        ↓ supported channel roles / formats / repurposing / measurement boundaries
Founder / Brand Context
        ↓ strategy-safe context
Validated Strategy Patterns
        ↓ reusable mechanisms with evidence grades
Strategy Memory + First-party Performance
        ↓ historical winners / losers / experiments
LeadUX Content Strategist
        ↓ strategy / portfolio / experiments / briefs
Creator
        ↓ published content
Performance observations
        └──────────────→ strategy memory / refresh
```

## What it is

This repository does **not** generate random ideas, does **not** recommend platforms merely because they are popular, and does **not** write final posts by default.

It makes content-strategy decisions from distinct evidence layers:

1. **Identity** — self-stated/confirmed founder identity, expertise, values and public boundaries when founder-led.
2. **Business Context** — what the business actually sells, current goals, revenue model, resources and constraints.
3. **Market evidence** — verified competitor/customer/VOC/GTM/signals from LeadUX Competitor Research.
4. **Audience / ICP Fit** — separates who consumes content from who has the problem, uses, buys, decides, influences, and actually fits the business commercially.
5. **Customer Journey / Funnel Intent** — maps supported roles to decision states, objections, trust/proof needs, triggers, next decisions and CTA boundaries without equating engagement with purchase intent.
6. **Positioning / Offer Fit** — which offer to prioritize, which approved ICP/problem is supported, what promise is defensible, and why the customer should choose it.
7. **Channel / Distribution Fit** — decides where content should be distributed, what job each channel performs, what format fits, and whether the business can execute it sustainably.
8. **Founder/Brand Context** — merged strategy context used downstream.
9. **Validated Strategy Patterns** — mechanisms adapted from researched open-source strategy systems, with explicit evidence grades and limitations.
10. **First-party learning** — the brand's own historical content and performance patterns.

The goal is not “what content is popular?” but:

```text
What should THIS business say and do,
for THIS supported audience role,
at THIS supported decision state,
around THIS priority offer,
on THIS supportable distribution surface,
with THIS defensible promise,
based on THIS evidence,
and what should it deliberately not claim or pursue?
```

## v0.8 highlights

- new first-class `channel-distribution-fit` skill after Positioning / Offer Fit;
- channel families cover owned site, search, email, messaging, social, short/long video, communities, marketplaces/directories, partners, PR, paid, outbound and events;
- channel evidence states: `CONFIRMED_FIT`, `SUPPORTED_FIT`, `HYPOTHESIS`, `INSUFFICIENT_EVIDENCE`, `REJECTED`;
- channel priorities: `PRIMARY`, `SECONDARY`, `REPURPOSE_ONLY`, `EXPERIMENTAL`, `DEFERRED`, `REJECTED`;
- explicit separation of WHO / STATE / JOB / WHERE / FORMAT / ACTION / OUTCOME;
- platform popularity and competitor presence do not prove fit;
- views/reach/engagement are not leads or revenue by default;
- owned vs rented distribution is modeled explicitly;
- repurposing graph preserves strategic intent while adapting packaging per channel;
- operational capacity, response burden, budget and compliance are part of channel selection;
- Creator briefs now preserve approved channel role, format adaptation, CTA and measurement level;
- CLI schema inference and tests cover Channel / Distribution Fit objects.

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
→ strategic-wedge
→ content-pillars
→ content-opportunity-engine
→ portfolio-prioritization
→ experiment-design
→ strategy-challenger
→ content-briefing
→ synthesis
        ↺ performance-learning
```

## Evidence lineage

Every material opportunity or decision should be traceable to one or more of:

- research `claim_id` / `insight_id` / `market_opportunity_id`;
- VOC / strategic signal / content-performance evidence;
- Identity Profile field;
- Business Context field;
- Audience / ICP Fit segment/role/evidence status;
- Customer Journey / Funnel Intent path/state/confidence;
- Positioning / Offer Fit object;
- Channel / Distribution Fit channel/evidence/job mapping;
- first-party `performance_pattern_id`;
- validated `pattern_id`;
- explicit business constraint.

## External pattern evidence

See:

- `references/validated-strategy-patterns.json`
- `docs/STRATEGY_SOURCES.md`

GitHub stars, installs or one creator's result are not treated as business proof. The repository explicitly distinguishes adoption, independent usage, author-reported results and independent replication.

## Install

```bash
pip install -e '.[dev]'
pytest
```

## Quick start

```bash
leadux-strategist validate examples/business-context.example.json
leadux-strategist validate examples/audience-icp-fit.example.json
leadux-strategist validate examples/customer-journey-intent.example.json
leadux-strategist validate examples/positioning-offer-fit.example.json
leadux-strategist validate examples/channel-distribution-fit.example.json
leadux-strategist validate examples/research-package.example.json
leadux-strategist preflight --research examples/research-package.example.json
leadux-strategist score examples/content-opportunity.example.json
```

See `docs/CLI.md`, `docs/HANDOFF.md`, `docs/SKILLS.md`, and `docs/STRATEGY_SOURCES.md` for details.
