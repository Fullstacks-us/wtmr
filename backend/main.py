from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
import json
import os
from datetime import datetime
from uuid import uuid4
from routes import water, meter, mileage

app = FastAPI(title="Water/Mileage Logger")

# CORS setup for local development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # We'll tighten this later for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create necessary directories
os.makedirs("db", exist_ok=True)
os.makedirs("images", exist_ok=True)

# Mount static files
app.mount("/static", StaticFiles(directory="frontend"), name="static")

# Include routers
app.include_router(water.router)
app.include_router(meter.router)
app.include_router(mileage.router)

@app.get("/")
async def read_root():
    return {"status": "ok", "message": "Water/Mileage Logger API"}

# Basic health check
@app.get("/health")
async def health_check():
    return {"status": "healthy", "timestamp": datetime.now().isoformat()} 