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

This repository does **not** generate random ideas and does **not** write final posts by default.

It makes content-strategy decisions from distinct evidence layers:

1. **Identity** — self-stated/confirmed founder identity, expertise, values and public boundaries when founder-led.
2. **Business Context** — what the business actually sells, current goals, revenue model, resources and constraints.
3. **Market evidence** — verified competitor/customer/VOC/GTM/signals from LeadUX Competitor Research.
4. **Audience / ICP Fit** — separates who consumes content from who has the problem, uses, buys, decides, influences, and actually fits the business commercially.
5. **Customer Journey / Funnel Intent** — maps supported roles to decision states, objections, trust/proof needs, triggers, next decisions and CTA boundaries without equating engagement with purchase intent.
6. **Positioning / Offer Fit** — which offer to prioritize, which approved ICP/problem is supported, what promise is defensible, and why the customer should choose it.
7. **Founder/Brand Context** — the merged strategy context used downstream.
8. **Validated Strategy Patterns** — mechanisms adapted from researched open-source strategy systems, with explicit evidence grades and limitations.
9. **First-party learning** — the brand's own historical content and performance patterns.

The goal is not “what content is popular?” but:

```text
What should THIS business say and do,
for THIS supported audience role,
at THIS supported decision state,
around THIS priority offer,
with THIS defensible promise,
based on THIS evidence,
and what should it deliberately not claim or pursue?
```

## v0.7 highlights

- new first-class `customer-journey-intent` skill between Audience / ICP Fit and Positioning / Offer Fit;
- explicit journey states from `UNAWARE` through `PURCHASE_READY`, onboarding, adoption, retention/expansion and advocacy;
- journey state and buying role are modeled as separate axes;
- engagement is never treated as purchase intent by default;
- TOFU/MOFU/BOFU cannot substitute for evidence-backed customer-state reasoning;
- objections, trust needs, proof needs, triggers and switching friction remain evidence-bound;
- CTA strength must match supported intent;
- non-linear and unknown journeys are allowed;
- positioning, Founder/Brand Context, strategy intake and quality gates now consume journey evidence;
- CLI schema inference and tests cover Customer Journey / Funnel Intent objects.

## Core strategy flow

```text
identity-unpacking
→ business-context
→ research handoff
→ strategy-intake
→ audience-icp-fit
→ customer-journey-intent
→ positioning-offer-fit
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
leadux-strategist validate examples/research-package.example.json
leadux-strategist preflight --research examples/research-package.example.json
leadux-strategist score examples/content-opportunity.example.json
```

See `docs/CLI.md`, `docs/HANDOFF.md`, `docs/SKILLS.md`, and `docs/STRATEGY_SOURCES.md` for details.
