from sqlmodel import SQLModel, Field
from datetime import datetime, UTC


# Model for the user table
class User(SQLModel, table=True):
    __tablename__ = "auth_user"
    id: int | None = Field(default=None, primary_key=True)
    username: str
    first_name: str
    last_name: str
    email: str
    password: str
    is_superuser: bool = Field(default=False)
    is_staff: bool = Field(default=False)
    is_active: bool = Field(default=True)
    date_joined: datetime = Field(default_factory=lambda: datetime.now(UTC))
