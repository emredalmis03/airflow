from pathlib import Path

import anyio
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

BASE_DIRECTORY = Path("/tmp").resolve()


class FileResponse(BaseModel):
    filename: str
    content: str


@router.get("/coderabbit-demo", response_model=FileResponse)
async def read_user_file(filename: str) -> FileResponse:
    requested_path = (BASE_DIRECTORY / filename).resolve()

    if BASE_DIRECTORY not in requested_path.parents:
        raise HTTPException(status_code=400, detail="Invalid filename")

    if not requested_path.is_file():
        raise HTTPException(status_code=404, detail="File not found")

    content = await anyio.to_thread.run_sync(requested_path.read_text)

    return FileResponse(
        filename=filename,
        content=content,
    )