

"""def transform_order(order):
    order["order_value"] = order["quantity"] * order["price"]
    return order


order = {
    "order_id": 101,
    "quantity": 2,
    "price": 15.50
}

result = transform_order(order)

print(result)"""

orders = [
    {"order_id": 101, "quantity": 2, "price": 15.50},
    {"order_id": 102, "quantity": 1, "price": 40.00},
    {"order_id": 103, "quantity": 3, "price": 8.25}
]

def transform_order(order):
    order["order_value"] = order["quantity"] * order["price"]
    return order

"""transformed_orders = []

for order in orders:
    transformed_order = transform_order(order)
    transformed_orders.append(transformed_order)

print(transformed_orders)"""

def is_valid_order(order):
    if order["quantity"] > 0 and order["price"] > 0:
        return True
    else:
        return False





def transform_orders(orders):
    valid_orders = []
    for order in orders:
        if is_valid_order(order):
            transformed_order = transform_order(order)
            valid_orders.append(transformed_order)
            
    return valid_orders


### use the transform_orders function to get valid orders with order_value
valid_orders = transform_orders(orders)

for order in valid_orders:
    print(order["order_id"], order["order_value"])

print("Valid orders:", len(valid_orders))

   





