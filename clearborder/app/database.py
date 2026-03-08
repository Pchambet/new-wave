"""Configuration base de données — SQLite (dev) ou PostgreSQL (prod)."""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.config import settings

_is_sqlite = "sqlite" in settings.database_url

_engine_kwargs = {
    "connect_args": {"check_same_thread": False} if _is_sqlite else {},
    "pool_pre_ping": not _is_sqlite,
    "echo": settings.debug,
}
if not _is_sqlite:
    _engine_kwargs.update(pool_size=10, max_overflow=20, pool_recycle=3600)

engine = create_engine(settings.database_url, **_engine_kwargs)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    """Dependency FastAPI pour obtenir une session DB."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def init_db():
    """Crée toutes les tables."""
    from app import models  # noqa: F401 - load models for metadata
    Base.metadata.create_all(bind=engine)
