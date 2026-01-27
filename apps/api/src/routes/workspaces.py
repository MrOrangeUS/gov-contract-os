from __future__ import annotations

from fastapi import APIRouter
from pydantic import BaseModel

from ..db import supabase


router = APIRouter()


class WorkspaceCreate(BaseModel):
    opportunity_id: str
    name: str | None = None


@router.post("")
def create_workspace(body: WorkspaceCreate) -> dict:
    """Create a new bid workspace for an opportunity.

    If Supabase is not configured, returns a placeholder response.
    """
    if not supabase:
        return {"id": "placeholder", "name": body.name or "Bid Workspace", "opportunity_id": body.opportunity_id}
    payload = {
        "opportunity_id": body.opportunity_id,
        "name": body.name or "Bid Workspace",
    }
    data = supabase.table("workspaces").insert(payload).execute().data
    return data[0] if data else payload