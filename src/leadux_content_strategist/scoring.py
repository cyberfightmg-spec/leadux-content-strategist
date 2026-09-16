from __future__ import annotations

MAP={"HIGH":3.0,"MEDIUM":2.0,"LOW":1.0,"UNKNOWN":None}
DEFAULT_WEIGHTS={
 "audience_evidence":0.22,
 "business_relevance":0.20,
 "competitive_whitespace":0.14,
 "freshness":0.10,
 "historical_fit":0.10,
 "differentiation":0.10,
 "production_feasibility":0.06,
 "evidence_confidence":0.08,
}

def score_dimensions(dimensions: dict, weights: dict | None=None) -> dict:
    weights=weights or DEFAULT_WEIGHTS
    known=[]; missing=[]
    for key,w in weights.items():
        raw=dimensions.get(key,"UNKNOWN")
        val=MAP.get(raw)
        if val is None: missing.append(key)
        else: known.append((key,val,w))
    if not known:
        return {"aggregate_score":None,"known_weight":0.0,"coverage":0.0,"missing_dimensions":missing}
    denom=sum(w for _,_,w in known)
    raw=sum(((v-1)/2)*w for _,v,w in known)/denom
    score=round(raw*100,1)
    return {"aggregate_score":score,"known_weight":round(denom,4),"coverage":round(denom/sum(weights.values()),4),"missing_dimensions":missing}
