from fastapi import APIRouter

router = APIRouter(prefix="/health", tags=["Health"])


@router.get("")
async def health():
    return {
        "status": "healthy",
        "service": "Agentic Finance Platform",
    }


@router.get("/readiness")
async def readiness():
    return {
        "status": "ready",
    }


@router.get("/liveness")
async def liveness():
    return {
        "status": "alive",
    }