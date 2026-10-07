# Python Software Engineering Bootcamp — Production-style FastAPI Service

A small but production-structured **REST API** for users and their liked posts. I built it to practise backend and MLOps engineering habits: layered architecture, containerisation, typed code and automated tests.

## Features

- **FastAPI** application factory with separate **routes**, **services**, **schemas** (Pydantic) and **models** (SQLAlchemy).
- CRUD endpoints with **pagination**, partial updates, and centralised **custom exceptions and handlers**.
- **PostgreSQL** with SQLAlchemy models, foreign keys, unique constraints and indexes.
- **Sync vs async HTTP clients** (`requests` vs `aiohttp`) in `sample_requests/`.
- **Tests:** unit tests (services, mocked HTTP via `aioresponses`) and integration tests on the API endpoints, using **pytest** fixtures.
- **Type checking** with **mypy**.

## Run it

```bash
make start_build     # build & start the API + Postgres with docker-compose
make unit_tests      # run pytest inside the test container
make check_typing    # mypy
make stop
```

The API is served on `http://localhost:8080`, with interactive docs at `/docs`.

**Stack:** Python · FastAPI · Pydantic · SQLAlchemy · PostgreSQL · Docker / docker-compose · pytest · mypy · Make
