from typing import Any, Generic, TypeVar
from pydantic import BaseModel

T = TypeVar("T")


class SuccessResponse(BaseModel, Generic[T]):
    success: bool = True
    message: str
    data: T | None = None


class ErrorDetail(BaseModel):
    code: str


class ErrorResponse(BaseModel):
    success: bool = False
    message: str
    error: ErrorDetail