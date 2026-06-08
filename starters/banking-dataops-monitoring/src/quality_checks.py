"""Data-quality checks for the Banking DataOps Monitoring starter."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime

from db import connect


@dataclass(frozen=True)
class QualityCheck:
    """A single SQL-backed data-quality check."""

    check_id: str
    check_name: str
    sql: str
    failure_threshold: int = 0


@dataclass(frozen=True)
class QualityCheckResult:
    """Result of a single quality check."""

    check_id: str
    check_name: str
    failed_rows: int
    status: str
    executed_at: datetime


def status_from_failed_rows(failed_rows: int, threshold: int = 0) -> str:
    """Return PASS when failures are within threshold, otherwise FAIL."""

    return "PASS" if failed_rows <= threshold else "FAIL"


QUALITY_CHECKS = [
    QualityCheck(
        check_id="CTRL-001",
        check_name="critical_nulls",
        sql="""
            SELECT COUNT(*)
            FROM transactions
            WHERE transaction_id IS NULL
               OR account_id IS NULL
               OR event_timestamp IS NULL
               OR amount_chf IS NULL
        """,
    ),
    QualityCheck(
        check_id="CTRL-002",
        check_name="duplicate_transactions",
        sql="""
            SELECT COUNT(*)
            FROM (
                SELECT transaction_id
                FROM transactions
                GROUP BY transaction_id
                HAVING COUNT(*) > 1
            ) duplicates
        """,
    ),
    QualityCheck(
        check_id="CTRL-003",
        check_name="invalid_amounts",
        sql="""
            SELECT COUNT(*)
            FROM transactions
            WHERE amount_chf <= 0 OR amount_chf > 1000000
        """,
    ),
    QualityCheck(
        check_id="CTRL-004",
        check_name="orphan_transactions",
        sql="""
            SELECT COUNT(*)
            FROM transactions t
            LEFT JOIN accounts a ON t.account_id = a.account_id
            WHERE a.account_id IS NULL
        """,
    ),
]


def run_quality_checks() -> list[QualityCheckResult]:
    """Run all configured quality checks and persist summary results."""

    results: list[QualityCheckResult] = []
    executed_at = datetime.utcnow()
    with connect() as connection:
        with connection.cursor() as cursor:
            for check in QUALITY_CHECKS:
                cursor.execute(check.sql)
                failed_rows = int(cursor.fetchone()[0])
                result = QualityCheckResult(
                    check_id=check.check_id,
                    check_name=check.check_name,
                    failed_rows=failed_rows,
                    status=status_from_failed_rows(failed_rows, check.failure_threshold),
                    executed_at=executed_at,
                )
                results.append(result)
                cursor.execute(
                    """
                    INSERT INTO quality_check_results
                        (check_id, check_name, status, failed_rows, executed_at)
                    VALUES (%s, %s, %s, %s, %s)
                    ON CONFLICT (check_id)
                    DO UPDATE SET
                        check_name = EXCLUDED.check_name,
                        status = EXCLUDED.status,
                        failed_rows = EXCLUDED.failed_rows,
                        executed_at = EXCLUDED.executed_at
                    """,
                    (
                        result.check_id,
                        result.check_name,
                        result.status,
                        result.failed_rows,
                        result.executed_at,
                    ),
                )
        connection.commit()
    return results


def print_quality_summary(results: list[QualityCheckResult]) -> None:
    """Print a CLI-friendly quality summary."""

    for result in results:
        print(f"{result.check_id} | {result.status} | {result.check_name} | failed={result.failed_rows}")


if __name__ == "__main__":
    print_quality_summary(run_quality_checks())
