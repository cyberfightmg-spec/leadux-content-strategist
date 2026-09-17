---
name: founder-brand-context
description: >-
  Build, validate, and load the founder or brand context that constrains and personalizes every strategic decision.
metadata:
  version: 0.4.0
  category: content-strategy
  evidence_mode: required
license: MIT
---

# Skill: Founder / Brand Context

## Mission
Make the strategy specific to the actual founder, brand, offers, audiences, credibility, channels, voice, constraints, and commercial priorities.

A market can support many valid strategies. This skill determines which of them are valid for this brand.

## Required input
Use a context object conforming to:

`schemas/founder-brand-context.schema.json`

If a complete context already exists, reuse it. Do not ask again for facts already supplied.

## Required dimensions
At minimum establish:
- founder/brand identity and expertise;
- business model and current commercial priority;
- positioning and anti-positioning;
- priority audiences;
- active offers and their relative importance;
- credible proof assets;
- channel roles;
- content jobs;
- tone/voice;
- signature topics;
- topics/angles that dilute the brand;
- production/capacity constraints.

## Strategic use
Every proposed pillar, content opportunity, channel role, experiment, and Creator brief must pass these checks:

1. **Credibility fit** — can this brand speak about it with believable authority?
2. **Commercial fit** — does it support an active business objective or strategic asset?
3. **Audience fit** — is it relevant to a priority audience?
4. **Positioning fit** — does it reinforce rather than blur the brand's point of view?
5. **Capability fit** — can the founder/team execute it repeatedly at sufficient quality?
6. **Channel fit** — does the idea make sense for the intended distribution surface?

## Founder-led strategy rule
For founder-led brands, distinguish:

```text
what the market cares about
×
what the founder can prove / demonstrate / explain uniquely
×
what the business needs to sell or compound
```

Do not optimize for market demand alone. That produces generic category content.

## Anti-generic gate
Reject or narrow a recommendation when:
- it could be assigned unchanged to any competitor;
- it depends on expertise the founder does not credibly possess;
- it promotes a low-priority offer at the expense of a core commercial priority;
- it creates audience confusion between unrelated business directions;
- it conflicts with explicit brand values or tone constraints;
- it requires an unsustainable content format/cadence.

## Output
Return:
- `active_identity`;
- `priority_audiences`;
- `priority_offers`;
- `positioning_non_negotiables`;
- `proof_assets`;
- `content_strengths`;
- `channel_roles`;
- `brand_dilution_risks`;
- `capacity_constraints`;
- `context_gaps`.

## Quality rule
A full strategy cannot receive the highest integrity status when Founder/Brand Context is missing or materially incomplete.
