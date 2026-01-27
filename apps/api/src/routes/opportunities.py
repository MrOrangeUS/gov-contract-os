from __future__ import annotations

from fastapi import APIRouter, Query

from ..db import supabase


router = APIRouter()


@router.get("")
def list_opportunities(
    state: str | None = None,
    source: str | None = None,
    q: str | None = None,
    limit: int = Query(default=50, le=200),
) -> list[dict]:
    """Return a list of opportunities filtered by state, source, and optional search query.

    If Supabase is not configured, returns an empty list.
    """
    if not supabase:
        return []
    query = supabase.table("opportunities").select("*").order("due_at", desc=False).limit(limit)
    if state:
        query = query.eq("state", state)
    if source:
        query = query.eq("source", source)
    if q:
        pattern = f"%{q}%"
        query = query.or_(f"title.ilike.{pattern},summary.ilike.{pattern}")
    data = query.execute().data or []
    return data


@router.get("/{opp_id}")
def get_opportunity(opp_id: str) -> dict | None:
    """Return a single opportunity by ID."""
    if not supabase:
        return None
    res = supabase.table("opportunities").select("*").eq("id", opp_id).single().execute()
    return res.data