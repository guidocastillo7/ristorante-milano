from fastapi import Depends
from typing import Annotated
from sqlmodel import Session, create_engine
from decouple import config


# Creating the connection to the database
db_url = config("DATABASE_URL")
engine = create_engine(db_url)


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]
