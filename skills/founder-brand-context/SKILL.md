---
name: founder-brand-context
description: >-
  Merge confirmed identity, business context, audience/ICP fit, and positioning/offer-fit into the strategy context that constrains audiences, offers, proof, channels, voice, and execution choices.
metadata:
  version: 0.6.0
  category: content-strategy
  evidence_mode: required
license: MIT
---

# Skill: Founder / Brand Context

## Mission
Create the context layer that the Strategist reasons over by combining separate confirmed inputs:

```text
identity-profile
+
business-context
+
audience-icp-fit
+
positioning-offer-fit
→ founder-brand-context
```

For non-founder-led organizations, replace identity-profile with an appropriate confirmed organization/brand identity source.

## Absolute rule
Do not invent missing identity, business, audience, positioning, promise, proof, or differentiation fields during the merge.

If a needed field is absent or unsupported, preserve it as `UNKNOWN` and route back to the owning skill.

## Required inputs
- `schemas/identity-profile.schema.json` when founder-led;
- `schemas/business-context.schema.json`;
- `schemas/audience-icp-fit.schema.json`;
- `schemas/positioning-offer-fit.schema.json`;
- explicit brand facts if separately supplied.

Output conforms to `schemas/founder-brand-context.schema.json`.

## Merge responsibilities

### From Identity Profile
Use only confirmed/self-stated fields for public identity, expertise boundaries, values/non-negotiables, public/private content boundaries, self-definition, and credible right-to-speak.

### From Business Context
Use only confirmed/documented fields for business model, goals, revenue-model priorities, delivery/resources/capacity, markets not served, and operational constraints.

### From Audience / ICP Fit
Use only supported classifications for:
- primary and secondary ICPs;
- content-audience-only segments;
- problem-holder/user/buyer/decision-maker relationships;
- supported jobs/problems/outcomes;
- known objections/triggers;
- rejected/deferred segments;
- unknown role relationships.

Never upgrade `HYPOTHESIS` or `AUDIENCE_NOT_ICP` to a sales ICP during merge.

### From Positioning / Offer Fit
Use only supported/confirmed fields for primary/secondary offers, main promise and claim status, positioning statement, reasons to choose, proof assets, allowed/qualified/forbidden claims, strengthening/diluting topics, and unresolved positioning gaps.

## Traceability
Every derived context field must remain traceable to source fields or research IDs.

Do not silently upgrade:
- `HYPOTHESIS` → `CONFIRMED_ICP`;
- `AUDIENCE_NOT_ICP` → buyer target;
- `PLAUSIBLE_BUT_UNPROVEN` → `SUPPORTED`;
- `POSITIONING_GAP` → invented differentiation.

## Strategic use
Every proposed pillar, opportunity, channel role, experiment and Creator brief must pass:

1. **Credibility fit** — can this person/brand credibly speak or demonstrate it?
2. **Commercial fit** — does it support a primary/secondary offer or strategic objective?
3. **Audience-role fit** — is the content aimed at the right role: ICP, buyer, decision-maker, user, influencer, or audience-only segment?
4. **Positioning fit** — does it reinforce the approved promise/reason-to-choose?
5. **Proof fit** — are claims inside allowed evidence boundaries?
6. **Capability fit** — can it be executed repeatedly with actual resources?
7. **Channel fit** — does it suit the intended distribution surface?
8. **Boundary fit** — does it respect ethical, personal, industry and operational exclusions?

## Anti-generic gate
Reject or narrow a recommendation when it could be assigned unchanged to any competitor, relies on unsupported expertise/proof, targets a non-ICP as if it were the buyer, promotes a deferred/rejected offer without reason, creates audience confusion, violates claim boundaries, or weakens the approved positioning.

## Output
Return:
- `active_identity`;
- `business_model`;
- `commercial_priorities`;
- `primary_icps`;
- `secondary_icps`;
- `content_audiences`;
- `audience_role_map`;
- `priority_offers`;
- `positioning_non_negotiables`;
- `supported_promises`;
- `reasons_to_choose`;
- `proof_assets`;
- `allowed_claims`;
- `forbidden_claims`;
- `content_strengths`;
- `channel_roles`;
- `brand_dilution_risks`;
- `capacity_constraints`;
- `context_gaps`;
- `source_field_map`.

## Quality rule
A full strategy cannot receive `READY` when required identity/business context is incomplete, Audience / ICP Fit is unsafe, Positioning / Offer Fit is unsafe, the main promise is unsupported, or the primary ICP remains only an unsupported hypothesis.
