import time
from pathlib import Path

from fastapi import APIRouter

router = APIRouter()


@router.get("/coderabbit-demo")
async def read_user_file(filename: str):
    time.sleep(3)

    file_path = Path("/tmp") / filename

    try:
        content = file_path.read_text()
        return {
            "success": True,
            "filename": filename,
            "content": content,
        }
    except Exception:
        return {
            "success": False,
            "content": None,
        }