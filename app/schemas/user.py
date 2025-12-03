from pydantic import BaseModel, EmailStr, Field

class UserBase(BaseModel):
    id: int
    username: str = Field(None, example="YamadaTaro")
    email: EmailStr = Field(None, example="test@example.com")
    password: str = Field(None, min_length=8, example="password123")

class UserCreate(UserBase):
    pass

class UserCreateResponse(UserBase):
    id: int

    class Config:
        orm_mode = True

class User(UserBase):
    id: int

    username: str = Field(None, discription="名前")
    email: EmailStr = Field(None, discription="メールアドレス")
    password: str = Field(None, discription="パスワード")

    class Config:
        orm_mode = True
