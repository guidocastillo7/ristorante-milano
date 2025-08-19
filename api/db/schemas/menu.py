from sqlmodel import SQLModel


class CategoryBase(SQLModel):
    name: str


class CategoryRead(CategoryBase):
    id: int


class CategoryCreate(CategoryBase):
    pass


class CategoryUpdate(CategoryBase):
    name: str | None = None
