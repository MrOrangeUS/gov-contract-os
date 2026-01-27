"""Celery tasks related to attachment synchronization."""

from ..celery_app import celery_app


@celery_app.task(name="src.tasks.attachment_tasks.sync_attachments_task")
def sync_attachments_task(opp_id: str) -> dict:
    """Stub task to sync attachments for a given opportunity.

    Args:
        opp_id: The opportunity identifier.

    Returns:
        A placeholder dictionary indicating the task was executed.
    """
    return {"status": "stub", "task": "sync_attachments_task", "opp_id": opp_id}
