---
name: content-opportunity-engine
description: >-
  Convert research, VOC, signals, founder context, validated strategy patterns, and first-party history into traceable founder-fit content opportunities.
metadata:
  version: 0.4.0
  category: content-strategy
  evidence_mode: required
license: MIT
---

# Skill: Content Opportunity Engine

## Mission
Convert verified market evidence plus Founder/Brand Context and first-party learning into specific content opportunities that this founder/brand has a reason to pursue.

## Opportunity construction
A strong opportunity should combine as many of these as are genuinely available:

```text
audience problem / desired outcome
+
market or competitor gap
+
founder credibility / proof
+
business or offer relevance
+
timing signal (optional)
+
first-party performance pattern (optional)
+
validated strategy mechanism (optional)
```

## Required questions
For each candidate answer:

1. Why this audience?
2. Why this problem/tension?
3. Why this founder/brand?
4. Why this business objective or offer?
5. Why now, if timing matters?
6. Why this angle instead of the obvious category angle?
7. Why this channel/format, if recommended?
8. What evidence supports it?
9. What contradicts or weakens it?
10. What would make us defer/reject/stop it?

## Rules
- preserve lineage to upstream IDs;
- include relevant Founder/Brand Context references;
- include selected `pattern_id`s when an external mechanism influenced the opportunity;
- do not infer demand from trend presence alone;
- do not infer competitor success from activity alone;
- do not copy competitor angles merely because they are frequent;
- separate evergreen opportunity from timing advantage;
- mark weakly evidenced candidates as experiments;
- record contradictory evidence and unknowns;
- downgrade ideas that attract the wrong audience or dilute a priority offer/positioning;
- prefer opportunities that can be demonstrated with founder proof over generic commentary.

## Anti-copy rule
Competitor success, creator success, or a proven external pattern may establish that a mechanism deserves consideration. It does not justify cloning the visible execution.

Always transform:

```text
external mechanism
→ LeadUX/founder-specific strategic job
→ differentiated angle
→ evidence/proof available to this brand
```

## Output
Objects conforming to `schemas/content-opportunity.schema.json` plus, where supported by the schema's open properties:
- `founder_fit`;
- `commercial_fit`;
- `proof_assets`;
- `selected_pattern_ids`;
- `transfer_assumptions`;
- `rejection_or_stop_conditions`.
