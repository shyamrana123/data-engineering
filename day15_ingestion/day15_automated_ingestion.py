import logging
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename=str(Path(__file__).parent / "pipeline.log"),    ###Creates a log file in the same folder as the script, day15_ingestion.
    filemode='a'
)

import csv
from decimal import Decimal, InvalidOperation

data_folder = Path(__file__).parent / "data"    ###Path(__file__) identifies the path of your Python script.
                                                ###.parent gets the folder containing the script, day15_ingestion.
                                                ###/ "data" points to the data folder inside it.

csv_files = list(data_folder.glob("*.csv"))

all_orders = []
valid_orders = []
rejected_orders = []

logging.info("Pipeline started")
for file_path in csv_files:
    with open(file_path, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            all_orders.append(row)

for row in all_orders:
    try:
        order_id = int(row["order_id"])
        quantity = int(row["quantity"])
        price = Decimal(row["price"])

        if quantity <= 0:
            raise ValueError("Quantity must be positive")

        if price <= 0:
            raise ValueError("Price must be positive")
        

    except (ValueError,InvalidOperation, KeyError) as err:
        rejected_orders.append({
            "row": row,
            "reason": str(err)
        })
        logging.warning(
            "rejected order %s: %s",
            row.get("order_id", "unknown"),
            str(err)
        )
        continue 

    valid_orders.append({
            "order_id": order_id,
            "quantity": quantity,
            "price": price,
            "order_value": quantity * price     
        }) 

logging.info("Total orders loaded: %d", len(all_orders))
logging.info("Valid orders: %d", len(valid_orders))
logging.info("Rejected orders: %d", len(rejected_orders))

total_value = sum(
    (order["order_value"] for order in valid_orders),
    Decimal(0)
)

print("Total order value:", total_value)
logging.info("Total order value: %s", total_value)
logging.info("Pipeline finished")

"""print("Files found:", len(csv_files))
print("Total orders loaded:", len(all_orders))
print("Valid orders:", len(valid_orders))
print("Rejected orders:", len(rejected_orders))"""



###PROJECT CHECKLIST:
"""Automatically discover CSV files with pathlib

Read and combine records using csv.DictReader

Convert quantities and prices to appropriate types

Validate records and preserve rejection reasons

Continue processing when a record is invalid

Calculate the total value using Decimal

Log pipeline activity to pipeline.log

Keep generated log files out of Git"""