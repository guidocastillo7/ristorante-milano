"""
Hasta aqui todo me va funcionando, puedo leer los datos de la bbdd
Ahora tengo que estructurar bien el proyecto por carpetas
Crear los modelos para mapear cada tabla e ir creando los routers
"""

from typing import Annotated, List # Quiero ver la explicacion para que sirven estas librerias

from fastapi import Depends, FastAPI
from routers import menu


app = FastAPI()


# Routers
app.include_router(menu.category_router)
app.include_router(menu.dish_router)


@app.get("/")
async def root():
    return {"mensaje": "Prueba exitosa"}
