---
name: customer-journey-intent
description: >-
  Map supported ICPs and buying roles to evidence-backed customer journey states, objections, triggers, trust needs, and content jobs without assuming funnel stage from demographics or platform behavior.
metadata:
  version: 0.7.0
  category: customer-journey
  evidence_mode: required
license: MIT
---

# Skill: Customer Journey / Funnel Intent

## Mission
Determine what state a supported audience or ICP is in relative to the problem, solution category, offer, and purchase decision so strategy can assign the right content job instead of treating everyone as one generic funnel stage.

This skill answers:

> What does this person already understand, what are they trying to decide next, what evidence do they need, and what content job is appropriate now?

## Absolute rule: no invented stage

Never assign a journey stage merely because someone:
- follows the account;
- watched a video;
- clicked a post;
- belongs to a demographic;
- works in a certain industry;
- visited a page;
- is labeled TOFU/MOFU/BOFU by convention.

When journey state is not evidenced, use `UNKNOWN` or a clearly labeled hypothesis.

## Required inputs
- `audience-icp-fit`;
- `business-context`;
- `positioning-offer-fit` when available;
- research/VOC/customer evidence;
- first-party funnel/performance evidence when available.

## Journey state model

Use these states when supported:

```text
UNAWARE
PROBLEM_AWARE
SOLUTION_AWARE
CATEGORY_EXPLORING
VENDOR_COMPARING
TRUST_VALIDATING
PURCHASE_READY
CUSTOMER_ONBOARDING
CUSTOMER_ADOPTION
RETENTION_EXPANSION
ADVOCACY
UNKNOWN
```

These are decision states, not a rigid linear funnel. A person may skip, regress, or occupy different states for different problems/offers.

## State evidence

For each state preserve:
- audience/ICP ID;
- buying role;
- problem/job;
- observed question or decision;
- evidence IDs;
- confidence;
- unresolved unknowns.

State confidence:

```text
CONFIRMED
SUPPORTED
HYPOTHESIS
UNKNOWN
```

## Decision questions by state

### UNAWARE
The audience is not yet actively framing the problem.
Content job: recognition, reframing, consequence, category education.
Do not force product CTA.

### PROBLEM_AWARE
They recognize the problem but may not know solution classes.
Content job: diagnosis, problem decomposition, cost/risk of inaction, desired outcome.

### SOLUTION_AWARE
They know solutions exist.
Content job: explain mechanisms, solution types, trade-offs, when each approach fits.

### CATEGORY_EXPLORING
They are actively researching the category.
Content job: evaluation criteria, frameworks, comparisons, implementation expectations.

### VENDOR_COMPARING
They compare providers/products/approaches.
Content job: differentiation, proof, scope, process, alternatives, fit/non-fit.

### TRUST_VALIDATING
They need confidence before acting.
Content job: cases, demonstrations, proof, limitations, objections, risk reduction.

### PURCHASE_READY
They have sufficient intent to take a commercial action.
Content job: concrete next step, offer clarity, scope, qualification, CTA.

### CUSTOMER_ONBOARDING
They bought and need successful activation.
Content job: orientation, setup, expectations, first value.

### CUSTOMER_ADOPTION
They need repeated successful use/delivery.
Content job: education, usage patterns, best practices, implementation support.

### RETENTION_EXPANSION
They already receive value and may renew, deepen, upgrade or cross-buy.
Content job: advanced outcomes, new use cases, expansion logic, retention proof.

### ADVOCACY
They are willing to recommend or contribute proof.
Content job: referral, case participation, community, co-creation.

## Buying-role rule

Journey state and buying role are separate axes.

Example:
- USER may be `SOLUTION_AWARE`;
- DECISION_MAKER may be `TRUST_VALIDATING`;
- BUYER may be `VENDOR_COMPARING`.

Do not collapse them into one persona.

## Objection and trust map

For each material state capture only supported:
- questions;
- objections;
- perceived risks;
- trust requirements;
- proof needed;
- alternatives considered;
- switching friction;
- trigger/event;
- desired next action.

Unknown objections remain unknown.

## Content job mapping

For each state map one or more content jobs:

```text
RECOGNIZE
DIAGNOSE
EDUCATE
REFRAME
COMPARE
PROVE
DE_RISK
QUALIFY
CONVERT
ONBOARD
ENABLE
RETAIN
EXPAND
ADVOCATE
```

Do not default every stage to conversion.

## CTA fit

CTA strength must match observed intent.

Examples:
- early-state content may use `learn`, `save`, `self-assess`, `explore`;
- comparison/trust states may use `see proof`, `review fit`, `request details`;
- purchase-ready states may use `book`, `buy`, `start`, `apply` when appropriate.

Do not infer purchase readiness from engagement alone.

## Non-linear journey rule

Do not force a single universal funnel. Different offers, segments, buying roles and markets may have different paths.

Represent supported transitions as:

```text
current_state → next_decision → evidence/content_needed → desired_action
```

## Output
Produce one object conforming to:

`schemas/customer-journey-intent.schema.json`

Also return:
- `primary_journeys`;
- `unknown_journey_states`;
- `content_jobs_by_state`;
- `proof_needs_by_state`;
- `objections_by_state`;
- `cta_boundaries`;
- `journey_gaps`;
- `research_requests`;
- `safe_for_strategy`.

## Quality gate
A full strategy must not:
- use TOFU/MOFU/BOFU as a substitute for actual customer-state reasoning;
- treat engagement as buying intent;
- use one CTA for every state;
- target a user with buyer messaging when roles differ;
- claim a customer journey is linear without evidence.

If a journey assumption materially affects offer, content job, CTA, or channel strategy and is unsupported, mark it as a hypothesis or request evidence.
