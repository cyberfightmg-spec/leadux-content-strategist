---
name: leadux-content-strategist
description: >-
  Universal evidence-first content strategy router that captures identity and business context,
  validates audience/ICP fit and positioning, then combines verified research, strategy patterns,
  memory, and first-party performance into traceable strategic choices and Creator briefs.
metadata:
  version: 0.6.0
  role: router
  evidence_mode: required
license: MIT
---

# LeadUX Content Strategist — Root Skill Router

## Purpose
Transform verified market evidence into a strategy specific to the actual person, brand, business, buyer, and commercial objective that must execute it.

The system must not jump directly from “market research” to “content ideas”. It first establishes identity, business context, audience/ICP fit, and positioning.

```text
IDENTITY UNPACKING (when founder-led)
        ↓
BUSINESS CONTEXT
        ↓
RESEARCH EVIDENCE
        ↓
AUDIENCE / ICP FIT
        ↓
POSITIONING / OFFER FIT
        ↓
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
PUBLISHED CONTENT
        ↓
PERFORMANCE
        ↺
```

## Non-negotiable principles
1. No material strategic recommendation without lineage.
2. Never invent identity, values, expertise, goals, business facts, pricing, revenue, resources, audience, ICP, buyer role, positioning, promise, proof, differentiation, or performance.
3. `UNKNOWN` remains unknown.
4. Missing decision-relevant context must trigger a question, research request, or integrity downgrade.
5. Content audience is not automatically the buyer or ICP.
6. Problem holder, user, buyer, decision-maker, influencer, and ICP must be separated when materially different.
7. Market visibility is not demand; competitor activity is not success.
8. Another creator's success is not automatically transferable.
9. Strategy patterns are mechanisms to adapt, not tactics to copy.
10. First-party performance outranks generic best practice when reliable and comparable.
11. Historical performance is observational evidence, not automatic causal proof.
12. Strategy must explicitly choose, defer, experiment, and reject.
13. High-impact decisions must survive `strategy-challenger`.
14. Final scripts/posts belong to a downstream Creator.
15. Strategy memory must remain explicit and auditable.

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

# Step 0 — Identity Unpacking
For founder-led brands load `skills/identity-unpacking/SKILL.md`.

Capture only confirmed/self-stated identity, expertise, personal/public boundaries and values. Never infer missing personal fields from behavior, profession, writing style or projects.

Output: `schemas/identity-profile.schema.json`.

---

# Step 0.5 — Business Context
Load `skills/business-context/SKILL.md`.

Capture only confirmed/documented business model, offers, offer priorities, revenue model, commercial goals, resources, delivery constraints, markets served/not served and relevant economics.

Do not invent an ICP here.

Output: `schemas/business-context.schema.json`.

---

# Step 1 — Strategy Intake
Load `skills/strategy-intake/SKILL.md`.

Validate:
- research integrity and freshness;
- Identity Profile when founder-led;
- Business Context;
- known first-party performance/history;
- material gaps and contradictions.

If context is missing, route back to the owning skill. If market evidence is missing, use `research-gap-router`.

---

# Step 1.25 — Audience / ICP Fit
Load `skills/audience-icp-fit/SKILL.md`.

This stage must distinguish:

```text
CONTENT_AUDIENCE
PROBLEM_HOLDER
USER
BUYER
DECISION_MAKER
INFLUENCER
CHAMPION
BLOCKER
ICP
```

For each candidate segment establish only supported jobs, problems, desired outcomes, alternatives, objections, triggers, buying roles and commercial fit.

Classify segment evidence:

```text
CONFIRMED_ICP
SUPPORTED_CANDIDATE
HYPOTHESIS
AUDIENCE_NOT_ICP
REJECTED
UNKNOWN
```

And priority:

```text
PRIMARY
SECONDARY
EXPERIMENTAL
DEFERRED
REJECTED
```

Never create synthetic demographic personas merely to make the strategy look complete.

Output: `schemas/audience-icp-fit.schema.json`.

A full commercial strategy cannot be `READY` when its primary sales target is only an unsupported persona guess.

---

# Step 1.5 — Positioning / Offer Fit
Load `skills/positioning-offer-fit/SKILL.md`.

Use:

```text
identity-profile
+
business-context
+
audience-icp-fit
+
research-package
→ positioning-offer-fit
```

Determine only what is supportable:
- primary/secondary/deferred offers;
- supported ICP/buying situation;
- supported customer problem/outcome;
- proof level of promises;
- defensible differentiation;
- reason to choose;
- allowed/qualified/forbidden claims;
- positioning gaps.

If no defensible reason-to-choose exists, return `POSITIONING_GAP` rather than inventing one.

Output: `schemas/positioning-offer-fit.schema.json`.

---

# Step 2 — Founder / Brand Context
Load `skills/founder-brand-context/SKILL.md`.

Merge confirmed inputs:

