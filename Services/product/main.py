from fastapi import FastAPI
from routes import products
import os

app = FastAPI(title="Product Service")

@app.get("/health")
def health():
    return {"status": "ok", "service": "product-service"}

@app.get("/info")
def info():
    return {
        "service": "product-service",
        "version": "1.0.0",
        "port": os.getenv("PORT", 8002)
    }

app.include_router(products.router)
