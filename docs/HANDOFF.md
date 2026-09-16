# Research → Strategy Handoff v0.2

The upstream researcher owns evidence collection and verification. The strategist owns decisions under uncertainty.

## Stable IDs
Never regenerate upstream IDs. The strategist stores them as lineage references.

## Required route
`leadux-competitor-research` should add the bundled `integrations/leadux-competitor-research/skills/strategy-handoff/` skill and schema. That skill exports `research-package.json` compatible with this repository.

## Failure behavior
- `VERIFIED`: normal planning allowed.
- `VERIFIED_WITH_GAPS`: planning allowed with explicit affected gaps.
- `DEGRADED`: only scoped/low-confidence planning unless user knowingly accepts risk.
- `INSUFFICIENT_EVIDENCE`: strategist returns `NEEDS_RESEARCH` for decisions dependent on the missing evidence.
