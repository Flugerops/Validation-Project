from sqlmodel import Session, select
from fastapi import Depends
from .. import app
from ..db import AsyncDB, Book


@app.get("/")
def index():
    return {"Hello": "World!"}

@app.post("/create_book",response_model=Book, status_code=201)
def create_book(data: Book, session: Session = Depends(AsyncDB.get_session)):
        book = Book(**data.model_dump())
        session.add(book)
        return book
