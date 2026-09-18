---
name: strategic-wedge
description: >-
  Derive the content-facing strategic wedge from a validated selected strategic thesis without
  changing the thesis or inventing a new strategy.
metadata:
  version: 0.9.0
  category: content-strategy
  evidence_mode: required
license: MIT
---

# Skill: Strategic Wedge

## Mission
Translate the validated Strategic Thesis into the differentiated **content-facing way to compete**.

The wedge is downstream of strategy. It must not replace or silently rewrite the selected thesis.

## Required inputs
- selected `strategic-thesis`;
- `strategy-validation` result;
- audience/VOC evidence;
- Founder/Brand Context;
- proof assets/right-to-speak;
- channel/distribution constraints.

## Method
Derive the wedge from:
- thesis `where_to_play`;
- thesis `how_to_win`;
- thesis `advantage_source`;
- thesis `content_trust_mechanism`;
- thesis `tradeoffs`;
- thesis `will_not_do`.

Test:
1. **Thesis fidelity** — does the wedge clearly come from the selected thesis?
2. **Audience relevance** — is it meaningful to the priority buying situation?
3. **Founder credibility** — can this brand explain, demonstrate, or prove it?
4. **Distinctiveness** — could a direct competitor use it unchanged?
5. **Repeatability** — can it support repeated content?
6. **Distribution fit** — can it work through approved channel roles?
7. **Proof fit** — are claims inside approved boundaries?

## Coherence rule
Complete:

> This wedge exists because thesis [thesis_id] chose ______ over ______.

If this cannot be answered, the wedge is generic.

## Output
Return:
- `thesis_id`;
- selected wedge;
- supporting evidence/context IDs;
- proof assets;
- commercial connection;
- risks;
- explicit `will_not_compete_on`;
- downstream implications.

Do not generate a second strategy here.
