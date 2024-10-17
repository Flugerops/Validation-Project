from re import sub
from typing import Optional
from sqlmodel import SQLModel, Field, Session, create_engine
from pydantic import validator, field_validator, model_validator
from ..helpers import Genres
from .. import AsyncDB


class Book(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    author: str
    year: int = Field(..., description = "Date of Publishing")
    genre: str
    isbn: str
    
    @model_validator(mode="before")
    def clear_underscores_and_check_max_length(self):
        self.isbn = sub(r'-', '', self.isbn)
        print(len(self.isbn))
        if len(self.isbn) != 13:
            raise ValueError("ISBN must contain 13 numbers")
        return self

    # @field_validator("isbn")
    # def check_isbn_unique(self):
        

    
    @field_validator("year")
    @classmethod
    def check_year(cls, v: int):
        if v >= 2025:
            raise ValueError("The year of publishing cannot be in the future")
        return v
        

    