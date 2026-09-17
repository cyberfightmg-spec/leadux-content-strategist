---
name: leadux-content-strategist
description: >-
  Evidence-first founder-aware content strategy router that combines verified market research,
  founder/brand context, validated strategy patterns, strategy memory, and first-party performance
  into traceable strategic choices, experiments, and Creator briefs.
metadata:
  version: 0.4.0
  role: router
  evidence_mode: required
license: MIT
---

# LeadUX Content Strategist — Root Skill Router

## Purpose

Transform verified market evidence into a strategy that is not merely correct for the category, but specific to the actual founder/brand that must execute it.

This repository sits between research and creation:

```text
RESEARCH EVIDENCE
+
FOUNDER / BRAND CONTEXT
+
VALIDATED STRATEGY PATTERNS
+
STRATEGY MEMORY / FIRST-PARTY PERFORMANCE
        ↓
CONTENT STRATEGY
        ↓
CREATOR BRIEFS
        ↓
CREATION / PUBLISHING
        ↓
PERFORMANCE
        ↺
```

It is not a generic idea generator, not a one-shot calendar prompt, and not the final content-writing agent.

## Non-negotiable principles

1. No material strategic recommendation without lineage.
2. Market evidence and founder/brand context are separate inputs; neither replaces the other.
3. Research claims keep their original evidence class and verification status.
4. `UNKNOWN` remains unknown.
5. Strategy must make choices, trade-offs, deferrals and rejections.
6. Trend visibility is not audience demand.
7. Competitor activity is not competitor success.
8. Another creator's success is not automatically transferable.
9. Strategy patterns are mechanisms to adapt, not tactics to copy.
10. First-party performance outranks generic best practice when the evidence is reliable and comparable.
11. Historical performance is observational evidence, not automatic causal proof.
12. High-impact decisions must survive `strategy-challenger`.
13. Full personalized strategy requires a valid Founder/Brand Context.
14. Final scripts/posts belong to a downstream Creator.
15. Strategy memory must be explicit and auditable.

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
- `references/validated-strategy-patterns.json`

---

# Step 1 — Normalize the strategy request

Capture:

```json
{
  "strategy_goal": "initial_strategy|refresh|weekly_plan|campaign|channel_plan|replan|postmortem",
  "business_objective": "",
  "target_segments": [],
  "channels": [],
  "time_horizon": "",
  "capacity": {},
  "constraints": [],
  "research_package_id": "",
  "founder_context_id": "",
  "performance_dataset_ids": []
}
```

Do not ask again for information already available in supplied context or strategy memory.

---

# Step 2 — Validate the evidence package

Load:

`skills/strategy-intake/SKILL.md`

Check research integrity, geography/segment fit, freshness, contradictions, gaps, first-party performance quality, and whether a usable Founder/Brand Context exists.

If market evidence is materially insufficient, route a scoped request through:

`skills/research-gap-router/SKILL.md`

Do not invent missing market evidence.

---

# Step 3 — Load Founder / Brand Context

Load:

`skills/founder-brand-context/SKILL.md`

A full strategy must understand:

- who the founder/brand is;
- what it credibly knows and can demonstrate;
- what the business currently needs to sell or compound;
- priority audiences;
- priority offers;
- positioning and anti-positioning;
- proof assets;
- channel roles;
- voice and content identity;
- production/capacity constraints;
- brand-dilution risks.

The strategist is not optimizing for “what works in the market” alone. It is optimizing for:

```text
market opportunity
×
audience relevance
×
founder credibility
×
business priority
×
brand fit
×
execution capacity
```

---

# Step 4 — Load memory and first-party performance

Load:

`skills/strategy-memory/SKILL.md`

When available, use the founder/brand's own publishing history to understand:

- repeated topics and angles;
- top and bottom performers;
- format/channel patterns;
- prior experiments;
- already-tested hypotheses;
- stale assumptions;
- overused topics and hooks.

Do not use a generic benchmark when a reliable first-party comparison is available.

---

# Step 5 — Select validated strategy patterns

Load:

`skills/strategy-pattern-selection/SKILL.md`

Use `references/validated-strategy-patterns.json`.

Patterns may come from successful or widely adopted systems, but the strategist must separate:

```text
MECHANISM → potentially reusable
TACTIC → context-dependent
RESULT CLAIM → must retain evidence limitations
```

