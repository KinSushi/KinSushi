.PHONY: install test lint ci up down generate ingest quality reconcile dashboard reset

install:
	python -m pip install --upgrade pip
	pip install -e ".[dev]"

test:
	pytest

lint:
	ruff check .

ci: lint test

up:
	docker compose up -d

down:
	docker compose down

generate:
	python src/generate_synthetic_data.py

ingest:
	python src/ingest_transactions.py

quality:
	python src/quality_checks.py

reconcile:
	python src/reconciliation.py

dashboard:
	streamlit run dashboard/streamlit_app.py

reset:
	docker compose down -v
	docker compose up -d
	python src/generate_synthetic_data.py
	python src/ingest_transactions.py
	python src/quality_checks.py
