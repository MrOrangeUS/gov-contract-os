"""Celery task for orchestrating the opportunity processing pipeline."""

from ..celery_app import celery_app


@celery_app.task(name="src.tasks.pipeline_tasks.run_pipeline_task")
def run_pipeline_task(opp_id: str) -> dict:
    """Stub task to run the full processing pipeline for an opportunity.

    Args:
        opp_id: The opportunity identifier.

    Returns:
        A placeholder dictionary indicating the task was executed.
    """
    return {"status": "stub", "task": "run_pipeline_task", "opp_id": opp_id}
