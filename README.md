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
5. **Positioning / Offer Fit** — which offer to prioritize, which approved ICP/problem is supported, what promise is defensible, and why the customer should choose it.
6. **Founder/Brand Context** — the merged strategy context used downstream.
7. **Validated Strategy Patterns** — mechanisms adapted from researched open-source strategy systems, with explicit evidence grades and limitations.
8. **First-party learning** — the brand's own historical content and performance patterns.

The goal is not “what content is popular?” but:

```text
What should THIS business say and do,
for THIS supported ICP or content audience,
around THIS priority offer,
with THIS defensible promise,
based on THIS evidence,
and what should it deliberately not claim or pursue?
```

## v0.6 highlights

- new first-class `audience-icp-fit` skill before positioning;
- strict separation of `CONTENT_AUDIENCE`, `PROBLEM_HOLDER`, `USER`, `BUYER`, `DECISION_MAKER`, `INFLUENCER`, `CHAMPION`, `BLOCKER`, and `ICP`;
- segment evidence states: `CONFIRMED_ICP`, `SUPPORTED_CANDIDATE`, `HYPOTHESIS`, `AUDIENCE_NOT_ICP`, `REJECTED`, `UNKNOWN`;
- no fabricated demographic personas;
- content audience may be useful for reach/community without becoming a sales ICP;
- positioning now consumes approved Audience / ICP Fit instead of inventing audience roles;
- strategy intake and quality gates block `READY` when the primary ICP is unsupported;
- Founder/Brand Context preserves buyer-role relationships and audience-only segments;
- CLI schema inference and tests cover Audience / ICP Fit objects.

## Core strategy flow

```text
identity-unpacking
→ business-context
→ research handoff
→ strategy-intake
→ audience-icp-fit
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
leadux-strategist validate examples/positioning-offer-fit.example.json
leadux-strategist validate examples/research-package.example.json
leadux-strategist preflight --research examples/research-package.example.json
leadux-strategist score examples/content-opportunity.example.json
```

See `docs/CLI.md`, `docs/HANDOFF.md`, `docs/SKILLS.md`, and `docs/STRATEGY_SOURCES.md` for details.
