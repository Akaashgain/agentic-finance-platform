from fastapi import FastAPI
from src.bootstrap.lifespan import lifespan
from src.bootstrap.router import register_routes
from src.core.config import get_settings
from src.core.logging import setup_logging


def create_application() -> FastAPI:
    settings = get_settings()

    setup_logging(settings.LOG_LEVEL)

    app = FastAPI(
        title=settings.APP_NAME,
        version=settings.APP_VERSION,
        description="Enterprise Agentic Financial Intelligence Platform",
        lifespan=lifespan,
    )

    register_routes(app)

    return app