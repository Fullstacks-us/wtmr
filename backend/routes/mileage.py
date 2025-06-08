from fastapi import APIRouter, Form, HTTPException
from typing import List, Optional
from datetime import datetime
from uuid import uuid4
import json
import os

router = APIRouter()

def get_db_path():
    return "db/mileage_log.json"

def ensure_db_exists():
    os.makedirs(os.path.dirname(get_db_path()), exist_ok=True)
    if not os.path.exists(get_db_path()):
        with open(get_db_path(), "w") as f:
            pass

@router.post("/api/mileage-log")
async def create_mileage_log(
    start_location: str = Form(...),
    end_location: str = Form(...),
    distance: float = Form(...),
    purpose: str = Form(""),
    billable: bool = Form(False)
):
    ensure_db_exists()
    log = {
        "id": str(uuid4()),
        "timestamp": datetime.now().isoformat(),
        "start_location": start_location,
        "end_location": end_location,
        "distance": distance,
        "purpose": purpose,
        "billable": billable,
        "category": "mileage"
    }
    
    with open(get_db_path(), "a") as f:
        f.write(json.dumps(log) + "\n")
    
    return log

@router.get("/api/mileage-logs")
async def get_mileage_logs():
    ensure_db_exists()
    logs = []
    try:
        with open(get_db_path(), "r") as f:
            for line in f:
                logs.append(json.loads(line))
    except FileNotFoundError:
        pass
    return logs

@router.get("/api/mileage-log/{log_id}")
async def get_mileage_log(log_id: str):
    ensure_db_exists()
    try:
        with open(get_db_path(), "r") as f:
            for line in f:
                log = json.loads(line)
                if log["id"] == log_id:
                    return log
    except FileNotFoundError:
        pass
    raise HTTPException(status_code=404, detail="Log not found")

@router.put("/api/mileage-log/{log_id}")
async def update_mileage_log(
    log_id: str,
    start_location: str = Form(...),
    end_location: str = Form(...),
    distance: float = Form(...),
    purpose: str = Form(""),
    billable: bool = Form(False)
):
    ensure_db_exists()
    logs = []
    found = False

    try:
        with open(get_db_path(), "r") as f:
            for line in f:
                log = json.loads(line)
                if log["id"] == log_id:
                    log.update({
                        "start_location": start_location,
                        "end_location": end_location,
                        "distance": distance,
                        "purpose": purpose,
                        "billable": billable
                    })
                    found = True
                logs.append(log)
    except FileNotFoundError:
        pass
    
    if not found:
        raise HTTPException(status_code=404, detail="Log not found")
    
    with open(get_db_path(), "w") as f:
        for log in logs:
            f.write(json.dumps(log) + "\n")
    
    return {"status": "updated", "id": log_id}

@router.delete("/api/mileage-log/{log_id}")
async def delete_mileage_log(log_id: str):
    ensure_db_exists()
    logs = []
    found = False

    try:
        with open(get_db_path(), "r") as f:
            for line in f:
                log = json.loads(line)
                if log["id"] != log_id:
                    logs.append(log)
                else:
                    found = True
    except FileNotFoundError:
        pass
    
    if not found:
        raise HTTPException(status_code=404, detail="Log not found")
    
    with open(get_db_path(), "w") as f:
        for log in logs:
            f.write(json.dumps(log) + "\n")
    
    return {"status": "deleted", "id": log_id} 