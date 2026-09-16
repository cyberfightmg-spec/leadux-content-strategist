---
name: performance-learning
description: >-
  Convert observed content performance into cautious strategy updates while separating association from causal claims.
metadata:
  version: 0.3.0
  category: content-strategy
  evidence_mode: required
license: MIT
---

# Skill: Performance Learning

## Mission
Convert observed content outcomes into cautious strategy updates while keeping observation, association, and causality separate.

## Inputs
- performance observations;
- strategy memory;
- originating briefs/opportunities;
- platform/account/period context.

## Procedure
1. Validate observation records and missing metrics.
2. Build account/platform/period baselines where enough data exists.
3. Compare content against the stated baseline.
4. Group by controlled tags from Creator briefs: topic, angle, format, CTA intent, pillar, channel.
5. Propose performance patterns only when sample size and consistency justify them.
6. Store observation IDs and confounders with every pattern.
7. Update `historical_fit` only as an association signal, never as proof of future performance.
8. Recommend the next test that could strengthen or falsify the pattern.

## Hard rules
- unknown metric ≠ zero;
- views/followers ≠ business outcome by default;
- historical winners do not establish causality;
- no pattern without sample size and period;
- platform algorithm changes can stale old patterns;
- a strategy refresh must preserve old versions rather than overwrite history.

## Deterministic support
Use the v0.2 CLI baseline utilities where useful. Code calculates; the agent interprets with the limitations above.
