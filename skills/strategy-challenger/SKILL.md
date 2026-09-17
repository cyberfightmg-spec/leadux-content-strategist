---
name: strategy-challenger
description: >-
  Red-team strategic decisions, test transfer assumptions and founder fit, surface weak lineage and alternative explanations, and narrow or invalidate unsupported choices.
metadata:
  version: 0.4.0
  category: content-strategy
  evidence_mode: required
license: MIT
---

# Skill: Strategy Challenger

## Mission
Try to disprove, narrow, or redirect the proposed strategy before it becomes a plan.

The challenger is not a stylistic critic. It attacks decision quality.

## Challenge categories
- weak evidence lineage;
- stale or contradictory evidence;
- alternative explanations;
- audience mismatch;
- founder credibility/right-to-speak mismatch;
- active-offer / commercial-priority mismatch;
- recommendation could be copied unchanged by a competitor;
- brand dilution or audience confusion;
- resource/capacity mismatch;
- channel dependency;
- overfitting to recent winners;
- trend chasing;
- duplicated pillars/opportunities;
- missing falsification or reversal criteria;
- risk that proxy metrics replace business outcomes;
- external strategy pattern applied outside its transfer conditions;
- author-reported success treated as independent proof;
- popular tactic copied without evidence that the underlying mechanism fits this brand.

## Pattern-transfer challenge
When a `pattern_id` materially influenced a decision, ask:

1. What exactly is being transferred: mechanism or tactic?
2. What conditions made it work upstream?
3. Which of those conditions are present here?
4. Which are unknown or different?
5. What first-party evidence could confirm or reject the transfer?

## Founder-specific challenge
Ask:

> Why is this recommendation especially suitable for this founder/brand?

If the answer relies only on category popularity, invalidate or narrow it.

## Output per decision
Return:
- `SURVIVES | NARROWED | INVALIDATED`;
- strongest objection;
- contradictory/supporting evidence;
- founder/brand conflict if any;
- external pattern transfer risk if any;
- required change;
- what evidence would settle unresolved disagreement;
- reversal condition.
