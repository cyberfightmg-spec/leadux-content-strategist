from __future__ import annotations
from collections import Counter

LINEAGE_KEYS=("claim_ids","insight_ids","market_opportunity_ids","voc_ids","signal_ids","content_footprint_ids","performance_pattern_ids")

def _dupes(values):
    return sorted(k for k,v in Counter(values).items() if k and v>1)

def research_integrity_errors(data: dict) -> list[str]:
    errors=[]
    ids={
      "claim_ids": {x.get("claim_id") for x in data.get("claims",[])},
      "insight_ids": {x.get("insight_id") for x in data.get("insights",[])},
      "market_opportunity_ids": {x.get("opportunity_id") for x in data.get("market_opportunities",[])},
      "voc_ids": {x.get("voc_id") for x in data.get("voc_records",[])},
      "signal_ids": {x.get("signal_id") for x in data.get("strategic_signals",[])},
      "content_footprint_ids": {x.get("content_footprint_id") for x in data.get("content_footprints",[])},
    }
    for name, values in ids.items():
        for d in _dupes(values): errors.append(f"duplicate {name[:-1]}: {d}")
    for ins in data.get("insights",[]):
        for cid in ins.get("supporting_claim_ids",[])+ins.get("contradicting_claim_ids",[]):
            if cid not in ids["claim_ids"]:
                errors.append(f"insight {ins.get('insight_id')} references missing claim_id {cid}")
    return errors

def strategy_integrity_errors(data: dict, research: dict | None = None) -> list[str]:
    errors=[]
    opps=data.get("content_opportunities",[])
    opp_ids={x.get("content_opportunity_id") for x in opps}
    if len(opp_ids) != len(opps): errors.append("duplicate content_opportunity_id detected")
    research_ids={k:set() for k in LINEAGE_KEYS}
    if research:
        research_ids.update({
          "claim_ids": {x.get("claim_id") for x in research.get("claims",[])},
          "insight_ids": {x.get("insight_id") for x in research.get("insights",[])},
          "market_opportunity_ids": {x.get("opportunity_id") for x in research.get("market_opportunities",[])},
          "voc_ids": {x.get("voc_id") for x in research.get("voc_records",[])},
          "signal_ids": {x.get("signal_id") for x in research.get("strategic_signals",[])},
          "content_footprint_ids": {x.get("content_footprint_id") for x in research.get("content_footprints",[])},
        })
    for opp in opps:
        oid=opp.get("content_opportunity_id","<unknown>")
        lin=opp.get("research_lineage",{})
        if not any(lin.get(k) for k in LINEAGE_KEYS):
            errors.append(f"content opportunity {oid} has no research/performance lineage")
        if research:
            for k in LINEAGE_KEYS[:-1]:
                for rid in lin.get(k,[]):
                    if rid not in research_ids[k]: errors.append(f"{oid} references missing {k[:-4]} {rid}")
    for bucket, values in data.get("portfolio",{}).items():
        for oid in values:
            if oid not in opp_ids: errors.append(f"portfolio.{bucket} references missing content opportunity {oid}")
    for b in data.get("creator_briefs",[]):
        if b.get("content_opportunity_id") not in opp_ids:
            errors.append(f"creator brief {b.get('brief_id')} references missing content opportunity {b.get('content_opportunity_id')}")
    dec_ids={d.get("decision_id") for d in data.get("decisions",[])}
    for b in data.get("creator_briefs",[]):
        did=b.get("decision_id")
        if did and did not in dec_ids: errors.append(f"creator brief {b.get('brief_id')} references missing decision {did}")
    return errors
