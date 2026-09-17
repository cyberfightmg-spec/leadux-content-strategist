from __future__ import annotations
import json
from pathlib import Path
from jsonschema import Draft202012Validator
from referencing import Registry, Resource

PACKAGE_ROOT = Path(__file__).resolve().parents[2]
REPO_ROOT = PACKAGE_ROOT.parent if PACKAGE_ROOT.name == "src" else PACKAGE_ROOT
SCHEMA_DIR = REPO_ROOT / "schemas"

HINTS = [
    ("strategy_id", "strategy-output.schema.json"),
    ("context_id", "founder-brand-context.schema.json"),
    ("research_package_id", "research-package.schema.json"),
    ("content_opportunity_id", "content-opportunity.schema.json"),
    ("brief_id", "content-brief.schema.json"),
    ("observation_id", "performance-observation.schema.json"),
    ("memory_id", "strategy-memory.schema.json"),
    ("request_id", "strategy-request.schema.json"),
]

def registry() -> Registry:
    items=[]
    for p in SCHEMA_DIR.glob("*.json"):
        s=json.loads(p.read_text(encoding="utf-8"))
        if "$id" in s:
            items.append((s["$id"], Resource.from_contents(s)))
    return Registry().with_resources(items)

def infer_schema(data: dict) -> str | None:
    for key, name in HINTS:
        if key in data:
            return name
    return None

def validate_schema(data: dict, schema_name: str | None = None) -> list[str]:
    schema_name = schema_name or infer_schema(data)
    if not schema_name:
        return ["cannot infer schema from top-level keys"]
    schema=json.loads((SCHEMA_DIR/schema_name).read_text(encoding="utf-8"))
    v=Draft202012Validator(schema, registry=registry())
    out=[]
    for e in sorted(v.iter_errors(data), key=lambda x:list(x.path)):
        loc=".".join(str(x) for x in e.path) or "<root>"
        out.append(f"{loc}: {e.message}")
    return out
