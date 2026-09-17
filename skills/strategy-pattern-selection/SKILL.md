---
name: strategy-pattern-selection
description: >-
  Select only relevant strategy patterns from the validated pattern library and adapt them to current evidence, founder context, objectives, and constraints.
metadata:
  version: 0.4.0
  category: content-strategy
  evidence_mode: required
license: MIT
---

# Skill: Strategy Pattern Selection

## Mission
Use proven or promising strategic mechanisms as reusable reasoning patterns without treating another creator's tactics as universal truth.

Read:

`references/validated-strategy-patterns.json`

## Inputs
- Founder/Brand Context;
- research package;
- business/content objective;
- current channels/capacity;
- first-party performance history;
- strategy goal.

## Method
For every candidate pattern:
1. check whether its mechanism applies to this decision;
2. check evidence grade and limitations;
3. identify what must be adapted for this founder/brand;
4. reject patterns that conflict with actual evidence or constraints;
5. record the pattern ID when it materially influences a decision.

## Rules
- Never copy another creator's cadence, hook, channel mix, or content ratio solely because it worked for them.
- Separate a **mechanism** from a **tactic**.
- Prefer first-party evidence when it conflicts with generic best practice.
- Grade C patterns are experiments, not defaults.
- Grade A/B patterns may still be rejected when brand, audience, offer, geography, capacity, or platform conditions differ.
- Stars/forks/install counts are adoption evidence, not ROI proof.
- Author claims are not independent replication.

## Output
Return:
- `selected_pattern_ids`;
- `rejected_pattern_ids` with reasons;
- `adaptations`;
- `pattern_conflicts`;
- `strategy_implications`;
- `tests_required`.

## Quality gate
No full strategy should cite a generic best practice without either:
- a pattern ID plus adaptation rationale;
- first-party performance evidence;
- research evidence;
- or an explicit hypothesis/experiment label.
