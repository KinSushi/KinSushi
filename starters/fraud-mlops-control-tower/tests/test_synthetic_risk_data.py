from pathlib import Path
import sys

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from generate_synthetic_risk_data import RiskDataConfig, generate
from features import FEATURE_COLUMNS, TARGET_COLUMN, split_features_target


def test_generate_synthetic_risk_data(tmp_path: Path) -> None:
    output = tmp_path / "synthetic_risk_events.csv"
    generate(RiskDataConfig(rows=25), output)

    frame = pd.read_csv(output)

    assert len(frame) == 25
    assert TARGET_COLUMN in frame.columns
    assert set(FEATURE_COLUMNS).issubset(frame.columns)


def test_split_features_target(tmp_path: Path) -> None:
    output = tmp_path / "synthetic_risk_events.csv"
    generate(RiskDataConfig(rows=10), output)
    frame = pd.read_csv(output)

    features, target = split_features_target(frame)

    assert list(features.columns) == FEATURE_COLUMNS
    assert len(target) == 10
    assert set(target.unique()).issubset({0, 1})
