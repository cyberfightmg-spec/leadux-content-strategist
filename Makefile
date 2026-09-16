.PHONY: test validate install
install:
	pip install -e '.[dev]'
test:
	pytest
validate:
	leadux-strategist validate examples/research-package.example.json
	leadux-strategist validate examples/strategy-output.example.json --research examples/research-package.example.json
