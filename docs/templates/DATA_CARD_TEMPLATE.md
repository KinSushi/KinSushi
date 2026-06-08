# Data Card Template

## Dataset overview

| Field | Value |
|---|---|
| Dataset name | `<dataset_name>` |
| Version | `<version>` |
| Owner | `<repo_or_project>` |
| Data type | Synthetic / open data |
| Sensitive data | None |
| Intended use | Portfolio demo / model training / SQL validation |

## Dataset purpose

Describe why the dataset exists and which project it supports.

## Source

| Source | Type | Notes |
|---|---|---|
| Synthetic generator | Synthetic | No real banking/client data |
| Open dataset | Public | Include license if applicable |

## Schema

| Column | Type | Description | Quality rule |
|---|---|---|---|
| `<column>` | `<type>` | `<description>` | `<rule>` |

## Quality checks

| Check | Rule | Failure action |
|---|---|---|
| Null check | Required fields must not be null | Reject / flag row |
| Uniqueness | Primary key must be unique | Deduplicate / investigate |
| Range check | Values must be inside expected bounds | Flag anomaly |
| Referential integrity | Foreign keys must match reference table | Reject / investigate |
| Freshness | Dataset updated within expected period | Alert |

## Known limitations

- Synthetic data may not reflect real financial distributions.
- Some edge cases may be simplified.
- No client behavior should be inferred from this dataset.

## Privacy and compliance

- No real client data.
- No real account numbers.
- No real transaction identifiers.
- No PII.
- No employer or bank data.

## Usage boundaries

Allowed:

- portfolio demos;
- SQL validation;
- MLOps workflows;
- data-quality examples.

Not allowed:

- real decisioning;
- investment advice;
- real fraud operations;
- use as proxy for real banking populations.
