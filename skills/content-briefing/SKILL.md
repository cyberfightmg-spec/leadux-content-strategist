---
name: content-briefing
description: >-
  Convert an approved thesis-linked strategy decision into an execution-ready Creator brief without
  allowing the Creator layer to rewrite the strategy.
metadata:
  version: 0.9.0
  category: content-strategy
  evidence_mode: required
license: MIT
---

# Skill: Content Briefing

## Mission
Turn an approved content opportunity/decision into a Creator-ready brief while preserving the selected Strategic Thesis.

## Required brief fields
- `strategic_thesis_id`;
- thesis link: what strategic choice this execution serves;
- objective;
- audience / buying role;
- journey state / next decision;
- content job;
- pillar;
- topic/tension;
- angle;
- approved channel role and format;
- evidence IDs;
- proof assets;
- required facts;
- forbidden/qualified claims;
- CTA intent/strength;
- success metric and measurement level;
- experiment/bet/assumption ID when applicable;
- constraints.

## Coherence rule
The Creator must be able to answer:

> Which part of thesis [thesis_id] does this asset implement?

If that answer is missing, return the brief upstream rather than inventing strategic intent.

## Boundary
Do not write final posts/scripts by default.

The Creator may adapt execution to the channel, but may not change:
- audience priority;
- strategic promise;
- proof boundary;
- thesis trade-offs;
- core CTA intent;
- `will_not_do`.
