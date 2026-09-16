import json
from pathlib import Path
from jsonschema import Draft202012Validator
from referencing import Registry, Resource

ROOT = Path(__file__).resolve().parents[1]
SCHEMAS = ROOT / "schemas"

def registry():
    resources = []
    for p in SCHEMAS.glob("*.json"):
        schema = json.loads(p.read_text())
        if "$id" in schema:
            resources.append((schema["$id"], Resource.from_contents(schema)))
    return Registry().with_resources(resources)

def validate(example, schema_name):
    schema = json.loads((SCHEMAS / schema_name).read_text())
    data = json.loads((ROOT / "examples" / example).read_text())
    Draft202012Validator(schema, registry=registry()).validate(data)

def test_all_schemas_are_valid():
    for p in SCHEMAS.glob("*.json"):
        Draft202012Validator.check_schema(json.loads(p.read_text()))

def test_research_package_example():
    validate("research-package.example.json", "research-package.schema.json")

def test_strategy_output_example():
    validate("strategy-output.example.json", "strategy-output.schema.json")
