---
name: founder-brand-context
description: >-
  Merge confirmed identity, business context, and positioning/offer-fit into the strategy context that constrains audiences, offers, proof, channels, voice, and execution choices.
metadata:
  version: 0.5.0
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
positioning-offer-fit
→ founder-brand-context
```

For non-founder-led organizations, replace identity-profile with an appropriate confirmed organization/brand identity source.

## Absolute rule
Do not invent missing identity, business, positioning, audience, promise, proof, or differentiation fields during the merge.

If a needed field is absent or unsupported, preserve it as `UNKNOWN` and route back to the owning skill.

## Required inputs
- `schemas/identity-profile.schema.json` when founder-led;
- `schemas/business-context.schema.json`;
- `schemas/positioning-offer-fit.schema.json`;
- explicit brand facts if separately supplied.

Output conforms to:

`schemas/founder-brand-context.schema.json`

## Merge responsibilities

### From Identity Profile
Use only confirmed/self-stated fields for:
- public identity;
- expertise boundaries;
- values/non-negotiables;
- personal/public-content boundaries;
- self-definition;
- credible right-to-speak.

### From Business Context
Use only confirmed/documented fields for:
- business model;
- goals;
- revenue-model priorities;
- delivery/resources/capacity;
- markets not served;
- operational constraints.

### From Positioning / Offer Fit
Use only supported/confirmed fields for:
- primary/secondary offers;
- priority audiences;
- main promise and claim status;
- positioning statement;
- reasons to choose;
- proof assets;
- allowed/qualified/forbidden claims;
- strengthening/diluting topics;
- unresolved positioning gaps.

## Traceability
Every derived context field must remain traceable to one or more source fields or research IDs.

Do not silently upgrade:
- `PLAUSIBLE_BUT_UNPROVEN` → `SUPPORTED`;
- `PARTIAL` → `PROVEN`;
- `POSITIONING_GAP` → invented differentiation.

## Strategic use
Every proposed pillar, opportunity, channel role, experiment and Creator brief must pass:

1. **Credibility fit** — can this person/brand credibly speak or demonstrate it?
2. **Commercial fit** — does it support a primary/secondary offer or stated strategic objective?
3. **Audience fit** — does it serve a supported priority audience?
4. **Positioning fit** — does it reinforce the approved promise/reason-to-choose rather than blur it?
5. **Proof fit** — are content claims within allowed evidence boundaries?
6. **Capability fit** — can it be executed repeatedly with actual resources?
7. **Channel fit** — does it suit the intended distribution surface?
8. **Boundary fit** — does it respect ethical, personal, industry and operational exclusions?

## Anti-generic gate
Reject or narrow a recommendation when:
- it could be assigned unchanged to any competitor;
- it requires expertise/proof the person or brand does not have;
- it promotes a deferred/rejected offer without explicit strategic reason;
- it creates audience confusion between unrelated directions;
- it conflicts with allowed/forbidden claim boundaries;
- it violates stated values/industry exclusions;
- it requires unsustainable production;
- it weakens the approved primary positioning.

## Output
Return:
- `active_identity`;
- `business_model`;
- `commercial_priorities`;
- `priority_audiences`;
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
A full strategy cannot receive `READY` when:
- required identity/business context is materially incomplete;
- positioning-offer-fit is unsafe for strategy;
- the main promise remains unsupported;
- no defensible reason-to-choose exists for the selected primary offer.
