"""Utilities for authenticating job endpoints."""

from fastapi import Header, HTTPException

from ..config import settings


def require_jobs_key(x_jobs_key: str | None = Header(default=None)) -> None:
    """Validate that the provided X-Jobs-Key header matches the configured jobs API key."""
    configured = settings.jobs_api_key
    if not configured or x_jobs_key != configured:
        raise HTTPException(status_code=401, detail="Unauthorized")
