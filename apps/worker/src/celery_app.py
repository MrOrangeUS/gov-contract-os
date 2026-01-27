from celery import Celery
from .config import settings


celery_app = Celery(
    "gov_contract_os_worker",
    broker=settings.redis_url,
    backend=settings.redis_url,
)

celery_app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="UTC",
    enable_utc=True,
)

# Automatically discover tasks from the src.tasks package
celery_app.autodiscover_tasks(["src.tasks"])
