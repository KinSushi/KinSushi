"""Database helpers for PostgreSQL-backed starter workflows."""

from __future__ import annotations

from collections.abc import Iterable
from pathlib import Path

import psycopg

from config import DatabaseConfig, load_database_config


def connect(config: DatabaseConfig | None = None) -> psycopg.Connection:
    """Open a PostgreSQL connection."""

    return psycopg.connect((config or load_database_config()).dsn)


def split_sql_statements(sql_text: str) -> list[str]:
    """Split simple SQL files into executable statements.

    This is intentionally minimal and sufficient for the starter SQL files. It is
    not a general SQL parser.
    """

    return [statement.strip() for statement in sql_text.split(";") if statement.strip()]


def execute_sql_file(path: Path, config: DatabaseConfig | None = None) -> None:
    """Execute all statements from a SQL file inside one transaction."""

    statements = split_sql_statements(path.read_text(encoding="utf-8"))
    with connect(config) as connection:
        with connection.cursor() as cursor:
            for statement in statements:
                cursor.execute(statement)
        connection.commit()


def execute_sql_files(paths: Iterable[Path], config: DatabaseConfig | None = None) -> None:
    """Execute a sequence of SQL files."""

    for path in paths:
        execute_sql_file(path, config=config)
