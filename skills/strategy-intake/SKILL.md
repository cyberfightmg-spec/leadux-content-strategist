---
name: strategy-intake
description: >-
  Validate upstream market evidence, founder/brand context, objectives, constraints, and performance history before any strategic decision is made.
metadata:
  version: 0.4.0
  category: content-strategy
  evidence_mode: required
license: MIT
---

# Skill: Strategy Intake

## Mission
Validate that the strategist has enough evidence about both the **market** and the **actual founder/brand** before making decisions.

A strong research package without brand context is insufficient for a personalized full strategy. A strong brand profile without market evidence is also insufficient.

## Required checks

### Research side
- research integrity status;
- target segment/geography match;
- freshness of time-sensitive claims/signals;
- unresolved contradictions;
- high-impact data gaps.

### Founder / brand side
- Founder/Brand Context exists and validates against `schemas/founder-brand-context.schema.json`;
- current commercial priorities are explicit;
- priority audiences and offers are distinguishable;
- positioning and anti-positioning are clear;
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
- `usable_brand_context`;
- `brand_context_gaps`;
- `blocked_decisions`;
- `research_requests`;
- proposed strategy run scope;
- proposed strategy integrity ceiling.

## Integrity ceiling
For a full personalized strategy:
- missing/materially incomplete founder context → cannot receive highest integrity status;
- `INSUFFICIENT_EVIDENCE` research → core market-dependent decisions remain blocked;
- weak performance history → strategy may proceed, but performance-derived recommendations remain experiments.

Do not repair weak research or weak founder context by inventing missing facts.
