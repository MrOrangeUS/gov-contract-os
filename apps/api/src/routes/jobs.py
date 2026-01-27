from __future__ import annotations

from fastapi import APIRouter, Depends, Path
from pydantic import BaseModel

from ._jobs_auth import require_jobs_key
from ..jobs_client import celery_client


router = APIRouter()


class EnqueueResponse(BaseModel):
    task_id: str
    task_name: str


############### TASK NAME CONSTANTS ###############

# These strings must match the task names defined in the Celery worker
TASK_INGEST_SAM = "src.tasks.ingest_tasks.ingest_sam_task"
TASK_SYNC_ATTACHMENTS = "src.tasks.attachment_tasks.sync_attachments_task"
TASK_PARSE_OPP = "src.tasks.parse_tasks.parse_opportunity_task"
TASK_REQS_OPP = "src.tasks.parse_tasks.extract_requirements_task"
TASK_XLSX_OPP = "src.tasks.parse_tasks.export_compliance_xlsx_task"
TASK_RUN_PIPELINE = "src.tasks.pipeline_tasks.run_pipeline_task"


@router.post("/ingest/sam", response_model=EnqueueResponse)
def enqueue_ingest_sam(_: None = Depends(require_jobs_key)) -> EnqueueResponse:
    """Enqueue the SAM.gov ingestion job."""
    result = celery_client.send_task(TASK_INGEST_SAM)
    return EnqueueResponse(task_id=result.id, task_name=TASK_INGEST_SAM)


@router.post("/opportunity/{opp_id}/sync-attachments", response_model=EnqueueResponse)
def enqueue_sync_attachments(
    opp_id: str = Path(...),
    _: None = Depends(require_jobs_key),
) -> EnqueueResponse:
    result = celery_client.send_task(TASK_SYNC_ATTACHMENTS, args=[opp_id])
    return EnqueueResponse(task_id=result.id, task_name=TASK_SYNC_ATTACHMENTS)


@router.post("/opportunity/{opp_id}/parse", response_model=EnqueueResponse)
def enqueue_parse_opportunity(
    opp_id: str = Path(...),
    _: None = Depends(require_jobs_key),
) -> EnqueueResponse:
    result = celery_client.send_task(TASK_PARSE_OPP, args=[opp_id])
    return EnqueueResponse(task_id=result.id, task_name=TASK_PARSE_OPP)


@router.post("/opportunity/{opp_id}/requirements", response_model=EnqueueResponse)
def enqueue_requirements(
    opp_id: str = Path(...),
    _: None = Depends(require_jobs_key),
) -> EnqueueResponse:
    result = celery_client.send_task(TASK_REQS_OPP, args=[opp_id])
    return EnqueueResponse(task_id=result.id, task_name=TASK_REQS_OPP)


@router.post("/opportunity/{opp_id}/export-compliance", response_model=EnqueueResponse)
def enqueue_export_compliance(
    opp_id: str = Path(...),
    _: None = Depends(require_jobs_key),
) -> EnqueueResponse:
    result = celery_client.send_task(TASK_XLSX_OPP, args=[opp_id])
    return EnqueueResponse(task_id=result.id, task_name=TASK_XLSX_OPP)


@router.post("/opportunity/{opp_id}/run-pipeline", response_model=EnqueueResponse)
def enqueue_run_pipeline(
    opp_id: str = Path(...),
    _: None = Depends(require_jobs_key),
) -> EnqueueResponse:
    result = celery_client.send_task(TASK_RUN_PIPELINE, args=[opp_id])
    return EnqueueResponse(task_id=result.id, task_name=TASK_RUN_PIPELINE)


@router.get("/status/{task_id}")
def get_task_status(task_id: str, _: None = Depends(require_jobs_key)) -> dict:
    """Return the current status of a Celery task."""
    res = celery_client.AsyncResult(task_id)
    return {
        "task_id": task_id,
        "state": res.state,
        "result": res.result if res.successful() else None,
        "error": str(res.result) if res.failed() else None,
    }