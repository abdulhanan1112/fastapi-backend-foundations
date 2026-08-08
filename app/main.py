from fastapi import FastAPI, status
from app.api.routers.students import router as student_router
from app.api.routers.experiments import router as experiment_router
from app.core.config import settings
from app.core.logging import configure_logging

configure_logging(settings.log_level)

app=FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    debug=settings.debug
)

app.include_router(
    student_router,
)

app.include_router(
    experiment_router,
)