"""Starter code for Building REST APIs with FastAPI assignment."""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="Book API")


class Book(BaseModel):
    id: int
    title: str = Field(min_length=1)
    author: str = Field(min_length=1)
    year: int


books = [
    {"id": 1, "title": "The Pragmatic Programmer", "author": "Andrew Hunt", "year": 1999},
    {"id": 2, "title": "Clean Code", "author": "Robert C. Martin", "year": 2008},
    {"id": 3, "title": "Fluent Python", "author": "Luciano Ramalho", "year": 2015},
]


@app.get("/books")
def get_books():
    return books


@app.get("/books/{book_id}")
def get_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")


@app.post("/books")
def create_book(book: Book):
    if any(existing["id"] == book.id for existing in books):
        raise HTTPException(status_code=400, detail="Book ID already exists")

    new_book = book.model_dump()
    books.append(new_book)
    return new_book
