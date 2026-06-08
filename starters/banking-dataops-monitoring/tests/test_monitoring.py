from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from monitoring import summarize_quality_status


def test_summarize_quality_status_pass() -> None:
    summary = summarize_quality_status(["PASS", "PASS"])

    assert summary.total_checks == 2
    assert summary.passed_checks == 2
    assert summary.failed_checks == 0
    assert summary.overall_status == "PASS"


def test_summarize_quality_status_fail() -> None:
    summary = summarize_quality_status(["PASS", "FAIL"])

    assert summary.total_checks == 2
    assert summary.passed_checks == 1
    assert summary.failed_checks == 1
    assert summary.overall_status == "FAIL"
