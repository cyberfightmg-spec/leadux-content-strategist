---
name: strategy-intake
description: >-
  Validate an upstream evidence package and strategy context before any strategic decisions are made.
metadata:
  version: 0.3.0
  category: content-strategy
  evidence_mode: required
license: MIT
---

# Skill: Strategy Intake

## Mission
Validate the upstream research package and strategy context before decisions are made.

## Required checks
- research integrity status;
- target segment/geography match;
- freshness of time-sensitive claims/signals;
- unresolved contradictions;
- high-impact data gaps;
- availability and quality of performance history;
- business objective and capacity constraints.

## Output
Return `usable_evidence`, `limited_evidence`, `blocked_decisions`, `research_requests`, and a proposed strategy run scope.

Do not repair weak research by inventing missing facts.
