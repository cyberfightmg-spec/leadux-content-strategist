# LeadUX Content Strategist

Open-source universal, founder-aware, evidence-first strategy layer between market research and content creation.

```text
Identity Unpacking (when founder-led)
        ↓ confirmed identity
Business Context
        ↓ confirmed commercial reality
LeadUX Competitor Research
        ↓ verified market evidence
Positioning / Offer Fit
        ↓ supported offer / audience / promise / reason-to-choose
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
2. **Business Context** — what the business actually sells, to whom, current goals, revenue model, resources and constraints.
3. **Market evidence** — verified competitor/customer/VOC/GTM/signals from LeadUX Competitor Research.
4. **Positioning / Offer Fit** — which offer to prioritize, which audience/problem is supported, what promise is defensible, and why the customer should choose it.
5. **Founder/Brand Context** — the merged strategy context used downstream.
6. **Validated Strategy Patterns** — mechanisms adapted from researched open-source strategy systems, with explicit evidence grades and limitations.
7. **First-party learning** — the brand's own historical content and performance patterns.

The goal is not “what content is popular?” but:

```text
What should THIS business say and do,
for THIS supported audience,
around THIS priority offer,
with THIS defensible promise,
based on THIS evidence,
and what should it deliberately not claim or pursue?
```

## v0.5 highlights

- universal `identity-unpacking` skill with strict no-inference protocol;
- universal `business-context` skill with commercial conflict handling;
- new `positioning-offer-fit` skill;
- strict `positioning-offer-fit.schema.json`;
- offer statuses: PRIMARY / SECONDARY / EXPERIMENT / DEFERRED / REJECTED;
- promise statuses: PROVEN / SUPPORTED / PLAUSIBLE_BUT_UNPROVEN / UNSUPPORTED;
- defensible reason-to-choose or explicit `POSITIONING_GAP`;
- allowed / qualified / forbidden claim boundaries;
- Founder/Brand Context now merges identity + business + safe positioning/offer-fit;
- strategy intake blocks `READY` when the main promise or differentiation is unsupported;
- first-party evidence and verified market evidence remain separate from generic best practices.

## Core strategy flow

```text
identity-unpacking
→ business-context
→ research handoff
→ strategy-intake
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
leadux-strategist validate examples/positioning-offer-fit.example.json
leadux-strategist validate examples/research-package.example.json
leadux-strategist preflight --research examples/research-package.example.json
leadux-strategist score examples/content-opportunity.example.json
```

See `docs/CLI.md`, `docs/HANDOFF.md`, `docs/SKILLS.md`, and `docs/STRATEGY_SOURCES.md` for details.
