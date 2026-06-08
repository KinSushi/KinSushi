from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from generate_synthetic_data import SyntheticConfig, generate


def test_generate_synthetic_data_files(tmp_path: Path) -> None:
    generate(SyntheticConfig(customers=3, accounts_per_customer=2, transactions=10), tmp_path)

    assert (tmp_path / "synthetic_customers.csv").exists()
    assert (tmp_path / "synthetic_accounts.csv").exists()
    assert (tmp_path / "synthetic_transactions.csv").exists()

    assert len((tmp_path / "synthetic_customers.csv").read_text().splitlines()) == 4
    assert len((tmp_path / "synthetic_accounts.csv").read_text().splitlines()) == 7
    assert len((tmp_path / "synthetic_transactions.csv").read_text().splitlines()) == 11
