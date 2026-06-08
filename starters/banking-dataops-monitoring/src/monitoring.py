"""Monitoring summary helpers for the Banking DataOps starter."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class QualitySummary:
    """Aggregated quality status for dashboard and CLI output."""

    total_checks: int
    passed_checks: int
    failed_checks: int

    @property
    def overall_status(self) -> str:
        """Return PASS if no checks failed, otherwise FAIL."""

        return "PASS" if self.failed_checks == 0 else "FAIL"


def summarize_quality_status(statuses: list[str]) -> QualitySummary:
    """Summarize PASS/FAIL statuses."""

    normalized = [status.upper() for status in statuses]
    passed = normalized.count("PASS")
    failed = normalized.count("FAIL")
    return QualitySummary(
        total_checks=len(normalized),
        passed_checks=passed,
        failed_checks=failed,
    )
