from fastapi import APIRouter, Depends, HTTPException
from bson import ObjectId
from database import get_order_collection
from schemas import OrderCreate, OrderOut
from models import order_helper
from service_clients import get_user, get_product

router = APIRouter(prefix="/orders", tags=["Orders"])

@router.get("/", response_model=list[OrderOut])
async def list_orders(collection=Depends(get_order_collection)):
    orders = []
    async for order in collection.find():
        orders.append(order_helper(order))
    return orders

@router.get("/{order_id}", response_model=OrderOut)
async def get_order(order_id: str, collection=Depends(get_order_collection)):
    order = await collection.find_one({"_id": ObjectId(order_id)})
    if not order:
        raise HTTPException(404, "Order not found")
    return order_helper(order)

@router.post("/", response_model=OrderOut)
async def create_order(data: OrderCreate, collection=Depends(get_order_collection)):

    user = await get_user(data.user_id)
    if not user:
        raise HTTPException(400, "User does not exist")

    product = await get_product(data.product_id)
    if not product:
        raise HTTPException(400, "Product does not exist")

    doc = data.dict()
    result = await collection.insert_one(doc)
    new_order = await collection.find_one({"_id": result.inserted_id})
    return order_helper(new_order)

@router.put("/{order_id}", response_model=OrderOut)
async def update_order(order_id: str, data: OrderCreate, collection=Depends(get_order_collection)):
    update_doc = data.dict()
    result = await collection.update_one({"_id": ObjectId(order_id)}, {"$set": update_doc})
    
    if result.modified_count == 0:
        raise HTTPException(404, "Order not found or unchanged")
    
    updated = await collection.find_one({"_id": ObjectId(order_id)})
    return order_helper(updated)

@router.delete("/{order_id}")
async def delete_order(order_id: str, collection=Depends(get_order_collection)):
    result = await collection.delete_one({"_id": ObjectId(order_id)})
    if result.deleted_count == 0:
        raise HTTPException(404, "Order not found")
    return {"status": "deleted"}
