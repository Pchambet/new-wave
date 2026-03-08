FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

ENV PYTHONPATH=/app
ENV DATABASE_URL=sqlite:///./clearborder.db

EXPOSE 8080

# Cloud Run utilise PORT=8080 par défaut
CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8080}"]
