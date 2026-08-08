from typing import Literal
from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict
)

class Settings(BaseSettings):
    app_name : str = "FASTAPI BACKEND FOUNDATIONS"
    app_version :str = '1.0.0'
    debug:bool =False

    log_level : Literal[
        "DEBUG",
        "INFO",
        "ERROR",
        "WARNINGS",
        "CRITICAL"
    ] = "INFO"

    model_config=SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )


settings = Settings()