from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Application settings loaded from environment variables.
    """

    app_name: str = Field(default="DevPilot AI")
    app_version: str = Field(default="0.1.0")
    debug: bool = Field(default=True)

    database_url: str = Field(default="sqlite:///data/devpilot.db")

    embedding_model: str = Field(default="all-MiniLM-L6-v2")

    openai_api_key: str = Field(default="")
    github_token: str = Field(default="")

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    """
    Return a cached Settings instance.
    """
    return Settings()


settings = get_settings()