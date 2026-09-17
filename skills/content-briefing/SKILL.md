---
name: content-briefing
description: >-
  Convert an approved strategy decision into an execution-ready Creator brief that preserves audience role,
  journey state, channel role, format adaptation, proof boundaries, CTA intent, and measurement level without writing final content.
metadata:
  version: 0.8.0
  category: content-strategy
  evidence_mode: required
license: MIT
---

# Skill: Content Briefing

## Mission
Turn an approved content opportunity/strategy decision into an execution-ready brief for a downstream Creator.

The brief must preserve strategy. It must not let the Creator silently change the target audience, journey state, channel job, claim boundary, or CTA pressure.

## Required inputs
- approved content opportunity;
- approved strategy decision;
- Audience / ICP Fit;
- Customer Journey / Funnel Intent when material;
- Positioning / Offer Fit;
- Channel / Distribution Fit;
- Founder / Brand Context;
- required research evidence;
- experiment definition when applicable.

## Brief fields
Include when known/material:
- objective;
- audience / segment IDs;
- audience role (`ICP`, buyer, user, decision-maker, content audience, etc.);
- journey state and confidence;
- next decision/question the content should help resolve;
- content job;
- content pillar;
- topic/tension;
- angle;
- positioning job;
- founder/brand POV and proof assets;
- required evidence IDs;
- required facts;
- claims that must not be made;
- approved `channel_fit_id` and `channel_id`;
- channel role / family;
- recommended format for that channel;
- adaptation notes when derived from another asset;
- CTA intent and CTA strength;
- desired next action;
- success metric;
- metric level: distribution signal / audience response / lead signal / business outcome;
- constraints;
- experiment ID if applicable.

## Channel rule
Do not choose a channel because it is popular or because the Creator prefers it.

If a channel is not approved in Channel / Distribution Fit:
- route it back as a strategy change;
- or mark it as an explicit channel experiment.

Do not copy the same final asset unchanged across every channel. Preserve the strategic message while adapting packaging, pacing, depth, format, CTA, and proof presentation to the surface.

## Measurement rule
A brief may optimize for a distribution signal when that is the actual job, but it must not describe that metric as a lead or business outcome.

Examples:
- view completion = distribution/content signal;
- qualified reply = audience-response/lead signal depending on definition;
- booked qualified call = lead signal;
- customer/revenue = business outcome.

## Creator boundary
Do not write the final post, script, caption, email, article, carousel, or video in this skill.

Output conforms to `schemas/content-brief.schema.json`.
