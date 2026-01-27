"""Celery tasks for Gov Contract OS."""

# Import task modules to ensure they are registered when the package is imported
from . import attachment_tasks  # noqa: F401
from . import ingest_tasks  # noqa: F401
from . import parse_tasks  # noqa: F401
from . import pipeline_tasks  # noqa: F401
