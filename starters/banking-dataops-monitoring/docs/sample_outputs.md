# Sample Outputs — Banking DataOps Monitoring

This file documents expected local outputs for the starter kit.

The values below are examples. Actual values may differ because the synthetic generator can be configured.

---

## Synthetic data generation

```bash
make generate
```

Expected files:

```text
data/synthetic_customers.csv
data/synthetic_accounts.csv
data/synthetic_transactions.csv
```

---

## Quality checks

```bash
make quality
```

Example output:

```text
CTRL-001 | PASS | critical_nulls | failed=0
CTRL-002 | PASS | duplicate_transactions | failed=0
CTRL-003 | PASS | invalid_amounts | failed=0
CTRL-004 | PASS | orphan_transactions | failed=0
```

---

## Reconciliation

```bash
make reconcile
```

Example output:

```text
card_processor | count=165 | total_chf=154231.40
core_banking | count=170 | total_chf=161882.75
payments_gateway | count=165 | total_chf=149923.20
```

---

## Dashboard

```bash
make dashboard
```

Expected dashboard sections:

- Quality status;
- Transaction volume by day;
- Source-system reconciliation;
- Public-safety note.

---

## CI

```bash
make ci
```

Expected local checks:

- Ruff linting;
- pytest unit tests.

---

## Public-safety note

All outputs are generated from synthetic data. Do not paste real operational output from a bank, insurance, health, employer or client system into this file.
