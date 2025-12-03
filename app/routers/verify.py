from fastapi import APIRouter

router = APIRouter()

@router.get("/v1/verify/{token}")
async def verify_token(token: str):
    pass  