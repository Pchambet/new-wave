"""ClearBorder — Configuration centrale."""
from pydantic import field_validator
from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    """Configuration de l'application."""
    
    app_name: str = "ClearBorder"
    app_version: str = "0.1.0"
    debug: bool = True
    
    database_url: str = "sqlite:///./clearborder.db"
    
    api_secret_key: str = "dev-secret-change-in-production"
    api_prefix: str = "/api/v1"
    api_keys: list[str] = []  # Vide = pas d'auth (dev). En prod: API_KEYS="key1,key2"

    @field_validator("api_keys", mode="before")
    @classmethod
    def parse_api_keys(cls, v):
        if v is None or v == []:
            return []
        if isinstance(v, str):
            return [k.strip() for k in v.split(",") if k.strip()]
        return v

    # CBAM
    cbam_sectors: list[str] = [
        "iron_steel", "aluminium", "cement", "fertilisers", 
        "hydrogen", "electricity"
    ]
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "ignore"


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
