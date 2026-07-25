from contextlib import asynccontextmanager
from collections.abc import AsyncIterator

from fastapi import FastAPI

async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    yield