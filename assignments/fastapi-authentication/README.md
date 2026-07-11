# 📘 Assignment: FastAPI Authentication Basics

## 🎯 Objective

Build authentication into a FastAPI application so protected endpoints are only accessible to signed-in users. You will practice login flow, token handling, and route protection.

## 📝 Tasks

### 🛠️	Create a Login Endpoint

#### Description
Set up a simple in-memory user store and build a login route that verifies username and password. When credentials are valid, return an access token.

#### Requirements
Completed program should:

- Define at least 2 users in an in-memory dictionary.
- Add a `POST /login` endpoint that accepts username and password.
- Return `401` for invalid credentials.
- Return a JSON response with an `access_token` and `token_type` when login succeeds.

### 🛠️	Protect API Routes with a Token

#### Description
Create a dependency that reads a bearer token from the request and validates it. Use that dependency to protect selected routes in the API.

#### Requirements
Completed program should:

- Add a dependency that reads the `Authorization: Bearer <token>` header.
- Return `401` when the token is missing or invalid.
- Add a protected `GET /me` endpoint that returns the current user profile.
- Keep `GET /books` public and make `POST /books` protected.

### 🛠️	Test Authentication Behavior

#### Description
Run the app locally and test login and protected routes through FastAPI docs or curl commands.

#### Requirements
Completed program should:

- Run with `uvicorn starter-code:app --reload`.
- Show successful login and token usage on a protected route.
- Show correct `401` behavior for missing/invalid tokens.
- Include clear comments or TODOs where students must complete logic.
