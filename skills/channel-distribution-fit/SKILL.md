---
name: channel-distribution-fit
description: >-
  Select and assign channel roles using supported audience presence, customer-journey intent, content-job fit, format capability, business resources, and observable performance instead of platform popularity.
metadata:
  version: 0.8.0
  category: distribution-strategy
  evidence_mode: required
license: MIT
---

# Skill: Channel / Distribution Fit

## Mission
Decide **where content should be distributed, what job each channel performs, which audience/role/state it serves, and whether the business can execute that channel sustainably**.

This skill is not a social-platform popularity recommender.

```text
audience-icp-fit
+
customer-journey-intent
+
business-context
+
positioning-offer-fit
+
research-package
+
first-party channel performance (when available)
→ channel-distribution-fit
```

## Absolute rule: no invented channel fit

Never invent:
- that a target audience uses a platform;
- that a platform produces leads or sales;
- channel ROI;
- organic reach;
- CPM/CPC/CAC;
- conversion rate;
- posting frequency required for success;
- best posting time;
- algorithm preference;
- format preference of the target audience;
- competitor channel performance;
- whether a channel is necessary because it is popular.

Unknown evidence remains `UNKNOWN`.

## Channel is not audience, intent, or outcome

Keep these separate:

```text
WHO     → audience / ICP / buying role
STATE   → customer-journey intent
JOB     → what content/distribution must accomplish
WHERE   → channel / surface
FORMAT  → how the message is packaged
ACTION  → desired next step
OUTCOME → measured result
```

A platform does not automatically define the audience or funnel stage.

## Channel families

Evaluate any relevant distribution surface, not only social media:

- `OWNED_SITE` — website, blog, landing pages, product pages;
- `SEARCH` — organic search / answer discovery;
- `EMAIL` — newsletter, lifecycle, nurture;
- `MESSAGING` — Telegram, WhatsApp, Messenger, direct communities;
- `SOCIAL_FEED` — LinkedIn, Instagram, Threads, X, VK, etc.;
- `SHORT_VIDEO` — Reels, Shorts, TikTok-like surfaces;
- `LONG_VIDEO` — YouTube and comparable video libraries;
- `COMMUNITY` — forums, professional groups, Discord/Slack communities;
- `MARKETPLACE_DIRECTORY` — marketplaces, review directories, app/service catalogs;
- `PARTNER` — partner newsletters, integrations, affiliates, co-marketing;
- `PR_EARNED` — publications, podcasts, media, guest appearances;
- `PAID` — paid social/search/native/sponsorship;
- `OUTBOUND` — direct outreach where lawful/appropriate;
- `EVENT` — webinars, workshops, conferences, offline events;
- `OTHER`.

The same named platform may perform different jobs and should not be treated as one universal channel role.

## Evidence states

For each channel/segment/state combination classify evidence:

```text
CONFIRMED_FIT
SUPPORTED_FIT
HYPOTHESIS
INSUFFICIENT_EVIDENCE
REJECTED
```

Definitions:
- `CONFIRMED_FIT` — reliable first-party evidence shows the channel works for the intended audience/job/outcome.
- `SUPPORTED_FIT` — credible external/market evidence plus business capability supports use, but first-party confirmation is limited.
- `HYPOTHESIS` — strategically plausible and testable but unproven.
- `INSUFFICIENT_EVIDENCE` — too little evidence to prioritize confidently.
- `REJECTED` — explicit conflict with audience, resources, economics, compliance, positioning, or observed performance.

## Channel priority

Classify each channel:

```text
PRIMARY
SECONDARY
REPURPOSE_ONLY
EXPERIMENTAL
DEFERRED
REJECTED
```

Do not make every channel `PRIMARY`.

## Step 1 — Map channel to audience and buying state

For each candidate channel identify:
- audience/segment IDs;
- relevant buying roles;
- relevant journey-state IDs;
- evidence that those people/states are reachable there;
- content job(s) the channel can perform.

Never use generic platform demographics as proof of fit for a specific ICP without qualification.

## Step 2 — Assign a distribution job

Choose one or more explicit jobs:

```text
DISCOVER
EDUCATE
FRAME_PROBLEM
BUILD_TRUST
PROVE
COMPARE
DE_RISK
QUALIFY
CONVERT
NURTURE
ONBOARD
ADOPT
RETAIN
EXPAND
ADVOCATE
COMMUNITY
RECAPTURE
```

A channel may have several jobs, but one should normally be primary for a given audience/state combination.

## Step 3 — Evaluate format / message fit

