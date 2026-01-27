"""Celery tasks for parsing opportunities and generating compliance documents."""

from ..celery_app import celery_app


@celery_app.task(name="src.tasks.parse_tasks.parse_opportunity_task")
def parse_opportunity_task(opp_id: str) -> dict:
    """Stub task to parse an opportunity.

    Args:
        opp_id: The opportunity identifier.

    Returns:
        A placeholder dictionary indicating the task was executed.
    """
    return {"status": "stub", "task": "parse_opportunity_task", "opp_id": opp_id}


@celery_app.task(name="src.tasks.parse_tasks.extract_requirements_task")
def extract_requirements_task(opp_id: str) -> dict:
    """Stub task to extract requirements from an opportunity.

    Args:
        opp_id: The opportunity identifier.

    Returns:
        A placeholder dictionary indicating the task was executed.
    """
    return {"status": "stub", "task": "extract_requirements_task", "opp_id": opp_id}


@celery_app.task(name="src.tasks.parse_tasks.export_compliance_xlsx_task")
def export_compliance_xlsx_task(opp_id: str) -> dict:
    """Stub task to export a compliance XLSX for an opportunity.

    Args:
        opp_id: The opportunity identifier.

    Returns:
        A placeholder dictionary indicating the task was executed.
    """
    return {"status": "stub", "task": "export_compliance_xlsx_task", "opp_id": opp_id}
