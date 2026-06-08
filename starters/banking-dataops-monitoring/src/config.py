"""Runtime configuration for the Banking DataOps Monitoring starter."""

from __future__ import annotations

from dataclasses import dataclass
import os


@dataclass(frozen=True)
class DatabaseConfig:
    """PostgreSQL connection configuration."""

    host: str = "localhost"
    port: int = 5432
    dbname: str = "banking_dataops"
    user: str = "dataops"
    password: str = "dataops_local_only"

    @property
    def dsn(self) -> str:
        """Return a psycopg-compatible DSN."""

        return (
            f"host={self.host} port={self.port} dbname={self.dbname} "
            f"user={self.user} password={self.password}"
        )


def load_database_config() -> DatabaseConfig:
    """Load database configuration from environment variables with safe local defaults."""

    return DatabaseConfig(
        host=os.getenv("BANKING_DATAOPS_DB_HOST", "localhost"),
        port=int(os.getenv("BANKING_DATAOPS_DB_PORT", "5432")),
        dbname=os.getenv("BANKING_DATAOPS_DB_NAME", "banking_dataops"),
        user=os.getenv("BANKING_DATAOPS_DB_USER", "dataops"),
        password=os.getenv("BANKING_DATAOPS_DB_PASSWORD", "dataops_local_only"),
    )
