from typing import Annotated

from fastapi import APIRouter
from pydantic import BaseModel, Field

router = APIRouter()


class StatisticsRequest(BaseModel):
    values: Annotated[
        list[float],
        Field(min_length=1, max_length=10_000),
    ]


class StatisticsResponse(BaseModel):
    average: float
    minimum: float
    maximum: float


@router.post("/coderabbit-statistics")
async def calculate_statistics(
    request: StatisticsRequest,
) -> StatisticsResponse:
    average = sum(request.values) / len(request.values)

    return StatisticsResponse(
        average=average,
        minimum=min(request.values),
        maximum=max(request.values),
    )