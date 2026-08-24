# ch4-bookstore

A Django bookstore project with a custom user model, built as part of working through Chapter 4 of a Django tutorial/book. Currently the `accounts` app provides authentication scaffolding (custom user model, forms, admin); bookstore-specific models/views are not yet implemented.

## Stack

- Python / Django 4.0.10
- PostgreSQL 13
- Docker Compose

## Project layout

- `django_project/` — project settings, root URL config
- `accounts/` — custom user app (`CustomUser` model, creation/change forms, admin registration)
- `create_superuser.py` — script run on container startup to ensure a default superuser exists
- `docker-compose.yml` — `web` (app server), `db` (Postgres), `test` (test runner) services

## Setup

### 1. Environment variables

Create a `.env` file in the project root with:

```env
POSTGRES_DB=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_HOST_AUTH_METHOD=trust
```

### 2. Run with Docker Compose

```bash
docker-compose up --build
```

This will:
1. Start the Postgres database
2. Run migrations
3. Create a default superuser (see `create_superuser.py`)
4. Start the dev server at [http://localhost:8000](http://localhost:8000)

Admin site: [http://localhost:8000/admin/](http://localhost:8000/admin/)

### 3. Run tests

```bash
docker-compose run --rm test
```

## Notes

- `AUTH_USER_MODEL` is set to `accounts.CustomUser`.
- The default `SECRET_KEY` and `DEBUG=True` in `django_project/settings.py` are for local development only — replace/override before deploying anywhere public.
- The default superuser credentials in `create_superuser.py` are for local development convenience and should not be used as-is in any shared or production environment.
