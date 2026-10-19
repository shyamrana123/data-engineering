from pathlib import Path
data_folder = Path("data")
csv_files = list(data_folder.glob("*.csv"))

for file_path in csv_files:
    print(file_path)

### Path("data") represents the folder named data.
### .glob("*.csv") finds files in that folder whose names end in .csv.
### list(...) collects the matching paths into a list.
### The for loop processes each discovered path.



import csv
from pathlib import Path

data_folder = Path("data")
all_orders = []

csv_files = list(data_folder.glob("*.csv"))

for file_path in csv_files:
    with open(file_path, "r", newline="") as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            all_orders.append(row)

print("Total orders:", len(all_orders))
print(all_orders)

#continuation: convert the strings into correct data types for calculations.

from decimal import Decimal

total_value = Decimal("0")   ### initialize total_value as a Decimal object to avoid floating-point precision issues.

for row in all_orders:
    quantity = int(row['quantity'])
    price = Decimal(row['price'])
    
    order_value = quantity * price
    total_value += order_value

print("Total value:", total_value)


### Combining file handling, logging, exception handling and validation:

from decimal import Decimal, InvalidOperation

valid_orders = []
rejected_orders = []

for row in all_orders:
    try:
        order_id = row['order_id']
        quantity = int(row['quantity'])
        price = Decimal(row['price'])

        if quantity <=0:
            raise ValueError("Quanity must be positive")

        if price <= 0:
            raise ValueError("Price must be positive")

    except (ValueError, InvalidOperation, KeyError) as err:
        rejected_orders.append({
            "row": row,
            "reason": str(err)  
        })
        continue
    valid_orders.append({
        "order_id": order_id,
        "quantity": quantity,
        "price": price,
        "order_value": quantity * price
    })

        
