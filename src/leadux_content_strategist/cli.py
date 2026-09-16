from __future__ import annotations
import argparse, json
from .io import load_json, dump_json
from .schemas import validate_schema
from .integrity import research_integrity_errors, strategy_integrity_errors
from .scoring import score_dimensions
from .memory import find_near_duplicates
from .performance import build_baseline, compare_to_baseline
from .workspace import init_workspace
from .handoff import build_handoff, load_optional
from .preflight import research_preflight

def emit(data): print(json.dumps(data,ensure_ascii=False,indent=2))

def cmd_validate(a):
    data=load_json(a.file); errs=validate_schema(data)
    if "research_package_id" in data and "strategy_id" not in data: errs += research_integrity_errors(data)
    if "strategy_id" in data: errs += strategy_integrity_errors(data,load_json(a.research) if a.research else None)
    if errs:
        for e in errs: print(f"ERROR: {e}")
        return 1
    print(f"OK: {a.file}"); return 0

def cmd_preflight(a): emit(research_preflight(load_json(a.research))); return 0

def cmd_score(a): emit(score_dimensions(load_json(a.file).get("dimensions",{}))); return 0

def cmd_init(a):
    request=load_json(a.request); research=load_json(a.research)
    errs=validate_schema(request,"strategy-request.schema.json")+validate_schema(research,"research-package.schema.json")+research_integrity_errors(research)
    if errs:
        for e in errs: print(f"ERROR: {e}")
        return 1
    emit(init_workspace(a.output,request,research)); return 0

def cmd_duplicates(a): emit(find_near_duplicates(load_json(a.candidate),load_json(a.memory),a.threshold)); return 0

def cmd_baseline(a):
    obs=load_json(a.observations); obs=obs if isinstance(obs,list) else [obs]; b=build_baseline(obs,a.metric)
    emit({"baseline":b,"comparison":compare_to_baseline(load_json(a.compare),b)} if a.compare else b); return 0

def cmd_handoff(a):
    rr=load_json(a.research_run)
    artifacts={k:load_optional(getattr(a,k)) for k in ("claims","insights","market_opportunities","voc_records","voc_themes","strategic_signals","content_footprints","contradictions","data_gaps")}
    out=build_handoff(rr,artifacts,a.package_id)
    errs=validate_schema(out,"research-package.schema.json")+research_integrity_errors(out)
    if errs:
        for e in errs: print(f"ERROR: {e}")
        return 1
    dump_json(out,a.output); print(f"OK: wrote {a.output}"); return 0

def main(argv=None):
    p=argparse.ArgumentParser(prog="leadux-strategist",description="Deterministic infrastructure for LeadUX Content Strategist")
    sub=p.add_subparsers(dest="cmd",required=True)
    v=sub.add_parser("validate"); v.add_argument("file"); v.add_argument("--research"); v.set_defaults(fn=cmd_validate)
    pf=sub.add_parser("preflight"); pf.add_argument("--research",required=True); pf.set_defaults(fn=cmd_preflight)
    s=sub.add_parser("score"); s.add_argument("file"); s.set_defaults(fn=cmd_score)
    i=sub.add_parser("init"); i.add_argument("--request",required=True); i.add_argument("--research",required=True); i.add_argument("--output",required=True); i.set_defaults(fn=cmd_init)
    d=sub.add_parser("duplicates"); d.add_argument("--candidate",required=True); d.add_argument("--memory",required=True); d.add_argument("--threshold",type=float,default=.55); d.set_defaults(fn=cmd_duplicates)
    b=sub.add_parser("baseline"); b.add_argument("--observations",required=True); b.add_argument("--metric",required=True); b.add_argument("--compare"); b.set_defaults(fn=cmd_baseline)
    h=sub.add_parser("handoff"); h.add_argument("--research-run",required=True); h.add_argument("--output",required=True); h.add_argument("--package-id")
    for name in ("claims","insights","market_opportunities","voc_records","voc_themes","strategic_signals","content_footprints","contradictions","data_gaps"): h.add_argument("--"+name.replace("_","-"),dest=name)
    h.set_defaults(fn=cmd_handoff)
    a=p.parse_args(argv); return a.fn(a)

if __name__ == "__main__": raise SystemExit(main())
