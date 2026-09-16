---
name: research-gap-router
description: >-
  Route strategy-blocking evidence gaps back to the upstream Research Agent as precise research requests.
metadata:
  version: 0.3.0
  category: content-strategy
  evidence_mode: required
license: MIT
---

# Skill: Research Gap Router

## Mission
Convert a strategy-blocking evidence gap into a precise upstream research request instead of filling the gap with model intuition.

## Trigger
Use when strategy intake or the challenger finds that a material decision cannot be supported by the current package.

## Output
Produce a `research-request.schema.json` artifact with:
- the blocked question;
- why it matters;
- evidence needed;
- suggested upstream research skills;
- blocked decision IDs;
- priority;
- a stop condition so research does not expand indefinitely.

## Routing examples
- unclear audience demand → `customer-research`, `voice-of-customer`;
- unclear competitor coverage → `competitor-profiling`, `gtm-intelligence`;
- timing/change uncertainty → `strategic-signals`, `market-monitoring`;
- contested fact → `contradiction-check`, `evidence-verification`;
- market gap claim → `market-whitespace` plus supporting customer/coverage evidence.

Do not ask the upstream researcher to prove a strategy that has already been chosen. Frame the request neutrally.
