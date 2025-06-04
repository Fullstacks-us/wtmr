from fastapi import APIRouter, UploadFile, File, Form
from datetime import datetime
import json
import os
from uuid import uuid4
from typing import Optional, List

router = APIRouter()

def get_db_path():
    return "db/meter_log.json"

def ensure_db_exists():
    if not os.path.exists(get_db_path()):
        with open(get_db_path(), "w") as f:
            json.dump([], f)

def get_last_reading():
    ensure_db_exists()
    try:
        with open(get_db_path(), "r") as f:
            logs = json.load(f)
            if logs:
                return logs[-1]["reading"]
    except (json.JSONDecodeError, KeyError, IndexError):
        pass
    return None

@router.get("/api/meter-last")
async def get_last_meter_reading():
    last_reading = get_last_reading()
    return {"last_reading": last_reading}

@router.post("/api/meter-log")
async def create_meter_log(
    reading: float = Form(...),
    notes: str = Form(""),
    image: Optional[UploadFile] = File(None)
):
    # Ensure DB exists
    ensure_db_exists()
    
    # Get last reading for delta calculation
    last_reading = get_last_reading()
    delta = reading - last_reading if last_reading is not None else None
    
    # Generate unique ID for the record
    record_id = str(uuid4())
    
    # Handle image if provided
    image_path = None
    if image:
        image_filename = f"{record_id}_{image.filename}"
        image_path = os.path.join("images", image_filename)
        with open(image_path, "wb") as buffer:
            content = await image.read()
            buffer.write(content)
    
    # Create record
    record = {
        "id": record_id,
        "timestamp": datetime.now().isoformat(),
        "reading": reading,
        "delta": delta,
        "notes": notes,
        "image_path": image_path,
        "category": "daily meter log"
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
    
    return {
        "status": "success", 
        "id": record_id,
        "delta": delta
    }

@router.get("/api/meter-log/{log_id}")
async def get_meter_log(log_id: str):
    ensure_db_exists()
    
    with open(get_db_path(), "r") as f:
        logs = json.load(f)
        for log in logs:
            if log["id"] == log_id:
                return log
    return {"error": "Log not found"}

@router.get("/api/meter-logs")
async def get_meter_logs():
    logs = []
    try:
        with open(get_db_path(), "r") as f:
            for line in f:
                logs.append(json.loads(line))
    except FileNotFoundError:
        pass
    return logs 