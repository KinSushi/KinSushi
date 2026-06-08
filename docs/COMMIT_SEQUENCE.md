# Commit Sequence

This document records the recommended implementation order for the public portfolio.

It is a technical execution plan, not a job application plan.

---

## Existing repositories

### sovralys-infra-lab

```text
docs: add hardening checklist
docs: add monitoring baseline
docs: add backup restore test procedure
docs: add data mlops docker compose example
docs: add mermaid architecture diagram
```

### pty-flights-pricing

```text
chore: add requirements file
chore: add pyproject for reproducible tooling
feat: add testable pricing signal module
feat: add explicit runtime config module
test: add pricing signal unit tests
test: add config unit tests
ci: add python lint and test workflow
chore: add make targets for local workflow
docs: add sanitized sample outputs
```

---

## New repository: banking-dataops-monitoring

```text
chore: initialize repository structure
docs: add portfolio-ready readme
feat: add postgres docker compose
feat: add synthetic banking data generator
feat: add data quality SQL checks
feat: add reconciliation queries
feat: add streamlit monitoring dashboard
test: add quality check tests
ci: add github actions workflow
docs: add controls matrix and incident runbook
```

---

## New repository: fraud-mlops-control-tower

```text
chore: initialize mlops repository
feat: add synthetic fraud dataset
feat: add baseline model training
feat: add mlflow tracking
feat: add fastapi prediction endpoint
feat: add dockerfile
test: add feature and api tests
ci: add github actions
docs: add model card data card risk assessment
```

---

## New repository: database-migration-quality-lab

```text
chore: initialize migration quality lab
docs: add portfolio-ready readme
feat: add legacy schema
feat: add target schema
feat: add migration sql
feat: add validation checks
feat: add reconciliation report generator
test: add migration tests
docs: add rollback plan and controls matrix
```

---

## New repository: secure-wealth-rag-assistant

```text
chore: initialize secure rag assistant
feat: add synthetic wealth documents
feat: add ingestion and chunking
feat: add vector store integration
feat: add rag pipeline
feat: add retrieval evaluation
test: add prompt injection tests
test: add privacy filter tests
docs: add ai governance and non-advice policy
```
