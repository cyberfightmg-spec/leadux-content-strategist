---
name: content-opportunity-engine
description: >-
  Convert research, VOC, journey intent, channel/distribution fit, founder context, validated strategy patterns,
  and first-party history into traceable founder-fit content opportunities.
metadata:
  version: 0.8.0
  category: content-strategy
  evidence_mode: required
license: MIT
---

# Skill: Content Opportunity Engine

## Mission
Convert verified market evidence plus approved audience, journey, positioning, channel, Founder/Brand Context and first-party learning into specific content opportunities that this brand has a reason and a distribution path to pursue.

## Opportunity construction
A strong opportunity should combine as many of these as are genuinely available:

```text
audience problem / desired outcome
+
audience role / ICP status
+
journey state / next decision
+
market or competitor gap
+
founder credibility / proof
+
business or offer relevance
+
approved channel job / format fit
+
timing signal (optional)
+
first-party performance pattern (optional)
+
validated strategy mechanism (optional)
```

## Required questions
For each candidate answer:

1. Why this audience and role?
2. Why this journey state / next decision?
3. Why this problem/tension?
4. Why this founder/brand?
5. Why this business objective or offer?
6. Why now, if timing matters?
7. Why this angle instead of the obvious category angle?
8. Why this approved channel?
9. Why this format on that channel?
10. What is the intended next action and is CTA strength appropriate?
11. What evidence supports it?
12. What contradicts or weakens it?
13. What would make us defer/reject/stop it?

## Rules
- preserve lineage to upstream IDs;
- include relevant Audience / ICP Fit, Customer Journey, Positioning and Channel / Distribution Fit IDs;
- include relevant Founder/Brand Context references;
- include selected `pattern_id`s when an external mechanism influenced the opportunity;
- do not infer demand from trend presence alone;
- do not infer competitor success from activity alone;
- do not infer channel fit from platform popularity;
- do not infer lead/revenue potential from reach or engagement alone;
- do not copy competitor angles or formats merely because they are frequent;
- do not force an opportunity into a channel that is `DEFERRED` or `REJECTED`;
- `HYPOTHESIS` channel fit requires an explicit experiment framing;
- separate evergreen opportunity from timing advantage;
- mark weakly evidenced candidates as experiments;
- record contradictory evidence and unknowns;
- downgrade ideas that attract the wrong audience or dilute a priority offer/positioning;
- prefer opportunities that can be demonstrated with real proof over generic commentary.

## Channel adaptation rule
An opportunity may have one core strategic idea and multiple channel-specific executions, but each execution must preserve:

```text
audience role
+
journey job
+
positioning job
+
proof requirement
```

while adapting:

```text
format
+
depth
+
pacing
+
opening
+
CTA
+
proof presentation
```

to the selected channel.

Do not create identical cross-posting merely to increase channel count.

## Anti-copy rule
Competitor success, creator success, or a validated external pattern may establish that a mechanism deserves consideration. It does not justify cloning visible execution.

Always transform:

```text
external mechanism
→ brand-specific strategic job
→ differentiated angle
→ approved audience / journey
→ approved distribution surface
→ evidence/proof available to this brand
```

## Output
Objects conforming to `schemas/content-opportunity.schema.json` and include when known:
- `target_segment_ids`;
- `audience_roles`;
- `journey_state_ids`;
- `content_jobs`;
- `channel_fit_id`;
- `recommended_channel_ids`;
- `recommended_formats`;
- `desired_next_actions`;
- `founder_fit`;
- `commercial_fit`;
- `proof_assets`;
- `selected_pattern_ids`;
- `transfer_assumptions`;
- `rejection_or_stop_conditions`.
