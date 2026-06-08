"""Streamlit dashboard for the Banking DataOps Monitoring starter."""

from __future__ import annotations

import pandas as pd
import streamlit as st

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from db import connect  # noqa: E402


st.set_page_config(page_title="Banking DataOps Monitoring", layout="wide")

st.title("Banking DataOps Monitoring")
st.caption("Synthetic regulated-data monitoring dashboard — public technical evidence only")


def read_sql(query: str) -> pd.DataFrame:
    with connect() as connection:
        return pd.read_sql_query(query, connection)


try:
    quality = read_sql(
        """
        SELECT check_id, check_name, status, failed_rows, executed_at
        FROM quality_check_results
        ORDER BY check_id
        """
    )
    transactions_by_day = read_sql(
        """
        SELECT booking_date, COUNT(*) AS transaction_count, SUM(amount_chf) AS total_amount_chf
        FROM transactions
        GROUP BY booking_date
        ORDER BY booking_date
        """
    )
    source_summary = read_sql(
        """
        SELECT source_system, COUNT(*) AS transaction_count, SUM(amount_chf) AS total_amount_chf
        FROM transactions
        GROUP BY source_system
        ORDER BY source_system
        """
    )
except Exception as exc:  # pragma: no cover - dashboard runtime path
    st.error("Database is not ready. Start PostgreSQL, generate data, ingest CSVs and run checks.")
    st.code(str(exc))
    st.stop()

st.subheader("Quality status")
if quality.empty:
    st.warning("No quality checks have been executed yet. Run `make quality`.")
else:
    passed = int((quality["status"] == "PASS").sum())
    failed = int((quality["status"] == "FAIL").sum())
    col1, col2, col3 = st.columns(3)
    col1.metric("Checks", len(quality))
    col2.metric("Passed", passed)
    col3.metric("Failed", failed)
    st.dataframe(quality, use_container_width=True)

st.subheader("Transaction volume by day")
st.line_chart(transactions_by_day.set_index("booking_date")["transaction_count"])

st.subheader("Source-system reconciliation")
st.dataframe(source_summary, use_container_width=True)

st.subheader("Public-safety note")
st.info("This dashboard uses synthetic data only. No real bank, insurance, health, client or employer data should be loaded.")