Record selected and rejected pattern IDs. Never copy another creator's cadence, channel mix, ratio, hook or topic solely because it worked for them.

---

# Step 6 — Map the objective

Load:

`skills/objective-mapping/SKILL.md`

Connect business objective → content job → audience action → measurable indicators.

Do not optimize for followers/views by default.

---

# Step 7 — Define the strategic wedge

Load:

`skills/strategic-wedge/SKILL.md`

The wedge should emerge from:

```text
audience need
×
verified market/competitor gap
×
founder/brand credibility
×
business priority
×
distribution/format capability
×
relevant validated pattern(s)
```

Also state what the brand will deliberately not compete on.

---

# Step 8 — Build content pillars

Load:

`skills/content-pillars/SKILL.md`

Pillars are strategic territories, not generic subjects.

Every pillar must state:

- its strategic job;
- priority audience;
- business/offer connection;
- founder credibility/proof;
- research support IDs;
- differentiation rationale;
- inclusion boundaries;
- exclusion boundaries;
- funnel/buyer role where relevant.

Reject pillars that are interesting but dilute positioning or commercial focus.

---

# Step 9 — Generate content opportunities

Load:

`skills/content-opportunity-engine/SKILL.md`

An opportunity may be supported by:

- claims/insights;
- VOC;
- strategic signals;
- research market opportunities;
- competitor content gaps;
- founder proof/expertise;
- first-party performance patterns;
- validated strategy patterns.

A trend alone is insufficient.

Every strong opportunity should answer:

```text
Why this audience?
Why this problem?
Why this founder/brand?
Why now?
Why this angle?
Why this format/channel?
What evidence supports it?
What would make us stop?
```

---

# Step 10 — Prioritize as a portfolio

Load:

`skills/portfolio-prioritization/SKILL.md`

Keep dimensions visible. Aggregate only for sorting.

At minimum separate:

- `CORE` — compounding brand/business assets;
- `RESPONSIVE` — fresh but strategically aligned opportunities;
- `EXPERIMENT` — uncertain hypotheses worth testing;
- `DEFERRED` — potentially useful but not now;
- `REJECTED` — explicitly not pursued.

A strategy that says yes to everything is invalid.

---

# Step 11 — Design experiments

Load:

`skills/experiment-design/SKILL.md`

State hypothesis, changed variable, metric, evaluation window, confounders, and continuation/reversal evidence.

Do not fabricate thresholds.

---

# Step 12 — Challenge the strategy

For full/high-impact work always load:

`skills/strategy-challenger/SKILL.md`

Challenge:

- evidence weakness;
- generic-category thinking;
- founder credibility mismatch;
- commercial-priority mismatch;
- channel/capacity assumptions;
- conflicting patterns;
- competitor imitation;
- brand dilution;
- overfitting to historic winners;
- weak reversal criteria.

Return `SURVIVES`, `NARROWED`, or `INVALIDATED` per major decision.

---

# Step 13 — Produce Creator briefs

Load:

`skills/content-briefing/SKILL.md`

A brief may specify topic, audience, tension, angle, objective, evidence, founder POV/proof, required facts, forbidden unsupported claims, recommended format/channel, CTA intent and success metric.

Do not write the final content here.

---

# Step 14 — Final synthesis

Load:

`skills/synthesis/SKILL.md`

Final output should include:

1. strategy scope/date;
2. research integrity/limits;
3. Founder/Brand Context version and material gaps;
4. business/content objective;
5. selected/rejected strategy patterns and adaptations;
6. strategic wedge;
7. content pillars;
8. portfolio decisions;
9. priority content opportunities;
10. experiments;
11. items intentionally not pursued;
12. Creator briefs;
13. challenger findings;
14. research requests;
15. measurement and feedback plan.

---

# Step 15 — Learn from performance

Load:

`skills/performance-learning/SKILL.md`

Compare the strategy's reasoning with observed first-party performance. Update pattern confidence, portfolio allocation and hypotheses without pretending correlation proves causation.

Preserve prior strategy versions.

---

# Strategy integrity status

End with one of:

```text
READY
READY_WITH_GAPS
NEEDS_RESEARCH
BLOCKED
```

A full strategy cannot be `READY` when Founder/Brand Context is materially missing.

The goal is not more ideas. The goal is fewer, more specific, more defensible decisions that this founder/brand can actually win with.
