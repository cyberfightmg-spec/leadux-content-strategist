# LeadUX Content Strategist

Open-source founder-aware, evidence-first strategy layer between market research and content creation.

```text
LeadUX Competitor Research
        ↓ verified market evidence
Founder / Brand Context
        ↓ identity / offers / audiences / proof / constraints
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

It makes content-strategy decisions from four distinct evidence layers:

1. **Market evidence** — verified competitor/customer/VOC/GTM/signals from LeadUX Competitor Research.
2. **Founder/Brand Context** — who the founder is, what the business sells, priority audiences/offers, positioning, proof, channel roles and constraints.
3. **Validated Strategy Patterns** — mechanisms adapted from researched open-source strategy systems, with explicit evidence grades and limitations.
4. **First-party learning** — the brand's own historical content and performance patterns.

The goal is not “what content is popular?” but:

```text
What should THIS founder/brand do,
for THIS audience,
for THIS business objective,
based on THIS evidence,
and what should it deliberately not do?
```

## v0.4 highlights

- `founder-brand-context` is now a first-class strategy skill;
- strict `founder-brand-context.schema.json`;
- public LeadUX founder/brand context example;
- `strategy-pattern-selection` skill;
- evidence-graded reusable strategy pattern library;
- source audit separating adoption from result evidence and independent replication;
- anti-generic and brand-dilution gates;
- explicit credibility-fit and commercial-fit checks;
- external patterns are adapted mechanisms, never automatic tactics;
- first-party evidence may override generic best practice;
- Research Agent ↔ Strategist boundary remains explicit and auditable.

## Core strategy flow

```text
strategy-intake
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
- VOC / strategic signal / content-footprint evidence;
- Founder/Brand Context field;
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
leadux-strategist validate examples/research-package.example.json
leadux-strategist validate examples/founder-brand-context.leadux.example.json
leadux-strategist preflight --research examples/research-package.example.json
leadux-strategist score examples/content-opportunity.example.json
```

See `docs/CLI.md`, `docs/HANDOFF.md`, `docs/SKILLS.md`, and `docs/STRATEGY_SOURCES.md` for details.
