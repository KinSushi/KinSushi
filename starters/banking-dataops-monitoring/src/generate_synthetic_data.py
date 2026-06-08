"""Synthetic regulated-data generator for the banking-dataops-monitoring starter.

The generated data is fake and safe for public GitHub. It is designed to test
SQL quality checks, reconciliation queries and monitoring dashboards.
"""

from __future__ import annotations

import csv
from dataclasses import dataclass
from datetime import UTC, datetime, timedelta
from pathlib import Path
import random
import uuid


@dataclass(frozen=True)
class SyntheticConfig:
    customers: int = 50
    accounts_per_customer: int = 2
    transactions: int = 500
    seed: int = 42


def _write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def generate(config: SyntheticConfig, output_dir: Path) -> None:
    rng = random.Random(config.seed)
    customer_segments = ["retail", "premium", "sme"]
    countries = ["CH", "FR", "DE", "IT"]
    channels = ["web", "mobile", "branch", "api"]
    categories = ["grocery", "travel", "health", "utilities", "electronics", "services"]
    source_systems = ["core_banking", "card_processor", "payments_gateway"]

    customers: list[dict[str, object]] = []
    accounts: list[dict[str, object]] = []

    for index in range(config.customers):
        customer_id = f"CUST-{index:05d}"
        customers.append(
            {
                "customer_id": customer_id,
                "customer_segment": rng.choice(customer_segments),
                "country": rng.choice(countries),
                "created_at": datetime.now(UTC).isoformat(),
            }
        )
        for account_index in range(config.accounts_per_customer):
            accounts.append(
                {
                    "account_id": f"ACC-{index:05d}-{account_index:02d}",
                    "customer_id": customer_id,
                    "account_type": rng.choice(["current", "savings"]),
                    "currency": "CHF",
                    "opened_at": datetime.now(UTC).isoformat(),
                }
            )

    transactions: list[dict[str, object]] = []
    base_time = datetime.now(UTC) - timedelta(days=30)
    for _ in range(config.transactions):
        account = rng.choice(accounts)
        timestamp = base_time + timedelta(minutes=rng.randint(0, 30 * 24 * 60))
        amount = round(rng.lognormvariate(4.0, 0.8), 2)
        risk_score = round(min(0.9999, rng.random() ** 2), 4)
        transactions.append(
            {
                "transaction_id": f"TX-{uuid.uuid4().hex[:12].upper()}",
                "account_id": account["account_id"],
                "source_system": rng.choice(source_systems),
                "event_timestamp": timestamp.isoformat(),
                "booking_date": timestamp.date().isoformat(),
                "amount_chf": amount,
                "currency": "CHF",
                "channel": rng.choice(channels),
                "merchant_category": rng.choice(categories),
                "country": rng.choice(countries),
                "risk_score": risk_score,
                "status": rng.choice(["posted", "posted", "posted", "pending", "rejected"]),
                "is_suspicious": risk_score > 0.85,
                "created_at": datetime.now(UTC).isoformat(),
            }
        )

    _write_csv(output_dir / "synthetic_customers.csv", customers)
    _write_csv(output_dir / "synthetic_accounts.csv", accounts)
    _write_csv(output_dir / "synthetic_transactions.csv", transactions)


if __name__ == "__main__":
    generate(SyntheticConfig(), Path("data"))
