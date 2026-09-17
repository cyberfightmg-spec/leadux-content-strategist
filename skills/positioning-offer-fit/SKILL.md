---
name: positioning-offer-fit
description: >-
  Select which offer should drive strategy and define a defensible promise and positioning using confirmed identity, business context, audience/ICP fit, customer journey intent, and verified market evidence.
metadata:
  version: 0.7.0
  category: positioning
  evidence_mode: required
license: MIT
---

# Skill: Positioning / Offer Fit

## Mission
Decide what the brand should primarily sell through content, to whom, in which supported buying state, with what promise, and why that promise is credible.

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
→ founder-brand-context
→ content strategy
```

## Absolute rule: no invented differentiation or intent
Never invent an ICP, pain, journey stage, purchase readiness, objection, trigger, demand, offer priority, unique advantage, category leadership, proof, result, competitor weakness, guarantee, price/value advantage, or reason to choose.

If an attractive positioning claim lacks evidence or explicit business truth, mark it `UNSUPPORTED`, narrow it, or request evidence.

## Required inputs
- confirmed `identity-profile` when founder-led;
- confirmed `business-context`;
- `audience-icp-fit`;
- `customer-journey-intent` when message/CTA depends on decision state;
- verified `research-package` when market/customer/competitor facts matter;
- first-party proof assets when available.

## Audience and journey rule
Use `audience-icp-fit` as source of truth for segment/role and `customer-journey-intent` for supported decision state.

Do not collapse content audience, user, problem holder, buyer, decision-maker, influencer, or ICP. Do not assume they occupy the same journey state.

A content audience marked `AUDIENCE_NOT_ICP` may support reach/community goals but cannot silently become the primary sales target.

## Step 1 — Offer eligibility
Classify material offers as:
`ACTIVE / PLANNED / EXPERIMENTAL / DEPRIORITIZED / UNAVAILABLE / UNKNOWN`.

Test deliverability, commercial importance, ICP fit, relevant journey states, customer outcome, proof/capability, and whether content can realistically create or capture demand.

## Step 2 — Offer priority
Use visible dimensions:
- current/future revenue relevance;
- recurring/scalable potential when stated;
- ICP evidence;
- journey-state relevance;
- founder/brand credibility;
- proof strength;
- delivery capacity;
- known economics;
- whitespace/differentiation evidence;
- fit with stated goals.

Unknown remains unknown.

Classify: `PRIMARY / SECONDARY / EXPERIMENT / DEFERRED / REJECTED`.

## Step 3 — Audience / buying-state fit
For each priority offer use only supported segment and role information from `audience-icp-fit` and supported/hypothesized states from `customer-journey-intent`.

Preserve role-state differences. Example: USER may be `SOLUTION_AWARE` while DECISION_MAKER is `TRUST_VALIDATING`.

Do not fabricate personas or stage assignments.

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
+
journey-state relevance
```

Classify each promise:
`PROVEN / SUPPORTED / PLAUSIBLE_BUT_UNPROVEN / UNSUPPORTED`.

`UNSUPPORTED` cannot enter final positioning.

## Step 5 — Differentiation
Evaluate against real alternatives, substitutes and DIY/manual options.

Potential differentiation may come from workflow/approach, specialization, proof, evidenced speed/process, integration capability, delivery model, business model, founder perspective, category framing, customer experience, or offer architecture.

Reject empty claims such as “high quality”, “individual approach”, “innovative”, “best”, “AI-powered”, or “full-cycle” without concrete evidence.

## Step 6 — Reason to choose
Ask:

> Why would this supported ICP in this decision context choose this offer instead of the alternatives?

Cite business truth, identity/capability fact, proof asset, research/VOC, or verified market gap.

If no defensible answer exists, return `POSITIONING_GAP`.

## Step 7 — Positioning statement
Produce an internal statement:

```text
For [supported ICP / buying situation / relevant state],
[brand/offer] helps [supported outcome]
by [credible mechanism],
unlike [real alternatives],
because [defensible proof / difference].
```

Mark missing fields instead of forcing precision.

## Step 8 — Message and CTA boundaries
Define:
- claims allowed;
- claims requiring qualification;
- claims forbidden until evidence exists;
- messages suitable to different journey states;
- CTA strength appropriate to supported intent;
- topics that strengthen positioning;
- topics that dilute it;
- secondary offers that must not dominate the narrative.

Never use a purchase-ready CTA merely because the business wants sales.

## Step 9 — Conflict handling
Surface conflicts such as service revenue vs passive products, broad expertise vs narrow positioning, high-engagement audience vs weak ICP, strong market demand vs weak proof, strong capability vs weak buyer evidence, and desired CTA vs unsupported purchase intent.

Ask the user when the conflict changes priority.

## Output
Produce one object conforming to `schemas/positioning-offer-fit.schema.json` and include primary/secondary/deferred offers, priority ICPs, relevant journey path IDs, supported promises, positioning statement, reasons to choose, proof assets, allowed/forbidden claims, CTA boundaries, gaps, research requests, user questions, and `safe_for_strategy`.

## Quality gate
A full strategy cannot be `READY` when there is no primary offer, the primary ICP is unsupported, the main promise is unsupported, the reason-to-choose is invented, a critical CTA depends on invented purchase intent, or a central positioning conflict remains unresolved.
