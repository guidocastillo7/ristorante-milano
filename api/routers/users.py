from fastapi import APIRouter
from sqlmodel import select
from db.models.user import User
from db.schemas.user import UserRead
from db.client import SessionDep
from typing import List

user_router = APIRouter(prefix="/users",
                        tags=["users"])


@user_router.get("/", response_model=List[UserRead])
async def get_users(
    session: SessionDep,
    offset: int = 0,
    limit: int = 10
):
    users = session.exec(
        select(User).offset(offset).limit(limit)
    ).all()

    return users
