def calculate_order_value(quantity, price):
    return quantity*price
    pass

def transform_orders(orders):
    transformed_orders =[]
    rejected_orders = []

    for order in orders:
        if order["quantity"] <= 0:
            rejected_orders.append({
                "order":order,
                "reason": "Quantity must be positive"
            })
            continue

        elif order["price"] <=0:
            rejected_orders.append({
                "order": order,
                "reason": "Price must be positive"
            })

        else:
            transformed_order = order.copy()
            transformed_order["order_value"] = calculate_order_value(order["quantity"], order["price"])
            transformed_orders.append(transformed_order)

    return transformed_orders, rejected_orders

valid_orders = []
rejected_orders = []


orders = [
    {"order_id": 901, "quantity": 2, "price": 10.00},
    {"order_id": 902, "quantity": -3, "price": 5.00},
    {"order_id": 903, "quantity": 4, "price": 2.50},
    {"order_id": 904, "quantity": 3, "price": 0}
]

valid_orders, rejected_orders = transform_orders(orders)

print("valid orders list:", valid_orders)
print("rejected orders list:",rejected_orders)