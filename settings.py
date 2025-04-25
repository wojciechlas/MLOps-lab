# settings.py
from pydantic_settings import BaseSettings
from pydantic import field_validator


class Settings(BaseSettings):
    ENVIRONMENT: str
    APP_NAME: str

    @field_validator("ENVIRONMENT")
    def validate_environment(cls, value: str):
        if value in ["dev", "test", "prod"]:
            return value
        raise ValueError(
            f"Invalid environment: {value}. Must be one of ['dev', 'test', 'prod']"
        )

    @field_validator("APP_NAME")
    def validate_app_name(cls, value: str):
        if value == "":
            raise ValueError("APP_NAME cannot be empty")
        return value
