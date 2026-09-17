---
name: audience-icp-fit
description: >-
  Separate audience, user, buyer, decision-maker, problem-holder, and commercially viable ICP segments using explicit business context and verified market evidence without inventing personas.
metadata:
  version: 0.6.0
  category: audience-strategy
  evidence_mode: required
license: MIT
---

# Skill: Audience / ICP Fit

## Mission
Determine who the strategy should actually target and distinguish attention from buying fit.

This skill answers:

> Who has the problem, who uses the solution, who pays, who decides, who influences, who is reachable through content, and which of those people are commercially worth prioritizing?

## Absolute rule: no invented personas

Never invent:
- age;
- gender;
- income;
- company size;
- job title;
- budget;
- geography;
- buying trigger;
- objections;
- channel preference;
- decision authority;
- pain intensity;
- willingness to pay;
- urgency;
- ICP quality.

If a field is not explicit or research-supported, preserve `UNKNOWN`.

## Required distinction

Always separate these roles when relevant:

- `CONTENT_AUDIENCE` — consumes or follows content;
- `PROBLEM_HOLDER` — experiences the problem;
- `USER` — uses the product/service;
- `BUYER` — pays or owns budget;
- `DECISION_MAKER` — can approve purchase;
- `INFLUENCER` — materially influences the decision;
- `CHAMPION` — advocates internally;
- `BLOCKER` — can prevent purchase;
- `ICP` — segment the business deliberately wants and can serve well.

One person may hold several roles, but do not assume that automatically.

## Inputs
- `business-context`;
- `positioning-offer-fit`;
- `research-package`;
- VOC/customer research;
- first-party customer/sales data when available;
- identity/founder constraints only when they affect who the business wants to serve.

## Step 1 — Build candidate segments
Use only:
- explicit business target segments;
- observed customer segments;
- verified research segments;
- buyer/user roles found in VOC, reviews, interviews, communities, sales data, or official market sources.

Do not create synthetic persona names or demographic detail merely to make the strategy look complete.

## Step 2 — Role map
For each candidate segment identify, if known:
- problem holder;
- user;
- buyer;
- decision-maker;
- influencer/champion;
- blocker;
- content audience overlap.

Mark unresolved relationships explicitly.

## Step 3 — Problem / outcome fit
For each segment capture only evidenced:
- job-to-be-done;
- problem;
- desired outcome;
- workaround/current alternative;
- objection;
- buying trigger;
- urgency signal;
- switching reason;
- language used by the segment.

Separate frequency from intensity.
A frequently discussed problem is not automatically a high-value commercial problem.

## Step 4 — Commercial fit
Evaluate visible dimensions independently:
- problem relevance;
- ability/willingness to buy when evidenced;
- access to budget/decision authority;
- offer fit;
- proof/capability fit;
- delivery fit;
- geography/market fit;
- sales-cycle fit when known;
- strategic revenue fit;
- retention/recurring potential when known;
- reachability through current channels;
- founder/business willingness to serve the segment.

Unknown remains unknown.

## Step 5 — Evidence status
Every segment gets one status:

```text
CONFIRMED_ICP
SUPPORTED_CANDIDATE
HYPOTHESIS
AUDIENCE_NOT_ICP
REJECTED
UNKNOWN
```

Rules:
- `CONFIRMED_ICP` requires both commercial fit and evidence that the segment exists/has the problem;
- `SUPPORTED_CANDIDATE` has meaningful support but still lacks one or more buying/fit dimensions;
- `HYPOTHESIS` must be tested;
- `AUDIENCE_NOT_ICP` may be useful for reach/community but should not drive sales strategy;
- `REJECTED` must include the reason;
- `UNKNOWN` means insufficient evidence to classify.

## Step 6 — Content audience vs sales ICP
Produce two separate maps:

### Content audience map
Who is worth attracting for:
- reach;
- credibility;
- referrals;
- community;
- education;
- future demand creation.

### Sales ICP map
Who is worth prioritizing for:
- current offers;
- near-term revenue;
- repeatability;
- strategic fit;
- delivery fit.

Do not force these maps to be identical.

## Step 7 — Priority
Classify segments:

```text
PRIMARY
SECONDARY
EXPERIMENTAL
DEFERRED
REJECTED
```

Priority must be justified by evidence and business goals, not merely market size or content engagement.

## Step 8 — Research gaps
When ICP quality cannot be determined, request the smallest useful evidence set, for example:
- customer interviews;
- sales call notes;
- CRM win/loss data;
- VOC by segment;
- willingness-to-pay evidence;
- buyer-role evidence;
- conversion by segment;
- repeat purchase/retention by segment.

Do not request data that will not change the decision.

## Output
Produce one object conforming to:

`schemas/audience-icp-fit.schema.json`

Also return:
- `primary_icp_ids`;
- `secondary_icp_ids`;
- `content_audience_ids`;
- `audience_not_icp_ids`;
- `rejected_segment_ids`;
- `unknown_role_relationships`;
- `research_requests`;
- `questions_required_from_user`;
- `safe_for_positioning`;
- `safe_for_strategy`.

## Quality gate
A full commercial content strategy cannot be `READY` when:
- the primary segment is only a demographic guess;
- content audience and buyer are conflated without evidence;
- the decision-maker/buyer role materially matters but is unknown;
- the primary ICP is unsupported;
- a rejected/non-target segment is driving content merely because it gets more engagement.
