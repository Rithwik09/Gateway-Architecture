from pydantic import BaseModel, Field
from bson import ObjectId
from typing import Optional

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid ObjectId")
        return ObjectId(v)

class OrderCreate(BaseModel):
    user_id: str
    product_id: str
    quantity: int = 1

class OrderOut(BaseModel):
    id: PyObjectId = Field(alias="_id")
    user_id: str
    product_id: str
    quantity: int

    class Config:
        json_encoders = {ObjectId: str}
        allow_population_by_field_name = True
