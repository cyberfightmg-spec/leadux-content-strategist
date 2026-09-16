# Contributing

Contributions are welcome when they preserve evidence traceability and the Research → Strategy → Creator boundary.

## Before opening a PR

1. Explain which strategic failure mode or workflow gap the change addresses.
2. Add or update schemas when the output contract changes.
3. Add an example or test for new machine-readable behavior.
4. Do not introduce hidden paid-service dependencies as required defaults.
5. Do not replace unknown data with fabricated or assumed values.
6. Keep third-party code/text licensing explicit.

## Skill contributions

A new skill should contain:

- mission;
- inputs;
- method/decision rules;
- required output;
- quality rules;
- escalation conditions;
- clear boundary with neighboring skills.

## Validation

```bash
python -m pip install -r requirements-dev.txt
python tools/validate.py examples/research-package.example.json
python tools/validate.py examples/strategy-output.example.json
pytest -q
```
