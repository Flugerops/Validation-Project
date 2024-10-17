from typing import Optional
from re import sub
from pydantic import BaseModel, Field, model_validator, field_validator


class BookBase(BaseModel):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    author: str
    year: int = Field(..., description = "Date of Publishing")
    genre: str
    isbn: str
    
    @field_validator("isbn")
    def clear_underscores_and_check_max_length(cls, v):
        v = sub(r'-', '', v)
        print(len(v))
        if len(v) != 13:
            raise ValueError("ISBN must contain 13 numbers")
        return v
    
    @field_validator("year")
    @classmethod
    def check_year(cls, v: int):
        if v >= 2025:
            raise ValueError("The year of publishing cannot be in the future")
        return v