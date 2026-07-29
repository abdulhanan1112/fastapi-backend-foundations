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
