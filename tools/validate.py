#!/usr/bin/env python3
"""Validate LeadUX Content Strategist artifacts: schema + lightweight semantic integrity."""
from __future__ import annotations
import json
import sys
from pathlib import Path
from jsonschema import Draft202012Validator
from referencing import Registry, Resource

ROOT = Path(__file__).resolve().parents[1]
SCHEMAS = ROOT / "schemas"

# Order matters because a strategy output also contains research_package_id.
SCHEMA_BY_HINT = {
    "strategy_id": "strategy-output.schema.json",
    "research_package_id": "research-package.schema.json",
    "content_opportunity_id": "content-opportunity.schema.json",
    "brief_id": "content-brief.schema.json",
    "observation_id": "performance-observation.schema.json",
}

def load_registry() -> Registry:
    resources = []
    for p in SCHEMAS.glob("*.json"):
        schema = json.loads(p.read_text(encoding="utf-8"))
        resource = Resource.from_contents(schema)
        if "$id" in schema:
            resources.append((schema["$id"], resource))
    return Registry().with_resources(resources)

def semantic_errors(data: dict) -> list[str]:
    errors: list[str] = []

    if "research_package_id" in data and "strategy_id" not in data:
        claim_ids = {x.get("claim_id") for x in data.get("claims", [])}
        for insight in data.get("insights", []):
            iid = insight.get("insight_id", "<unknown>")
            for cid in insight.get("supporting_claim_ids", []) + insight.get("contradicting_claim_ids", []):
                if cid not in claim_ids:
                    errors.append(f"insight {iid} references missing claim_id {cid}")

    if "strategy_id" in data:
        opportunities = data.get("content_opportunities", [])
        opp_ids = {x.get("content_opportunity_id") for x in opportunities}
        for opp in opportunities:
            oid = opp.get("content_opportunity_id", "<unknown>")
            lineage = opp.get("research_lineage", {})
            lineage_ids = []
            for key in ("claim_ids", "insight_ids", "market_opportunity_ids", "voc_ids", "signal_ids", "performance_pattern_ids"):
                lineage_ids.extend(lineage.get(key, []))
            if not lineage_ids:
                errors.append(f"content opportunity {oid} has no research/performance lineage")

        for bucket, ids in data.get("portfolio", {}).items():
            for oid in ids:
                if oid not in opp_ids:
                    errors.append(f"portfolio.{bucket} references missing content opportunity {oid}")

        for brief in data.get("creator_briefs", []):
            bid = brief.get("brief_id", "<unknown>")
            oid = brief.get("content_opportunity_id")
            if oid not in opp_ids:
                errors.append(f"creator brief {bid} references missing content opportunity {oid}")

    return errors

def main(path_str: str) -> int:
    path = Path(path_str)
    data = json.loads(path.read_text(encoding="utf-8"))
    schema_name = next((v for k, v in SCHEMA_BY_HINT.items() if k in data), None)
    if not schema_name:
        print("Cannot infer schema from top-level keys", file=sys.stderr)
        return 2
    schema = json.loads((SCHEMAS / schema_name).read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema, registry=load_registry())
    errors = sorted(validator.iter_errors(data), key=lambda e: list(e.path))
    semantic = semantic_errors(data)
    if errors or semantic:
        for err in errors:
            loc = ".".join(str(p) for p in err.path) or "<root>"
            print(f"schema {loc}: {err.message}")
        for err in semantic:
            print(f"semantic: {err}")
        return 1
    print(f"OK: {path} -> {schema_name} + semantic checks")
    return 0

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: python tools/validate.py <artifact.json>", file=sys.stderr)
        raise SystemExit(2)
    raise SystemExit(main(sys.argv[1]))
