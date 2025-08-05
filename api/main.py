"""
Quede creando el router para orders, ahora tengo que organizar:
la seguridad con la autenticacion
los schemas (ver video explicativo)
"""

from typing import Annotated, List # Quiero ver la explicacion para que sirven estas librerias

from fastapi import Depends, FastAPI
from routers import menu, users, orders


app = FastAPI()


# Routers
app.include_router(menu.category_router)
app.include_router(menu.dish_router)
app.include_router(users.user_router)
app.include_router(orders.order_router)
app.include_router(orders.order_item_router)


@app.get("/")
async def root():
    return {"mensaje": "Prueba exitosa"}
