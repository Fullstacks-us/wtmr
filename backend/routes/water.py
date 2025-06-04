from fastapi import APIRouter, UploadFile, File, Form
from datetime import datetime
import json
import os
from uuid import uuid4
from typing import List

router = APIRouter()

def get_db_path():
    return "db/water_log.json"

def ensure_db_exists():
    if not os.path.exists(get_db_path()):
        with open(get_db_path(), "w") as f:
            json.dump([], f)

@router.post("/api/water-log")
async def create_water_log(
    ph: float = Form(...),
    chlorine: float = Form(...),
    hardness: float = Form(...),
    site: str = Form(...),
    notes: str = Form(""),
    image: UploadFile = File(...)
):
    # Ensure DB exists
    ensure_db_exists()
    
    # Generate unique ID for the record
    record_id = str(uuid4())
    
    # Save image
    image_filename = f"{record_id}_{image.filename}"
    image_path = os.path.join("images", image_filename)
    with open(image_path, "wb") as buffer:
        content = await image.read()
        buffer.write(content)
    
    # Create record
    record = {
        "id": record_id,
        "timestamp": datetime.now().isoformat(),
        "ph": ph,
        "chlorine": chlorine,
        "hardness": hardness,
        "site": site,
        "notes": notes,
        "image_path": image_path,
        "category": "daily water test"
    }
    
    # Save to JSON file
    with open(get_db_path(), "r+") as f:
        try:
            logs = json.load(f)
        except json.JSONDecodeError:
            logs = []
        logs.append(record)
        f.seek(0)
        json.dump(logs, f, indent=2)
        f.truncate()
    
    return {"status": "success", "id": record_id}

@router.get("/api/water-log/{log_id}")
async def get_water_log(log_id: str):
    ensure_db_exists()
    
    with open(get_db_path(), "r") as f:
        logs = json.load(f)
        for log in logs:
            if log["id"] == log_id:
                return log
    return {"error": "Log not found"}

@router.get("/api/water-logs")
async def get_water_logs():
    logs = []
    try:
        with open(get_db_path(), "r") as f:
            for line in f:
                logs.append(json.loads(line))
    except FileNotFoundError:
        pass
    return logs 