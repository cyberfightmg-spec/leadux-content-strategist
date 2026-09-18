---
name: strategy-challenger
description: >-
  Red-team the selected strategic thesis, its hard-gate assumptions, trade-offs, strongest
  alternative, evidence lineage, and reversal conditions before downstream content strategy.
metadata:
  version: 0.9.0
  category: strategy-formulation
  evidence_mode: required
license: MIT
---

# Skill: Strategy Challenger

## Mission
Try to disprove, narrow, or redirect the **selected strategic thesis** before it becomes pillars, opportunities, and execution.

The challenger is not a stylistic critic. It attacks the quality of the strategic choice.

## Required inputs
- selected `strategic-thesis`;
- strongest alternative thesis;
- `strategy-diagnosis`;
- `strategy-formulation`;
- evidence lineage;
- Founder/Brand Context;
- relevant journey/distribution context.

## Challenge categories

### Choice quality
- Are the alternatives materially different or merely differently worded?
- Did the formulation include a real status-quo baseline?
- Why was the selected thesis chosen over the strongest alternative?
- Did an aggregate score hide a fatal weakness?
- Is the choice actually a compromise that avoids a real trade-off?

### Hard gates
Attack:
- `EVIDENCE_VIABILITY`;
- `COMMERCIAL_FIT`;
- `CREDIBILITY_PROOF`;
- `CAPABILITY_CAPACITY`;
- `ETHICAL_LEGAL_FIT`.

A fatal gate failure cannot be compensated by market attractiveness or reach.

### Evidence quality
- weak/stale/contradictory lineage;
- upstream hypothesis silently upgraded;
- competitor activity treated as success;
- engagement treated as purchase intent;
- observational performance treated as causal proof;
- external pattern applied outside transfer conditions.

### Strategic coherence
- where-to-play does not match primary objective;
- how-to-win is generic or copyable unchanged;
- economic logic is disconnected from content logic;
- distribution logic contradicts channel evidence;
- selected thesis requires proof the brand does not have;
- proposed action would be unchanged under a competing thesis.

### Trade-offs
- too many audiences/offers/channels remain "primary";
- attractive but non-core opportunities are not actually rejected/deferred;
- resources are not concentrated;
- `will_not_do` is cosmetic rather than consequential.

### Failure and reversal
- critical assumptions have no observable signal;
- no pre-mortem exists;
- no reversal condition exists;
- status quo or strongest alternative is never reconsidered.

## Strongest-alternative test

Ask:

> What evidence would make the strongest rejected/deferred thesis superior to the selected one?

If the answer is "none", the review is probably biased.

## Pattern-transfer challenge
When a `pattern_id` materially influenced the thesis:
1. What exactly is being transferred: mechanism or tactic?
2. What conditions made it work upstream?
3. Which conditions are present here?
4. Which are unknown or materially different?
5. What first-party evidence could confirm or reject the transfer?

## Output
Return:
- `SURVIVES | NARROWED | INVALIDATED`;
- strongest objection;
- hard-gate objections;
- contradictory/supporting evidence;
- strongest-alternative challenge;
- thesis coherence problems;
- required change;
- what evidence would settle unresolved disagreement;
- reversal condition.

If a central hard gate fails or the options were not materially distinct, return `INVALIDATED`.
