---
name: strategy-diagnosis
description: >-
  Compress verified research, business context, audience, journey, positioning, distribution,
  objectives, and first-party learning into the few decision tensions that actually matter before
  strategic options are generated.
metadata:
  version: 0.9.0
  category: strategy-formulation
  evidence_mode: required
license: MIT
---

# Skill: Strategy Diagnosis

## Mission
Turn a large evidence package into a **decision diagnosis**.

Diagnosis is not a content plan and not a list of recommendations. It answers:

> What is the strategic situation, what tensions matter, what is constrained, what is still uncertain,
> and what choices must the strategy resolve?

Use:

```text
research-package
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
+
founder-brand-context
+
objective-mapping
+
strategy-memory / first-party performance
+
selected strategy patterns
→ strategy-diagnosis
```

Output conforms to `schemas/strategy-diagnosis.schema.json`.

## Absolute rules

1. Do not generate the strategy yet.
2. Do not convert weak evidence into a recommendation.
3. Do not hide contradictions for narrative neatness.
4. Do not make every observation "strategic"; compress to what changes a decision.
5. Unknown remains `UNKNOWN`.
6. A competitor pattern is not automatically an opportunity.
7. First-party performance is observational evidence unless causality was actually tested.
8. Separate a fact from the interpretation of why it matters.

## Step 1 — State the decision to be made

Write one decision statement:

```text
Given [current situation and constraints],
what strategic approach should [brand/business]
use to achieve [primary objective]
for [priority audience/buying situation]
within [time/capacity constraints]?
```

If this cannot be stated cleanly, return a gap rather than continuing.

## Step 2 — Extract decisive evidence

Keep only evidence that can change the strategic choice.

Classify:
- `DECISIVE_FACT` — materially changes viable options;
- `CONSTRAINT` — rules out or limits options;
- `TENSION` — two desirable things cannot both be maximized;
- `OPPORTUNITY_SIGNAL` — evidence suggests a potentially attractive direction;
- `RISK` — could make an otherwise attractive choice fail;
- `UNCERTAINTY` — important unknown requiring an experiment, question, or research request.

Each item must preserve evidence/source IDs.

## Step 3 — Identify strategic tensions

A useful diagnosis surfaces trade-offs such as:

```text
broad audience vs narrow commercial fit
reach vs buyer quality
services revenue vs scalable recurring revenue
fast execution vs proof quality
category familiarity vs differentiation
founder credibility vs market attractiveness
one-channel depth vs multi-channel coverage
short-term demand capture vs long-term category creation
```

Do not invent a tension merely because strategy frameworks commonly contain one.

## Step 4 — Identify capability and proof constraints

Explicitly record:
- what the business can repeatedly execute;
- what it can credibly prove;
- what it cannot currently prove;
- where capacity creates a hard ceiling;
- where compliance/ethics create a hard boundary.

## Step 5 — Define choice questions

End diagnosis with 2–5 questions that the strategic options must answer differently.

Examples:
- Which audience/problem receives scarce attention first?
- Do we compete by demand capture, demand creation, or a deliberate combination?
- Is the primary economic path service revenue, recurring revenue, or audience asset creation?
- Which proof mechanism is strong enough to support the promise?
- Which channel role is essential and which is merely optional?

## Step 6 — Decide readiness

Use:
- `READY_FOR_FORMULATION`
- `READY_WITH_UNCERTAINTY`
- `NEEDS_INPUT`
- `BLOCKED`

A diagnosis may proceed with uncertainty only when the uncertainty can be represented as an explicit strategic bet or experiment.

## Quality bar

A strong diagnosis:
- is shorter than the input evidence;
- makes the real conflict visible;
- does not prematurely choose a solution;
- distinguishes constraints from preferences;
- names important unknowns;
- produces choice questions that can generate materially different strategies.

If the diagnosis simply restates the research package, it failed.
