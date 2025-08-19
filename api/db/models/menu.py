from sqlmodel import SQLModel, Field
from datetime import datetime, UTC

"""
Creating the models that represent the database tables
"""


# Model for the category table
class Category(SQLModel, table=True):
    __tablename__ = "menu_category"
    id: int | None = Field(default=None, primary_key=True)
    name: str
    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))


# Model for the dish table
class Dish(SQLModel, table=True):
    __tablename__ = "menu_dish"
    id: int = Field(primary_key=True)
    name: str
    description: str
    price: float
    available: bool
    created_at: datetime
    category_id: int
