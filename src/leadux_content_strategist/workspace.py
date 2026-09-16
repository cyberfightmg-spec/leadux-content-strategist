from __future__ import annotations
from datetime import datetime, timezone
from pathlib import Path
from .io import dump_json
from .memory import empty_memory

def init_workspace(out_dir: str|Path, request: dict, research: dict) -> dict:
    out=Path(out_dir); out.mkdir(parents=True,exist_ok=True)
    for d in ("inputs","working","outputs","memory"):(out/d).mkdir(exist_ok=True)
    dump_json(request,out/"inputs/strategy-request.json")
    dump_json(research,out/"inputs/research-package.json")
    mem=empty_memory(f"mem_{request.get('request_id','run')}")
    dump_json(mem,out/"memory/strategy-memory.json")
    manifest={
      "workspace_version":"0.2.0",
      "request_id":request.get("request_id"),
      "research_package_id":research.get("research_package_id"),
      "created_at":datetime.now(timezone.utc).isoformat(),
      "state":"INTAKE",
      "stages":["INTAKE","OBJECTIVES","WEDGE","PILLARS","OPPORTUNITIES","PORTFOLIO","EXPERIMENTS","CHALLENGE","BRIEFS","SYNTHESIS"],
      "human_approval_required_before":["BRIEFS"],
    }
    dump_json(manifest,out/"manifest.json")
    return manifest
