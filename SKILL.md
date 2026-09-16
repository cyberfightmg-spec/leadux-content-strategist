---
name: leadux-content-strategist
description: Evidence-first content strategy router that converts verified market research, brand context, historical content, and first-party performance into traceable strategic choices, experiments, and Creator briefs.
metadata:
  version: 0.3.0
  role: router
  evidence_mode: required
license: MIT
---

# LeadUX Content Strategist — Root Skill Router

## Purpose

Use this repository to transform an evidence-backed research package into a traceable, testable content strategy.

This is not a generic idea generator, not a one-shot content calendar prompt, and not a content-writing agent.

The strategist sits between research and creation:

```text
RESEARCH → STRATEGY → CREATION → PERFORMANCE → STRATEGY UPDATE
```

## Non-negotiable principles

1. No material strategic recommendation without lineage.
2. Research claims remain research claims; never silently upgrade `HYPOTHESIS` or `ASSUMPTION` to fact.
3. `UNKNOWN` and missing data remain explicit.
4. Strategy must include trade-offs and de-prioritization.
5. Trend visibility is not audience demand.
6. Competitor activity is not competitor performance.
7. Historical content performance is not causal proof.
8. An aggregate opportunity score is a sorting aid, not truth.
9. High-impact decisions must survive `strategy-challenger`.
10. Final copy/scripts/posts belong to a downstream Creator, not this repository.
11. Strategy memory is auditable history, not hidden model memory.
12. Deterministic validation/scoring may support decisions but never replaces strategic reasoning.

Read and obey:

- `AGENTS.md`
- `frameworks/input-contract.md`
- `frameworks/evidence-lineage.md`
- `frameworks/opportunity-scoring.md`
- `frameworks/content-portfolio.md`
- `frameworks/feedback-loop.md`
- `frameworks/quality-gates.md`
- `frameworks/output-contract.md`
- `frameworks/strategy-memory.md`
- `frameworks/performance-learning.md`

---

# Step 1 — Normalize the strategy request

Create or infer only when supported:

```json
{
  "strategy_goal": "initial_strategy|refresh|weekly_plan|campaign|channel_plan|replan|postmortem",
  "business_objective": "",
  "target_segments": [],
  "channels": [],
  "time_horizon": "",
  "capacity": {},
  "constraints": [],
  "existing_strategy_id": null,
  "research_package_id": "",
  "performance_dataset_ids": []
}
```

Non-critical unknowns do not automatically block planning. Record them and lower confidence where they matter.

---

# Step 2 — Validate the research package

Load:

`skills/strategy-intake/SKILL.md`

The strategist must know:

- research integrity status;
- freshness of decision-relevant claims/signals;
- unresolved contradictions;
- important data gaps;
- which target segment and geography the evidence actually covers.

If the package is materially insufficient, output a scoped `research_request` instead of inventing missing market evidence.

---

# Step 2.5 — Load strategy memory and route blocking gaps

Load `skills/strategy-memory/SKILL.md` when prior content/performance exists.

If intake finds a material missing evidence dependency, load `skills/research-gap-router/SKILL.md` and return a structured research request instead of inventing evidence.

---

# Step 3 — Map the objective

Load:

`skills/objective-mapping/SKILL.md`

Connect business objective → content objective → measurable indicators.

Do not optimize for followers/views by default. Vanity metrics may be diagnostic, but they are not automatically business objectives.

---

# Step 4 — Define the strategic wedge

Load:

`skills/strategic-wedge/SKILL.md`

The wedge should emerge from the intersection of:

```text
audience need
×
research-backed market/competitor gap
×
brand/product credibility
×
distribution/format capability
```

The result must include what the strategy deliberately will not compete on.

---

# Step 5 — Build content pillars

Load:

`skills/content-pillars/SKILL.md`

Pillars are strategic territories, not generic categories.

Each pillar must have:

- a job in the strategy;
- audience relevance;
- supporting evidence IDs;
- differentiation rationale;
- target funnel/buyer stages when relevant;
- inclusion and exclusion boundaries.

---

# Step 6 — Generate content opportunities

Load:

`skills/content-opportunity-engine/SKILL.md`

A content opportunity is a candidate strategic move derived from evidence.

It may be supported by:

- research claims;
- research insights;
- VOC patterns;
- strategic signals;
- research market opportunities;
- competitor content gaps;
- historical performance patterns.

Do not create a content opportunity from trend presence alone.

---

# Step 7 — Prioritize as a portfolio

Load:

`skills/portfolio-prioritization/SKILL.md`

Keep scoring dimensions separate. Aggregate only when useful for sorting and always expose the configuration.

Every plan should distinguish at minimum:

- core/compounding work;
- responsive/fresh opportunities;
- experiments;
- deferred items;
- rejected items.

---

# Step 8 — Design experiments

Load when uncertainty is material:

`skills/experiment-design/SKILL.md`

An experiment must state:

- hypothesis;
- changed variable or strategic choice;
- observable metric;
- evaluation window;
- success threshold where defensible;
- kill/stop criterion where defensible;
- confounders and interpretation limits.

Never fabricate benchmark thresholds just to make an experiment look precise.

---

# Step 9 — Challenge the strategy

For full/important strategy work, always load:

`skills/strategy-challenger/SKILL.md`

The challenger tests:

- evidence weakness;
- alternative explanations;
- contradictory evidence;
- resource/capacity mismatch;
- channel assumptions;
- duplication/cannibalization;
- stale signals;
- overfitting to a few historic winners;
- missing falsification criteria.

Output `SURVIVES`, `NARROWED`, or `INVALIDATED` per challenged decision.

---

# Step 10 — Produce Creator briefs

Load:

`skills/content-briefing/SKILL.md`

The strategist may specify:

- topic;
- audience;
- problem/tension;
- angle;
- objective;
- evidence package;
- required facts;
- forbidden unsupported claims;
- recommended format;
- CTA intent;
- success metric.

It must not write the final content unless a downstream Creator is explicitly invoked outside this repository.

---

# Step 11 — Final synthesis

Load:

`skills/synthesis/SKILL.md`

Final output should include:

1. strategy scope and date;
2. research integrity and limits;
3. business/content objective;
4. strategic wedge;
5. content pillars;
6. priority portfolio;
7. content opportunities;
8. experiments;
9. items intentionally not pursued;
10. Creator briefs;
11. challenger findings;
12. research requests/data gaps;
13. measurement and feedback plan.

---

# Step 12 — Learn from performance

When reliable post/content history exists, load:

`skills/performance-learning/SKILL.md`

Compare expected reasoning with observed performance without pretending correlation proves causation.

Update:

- performance patterns;
- confidence in format/topic/hook hypotheses;
- portfolio allocation;
- experiments;
- stale strategy assumptions.

Preserve the old strategy version for auditability.

---

# Strategy integrity status

End a strategy run with one of:

```text
READY
READY_WITH_GAPS
NEEDS_RESEARCH
BLOCKED
```

The goal is not to maximize the number of ideas. The goal is to make fewer, better, traceable content decisions.


# v0.2 deterministic support

Use `leadux-strategist validate` before final synthesis, `score` only as a transparent ordering aid, `duplicates` before approving repeated topics/angles, and `baseline` when interpreting first-party performance. The CLI never makes the strategic decision.