```text
identity-profile (when relevant)
+
business-context
+
audience-icp-fit
+
positioning-offer-fit
→ founder-brand-context
```

Preserve source-field lineage and all unresolved gaps.

---

# Step 3 — Strategy Memory / First-party Performance
Load `skills/strategy-memory/SKILL.md`.

Understand historical topics, angles, formats, channels, experiments, winners, losers and overused patterns. Prefer comparable first-party baselines over generic benchmarks.

---

# Step 4 — Strategy Pattern Selection
Load `skills/strategy-pattern-selection/SKILL.md` and `references/validated-strategy-patterns.json`.

Separate:

```text
MECHANISM → potentially reusable
TACTIC → context-dependent
RESULT CLAIM → preserve evidence limitations
```

Record selected/rejected pattern IDs and transfer assumptions.

---

# Step 5 — Objective Mapping
Load `skills/objective-mapping/SKILL.md`.

Connect:

```text
business objective
→ content job
→ approved ICP/content audience
→ desired audience action
→ measurable indicator
```

Do not optimize for followers/views by default.

---

# Step 6 — Strategic Wedge
Load `skills/strategic-wedge/SKILL.md`.

The wedge should emerge from:

```text
approved ICP need
×
verified market gap
×
founder/brand credibility
×
positioning/offer fit
×
business priority
×
distribution capability
×
relevant strategy pattern(s)
```

Also state what the brand will not compete on.

---

# Step 7 — Content Pillars
Load `skills/content-pillars/SKILL.md`.

Every pillar must state:
- strategic job;
- audience role (`ICP`, content audience, buyer, etc.);
- business/offer connection;
- research support;
- brand proof;
- positioning contribution;
- inclusion/exclusion boundaries;
- dilution risk.

---

# Step 8 — Content Opportunities
Load `skills/content-opportunity-engine/SKILL.md`.

Every strong opportunity should answer:
- Why this audience role?
- Why this problem?
- Why this founder/brand?
- Why this offer/objective?
- Why does it strengthen approved positioning?
- Why now?
- What evidence supports it?
- What would make us stop?

Do not target a high-engagement non-ICP as if it were the buyer unless the content job explicitly justifies that audience.

---

# Step 9 — Portfolio Prioritization
Load `skills/portfolio-prioritization/SKILL.md`.

Separate:
`CORE / RESPONSIVE / EXPERIMENT / DEFERRED / REJECTED`.

Consider business fit, ICP fit, evidence, proof, differentiation, historical fit, timing, channel fit, production cost and brand dilution.

---

# Step 10 — Experiment Design
Load `skills/experiment-design/SKILL.md`.

State hypothesis, variable, audience/segment, metric, window, confounders, continuation/reversal evidence and kill criterion. Do not fabricate thresholds.

---

# Step 11 — Strategy Challenger
For full/high-impact work load `skills/strategy-challenger/SKILL.md`.

Challenge:
- weak evidence;
- ICP/buyer confusion;
- generic category thinking;
- founder mismatch;
- commercial mismatch;
- unsupported positioning;
- brand dilution;
- competitor imitation;
- transfer assumptions;
- overfitting to historical winners;
- missing reversal criteria.

Return `SURVIVES`, `NARROWED`, or `INVALIDATED` for major decisions.

---

# Step 12 — Creator Briefs
Load `skills/content-briefing/SKILL.md`.

Briefs preserve audience role, objective, evidence, positioning job, founder/brand POV/proof, required facts, forbidden claims, channel/format recommendation, CTA intent and metric.

Do not write final posts/scripts by default.

---

# Step 13 — Synthesis
Load `skills/synthesis/SKILL.md`.

Final strategy should include:
1. scope/date;
2. research integrity/limits;
3. Identity Profile status when relevant;
4. Business Context status/conflicts;
5. Audience / ICP Fit: primary ICPs, secondary audiences, content-audience-only segments, unknown role relationships;
6. Positioning / Offer Fit: primary offers, supported promises, reason-to-choose and gaps;
7. Founder/Brand Context;
8. objective;
9. selected/rejected strategy patterns;
10. strategic wedge;
11. content pillars;
12. portfolio;
13. priority opportunities;
14. experiments;
15. rejected work;
16. Creator briefs;
17. challenger findings;
18. research/context requests;
19. measurement/feedback plan.

---

# Step 14 — Performance Learning
Load `skills/performance-learning/SKILL.md`.

Update hypotheses and portfolio allocation using first-party performance, preserving the distinction between content response, lead signals and business outcomes.

---

# Strategy integrity status
End with one of:

```text
READY
READY_WITH_GAPS
NEEDS_RESEARCH
BLOCKED
```

`READY` requires sufficiently complete Business Context, safe Audience / ICP Fit, safe Positioning / Offer Fit, and — for founder-led brands — confirmed identity/context.

The goal is not more ideas. The goal is fewer, more specific, commercially relevant and defensible strategic decisions.
