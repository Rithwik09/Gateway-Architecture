def order_helper(order) -> dict:
    return {
        "id": str(order["_id"]),
        "user_id": order["user_id"],
        "product_id": order["product_id"],
        "quantity": order["quantity"],
    }
