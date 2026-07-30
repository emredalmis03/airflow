from airflow.api_fastapi.coderabbit_statistics_demo import (
    StatisticsRequest,
    calculate_statistics,
)


async def test_calculate_statistics():
    request = StatisticsRequest(values=[1, 2, 3])

    result = await calculate_statistics(request)

    assert result.average == 3
    assert result.minimum == 1
    assert result.maximum == 3