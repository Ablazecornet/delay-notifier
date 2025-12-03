from fastapi import APIRouter
from typing import Optional

router = APIRouter()

@router.get("/v1/delays/")
async def get_delays(line_id: int, date: Optional[str] = None):
    pass

@router.post("/v1/delays/refresh")
async def refresh_delays():
    pass