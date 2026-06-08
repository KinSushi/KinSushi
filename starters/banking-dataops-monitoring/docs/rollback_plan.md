# Rollback Plan — Banking DataOps Monitoring

## Purpose

This rollback plan defines how to safely reset the synthetic local environment.

It is not a production rollback plan. It is public technical evidence showing operational thinking.

---

## Reset strategy

The local environment is disposable and synthetic. The safest rollback is to remove local containers and volumes, then regenerate the synthetic dataset.

```bash
make reset
```

This runs:

```bash
docker compose down -v
docker compose up -d
python src/generate_synthetic_data.py
python src/ingest_transactions.py
python src/quality_checks.py
```

---

## Manual rollback

```bash
# Stop services and delete local volume
docker compose down -v

# Restart PostgreSQL
docker compose up -d

# Regenerate synthetic data
python src/generate_synthetic_data.py

# Re-ingest synthetic data
python src/ingest_transactions.py

# Re-run quality checks
python src/quality_checks.py
```

---

## Pre-rollback checklist

- [ ] confirm this is the local synthetic environment;
- [ ] no real data has been loaded;
- [ ] current failure has been documented if relevant;
- [ ] no private logs or screenshots will be published.

---

## Post-rollback validation

```bash
make quality
make reconcile
make test
```

Expected:

- quality checks execute;
- reconciliation returns source-system summaries;
- tests pass.

---

## Public-safety note

Do not use this rollback pattern for a production system. It is a portfolio artifact for synthetic local data only.
