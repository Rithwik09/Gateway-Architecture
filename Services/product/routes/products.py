from fastapi import APIRouter, Depends, HTTPException
from database import get_product_collection
from schemas import ProductCreate, ProductOut
from models import product_helper
from bson import ObjectId

router = APIRouter(prefix="/products", tags=["Products"])

@router.get("/", response_model=list[ProductOut])
async def get_products(collection=Depends(get_product_collection)):
    products = []
    async for product in collection.find():
        products.append(product_helper(product))
    return products

@router.get("/{product_id}", response_model=ProductOut)
async def get_product(product_id: str, collection=Depends(get_product_collection)):
    product = await collection.find_one({"_id": ObjectId(product_id)})
    if not product:
        raise HTTPException(404, "Product not found")
    return product_helper(product)

@router.post("/", response_model=ProductOut)
async def create_product(data: ProductCreate, collection=Depends(get_product_collection)):
    doc = data.dict()
    result = await collection.insert_one(doc)
    prod = await collection.find_one({"_id": result.inserted_id})
    return product_helper(prod)

@router.put("/{product_id}", response_model=ProductOut)
async def update_product(product_id: str, data: ProductCreate, collection=Depends(get_product_collection)):
    update_data = data.dict()
    result = await collection.update_one({"_id": ObjectId(product_id)}, {"$set": update_data})

    if result.modified_count == 0:
        raise HTTPException(404, "Product not found or unchanged")

    updated = await collection.find_one({"_id": ObjectId(product_id)})
    return product_helper(updated)

@router.delete("/{product_id}")
async def delete_product(product_id: str, collection=Depends(get_product_collection)):
    result = await collection.delete_one({"_id": ObjectId(product_id)})
    if result.deleted_count == 0:
        raise HTTPException(404, "Product not found")
    return {"status": "deleted"}
