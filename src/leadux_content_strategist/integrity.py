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
    selected_thesis_id=data.get("selected_strategic_thesis_id")
    if selected_thesis_id:
        thesis_ids={x.get("thesis_id") for x in data.get("strategic_options",[])}
        if selected_thesis_id not in thesis_ids:
            errors.append(f"selected_strategic_thesis_id references missing thesis {selected_thesis_id}")
        for label, items in (
            ("content pillar", data.get("content_pillars",[])),
            ("content opportunity", data.get("content_opportunities",[])),
            ("creator brief", data.get("creator_briefs",[])),
            ("strategy decision", data.get("decisions",[])),
        ):
            for item in items:
                tid=item.get("strategic_thesis_id")
                if tid != selected_thesis_id:
                    ident=item.get("pillar_id") or item.get("content_opportunity_id") or item.get("brief_id") or item.get("decision_id") or "<unknown>"
                    errors.append(f"{label} {ident} must trace to selected thesis {selected_thesis_id}")
    return errors


HARD_GATES={"EVIDENCE_VIABILITY","COMMERCIAL_FIT","CREDIBILITY_PROOF","CAPABILITY_CAPACITY","ETHICAL_LEGAL_FIT"}

def strategy_formulation_integrity_errors(data: dict) -> list[str]:
    errors=[]
    options=data.get("options",[])
    ids=[x.get("thesis_id") for x in options]
    for d in _dupes(ids):
        errors.append(f"duplicate thesis_id: {d}")
    status_quo=[x for x in options if x.get("option_type")=="STATUS_QUO"]
    if len(status_quo)!=1:
        errors.append(f"strategy formulation must contain exactly one STATUS_QUO option, found {len(status_quo)}")
    selected=[x for x in options if x.get("status")=="SELECTED"]
    if len(selected)!=1:
        errors.append(f"strategy formulation must contain exactly one SELECTED thesis, found {len(selected)}")
    selected_id=data.get("selected_thesis_id")
    if selected_id not in ids:
        errors.append(f"selected_thesis_id references missing thesis {selected_id}")
    elif len(selected)==1 and selected[0].get("thesis_id")!=selected_id:
        errors.append("selected_thesis_id does not match thesis with status SELECTED")
    alt=data.get("strongest_alternative_id")
    if alt not in ids:
        errors.append(f"strongest_alternative_id references missing thesis {alt}")
    if alt and alt==selected_id:
        errors.append("strongest alternative cannot equal selected thesis")
    for opt in options:
        oid=opt.get("thesis_id","<unknown>")
        gates=opt.get("hard_gates",[])
        names=[g.get("gate") for g in gates]
        if set(names)!=HARD_GATES or len(names)!=len(HARD_GATES):
            errors.append(f"thesis {oid} must contain each hard gate exactly once")
    if len(selected)==1:
        for gate in selected[0].get("hard_gates",[]):
            if gate.get("status") in {"FAIL","UNKNOWN"}:
                errors.append(f"selected thesis {selected_id} has non-viable hard gate {gate.get('gate')}={gate.get('status')}")
    return errors

def strategy_validation_integrity_errors(data: dict, formulation: dict | None = None) -> list[str]:
    errors=[]
    result=data.get("result")
    gates=data.get("hard_gate_review",[])
    if result in {"SURVIVES","NARROWED"}:
        for gate in gates:
            if gate.get("status") in {"FAIL","UNKNOWN"}:
                errors.append(f"validation {result} cannot retain hard gate {gate.get('gate')}={gate.get('status')}")
    if result=="SURVIVES":
        for c in data.get("coherence_checks",[]):
            if c.get("status")=="CONTRADICTORY":
                errors.append("SURVIVES validation cannot contain CONTRADICTORY coherence item")
    if formulation:
        if data.get("formulation_id")!=formulation.get("formulation_id"):
            errors.append("validation formulation_id does not match formulation")
        if data.get("thesis_id")!=formulation.get("selected_thesis_id"):
            errors.append("validation thesis_id does not match selected thesis")
        alt=(data.get("strongest_alternative_review") or {}).get("alternative_thesis_id")
        if alt and alt!=formulation.get("strongest_alternative_id"):
            errors.append("validation strongest alternative does not match formulation")
    return errors
