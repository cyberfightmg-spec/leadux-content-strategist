---
name: founder-brand-context
description: >-
  Merge confirmed identity, business context, audience/ICP fit, customer journey intent,
  positioning/offer-fit, and channel/distribution fit into the strategy context that constrains audiences,
  offers, proof, channels, voice, and execution choices.
metadata:
  version: 0.8.0
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
customer-journey-intent
+
positioning-offer-fit
+
channel-distribution-fit
→ founder-brand-context
```

For non-founder-led organizations, replace identity-profile with an appropriate confirmed organization/brand identity source.

## Absolute rule
Do not invent missing identity, business, audience, journey, positioning, promise, proof, channel, distribution, or performance fields during the merge.

If a needed field is absent or unsupported, preserve it as `UNKNOWN` and route back to the owning skill.

## Required inputs
- `schemas/identity-profile.schema.json` when founder-led;
- `schemas/business-context.schema.json`;
- `schemas/audience-icp-fit.schema.json`;
- `schemas/customer-journey-intent.schema.json` when journey assumptions matter;
- `schemas/positioning-offer-fit.schema.json`;
- `schemas/channel-distribution-fit.schema.json` when channel recommendations matter;
- explicit brand facts if separately supplied.

Output conforms to `schemas/founder-brand-context.schema.json`.

## Merge responsibilities

### From Identity Profile
Use only confirmed/self-stated fields for public identity, expertise boundaries, values/non-negotiables, public/private content boundaries, self-definition, and credible right-to-speak.

### From Business Context
Use only confirmed/documented fields for business model, goals, revenue-model priorities, delivery/resources/capacity, markets not served, and operational constraints.

### From Audience / ICP Fit
Use only supported classifications for primary/secondary ICPs, content-audience-only segments, role relationships, supported jobs/problems/outcomes, rejected/deferred segments, and unknown role relationships.

Never upgrade `HYPOTHESIS` or `AUDIENCE_NOT_ICP` to a sales ICP during merge.

### From Customer Journey / Funnel Intent
Preserve supported journey path IDs, audience-role × journey-state mappings, confidence per journey state, next decisions/questions, objections, trust/proof requirements, triggers, content jobs, CTA boundaries, and unknown transitions.

Never upgrade `HYPOTHESIS` journey state to confirmed intent and never convert engagement into purchase readiness.

### From Positioning / Offer Fit
Use only supported/confirmed fields for primary/secondary offers, main promise and claim status, positioning statement, reasons to choose, proof assets, allowed/qualified/forbidden claims, strengthening/diluting topics, and unresolved positioning gaps.

### From Channel / Distribution Fit
Preserve:
- primary / secondary / repurpose-only / experimental / deferred / rejected channels;
- channel evidence status;
- audience-role × journey-state × channel mappings;
- channel content/distribution jobs;
- supported formats;
- desired next actions and CTA strength;
- owned/rented/earned/paid distinctions;
- repurposing graph;
- operational constraints;
- measurement levels and interpretation limits;
- channel gaps and experiments.

Never upgrade `HYPOTHESIS` channel fit to confirmed performance and never treat platform reach as lead/revenue proof.

## Traceability
Every derived context field must remain traceable to source fields or research IDs.

Do not silently upgrade:
- `HYPOTHESIS` → `CONFIRMED_ICP`;
- `AUDIENCE_NOT_ICP` → buyer target;
- journey `HYPOTHESIS` → observed intent;
- engagement → `PURCHASE_READY`;
- channel `HYPOTHESIS` → `CONFIRMED_FIT`;
- views/reach → lead/revenue evidence;
- `PLAUSIBLE_BUT_UNPROVEN` → `SUPPORTED`;
- `POSITIONING_GAP` → invented differentiation.

## Strategic use
Every proposed pillar, opportunity, channel role, experiment and Creator brief must pass:

1. **Credibility fit** — can this person/brand credibly speak or demonstrate it?
2. **Commercial fit** — does it support a primary/secondary offer or strategic objective?
3. **Audience-role fit** — is the content aimed at the right role?
4. **Journey fit** — does content match what that role is trying to decide next?
5. **Positioning fit** — does it reinforce the approved promise/reason-to-choose?
6. **Proof fit** — are claims inside allowed evidence boundaries?
7. **Channel fit** — does the selected surface have a supportable role for this audience/state/job?
8. **Format fit** — is the content packaged appropriately for that surface rather than copied unchanged?
9. **CTA fit** — does the CTA match supported intent rather than desired sales pressure?
10. **Capability fit** — can it be executed repeatedly with actual resources?
11. **Measurement fit** — are distribution signals separated from lead/business outcomes?
12. **Boundary fit** — does it respect ethical, personal, industry and operational exclusions?

## Anti-generic gate
Reject or narrow a recommendation when it could be assigned unchanged to any competitor, relies on unsupported expertise/proof, targets a non-ICP as if it were the buyer, assumes purchase intent from engagement, selects a channel only because it is popular, uses a CTA too strong for the supported journey state, promotes a deferred/rejected offer without reason, creates audience confusion, violates claim boundaries, or weakens approved positioning.

## Output
Return:
- `active_identity`;
- `business_model`;
- `commercial_priorities`;
- `primary_icps`;
- `secondary_icps`;
- `content_audiences`;
- `audience_role_map`;
- `journey_state_map`;
- `journey_confidence_map`;
- `proof_needs_by_state`;
- `cta_boundaries`;
- `priority_offers`;
- `positioning_non_negotiables`;
- `supported_promises`;
- `reasons_to_choose`;
- `proof_assets`;
- `allowed_claims`;
- `forbidden_claims`;
- `primary_channels`;
- `secondary_channels`;
- `experimental_channels`;
- `channel_role_map`;
- `repurposing_graph`;
- `owned_distribution_plan`;
- `channel_measurement_limits`;
- `content_strengths`;
- `brand_dilution_risks`;
- `capacity_constraints`;
- `context_gaps`;
- `source_field_map`.

## Quality rule
A full strategy cannot receive `READY` when required identity/business context is incomplete, Audience / ICP Fit is unsafe, a critical journey assumption is invented, Positioning / Offer Fit is unsafe, Channel / Distribution Fit is unsafe, the main promise is unsupported, or the primary ICP remains only an unsupported hypothesis.
