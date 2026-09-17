# Skills architecture

LeadUX Content Strategist intentionally separates context discovery, market evidence, buyer-state reasoning, positioning, distribution selection, strategic selection, and performance learning instead of using one large prompt.

| Skill | Responsibility | Must not do |
|---|---|---|
| identity-unpacking | Build confirmed founder/expert identity profile | Infer personality, values, expertise or goals |
| business-context | Capture commercial reality, offers, goals, resources and constraints | Invent pricing, economics, audience or priorities |
| strategy-intake | Validate research/context readiness | Repair weak evidence by invention |
| audience-icp-fit | Separate content audience, users, buyers, decision-makers and ICP | Fabricate personas or equate reach with ICP fit |
| customer-journey-intent | Map evidence-backed decision states, objections, proof needs and CTA boundaries | Infer purchase intent from engagement or force linear funnels |
| positioning-offer-fit | Select priority offers, supported promise and defensible reason-to-choose | Invent USP, differentiation, buyer pain or readiness |
| channel-distribution-fit | Select channel roles, formats, repurposing and measurement from audience/state/job/capability evidence | Recommend platforms by popularity or equate reach with business results |
| founder-brand-context | Merge confirmed context into strategy-safe working context | Upgrade hypotheses/unknowns into facts |
| strategy-memory | Load auditable history | Treat memory as market evidence |
| strategy-pattern-selection | Adapt reusable mechanisms from validated pattern library | Copy another creator's tactics/results blindly |
| objective-mapping | Map business goals to content jobs, audience action and approved distribution role | Default to vanity metrics |
| strategic-wedge | Choose differentiated way to compete | Invent whitespace |
| content-pillars | Define bounded strategic territories | Produce broad generic categories |
| content-opportunity-engine | Convert evidence into opportunities with audience, journey and distribution path | Treat trends/activity/reach as demand or business performance |
| portfolio-prioritization | Make trade-offs under capacity | Put everything in the plan |
| experiment-design | Make uncertainty testable | Fake scientific precision |
| strategy-challenger | Try to disprove decisions | Hide contradictions |
| content-briefing | Produce Creator-ready, channel-specific briefs | Write final content |
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
→ channel-distribution-fit
→ founder-brand-context
→ strategy-intake / downstream strategy
```

The ordering prevents four common failures:

1. inventing an ICP from broad audience language;
2. treating engagement or awareness as purchase intent;
3. inventing differentiation because a strategy template expects a USP;
4. recommending every popular platform without evidence that the target audience/state/job and business capacity actually fit the channel.

## Distribution model

Channel selection uses separate dimensions:

```text
WHO     → audience / role / ICP
STATE   → journey intent
JOB     → content/distribution job
WHERE   → channel
FORMAT  → execution packaging
ACTION  → desired next step
OUTCOME → measured result
```

The system keeps distribution signals, audience-response signals, lead signals and business outcomes separate.

## Upstream bridge

`integrations/leadux-competitor-research/skills/strategy-handoff/SKILL.md` is the bridge for the companion Research Agent.
