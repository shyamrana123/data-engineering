###What does idempotency mean?
###Running the same operation multiple times produces the same final result as running it once, rather than repeatedly duplicating its effects.

""" Idempotent pipeline
    Run 1: 100 unique orders. Run 2: still 100 unique orders.

    Non-idempotent pipeline
    Run 1: 100 orders. Run 2: 200 records, including duplicates."""


"""orders = [
    {"order_id": "701", "quantity": "2", "price": "10.00"},
    {"order_id": "702", "quantity": "1", "price": "5.00"},
    {"order_id": "701", "quantity": "2", "price": "10.00"},
    {"order_id": "703", "quantity": "3", "price": "4.00"}
]   

seen_order_ids = set()
unique_orders = []

for order in orders:
    order_id = order["order_id"]

    if order_id not in seen_order_ids:
        unique_orders.append(order)
        seen_order_ids.add(order_id)

print("Original Orders:", len(orders))
print("Unique Orders:", len(unique_orders))
"""
"""List versus set
- List: Preserves insertion order and allows duplicate values.
- Set: Stores unique values and doesn't guarantee insertion order."""


orders = [
    {"order_id": "801", "quantity": "2", "price": "10.00"},
    {"order_id": "802", "quantity": "1", "price": "5.00"},
    {"order_id": "801", "quantity": "2", "price": "10.00"},
    {"order_id": "801", "quantity": "5", "price": "10.00"}
]

orders_by_id = {}
exact_duplicates = []
conflicting_duplicates = []

for order in orders:
    order_id = order["order_id"]

    if order_id not in orders_by_id:
        orders_by_id[order_id] = order   ###Use a dictionary to track the first record for each order ID

    elif orders_by_id[order_id] == order:
        exact_duplicates.append(order)

    else:
        conflicting_duplicates.append(order)

print("Unique orders:", len(orders_by_id))
print("Exact duplicates:", len(exact_duplicates))
print("Conflicting duplicates:", len(conflicting_duplicates))
