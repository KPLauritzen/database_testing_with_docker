# Exploration of database testing with Docker

This repository contains a simple example of how to test a database with Docker.

## Quickstart

Install the project with `poetry`:

```
poetry install
```

Run the tests:

```
poetry run pytest
```

## What is this?

In `docker_test/` I'm defining a database schema. I'm using `alembic` to generate migration files
from that.

I want to run some test against a database with that schema. I'm using `pytest` to run the tests.
The issue I'm trying to solve is how to easily spin a replaceable database with the schema I want to
test against.

This is solved in `tests/conftest.py`. There I'm define some fixtures, including a `filled_db`
fixture. It will, if requested, spin up a docker container with a postgres image, apply all
migrations and insert some fake data into the database.

In `tests/test_database.py` I'm using the `filled_db` fixture to test that the database contains the
data I expect it to contain.
