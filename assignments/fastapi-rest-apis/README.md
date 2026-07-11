# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a REST API using FastAPI and practice core backend concepts such as routing, request validation, and HTTP status codes.

## 📝 Tasks

### 🛠️	Create API Endpoints

#### Description
Set up a FastAPI app and implement endpoints to manage a small collection of books. You will create routes for listing books, retrieving one book, and adding a new book.

#### Requirements
Completed program should:

- Define a FastAPI app in `starter-code.py`.
- Add a `GET /books` endpoint that returns a list of all books.
- Add a `GET /books/{book_id}` endpoint that returns one book by ID.
- Add a `POST /books` endpoint that adds a new book and returns the created book.
- Return `404` when a requested book ID does not exist.

### 🛠️	Validate Data with Pydantic

#### Description
Use a Pydantic model to validate incoming data for new books. Ensure required fields are present and types are correct.

#### Requirements
Completed program should:

- Create a `Book` Pydantic model with `id`, `title`, `author`, and `year` fields.
- Require `id` and `year` to be integers.
- Require `title` and `author` to be non-empty strings.
- Use the model in the `POST /books` endpoint request body.
- Return a proper error response when invalid data is sent.

### 🛠️	Test and Run the API

#### Description
Run the application locally with Uvicorn and test all endpoints with the interactive API docs.

#### Requirements
Completed program should:

- Run with `uvicorn starter-code:app --reload`.
- Successfully handle `GET`, `POST`, and invalid route/data cases.
- Include at least 3 sample books in the in-memory data store for testing.
- Be testable through `/docs` in the browser.
