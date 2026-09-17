# Skills architecture

LeadUX Content Strategist intentionally separates context discovery, market evidence, buyer-state reasoning, strategic selection, and performance learning instead of using one large prompt.

| Skill | Responsibility | Must not do |
|---|---|---|
| identity-unpacking | Build confirmed founder/expert identity profile | Infer personality, values, expertise or goals |
| business-context | Capture commercial reality, offers, goals, resources and constraints | Invent pricing, economics, audience or priorities |
| strategy-intake | Validate research/context readiness | Repair weak evidence by invention |
| audience-icp-fit | Separate content audience, users, buyers, decision-makers and ICP | Fabricate personas or equate reach with ICP fit |
| customer-journey-intent | Map evidence-backed decision states, objections, proof needs and CTA boundaries | Infer purchase intent from engagement or force linear funnels |
| positioning-offer-fit | Select priority offers, supported promise and defensible reason-to-choose | Invent USP, differentiation, buyer pain or readiness |
| founder-brand-context | Merge confirmed context into strategy-safe working context | Upgrade hypotheses/unknowns into facts |
| strategy-memory | Load auditable history | Treat memory as market evidence |
| strategy-pattern-selection | Adapt reusable mechanisms from validated pattern library | Copy another creator's tactics/results blindly |
| objective-mapping | Map business goals to content jobs and audience action | Default to vanity metrics |
| strategic-wedge | Choose differentiated way to compete | Invent whitespace |
| content-pillars | Define bounded strategic territories | Produce broad generic categories |
| content-opportunity-engine | Convert evidence into opportunities | Treat trends/activity as demand/performance |
| portfolio-prioritization | Make trade-offs under capacity | Put everything in the plan |
| experiment-design | Make uncertainty testable | Fake scientific precision |
| strategy-challenger | Try to disprove decisions | Hide contradictions |
| content-briefing | Produce Creator-ready briefs | Write final content |
| synthesis | Compile final strategy | Remove unresolved gaps for neatness |
| performance-learning | Learn from first-party outcomes | Claim causality from correlation |
| research-gap-router | Request missing evidence | Fill gaps with model intuition |

## Pre-strategy pipeline

```text
identity-unpacking (when founder-led)
→ business-context
→ research handoff
→ audience-icp-fit
→ customer-journey-intent
→ positioning-offer-fit
→ founder-brand-context
→ strategy-intake / downstream strategy
```

The ordering prevents three common failures:

1. inventing an ICP from broad audience language;
2. treating engagement or awareness as purchase intent;
3. inventing differentiation because a strategy template expects a USP.

## Upstream bridge

`integrations/leadux-competitor-research/skills/strategy-handoff/SKILL.md` is the bridge for the companion Research Agent.
