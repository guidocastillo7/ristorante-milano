from sqlmodel import SQLModel, Field


class UserBase(SQLModel):
    username: str
    first_name: str
    last_name: str
    email: str


class UserRead(UserBase):
    id: int


class UserCreate(UserBase):
    password: str


class UserUpdate(UserBase):
    username: str | None = None
    first_name: str | None = None
    last_name: str | None = None
    email: str | None = None
    password: str | None = None
