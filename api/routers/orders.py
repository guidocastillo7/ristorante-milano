from fastapi import APIRouter
from sqlmodel import select
from db.models.order import Order, OrderItem
from db.client import SessionDep
from typing import List

order_router = APIRouter(prefix="/orders",
                         tags=["orders"])

order_item_router = APIRouter(prefix="/order_items",
                              tags=["order_items"])


# Order endpoints
@order_router.get("/", response_model=List[Order])
async def get_orders(
    session: SessionDep,
    offset: int = 0,
    limit: int = 10
):
    orders = session.exec(
        select(Order).offset(offset).limit(limit)
    ).all()

    return orders


# Order item endpoints
@order_item_router.get("/", response_model=List[OrderItem])
async def get_order_items(
    session: SessionDep,
    offset: int = 0,
    limit: int = 10
):
    order_items = session.exec(
        select(OrderItem).offset(offset).limit(limit)
    ).all()

    return order_items
