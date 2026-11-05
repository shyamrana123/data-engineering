import os
import psycopg
import pandas as pd

from pathlib import Path
from dotenv import load_dotenv

#1. Define project directories
BASE_DIR = Path(__file__).resolve().parent.parent
REPO_DIR = BASE_DIR.parent
DATA_DIR = BASE_DIR/"data"

#2. Load database credentials from the existing .env
load_dotenv(REPO_DIR/".env")

#3. Read source CSV files
customers = pd.read_csv(DATA_DIR/"customers.csv")
products = pd.read_csv(DATA_DIR/"products.csv")
orders = pd.read_csv(DATA_DIR/"orders.csv")

#4. Transform the data
sales = orders.merge(customers, on = "customer_id", how = "left")
sales = sales.merge(products, on = "product_id", how = "left")

sales["sales_amount"] = sales["quantity"] * sales["unit_price"]
sales["order_date"] = pd.to_datetime(sales["order_date"]).dt.date

#5. Prepare database connection settings
db_config = {
    "host": os.getenv("DB_HOST"),
    "port": os.getenv("DB_PORT"),
    "dbname": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
}

#6. Check that all credentials are available
if not all(db_config.values()):
    raise ValueError("Missing database settings. Check you .env file")

#7. Connect and load data
try:
    with psycopg.connect(**db_config) as conn:
        with conn.cursor() as cur:
            #Clear previous staging data for safe reruns
            cur.execute("""
                TRUNCATE TABLE
                    stg_orders,
                    stg_products,
                    stg_customers;
                """)
            
            #Load customers
            cur.executemany("""
                INSERT INTO stg_customers (
                customer_id,
                customer_name,
                email,
                country,
                city)
                VALUES (%s, %s, %s, %s, %s);
            """, customers.itertuples(index=False, name = None))

            #Load products
            cur.executemany("""
                INSERT INTO stg_products(
                    product_id,
                    product_name,
                    category,
                    unit_price
                )
                VALUES(%s,%s,%s, %s);
            """, products.itertuples(index = False, name = None))

            #Load transformed orders
            order_columns = [
                "order_id",
                "order_item_number",
                "customer_id",
                "product_id",
                "order_date",
                "quantity",
                "unit_price",
                "sales_amount",
                "customer_name",
                "country",
                "city",
                "product_name",
                "category",
            ]

            cur.executemany("""
                INSERT INTO stg_orders(
                    order_id,
                    order_item_number,
                    customer_id,
                    product_id,
                    order_date,
                    quantity,
                    unit_price,
                    sales_amount,
                    customer_name,
                    country,
                    city,
                    product_name,
                    category)
                VALUES(
                    %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s
                );
                """, sales[order_columns].itertuples(index = False,name = None))
        # The connection context commits if successful.
        print("Data loaded successfully!") 

except Exception as error:
    print("Data loading failed.")
    print(f"Error:{error}")
    raise

#8. Display loading summary
print(f"Customer loaded: {len(customers)}")
print(f"Products loaded: {len(products)}")
print(f"Order items loaded: {len(sales)}")
print(f"Total sales revenue: ${sales['sales_amount'].sum():,.2f}")