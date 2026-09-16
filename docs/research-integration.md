# Integration with LeadUX Competitor Research

The upstream research repository already defines durable IDs for research runs, claims, insights and market opportunities. The strategist should preserve those IDs.

## Important semantic distinction

### Market opportunity

An upstream research conclusion about a market, audience, workflow, product, channel, positioning or related whitespace.

### Content opportunity

A downstream strategic candidate for what the brand should communicate or test.

A market opportunity may produce zero, one or many content opportunities. A content opportunity may also emerge from VOC, strategic signals, competitor content gaps or first-party performance patterns even when no formal market opportunity exists.

## Adapter rule

Do not force the upstream repository to adopt the strategist's schema. Instead export the necessary research artifacts into `research-package.schema.json` while keeping original IDs and evidence semantics.

## Planned integration skill

A future upstream `strategy-handoff` / export skill should:

1. select only strategy-relevant verified artifacts;
2. preserve claim/insight/opportunity IDs;
3. include relevant contradictions and data gaps;
4. include observation/completion dates;
5. produce a research package without reinterpreting evidence.
