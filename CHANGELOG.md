# Changelog

## 0.6.0 — Audience / ICP fit
- Added first-class `audience-icp-fit` skill before positioning.
- Added strict separation between content audience, problem holder, user, buyer, decision-maker, influencer, champion, blocker and ICP.
- Added segment evidence states: `CONFIRMED_ICP`, `SUPPORTED_CANDIDATE`, `HYPOTHESIS`, `AUDIENCE_NOT_ICP`, `REJECTED`, `UNKNOWN`.
- Added segment priority states: `PRIMARY`, `SECONDARY`, `EXPERIMENTAL`, `DEFERRED`, `REJECTED`.
- Added `audience-icp-fit.schema.json` and generic example.
- Added explicit commercial-fit dimensions without imputing unknowns.
- Positioning / Offer Fit now consumes Audience / ICP Fit rather than inventing audience roles internally.
- Founder / Brand Context now preserves ICP, content-audience-only segments and buyer-role relationships.
- Strategy Intake and Quality Gates now block `READY` when the primary ICP is unsupported or content audience is confused with buyer ICP.
- Root router, registry, CLI schema inference and tests updated for the new stage.

## 0.5.0 — Universal context + positioning / offer fit
- Added universal `identity-unpacking` skill with strict no-inference interview protocol.
- Added universal `business-context` skill and schema.
- Added `positioning-offer-fit` as a first-class pre-strategy decision layer.
- Added `positioning-offer-fit.schema.json` and generic example.
- Added explicit offer buckets: PRIMARY / SECONDARY / EXPERIMENT / DEFERRED / REJECTED.
- Added promise evidence states: PROVEN / SUPPORTED / PLAUSIBLE_BUT_UNPROVEN / UNSUPPORTED.
- Added explicit `POSITIONING_GAP` instead of inventing differentiation.
- Added allowed / qualified / forbidden claim boundaries.
- Founder/Brand Context now merges confirmed identity + business + safe positioning/offer-fit.
- Strategy intake now blocks `READY` when the primary promise, audience, or reason-to-choose is materially unsupported.
- Root router and registry updated to run positioning/offer fit before downstream content strategy.
- CLI schema inference and tests now support positioning/offer-fit objects.

## 0.4.0 — Founder-aware validated-strategy architecture
- Added first-class `founder-brand-context` skill and JSON schema.
- Added public LeadUX founder/brand context example.
- Added `strategy-pattern-selection` skill.
- Added evidence-graded `validated-strategy-patterns.json` library.
- Added strategy-source audit separating adoption, independent usage, result evidence and replication strength.
- Upgraded root router and agent rules so full strategy requires both market evidence and founder/brand context.
- Added explicit anti-generic, brand-dilution, credibility-fit and commercial-fit gates.
- Added pattern IDs and transfer-assumption discipline to strategic reasoning.
- Added Marketing Council architecture attribution for skeptical counterweights and reversal criteria.
- Added external `content-performance-pattern` schema for normalized competitor/adjacent-creator outliers coming from LeadUX Competitor Research.
- Extended research-package and handoff infrastructure to preserve content-performance patterns, evidence levels, transfer assumptions and limitations.
- Strategy opportunities must distinguish observable content success from audience, lead and business outcomes.

## 0.3.0
- Packaged the project as a public Agent Skills repository.
- Added YAML frontmatter to the root router and every specialized skill.
- Added `skills/registry.json` and the skill catalog documentation.
- Formalized the `strategy-handoff` bridge as an installable upstream skill.
- Added skill metadata validation to CI/tests.
- Preserved deterministic schemas, semantic validation, CLI, memory and performance-learning infrastructure from v0.2.

## 0.2.0 — Executable strategy infrastructure
- Added installable Python package and `leadux-strategist` CLI.
- Added deterministic schema + semantic validation.
- Added upstream `strategy-handoff` integration pack for LeadUX Competitor Research.
- Expanded research handoff for VOC, strategic signals, content footprints, market opportunities, contradictions and gaps.
- Added transparent opportunity scoring that does not impute UNKNOWN values.
- Added strategy memory and duplicate/repetition warning.
- Added platform-neutral performance baselines and comparison helpers.
- Added workspace initializer/state manifest and GitHub Actions CI.
- Added strategy request, experiment, memory and performance-pattern schemas.

## 0.1.0 — Strategy kernel
- Initial evidence-first strategist contracts, skills and schemas.
