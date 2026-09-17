from __future__ import annotations
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from .io import load_json

KEY_ALIASES={
 "claims": ("claims",),
 "insights": ("insights",),
 "market_opportunities": ("market_opportunities","opportunities"),
 "voc_records": ("voc_records",),
 "voc_themes": ("voc_themes","themes"),
 "strategic_signals": ("strategic_signals","signals"),
 "content_footprints": ("content_footprints","content_footprint"),
 "content_performance_patterns": ("content_performance_patterns","performance_patterns"),
 "contradictions": ("contradictions",),
 "data_gaps": ("data_gaps",),
}

def extract(payload: Any, logical_key: str) -> list:
    if payload is None: return []
    if isinstance(payload,list): return payload
    if not isinstance(payload,dict): return []
    for container in (payload, payload.get("artifacts",{})):
        if isinstance(container,dict):
            for key in KEY_ALIASES[logical_key]:
                value=container.get(key)
                if isinstance(value,list): return value
    return []

def build_handoff(research_run: dict, artifacts: dict[str,Any], package_id: str|None=None, producer_version: str="0.4.0") -> dict:
    rid=research_run.get("research_id") or "unknown"
    now=datetime.now(timezone.utc).isoformat()
    out={
      "research_package_id": package_id or f"rp_{rid}",
      "research_run": research_run,
      "claims": extract(artifacts.get("claims"),"claims"),
      "insights": extract(artifacts.get("insights"),"insights"),
      "market_opportunities": extract(artifacts.get("market_opportunities"),"market_opportunities"),
      "voc_records": extract(artifacts.get("voc_records"),"voc_records"),
      "voc_themes": extract(artifacts.get("voc_themes"),"voc_themes"),
      "strategic_signals": extract(artifacts.get("strategic_signals"),"strategic_signals"),
      "content_footprints": extract(artifacts.get("content_footprints"),"content_footprints"),
      "content_performance_patterns": extract(artifacts.get("content_performance_patterns"),"content_performance_patterns"),
      "contradictions": extract(artifacts.get("contradictions"),"contradictions"),
      "data_gaps": extract(artifacts.get("data_gaps"),"data_gaps"),
      "integrity_status": research_run.get("integrity_status","NOT_YET_VERIFIED"),
      "generated_at": now,
      "handoff": {"generated_at":now,"producer_version":producer_version,"target_system":"leadux-content-strategist","selection_notes":[],"omitted_artifact_types":[]},
    }
    for k in KEY_ALIASES:
        if k not in artifacts or artifacts.get(k) is None:
            out["handoff"]["omitted_artifact_types"].append(k)
    return out

def load_optional(path: str|None) -> Any:
    return None if not path else load_json(Path(path))
