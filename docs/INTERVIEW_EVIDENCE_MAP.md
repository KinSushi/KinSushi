# Interview Evidence Map

This document maps common technical interview questions to public portfolio evidence.

It is not an interview script and does not contain employer-specific preparation. It is a public technical evidence map.

---

## DataOps / Application Support questions

| Interview question | Public evidence target |
|---|---|
| How do you detect bad data? | `banking-dataops-monitoring`: SQL checks, Python runner, controls matrix |
| How do you investigate duplicate transactions? | reconciliation queries, incident runbook |
| How do you monitor a scheduled pipeline? | `pty-flights-pricing`, `OPERATIONS.md`, log examples |
| How do you handle a failed cron job? | operations notes, incident template |
| How do you validate source vs target data? | `database-migration-quality-lab`, reconciliation report |

---

## Data Engineering questions

| Interview question | Public evidence target |
|---|---|
| How do you design a relational schema? | PostgreSQL schema and data dictionary |
| How do you handle incremental loads? | ingestion scripts and freshness checks |
| How do you document data quality rules? | controls matrix, data card |
| How do you migrate legacy data? | migration strategy and rollback plan |
| How do you optimize a SQL query? | performance notes and indexing comments |

---

## MLOps questions

| Interview question | Public evidence target |
|---|---|
| How do you track experiments? | MLflow runs in `fraud-mlops-control-tower` |
| How do you deploy a model? | FastAPI endpoint, Dockerfile, deployment runbook |
| How do you monitor drift? | Evidently/NannyML or monitoring plan |
| How do you roll back a model? | deployment runbook and rollback plan |
| How do you document model risk? | model card, risk assessment |

---

## LLMOps / GenAI questions

| Interview question | Public evidence target |
|---|---|
| How do you evaluate RAG retrieval? | retrieval evaluation report |
| How do you reduce hallucinations? | faithfulness / citation-grounding tests |
| How do you defend against prompt injection? | prompt-injection tests |
| How do you protect PII? | privacy controls and PII masking notes |
| How do you keep humans in the loop? | human review policy |

---

## Infrastructure / Production questions

| Interview question | Public evidence target |
|---|---|
| How do you recover a failed VM? | `sovralys-infra-lab` operations runbook |
| How do you harden public documentation? | `SECURITY.md`, hardening checklist |
| How do you monitor host health? | monitoring baseline |
| Why separate Docker/Jupyter from Windows VM workloads? | ADR-001 host/VM separation |
| How do you verify backups? | backup restore test procedure |

---

## Governance / regulated finance questions

| Interview question | Public evidence target |
|---|---|
| How do you document data lineage or controls? | controls matrix, data dictionary |
| How do you document model limitations? | model card |
| How do you avoid publishing private data? | public repository rules, private workspace guide |
| How do you handle AI governance? | AI governance docs in RAG/MLOps repos |
| How do you ensure public portfolio safety? | PR template and public-safety gates |

---

## Final rule

Do not write employer-specific answers in this repository.

Use this file to map public evidence to technical capabilities only.
