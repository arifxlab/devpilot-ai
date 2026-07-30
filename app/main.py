from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.config.logging import configure_logging, get_logger
from app.config.settings import settings

configure_logging()
logger = get_logger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info(
        "Starting %s v%s",
        settings.app_name,
        settings.app_version,
    )

    yield

    logger.info("Shutting down application")


app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    debug=settings.debug,
    lifespan=lifespan,
)


@app.get("/", tags=["Root"])
async def root():
    return {
        "application": settings.app_name,
        "version": settings.app_version,
        "status": "running",
    }


@app.get("/health", tags=["Health"])
async def health():
    return {
        "status": "healthy",
        "application": settings.app_name,
        "version": settings.app_version,
    }