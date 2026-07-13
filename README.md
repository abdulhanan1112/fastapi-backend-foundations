# FastAPI Backend Foundations

A hands-on backend development learning repository built with **Python** and **FastAPI**.

This repository documents my journey from backend fundamentals to building production-style REST APIs using clean architecture, PostgreSQL, authentication, automated testing, Docker, and deployment.

## Learning Goals

By completing this repository, I aim to understand and practice:

- Client-server architecture
- HTTP requests and responses
- REST API design
- HTTP methods and status codes
- FastAPI fundamentals
- Pydantic validation
- Clean architecture
- PostgreSQL and SQL
- SQLAlchemy ORM
- Alembic migrations
- Authentication and authorization
- JWT access tokens
- Automated testing with pytest
- Docker and Docker Compose
- API deployment
- Flutter integration with FastAPI

## Learning Schedule

The learning phase runs from **13 July 2026 to 31 July 2026**.

I am following a project-first approach:

1. Learn the concept.
2. Build a small implementation.
3. Test successful and failed requests.
4. Refactor the code.
5. Document the lesson.
6. Push the progress to GitHub.

## Current Progress

### Day 1 — HTTP, REST, Status Codes, and Clean Architecture

Topics covered:

- Client and server communication
- HTTP request and response structure
- HTTP methods
- REST resources and endpoints
- Path and query parameters
- Common HTTP status codes
- Clean architecture layers
- Separation of responsibilities
- Repository pattern
- Dependency direction

Planned implementation:

- `GET /`
- `GET /health`
- One path-parameter endpoint
- One query-parameter endpoint
- Swagger UI testing
- Postman testing

## Planned Project Structure

```text
app/
├── api/
│   ├── routes/
│   └── dependencies/
├── core/
│   ├── config/
│   └── logging/
├── domain/
│   ├── entities/
│   └── exceptions/
├── use_cases/
├── repositories/
├── infrastructure/
│   ├── database/
│   ├── security/
│   └── email/
├── schemas/
└── main.py

tests/
requirements.txt
README.md
.env.example
.gitignore
```

The project will begin with a simple structure and gradually move toward a cleaner architecture as more backend concepts are introduced.

## Technologies

- Python
- FastAPI
- Uvicorn
- Pydantic
- PostgreSQL
- SQLAlchemy
- Alembic
- pytest
- Docker
- Postman
- Git and GitHub

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/abdulhanan1112/fastapi-backend-foundations.git
cd fastapi-backend-foundations
```

### 2. Create a virtual environment

On Fedora or Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install fastapi uvicorn
```

Later, when a requirements file is added:

```bash
pip install -r requirements.txt
```

### 4. Run the FastAPI application

```bash
uvicorn app.main:app --reload
```

### 5. Open the API documentation

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

ReDoc:

```text
http://127.0.0.1:8000/redoc
```

## API Design Principles

This repository follows these rules:

- Use nouns for resource URLs.
- Use HTTP methods to describe actions.
- Return appropriate HTTP status codes.
- Keep API routes small.
- Separate business logic from database logic.
- Validate all incoming data.
- Protect private resources with authentication.
- Test successful and unsuccessful cases.
- Never expose secrets or internal errors to clients.

Example REST endpoints:

```text
GET     /tasks
GET     /tasks/{task_id}
POST    /tasks
PATCH   /tasks/{task_id}
DELETE  /tasks/{task_id}
```

## Status Code Guide

| Status Code | Meaning |
|---|---|
| `200 OK` | Request completed successfully |
| `201 Created` | A new resource was created |
| `204 No Content` | Request succeeded with no response body |
| `400 Bad Request` | General invalid request |
| `401 Unauthorized` | Authentication is missing or invalid |
| `403 Forbidden` | User is authenticated but not allowed |
| `404 Not Found` | Requested resource does not exist |
| `409 Conflict` | Request conflicts with existing data |
| `422 Unprocessable Content` | Request validation failed |
| `500 Internal Server Error` | Unexpected backend error |

## Future Projects

After completing the learning phase, I will build:

1. **StudyFlow Pro Backend API**
   - Authentication
   - Subjects
   - Tasks
   - Notes
   - Reminders
   - Analytics
   - Flutter integration

2. **Service Booking API**
   - Multiple user roles
   - Staff and services
   - Appointment availability
   - Bookings
   - Invoices
   - Notifications
   - Business analytics

## Author

**Abdul Hanan**

- GitHub: [abdulhanan1112](https://github.com/abdulhanan1112)
- Software Engineering student
- Flutter developer learning production backend development

## License

This repository is created for learning, practice, and portfolio development.
