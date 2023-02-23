import pytest
import docker
import os
import time
from sqlalchemy.orm import sessionmaker


@pytest.fixture(scope="session")
def empty_db():
    from docker_test.config import config

    client = docker.from_env()
    container = client.containers.run(
        "postgres:14",
        environment={
            "POSTGRES_USER": config.DB_USER,
            "POSTGRES_PASSWORD": config.DB_PASSWORD,
            "POSTGRES_DB": config.DB_NAME,
        },
        ports={5432: config.DB_PORT},
        detach=True,
        auto_remove=True,
    )
    # allow up to 10 seconds for the container to start
    for _ in range(10):
        is_ready, _ = container.exec_run("pg_isready")
        if is_ready == 0:
            break
        time.sleep(1)

    # Apply migrations
    os.system("alembic upgrade head")

    yield

    container.stop()


@pytest.fixture(scope="session")
def filled_db(empty_db, db_session):
    from docker_test.schema import Dog

    fake_dogs = [
        Dog(name="Fido", age=3),
    ]
    with db_session() as session:
        session.add_all(fake_dogs)
        session.commit()
    yield


@pytest.fixture(scope="session")
def db_session():
    from docker_test.db import get_engine

    engine = get_engine()
    session = sessionmaker(bind=engine)
    return session
