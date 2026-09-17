---
name: strategy-intake
description: >-
  Validate upstream market evidence, identity/business context, positioning/offer fit, objectives, constraints, and performance history before any strategic decision is made.
metadata:
  version: 0.5.0
  category: content-strategy
  evidence_mode: required
license: MIT
---

# Skill: Strategy Intake

## Mission
Validate that the strategist has enough evidence about the market, the actual business, and its supported positioning before making content decisions.

A strong research package without commercial context is insufficient. A complete business profile without market evidence is also insufficient. A content strategy must not proceed as `READY` when the primary promise or reason-to-choose is invented.

## Required checks

### Research side
- research integrity status;
- target segment/geography match;
- freshness of time-sensitive claims/signals;
- unresolved contradictions;
- high-impact data gaps.

### Identity side (founder-led)
- confirmed Identity Profile exists;
- strategically material unknowns are visible;
- expertise and public/private boundaries are not inferred.

### Business side
- Business Context exists and validates;
- commercial goals are explicit enough to prioritize;
- active/planned offers are distinguishable;
- resource/delivery constraints are known where material;
- unresolved commercial conflicts are visible.

### Positioning / offer-fit side
- `positioning-offer-fit` exists and validates;
- at least one primary commercial/strategic offer is selected;
- primary audience/buying situation is supported or explicitly partial;
- main promise status is not `UNSUPPORTED`;
- reason-to-choose is defensible or the gap is explicit;
- forbidden/qualified claims are preserved;
- `safe_for_strategy` is true for a full `READY` run.

### Founder / brand side
- Founder/Brand Context exists and validates when required;
- commercial priorities reflect positioning/offer-fit rather than guessed priorities;
- positioning and anti-positioning are clear enough for content selection;
- credible proof assets are known;
- channel roles and production capacity are known;
- brand-dilution constraints are explicit.

### Learning side
- availability and quality of first-party performance history;
- strategy memory freshness;
- existing winners/losers and sample-size limitations.

### Decision side
- business objective;
- time horizon;
- capacity constraints;
- required/forbidden channels or formats;
- decision that strategy must actually support.

## Output
Return:
- `usable_evidence`;
- `limited_evidence`;
- `identity_gaps`;
- `business_context_gaps`;
- `positioning_gaps`;
- `usable_brand_context`;
- `brand_context_gaps`;
- `blocked_decisions`;
- `research_requests`;
- `questions_required_from_user`;
- proposed strategy run scope;
- proposed strategy integrity ceiling.

## Integrity ceiling
For a full commercial strategy:
- materially incomplete Business Context → cannot receive `READY`;
- `safe_for_strategy = false` in Positioning / Offer Fit → cannot receive `READY`;
- unsupported main promise or invented reason-to-choose → `BLOCKED` or `NEEDS_RESEARCH` depending on what is missing;
- missing/materially incomplete founder context for founder-led work → cannot receive `READY`;
- `INSUFFICIENT_EVIDENCE` research → core market-dependent decisions remain blocked;
- weak performance history → strategy may proceed, but performance-derived recommendations remain experiments.

Do not repair weak research, weak context, or weak positioning by inventing missing facts.
