from fastapi import APIRouter

router = APIRouter()

@router.post("/v1/auth/signup")
async def signup():
    pass

@router.post("/v1/auth/login")
async def login():
    pass

@router.get("v1/auth/me")
async def me():
    pass