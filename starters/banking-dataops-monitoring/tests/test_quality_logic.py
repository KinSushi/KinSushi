from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from db import split_sql_statements
from quality_checks import QualityCheckResult, status_from_failed_rows
from datetime import datetime


def test_status_from_failed_rows() -> None:
    assert status_from_failed_rows(0) == "PASS"
    assert status_from_failed_rows(1) == "FAIL"
    assert status_from_failed_rows(1, threshold=1) == "PASS"


def test_quality_check_result_shape() -> None:
    result = QualityCheckResult(
        check_id="CTRL-001",
        check_name="critical_nulls",
        failed_rows=0,
        status="PASS",
        executed_at=datetime.utcnow(),
    )

    assert result.check_id == "CTRL-001"
    assert result.status == "PASS"


def test_split_sql_statements() -> None:
    statements = split_sql_statements("SELECT 1; SELECT 2;   ")

    assert statements == ["SELECT 1", "SELECT 2"]
