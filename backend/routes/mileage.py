from fastapi import APIRouter, Form, HTTPException
from typing import List, Optional
from datetime import datetime
from uuid import uuid4
import json
import os

router = APIRouter()

@router.post("/api/mileage-log")
async def create_mileage_log(
    start_location: str = Form(...),
    end_location: str = Form(...),
    distance: float = Form(...),
    purpose: str = Form(""),
    billable: bool = Form(False)
):
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
    
    with open("mileage_log.json", "a") as f:
        f.write(json.dumps(log) + "\n")
    
    return log

@router.get("/api/mileage-logs")
async def get_mileage_logs():
    logs = []
    try:
        with open("mileage_log.json", "r") as f:
            for line in f:
                logs.append(json.loads(line))
    except FileNotFoundError:
        pass
    return logs

@router.get("/api/mileage-log/{log_id}")
async def get_mileage_log(log_id: str):
    try:
        with open("mileage_log.json", "r") as f:
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
    logs = []
    found = False
    
    try:
        with open("mileage_log.json", "r") as f:
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
    
    with open("mileage_log.json", "w") as f:
        for log in logs:
            f.write(json.dumps(log) + "\n")
    
    return {"status": "updated", "id": log_id}

@router.delete("/api/mileage-log/{log_id}")
async def delete_mileage_log(log_id: str):
    logs = []
    found = False
    
    try:
        with open("mileage_log.json", "r") as f:
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
    
    with open("mileage_log.json", "w") as f:
        for log in logs:
            f.write(json.dumps(log) + "\n")
    
    return {"status": "deleted", "id": log_id} 