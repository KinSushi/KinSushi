"""Feature engineering helpers for synthetic risk/anomaly modeling."""

from __future__ import annotations

import pandas as pd

FEATURE_COLUMNS = [
    "amount_chf",
    "hour",
    "customer_tenure_days",
    "channel_mobile",
    "channel_web",
    "country_risk_score",
    "previous_alerts_30d",
    "velocity_1h",
]
TARGET_COLUMN = "is_anomaly"


def split_features_target(frame: pd.DataFrame) -> tuple[pd.DataFrame, pd.Series]:
    """Return X/y after validating required columns."""

    missing = [column for column in [*FEATURE_COLUMNS, TARGET_COLUMN] if column not in frame.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")
    return frame[FEATURE_COLUMNS].copy(), frame[TARGET_COLUMN].astype(int).copy()
