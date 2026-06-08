# Controls Matrix

| Control ID | Control name | Risk covered | Evidence | Frequency | Status |
|---|---|---|---|---|---|
| CTRL-001 | Critical fields not null | Missing key operational data | `sql/02_data_quality_checks.sql` | Every run | Planned |
| CTRL-002 | Transaction ID uniqueness | Duplicate transaction records | `sql/02_data_quality_checks.sql` | Every run | Planned |
| CTRL-003 | Amount validity | Implausible transaction amounts | `sql/02_data_quality_checks.sql` | Every run | Planned |
| CTRL-004 | Referential integrity | Orphan transactions without account | `sql/02_data_quality_checks.sql` | Every run | Planned |
| CTRL-005 | Freshness | Stale transaction dataset | `sql/02_data_quality_checks.sql` | Daily | Planned |
| CTRL-006 | Source-system reconciliation | Source imbalance or missing feeds | `sql/03_reconciliation_queries.sql` | Daily | Planned |
| CTRL-007 | Channel-level monitoring | Operational anomalies by channel | `sql/03_reconciliation_queries.sql` | Daily | Planned |
| CTRL-008 | Public-safety check | Private or real data exposure | manual review | Every release | Planned |

## Public-safety rule

All datasets must be synthetic or open. Do not publish real banking, insurance, health, client or employer data.
