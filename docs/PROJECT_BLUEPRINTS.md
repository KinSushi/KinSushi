# Project Blueprints

<div align="center">

**Reusable public project blueprints for Swiss banking, financial infrastructure and big-tech data roles**

DataOps · Data Engineering · MLOps · LLMOps · Governance · Production Readiness

![Blueprints](https://img.shields.io/badge/Blueprints-Portfolio%20Projects-1F6FEB?style=flat)
![DataOps](https://img.shields.io/badge/DataOps-SQL%20%2B%20Controls-2EA043?style=flat)
![MLOps](https://img.shields.io/badge/MLOps-MLflow%20%2B%20Serving-0194E2?style=flat)
![LLMOps](https://img.shields.io/badge/LLMOps-RAG%20%2B%20Governance-6F42C1?style=flat)

</div>

---

## Purpose

This file defines the future public repositories and their expected scope. It keeps the portfolio coherent without adding application material.

Each project must use synthetic or open data only.

---

## Blueprint 1 — banking-dataops-monitoring

### Goal

Prove SQL, Python, data quality, monitoring, incident investigation and production support readiness.

### Target role families

- Data Engineer
- DataOps Engineer
- Application & Data Support Engineer
- IT Production Engineer
- Data Quality Analyst
- Banking IT Analyst

### Repository structure

```text
banking-dataops-monitoring/
├── README.md
├── PORTFOLIO.md
├── docker-compose.yml
├── pyproject.toml
├── .github/workflows/ci.yml
├── data/
│ ├── synthetic_transactions.csv
│ └── synthetic_customers.csv
├── sql/
│ ├── schema.sql
│ ├── data_quality_checks.sql
│ ├── reconciliation_queries.sql
│ ├── anomaly_queries.sql
│ └── performance_queries.sql
├── src/
│ ├── ingest_transactions.py
│ ├── quality_checks.py
│ ├── monitoring.py
│ ├── alerting.py
│ └── incident_report.py
├── dashboard/
│ └── streamlit_app.py
├── tests/
│ ├── test_ingestion.py
│ └── test_quality_checks.py
└── docs/
 ├── architecture.md
 ├── data_dictionary.md
 ├── controls_matrix.md
 ├── incident_runbook.md
 └── rollback_plan.md
```

### Key evidence

| Evidence | Signal |
|---|---|
| PostgreSQL schema | data modeling and relational thinking |
| SQL quality checks | production data controls |
| Reconciliation queries | banking-style integrity checks |
| Streamlit dashboard | operational monitoring |
| Incident runbook | production support maturity |
| CI tests | software discipline |

---

## Blueprint 2 — fraud-mlops-control-tower

### Goal

Prove Data Science + MLOps + model governance using synthetic fraud/risk data.

### Target role families

- Data Scientist
- MLOps Engineer
- Fraud Analytics Engineer
- Risk Analytics Engineer
- ML Platform Engineer

### Repository structure

```text
fraud-mlops-control-tower/
├── README.md
├── PORTFOLIO.md
├── Dockerfile
├── docker-compose.yml
├── pyproject.toml
├── .github/workflows/ci.yml
├── data/
│ └── synthetic_transactions.csv
├── notebooks/
│ ├── 01_eda.ipynb
│ ├── 02_training.ipynb
│ └── 03_evaluation.ipynb
├── src/
│ ├── features.py
│ ├── train.py
│ ├── evaluate.py
│ ├── api.py
│ ├── monitor.py
│ └── drift_detection.py
├── tests/
│ ├── test_features.py
│ ├── test_api.py
│ └── test_monitoring.py
└── docs/
 ├── data_card.md
 ├── model_card.md
 ├── risk_assessment.md
 ├── monitoring_plan.md
 └── deployment_runbook.md
```

### Key evidence

| Evidence | Signal |
|---|---|
| PR-AUC / precision / recall | correct fraud metrics |
| MLflow tracking | reproducible ML lifecycle |
| FastAPI endpoint | model serving readiness |
| Dockerfile | deployability |
| model card / data card | governance maturity |
| monitoring plan | post-deployment awareness |

---

## Blueprint 3 — database-migration-quality-lab

### Goal

Prove legacy-to-modern migration, SQL validation and reconciliation.

### Target role families

- Data Engineer
- Data Migration Engineer
- Database Administrator
- Banking IT Analyst
- Core banking integration support

### Repository structure

```text
database-migration-quality-lab/
├── README.md
├── docker-compose.yml
├── pyproject.toml
├── sql/
│ ├── legacy_schema.sql
│ ├── target_schema.sql
│ ├── migration.sql
│ ├── validation_checks.sql
│ └── reconciliation_report.sql
├── src/
│ ├── migrate.py
│ ├── validate.py
│ └── generate_report.py
├── tests/
│ ├── test_migration.py
│ └── test_reconciliation.py
└── docs/
 ├── migration_strategy.md
 ├── data_quality_rules.md
 ├── rollback_plan.md
 └── performance_notes.md
```

### Key evidence

| Evidence | Signal |
|---|---|
| legacy + target schemas | migration understanding |
| validation SQL | quality controls |
| rollback plan | production safety |
| reconciliation report | banking-style auditability |
| performance notes | data engineering maturity |

---

## Blueprint 4 — secure-wealth-rag-assistant

### Goal

Prove RAG/LLMOps, privacy, retrieval evaluation and AI governance on synthetic private-banking documents.

### Target role families

- AI Engineer
- LLMOps Engineer
- GenAI Engineer
- AI Platform Engineer
- Wealth/Risk Analytics Engineer

### Repository structure

```text
secure-wealth-rag-assistant/
├── README.md
├── PORTFOLIO.md
├── pyproject.toml
├── docker-compose.yml
├── docs_sample/
│ ├── portfolio_report_sample.md
│ ├── market_note_sample.md
│ └── client_profile_synthetic.json
├── src/
│ ├── ingest_documents.py
│ ├── rag_pipeline.py
│ ├── guardrails.py
│ ├── evaluation.py
│ └── app.py
├── tests/
│ ├── test_retrieval.py
│ ├── test_prompt_injection.py
│ └── test_privacy_filters.py
└── docs/
 ├── hallucination_evaluation.md
 ├── prompt_injection_tests.md
 ├── privacy_controls.md
 ├── human_review_policy.md
 └── ai_governance.md
```

### Key evidence

| Evidence | Signal |
|---|---|
| synthetic documents | safe public portfolio |
| vector DB | practical RAG architecture |
| retrieval evaluation | measurable GenAI quality |
| prompt-injection tests | security awareness |
| PII masking | privacy controls |
| human review policy | regulated-AI maturity |

---

## Blueprint 5 — jedha-rncp35288-portfolio

### Goal

Provide a public sanitized technical map of the six Jedha RNCP Level 6 blocks.

### Repository structure

```text
jedha-rncp35288-portfolio/
├── README.md
├── bloc_1_data_infrastructure/
├── bloc_2_eda_statistics/
├── bloc_3_machine_learning/
├── bloc_4_nlp_deep_learning/
├── bloc_5_mlops_deployment/
├── bloc_6_project_governance/
└── docs/
 ├── evidence_index.md
 ├── public_safety_rules.md
 └── certification_mapping.md
```

### Public-safety constraint

Do not publish private school files, grades, certificates with IDs, administrative PDFs or non-public course content.

---

## Recommended project order

| Priority | Project | Reason |
|---:|---|---|
| 1 | `banking-dataops-monitoring` | Highest immediate employability signal for banking IT and DataOps |
| 2 | `fraud-mlops-control-tower` | Strong bridge from Data Science to MLOps and risk analytics |
| 3 | `jedha-rncp35288-portfolio` | Certification evidence and six-block structure |
| 4 | `database-migration-quality-lab` | Useful for banks, core banking vendors and integration firms |
| 5 | `secure-wealth-rag-assistant` | Strong but should come after SQL/DataOps/MLOps foundations |
# Project Blueprints

<div align="center">

**Reusable public project blueprints for Swiss banking, financial infrastructure and big-tech data roles**

DataOps · Data Engineering · MLOps · LLMOps · Governance · Production Readiness

![Blueprints](https://img.shields.io/badge/Blueprints-Portfolio%20Projects-1F6FEB?style=flat)
![DataOps](https://img.shields.io/badge/DataOps-SQL%20%2B%20Controls-2EA043?style=flat)
![MLOps](https://img.shields.io/badge/MLOps-MLflow%20%2B%20Serving-0194E2?style=flat)
![LLMOps](https://img.shields.io/badge/LLMOps-RAG%20%2B%20Governance-6F42C1?style=flat)

</div>

---

## Purpose

This file defines the future public repositories and their expected scope. It keeps the portfolio coherent without adding application material.

Each project must use synthetic or open data only.

---

## Blueprint 1 — banking-dataops-monitoring

### Goal

Prove SQL, Python, data quality, monitoring, incident investigation and production support readiness.

### Target role families

- Junior Data Engineer
- DataOps Engineer
- Application & Data Support Engineer
- IT Production Engineer Junior
- Data Quality Analyst
- Banking IT Analyst

### Repository structure

```text
banking-dataops-monitoring/
├── README.md
├── PORTFOLIO.md
├── docker-compose.yml
├── pyproject.toml
├── .github/workflows/ci.yml
├── data/
│   ├── synthetic_transactions.csv
│   └── synthetic_customers.csv
├── sql/
│   ├── schema.sql
│   ├── data_quality_checks.sql
│   ├── reconciliation_queries.sql
│   ├── anomaly_queries.sql
│   └── performance_queries.sql
├── src/
│   ├── ingest_transactions.py
│   ├── quality_checks.py
│   ├── monitoring.py
│   ├── alerting.py
│   └── incident_report.py
├── dashboard/
│   └── streamlit_app.py
├── tests/
│   ├── test_ingestion.py
│   └── test_quality_checks.py
└── docs/
    ├── architecture.md
    ├── data_dictionary.md
    ├── controls_matrix.md
    ├── incident_runbook.md
    └── rollback_plan.md
```

### Key evidence

| Evidence | Signal |
|---|---|
| PostgreSQL schema | data modeling and relational thinking |
| SQL quality checks | production data controls |
| Reconciliation queries | banking-style integrity checks |
| Streamlit dashboard | operational monitoring |
| Incident runbook | production support maturity |
| CI tests | software discipline |

---

## Blueprint 2 — fraud-mlops-control-tower

### Goal

Prove Data Science + MLOps + model governance using synthetic fraud/risk data.

### Target role families

- Junior Data Scientist
- Junior MLOps Engineer
- Fraud Analytics Engineer
- Risk Analytics Engineer
- ML Platform Engineer Junior

### Repository structure

```text
fraud-mlops-control-tower/
├── README.md
├── PORTFOLIO.md
├── Dockerfile
├── docker-compose.yml
├── pyproject.toml
├── .github/workflows/ci.yml
├── data/
│   └── synthetic_transactions.csv
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_training.ipynb
│   └── 03_evaluation.ipynb
├── src/
│   ├── features.py
│   ├── train.py
│   ├── evaluate.py
│   ├── api.py
│   ├── monitor.py
│   └── drift_detection.py
├── tests/
│   ├── test_features.py
│   ├── test_api.py
│   └── test_monitoring.py
└── docs/
    ├── data_card.md
    ├── model_card.md
    ├── risk_assessment.md
    ├── monitoring_plan.md
    └── deployment_runbook.md
```

### Key evidence

| Evidence | Signal |
|---|---|
| PR-AUC / precision / recall | correct fraud metrics |
| MLflow tracking | reproducible ML lifecycle |
| FastAPI endpoint | model serving readiness |
| Dockerfile | deployability |
| model card / data card | governance maturity |
| monitoring plan | post-deployment awareness |

---

## Blueprint 3 — database-migration-quality-lab

### Goal

Prove legacy-to-modern migration, SQL validation and reconciliation.

### Target role families

- Junior Data Engineer
- Data Migration Engineer
- Database Administrator Junior
- Banking IT Analyst
- Core banking integration support

### Repository structure

```text
database-migration-quality-lab/
├── README.md
├── docker-compose.yml
├── pyproject.toml
├── sql/
│   ├── legacy_schema.sql
│   ├── target_schema.sql
│   ├── migration.sql
│   ├── validation_checks.sql
│   └── reconciliation_report.sql
├── src/
│   ├── migrate.py
│   ├── validate.py
│   └── generate_report.py
├── tests/
│   ├── test_migration.py
│   └── test_reconciliation.py
└── docs/
    ├── migration_strategy.md
    ├── data_quality_rules.md
    ├── rollback_plan.md
    └── performance_notes.md
```

### Key evidence

| Evidence | Signal |
|---|---|
| legacy + target schemas | migration understanding |
| validation SQL | quality controls |
| rollback plan | production safety |
| reconciliation report | banking-style auditability |
| performance notes | data engineering maturity |

---

## Blueprint 4 — secure-wealth-rag-assistant

### Goal

Prove RAG/LLMOps, privacy, retrieval evaluation and AI governance on synthetic private-banking documents.

### Target role families

- Junior AI Engineer
- LLMOps Engineer Junior
- GenAI Engineer
- AI Platform Engineer
- Wealth/Risk Analytics Engineer

### Repository structure

```text
secure-wealth-rag-assistant/
├── README.md
├── PORTFOLIO.md
├── pyproject.toml
├── docker-compose.yml
├── docs_sample/
│   ├── portfolio_report_sample.md
│   ├── market_note_sample.md
│   └── client_profile_synthetic.json
├── src/
│   ├── ingest_documents.py
│   ├── rag_pipeline.py
│   ├── guardrails.py
│   ├── evaluation.py
│   └── app.py
├── tests/
│   ├── test_retrieval.py
│   ├── test_prompt_injection.py
│   └── test_privacy_filters.py
└── docs/
    ├── hallucination_evaluation.md
    ├── prompt_injection_tests.md
    ├── privacy_controls.md
    ├── human_review_policy.md
    └── ai_governance.md
```

### Key evidence

| Evidence | Signal |
|---|---|
| synthetic documents | safe public portfolio |
| vector DB | practical RAG architecture |
| retrieval evaluation | measurable GenAI quality |
| prompt-injection tests | security awareness |
| PII masking | privacy controls |
| human review policy | regulated-AI maturity |

---

## Blueprint 5 — jedha-rncp35288-portfolio

### Goal

Provide a public sanitized technical map of the six Jedha RNCP Level 6 blocks.

### Repository structure

```text
jedha-rncp35288-portfolio/
├── README.md
├── bloc_1_data_infrastructure/
├── bloc_2_eda_statistics/
├── bloc_3_machine_learning/
├── bloc_4_nlp_deep_learning/
├── bloc_5_mlops_deployment/
├── bloc_6_project_governance/
└── docs/
    ├── evidence_index.md
    ├── public_safety_rules.md
    └── certification_mapping.md
```

### Public-safety constraint

Do not publish private school files, grades, certificates with IDs, administrative PDFs or non-public course content.

---

## Recommended project order

| Priority | Project | Reason |
|---:|---|---|
| 1 | `banking-dataops-monitoring` | Highest immediate employability signal for banking IT and DataOps |
| 2 | `fraud-mlops-control-tower` | Strong bridge from Data Science to MLOps and risk analytics |
| 3 | `jedha-rncp35288-portfolio` | Certification evidence and six-block structure |
| 4 | `database-migration-quality-lab` | Useful for banks, core banking vendors and integration firms |
| 5 | `secure-wealth-rag-assistant` | Strong but should come after SQL/DataOps/MLOps foundations |
