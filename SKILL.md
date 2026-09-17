---
name: leadux-content-strategist
description: >-
  Universal evidence-first content strategy router that captures identity and business context,
  validates audience/ICP fit, customer journey intent, positioning, and channel/distribution fit,
  then combines verified research, strategy patterns, memory, and first-party performance into traceable strategic choices and Creator briefs.
metadata:
  version: 0.8.0
  role: router
  evidence_mode: required
license: MIT
---

# LeadUX Content Strategist — Root Skill Router

## Purpose
Transform verified market evidence into a strategy specific to the actual person, brand, business, buyer, buying state, distribution surface, and commercial objective that must execute it.

The system must not jump directly from market research to content ideas. It first establishes identity, business context, audience/ICP fit, journey intent, positioning, and channel/distribution fit.

```text
IDENTITY UNPACKING (when founder-led)
        ↓
BUSINESS CONTEXT
        ↓
RESEARCH EVIDENCE
        ↓
AUDIENCE / ICP FIT
        ↓
CUSTOMER JOURNEY / FUNNEL INTENT
        ↓
POSITIONING / OFFER FIT
        ↓
CHANNEL / DISTRIBUTION FIT
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
2. Never invent identity, values, expertise, goals, business facts, pricing, revenue, resources, audience, ICP, buying role, journey stage, objection, trigger, positioning, promise, proof, differentiation, channel fit, audience presence, channel ROI, conversion, or performance.
3. `UNKNOWN` remains unknown.
4. Missing decision-relevant context must trigger a question, research request, hypothesis label, or integrity downgrade.
5. Content audience is not automatically the buyer or ICP.
6. Problem holder, user, buyer, decision-maker, influencer, champion, blocker, and ICP must be separated when materially different.
7. Journey state and buying role are separate axes.
8. Channel, journey state, content job, format, desired action, and business outcome are separate concepts.
9. Engagement is not purchase intent, and reach is not revenue.
10. Platform popularity is not channel fit.
11. Market visibility is not demand; competitor activity is not success.
12. Another creator's success is not automatically transferable.
13. Strategy patterns are mechanisms to adapt, not tactics to copy.
14. First-party performance outranks generic best practice when reliable and comparable.
15. Historical performance is observational evidence, not automatic causal proof.
16. Strategy must explicitly choose, defer, experiment, and reject.
17. High-impact decisions must survive `strategy-challenger`.
18. Final scripts/posts belong to a downstream Creator.
19. Strategy memory must remain explicit and auditable.

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

Do not invent an ICP or channel strategy here.

Output: `schemas/business-context.schema.json`.

---

# Step 1 — Strategy Intake
Load `skills/strategy-intake/SKILL.md`.

Validate research integrity/freshness, Identity Profile when founder-led, Business Context, known first-party performance/history, and material gaps/contradictions.

If context is missing, route back to the owning skill. If market evidence is missing, use `research-gap-router`.

---

# Step 1.25 — Audience / ICP Fit
Load `skills/audience-icp-fit/SKILL.md`.

Distinguish:

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

Never create synthetic demographic personas merely to make the strategy look complete.

Output: `schemas/audience-icp-fit.schema.json`.

---

# Step 1.4 — Customer Journey / Funnel Intent
Load `skills/customer-journey-intent/SKILL.md`.

Map supported audiences/ICPs and buying roles to evidence-backed decision states:

```text
UNAWARE
PROBLEM_AWARE
SOLUTION_AWARE
CATEGORY_EXPLORING
VENDOR_COMPARING
TRUST_VALIDATING
PURCHASE_READY
CUSTOMER_ONBOARDING
CUSTOMER_ADOPTION
RETENTION_EXPANSION
ADVOCACY
UNKNOWN
```

Do not infer stage from platform engagement, demographics, or generic TOFU/MOFU/BOFU assumptions.

For each material role/state capture only supported current question/decision, objections, perceived risks, trust/proof requirements, triggers, switching friction, appropriate content jobs, desired next action, and CTA strength.

Output: `schemas/customer-journey-intent.schema.json`.

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
customer-journey-intent
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

# Step 1.75 — Channel / Distribution Fit
Load `skills/channel-distribution-fit/SKILL.md`.

Use:

```text
audience-icp-fit
+
customer-journey-intent
+
positioning-offer-fit
+
business-context
+
research-package
+
first-party channel performance (when available)
→ channel-distribution-fit
```

For each candidate channel determine only what is supported or explicitly experimental:
- which segment/role it serves;
- which journey state(s) it serves;
- its primary distribution/content job;
- channel evidence status;
- appropriate formats;
- desired next actions and CTA strength;
- operational fit and production burden;
- owned/rented/earned/paid role;
- measurement by distribution, audience-response, lead, and business-outcome levels;
- whether the channel is `PRIMARY`, `SECONDARY`, `REPURPOSE_ONLY`, `EXPERIMENTAL`, `DEFERRED`, or `REJECTED`.

Do not recommend a platform merely because competitors use it, because it is popular, or because it can generate reach.

Do not equate views, followers, comments, or watch time with leads or revenue.

Output: `schemas/channel-distribution-fit.schema.json`.

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
customer-journey-intent
+
positioning-offer-fit
+
channel-distribution-fit
→ founder-brand-context
```

