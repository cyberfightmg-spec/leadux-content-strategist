# Architecture

## System boundary

```text
┌──────────────────────────────┐
│ LeadUX Competitor Research   │
│ evidence collection/verify   │
└──────────────┬───────────────┘
               │ research package
               ▼
┌──────────────────────────────┐
│ LeadUX Content Strategist    │
│ decisions/priorities/tests   │
└──────────────┬───────────────┘
               │ Creator briefs
               ▼
┌──────────────────────────────┐
│ Creator / Production         │
│ final content assets         │
└──────────────┬───────────────┘
               │ published content
               ▼
┌──────────────────────────────┐
│ Performance observations     │
└──────────────┬───────────────┘
               │ feedback
               └──────────────► Strategist
```

## Why separate agents

Research has a different truth contract from strategy. Research reduces uncertainty and preserves evidence classes. Strategy makes choices under uncertainty. Creation optimizes execution within an approved brief.

Mixing them encourages the model to search for evidence that justifies a content idea it already wants to write.

## v0.1 state model

A strategy run may finish as:

- `READY`;
- `READY_WITH_GAPS`;
- `NEEDS_RESEARCH`;
- `BLOCKED`.

Individual challenger decisions may finish as:

- `SURVIVES`;
- `NARROWED`;
- `INVALIDATED`.
