def utc_now_iso() -> str:
    from datetime import UTC, datetime
    return datetime.now(UTC).isoformat()