import csv
with open('orders.csv', "r", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        quantity = int(row['quantity'])
        price = float(row['price'])

        order_value = quantity * price
        
        print(order_value)

### example of json data
"""
[
    {
        "order_id": 301,
        "quantity": 2,
        "price": 15.50
    },
    {
        "order_id": 302,
        "quantity": 4,
        "price": 8.25
    }
]
"""

from fileinput import filename
import json
with open('orders.json', "r") as file:
    orders = json.load(file)

for order in orders:
    order_value = order['quantity'] * order['price']
    print(order_value)

###Unlike csv.DictReader, json.load() can preserve the data types represented in JSON. Here, quantity is an integer and price is a number, so you don't need to convert them first.


import json
import logging

logging.basicConfig( level=logging.INFO)

try:
    with open('orders.json', "r") as file:
        orders = json.load(file)
except FileNotFoundError as err:
    logging.error("Orders file was not found")

except json.JSONDecodeError as err:
    logging.error("Orders file contains invalid JSON")

else:
    logging.info("Orders file loaded successfully")
    print(orders)



###Build a reusable Json loader:


import json
import logging

logging.basicConfig(level = logging.INFO)

def load_json_file(filename):
    try:
        with open(filename, "r") as file:
            data = json.load(file)

    except FileNotFoundError:
        logging.error("File not found: %s", filename)
        return None

    except json.JSONDecodeError:
        logging.error("Invalid JSON in file: %s", filename)
        return None

    else:
        logging.info("Successfully loaded: %s", filename)
        return data


### orders = load_json_file("orders.json")
### if orders is not None:
###     print("Orders are ready for processing")


### EXERCISE
#JSON data with some invalid orders:
[
    {"order_id": 401, "quantity": 2, "price": 10.50},
    {"order_id": 402, "quantity": -1, "price": 5.00},
    {"order_id": 403, "quantity": 3, "price": 7.00}
]

def process_orders(orders):
    valid_orders = []
    rejected_count = 0

    for order in orders:
        try:
            quantity = int(order["quantity"])
            price = float(order["price"])

            if quantity <= 0:
                raise ValueError("Quantity must be positive")

        except (ValueError, KeyError) as err:
            rejected_count += 1
            logging.warning(
                "Order %s rejected: %s",
                order.get("order_id", "unknown"),   ###Note: er.get("order_id", "unknown") avoids another KeyError if the order ID itself is missing.
                err
            )

        else:
            order["order_value"] = quantity * price
            valid_orders.append(order)

    logging.info("Valid orders: %d", len(valid_orders))
    logging.info("Rejected orders: %d", rejected_count)

    return valid_orders