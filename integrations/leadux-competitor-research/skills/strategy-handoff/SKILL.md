---
name: strategy-handoff
description: >-
  Export a verified LeadUX Competitor Research run into the normalized research package consumed by LeadUX Content Strategist.
metadata:
  version: 0.3.0
  category: research-integration
  evidence_mode: required
license: MIT
---

# Skill: Strategy Handoff

## Mission
Export a strategy-ready evidence package from a completed LeadUX Competitor Research run without reinterpreting or upgrading the upstream evidence.

## Hard boundary
This skill packages research. It does not decide content pillars, topics, channels, formats, cadence, hooks, or creative angles.

## Required preconditions
For deep/full work, run upstream quality gates first:

```text
contradiction-check
→ evidence-verification
→ red-team
→ synthesis
→ strategy-handoff
```

If the research integrity status is `INSUFFICIENT_EVIDENCE`, export may still occur for diagnosis, but the package must preserve that status and must not imply strategy readiness.

## Export selection
Include only artifacts relevant to strategic content decisions and preserve stable upstream IDs:
- research run metadata;
- claims and insights;
- market opportunities;
- VOC records/themes;
- strategic signals;
- GTM/content-footprint artifacts;
- contradictions;
- data gaps.

Do not flatten IDs into prose. Do not rewrite `HYPOTHESIS` as `FACT`. Do not drop contradicting claims because they make downstream planning harder.

## Output
Produce one JSON object conforming to:

`schemas/strategy-handoff.schema.json`

Populate `handoff.generated_at`, `handoff.producer_version`, `handoff.selection_notes`, and `handoff.omitted_artifact_types`.

## Quality checks
- every insight reference resolves to a claim in the package or is explicitly documented as omitted;
- all stable IDs are preserved exactly;
- freshness dates are preserved where available;
- integrity status matches the research run;
- no strategic recommendation is added during export.
