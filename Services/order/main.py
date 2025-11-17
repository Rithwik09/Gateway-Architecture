from fastapi import FastAPI
from routes import orders
import os

app = FastAPI(title="Order Service")

@app.get("/health")
def health():
    return {"status": "ok", "service": "order-service"}

@app.get("/info")
def info():
    return {
        "service": "order-service",
        "version": "1.0.0",
        "port": os.getenv("PORT", 8003)
    }

app.include_router(orders.router)
