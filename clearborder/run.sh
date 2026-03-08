#!/bin/bash
# Lancement ClearBorder - API + Dashboard
cd "$(dirname "$0")"

# Créer venv si besoin
if [ ! -d "venv" ]; then
    python3 -m venv venv
fi
source venv/bin/activate

# Installer deps
pip install -q -r requirements.txt

# Seed data
python scripts/seed_data.py

# Lancer API en arrière-plan
echo "Starting API on http://localhost:8000"
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000 &
API_PID=$!

# Lancer Dashboard
sleep 2
echo "Starting Dashboard on http://localhost:8501"
streamlit run dashboard/app.py --server.port 8501 --server.address 0.0.0.0

# Cleanup
kill $API_PID 2>/dev/null
