"""Celery tasks related to ingesting opportunities from external systems."""

from ..celery_app import celery_app


@celery_app.task(name="src.tasks.ingest_tasks.ingest_sam_task")
def ingest_sam_task(opp_id: str) -> dict:
    """Stub task to ingest data for a given opportunity from SAM.

    Args:
        opp_id: The opportunity identifier.

    Returns:
        A placeholder dictionary indicating the task was executed.
    """
    return {"status": "stub", "task": "ingest_sam_task", "opp_id": opp_id}
