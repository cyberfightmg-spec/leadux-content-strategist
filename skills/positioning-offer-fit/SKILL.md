---
name: positioning-offer-fit
description: >-
  Select which offer and audience should drive content strategy, define a defensible positioning and promise, and reject unsupported differentiation using identity, business context, and verified market evidence.
metadata:
  version: 0.5.0
  category: positioning
  evidence_mode: required
license: MIT
---

# Skill: Positioning / Offer Fit

## Mission
Decide what the brand should primarily sell through content, to whom, with what promise, and why that promise is credible.

This skill sits between context collection/research and content strategy.

```text
identity-profile
+
business-context
+
research-package
→ positioning-offer-fit
→ founder-brand-context
→ content strategy
```

## Absolute rule: no invented differentiation

Never invent:
- an ICP;
- customer pain;
- demand;
- offer priority;
- unique advantage;
- category leadership;
- proof;
- customer result;
- competitor weakness;
- guarantee;
- price/value advantage;
- reason to choose.

If an attractive positioning claim lacks evidence or explicit business truth, mark it `UNSUPPORTED` and either narrow it or request evidence.

## Required inputs
- confirmed `identity-profile` when founder-led;
- confirmed `business-context`;
- verified `research-package` when the decision depends on market/customer/competitor facts;
- first-party proof assets when available.

## Step 1 — Offer eligibility
For every material offer classify:

```text
ACTIVE
PLANNED
EXPERIMENTAL
DEPRIORITIZED
UNAVAILABLE
UNKNOWN
```

Then test:
- is it actually deliverable now?
- is it commercially important now?
- is there a known target audience?
- is the customer outcome stated?
- is there proof or at least credible capability?
- can content realistically create or capture demand for it?

Do not automatically choose the highest-priced, newest, most scalable, or most exciting offer.

## Step 2 — Offer priority
Prioritize offers using visible dimensions, not a hidden score:

- current revenue relevance;
- strategic/future revenue relevance;
- recurring/scalable potential when explicitly stated;
- audience evidence;
- founder/brand credibility;
- proof strength;
- delivery capacity;
- margin/economics only when known;
- market whitespace/differentiation evidence;
- fit with stated goals.

Unknown dimensions remain unknown.

Output:

```text
PRIMARY
SECONDARY
EXPERIMENT
DEFERRED
REJECTED
```

## Step 3 — Audience / problem fit
For each priority offer identify only supported:
- target segment;
- buyer role;
- job/problem;
- desired outcome;
- objections;
- switching trigger;
- current alternatives/substitutes;
- buying situation.

Evidence may come from explicit business context or verified research.

Do not turn broad audience labels into invented personas.

## Step 4 — Promise design
Build candidate promises from:

```text
problem / desired outcome
+
offer capability
+
proof level
+
brand/founder credibility
```

Every promise must be assigned one status:

```text
PROVEN
SUPPORTED
PLAUSIBLE_BUT_UNPROVEN
UNSUPPORTED
```

Rules:
- `PROVEN` requires direct first-party evidence appropriate to the claim;
- `SUPPORTED` may use strong capability + evidence without implying guaranteed outcome;
- `PLAUSIBLE_BUT_UNPROVEN` is allowed only as a hypothesis/test, not as confident marketing copy;
- `UNSUPPORTED` cannot enter the final positioning.

## Step 5 — Differentiation
Evaluate differentiation against real alternatives, including substitutes and DIY/manual options.

Potential differentiation may come from:
- workflow/approach;
- specialization;
- proof;
- speed/process only when evidenced;
- integration capability;
- delivery model;
- business model;
- founder perspective;
- category framing;
- customer experience;
- offer architecture.

Do not use empty claims such as:
- “high quality”;
- “individual approach”;
- “innovative”;
- “best”;
- “AI-powered”;
- “full-cycle”
without concrete meaning and evidence.

## Step 6 — Reason to choose
A valid reason-to-choose must answer:

> Why would this target customer choose this offer instead of the alternatives?

Every answer must cite one or more of:
- business truth;
- identity/capability fact;
- proof asset;
- research claim/insight/VOC;
- verified competitor/substitute gap.

If no defensible answer exists, return `POSITIONING_GAP` instead of inventing one.

## Step 7 — Positioning statement
Produce an internal positioning statement, not necessarily final copy:

```text
For [supported audience / buying situation],
[brand/offer] helps [supported outcome]
by [credible mechanism / capability],
unlike [real alternatives],
because [defensible proof / difference].
```

Do not force every field when evidence is missing. Mark gaps.

## Step 8 — Message boundaries
Define:
- claims allowed;
- claims requiring qualification;
- claims forbidden until evidence exists;
- topics that strengthen positioning;
- topics that dilute positioning;
- secondary offers that must not dominate the narrative.

## Step 9 — Conflict handling
Surface rather than resolve silently:
- service revenue vs scalable/passive product priority;
- broad expertise vs narrow market positioning;
- audience with demand vs audience founder does not want to serve;
- strong market opportunity vs weak brand proof;
- strong founder capability vs weak buyer demand evidence.

Ask the user when the conflict changes strategic priority.

## Output
Produce one object conforming to:

`schemas/positioning-offer-fit.schema.json`

Also output:
- `primary_offer_ids`;
- `secondary_offer_ids`;
- `deferred_offer_ids`;
- `priority_audiences`;
- `supported_promises`;
- `positioning_statement`;
- `reasons_to_choose`;
- `proof_assets`;
- `allowed_claims`;
- `forbidden_claims`;
- `positioning_gaps`;
- `research_requests`;
- `questions_required_from_user`;
- `safe_for_strategy`.

## Quality gate
A full content strategy should not proceed as `READY` when:
- no primary offer or strategic commercial focus exists;
- the primary audience is unknown;
- the main promise is unsupported;
- the reason-to-choose is invented;
- a central positioning conflict remains unresolved.
