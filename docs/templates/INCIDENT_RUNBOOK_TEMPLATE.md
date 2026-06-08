# Incident Runbook Template

## Incident metadata

| Field | Value |
|---|---|
| Incident title | `<short_title>` |
| Date / time | `YYYY-MM-DD HH:MM` |
| Project | `<repo_name>` |
| Severity | Low / Medium / High |
| Status | Open / Mitigated / Resolved |
| Owner | `<owner>` |

## Impact

Describe what failed and what was affected.

Examples:

- Data ingestion failed.
- SQL quality checks flagged a control breach.
- Model API returned invalid predictions.
- Dashboard did not refresh.
- Scheduled job did not run.

## Detection

How was the issue detected?

- log review;
- dashboard alert;
- failed CI;
- failed data-quality check;
- manual review;
- API error.

## Symptoms

```text
Paste sanitized logs, errors or observations here.
```

## Root cause

Explain the technical root cause.

## Resolution steps

```bash
# Commands or operational steps used to resolve
```

## Rollback plan

Describe how to restore the previous stable state.

## Preventive actions

| Action | Owner | Status |
|---|---|---|
| Add test | TBD | Open |
| Improve logging | TBD | Open |
| Update runbook | TBD | Open |

## Evidence

- sanitized log snippet;
- commit reference;
- screenshot without secrets;
- SQL query output;
- test result.

## Lessons learned

Summarize what should change in the system or process.
