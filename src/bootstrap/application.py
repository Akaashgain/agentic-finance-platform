from fastapi import FastAPI

from src.shared.config.settings import get_settings


def create_application() -> FastAPI:
    settings = get_settings()

    app = FastAPI(
        title=settings.APP_NAME,
        version=settings.APP_VERSION,
    )

    return app