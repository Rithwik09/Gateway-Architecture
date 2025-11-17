import httpx

USER_SERVICE_URL = "http://localhost:8001"
PRODUCT_SERVICE_URL = "http://localhost:8002"

async def get_user(user_id: str):
    async with httpx.AsyncClient() as client:
        r = await client.get(f"{USER_SERVICE_URL}/users/{user_id}")
        if r.status_code != 200:
            return None
        return r.json()

async def get_product(product_id: str):
    async with httpx.AsyncClient() as client:
        r = await client.get(f"{PRODUCT_SERVICE_URL}/products/{product_id}")
        if r.status_code != 200:
            return None
        return r.json()
