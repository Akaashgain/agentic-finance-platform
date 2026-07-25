import logging
import time
import uuid
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

logger = logging.getLogger(__name__)


def register_middlewares(app: FastAPI) -> None:

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # Change when frontend is added
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @app.middleware("http")
    async def logging_middleware(
        request: Request,
        call_next,
    ):
        request.state.request_id = str(uuid.uuid4())

        start = time.perf_counter()

        response = await call_next(request)

        elapsed = (time.perf_counter() - start) * 1000

        logger.info(
            "[%s] %s %s %.2f ms",
            request.state.request_id,
            request.method,
            request.url.path,
            elapsed,
        )

        response.headers["X-Request-ID"] = request.state.request_id

        return response