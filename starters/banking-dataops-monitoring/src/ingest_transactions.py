"""Load synthetic CSV datasets into PostgreSQL."""

from __future__ import annotations

from pathlib import Path

from db import connect, execute_sql_file

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
SQL_DIR = ROOT / "sql"


def bootstrap_schema() -> None:
    """Create target tables from the starter schema."""

    execute_sql_file(SQL_DIR / "00_schema.sql")


def _copy_csv(table_name: str, csv_path: Path) -> None:
    """Copy a CSV file into PostgreSQL using psycopg COPY."""

    if not csv_path.exists():
        raise FileNotFoundError(f"Missing CSV file: {csv_path}")

    with connect() as connection:
        with connection.cursor() as cursor:
            with csv_path.open("r", encoding="utf-8") as file:
                with cursor.copy(f"COPY {table_name} FROM STDIN WITH CSV HEADER") as copy:
                    for line in file:
                        copy.write(line)
        connection.commit()


def load_all() -> None:
    """Load all synthetic datasets into the database."""

    bootstrap_schema()
    _copy_csv("customers", DATA_DIR / "synthetic_customers.csv")
    _copy_csv("accounts", DATA_DIR / "synthetic_accounts.csv")
    _copy_csv("transactions", DATA_DIR / "synthetic_transactions.csv")


if __name__ == "__main__":
    load_all()