For each channel evaluate only supported or testable format capabilities:
- text depth;
- short video;
- long video;
- image/carousel;
- live/demo;
- searchable evergreen content;
- conversational/direct response;
- downloadable/lead-magnet delivery;
- case-study/proof presentation;
- comparison/evaluation support.

Do not force the same asset unchanged into every channel.

Repurposing must preserve the strategic message while adapting packaging to the distribution surface.

## Step 4 — Evaluate operational fit

Check:
- founder/team production capability;
- sustainable cadence, if explicitly known;
- editing/design burden;
- moderation/community burden;
- sales-response burden;
- paid budget when applicable;
- tooling/automation available;
- legal/compliance restrictions;
- language/geography limitations;
- dependency risk on one rented platform.

Unknown capacity remains unknown.

## Step 5 — Evaluate economic / conversion fit

Use only known evidence for:
- lead quality;
- sales conversations;
- assisted conversions;
- attributable conversions;
- cost per lead/customer;
- retention/expansion contribution;
- revenue influence.

Views, followers, likes, comments and watch time are **content/distribution signals**, not business outcomes by default.

## Step 6 — Owned vs rented distribution

For each strategy distinguish:

```text
RENTED_DISTRIBUTION
→ social/platform reach controlled by third party

OWNED_ASSET
→ email list, website, subscriber/customer database, community or other permissioned asset
```

When relevant, define how rented attention can move into an owned relationship without forcing a conversion CTA too early.

Do not assume every business needs an email list/community; evaluate fit first.

## Step 7 — Channel portfolio

Build a portfolio rather than a platform checklist.

A typical portfolio may include different roles such as:
- one primary discovery surface;
- one trust/depth surface;
- one owned nurture surface;
- one conversion/evaluation surface;
- one experimental channel.

This is a pattern, not a mandatory template.

Choose fewer channels when capacity is constrained.

## Step 8 — Repurposing graph

When useful, define:

```text
SOURCE_ASSET
→ DERIVED_ASSET
→ CHANNEL
→ AUDIENCE / STATE
→ CONTENT JOB
```

Example mechanism:

```text
long-form demonstration
→ short proof clip
→ discovery channel
→ PROBLEM_AWARE buyer
→ BUILD_TRUST
```

Do not assume one source asset should be distributed everywhere.

## Step 9 — Measurement contract

For each priority channel define metrics by level:

### Distribution signals
- impressions/reach;
- views;
- watch/read depth;
- saves/shares;
- clicks.

### Audience-response signals
- relevant replies/comments;
- return visitors/viewers;
- qualified subscriptions;
- direct questions.

### Lead signals
- qualified inquiries;
- booked calls;
- demo/trial requests;
- lead captures where relevant.

### Business outcomes
- customers;
- revenue;
- retention/expansion;
- other explicit commercial outcome.

Do not collapse these levels into one success score.

## Step 10 — Channel experiment design

For `HYPOTHESIS` channels specify:
- audience/state;
- content job;
- format;
- test duration or sample requirement if known;
- observable metric;
- baseline where available;
- continuation condition;
- rejection/defer condition;
- confounders.

Do not invent numeric thresholds merely to complete the experiment.

## Conflict handling

Surface conflicts such as:
- audience present but business lacks production capability;
- high reach but poor lead quality;
- strong first-party performance but wrong current ICP;
- platform works for awareness but not evaluation/conversion;
- founder likes a channel but target buyer evidence is weak;
- competitor success but transfer conditions differ;
- owned channel strategically useful but audience acquisition source is unknown.

Do not resolve these conflicts silently.

## Output

Produce one object conforming to:

`schemas/channel-distribution-fit.schema.json`

Include:
- `channel_fit_id`;
- `audience_icp_fit_id`;
- `customer_journey_intent_id`;
- `channels`;
- `primary_channel_ids`;
- `secondary_channel_ids`;
- `repurpose_only_channel_ids`;
- `experimental_channel_ids`;
- `deferred_channel_ids`;
- `rejected_channel_ids`;
- `repurposing_graph`;
- `owned_distribution_plan`;
- `measurement_contract`;
- `channel_gaps`;
- `research_requests`;
- `questions_required_from_user`;
- `safe_for_strategy`.

## Quality gate

A full channel strategy cannot be `READY` when:
- channels are selected only because they are popular;
- primary channel has no supported audience/job relationship;
- the plan exceeds known execution capacity;
- engagement is presented as sales performance;
- conversion expectations are invented;
- channel roles conflict with Customer Journey Intent;
- the system cannot explain why each primary channel exists.
