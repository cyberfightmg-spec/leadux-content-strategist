---
name: content-pillars
description: >-
  Derive bounded content territories from the validated strategic thesis so every pillar has a
  specific strategic job and cannot exist independently of the chosen strategy.
metadata:
  version: 0.9.0
  category: content-strategy
  evidence_mode: required
license: MIT
---

# Skill: Content Pillars

## Mission
Turn the selected Strategic Thesis and wedge into a small set of bounded content territories.

Pillars are **not the strategy**. They are consequences of the strategy.

## Required inputs
- selected `strategic-thesis`;
- validated `strategic-wedge`;
- Founder/Brand Context;
- Audience / ICP Fit;
- Customer Journey / Funnel Intent;
- Channel / Distribution Fit;
- research evidence.

## Required pillar fields
Every pillar must state:
- `thesis_id`;
- strategic job;
- audience/buying role;
- relevant journey state(s);
- business/offer connection;
- thesis connection: which where-to-play/how-to-win/bet it supports;
- research evidence;
- brand proof/right-to-speak;
- positioning contribution;
- suitable channel roles;
- inclusion boundary;
- exclusion boundary;
- dilution risk;
- stop/review condition.

## Coherence test

Ask:

> If the selected thesis were replaced by the strongest alternative, would this pillar remain unchanged?

If yes, the pillar is likely generic. Narrow, experimentally justify, or reject it.

## Rules
- prefer fewer stronger pillars;
- do not create a pillar solely because a topic is popular;
- do not use a broad expertise category as a pillar without a strategic job;
- protect selected-thesis trade-offs;
- a pillar that violates `will_not_do` is invalid;
- preserve evidence lineage.

## Output
Objects conforming to `schemas/content-pillar.schema.json` plus thesis/coherence fields where supported.
