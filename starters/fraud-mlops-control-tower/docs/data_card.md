# Data Card — Synthetic Risk Events

## Dataset overview

| Field | Value |
|---|---|
| Dataset name | synthetic_risk_events.csv |
| Type | Synthetic |
| Sensitive data | None |
| Intended use | Public MLOps and model-governance demo |

---

## Columns

| Column | Description |
|---|---|
| event_id | Synthetic unique event identifier |
| amount_chf | Synthetic amount in CHF |
| hour | Event hour, 0-23 |
| customer_tenure_days | Synthetic tenure proxy |
| channel_mobile | Binary channel flag |
| channel_web | Binary channel flag |
| country_risk_score | Synthetic country-risk proxy |
| previous_alerts_30d | Synthetic previous-alert count |
| velocity_1h | Synthetic short-window event velocity |
| is_anomaly | Synthetic target label |

---

## Quality rules

- `event_id` must be unique.
- numeric values must be non-null.
- `hour` must be between 0 and 23.
- channel flags must be binary.
- target must be binary.

---

## Public-safety note

This dataset is generated and synthetic. It must not be interpreted as real banking, insurance, health, client or employer data.
