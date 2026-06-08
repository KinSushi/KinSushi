# 24-Week Execution Plan

This plan turns the public GitHub profile into a technical portfolio for Swiss regulated finance and Swiss big-tech data environments.

Application material remains outside GitHub.

---

## Phase overview

| Phase | Weeks | Main outcome |
|---|---:|---|
| 1 | 1-2 | Existing repos polished and hardened |
| 2 | 3-6 | `banking-dataops-monitoring` Level 4 demo |
| 3 | 7-11 | `fraud-mlops-control-tower` Level 4 demo |
| 4 | 12-14 | `jedha-rncp35288-portfolio` public six-block evidence |
| 5 | 15-17 | `database-migration-quality-lab` Level 3/4 demo |
| 6 | 18-22 | `secure-wealth-rag-assistant` Level 3 demo |
| 7 | 23-24 | Public profile polish and private application readiness |

---

## Weeks 1-2 — Existing repositories

| Task | Repository | Deliverable |
|---|---|---|
| Add hardening checklist | `sovralys-infra-lab` | `docs/HARDENING_CHECKLIST.md` |
| Add monitoring baseline | `sovralys-infra-lab` | `docs/MONITORING_BASELINE.md` |
| Add backup restore procedure | `sovralys-infra-lab` | `docs/BACKUP_RESTORE_TEST.md` |
| Add Data/MLOps runtime example | `sovralys-infra-lab` | Docker Compose example |
| Add requirements and pyproject | `pty-flights-pricing` | `requirements.txt`, `pyproject.toml` |
| Add tests and CI | `pty-flights-pricing` | `tests/`, GitHub Actions |

---

## Weeks 3-6 — banking-dataops-monitoring

| Week | Focus | Deliverable |
|---:|---|---|
| 3 | Skeleton and runtime | README, Docker Compose, PostgreSQL |
| 4 | Synthetic data and schema | customers, accounts, transactions |
| 5 | Data quality and reconciliation | SQL checks, Python runner |
| 6 | Dashboard and docs | Streamlit, controls matrix, runbook, CI |

Definition of Done:

- Docker Compose works.
- PostgreSQL schema loads.
- Synthetic data generator runs.
- SQL quality checks execute.
- Streamlit dashboard displays status.
- Tests pass in CI.
- Data dictionary and controls matrix exist.
- No real banking data.

---

## Weeks 7-11 — fraud-mlops-control-tower

| Week | Focus | Deliverable |
|---:|---|---|
| 7 | Synthetic fraud dataset and EDA | notebook and data card draft |
| 8 | Baselines and MLflow | logistic regression, random forest, MLflow runs |
| 9 | Evaluation and thresholds | PR-AUC, recall, precision, threshold policy |
| 10 | Serving and containerization | FastAPI, Docker, tests |
| 11 | Governance | model card, risk assessment, monitoring plan |

Definition of Done:

- MLflow logs experiments.
- FastAPI `/predict` works.
- Docker build works.
- Tests pass in CI.
- Model card, data card and risk assessment are complete.
- Monitoring and rollback plan are documented.

---

## Weeks 12-14 — jedha-rncp35288-portfolio

| Week | Focus | Deliverable |
|---:|---|---|
| 12 | Public skeleton | one folder per block |
| 13 | Sanitized evidence | README, notebooks, scripts, reports |
| 14 | Final polish | evidence index, public-safety rules |

Definition of Done:

- Six blocks visible.
- No private school files.
- No certificates with personal identifiers.
- Evidence is technical and sanitized.
- Level 6 / Level 7 wording remains conservative and accurate.

---

## Weeks 15-17 — database-migration-quality-lab

| Week | Focus | Deliverable |
|---:|---|---|
| 15 | Legacy and target schema | SQL schemas |
| 16 | Migration and validation | migration script, validation checks |
| 17 | Reconciliation and rollback | report, rollback plan, CI |

Definition of Done:

- Legacy schema and target schema exist.
- Migration is reproducible.
- Validation checks run.
- Reconciliation report is generated.
- Rollback plan is documented.

---

## Weeks 18-22 — secure-wealth-rag-assistant

| Week | Focus | Deliverable |
|---:|---|---|
| 18 | Synthetic documents | sample corpus |
| 19 | Ingestion and vector store | embeddings and retrieval |
| 20 | RAG app | API or dashboard |
| 21 | Evaluation and attacks | retrieval eval, hallucination checks, prompt injection tests |
| 22 | Governance | privacy controls, human review policy, non-advice policy |

Definition of Done:

- Synthetic documents only.
- Retrieval evaluation exists.
- Prompt-injection tests exist.
- PII controls are documented.
- Human review and non-advice policy are documented.

---

## Weeks 23-24 — final public polish and private applications

Public GitHub:

- update pinned repository order;
- update README repository map with active repos;
- add screenshots;
- close completed portfolio issues;
- verify no application material is public.

Private workspace outside GitHub:

- CV variants;
- cover letters;
- job tracker;
- recruiter messages;
- interview notes;
- salary strategy;
- school/certification private documents.

---

## Weekly operating rhythm

| Day | Work type |
|---|---|
| Monday | Plan work, review issues |
| Tuesday-Wednesday | Build code / SQL / tests |
| Thursday | Documentation, runbooks, controls |
| Friday | CI, polish, screenshots, commit hygiene |
| Weekend | Review, LinkedIn/private career updates outside GitHub |

---

## Rule

Do not keep extending documentation forever. Each phase must produce runnable or reviewable technical evidence.
