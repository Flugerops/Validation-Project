from sqlalchemy.orm import Mapped
from ..helpers import Base


class Book(Base):
    __tablename__ = "books"
    title: Mapped[str]
    author: Mapped[str]
    year: Mapped[int]
    genre: Mapped[str]
    isbn: Mapped[str]