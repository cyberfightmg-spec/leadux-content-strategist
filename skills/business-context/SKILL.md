---
name: business-context
description: >-
  Interview and structure the commercial context before strategy: what the business sells, to whom, how it makes money, what is prioritized, what resources exist, and what constraints apply — without inventing missing business facts.
metadata:
  version: 0.4.0
  category: business-context
  evidence_mode: required
license: MIT
---

# Skill: Business Context

## Mission
Build a strategy-safe business context that is independent from personality.

This skill answers:

> What business are we actually building, what do we sell, who buys it, what matters commercially now, and what constraints must strategy respect?

## Absolute rule: no invention

Never infer or fabricate:
- pricing;
- revenue;
- margin;
- conversion;
- CAC;
- sales cycle;
- demand;
- target audience;
- offer priority;
- delivery capacity;
- recurring revenue potential;
- business stage;
- channel economics.

If a strategically important field is missing:

```text
UNKNOWN
→ ask a direct business question
→ wait for answer
→ record answer and provenance
```

## Separation from Identity

`identity-unpacking` answers **who the person is**.

`business-context` answers **what the business is trying to achieve commercially**.

Do not put personality traits, family information or values into this skill unless they directly create a business constraint already stated by the user.

## Required blocks

### 1. Business
Capture:
- business/company/project name when relevant;
- business model;
- current stage;
- geography/language markets;
- current revenue model;
- desired future revenue model.

### 2. Offers
For every material offer capture:
- what it is;
- current status;
- priority;
- target audience;
- problem solved;
- desired customer outcome;
- pricing model if known;
- delivery model;
- proof assets;
- capacity constraints.

Do not assume the highest-priced or newest offer is the priority.

### 3. Audiences
Capture only explicit or research-supported audiences:
- buyer/customer type;
- buyer role;
- jobs;
- known problems;
- desired outcomes;
- evidence status.

If the founder says “business owners” and no narrower evidence exists, preserve that broadness instead of inventing an ICP.

### 4. Economics
Capture only what the user is comfortable making strategy-relevant:
- immediate revenue priorities;
- recurring/passive revenue priorities;
- one-time service priorities;
- price or margin constraints;
- financial unknowns.

Exact numbers are optional unless the strategy decision depends on them.

### 5. Goals
Every goal should state when possible:
- goal;
- priority;
- time horizon;
- what success means;
- whether measurement is actually defined.

“Make more money” is valid input, but may require a follow-up before it can drive channel/content allocation.

### 6. Resources
Capture:
- team model;
- time capacity;
- budget capacity;
- tools/channels already available;
- existing assets;
- operational/delivery constraints.

### 7. Constraints
Capture:
- must-do conditions;
- must-not-do conditions;
- markets/industries not served;
- offer constraints;
- legal or operational restrictions when explicitly known.

## Interview protocol

### Phase A — reuse explicit facts
Reuse facts already explicitly supplied in current input/profile/documents. Mark provenance.

Do not reuse interpretations as facts.

### Phase B — gap map
Classify strategically material fields as:

```text
KNOWN
AMBIGUOUS
UNKNOWN
NOT_REQUIRED
```

### Phase C — ask only decision-relevant questions
Ask in small groups. Prefer questions such as:

- Что ты сейчас реально продаёшь?
- Что из этого приносит деньги уже сейчас, а что только планируется?
- Какой оффер для тебя сейчас главный?
- Кому ты хочешь его продавать?
- Какую проблему он решает?
- Что клиент получает в результате?
- Какой доход ты хочешь усиливать: услуги, подписку, продукты, партнёрку, другое?
- Какие направления не хочешь развивать даже если там есть спрос?
- Сколько проектов/контента/клиентов ты реально можешь обслуживать одновременно?
- Какие ресурсы уже есть: команда, каналы, аудитория, продукты, кейсы, сайт, база?
- Что должно измениться через 30/90/365 дней, чтобы ты сказал «стратегия работает»?

Do not ask every question by default.

### Phase D — contradiction check
If two answers conflict (for example “хочу пассивный доход” and “приоритет — кастомные проекты руками”), do not resolve it yourself. Surface the conflict and ask which one wins now.

### Phase E — confirmation
Show a concise structured business summary before strategy starts.

The user must be able to correct:
- wrong priorities;
- wrong audience mapping;
- wrong offer status;
- overly precise normalization;
- missing constraints.

## Output
Produce one object conforming to:

`schemas/business-context.schema.json`

Also output:
- `known_fields`;
- `unknown_fields`;
- `commercial_conflicts`;
- `questions_required_before_strategy`;
- `safe_to_start_strategy`;
- `blocking_reason`.

## Handoff
The universal context pipeline is:

```text
identity-profile
+
business-context
→ founder-brand-context
```

For non-founder-led brands, identity may be replaced with an organization/brand identity source, but business-context remains required for full commercial strategy.
