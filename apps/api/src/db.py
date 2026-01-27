from __future__ import annotations

from typing import Any

from supabase import create_client, Client
from .config import settings


def get_supabase_client() -> Client | None:
    """Return a supabase client or None if configuration is incomplete."""
    url = settings.supabase_url
    key = settings.supabase_service_role_key
    if not url or not key:
        return None
    return create_client(url, key)


supabase: Client | None = get_supabase_client()
