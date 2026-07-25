import logging
import time

from fastapi import FastAPI, Request

logger = logging.getLogger(__name__)


def register_middlewares(app: FastAPI):

    @app.middleware("http")
    async def log_requests(request: Request, call_next):

        start = time.perf_counter()

        response = await call_next(request)

        elapsed = (time.perf_counter() - start) * 1000

        logger.info(
            "%s %s %.2f ms",
            request.method,
            request.url.path,
            elapsed,
        )
    from fastapi.middleware.cors import CORSMiddleware

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    return response