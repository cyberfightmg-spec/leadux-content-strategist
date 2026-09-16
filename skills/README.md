# Skill catalog

This directory contains the specialized skills used by the root `SKILL.md` router.

## Core pipeline

`strategy-intake → strategy-memory → objective-mapping → strategic-wedge → content-pillars → content-opportunity-engine → portfolio-prioritization → experiment-design → strategy-challenger → content-briefing → synthesis`

Two skills run conditionally or after publication:

- `research-gap-router` sends evidence gaps back to the upstream Research Agent.
- `performance-learning` updates auditable strategy memory from first-party results.

## Contract

Each skill has a `SKILL.md` with Agent Skills-compatible YAML frontmatter plus an explicit mission, rules, and output contract. Machine-readable artifact definitions live in `../schemas/`.

The registry in `registry.json` is descriptive. The root router remains the source of truth for execution order.
