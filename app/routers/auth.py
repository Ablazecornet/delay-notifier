from fastapi import APIRouter, Depends
from app.schemas.user import UserCreate, UserCreateResponse, User
from app.schemas.auth import LoginRequest, LoginResponse

router = APIRouter()

@router.post("/auth/signup", response_model=UserCreateResponse)
async def signup(user_body: UserCreate):
    return UserCreateResponse(
        id=1,
        username=user_body.username,
        email=user_body.email,
        password=user_body.password
    )

@router.post("/auth/login", response_model=LoginResponse)
async def login(login_body: LoginRequest):
    return LoginResponse(
        access_token="fake_token",
        token_type="bearer"
    )

@router.post("/auth/logout")
async def logout():
    return {"message": "Logged out (dummy)"}

async def get_current_user():
    return User(
        id=1,
        username="YamadaTaro",
        email="test@example.com",
        password="password123"
    )

@router.get("/auth/me", response_model=User)
async def me(current_user: User = Depends(get_current_user)):
    return current_user