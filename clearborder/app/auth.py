"""Authentification API - API Keys (optionnel en dev)."""
from fastapi import HTTPException, Security, status
from fastapi.security import APIKeyHeader

from .config import settings

API_KEY_HEADER = APIKeyHeader(name="X-API-Key", auto_error=False)


def get_api_key(api_key: str = Security(API_KEY_HEADER)) -> str | None:
    """Vérifie la clé API. En dev (api_keys vide), accepte tout."""
    if not settings.api_keys:
        return None  # Pas d'auth en dev
    if not api_key:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Clé API manquante (header X-API-Key)",
        )
    if api_key not in settings.api_keys:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Clé API invalide",
        )
    return api_key
