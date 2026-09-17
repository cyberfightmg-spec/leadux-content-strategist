# Strategy Quality Gates

A full strategy must pass all applicable gates.

## 1. Research Integrity Gate
- research package integrity is known;
- high-impact contradictions/gaps are visible;
- market-dependent decisions are not built on `INSUFFICIENT_EVIDENCE`.

## 2. Identity Gate (founder-led)
- Identity Profile is confirmed;
- expertise boundaries are explicit enough for strategy;
- public/private boundaries are explicit where material;
- no identity/value/personality field was inferred merely from behavior or style.

## 3. Business Context Gate
- business model and current goals are explicit;
- active/planned offers are distinguishable;
- resource/delivery constraints are known where material;
- unresolved commercial conflicts are visible;
- `UNKNOWN` economics remain unknown.

A full commercial strategy cannot be `READY` when Business Context is materially incomplete.

## 4. Audience / ICP Fit Gate
- content audience is not silently equated with buyer ICP;
- problem holder, user, buyer and decision-maker are separated when materially different;
- primary ICP status is supported by evidence or explicitly labeled hypothesis;
- demographic/persona details are not invented for completeness;
- audience priorities match current business goals and serviceability;
- high-engagement but commercially weak audiences are marked `AUDIENCE_NOT_ICP` when appropriate;
- unknown buyer/decision relationships remain visible;
- `safe_for_strategy = true` for a full `READY` commercial strategy.

A strategy cannot be `READY` when its primary sales target is only an unsupported persona guess.

## 5. Customer Journey / Funnel Intent Gate
- journey state and buying role are kept separate;
- engagement is not treated as purchase intent;
- TOFU/MOFU/BOFU labels do not substitute for actual customer-state evidence;
- objections, triggers, trust needs and proof needs are supported or marked unknown/hypothesis;
- CTA strength matches supported intent rather than desired conversion pressure;
- different buying roles may have different journey states for the same offer;
- non-linear paths and unknown transitions remain visible;
- material journey assumptions that affect messaging or CTA are evidence-backed or explicitly experimental.

A strategy cannot be `READY` when a critical conversion path depends on an invented journey stage or unverified purchase-readiness assumption.

## 6. Positioning / Offer Fit Gate
- at least one primary offer or strategic commercial focus is explicit;
- priority ICP/buying situation comes from `audience-icp-fit` or equivalent verified evidence;
- positioning does not contradict known journey-state evidence;
- main promise is not `UNSUPPORTED`;
- reason-to-choose is defensible or `POSITIONING_GAP` is explicitly returned;
- differentiation is based on business truth, proof, identity/capability, or verified market evidence;
- allowed / qualified / forbidden claim boundaries are preserved;
- central offer/positioning conflicts are resolved or explicitly block the run;
- `safe_for_strategy = true` for a full `READY` strategy.

Never invent a USP merely to pass this gate.

## 7. Channel / Distribution Fit Gate
- each primary channel has an explicit audience/role and journey-state relationship;
- each primary channel has a defined distribution/content job;
- platform popularity is not treated as evidence of fit;
- competitor channel presence is not treated as proof of competitor channel success;
- first-party performance is preferred over generic benchmark claims when comparable;
- format recommendations fit the channel rather than copying one asset everywhere unchanged;
- the plan fits known production, response, budget, language and compliance constraints;
- views/reach/engagement are not presented as leads or revenue;
- owned, rented, earned and paid surfaces are distinguished where material;
- experimental channels are explicitly labeled hypotheses with a measurement plan;
- deferred/rejected channels have reasons when they appear attractive but do not fit;
- `safe_for_strategy = true` for a full `READY` distribution plan.

A full strategy cannot be `READY` when its primary distribution plan is based only on popularity, unsupported audience presence, or capacity the business does not have.

## 8. Founder / Brand Context Gate
- founder/brand identity is explicit when relevant;
- priority audiences and offers match approved Audience / ICP Fit and Positioning / Offer Fit;
- customer-state assumptions used in strategy are preserved with their confidence;
- channel roles match Channel / Distribution Fit rather than guessed platform priorities;
- positioning and anti-positioning are explicit;
- credible proof assets are known;
- capacity constraints are known;
- brand-dilution constraints are known.

A full strategy cannot be `READY` when this context is materially incomplete.

## 9. Objective Traceability Gate
Every major content job connects to a current business/content objective, audience role, relevant journey state or decision, approved channel role, and intended audience action.

## 10. Evidence Lineage Gate
Every material decision is traceable to research evidence, Identity/Business Context, Audience / ICP Fit, Customer Journey / Funnel Intent, Positioning / Offer Fit, Channel / Distribution Fit, Founder/Brand Context, first-party performance, a validated pattern, or an explicit constraint.

## 11. Anti-Generic Gate
For every major recommendation ask:

> Could this recommendation be given unchanged to a direct competitor?

If yes, narrow or reject it unless the generic element is intentionally infrastructural.

## 12. Validated Pattern Gate
When an external strategy pattern influences a decision:
- record its `pattern_id`;
- preserve its evidence grade and limitations;
- state transfer assumptions;
- adapt the mechanism to the brand/business;
- do not copy tactics by default.

## 13. Trade-off Gate
The strategy states what is `CORE`, `RESPONSIVE`, `EXPERIMENT`, `DEFERRED`, and `REJECTED`.

The channel plan separately states `PRIMARY`, `SECONDARY`, `REPURPOSE_ONLY`, `EXPERIMENTAL`, `DEFERRED`, and `REJECTED` channel roles.

## 14. Credibility / Proof Gate
The founder/brand can credibly explain, demonstrate, document or prove the proposed territory and content claims remain inside approved evidence boundaries.

## 15. Commercial Fit Gate
Priority work supports a primary/secondary offer, strategic asset, approved ICP or business objective. Interesting but commercially distracting topics and channels are downgraded or rejected.

## 16. Feasibility Gate
Cadence, format, channel count, moderation/response load, and production requirements fit actual capacity.

## 17. Challenger Gate
High-impact decisions have a skeptical counterweight, credible alternative, failure mode and reversal evidence.

## 18. Creator Handoff Gate
Creator briefs preserve strategic intent, evidence, approved positioning, ICP role, journey state/next decision, approved channel role, proof, CTA boundary and forbidden unsupported claims without prematurely writing final content.

## 19. Measurement Gate
The strategy defines observable indicators and interpretation limits. Unknown thresholds remain unknown. Distribution signals, audience response, journey progression, lead signals and business outcomes are not conflated.

## 20. Learning Gate
Where first-party performance exists, the strategy compares against relevant internal baselines and avoids causal overclaiming. Channel fit can be upgraded or downgraded only from actual evidence, not preference.

## Status rules

Use `NEEDS_RESEARCH` when a central market-dependent, audience-dependent, journey-dependent, positioning-dependent or channel-dependent decision lacks adequate evidence.

Use `READY_WITH_GAPS` when the strategy can proceed but material context, ICP, journey, positioning, distribution, research, performance or pattern-transfer uncertainty remains.

Use `BLOCKED` when missing evidence/context, unsupported ICP, invented journey intent, unsupported positioning, or an unusable distribution plan prevents safe or useful strategic selection.
