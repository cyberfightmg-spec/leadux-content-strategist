---
name: strategy-validation
description: >-
  Validate the selected strategic thesis before downstream planning by rechecking hard gates,
  running coherence and counterfactual tests, integrating challenger findings, performing a
  pre-mortem, and defining explicit reversal triggers.
metadata:
  version: 0.9.0
  category: strategy-formulation
  evidence_mode: required
license: MIT
---

# Skill: Strategy Validation

## Mission
Try to break the selected strategy **before** it becomes pillars, opportunities and execution.

Inputs:
- `strategy-formulation`;
- selected `strategic-thesis`;
- `strategy-challenger` output;
- all upstream evidence/context used by the thesis.

Output conforms to `schemas/strategy-validation.schema.json`.

## Validation is not another strategy generator

Do not quietly replace the selected thesis with a new idea.

Return:
- `SURVIVES`
- `NARROWED`
- `INVALIDATED`
- `BLOCKED`

If invalidated, route back to `strategy-formulation`.

## Test 1 — Hard-gate recheck

Re-evaluate:
- evidence viability;
- commercial fit;
- credibility/proof;
- capability/capacity;
- ethical/legal fit.

A thesis cannot pass because other dimensions compensate for a failed hard gate.

## Test 2 — Coherence test

For every major downstream implication ask:
1. Does this action follow from the selected thesis?
2. Would we still recommend it unchanged under a competing thesis?
3. Does it reinforce where-to-play and how-to-win?
4. Does it consume resources consistent with the trade-offs?
5. Does it preserve proof/claim boundaries?

Use:
- `COHERENT`
- `WEAKLY_LINKED`
- `GENERIC`
- `CONTRADICTORY`

A downstream element marked `GENERIC` must be narrowed, experimentally justified, or removed.

## Test 3 — Strongest alternative

Compare the selected thesis against the strongest rejected/deferred alternative.

Ask:
- What evidence would make the alternative superior?
- Did selection ignore any decisive fact?
- Is the difference material or mostly rhetorical?
- Is sunk-cost/status-quo bias influencing the choice?

## Test 4 — Pre-mortem

Assume the strategy failed after the stated horizon.

List the most plausible failure modes, especially:
- wrong ICP/problem priority;
- weak proof;
- channel dependency;
- insufficient capability/capacity;
- attractive content but weak commercial movement;
- copied category convention disguised as differentiation;
- unsupported causal assumption;
- offer/strategy mismatch;
- execution burden higher than expected.

Each failure mode must link to an observable warning sign where possible.

## Test 5 — Reversal triggers

Define evidence that should:
- continue the thesis;
- narrow it;
- switch an assumption into an experiment;
- reconsider the strongest alternative;
- stop the strategy.

Do not invent numeric thresholds when no baseline exists. Qualitative triggers are acceptable when explicit.

## Test 6 — Challenger integration

Use `strategy-challenger` as the skeptical sub-review.

No high-impact thesis may be `SURVIVES` if the challenger found an unresolved central contradiction, fatal proof gap, or capacity conflict.

## Final quality rule

A strategy is validated only if:
- it represents a real choice;
- alternatives were genuinely different;
- hard gates are acceptable;
- trade-offs are explicit;
- downstream actions can be traced to the thesis;
- major failure modes are visible;
- reversal evidence is defined.

A polished narrative is not validation.
