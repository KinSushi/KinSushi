# fraud-mlops-control-tower — Starter Kit

<div align="center">

**Synthetic risk/anomaly analytics project with MLOps, model governance and monitored serving**

Python · scikit-learn · MLflow · FastAPI · Docker · CI/CD · Model Card · Data Card

![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=flat&logo=python&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-F7931E?style=flat&logo=scikitlearn&logoColor=white)
![MLflow](https://img.shields.io/badge/MLflow-Tracking-0194E2?style=flat&logo=mlflow&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-Serving-009688?style=flat&logo=fastapi&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Packaging-2496ED?style=flat&logo=docker&logoColor=white)
![Governance](https://img.shields.io/badge/Governance-Model%20Risk-6F42C1?style=flat)

</div>

---

## Purpose

This starter kit defines the future `fraud-mlops-control-tower` repository.

It is a public, synthetic MLOps project designed to prove:

- supervised model training on imbalanced risk/anomaly data;
- model evaluation using recall, precision, F1 and PR-AUC;
- MLflow experiment tracking;
- FastAPI model serving;
- Docker packaging;
- monitoring and drift documentation;
- model card, data card and risk assessment.

No real banking, insurance, health, client, employer or private data belongs here.

---

## Target roles

| Role family | Why this project helps |
|---|---|
| Junior Data Scientist | feature engineering, evaluation, threshold analysis |
| Junior MLOps Engineer | MLflow, FastAPI, Docker, tests, runbooks |
| Risk Analytics Engineer | risk/anomaly modeling and model limitations |
| AI Platform Engineer Junior | model lifecycle, serving, governance, monitoring |
| Insurance / finance analytics | synthetic claims/risk-style modeling patterns |

---

## Planned repository structure

```text
fraud-mlops-control-tower/
├── README.md
├── PORTFOLIO.md
├── Dockerfile
├── docker-compose.yml
├── pyproject.toml
├── .env.example
├── .github/workflows/ci.yml
├── data/
│   └── synthetic_risk_events.csv
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_training.ipynb
│   └── 03_evaluation.ipynb
├── src/
│   ├── config.py
│   ├── generate_synthetic_risk_data.py
│   ├── features.py
│   ├── train.py
│   ├── evaluate.py
│   ├── api.py
│   ├── monitor.py
│   └── drift_detection.py
├── tests/
│   ├── test_synthetic_data.py
│   ├── test_features.py
│   └── test_api_schema.py
└── docs/
    ├── data_card.md
    ├── model_card.md
    ├── risk_assessment.md
    ├── monitoring_plan.md
    └── deployment_runbook.md
```

---

## Minimum viable demo

The first functional version must include:

- synthetic data generator;
- feature engineering module;
- baseline model training script;
- evaluation report focused on imbalanced data;
- MLflow tracking;
- FastAPI `/health` and `/predict` endpoints;
- Dockerfile;
- pytest tests;
- GitHub Actions CI;
- model card, data card and monitoring plan.

---

## Public-safety rules

- synthetic data only;
- no real client data;
- no production decisioning claims;
- no performance guarantees;
- no employer-specific application content;
- no CVs, cover letters or job trackers;
- no secrets or private infrastructure identifiers.
