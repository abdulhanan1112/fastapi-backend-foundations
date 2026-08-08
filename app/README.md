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

# Day 2 — Routing and Request Inputs

Day 2 focuses on receiving, validating, and processing different types of input in FastAPI.

The project implements a temporary in-memory Student API using:

- Path parameters
- Query parameters
- Request bodies
- Python type annotations
- Pydantic models
- Enums
- FastAPI validation
- Filtering
- Route ordering

No database is used yet. Student data is stored temporarily in a Python list and is deleted whenever the server restarts.

---

## Concepts Practised

### Path Parameters

Path parameters identify a specific resource.

Example:

```text
GET /students/1

# Day 3 — Pydantic Models, Response Schemas and API Errors

## Overview

This project is part of my FastAPI backend engineering roadmap.

Day 3 focuses on creating clear API contracts for incoming and outgoing data using Pydantic models.

The Student API now supports:

- Pydantic request models
- Separate response models
- Nested schemas
- Field constraints
- Request validation
- Response filtering
- Serialization
- Correct HTTP status codes
- API errors using `HTTPException`

The project still uses temporary in-memory storage. PostgreSQL will be introduced later.

---

## Learning Objectives

By completing Day 3, I learned how to:

- Define structured request bodies using Pydantic
- Separate input schemas from output schemas
- Validate fields using `Field`
- Create nested models
- Convert Pydantic objects using `model_dump()`
- Control API output using `response_model`
- Serialize Python data into JSON responses
- Use appropriate HTTP status codes
- Raise proper API errors using `HTTPException`
- Separate structural validation from business validation

---

# Request and Response Flow

```text
Client sends JSON
        ↓
Pydantic validates the request body
        ↓
FastAPI creates a Python model object
        ↓
Endpoint business logic executes
        ↓
Endpoint returns Python data
        ↓
response_model validates and filters the response
        ↓
FastAPI serializes the data
        ↓
Client receives JSON


# Day 4 — CRUD and Project Structure

Day 4 focuses on completing CRUD operations and separating the Student API into clean layers.

The project still uses temporary in-memory storage, so data disappears when the server restarts.

## Topics Covered

- CRUD operations
- `APIRouter`
- Router inclusion
- Repository pattern
- Service layer
- Dependency injection
- Custom exceptions
- `PUT` updates
- `DELETE` operations
- Clean project structure

---

## CRUD Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| `POST` | `/students` | Create a student |
| `GET` | `/students` | List students |
| `GET` | `/students/search` | Search by name |
| `GET` | `/students/{student_id}` | Get one student |
| `PUT` | `/students/{student_id}` | Update a student |
| `DELETE` | `/students/{student_id}` | Delete a student |

---

## Architecture

```text
Client
  ↓
Router
  ↓
Service
  ↓
Repository
  ↓
In-memory students list
```

### Router

Handles:

- URLs and HTTP methods
- Request validation
- Response models
- Status codes
- Converting custom exceptions into `HTTPException`

### Service

Handles:

- Business logic
- Duplicate email checks
- Missing student checks
- Converting Pydantic models using `model_dump()`

### Repository

Handles:

- The students list
- Creating IDs
- Creating, reading, searching, updating and deleting students

---

## Project Structure

```text
app/
├── main.py
├── api/
│   └── routers/
│       └── students.py
├── core/
│   └── exceptions.py
├── dependencies/
│   └── students.py
├── repositories/
│   └── student_repository.py
├── services/
│   └── student_service.py
└── schemas/
    └── student.py
```

---

## Repository Storage

The temporary students list belongs inside the repository:

```python
class InMemoryStudentRepository:
    def __init__(self) -> None:
        self._students: list[dict[str, object]] = []
        self._next_id: int = 1
```

The repository implements:

```text
create
list_all
get_by_id
get_by_email
search_by_name
update
delete
```

A separate `_next_id` counter prevents duplicate IDs after deletion.

---

## Input and Output Flow

```text
Client JSON
    ↓
Router: StudentCreate or StudentUpdate
    ↓
Service: Pydantic model
    ↓ model_dump()
Repository: dictionary
```

Output:

```text
Repository: dictionary
    ↓
Service: dictionary
    ↓
Router response_model
    ↓
Client JSON
```

---

## Dependency Injection

One shared repository and service are created:

