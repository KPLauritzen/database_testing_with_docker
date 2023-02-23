from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL

from docker_test.config import config


def get_engine():
    return create_engine(
        URL.create(
            drivername="postgresql+psycopg2",
            username=config.DB_USER,
            password=config.DB_PASSWORD,
            host=config.DB_HOST,
            port=config.DB_PORT,
            database=config.DB_NAME,
        )
    )


def get_alemic_dir():
    from pathlib import Path

    return Path(__file__).parent.parent / "alembic"
