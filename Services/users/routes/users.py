# app/routes/users.py
from fastapi import APIRouter, Depends, HTTPException
from database import get_user_collection
from schemas import UserCreate, UserOut
from models import user_helper
from bson import ObjectId

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/", response_model=list[UserOut])
async def get_users(collection=Depends(get_user_collection)):
    users = []
    async for user in collection.find():
        users.append(user_helper(user))
    return users

@router.get("/{user_id}", response_model=UserOut)
async def get_user(user_id: str, collection=Depends(get_user_collection)):
    user = await collection.find_one({"_id": ObjectId(user_id)})
    if not user:
        raise HTTPException(404, "User not found")
    return user_helper(user)

@router.post("/", response_model=UserOut)
async def create_user(data: UserCreate, collection=Depends(get_user_collection)):
    new_user = data.dict()
    result = await collection.insert_one(new_user)
    created_user = await collection.find_one({"_id": result.inserted_id})
    return user_helper(created_user)

@router.put("/{user_id}", response_model=UserOut)
async def update_user(user_id: str, data: UserCreate, collection=Depends(get_user_collection)):
    update_data = data.dict()
    result = await collection.update_one({"_id": ObjectId(user_id)}, {"$set": update_data})

    if result.modified_count == 0:
        raise HTTPException(404, "User not found or no changes made")

    updated_user = await collection.find_one({"_id": ObjectId(user_id)})
    return user_helper(updated_user)

@router.delete("/{user_id}")
async def delete_user(user_id: str, collection=Depends(get_user_collection)):
    result = await collection.delete_one({"_id": ObjectId(user_id)})

    if result.deleted_count == 0:
        raise HTTPException(404, "User not found")

    return {"status": "deleted"}