```python
student_repository = InMemoryStudentRepository()
student_service = StudentService(student_repository)


def get_student_service() -> StudentService:
    return student_service
```

The router receives the service using `Depends`.

---

## Error Handling

The service raises custom exceptions:

```text
StudentNotFoundError
DuplicateStudentEmailError
```

The router converts them into HTTP responses:

| Error | Status |
|---|---:|
| Student not found | `404 Not Found` |
| Duplicate email | `409 Conflict` |
| Invalid request data | `422 Unprocessable Content` |

---

## Status Codes

| Operation | Status |
|---|---:|
| Create student | `201 Created` |
| Read student | `200 OK` |
| Update student | `200 OK` |
| Delete student | `204 No Content` |

---

## Lessons Learned

- Routers handle HTTP concerns.
- Services handle business rules.
- Repositories handle data access.
- Schemas define API contracts.
- Dependencies provide shared services.
- Custom exceptions keep business logic separate from FastAPI.
- `PUT` replaces the complete student data while preserving the ID.
- A successful `DELETE` returns `204 No Content`.

---
# Day 5 — Backend Python Skills

Day 5 focuses on Python concepts that are important for building maintainable FastAPI applications.

## Topics Covered

- Type hints
- Dataclasses vs Pydantic models
- Custom exceptions
- Context managers
- Environment variables
- Application settings
- Logging
- `async` and `await`
- Blocking vs non-blocking operations

---

## Application Settings

Application configuration is moved outside the source code using `.env`.

Example:

```env
APP_NAME=FastAPI Backend Foundations
APP_VERSION=1.0.0
DEBUG=true
LOG_LEVEL=INFO
```

Settings are loaded using `pydantic-settings`.

```text
.env
  ↓
Settings
  ↓
FastAPI application
```

`.env` is ignored by Git, while `.env.example` provides safe example configuration.

---

## Logging

A reusable logging configuration was added.

Each module creates its logger using:

```python
logger = logging.getLogger(__name__)
```

Logging levels used:

| Level | Purpose |
|---|---|
| `DEBUG` | Detailed development information |
| `INFO` | Successful important operations |
| `WARNING` | Expected but unusual situations |
| `ERROR` | Failed technical operations |

Examples:

```text
student_created student_id=1
student_updated student_id=1
student_deleted student_id=1
student_not_found student_id=10
```

---

## Timing Context Manager

A reusable context manager was created to measure execution time.

```python
with measure_time("operation_name"):
    ...
```

Flow:

```text
Start timer
    ↓
Execute operation
    ↓
Calculate elapsed time
    ↓
Write timing log
```

The `finally` block ensures that execution time is recorded even when an exception occurs.

---

## Async and Blocking Operations

Three experiment endpoints were created:

```text
GET /experiments/non-blocking
GET /experiments/blocked-event-loop
GET /experiments/threadpool-wait
```

### Non-blocking

```python
async def
```

with:

```python
await asyncio.sleep()
```

allows the event loop to work on other requests while waiting.

### Blocking inside async

```python
async def
```

with:

```python
time.sleep()
```

blocks the event loop and delays other requests.

### Synchronous route

```python
def
```

with a blocking operation is handled by FastAPI using a thread pool.

---

## Key Async Lesson

```text
async def + await non-blocking operation
→ good for asynchronous I/O

async def + blocking operation
→ blocks the event loop

def + blocking operation
→ FastAPI can run it in a thread pool
```

`async` should not be added to every function automatically.

The function style should match the operation or library being used.

---

## Updated Structure

```text
app/
├── api/
│   └── routers/
│       ├── students.py
│       └── experiments.py
│
├── core/
│   ├── config.py
│   ├── exceptions.py
│   ├── logging.py
│   └── timing.py
│
├── repositories/
├── services/
├── schemas/
├── dependencies/
└── main.py

.env
.env.example
```

---

## Lessons Learned

- Type hints make function contracts clearer.
- Pydantic is useful for validating external API data.
- Dataclasses can represent trusted internal data.
- Environment variables separate configuration from code.
- `.env` should not be committed to Git.
- Logging is better than using `print()` for backend applications.
- Context managers handle setup and cleanup reliably.
- `async` is mainly useful for non-blocking I/O.
- Blocking code inside `async def` can block the event loop.
- FastAPI can execute synchronous route functions in a thread pool.

---



