---
name: founder-brand-context
description: >-
  Convert a confirmed founder identity profile plus explicit business facts into the brand context that constrains and personalizes every strategic decision, without filling gaps by inference.
metadata:
  version: 0.4.0
  category: content-strategy
  evidence_mode: required
license: MIT
---

# Skill: Founder / Brand Context

## Mission
Make strategy specific to the actual founder, brand, offers, audiences, credibility, channels, voice, constraints, and commercial priorities.

A market can support many valid strategies. This skill determines which of them are valid for this founder/brand.

## Required upstream input
For founder-led strategy, first load a **confirmed** object conforming to:

`schemas/identity-profile.schema.json`

Then combine it only with explicit business/offer/channel facts.

Output must conform to:

`schemas/founder-brand-context.schema.json`

## No-inference rule
Do not convert:
- interest → expertise;
- project → commercial priority;
- frequent topic → personal value;
- current revenue need → long-term identity;
- public biography → self-definition;
- audience engagement → desired audience;
- a temporary experiment → core offer.

If a mapping is unclear, ask the founder.

## Required dimensions
At minimum establish, when relevant:
- confirmed founder identity and expertise;
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

## Mapping protocol
For every material context field record its origin as one of:

```text
IDENTITY_PROFILE
EXPLICIT_BUSINESS_FACT
FOUNDER_CONFIRMATION
PUBLIC_FACT
UNKNOWN
```

Do not silently manufacture a bridge between identity and business.

## Strategic use
Every proposed pillar, content opportunity, channel role, experiment, and Creator brief must pass:

1. **Credibility fit** — can this founder/brand speak about it with believable authority?
2. **Commercial fit** — does it support an active objective, offer, or strategic asset?
3. **Audience fit** — is it relevant to a priority audience?
4. **Positioning fit** — does it reinforce rather than blur the point of view?
5. **Capability fit** — can the founder/team execute it repeatedly?
6. **Channel fit** — does it make sense for the intended distribution surface?
7. **Identity fit** — does it conflict with explicitly stated values, boundaries, or rejected labels?

## Founder-led strategy rule

```text
what the market cares about
×
what the founder can prove / demonstrate / explain uniquely
×
what the business needs to sell or compound
×
what the founder is willing to represent publicly
```

Do not optimize for market demand alone.

## Anti-generic gate
Reject or narrow a recommendation when:
- it could be assigned unchanged to any competitor;
- it depends on expertise the founder does not credibly possess;
- it promotes a low-priority offer at the expense of a core priority;
- it creates audience confusion between unrelated directions;
- it conflicts with stated identity/values/boundaries;
- it requires an unsustainable format or cadence.

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
- `context_gaps`;
- `mapping_provenance`.

## Quality rule
A founder-led full strategy cannot receive the highest integrity status when either the Identity Profile is unconfirmed or Founder/Brand Context is materially incomplete.
