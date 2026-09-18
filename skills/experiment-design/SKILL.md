---
name: experiment-design
description: >-
  Turn uncertain strategic-thesis assumptions and downstream tactics into falsifiable experiments
  with explicit signals, confounders, review windows, and reversal logic.
metadata:
  version: 0.9.0
  category: content-strategy
  evidence_mode: required
license: MIT
---

# Skill: Experiment Design

## Mission
Use experiments to reduce uncertainty around the selected Strategic Thesis without pretending uncertain outcomes are known.

## Required inputs
- selected `strategic-thesis`;
- critical assumptions / strategic bets;
- strategy validation findings;
- thesis-linked strategy decisions.

## Every experiment states
- `strategic_thesis_id`;
- strategic bet or assumption being tested;
- hypothesis;
- changed variable;
- audience/segment;
- journey state when relevant;
- channel/format when relevant;
- observable leading signal;
- business-relevant lagging signal where measurable;
- evaluation window;
- confounders;
- continuation evidence;
- narrowing evidence;
- reversal/kill evidence.

## Rules
- do not fabricate thresholds;
- do not call an observational comparison causal proof;
- do not test multiple strategic variables at once when that prevents interpretation;
- do not optimize only proxy engagement when the assumption is commercial;
- a failed experiment may invalidate an assumption, not automatically the entire thesis;
- a repeated failure against a critical assumption must route back to Strategy Validation/Formulation.

## Output
Experiment objects plus explicit links to `thesis_id`, `bet_id`, or `assumption_id`.
