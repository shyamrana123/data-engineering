import pandas as pd
from pathlib import Path

#Project directory
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR/"data"

#Extract source data
customers = pd.read_csv(DATA_DIR/"customers.csv")
products = pd.read_csv(DATA_DIR/"products.csv")
orders = pd.read_csv(DATA_DIR/"orders.csv")

"""#Dislplay extracted data
print("CUSTOMERS")
print(customers.head())

print("\nPRODUCTS")
print(products.head())

print("\nORDERS")
print(orders.head())

#Display row counts
print("\nExtracted row counts:")
print(f"Customers: {len(customers)}")
print(f"Products: {len(products)}")
print(f"Orders: {len(orders)}")"""

#Transform: join orders with customers
sales = orders.merge(
        customers, 
        on = "customer_id",
        how = "left")

#Transform: join sales with products
sales = sales.merge(
    products,
    on = "product_id",
    how = "left"
)

# Calculate sales amount
sales["sales_amount"] = sales["quantity"] * sales["unit_price"]

# Convert order_date into datetime
sales["order_date"] = pd.to_datetime(sales["order_date"])

#Check for missing values:
print("\nMissing values:")
print(sales.isnull().sum())


#Check for duplicate order items
print("\nDuplicate order items:")
print(sales.duplicated(subset = ["order_id","order_item_number"]).sum())

#Display transformed data
print("\nTRANSFORMED SALES DATA")
print(sales[["order_id", "customer_name", "country","product_name", "category", "quantity", "unit_price", "sales_amount"]].to_string(index=False))
print("\nTotal sales revenue:")
print(sales["sales_amount"].sum())