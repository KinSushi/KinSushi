from decimal import Decimal
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from reconciliation import SourceSystemSummary


def test_source_system_summary_shape() -> None:
    summary = SourceSystemSummary(
        source_system="core_banking",
        transaction_count=42,
        total_amount_chf=Decimal("1234.56"),
    )

    assert summary.source_system == "core_banking"
    assert summary.transaction_count == 42
    assert summary.total_amount_chf == Decimal("1234.56")
