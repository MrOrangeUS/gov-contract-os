"""Celery producer client used to enqueue background tasks."""

from celery import Celery

from .config import settings


# Create a Celery client using the Redis broker
celery_client = Celery(
    "gov_contract_os_api_producer",
    broker=settings.redis_url,
    backend=settings.redis_url,
)

celery_client.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="UTC",
    enable_utc=True,
)
