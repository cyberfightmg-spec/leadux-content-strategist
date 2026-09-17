---
name: positioning-offer-fit
description: >-
  Select which offer should drive strategy and define a defensible promise and positioning using confirmed identity, business context, audience/ICP fit, and verified market evidence.
metadata:
  version: 0.6.0
  category: positioning
  evidence_mode: required
license: MIT
---

# Skill: Positioning / Offer Fit

## Mission
Decide what the brand should primarily sell through content, to whom, with what promise, and why that promise is credible.

```text
identity-profile
+
business-context
+
audience-icp-fit
+
research-package
→ positioning-offer-fit
→ founder-brand-context
→ content strategy
```

## Absolute rule: no invented differentiation
Never invent an ICP, pain, demand, offer priority, unique advantage, category leadership, proof, result, competitor weakness, guarantee, price/value advantage, or reason to choose.

If an attractive positioning claim lacks evidence or explicit business truth, mark it `UNSUPPORTED`, narrow it, or request evidence.

## Required inputs
- confirmed `identity-profile` when founder-led;
- confirmed `business-context`;
- `audience-icp-fit`;
- verified `research-package` when market/customer/competitor facts matter;
- first-party proof assets when available.

## Audience rule
Use `audience-icp-fit` as the source of truth for segment role and ICP status.

Do not collapse:
- content audience;
- user;
- problem holder;
- buyer;
- decision-maker;
- influencer;
- ICP.

If a content audience is explicitly `AUDIENCE_NOT_ICP`, it may still support reach/community strategy but cannot silently become the primary sales target.

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

Then test deliverability, commercial importance, ICP fit, customer outcome, proof/capability, and whether content can realistically create or capture demand.

## Step 2 — Offer priority
Prioritize using visible dimensions:
- current revenue relevance;
- strategic/future revenue relevance;
- recurring/scalable potential when stated;
- ICP evidence;
- founder/brand credibility;
- proof strength;
- delivery capacity;
- known economics;
- whitespace/differentiation evidence;
- fit with stated goals.

Unknown remains unknown.

Classify:
`PRIMARY / SECONDARY / EXPERIMENT / DEFERRED / REJECTED`.

## Step 3 — Audience / problem fit
For each priority offer use only supported segment information from `audience-icp-fit` and research:
- segment;
- problem holder;
- buyer/decision-maker when relevant;
- job/problem;
- desired outcome;
- objections;
- switching trigger;
- alternatives;
- buying situation.

Do not fabricate personas.

## Step 4 — Promise design
Build candidate promises from:

```text
supported problem / desired outcome
+
offer capability
+
proof level
+
brand/founder credibility
```

Classify each promise:
`PROVEN / SUPPORTED / PLAUSIBLE_BUT_UNPROVEN / UNSUPPORTED`.

`UNSUPPORTED` cannot enter final positioning.

## Step 5 — Differentiation
Evaluate against real alternatives, substitutes and DIY/manual options.

Potential differentiation may come from workflow/approach, specialization, proof, evidenced speed/process, integration capability, delivery model, business model, founder perspective, category framing, customer experience, or offer architecture.

Reject empty claims such as “high quality”, “individual approach”, “innovative”, “best”, “AI-powered”, or “full-cycle” without concrete evidence.

## Step 6 — Reason to choose
A valid reason-to-choose must answer:

> Why would this supported ICP choose this offer instead of the alternatives?

Cite business truth, identity/capability fact, proof asset, research/VOC, or verified market gap.

If no defensible answer exists, return `POSITIONING_GAP`.

## Step 7 — Positioning statement
Produce an internal statement:

```text
For [supported ICP / buying situation],
[brand/offer] helps [supported outcome]
by [credible mechanism],
unlike [real alternatives],
because [defensible proof / difference].
```

Mark missing fields instead of forcing precision.

## Step 8 — Message boundaries
Define claims allowed, claims requiring qualification, claims forbidden until evidence exists, topics that strengthen positioning, topics that dilute it, and secondary offers that must not dominate the narrative.

## Step 9 — Conflict handling
Surface conflicts such as service revenue vs passive products, broad expertise vs narrow positioning, high-engagement audience vs weak ICP, strong market demand vs weak proof, and strong capability vs weak buyer evidence.

Ask the user when the conflict changes priority.

## Output
Produce one object conforming to `schemas/positioning-offer-fit.schema.json` and include primary/secondary/deferred offers, priority ICPs, supported promises, positioning statement, reasons to choose, proof assets, allowed/forbidden claims, gaps, research requests, user questions, and `safe_for_strategy`.

## Quality gate
A full strategy cannot be `READY` when there is no primary offer, the primary ICP is unsupported, the main promise is unsupported, the reason-to-choose is invented, or a central positioning conflict remains unresolved.
