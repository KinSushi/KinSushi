"""Synthetic risk/anomaly dataset generator.

The dataset is fake and safe for public GitHub. It is intended for MLOps,
model-evaluation and governance demonstrations only.
"""

from __future__ import annotations

import csv
from dataclasses import dataclass
from pathlib import Path
import random
import uuid


@dataclass(frozen=True)
class RiskDataConfig:
    rows: int = 1000
    seed: int = 42


def generate(config: RiskDataConfig, output_path: Path) -> None:
    rng = random.Random(config.seed)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    fields = [
        "event_id",
        "amount_chf",
        "hour",
        "customer_tenure_days",
        "channel_mobile",
        "channel_web",
        "country_risk_score",
        "previous_alerts_30d",
        "velocity_1h",
        "is_anomaly",
    ]

    with output_path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        for _ in range(config.rows):
            amount = round(rng.lognormvariate(4.2, 0.9), 2)
            hour = rng.randint(0, 23)
            tenure = rng.randint(1, 4000)
            previous_alerts = rng.choices([0, 1, 2, 3, 4], weights=[80, 12, 5, 2, 1])[0]
            velocity = rng.randint(1, 30)
            country_risk = round(rng.random(), 3)
            channel = rng.choice(["mobile", "web"])
            score = (
                (amount > 5000) * 0.25
                + (hour < 5) * 0.15
                + (tenure < 90) * 0.15
                + (previous_alerts >= 2) * 0.25
                + (velocity > 12) * 0.15
                + (country_risk > 0.8) * 0.15
                + rng.random() * 0.10
            )
            is_anomaly = score > 0.45
            writer.writerow(
                {
                    "event_id": f"EVT-{uuid.uuid4().hex[:12].upper()}",
                    "amount_chf": amount,
                    "hour": hour,
                    "customer_tenure_days": tenure,
                    "channel_mobile": int(channel == "mobile"),
                    "channel_web": int(channel == "web"),
                    "country_risk_score": country_risk,
                    "previous_alerts_30d": previous_alerts,
                    "velocity_1h": velocity,
                    "is_anomaly": int(is_anomaly),
                }
            )


if __name__ == "__main__":
    generate(RiskDataConfig(), Path("data/synthetic_risk_events.csv"))
