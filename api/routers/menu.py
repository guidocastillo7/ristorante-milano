from fastapi import APIRouter, HTTPException
from sqlmodel import select
from db.models.menu import Category, Dish
from db.schemas.menu import CategoryRead, CategoryCreate
from db.client import SessionDep
from typing import List

category_router = APIRouter(prefix="/categories",
                              tags=["categories"])

dish_router = APIRouter(prefix="/dishes",
                          tags=["dishes"])


# Category endpoints
@category_router.get("/", response_model=List[CategoryRead])
async def get_categories(
    session: SessionDep,
    offset: int = 0,
    limit: int = 10
):
    categories = session.exec(
        select(Category).offset(offset).limit(limit)
    ).all()

    return categories


@category_router.get("/{category_id}", response_model=CategoryRead)
async def get_category(
    category_id: int,
    session: SessionDep
):
    category = session.get(Category, category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")

    return category


@category_router.post("/", response_model=CategoryRead)
async def create_category(
    category: CategoryCreate,
    session: SessionDep
):
    db_category = Category.model_validate(category)
    session.add(db_category)
    session.commit()
    session.refresh(db_category)

    return db_category


@category_router.delete("/{category_id}")
async def delete_category(
    category_id: int,
    session: SessionDep
):
    category = session.get(Category, category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    session.delete(category)
    session.commit()

    return {"message": f"Category '{category.name}' deleted succesfully"}


# Dish endpoints
@dish_router.get("/", response_model=List[Dish])
async def get_dishes(
    session: SessionDep,
    offset: int = 0,
    limit : int = 10
):
    dishes = session.exec(
        select(Dish).offset(offset).limit(limit)
    ).all()

    return dishes
