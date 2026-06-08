.PHONY: install test lint up down quality dashboard

install:
	python -m pip install --upgrade pip
	pip install -e ".[dev]"

test:
	pytest

lint:
	ruff check .

up:
	docker compose up -d

down:
	docker compose down

quality:
	@echo "Run SQL quality checks against local PostgreSQL. Implementation planned in src/quality_checks.py"

dashboard:
	streamlit run dashboard/streamlit_app.py
