# Incident Runbook — Banking DataOps Monitoring

## Incident metadata

| Field | Value |
|---|---|
| Incident title | `<short title>` |
| Date / time | `YYYY-MM-DD HH:MM` |
| Severity | Low / Medium / High |
| Status | Open / Mitigated / Resolved |
| Owner | DataOps pipeline |

---

## Detection

An incident can be detected through:

- failed SQL quality check;
- failed reconciliation query;
- dashboard status change;
- failed scheduled run;
- failed CI test;
- manual review.

---

## Triage steps

1. Identify failed control ID.
2. Review failed row count.
3. Check latest ingestion timestamp.
4. Compare source-system reconciliation summary.
5. Isolate affected booking date or source system.
6. Generate incident note.
7. Decide: fix data, rerun ingestion, or document known issue.

---

## Example investigation commands

```bash
# Start local database
make up

# Run SQL checks
make quality

# Run tests
make test

# Start dashboard
make dashboard
```

---

## Root-cause categories

| Category | Examples |
|---|---|
| Data ingestion | missing file, malformed rows, source delay |
| Data quality | nulls, duplicates, invalid amounts |
| Reconciliation | missing source system, unexpected totals |
| Runtime | container down, database unavailable |
| Documentation | missing data dictionary or control description |

---

## Resolution template

```markdown
# Incident: <title>

## Impact

What failed and which dataset/control was affected?

## Symptoms

Failed query, row count, dashboard status or log excerpt.

## Root cause

Technical explanation.

## Resolution

Steps taken.

## Preventive action

Additional control, test or documentation update.
```

---

## Public-safety rule

Do not paste real client, bank, insurance, health, account or employer data into incident notes. Use sanitized or synthetic examples only.
