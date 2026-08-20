.PHONY: install lint format check

install:
	pip install ruff pre-commit

lint:
	ruff check .
	ruff format --check .

format:
	ruff check --fix .
	ruff format .

check: lint
