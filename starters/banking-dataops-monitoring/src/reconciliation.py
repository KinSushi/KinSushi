"""Reconciliation summaries for synthetic regulated-data flows."""

from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal

from db import connect


@dataclass(frozen=True)
class SourceSystemSummary:
    """Source-system reconciliation summary."""

    source_system: str
    transaction_count: int
    total_amount_chf: Decimal


def source_system_summary() -> list[SourceSystemSummary]:
    """Return transaction counts and totals by source system."""

    query = """
        SELECT source_system, COUNT(*) AS transaction_count, ROUND(SUM(amount_chf), 2)
        FROM transactions
        GROUP BY source_system
        ORDER BY source_system
    """
    with connect() as connection:
        with connection.cursor() as cursor:
            cursor.execute(query)
            rows = cursor.fetchall()
    return [SourceSystemSummary(row[0], int(row[1]), row[2]) for row in rows]


def print_reconciliation_summary(summary: list[SourceSystemSummary]) -> None:
    """Print a CLI-friendly reconciliation summary."""

    for row in summary:
        print(f"{row.source_system} | count={row.transaction_count} | total_chf={row.total_amount_chf}")


if __name__ == "__main__":
    print_reconciliation_summary(source_system_summary())
