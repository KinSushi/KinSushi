# Premium Phase Roadmap

## Purpose

This document defines the next portfolio phase after the public GitHub hardening pass.

The current portfolio already has executable validation evidence across DataOps, MLOps, migration quality, RAG/LLMOps and the Jedha evidence map. The next phase is not basic repair. It is premium polish: screenshots, clearer validation, targeted refinements and recruiter-facing coherence.

---

## Current baseline

| Layer | Repository | Current evidence |
|---|---|---|
| DataOps | `banking-dataops-monitoring` | pip install, compileall, pytest, ruff, synthetic data generation, imports |
| MLOps | `fraud-mlops-control-tower` | pip install, compileall, pytest, ruff, synthetic data generation, imports, MLflow training |
| Data migration | `database-migration-quality-lab` | pip install, compileall, pytest, ruff, synthetic legacy data generation, imports |
| LLMOps / RAG | `secure-wealth-rag-assistant` | pip install, compileall, pytest, ruff, import check, RAG demo |
| Certification evidence | `jedha-rncp35288-portfolio` | required file checks and public sanitized structure |

---

## Phase 1 — Final GitHub presentation

Priority: P0.

Actions:

- pin repositories in strategic order;
- verify all five repositories are public;
- verify README banners render correctly;
- verify `docs/local_run_report.md` is visible in every active repository;
- verify `docs/screenshots/validation-preview.svg` renders correctly;
- keep all job-search material out of public GitHub.

Recommended pinned repositories:

```text
1. banking-dataops-monitoring
2. fraud-mlops-control-tower
3. database-migration-quality-lab
4. secure-wealth-rag-assistant
5. sovralys-infra-lab
6. pty-flights-pricing
```

---

## Phase 2 — True UI screenshots

Priority: P1.

The current screenshots are validation-output previews. They are acceptable and honest, but they are not yet full UI screenshots.

Target visuals:

| Repository | Premium screenshot target |
|---|---|
| `banking-dataops-monitoring` | Streamlit dashboard with quality status, volume chart and reconciliation table |
| `fraud-mlops-control-tower` | FastAPI `/docs`, MLflow run page, metrics JSON |
| `database-migration-quality-lab` | validation/reconciliation report table |
| `secure-wealth-rag-assistant` | RAG CLI answer with sources and safety boundary |
| `jedha-rncp35288-portfolio` | six-block evidence map |

Screenshots must be sanitized. They must not expose private paths, tokens, emails, hostnames, IP addresses or private data.

---

## Phase 3 — Technical upgrades

Priority: P1/P2.

| Repository | Upgrade |
|---|---|
| `banking-dataops-monitoring` | add Docker-backed integration validation and dashboard screenshot |
| `fraud-mlops-control-tower` | add precision-recall curve output and threshold report |
| `database-migration-quality-lab` | add generated reconciliation report artifact |
| `secure-wealth-rag-assistant` | format RAG answer as Answer / Sources / Safety Boundary / Human Review |
| `jedha-rncp35288-portfolio` | add stronger public-safety scan for forbidden files and folders |

---

## Phase 4 — Recruiter-facing coherence

Priority: P1.

Actions:

- align LinkedIn headline with GitHub positioning;
- align CV headline with `Junior Data / MLOps Engineer for regulated and data-intensive systems`;
- do not mention application strategy inside public repos;
- keep Swiss banking, insurance, health data, pharma/medtech and big-tech compatibility visible but neutral;
- avoid narrow positioning around one company.

---

## Phase 5 — What not to do

Do not add:

- CVs;
- cover letters;
- job trackers;
- recruiter messages;
- salary targets;
- private school documents;
- exam material;
- grades;
- real client data;
- real employer data;
- secrets or tokens.

---

## Final target

The final public signal should be:

> Reliable data and ML systems for regulated and data-intensive environments: SQL, Python, DataOps, MLOps, migration quality, RAG/LLMOps, validation evidence, monitoring and governance.
