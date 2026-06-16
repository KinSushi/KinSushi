# database-migration-quality-lab — Starter Kit

<div align="center">

**Legacy-to-target data migration lab with SQL validation, reconciliation and rollback documentation**

PostgreSQL · SQL · Python · Data Quality · Migration · Reconciliation · Rollback

![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-4169E1?style=flat&logo=postgresql&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-Migration%20%2F%20Validation-003B57?style=flat)
![Python](https://img.shields.io/badge/Python-Automation-3776AB?style=flat&logo=python&logoColor=white)
![Data Quality](https://img.shields.io/badge/Data%20Quality-Reconciliation-2EA043?style=flat)
![Public Safety](https://img.shields.io/badge/Data-Synthetic%20Only-24292F?style=flat)

</div>

---

## Purpose

This starter kit defines the future `database-migration-quality-lab` repository.

It is designed to prove legacy-to-modern migration thinking, SQL validation, source-to-target reconciliation, rollback planning and production-style documentation.

No real core-banking, insurance, health, client, employer or private data belongs here.

---

## Target roles

| Role family | Why this project helps |
|---|---|
| Data Engineer | schema design, migration SQL and validation |
| Data Migration Engineer | legacy-to-target mapping and rollback planning |
| Banking / insurance IT | regulated-data reconciliation and controls |
| Data Quality Analyst | validation rules and quality evidence |
| Integration / consulting | migration documentation and handover discipline |

---

## Planned repository structure

```text
database-migration-quality-lab/
├── README.md
├── docker-compose.yml
├── pyproject.toml
├── sql/
│ ├── 00_legacy_schema.sql
│ ├── 01_target_schema.sql
│ ├── 02_seed_legacy_data.sql
│ ├── 03_migration.sql
│ ├── 04_validation_checks.sql
│ └── 05_reconciliation_report.sql
├── src/
│ ├── migrate.py
│ ├── validate.py
│ └── generate_report.py
├── tests/
│ └── test_migration_contract.py
└── docs/
 ├── migration_strategy.md
 ├── data_quality_rules.md
 ├── rollback_plan.md
 └── performance_notes.md
```

---

## Minimum viable demo

- legacy schema;
- target schema;
- seed data;
- migration SQL;
- validation SQL;
- reconciliation report SQL;
- Python script to run migration/validation;
- rollback plan;
- tests for mapping contract.

---

## Public-safety rules

- synthetic data only;
- no real client records;
- no employer-specific application content;
- no private documents;
- no secrets;
- no production migration claims.
# database-migration-quality-lab — Starter Kit

<div align="center">

**Legacy-to-target data migration lab with SQL validation, reconciliation and rollback documentation**

PostgreSQL · SQL · Python · Data Quality · Migration · Reconciliation · Rollback

![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-4169E1?style=flat&logo=postgresql&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-Migration%20%2F%20Validation-003B57?style=flat)
![Python](https://img.shields.io/badge/Python-Automation-3776AB?style=flat&logo=python&logoColor=white)
![Data Quality](https://img.shields.io/badge/Data%20Quality-Reconciliation-2EA043?style=flat)
![Public Safety](https://img.shields.io/badge/Data-Synthetic%20Only-24292F?style=flat)

</div>

---

## Purpose

This starter kit defines the future `database-migration-quality-lab` repository.

It is designed to prove legacy-to-modern migration thinking, SQL validation, source-to-target reconciliation, rollback planning and production-style documentation.

No real core-banking, insurance, health, client, employer or private data belongs here.

---

## Target roles

| Role family | Why this project helps |
|---|---|
| Data Engineer | schema design, migration SQL and validation |
| Data Migration Engineer | legacy-to-target mapping and rollback planning |
| Banking / insurance IT | regulated-data reconciliation and controls |
| Data Quality Analyst | validation rules and quality evidence |
| Integration / consulting | migration documentation and handover discipline |

---

## Planned repository structure

```text
database-migration-quality-lab/
├── README.md
├── docker-compose.yml
├── pyproject.toml
├── sql/
│ ├── 00_legacy_schema.sql
│ ├── 01_target_schema.sql
│ ├── 02_seed_legacy_data.sql
│ ├── 03_migration.sql
│ ├── 04_validation_checks.sql
│ └── 05_reconciliation_report.sql
├── src/
│ ├── migrate.py
│ ├── validate.py
│ └── generate_report.py
├── tests/
│ └── test_migration_contract.py
└── docs/
 ├── migration_strategy.md
 ├── data_quality_rules.md
 ├── rollback_plan.md
 └── performance_notes.md
```

---

## Minimum viable demo

- legacy schema;
- target schema;
- seed data;
- migration SQL;
- validation SQL;
- reconciliation report SQL;
- Python script to run migration/validation;
- rollback plan;
- tests for mapping contract.

---

## Public-safety rules

- synthetic data only;
- no real client records;
- no employer-specific application content;
- no private documents;
- no secrets;
- no production migration claims.
