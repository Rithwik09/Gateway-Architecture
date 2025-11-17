# main.py
from fastapi import FastAPI
from routes import users
import os

app = FastAPI(title="User Service")

@app.get("/health")
async def health():
    return {"status": "ok", "service": "user-service"}

@app.get("/info")
async def info():
    return {
        "service": "user-service",
        "version": "1.0.0",
        "port": os.getenv("PORT", 8001)
    }

app.include_router(users.router)
