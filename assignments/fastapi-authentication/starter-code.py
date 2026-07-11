"""Starter code for FastAPI Authentication Basics assignment."""

from fastapi import Depends, FastAPI, Header, HTTPException
from pydantic import BaseModel

app = FastAPI(title="FastAPI Authentication Basics")


class LoginRequest(BaseModel):
    username: str
    password: str


class Book(BaseModel):
    id: int
    title: str
    author: str
    year: int


USERS = {
    "alex": {"password": "python123", "full_name": "Alex Kim"},
    "sam": {"password": "fastapi456", "full_name": "Sam Lee"},
}

# For this assignment, tokens are simple strings mapped to usernames.
# Students can replace this with JWT in an extension task.
TOKENS = {
    "token-alex": "alex",
    "token-sam": "sam",
}

books = [
    {"id": 1, "title": "The Pragmatic Programmer", "author": "Andrew Hunt", "year": 1999},
    {"id": 2, "title": "Clean Code", "author": "Robert C. Martin", "year": 2008},
    {"id": 3, "title": "Fluent Python", "author": "Luciano Ramalho", "year": 2015},
]


@app.post("/login")
def login(payload: LoginRequest):
    user = USERS.get(payload.username)
    if not user or user["password"] != payload.password:
        raise HTTPException(status_code=401, detail="Invalid username or password")

    # TODO: Improve token generation strategy (for example, JWT).
    access_token = f"token-{payload.username}"
    return {"access_token": access_token, "token_type": "bearer"}


def get_current_user(authorization: str | None = Header(default=None)):
    if not authorization:
        raise HTTPException(status_code=401, detail="Missing authorization header")

    scheme, _, token = authorization.partition(" ")
    if scheme.lower() != "bearer" or not token:
        raise HTTPException(status_code=401, detail="Invalid authorization format")

    username = TOKENS.get(token)
    if not username:
        raise HTTPException(status_code=401, detail="Invalid token")

    return {"username": username, "full_name": USERS[username]["full_name"]}


@app.get("/books")
def get_books():
    return books


@app.post("/books")
def create_book(book: Book, current_user: dict = Depends(get_current_user)):
    if any(existing["id"] == book.id for existing in books):
        raise HTTPException(status_code=400, detail="Book ID already exists")

    new_book = book.model_dump()
    books.append(new_book)
    return {"created_by": current_user["username"], "book": new_book}


@app.get("/me")
def read_me(current_user: dict = Depends(get_current_user)):
    return current_user
