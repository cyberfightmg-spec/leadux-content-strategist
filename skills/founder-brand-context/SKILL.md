---
name: founder-brand-context
description: >-
  Merge confirmed identity and business context into the strategy context that constrains positioning, audiences, offers, proof, channels, voice, and execution choices.
metadata:
  version: 0.4.0
  category: content-strategy
  evidence_mode: required
license: MIT
---

# Skill: Founder / Brand Context

## Mission
Create the context layer that the Strategist actually reasons over by combining separate confirmed inputs:

```text
identity-profile
+
business-context
→ founder-brand-context
```

For non-founder-led organizations, replace identity-profile with an appropriate confirmed organization/brand identity source. Business Context remains separate and required for full commercial strategy.

## Absolute rule
Do not invent missing identity or business fields during the merge.

If a field is needed but absent, preserve it as `UNKNOWN` and route back to the owning context skill.

## Required inputs
- `schemas/identity-profile.schema.json` when founder-led;
- `schemas/business-context.schema.json`;
- explicit brand/positioning facts if separately supplied.

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
- commercial priorities;
- priority offers;
- priority audiences;
- current/desired revenue model;
- goals and horizons;
- delivery/resources/capacity;
- markets not served;
- operational constraints.

### Derived strategic context
You may normalize, but not invent:
- positioning inputs;
- proof map;
- content jobs;
- channel roles;
- brand-dilution risks;
- execution constraints.

Every derived field must remain traceable to one or more source fields.

## Strategic use
Every proposed pillar, opportunity, channel role, experiment and Creator brief must pass:

1. **Credibility fit** — can this person/brand credibly speak or demonstrate it?
2. **Commercial fit** — does it support a confirmed business objective, offer or strategic asset?
3. **Audience fit** — does it serve a confirmed/research-supported priority audience?
4. **Positioning fit** — does it reinforce rather than blur the intended market position?
5. **Capability fit** — can it be executed repeatedly with real resources?
6. **Channel fit** — does it suit the intended distribution surface?
7. **Boundary fit** — does it respect stated ethical, personal, industry and operational exclusions?

## Anti-generic gate
Reject or narrow a recommendation when:
- it could be assigned unchanged to any competitor;
- it requires expertise/proof the person or brand does not have;
- it promotes a lower-priority offer over a confirmed commercial priority without justification;
- it creates audience confusion between unrelated directions;
- it violates stated boundaries;
- it requires an unsustainable format/cadence;
- it conflicts with the confirmed revenue model or business stage.

## Output
Return:
- `active_identity`;
- `business_model`;
- `commercial_priorities`;
- `priority_audiences`;
- `priority_offers`;
- `positioning_non_negotiables`;
- `proof_assets`;
- `content_strengths`;
- `channel_roles`;
- `brand_dilution_risks`;
- `capacity_constraints`;
- `context_gaps`;
- `source_field_map`.

## Quality rule
A full strategy cannot receive the highest integrity status when the required identity or Business Context is materially incomplete.