Preserve source-field lineage and unresolved gaps.

---

# Step 3 — Strategy Memory / First-party Performance
Load `skills/strategy-memory/SKILL.md`.

Understand historical topics, angles, formats, channels, experiments, winners, losers and overused patterns. Prefer comparable first-party baselines over generic benchmarks.

---

# Step 4 — Strategy Pattern Selection
Load `skills/strategy-pattern-selection/SKILL.md` and `references/validated-strategy-patterns.json`.

Separate reusable mechanism, context-dependent tactic, and claimed result. Record selected/rejected pattern IDs and transfer assumptions.

---

# Step 5 — Objective Mapping
Load `skills/objective-mapping/SKILL.md`.

Connect:

```text
business objective
→ content job
→ approved ICP/content audience
→ journey state / next decision
→ approved channel role
→ desired audience action
→ measurable indicator
```

Do not optimize for followers/views by default.

---

# Step 6 — Strategic Wedge
Load `skills/strategic-wedge/SKILL.md`.

The wedge should emerge from approved ICP need × verified market gap × founder/brand credibility × positioning/offer fit × business priority × verified distribution capability × relevant strategy patterns.

Also state what the brand will not compete on.

---

# Step 7 — Content Pillars
Load `skills/content-pillars/SKILL.md`.

Every pillar must state strategic job, audience role, relevant journey state(s), business/offer connection, research support, brand proof, positioning contribution, suitable channel roles, inclusion/exclusion boundaries, and dilution risk.

---

# Step 8 — Content Opportunities
Load `skills/content-opportunity-engine/SKILL.md`.

Every strong opportunity should answer:
- Why this audience role?
- Why this journey state / next decision?
- Why this problem?
- Why this founder/brand?
- Why this offer/objective?
- Why does it strengthen approved positioning?
- Why this channel role?
- Why this format on this channel?
- Why now?
- What evidence supports it?
- What would make us stop?

Do not target a high-engagement non-ICP as if it were the buyer unless the content job explicitly justifies that audience.

---

# Step 9 — Portfolio Prioritization
Load `skills/portfolio-prioritization/SKILL.md`.

Separate `CORE / RESPONSIVE / EXPERIMENT / DEFERRED / REJECTED`.

Consider business fit, ICP fit, journey coverage, evidence, proof, differentiation, historical fit, timing, channel fit, distribution dependency, production cost and brand dilution.

---

# Step 10 — Experiment Design
Load `skills/experiment-design/SKILL.md`.

State hypothesis, variable, audience/segment, journey state, channel, format, metric, window, confounders, continuation/reversal evidence and kill criterion. Do not fabricate thresholds.

---

# Step 11 — Strategy Challenger
For full/high-impact work load `skills/strategy-challenger/SKILL.md`.

Challenge weak evidence, ICP/buyer confusion, journey-stage guessing, engagement-as-intent assumptions, platform-popularity assumptions, channel-capacity mismatch, reach-as-business-outcome claims, generic category thinking, founder mismatch, commercial mismatch, unsupported positioning, brand dilution, competitor imitation, transfer assumptions, overfitting, and missing reversal criteria.

Return `SURVIVES`, `NARROWED`, or `INVALIDATED` for major decisions.

---

# Step 12 — Creator Briefs
Load `skills/content-briefing/SKILL.md`.

Briefs preserve audience role, journey state, next decision, content job, objective, evidence, positioning job, founder/brand POV/proof, approved channel role, channel-specific format, required facts, forbidden claims, CTA strength/intent, and metric.

Do not write final posts/scripts by default.

---

# Step 13 — Synthesis
Load `skills/synthesis/SKILL.md`.

Final strategy should include:
1. scope/date;
2. research integrity/limits;
3. Identity Profile status when relevant;
4. Business Context status/conflicts;
5. Audience / ICP Fit;
6. Customer Journey / Funnel Intent;
7. Positioning / Offer Fit;
8. Channel / Distribution Fit: primary/secondary/experimental/deferred channels, jobs, audience-state mapping, owned/rented roles, repurposing graph and measurement limits;
9. Founder/Brand Context;
10. objective;
11. selected/rejected strategy patterns;
12. strategic wedge;
13. content pillars;
14. portfolio;
15. priority opportunities;
16. experiments;
17. rejected work;
18. Creator briefs;
19. challenger findings;
20. research/context requests;
21. measurement/feedback plan.

---

# Step 14 — Performance Learning
Load `skills/performance-learning/SKILL.md`.

Update hypotheses and portfolio allocation using first-party performance, preserving distinctions among distribution signals, audience response, journey progression, lead signals and business outcomes.

---

# Strategy integrity status
End with one of:

```text
READY
READY_WITH_GAPS
NEEDS_RESEARCH
BLOCKED
```

`READY` requires sufficiently complete Business Context, safe Audience / ICP Fit, journey assumptions appropriate to the decisions being made, safe Positioning / Offer Fit, safe Channel / Distribution Fit, and — for founder-led brands — confirmed identity/context.

The goal is not more ideas or more channels. The goal is fewer, more specific, commercially relevant and defensible strategic decisions distributed through channels that have a clear job and a supportable reason to exist.
