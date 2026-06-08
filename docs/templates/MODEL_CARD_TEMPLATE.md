# Model Card Template

## Model overview

| Field | Value |
|---|---|
| Model name | `<model_name>` |
| Version | `<version>` |
| Owner | `<project_or_repo>` |
| Use case | `<fraud/risk/churn/document classification/etc.>` |
| Status | Prototype / Portfolio demo / Deprecated |
| Data type | Synthetic / open data only |

## Intended use

Describe what the model is designed to do.

## Out-of-scope use

Describe what the model must not be used for.

Examples:

- No real credit decisioning.
- No investment advice.
- No fully automated fraud blocking without human review.
- No use on real client data.

## Training data

| Dataset | Source | Notes |
|---|---|---|
| `<dataset_name>` | Synthetic / open | `<description>` |

## Features

| Feature | Description | Risk / limitation |
|---|---|---|
| `<feature>` | `<description>` | `<risk>` |

## Evaluation metrics

| Metric | Value | Why it matters |
|---|---:|---|
| Precision | TBD | False-positive control |
| Recall | TBD | Missed-risk control |
| F1 | TBD | Balance |
| PR-AUC | TBD | Better for imbalanced fraud/risk data |
| ROC-AUC | TBD | General separability |

## Explainability

Document the explainability method:

- SHAP;
- permutation importance;
- feature importance;
- error analysis.

## Known limitations

- Synthetic data may not represent real distribution shifts.
- Historical bias cannot be assessed without real-world context.
- Model behavior should not be interpreted as bank-grade validation.

## Monitoring plan

| Risk | Monitor | Action |
|---|---|---|
| Data drift | Feature distribution | Investigate / retrain |
| Performance drift | Precision, recall, PR-AUC | Recalibrate threshold |
| Label delay | Missing ground truth | Use proxy monitoring |
| Operational failure | API errors, latency | Rollback / disable endpoint |

## Human oversight

Describe when human review is required.

## Governance notes

- This is a public portfolio model.
- Data is synthetic or open.
- No production use without independent validation.
- No real client impact.
