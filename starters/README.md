# Starter Kits

This folder contains public starter kits for future portfolio repositories.

These are technical blueprints and executable seeds. They are not application materials.

| Starter | Purpose | Target maturity |
|---|---|---:|
| [banking-dataops-monitoring](banking-dataops-monitoring/README.md) | SQL, PostgreSQL, data quality, reconciliation, monitoring and incident runbooks | Level 4 |
| [fraud-mlops-control-tower](fraud-mlops-control-tower/README.md) | Synthetic risk/anomaly analytics with MLflow, FastAPI, Docker and model governance | Level 4 |
| [database-migration-quality-lab](database-migration-quality-lab/README.md) | Legacy-to-target migration, validation, reconciliation and rollback | Level 3-4 |
| [secure-wealth-rag-assistant](secure-wealth-rag-assistant/README.md) | Secure RAG / LLMOps with synthetic documents, privacy controls and evaluation | Level 3 |

## Public-safety rules

- synthetic or open data only;
- no real banking, insurance, health, client or employer data;
- no CVs, cover letters, job trackers or employer-specific notes;
- no secrets, tokens, private hosts or real infrastructure identifiers;
- no production decisioning or performance claims.

## Execution order

1. `banking-dataops-monitoring`
2. `fraud-mlops-control-tower`
3. `database-migration-quality-lab`
4. `secure-wealth-rag-assistant`

## Promotion path

When repository creation is available, each starter should be copied into its own dedicated public repository and completed to the quality gates defined in `docs/PORTFOLIO_QUALITY_GATES.md`.
