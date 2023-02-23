from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "dog app"
    DB_USER: str = "dev"
    DB_PASSWORD: str = "secret"
    DB_HOST: str = "localhost"
    DB_PORT: str = "5432"
    DB_NAME: str = "postgres"

    @property
    def DATABASE_URL(self)-> str:
        return f"postgresql://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"


config = Settings()

