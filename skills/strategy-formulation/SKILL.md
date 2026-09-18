---
name: strategy-formulation
description: >-
  Generate materially distinct strategic theses from a diagnosis, reject options that fail hard
  gates, compare surviving alternatives without hiding trade-offs in an aggregate score, and select
  one primary thesis with explicit bets, assumptions, and things the strategy will not do.
metadata:
  version: 0.9.0
  category: strategy-formulation
  evidence_mode: required
license: MIT
---

# Skill: Strategy Formulation

## Mission
Convert a validated diagnosis into a **real strategic choice**.

This skill is the center of the Strategist.

It must not jump from evidence to pillars. It must create competing strategic theses, test their viability, compare them, choose one primary thesis, and make the sacrifice explicit.

Inputs:
- `strategy-diagnosis`;
- `objective-mapping`;
- `founder-brand-context`;
- `research-package`;
- `strategy-memory`;
- selected/rejected `pattern_id`s;
- first-party performance where available.

Outputs:
- `schemas/strategy-formulation.schema.json`;
- each thesis conforms to `schemas/strategic-thesis.schema.json`.

## Core principle

Different wording is not a different strategy.

Two options are materially distinct only if choosing one changes at least two of these:
- **where to play** — audience, buying situation, problem/category, geography or demand state;
- **how to win** — advantage mechanism or reason to choose;
- **economic logic** — how the strategy contributes to revenue/asset creation;
- **proof mechanism** — how trust is earned;
- **distribution logic** — where/how attention and trust are accumulated;
- **resource allocation** — what receives scarce time/budget/capacity;
- **trade-offs** — what is deliberately not pursued.

If options differ only in wording, hooks, formats, topics, cadence, or slogans, collapse them.

## Step 1 — Generate 2–4 material options + status quo

Produce:
- 2–4 genuinely different candidate theses;
- one `STATUS_QUO` / do-nothing baseline.

The baseline exists to prevent forced change. Sometimes the evidence does not justify a strategic pivot.

Do not generate extra options merely to satisfy a number. If only two materially distinct options exist, return two plus status quo.

## Step 2 — Build each Strategic Thesis

Every thesis must specify:

```text
OBJECTIVE
WHERE TO PLAY
HOW TO WIN
ADVANTAGE SOURCE
ECONOMIC LOGIC
CONTENT / TRUST MECHANISM
DISTRIBUTION LOGIC
STRATEGIC BETS
TRADE-OFFS / WHAT WE WILL NOT DO
CAPABILITIES REQUIRED
CRITICAL ASSUMPTIONS
EVIDENCE LINEAGE
FAILURE / REVERSAL CONDITIONS
TIME HORIZON
```

Pillars, post ideas, hooks and calendars are downstream and do not belong here.

## Step 3 — Apply non-compensatory hard gates

Before comparing options, test each against:

1. `EVIDENCE_VIABILITY`
2. `COMMERCIAL_FIT`
3. `CREDIBILITY_PROOF`
4. `CAPABILITY_CAPACITY`
5. `ETHICAL_LEGAL_FIT`

Gate statuses:
- `PASS`
- `CONDITIONAL`
- `FAIL`
- `UNKNOWN`

Rules:
- a critical `FAIL` makes the thesis `INVALIDATED`;
- a critical `UNKNOWN` prevents unconditional selection;
- a gate cannot be rescued by strong scores on other dimensions;
- do not average a fatal weakness away.

An option with strong market attractiveness but no credible proof can be an experiment, not the primary strategy.

## Step 4 — Compare surviving options

Compare visibly on:
- expected strategic leverage;
- strength of evidence;
- commercial relevance;
- founder/brand credibility;
- defensibility/distinctiveness;
- strategic compounding value;
- time to useful learning;
- reversibility;
- dependency risk;
- channel/distribution support;
- capability burden;
- opportunity cost.

Do **not** let an aggregate score choose the strategy.

If a sortable score is used as an aid, expose all dimensions, missing values, weights, and the fact that it is not a prediction.

## Step 5 — Select one primary thesis

A full strategy has exactly one `SELECTED` primary thesis.

Other options become:
- `REJECTED`
- `DEFERRED`
- `EXPERIMENTAL`
- `INVALIDATED`

Selection rationale must answer:

> Why this thesis instead of the strongest alternative?

If the answer is only "highest score", selection failed.

## Step 6 — Make trade-offs explicit

For the selected thesis state:
- which audiences are not primary;
- which offers are not being led with;
- which channels are secondary/deferred;
- which content territories are excluded;
- which attractive opportunities are intentionally ignored;
- what resource is being concentrated and where.

Strategy without sacrifice is not strategy.

## Step 7 — Define strategic bets

Each bet must state:
- what must become true;
- why it is plausible;
- evidence supporting it;
- what remains uncertain;
- first observable signal;
- what would invalidate/reverse the bet.

A strategic bet is not a fabricated forecast.

## Step 8 — Hand off downstream

The selected thesis constrains:
- strategic wedge;
- content pillars;
- channel roles;
- content opportunities;
- portfolio allocation;
- experiments;
- Creator briefs.

Every downstream decision must be able to state:

```text
THIS EXISTS BECAUSE OF THESIS [thesis_id]
```

If it cannot, it is generic or strategically disconnected.
