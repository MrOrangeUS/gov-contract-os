from fastapi import APIRouter

from ..db import supabase


router = APIRouter()


@router.get("/ping")
def ping() -> dict[str, bool]:
    """Simple health check. Optionally pings Supabase."""
    if supabase:
        try:
            # Attempt a trivial select to keep the connection warm
            supabase.table("opportunities").select("id").limit(1).execute()
        except Exception:
            # Ignore errors in health ping; just return ok
            pass
    return {"ok": True}
