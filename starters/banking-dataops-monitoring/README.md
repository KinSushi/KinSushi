# banking-dataops-monitoring — Executable Starter

<div align="center">

**DataOps monitoring lab for regulated-data production support roles**

PostgreSQL · Python · SQL controls · Streamlit · Data quality · Reconciliation · Incident runbooks

![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=flat&logo=python&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-4169E1?style=flat&logo=postgresql&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?style=flat&logo=streamlit&logoColor=white)
![Data Quality](https://img.shields.io/badge/Data%20Quality-SQL%20Controls-2EA043?style=flat)
![CI](https://img.shields.io/badge/CI-GitHub%20Actions-2088FF?style=flat&logo=githubactions&logoColor=white)
![Public Safety](https://img.shields.io/badge/Data-Synthetic%20Only-24292F?style=flat)

</div>

---

## Executive summary

This starter is now an executable seed for the future `banking-dataops-monitoring` repository.

It demonstrates a full local DataOps control loop using synthetic regulated-data patterns:

```text
synthetic data -> PostgreSQL -> SQL controls -> Python runner -> reconciliation -> Streamlit dashboard -> runbook
```

It is designed to prove SQL, Python, data quality, data reconciliation, monitoring, incident investigation and regulated-data production support readiness.

No real banking, insurance, health, client, employer or private data belongs here.

---

## Documentation index

| Document | Purpose |
|---|---|
| [PORTFOLIO.md](PORTFOLIO.md) | Recruiter-readable technical brief |
| [docs/architecture.md](docs/architecture.md) | System architecture and execution flow |
| [docs/data_dictionary.md](docs/data_dictionary.md) | Table and field definitions |
| [docs/controls_matrix.md](docs/controls_matrix.md) | Data controls mapped to risks and evidence |
| [docs/incident_runbook.md](docs/incident_runbook.md) | Incident investigation workflow |
| [docs/rollback_plan.md](docs/rollback_plan.md) | Local reset and rollback procedure |
| [docs/sample_outputs.md](docs/sample_outputs.md) | Expected CLI and dashboard outputs |

---

## Target roles

| Role family | Why this project helps |
|---|---|
| Junior Data Engineer | schema, ingestion, SQL and Python data flow |
| DataOps Engineer | quality checks, monitoring, reconciliation, runbooks |
| Application & Data Support | incident investigation and operational controls |
| Data Quality Analyst | controls matrix and validation evidence |
| Banking / insurance IT | production-style checks on regulated-data patterns |
| Big-tech data platforms | reproducibility, CI, tests and monitoring pattern |

---

## Repository structure

```text
banking-dataops-monitoring/
├── README.md
├── PORTFOLIO.md
├── docker-compose.yml
├── pyproject.toml
├── Makefile
├── .env.example
├── data/                         # generated locally, not committed
├── sql/
│   ├── 00_schema.sql
│   ├── 02_data_quality_checks.sql
│   └── 03_reconciliation_queries.sql
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── db.py
│   ├── generate_synthetic_data.py
│   ├── ingest_transactions.py
│   ├── quality_checks.py
│   ├── reconciliation.py
│   └── monitoring.py
├── dashboard/
│   └── streamlit_app.py
├── tests/
│   ├── test_synthetic_data.py
│   ├── test_quality_logic.py
│   ├── test_reconciliation_logic.py
│   └── test_monitoring.py
└── docs/
    ├── architecture.md
    ├── data_dictionary.md
    ├── controls_matrix.md
    ├── incident_runbook.md
    ├── rollback_plan.md
    └── sample_outputs.md
```

---

## Local execution

```bash
# install dependencies
make install

# start PostgreSQL
make up

# generate synthetic data
make generate

# load CSV files into PostgreSQL
make ingest

# run quality controls
make quality

# run reconciliation summary
make reconcile

# launch dashboard
make dashboard
```

One-command local reset:

```bash
make reset
```

---

## Quality controls

| Control | Evidence |
|---|---|
| Critical nulls | `src/quality_checks.py`, `sql/02_data_quality_checks.sql` |
| Duplicate transactions | `src/quality_checks.py`, `sql/02_data_quality_checks.sql` |
| Invalid amounts | `src/quality_checks.py`, `sql/02_data_quality_checks.sql` |
| Referential integrity | `src/quality_checks.py`, `sql/02_data_quality_checks.sql` |
| Source-system reconciliation | `src/reconciliation.py`, `sql/03_reconciliation_queries.sql` |
| Dashboard monitoring | `dashboard/streamlit_app.py` |
| Incident workflow | `docs/incident_runbook.md` |
| Rollback/reset | `docs/rollback_plan.md` |

---

## Tests and CI

Local checks:

```bash
make ci
```

The root profile repository also contains a GitHub Actions workflow for this starter:

```text
.github/workflows/banking-dataops-starter-ci.yml
```

---

## Level 4 readiness

| Gate | Status |
|---|---|
| Synthetic data | Present |
| PostgreSQL schema | Present |
| Docker Compose | Present |
| Python ingestion | Present |
| SQL controls | Present |
| Python quality runner | Present |
| Reconciliation runner | Present |
| Streamlit dashboard | Present |
| Tests | Present |
| CI | Present |
| Data dictionary | Present |
| Controls matrix | Present |
| Incident runbook | Present |
| Rollback plan | Present |

---

## Public-safety rules

- synthetic data only;
- no real bank data;
- no real insurance or health data;
- no real client data;
- no employer-specific application content;
- no CVs, cover letters or job trackers;
- no secrets, tokens, hostnames or private IPs.

---

## Promotion path

When repository creation is available, copy this folder into a dedicated repository named `banking-dataops-monitoring`, keep the same public-safety rules, and add screenshots from the local dashboard.
