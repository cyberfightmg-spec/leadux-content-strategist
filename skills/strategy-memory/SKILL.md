---
name: strategy-memory
description: >-
  Load auditable prior strategy, published content, and first-party performance history without treating memory as evidence.
metadata:
  version: 0.3.0
  category: content-strategy
  evidence_mode: required
license: MIT
---

# Skill: Strategy Memory

## Mission
Load auditable prior strategy and published-content history so the strategist avoids accidental repetition and can use first-party performance carefully.

## Inputs
- `strategy-memory.schema.json` artifact;
- current research package;
- current strategy request.

## Procedure
1. Identify previously used topics, angles, formats, pillars and channels.
2. Flag near-duplicates for review; do not auto-reject them.
3. Identify stale pillars/opportunities that may need revalidation.
4. Load performance patterns with their sample size, period and confounders.
5. Pass relevant `performance_pattern_ids` into opportunity lineage.

## Rules
- memory records must be auditable;
- absence from memory is not proof content was never published;
- lexical duplicate checks are warnings, not semantic truth;
- historical performance changes `historical_fit`, not market evidence;
- never use another account's performance as if it were the current brand's history.
