---
name: identity-unpacking
description: >-
  Collect and structure a founder, expert, creator, or personal-brand identity profile through explicit answers only, using a strict no-inference protocol before strategy begins.
metadata:
  version: 0.5.0
  category: founder-strategy-intake
  evidence_mode: user-confirmed
license: MIT
---

# Skill: Identity Unpacking

## Mission
Build a strategy-ready identity profile for any founder, expert, creator, consultant, operator, or personal brand before content strategy starts.

This skill is universal. It must not assume anything about LeadUX, any specific person, industry, offer, geography, worldview, or business model.

## Core model
Collect four primary groups:

1. `personal` — what the person is willing to make public and what should remain private;
2. `definition` — how the person defines themselves in their own words;
3. `expertise` — what they can actually do, prove, teach, sell, or are still learning;
4. `values` — principles, boundaries, refusals, and ethical constraints.

Optional strategy-relevant groups may be collected when needed:
- goals;
- business model;
- offers;
- audiences;
- proof assets;
- channels;
- capacity.

## Absolute no-inference rule
Never infer, assume, psychoanalyze, complete, embellish, or normalize a missing identity field into a stronger claim.

Do not infer identity from:
- writing style;
- profession alone;
- project list;
- follower count;
- geography;
- demographic stereotypes;
- interests;
- market research;
- competitor behavior;
- previous assistant interpretations.

If a field matters and is not explicitly established:

```text
UNKNOWN
→ ask a direct question
→ wait for answer
→ record answer
```

## Four blocks

### 1. Personal / Личное
Collect only what the person chooses to make relevant to public strategy:
- relationships / family roles;
- life context;
- interests;
- personal topics allowed in content;
- personal topics that must remain private.

Do not force private disclosure. `prefer not to answer` is a valid final value.

### 2. Definition / Определение
Capture how the person defines themselves:
- self-definition;
- public roles;
- labels they accept;
- labels they reject;
- origin/location/age/gender only when voluntarily stated and strategy-relevant.

Use the person's own wording whenever possible.

### 3. Expertise / Экспертиза
Capture:
- actual activities;
- skills;
- services / tasks people may pay them for;
- topics they can credibly teach/explain;
- topics where they are not an expert;
- proof assets / shipped work / cases / code / products / measured results when available;
- goals that strategy should support.

Keep these distinctions explicit:

```text
I do this ≠ I am an expert in this
I am interested in this ≠ I can sell this
I have experience ≠ I have measurable proof
```

### 4. Values / Ценности
Capture only self-described:
- principles;
- personality traits;
- what they say no to;
- beliefs they want to keep over time;
- non-negotiables;
- ethical/content boundaries.

Never convert a vague answer into a broader ideology.

Example:

User: `моральные принципы`
→ record as ambiguous;
→ ask what this means in practice;
→ do not invent principles.

## Interview protocol

### Phase A — reuse explicit supplied facts
Reuse only facts explicitly stated by the person in supplied context or first-party materials.

Do not reuse an assistant interpretation as fact.

### Phase B — gap map
Compare available data with `schemas/identity-profile.schema.json`.

Classify each strategy-relevant field:

```text
KNOWN
AMBIGUOUS
UNKNOWN
PRIVATE / NOT_REQUIRED
```

### Phase C — ask questions
Ask only about `AMBIGUOUS` or decision-relevant `UNKNOWN` fields.

Rules:
- ask in small logical groups, normally 3–7 questions;
- use plain language;
- do not lead the answer;
- do not present guessed options as if likely true;
- allow `не знаю`, `не хочу отвечать`, and `неважно для стратегии`;
- if an answer is vague, ask a follow-up instead of strengthening it;
- do not proceed to full strategy while a missing field could materially change positioning, audience, offer, or content boundaries.

### Phase D — confirmation
Show a concise structured draft to the person.

They may:
- confirm;
- correct;
- narrow;
- remove;
- mark fields private.

Only after explicit confirmation may normalized summaries be marked `USER_CONFIRMED`.

## Evidence status
Every strategically meaningful populated field must be traceable as one of:

- `USER_STATED` — directly stated by the person;
- `USER_CONFIRMED` — explicitly confirmed summary/normalization;
- `DOCUMENTED` — confirmed by supplied first-party material without redefining identity;
- `UNKNOWN` — unresolved.

`INFERRED` is not a valid final identity state.

## Question bank
Questions are selected dynamically. Never ask all by default.

### Personal
- Какие роли в личной жизни ты сам считаешь частью публичного образа?
- Что из личного ты готов регулярно показывать?
- Какие личные темы нельзя использовать вообще?
- Какие интересы вне работы реально хочется включать в публичный образ?

### Definition
- Как ты сам отвечаешь на вопрос «кто я?»?
- Какими словами ты хочешь, чтобы тебя определяла аудитория?
- Какими словами или ярлыками тебя точно не надо описывать?

### Expertise
- За что тебе уже сейчас можно платить?
- Какие задачи ты реально умеешь доводить до результата?
- Где у тебя есть доказательства: кейсы, продукты, код, клиенты, цифры, проекты?
- В каких близких темах ты пока ученик, а не эксперт?
- Какие цели должна поддерживать стратегия?

### Values
- Какие принципы ты не готов нарушать ради денег или охватов?
- Чему ты говоришь «нет» в работе и контенте?
- Какие свои черты ты сам считаешь важными для публичного образа?
- Что аудитория никогда не должна ошибочно подумать о тебе?

## Output
Produce one object conforming to:

`schemas/identity-profile.schema.json`

Also output:
- `known_fields`;
- `ambiguous_fields`;
- `unknown_fields`;
- `questions_required_before_strategy`;
- `safe_to_start_strategy: true|false`;
- `blocking_reason` when false.

## Handoff
After confirmation:

```text
identity-profile
+
business / offer context
→ founder-brand-context
```

The next skill may map confirmed facts into strategy fields, but it still may not invent missing values.

## Boundary
This skill does not:
- build content pillars;
- select channels;
- invent positioning;
- judge personality type;
- perform psychometrics;
- infer values;
- infer motivations;
- create brand archetypes unless explicitly requested and confirmed.

Its job is accurate structured intake, not interpretation theater.
