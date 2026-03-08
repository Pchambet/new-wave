"""
ClearBorder API - Moteur CBAM & Landed Cost
"""
from contextlib import asynccontextmanager

from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from .database import engine, SessionLocal, init_db
from . import routes


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Init DB on startup."""
    init_db()
    yield
    # cleanup if needed


app = FastAPI(
    title="ClearBorder API",
    description="Moteur de calcul CBAM (Specific Embedded Emissions) et conformité douanière",
    version="0.1.0",
    lifespan=lifespan,
    docs_url="/docs",
    redoc_url="/redoc",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(routes.router, prefix="/api/v1", tags=["API"])


@app.get("/")
def root():
    return {
        "name": "ClearBorder",
        "version": "0.1.0",
        "docs": "/docs",
        "health": "/health",
    }


@app.get("/health")
def health():
    """Health check — utile pour les probes Kubernetes/Cloud Run."""
    from sqlalchemy import text
    from app.config import settings

    result = {"status": "ok"}
    if "sqlite" not in settings.database_url:
        try:
            with engine.connect() as conn:
                conn.execute(text("SELECT 1"))
            result["database"] = "connected"
        except Exception as e:
            result["database"] = "error"
            result["error"] = str(e)
    return result
