# Portfolio Quality Gates

<div align="center">

**Definition of Done for public Data / MLOps / AI portfolio repositories**

Data quality · Tests · CI/CD · Documentation · Security hygiene · Governance · Reproducibility

![Quality](https://img.shields.io/badge/Quality-Gates-2EA043?style=flat)
![Security](https://img.shields.io/badge/Security-No%20Secrets-DC143C?style=flat)
![MLOps](https://img.shields.io/badge/MLOps-Ready-0194E2?style=flat)
![Governance](https://img.shields.io/badge/Governance-Audit%20Evidence-6F42C1?style=flat)

</div>

---

## Purpose

This document defines the minimum quality standard for every public technical repository in this GitHub portfolio.

The goal is to show employability across regulated finance and large-scale engineering environments without publishing CVs, cover letters, private documents or employer-specific application material.

---

## Repository maturity levels

| Level | Meaning | Minimum evidence |
|---:|---|---|
| 0 | Idea | README with scope, non-goals and public-safety rules |
| 1 | Prototype | Reproducible local run, sample data, basic documentation |
| 2 | Engineering-ready | Tests, linting, Docker or reproducible environment, architecture notes |
| 3 | Portfolio-ready | Runbook, data/model governance docs, screenshots or sample outputs, CI |
| 4 | Bank-grade demo | Monitoring plan, controls matrix, risk assessment, rollback plan, security notes |

Public goal: reach **Level 3** for most repositories and **Level 4** for `banking-dataops-monitoring` and `fraud-mlops-control-tower`.

---

## Global Definition of Done

A public repository is considered portfolio-ready only if it has:

| Gate | Required evidence |
|---|---|
| Clear purpose | README explains the problem, scope, architecture and non-goals |
| Synthetic/open data | No real banking, client, employer or private data |
| Reproducibility | Setup instructions, dependencies and deterministic sample run |
| Code quality | `ruff` or equivalent, clear modules, no notebook-only logic |
| Tests | At least unit tests for core business logic or data checks |
| Operational docs | Runbook or operations notes |
| Security hygiene | `.gitignore`, no secrets, sanitized examples |
| Data governance | Data dictionary or data card when data is central |
| Model governance | Model card and monitoring plan when ML is central |
| Visual clarity | Badges, architecture diagram, tables and concise documentation |

---

## DataOps quality gates

For `banking-dataops-monitoring` and `database-migration-quality-lab`:

| Gate | Evidence |
|---|---|
| Schema design | SQL schema file and data dictionary |
| Data validation | SQL checks and Python validation runner |
| Reconciliation | Source-vs-target or expected-vs-observed report |
| Monitoring | Dashboard or CLI summary of quality status |
| Incident workflow | Incident runbook and failure-mode table |
| Performance awareness | At least one note on indexing, query plans or batch size |
| Controls matrix | Control name, risk covered, test query, owner, frequency |

---

## MLOps quality gates

For `fraud-mlops-control-tower`:

| Gate | Evidence |
|---|---|
| Experiment tracking | MLflow runs or equivalent screenshots / instructions |
| Model registry logic | Versioned model artifact and metadata |
| API serving | FastAPI endpoint with request/response example |
| Containerization | Dockerfile and local run command |
| Tests | Feature tests, API tests, scoring tests |
| Monitoring | Drift/performance monitoring plan or Evidently/NannyML demo |
| Governance | Model card, data card, risk assessment, deployment runbook |
| Failure handling | Rollback or fallback behavior documented |

---

## LLMOps quality gates

For `secure-wealth-rag-assistant`:

| Gate | Evidence |
|---|---|
| Synthetic documents | No private client or bank documents |
| Retrieval evaluation | Precision/recall-style retrieval checks or benchmark set |
| Hallucination control | Faithfulness or citation-grounding evaluation |
| Prompt-injection tests | Adversarial prompt examples and expected defenses |
| PII controls | PII masking/anonymization notes |
| Human oversight | Review policy for sensitive outputs |
| Governance | AI risk assessment and usage boundaries |
| Non-advice disclaimer | No investment advice claims |

---

## Visual quality gates

Every repo should include:

- centered title block with badges;
- one-line executive summary;
- architecture diagram using Mermaid or ASCII;
- “Why this matters” table;
- setup block;
- portfolio signal section;
- documentation index;
- public-safety / non-goals section.

Recommended README order:

```text
1. Title + badges
2. Executive summary
3. Documentation index
4. Problem statement
5. Architecture
6. Key features
7. Tech stack
8. Setup
9. Quality / controls
10. Portfolio signal
11. Non-goals
```

---

## Public-safety gate

Before publication, verify:

- no real bank data;
- no client data;
- no employer-specific application content;
- no CV or cover letter;
- no salary target;
- no private school document;
- no certificates with personal identifiers;
- no secrets, hostnames, tokens, keys or license values;
- screenshots are sanitized.

---

## Final test

A recruiter or engineering manager should be able to answer within 60 seconds:

1. What problem does this repo solve?
2. What technical skills does it prove?
3. How can it be run or reviewed?
4. What makes it relevant to regulated finance or large-scale engineering?
5. What safety/governance controls are documented?
