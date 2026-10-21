def calculate_order_value(quantity, price):
    return quantity * price

order_value = calculate_order_value(3,5.00)
print(order_value)

orders = [
    {"order_id": 901, "quantity": 2, "price": 10.00},
    {"order_id": 902, "quantity": 3, "price": 5.00},
    {"order_id": 903, "quantity": 4, "price": 2.50}
]
### Example of function composition: using one function inside another to build more useful functionality.

def calculate_total_value(orders):  ###function uses the previous calculate_order_value() function inside a loop
    total = 0

    for order in orders:
        order_value = calculate_order_value(
            order["quantity"],
            order["price"]
        )
        total += order_value

    return total


### function that transforms every order by adding an order_value field.

orders = [
    {"order_id": 901, "quantity": 2, "price": 10.00},
    {"order_id": 902, "quantity": 3, "price": 5.00},
    {"order_id": 903, "quantity": 4, "price": 2.50}
]

def transform_orders(orders):
    transformed_orders = []

    for order in orders:
        order_value = calculate_order_value(
            order["quanity"],
            order["price"]
        )

        transformed_order = order.copy()
        transformed_order["order_value"]= order_value

        transformed_orders.append(transformed_order)

    return transformed_orders

### Understanding:
#- transformed_orders = [] creates an empty list to store the results.
#- order.copy() creates a copy of the current order, leaving the original dictionary unchanged.
#- transformed_order["order_value"] = order_value adds the calculated value to the copied order.
#- transformed_orders.append(...) adds the transformed order to the results list.
#- return transformed_orders returns the completed list after the loop finishes.

### Result
"""[
    {"order_id": 901, "quantity": 2, "price": 10.00, "order_value": 20.00},
    {"order_id": 902, "quantity": 3, "price": 5.00, "order_value": 15.00},
    {"order_id": 903, "quantity": 4, "price": 2.50, "order_value": 10.00}
]"""


def transform_orders(orders):
    transformed_orders = []
    rejected_orders = []

    for order in orders:
        if order["quantity"] <= 0:
            rejected_orders.append({
                "order": order,
                "reason": "Quantity must be positive"
            })
            continue

        if order["price"] <= 0:
            rejected_orders.append({
                "order": order,
                "reason": "Price must be positive"
            })
            continue

        order_value = calculate_order_value(
            order["quantity"],
            order["price"]
        )

        transform_order = order.copy()
        transformed_order["order_value"] = order_value
        transformed_orders.append(transformed_order)

    return transformed_orders, rejected_orders


###Understand the new parts:
#- rejected_orders = [] creates a separate list for invalid records.
#- rejected_orders.append(...) saves the original order and a reason for rejection.
#- continue prevents an invalid order from reaching the transformation steps.
#- return transformed_orders, rejected_orders returns two results from the function.
#- Python allows a function to return multiple values. You can capture them like this:
#   valid_orders, rejected_orders = transform_orders(orders)

orders = [
    {"order_id": 901, "quantity": 2, "price": 10.00},
    {"order_id": 902, "quantity": -3, "price": 5.00},
    {"order_id": 903, "quantity": 4, "price": 2.50},
    {"order_id": 904, "quantity": 3, "price": 0}
]




