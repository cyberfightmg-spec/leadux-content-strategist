---
name: strategy-intake
description: >-
  Validate upstream market evidence, identity/business context, audience/ICP fit, customer journey intent, positioning/offer fit, objectives, constraints, and performance history before strategic decisions.
metadata:
  version: 0.7.0
  category: content-strategy
  evidence_mode: required
license: MIT
---

# Skill: Strategy Intake

## Mission
Validate that the strategist has enough evidence about the market, actual business, intended audience/ICP, customer decision state, and supported positioning before making content decisions.

A strong research package without commercial context is insufficient. A business profile without market evidence is insufficient. A content audience is not automatically a buyer. Engagement is not purchase intent. A full strategy must not proceed as `READY` when the primary ICP, journey intent, promise, or reason-to-choose is invented.

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

### Audience / ICP side
- `audience-icp-fit` exists and validates;
- content audience, problem holder, user, buyer and decision-maker are separated when material;
- primary ICP is `CONFIRMED_ICP` or `SUPPORTED_CANDIDATE`, or an explicit experiment/hypothesis with a strategy integrity downgrade;
- audience-only segments are not used as sales ICPs without evidence;
- unknown buyer/decision relationships are visible;
- `safe_for_strategy` is true for a full `READY` run.

### Customer journey / intent side
- `customer-journey-intent` exists when journey assumptions materially affect messaging, content jobs, CTA, or conversion path;
- journey state is not inferred from engagement alone;
- buying role and journey state are modeled separately;
- critical objections, trust needs, triggers and proof requirements are supported or explicitly unknown/hypothesis;
- CTA strength does not exceed supported purchase intent;
- non-linear or unknown transitions remain visible;
- `safe_for_strategy` is true when a critical journey path is used to justify a `READY` strategy.

### Positioning / offer-fit side
- `positioning-offer-fit` exists and validates;
- at least one primary commercial/strategic offer is selected;
- primary ICP/buying situation is consistent with Audience / ICP Fit;
- messaging and CTA do not contradict Customer Journey / Funnel Intent;
- main promise status is not `UNSUPPORTED`;
- reason-to-choose is defensible or the gap is explicit;
- forbidden/qualified claims are preserved;
- `safe_for_strategy` is true for a full `READY` run.

### Founder / brand side
- Founder/Brand Context exists and validates when required;
- commercial priorities reflect approved ICP, journey constraints, and positioning/offer-fit rather than guessed priorities;
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
- `audience_icp_gaps`;
- `journey_intent_gaps`;
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
- unsafe Audience / ICP Fit → cannot receive `READY`;
- primary ICP only an unsupported guess → `BLOCKED` or `NEEDS_RESEARCH`;
- a critical conversion/message decision based on invented journey intent → cannot receive `READY`;
- unsafe Positioning / Offer Fit → cannot receive `READY`;
- unsupported main promise or invented reason-to-choose → `BLOCKED` or `NEEDS_RESEARCH`;
- missing/materially incomplete founder context for founder-led work → cannot receive `READY`;
- `INSUFFICIENT_EVIDENCE` research → core market-dependent decisions remain blocked;
- weak performance history → strategy may proceed, but performance-derived recommendations remain experiments.

Do not repair weak research, weak context, weak ICP, weak journey evidence, or weak positioning by inventing missing facts.
