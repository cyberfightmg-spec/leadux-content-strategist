# Changelog

## 0.9.0 — Strategy Formulation Engine
- Added first-class `strategy-diagnosis`, `strategy-formulation`, and `strategy-validation` skills.
- Added `strategic-thesis.schema.json` as the central strategy object.
- Full strategy now requires 2–4 materially distinct candidate theses plus exactly one `STATUS_QUO` baseline.
- Added non-compensatory hard gates: `EVIDENCE_VIABILITY`, `COMMERCIAL_FIT`, `CREDIBILITY_PROOF`, `CAPABILITY_CAPACITY`, and `ETHICAL_LEGAL_FIT`.
- A critical hard-gate failure can no longer be averaged away by a strong score elsewhere.
- Added strongest-alternative comparison and explicit selection rationale.
- Added explicit thesis trade-offs / `will_not_do`, strategic bets, critical assumptions, and reversal conditions.
- Added Strategy Validation with hard-gate recheck, coherence test, strongest-alternative review, pre-mortem, and reversal triggers.
- Refactored Strategy Challenger to attack the selected thesis rather than only downstream content decisions.
- Refactored Strategic Wedge, Content Pillars, Content Opportunities, Portfolio Prioritization, Experiments, Creator Briefs, and Synthesis to trace to the selected `thesis_id`.
- Added counterfactual coherence rule: if a recommendation would remain unchanged under the strongest alternative thesis, it is likely generic.
- Added deterministic semantic checks for one status quo, one selected thesis, hard-gate completeness, selected-thesis viability, validation consistency, and downstream thesis lineage.
- Strategy output schema now preserves diagnosis/formulation/validation IDs, all strategic options, selected thesis, strongest alternative, explicit trade-offs, and reversal triggers.
- CLI schema inference and tests updated for all v0.9 strategy-formulation objects.

## 0.8.0 — Channel / distribution fit
- Added first-class `channel-distribution-fit` skill after Positioning / Offer Fit.
- Added channel evidence states: `CONFIRMED_FIT`, `SUPPORTED_FIT`, `HYPOTHESIS`, `INSUFFICIENT_EVIDENCE`, `REJECTED`.
- Added channel priorities: `PRIMARY`, `SECONDARY`, `REPURPOSE_ONLY`, `EXPERIMENTAL`, `DEFERRED`, `REJECTED`.
- Added explicit separation of audience (`WHO`), journey state (`STATE`), content job (`JOB`), channel (`WHERE`), format (`FORMAT`), next action (`ACTION`) and measured result (`OUTCOME`).
- Added broad channel families covering owned site/search/email/messaging/social/video/community/marketplaces/partners/PR/paid/outbound/events.
- Added rule that platform popularity and competitor presence do not prove channel fit.
- Added owned vs rented distribution modeling and rented-to-owned paths.
- Added repurposing graph with source asset → derived asset → channel → audience/state → content job.
- Added operational-fit checks for production capability, sustainability, response burden, budget and compliance.
- Added measurement layers separating distribution signals, audience response, lead signals and business outcomes.
- Added `channel-distribution-fit.schema.json` and generic example.
- Founder / Brand Context, Strategy Intake, Quality Gates, Content Opportunities and Creator Briefs now consume Channel / Distribution Fit.
- Strategy request/output schemas can trace `channel_distribution_fit_id` and distribution assumptions.
- CLI schema inference and tests updated for Channel / Distribution Fit objects.

## 0.7.0 — Customer journey / funnel intent
- Added first-class `customer-journey-intent` skill between Audience / ICP Fit and Positioning / Offer Fit.
- Added evidence-backed journey states: `UNAWARE`, `PROBLEM_AWARE`, `SOLUTION_AWARE`, `CATEGORY_EXPLORING`, `VENDOR_COMPARING`, `TRUST_VALIDATING`, `PURCHASE_READY`, onboarding, adoption, retention/expansion, advocacy and `UNKNOWN`.
- Added strict separation between buying role and journey state.
- Added journey-state confidence: `CONFIRMED`, `SUPPORTED`, `HYPOTHESIS`, `UNKNOWN`.
- Added objections, perceived risks, trust requirements, proof needs, triggers, switching friction, next decisions and CTA-strength boundaries.
- Added explicit rule that engagement does not imply purchase intent.
- Added non-linear journey support; TOFU/MOFU/BOFU cannot replace actual customer-state reasoning.
- Added `customer-journey-intent.schema.json` and generic example.
- Positioning / Offer Fit now consumes journey evidence and cannot use a purchase-ready CTA without support.
- Founder / Brand Context now preserves role × journey-state mappings and journey confidence.
- Strategy Intake and Quality Gates now block `READY` when critical messaging/conversion decisions depend on invented journey intent.
- Root router, registry, CLI schema inference and tests updated for the new stage.

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
