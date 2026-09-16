# LeadUX Content Strategist

Open-source evidence-first strategy layer between market research and content creation.

```text
LeadUX Competitor Research
        ↓ verified research package
LeadUX Content Strategist
        ↓ strategy / portfolio / experiments / briefs
Creator
        ↓ published content
Performance observations
        └──────────────→ strategy memory / refresh
```

## What it is
This repository does **not** generate random content ideas and does **not** write final posts by default. It transforms verified market/customer/competitor research into traceable strategic choices.

Every material content opportunity can point back to upstream claim, insight, VOC, signal, market-opportunity and content-footprint IDs.

## v0.3 highlights
- root `SKILL.md` + 13 specialized strategy skills with YAML frontmatter and a machine-readable skill registry;
- installable deterministic CLI;
- JSON Schema + semantic integrity validation;
- Research → Strategy handoff integration skill and schema for `leadux-competitor-research`;
- content-opportunity scoring with explicit missing dimensions;
- portfolio buckets: core / responsive / experiment / deferred / rejected;
- strategy challenger;
- Creator briefs with evidence and forbidden claims;
- strategy memory + repetition warning;
- performance baselines and cautious learning loop;
- GitHub Actions tests.

## Install

```bash
pip install -e '.[dev]'
pytest
```

## Quick start

```bash
leadux-strategist validate examples/research-package.example.json
leadux-strategist preflight --research examples/research-package.example.json
leadux-strategist score examples/content-opportunity.example.json
```

See `docs/CLI.md`, `docs/HANDOFF.md`, and `docs/SKILLS.md` for details.
