from __future__ import annotations
from statistics import median

def build_baseline(observations: list[dict], metric: str) -> dict:
    vals=[]
    for o in observations:
        v=o.get("metrics",{}).get(metric)
        if isinstance(v,(int,float)): vals.append(float(v))
    if not vals:
        return {"metric":metric,"n":0,"median":None,"min":None,"max":None}
    return {"metric":metric,"n":len(vals),"median":median(vals),"min":min(vals),"max":max(vals)}

def compare_to_baseline(observation: dict, baseline: dict) -> dict:
    metric=baseline["metric"]
    value=observation.get("metrics",{}).get(metric)
    med=baseline.get("median")
    if not isinstance(value,(int,float)) or med is None:
        return {"metric":metric,"value":value,"baseline_median":med,"ratio":None,"classification":"UNKNOWN"}
    ratio=None if med==0 else value/med
    if ratio is None: cls="UNKNOWN"
    elif ratio>=1.5: cls="ABOVE_BASELINE"
    elif ratio<=0.67: cls="BELOW_BASELINE"
    else: cls="NEAR_BASELINE"
    return {"metric":metric,"value":value,"baseline_median":med,"ratio":None if ratio is None else round(ratio,3),"classification":cls}
