from sqlmodel import SQLModel, Field
from datetime import datetime


# Model for the order table
class Order(SQLModel, table=True):
    __tablename__ = "orders_order"
    id: int = Field(primary_key=True)
    taken_by_id: int
    table_number: str
    created_at: datetime


# Model for the order item table
class OrderItem(SQLModel, table=True):
    __tablename__ = "orders_orderitem"
    id: int = Field(primary_key=True)
    dish_id: int
    quantity: int
    order_id: int
