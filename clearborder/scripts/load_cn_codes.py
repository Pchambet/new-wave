#!/usr/bin/env python3
"""Charge la nomenclature CN dans la base de données."""
import sys
import json
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from app.database import SessionLocal, init_db
from app.models import CNCode


def load_from_json(filepath: Path) -> list[dict]:
    """Charge les codes CN depuis un fichier JSON."""
    with open(filepath, encoding="utf-8") as f:
        return json.load(f)


def load_cn_codes():
    """Charge les codes CN dans la BDD."""
    init_db()
    db = SessionLocal()
    try:
        data_dir = Path(__file__).parent.parent / "data"
        json_file = data_dir / "cn_codes_sample.json"
        if not json_file.exists():
            print(f"Fichier non trouvé: {json_file}")
            return 0

        codes = load_from_json(json_file)
        count = 0
        for item in codes:
            code = item.get("code", "").replace(" ", "")
            desc = item.get("description", "")
            if db.query(CNCode).filter(CNCode.code == code).first():
                continue
            db.add(CNCode(code=code, description=desc, level=2))
            count += 1
        db.commit()
        print(f"Chargé {count} codes CN (total: {db.query(CNCode).count()})")
        return count
    finally:
        db.close()


if __name__ == "__main__":
    load_cn_codes()
