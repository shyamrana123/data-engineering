orders = [
    {"order_id": "801", "quantity": "2", "price": "10.00"},
    {"order_id": "802", "quantity": "1", "price": "5.00"},
    {"order_id": "801", "quantity": "2", "price": "10.00"},
    {"order_id": "801", "quantity": "5", "price": "10.00"},
    {"order_id": "803", "quantity": "3", "price": "4.00"},
    {"order_id": "802", "quantity": "1", "price": "5.00"}
]


from pathlib import Path
import logging

logging.basicConfig(
    level= logging.INFO,
    format= "%(asctime)s - %(levelname)s - %(message)s",
    filename =str(Path(__file__).parent / "duplicate_detection.log"),
    filemode= "a"
)

orders_by_id = {}
exact_duplicates = []
conflicting_duplicates = []

for order in orders:
    order_id = order["order_id"]

    if order_id not in orders_by_id:
        orders_by_id[order_id] = order
        logging.info("New order found: %s", order_id)

    elif orders_by_id[order_id] == order:
        exact_duplicates.append(order)
        logging.warning("Exact duplicate found: %s", order_id)

    else:
        conflicting_duplicates.append(order)
        logging.error("Conflicting duplicate found:%s", order_id)

print("Total input records: ", len(orders))
print("Unique orders: ", len(orders_by_id))
print("Exact duplicates: ", len(exact_duplicates))
print("Conflicting duplicates: ", len(conflicting_duplicates))

logging.info("Duplicate detection completed")
logging.info("Total input records: %s", len(orders))
logging.info("Unique orders: %s", len(orders_by_id))
logging.info("Exact duplicates: %s", len(exact_duplicates))
logging.info("Conflicting duplicates: %s", len(conflicting_duplicates))