import json
import os
import psycopg
from dotenv import load_dotenv

load_dotenv()

#Read the transformed  data from JSON.

with open("day24_apis_json_etl/cleaned_customers.json", "r", encoding = "utf-8") as file:
    customers=json.load(file)

print("Records loaded from JSON:", len(customers))

#Connect to PostgreSQL.
with psycopg.connect(
    host = os.getenv("DB_HOST"),
    port = os.getenv("DB_PORT"),
    dbname = os.getenv("DB_NAME"),
    user = os.getenv("DB_USER"),
    password = os.getenv("DB_PASSWORD")
) as connection:
    with connection.cursor() as cursor:
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS api_customers_staging(
        customer_id INTEGER PRIMARY KEY,
        customer_name VARCHAR(100),
        email VARCHAR(150),
        city VARCHAR(100)
        );
        """)
        print("Staging table is ready.")

        #The connection context commits when it exits successfully.

        # Insert records into the staging table.
        insert_query = """
            INSERT INTO api_customers_staging
                (customer_id, customer_name, email, city)
                VALUES (%s,%s,%s,%s)
                ON CONFLICT (customer_id)
                DO UPDATE SET
                    customer_name = EXCLUDED.customer_name,
                    email=EXCLUDED.email,
                    city=EXCLUDED.city
                """

        for customer in customers:
            cursor.execute(
                insert_query,
                (
                    customer["customer_id"],
                    customer["customer_name"],
                    customer["email"],
                    customer["city"]
                )
            )

        print("Records inserted or updated:", len(customers))

        #Verify the records.

        cursor.execute("""
                SELECT customer_id, customer_name, email, city
                FROM api_customers_staging
                ORDER BY customer_id;
                """)

        results = cursor.fetchall()

        print("\nStaging table contents:")
        for row in results:
            print(row)

print("\nDatabase operatioin completed successfully.")