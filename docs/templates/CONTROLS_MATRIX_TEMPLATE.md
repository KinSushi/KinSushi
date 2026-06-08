# Controls Matrix Template

| Control ID | Control name | Risk covered | Test / evidence | Frequency | Owner | Status |
|---|---|---|---|---|---|---|
| CTRL-001 | Required fields not null | Missing critical data | SQL null check | Every run | Data pipeline | Planned |
| CTRL-002 | Primary key uniqueness | Duplicate records | SQL uniqueness check | Every run | Data pipeline | Planned |
| CTRL-003 | Referential integrity | Broken relationships | FK / join validation | Every run | Data pipeline | Planned |
| CTRL-004 | Range validation | Implausible values | Min/max rule | Every run | Data pipeline | Planned |
| CTRL-005 | Freshness check | Stale data | Timestamp threshold | Daily | Data pipeline | Planned |
| CTRL-006 | Drift monitoring | Distribution shift | Evidently / NannyML report | Weekly | ML pipeline | Planned |
| CTRL-007 | Model performance | Degraded predictions | Precision / recall / PR-AUC | When labels available | ML pipeline | Planned |
| CTRL-008 | Secret hygiene | Credential exposure | `.gitignore` + secret scan | Every commit | Repo owner | Planned |
| CTRL-009 | Public-safety check | Private data leakage | Manual review checklist | Every release | Repo owner | Planned |
| CTRL-010 | Incident documentation | Poor operational handover | Runbook and incident note | Every incident | Repo owner | Planned |

## Usage

Adapt this matrix per repository.

A control should be:

- testable;
- linked to a risk;
- assigned to a system or owner;
- documented with evidence;
- safe for public GitHub.
