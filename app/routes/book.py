from sqlmodel import Session, select
from fastapi import Depends
from .. import app
from ..db import AsyncDB, Book
from ..db.schemas import BookBase

@app.get("/")
def index():
    return {"Hello": "World!"}

@app.post("/create_book", status_code=201)
def create_book(data: BookBase):
    with AsyncDB.SESSION.begin() as session:
        book = Book(**data.model_dump())
        session.add(book)
        return book
