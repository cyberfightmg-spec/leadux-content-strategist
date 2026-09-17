---
name: identity-unpacking
description: >-
  Interview a founder before strategy, using four explicit blocks — Personal, Definition, Expertise, Values — and populate only self-stated or confirmed facts without inference.
metadata:
  version: 0.4.0
  category: founder-context
  evidence_mode: required
license: MIT
---

# Skill: Identity Unpacking

## Mission
Build a strategy-safe founder identity profile before strategy begins.

This skill exists because a founder-led content strategy cannot be precise if the system does not know who the founder is, what they do, what they believe, what they will not talk about, and where their real expertise ends.

## Absolute rule: no invention

Never infer, assume, psychoanalyze, complete, embellish, or reinterpret a missing identity field.

Do not infer:
- personality from writing style;
- values from career choices;
- expertise from interests;
- goals from current projects;
- family/relationship facts from context clues;
- political/religious/worldview positions unless explicitly stated;
- financial motives from pricing or business stage;
- preferred public identity from biography fragments.

If a field matters and is unclear:

```text
UNKNOWN
→ ask a direct question
→ wait for answer
→ record answer
```

## Four blocks

### 1. Personal / Личное
Understand only what the founder wants to make relevant to public strategy:
- relationships / family roles;
- important people/roles;
- life context;
- interests;
- personal topics allowed in content;
- personal topics that must remain private.

Do not force private disclosure. `prefer not to answer` is a valid final value.

### 2. Definition / Определение
Capture how the founder defines themselves:
- gender, age/age range, origin only if relevant and voluntarily stated;
- current location context if relevant;
- self-definition;
- public roles;
- labels they accept;
- labels they reject.

Use the founder's own wording where possible.

### 3. Expertise / Экспертиза
Capture:
- businesses/projects;
- actual activities;
- skills;
- topics they can credibly teach/explain;
- topics where they are not an expert;
- proof assets / shipped work / results / repositories / cases;
- money/commercial context only when the founder chooses to make it strategy-relevant;
- goals.

Separate `I do this` from `I am interested in this`.
Separate `I have experience` from `I have measurable proof`.

### 4. Values / Ценности
Capture only self-described:
- principles;
- personality traits;
- what they say no to;
- beliefs they want to keep over time;
- non-negotiables;
- ethical/content boundaries.

Never convert one statement into a broader ideology without confirmation.

## Interview protocol

### Phase A — reuse explicit known facts
If the user has already directly stated a fact in the current supplied context, reuse it and mark provenance as `USER_STATED`.

Do not silently reuse an interpretation.

### Phase B — gap map
Compare available data with `schemas/identity-profile.schema.json`.

Classify each strategically relevant field:

```text
KNOWN
AMBIGUOUS
UNKNOWN
PRIVATE / NOT_REQUIRED
```

### Phase C — ask questions
Ask only about `AMBIGUOUS` or important `UNKNOWN` fields.

Rules:
- ask in small logical groups, normally 3–7 questions;
- use plain language;
- do not lead the answer;
- do not present guessed options as if they are likely true;
- allow “не знаю”, “не хочу отвечать”, and “неважно для контента”;
- when an answer is ambiguous, ask a follow-up before recording a precise field;
- do not continue to strategy while a missing field could materially change positioning/audience/content boundaries.

### Phase D — confirmation
Before finalizing the profile, show a concise structured summary and ask the founder to correct anything inaccurate or overly broad.

Only after confirmation may a derived field use `USER_CONFIRMED` provenance.

## Question bank

Questions are selected dynamically. Do not ask all by default.

### Personal
- Какие роли в личной жизни ты сам считаешь частью публичного образа?
- Что из личной жизни ты готов регулярно показывать в контенте?
- Какие личные темы нельзя использовать вообще?
- Какие интересы вне работы реально тебя характеризуют и тебе хочется о них говорить?

### Definition
- Как ты сам отвечаешь на вопрос «кто я?» в 1–3 фразах?
- Какими ролями/словами ты хочешь, чтобы тебя определяла аудитория?
- Какими словами или ярлыками тебя точно не надо описывать?
- Какие факты происхождения/места жизни важны для публичной истории, а какие нет?

### Expertise
- За что тебе уже сейчас можно платить как специалисту?
- Какие задачи ты реально умеешь делать сам от начала до результата?
- В каких темах у тебя есть подтверждение: кейсы, продукты, код, клиенты, цифры, проекты?
- В каких близких темах ты пока ученик, а не эксперт?
- Какие направления бизнеса для тебя приоритетны сейчас?
- Какие цели должна поддерживать контент-стратегия?

### Values
- Какие 3–7 принципов ты не хочешь нарушать ради охватов или денег?
- Чему ты обычно говоришь «нет» в работе и контенте?
- Какие свои черты ты сам считаешь важными для личного бренда?
- Какие убеждения ты хотел бы транслировать и через несколько лет?
- Что аудитория никогда не должна ошибочно подумать о тебе?

## Provenance rule
Every strategically meaningful populated field should be traceable in `provenance`.

Allowed provenance:
- `USER_STATED` — directly stated by founder;
- `USER_CONFIRMED` — explicitly confirmed summary/normalization;
- `PUBLIC_SOURCE` — factual public info that is appropriate to use and does not substitute for self-definition;
- `UNKNOWN` — unresolved.

For identity, values, personality and personal boundaries, prefer founder statements over public-source inference.

## Output
Produce one object conforming to:

`schemas/identity-profile.schema.json`

Also produce:
- `known_fields`;
- `unknown_fields`;
- `questions_required_before_strategy`;
- `safe_to_start_strategy: true|false`;
- `blocking_reason` when false.

## Handoff to Founder / Brand Context
After user confirmation:

```text
identity-profile
+
business/offer context
→ founder-brand-context
```

The next skill may map confirmed facts into business strategy fields, but it still may not invent missing values.
