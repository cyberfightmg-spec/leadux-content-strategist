import json
from pathlib import Path
from leadux_content_strategist.schemas import validate_schema
from leadux_content_strategist.integrity import research_integrity_errors, strategy_integrity_errors
from leadux_content_strategist.scoring import score_dimensions
from leadux_content_strategist.memory import find_near_duplicates, similarity
from leadux_content_strategist.performance import build_baseline, compare_to_baseline
from leadux_content_strategist.workspace import init_workspace

ROOT=Path(__file__).resolve().parents[1]

def load(rel): return json.loads((ROOT/rel).read_text())

def test_strategy_request_schema():
    assert validate_schema(load('examples/strategy-request.example.json'),'strategy-request.schema.json') == []

def test_business_context_schema():
    ctx=load('examples/business-context.example.json')
    assert validate_schema(ctx,'business-context.schema.json') == []
    assert ctx['offers'][0]['priority']=='CORE'
    assert ctx['safe_to_start_strategy'] is True

def test_audience_icp_fit_schema():
    fit=load('examples/audience-icp-fit.example.json')
    assert validate_schema(fit,'audience-icp-fit.schema.json') == []
    assert fit['primary_icp_ids']
    assert fit['segments'][0]['evidence_status']=='SUPPORTED_CANDIDATE'
    assert fit['segments'][1]['evidence_status']=='AUDIENCE_NOT_ICP'
    assert fit['safe_for_strategy'] is True

def test_customer_journey_intent_schema():
    journey=load('examples/customer-journey-intent.example.json')
    assert validate_schema(journey,'customer-journey-intent.schema.json') == []
    assert journey['primary_journeys']==['jp_demo_001']
    assert journey['journeys'][0]['state']=='PROBLEM_AWARE'
    assert journey['journeys'][1]['state_confidence']=='HYPOTHESIS'
    assert journey['safe_for_strategy'] is True

def test_positioning_offer_fit_schema():
    fit=load('examples/positioning-offer-fit.example.json')
    assert validate_schema(fit,'positioning-offer-fit.schema.json') == []
    assert fit['primary_offer_ids']
    assert fit['supported_promises'][0]['status'] in {'PROVEN','SUPPORTED'}
    assert fit['safe_for_strategy'] is True

def test_founder_brand_context_schema():
    ctx=load('examples/founder-brand-context.leadux.example.json')
    assert validate_schema(ctx,'founder-brand-context.schema.json') == []
    assert ctx['positioning']['core_promise']
    assert any(o['priority']=='CORE' for o in ctx['offers'])

def test_validated_strategy_pattern_library():
    lib=load('references/validated-strategy-patterns.json')
    assert lib['patterns']
    ids=[p['pattern_id'] for p in lib['patterns']]
    assert len(ids)==len(set(ids))
    assert all(p['evidence_grade'] in {'A','B','C'} for p in lib['patterns'])
    assert all(p.get('limitations') for p in lib['patterns'])

def test_memory_schema():
    assert validate_schema(load('examples/memory/strategy-memory.example.json'),'strategy-memory.schema.json') == []

def test_research_semantic_integrity():
    r=load('examples/research-package.example.json')
    assert research_integrity_errors(r) == []

def test_strategy_semantic_integrity_against_research():
    s=load('examples/strategy-output.example.json'); r=load('examples/research-package.example.json')
    assert strategy_integrity_errors(s,r) == []

def test_unknown_dimensions_are_not_imputed():
    result=score_dimensions({'audience_evidence':'HIGH','business_relevance':'HIGH','historical_fit':'UNKNOWN'})
    assert result['aggregate_score'] == 100.0
    assert 'historical_fit' in result['missing_dimensions']
    assert 0 < result['coverage'] < 1

def test_duplicate_warning_is_transparent():
    m=load('examples/memory/strategy-memory.example.json')
    candidate={'title':'Why automation setup takes longer than expected','topic':'automation setup','angle':'Hidden complexity in automation projects'}
    matches=find_near_duplicates(candidate,m,0.5)
    assert matches and matches[0]['content_id']=='content_old_001'
    assert similarity('abc automation setup','automation setup') > 0

def test_baseline_and_comparison():
    obs=load('examples/performance/observations.example.json')
    b=build_baseline(obs,'views')
    assert b['n']==3 and b['median']==1000.0
    c=compare_to_baseline({'metrics':{'views':1600}},b)
    assert c['classification']=='ABOVE_BASELINE'

def test_workspace_init(tmp_path):
    m=init_workspace(tmp_path,load('examples/strategy-request.example.json'),load('examples/research-package.example.json'))
    assert m['state']=='INTAKE'
    assert (tmp_path/'manifest.json').exists()
    assert (tmp_path/'memory/strategy-memory.json').exists()

def test_preflight_status():
    from leadux_content_strategist.preflight import research_preflight
    r=load('examples/research-package.example.json')
    assert research_preflight(r)['preflight_status']=='READY_WITH_GAPS'

def test_handoff_builder_preserves_ids():
    from leadux_content_strategist.handoff import build_handoff
    source=load('examples/research-package.example.json')
    rr=source['research_run'].copy(); rr['integrity_status']=source['integrity_status']
    artifacts={k:source.get(k) for k in ('claims','insights','market_opportunities','voc_records','voc_themes','strategic_signals','content_footprints','contradictions','data_gaps')}
    out=build_handoff(rr,artifacts,'rp_test')
    assert out['claims'][0]['claim_id']=='claim_demo_001'
    assert validate_schema(out,'research-package.schema.json')==[]
    assert research_integrity_errors(out)==[]

def test_tight_strategy_output_schema():
    s=load('examples/strategy-output.example.json')
    assert validate_schema(s,'strategy-output.schema.json')==[]
    assert s['decisions'][0]['decision_id']=='dec_demo_001'

def test_skill_registry_and_frontmatter():
    import re
    root = Path(__file__).resolve().parents[1]
    registry = json.loads((root / 'skills' / 'registry.json').read_text())
    registered = {row['name'] for row in registry['skills']}
    directories = {p.parent.name for p in (root / 'skills').glob('*/SKILL.md')}
    assert registered == directories

    for path in [root / 'SKILL.md', *list((root / 'skills').glob('*/SKILL.md'))]:
        text = path.read_text()
        assert text.startswith('---\n')
        header = text.split('---', 2)[1]
        assert re.search(r'^name:\s*.+$', header, re.M)
        assert re.search(r'^description:\s*>-', header, re.M)
        assert re.search(r'^license:\s*MIT$', header, re.M)
