"""###import csv
with open("orders.csv", "r") as order_file:
    reader = csv.DictReader(order_file)
    for row in reader:
        print(row) """

"""import csv

with open("orders.csv", "r") as order_file:
    reader = csv.DictReader(order_file)

    for row in reader:
        order_id = int(row["order_id"])
        product_id = int(row["product_id"])
        price = float(row["price"])
        quantity = int(row["quantity"])
        total = float(row["total"])

        print(order_id, product_id, price, quantity, total)  """

"""import csv
with open("orders.csv", "r") as order_file:
    reader = csv.DictReader(order_file)
    for row in reader:
        order_id = int(row["order_id"])
        product_id = int(row["product_id"])
        price = float(row["price"])
        quantity = int(row["quantity"])
        total = float(row["total"])
        
        order = {
            "order_id": order_id,           
            "customer_name": row["customer_name"],
            "customer_email": row["customer_email"],
            "product_id": product_id,
            "price": price,
            "quantity": quantity,
            "total": total
        }
        print(order)""" 

"""import csv
with open("orders.csv", "r") as order_file:
    reader = csv.DictReader(order_file)
    for row in reader:
        order_id = int(row["order_id"])
        product_id = int(row["product_id"])
        price = float(row["price"])
        quantity = int(row["quantity"])
        total = float(row["total"])
        calculated_total = price * quantity
        if total != calculated_total:
            print(f"Total mismatch:", order_id)
        else:
            print(f"Total matches:", order_id)
            
                
        order = {
            "order_id": order_id,           
            "customer_name": row["customer_name"],
            "customer_email": row["customer_email"],
            "product_id": product_id,
            "price": price,
            "quantity": quantity,
            "total": total,
     
        }
        print(order)"""


"""import csv

valid_orders = []
total_rows = 0
with open("orders.csv", "r") as order_file:
    reader = csv.DictReader(order_file)

    for row in reader:
        total_rows += 1
        order_id = int(row["order_id"])
        product_id = int(row["product_id"])
        price = float(row["price"])
        quantity = int(row["quantity"])
        total = float(row["total"])

        order = {
            "order_id": order_id,
            "customer_name": row["customer_name"],
            "customer_email": row["customer_email"],
            "product_id": product_id,
            "price": price,
            "quantity": quantity,
            "total": total
        }

        calculated_total = price * quantity

        if total != calculated_total:
            print(f"Total mismatch: {order_id}",
                  f"expected {calculated_total}, got {total}")
        else:
            valid_orders.append(order)


print("Total rows:", total_rows)
print("Valid orders:", len(valid_orders))
print("Invalid orders:", total_rows - len(valid_orders))"""

"""import csv
from decimal import Decimal

valid_orders = []
total_rows = 0
with open("orders.csv", "r") as order_file:
    reader = csv.DictReader(order_file)

    for row in reader:
        total_rows += 1
        order_id = int(row["order_id"])
        product_id = int(row["product_id"])
        price = Decimal(row["price"])
        quantity = int(row["quantity"])
        total = Decimal(row["total"])

        order = {
            "order_id": order_id,
            "customer_name": row["customer_name"],
            "customer_email": row["customer_email"],
            "product_id": product_id,
            "price": price,
            "quantity": quantity,
            "total": total
        }

        calculated_total = price * quantity

        if total != calculated_total:
            print(f"Total mismatch: {order_id}",
                  f"expected {calculated_total}, got {total}")
        else:
            valid_orders.append(order)


print("Total rows:", total_rows)
print("Valid orders:", len(valid_orders))
print("Invalid orders:", total_rows - len(valid_orders))"""

"""import psycopg
conn = psycopg.connect(
    host="localhost",
    dbname="postgres",
    user="postgres",
    password = input("Postgres password: ")
)
print("Database connection established successfully!")
conn.close()

import csv
import os
from pathlib import Path
from decimal import Decimal

print("Current working directory:", os.getcwd() )
BASE_DIR = Path(__file__).resolve().parent
csv_file = BASE_DIR / "orders.csv"
valid_orders = []
total_rows = 0
with open(csv_file, "r") as order_file:
    reader = csv.DictReader(order_file)

    for row in reader:
        total_rows += 1
        order_id = int(row["order_id"])
        product_id = int(row["product_id"])
        price = Decimal(row["price"])
        quantity = int(row["quantity"])
        total = Decimal(row["total"])
        order_value = price * quantity

        order = {
            "order_id": order_id,
            "customer_name": row["customer_name"],
            "customer_email": row["customer_email"],
            "product_id": product_id,
            "price": price,
            "quantity": quantity,
            "order_value": order_value
        }

        

        if total != order_value:
            print(f"Total mismatch: {order_id}",
                  f"expected {order_value}, got {total}")
        else:
            valid_orders.append(order)


print("Total rows:", total_rows)
print("Valid orders:", len(valid_orders))
print("Invalid orders:", total_rows - len(valid_orders))"""




import csv
from decimal import Decimal

valid_orders = []
total_rows = 0
with open("orders.csv", "r") as order_file:
    reader = csv.DictReader(order_file)

    for row in reader:
        total_rows += 1
        order_id = int(row["order_id"])
        product_id = int(row["product_id"])
        price = Decimal(row["price"])
        quantity = int(row["quantity"])
        total = Decimal(row["total"])
        order_value = price * quantity

        order = {
            "order_id": order_id,
            "customer_name": row["customer_name"],
            "customer_email": row["customer_email"],
            "product_id": product_id,
            "price": price,
            "quantity": quantity,
            "order_value": order_value
        }

        

        if total != order_value:
            print(f"Total mismatch: {order_id}",
                  f"expected {order_value}, got {total}")
        else:
            valid_orders.append(order)


print("Total rows:", total_rows)
print("Valid orders:", len(valid_orders))
print("Invalid orders:", total_rows - len(valid_orders))

import psycopg

conn = psycopg.connect(
    host="localhost",
    dbname="postgres",
    user="postgres",
    password = input("Postgres password: ")
)
try:
    with conn.cursor() as cur:
        for order in valid_orders:
            cur.execute(
                """
                INSERT INTO etl_orders (
                    order_id,
                    customer_name,
                    customer_email,
                    product_id,
                    price,
                    quantity,
                    order_value
                ) 
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                ON CONFLICT (order_id) 
                DO UPDATE SET 
                    customer_name = EXCLUDED.customer_name,
                    customer_email = EXCLUDED.customer_email,
                    product_id = EXCLUDED.product_id,
                    price = EXCLUDED.price,
                    quantity = EXCLUDED.quantity,
                    order_value = EXCLUDED.order_value                
                """,
                (
                    order["order_id"],
                    order["customer_name"],
                    order["customer_email"],
                    order["product_id"],
                    order["price"],
                    order["quantity"],
                    order["order_value"]
                )

            


            )
    conn.commit()
    print("Orders inserted successfully into the database!")
except Exception as e:
    conn.rollback()
    print("Load failed:", e)
finally:
    conn.close()
