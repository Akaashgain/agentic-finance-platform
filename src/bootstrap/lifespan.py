import logging
from contextlib import asynccontextmanager
from fastapi import FastAPI

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting Agentic Finance Platform...")
    logger.info("Dependency Injection Container initialized.")

    yield

    logger.info("Stopping Agentic Finance Platform...")