from decimal import Decimal

rows = [
    {"order_id": "101", "quantity": "2", "price": "15.50"},
    {"order_id": "102", "quantity": "abc", "price": "20.00"},
    {"order_id": "103", "quantity": "3", "price": "10.00"},
    {"order_id": "104", "quantity": "xyz", "price": "12.00"}
]



def process_orders(rows):
    valid_count = 0
    invalid_count = 0
    for row in rows:
        try:
            order_id = int(row["order_id"])
            quantity = int(row["quantity"])
            price = Decimal(row["price"])
        except ValueError:
            invalid_count += 1

        else:
            valid_count += 1
    return valid_count, invalid_count


### Separate the valid and invalid rows
def process_orders(rows):
    valid_rows = []
    invalid_rows = []

    for row in rows:
        try:
            order_id = int(row["order_id"])
            quantity = int(row["quantity"])
            price = Decimal(row["price"])
        except ValueError:
            invalid_rows.append(row)
        else:
            valid_rows.append(row)
    return valid_rows, invalid_rows



### function that separates valid and invalid rows and records why each row failed
from decimal import Decimal, InvalidOperation

def process_orders(rows):
    valid_rows = []
    rejected_rows = []

    for row in rows:
        try:
            order_id = int(row["order_id"])
            quantity = int(row["quantity"])
            price = Decimal(row["price"])

            if quantity <= 0:
                raise ValueError("Quantity must be positive")

            if price <= 0:
                raise ValueError("Price must be positive")

        except (ValueError, InvalidOperation) as err:
            rejected_rows.append({
                "row": row,
                "error_type": type(err).__name__,
                "reason": str(err)
            })

        else:
            valid_rows.append(row)

    return valid_rows, rejected_rows


### KeyError . Python raises it when you try to access a dictionary key that doesn't exist
### Add KeyError — Correct. We can update the handler to catch all three expected exceptions.

from decimal import Decimal, InvalidOperation

def process_orders(rows):
    valid_rows = []
    rejected_rows = []

    for row in rows:
        try:
            order_id = int(row["order_id"])
            quantity = int(row["quantity"])
            price = Decimal(row["price"])

            if quantity <= 0:
                raise ValueError("Quantity must be positive")

            if price <= 0:
                raise ValueError("Price must be positive")

        except (ValueError, InvalidOperation, KeyError) as err:
            rejected_rows.append({
                "row": row,
                "error_type": type(err).__name__,
                "reason": str(err)
            })

        else:
            valid_rows.append(row)

    return valid_rows, rejected_rows