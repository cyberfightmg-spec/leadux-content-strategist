# CLI

Install for development:

```bash
pip install -e '.[dev]'
```

Commands:

```bash
leadux-strategist validate examples/research-package.example.json
leadux-strategist validate examples/strategy-output.example.json --research examples/research-package.example.json
leadux-strategist preflight --research examples/research-package.example.json
leadux-strategist score examples/content-opportunity.example.json
leadux-strategist init --request examples/strategy-request.example.json --research examples/research-package.example.json --output runs/demo
leadux-strategist duplicates --candidate examples/content-opportunity.example.json --memory examples/memory/strategy-memory.example.json
leadux-strategist baseline --observations examples/performance/observations.example.json --metric views
```

The CLI is deterministic infrastructure. It does not call an LLM.

### Upstream handoff builder

`leadux-strategist handoff` can assemble a package from separate upstream artifact JSON files while preserving their IDs. This is an adapter, not a strategy step.
