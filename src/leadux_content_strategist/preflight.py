from __future__ import annotations
from collections import Counter

def research_preflight(r: dict) -> dict:
    status=r.get("integrity_status","NOT_YET_VERIFIED")
    mapping={"VERIFIED":"READY_FOR_STRATEGY","VERIFIED_WITH_GAPS":"READY_WITH_GAPS","DEGRADED":"LIMITED_STRATEGY_ONLY","INSUFFICIENT_EVIDENCE":"NEEDS_RESEARCH","NOT_YET_VERIFIED":"NEEDS_VERIFICATION"}
    claims=r.get("claims",[])
    ev=Counter(x.get("evidence_type","UNKNOWN") for x in claims)
    vs=Counter(x.get("verification_status","UNKNOWN") for x in claims)
    blockers=[]
    if status in ("INSUFFICIENT_EVIDENCE","NOT_YET_VERIFIED"): blockers.append(f"research integrity status is {status}")
    if vs.get("CONTRADICTED",0): blockers.append(f"{vs['CONTRADICTED']} claims are contradicted")
    return {
      "preflight_status":mapping.get(status,"LIMITED_STRATEGY_ONLY"),
      "integrity_status":status,
      "claim_count":len(claims),
      "evidence_types":dict(ev),
      "verification_statuses":dict(vs),
      "contradiction_count":len(r.get("contradictions",[])),
      "data_gap_count":len(r.get("data_gaps",[])),
      "voc_record_count":len(r.get("voc_records",[])),
      "signal_count":len(r.get("strategic_signals",[])),
      "content_footprint_count":len(r.get("content_footprints",[])),
      "blockers":blockers,
    }
