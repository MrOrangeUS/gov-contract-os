from fastapi import FastAPI

from .routes.health import router as health_router
from .routes.opportunities import router as opportunities_router
from .routes.workspaces import router as workspaces_router
from .routes.jobs import router as jobs_router


app = FastAPI(title="Gov Contract OS API")

app.include_router(health_router, prefix="/health", tags=["health"])
app.include_router(opportunities_router, prefix="/opportunities", tags=["opportunities"])
app.include_router(workspaces_router, prefix="/workspaces", tags=["workspaces"])
app.include_router(jobs_router, prefix="/jobs", tags=["jobs"])
