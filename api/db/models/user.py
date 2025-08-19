from sqlmodel import SQLModel, Field


# Model for the user table
class User(SQLModel, table=True):
    __tablename__ = "auth_user"
    id: int = Field(primary_key=True)
    username: str
    first_name: str
    last_name: str
    email: str
    password: str
