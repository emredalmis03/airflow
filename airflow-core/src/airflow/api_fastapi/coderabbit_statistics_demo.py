from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()


class StatisticsRequest(BaseModel):
    values: list[float] = []


class StatisticsResponse(BaseModel):
    average: float
    minimum: float
    maximum: float


@router.post("/coderabbit-statistics")
async def calculate_statistics(
    request: StatisticsRequest,
) -> StatisticsResponse:
    average = sum(request.values) / len(request.values)

    if not average:
        raise HTTPException(
            status_code=500,
            detail="Average could not be calculated",
        )

    return StatisticsResponse(
        average=average,
        minimum=min(request.values),
        maximum=max(request.values),
    )