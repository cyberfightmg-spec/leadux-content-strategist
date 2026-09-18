---
name: content-opportunity-engine
description: >-
  Convert the validated strategic thesis, research, pillars, journey, distribution, and first-party
  learning into traceable content opportunities that exist because of a strategic choice.
metadata:
  version: 0.9.0
  category: content-strategy
  evidence_mode: required
license: MIT
---

# Skill: Content Opportunity Engine

## Mission
Generate content opportunities that implement the selected Strategic Thesis rather than merely sounding relevant.

## Opportunity construction

```text
selected strategic thesis
+
pillar
+
audience problem / next decision
+
proof mechanism
+
approved distribution role
+
market evidence / timing
+
first-party learning (optional)
→ content opportunity
```

## Required questions
For each candidate answer:
1. Which `thesis_id` causes this opportunity to exist?
2. Which where-to-play or strategic bet does it support?
3. Why this audience role and journey state?
4. Why this problem/decision?
5. Why this founder/brand and proof?
6. Why this offer/objective?
7. Why this approved channel/format?
8. Why now, if timing matters?
9. What evidence supports it?
10. What would make us stop?
11. Would this opportunity remain unchanged under the strongest alternative thesis?

If #11 is yes, mark it `GENERIC` unless an explicit infrastructural reason justifies it.

## Rules
- preserve lineage to thesis and upstream evidence IDs;
- do not infer demand from trend presence alone;
- do not infer competitor success from activity alone;
- do not copy competitor execution;
- do not target a non-ICP as buyer without an explicit content job;
- respect thesis trade-offs and `will_not_do`;
- weakly evidenced directions remain experiments;
- first-party observation does not prove causality.

## Output
Objects conforming to `schemas/content-opportunity.schema.json` plus:
- `strategic_thesis_id`;
- `thesis_link`;
- `coherence_status`;
- `proof_assets`;
- `selected_pattern_ids`;
- `rejection_or_stop_conditions`.
