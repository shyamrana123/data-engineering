### Rollback before committing a record:

import os
import psycopg
from dotenv import load_dotenv

load_dotenv()

connection = None

try:
    connection = psycopg.connect(
        host = os.getenv("DB_HOST"),
        port = os.getenv("DB_PORT"),
        dbname = os.getenv("DB_NAME"),
        user = os.getenv("DB_USER"),
        password = os.getenv("DB_PASSWORD"),
    )

    print("Successfully connected to PostgreSQL")
    
    with connection.cursor() as cursor:
        cursor.execute(
            """
            UPDATE public.customers
            SET country = %s
            WHERE customer_id = %s
            """,
            ("Spain",107)
        )
        print("Rows updated:", cursor.rowcount)

    # Read the temporary value before rolling back.

    with connection.cursor() as cursor:
        cursor.execute(
            """
            SELECT customer_id, customer_name, country
            FROM public.customers
            WHERE customer_id = %s
            """,
            (107,)
        )

        print("Inside transaction:", cursor.fetchone())

    # Undo the uncommitted update.

    connection.rollback()
    print("Transaction rolled back.")

    # Verify the value after roll back.

    with connection.cursor() as cursor:
        cursor.execute(
            """
            SELECT customer_id, customer_name, country
            FROM public.customers
            WHERE customer_id = %s
            """,
            (107,)
        )
        print("After rollback:", cursor.fetchone())

except psycopg.OperationalError:
    print("Could not connect to PostgreSQL. Check your configuration and database server.")

finally:
    if connection is not None:
        connection.close() 
        print("Database connection closed.")









### COMMITTING A RECORD (difference between commit and rollback):

import os
import psycopg
from dotenv import load_dotenv

load_dotenv()

connection = None

try:
    connection = psycopg.connect(
        host = os.getenv("DB_HOST"),
        port = os.getenv("DB_PORT"),
        dbname = os.getenv("DB_NAME"),
        user = os.getenv("DB_USER"),
        password = os.getenv("DB_PASSWORD"),
    )

    print("Successfully connected to PostgreSQL")
    
    with connection.cursor() as cursor:
        cursor.execute(
            """
            UPDATE public.customers
            SET country = %s
            WHERE customer_id = %s
            """,
            ("Spain",107)
        )
        print("Rows updated:", cursor.rowcount)

    # Read the temporary value before rolling back.

    with connection.cursor() as cursor:
        cursor.execute(
            """
            SELECT customer_id, customer_name, country
            FROM public.customers
            WHERE customer_id = %s
            """,
            (107,)
        )

        print("Inside transaction:", cursor.fetchone())

    # Undo the uncommitted update.

    connection.commit()
    print("Transaction committed.")

    # Verify the value after roll back.

    with connection.cursor() as cursor:
        cursor.execute(
            """
            SELECT customer_id, customer_name, country
            FROM public.customers
            WHERE customer_id = %s
            """,
            (107,)
        )
        print("After rollback:", cursor.fetchone())

except psycopg.OperationalError:
    print("Could not connect to PostgreSQL. Check your configuration and database server.")

finally:
    if connection is not None:
        connection.close() 
        print("Database connection closed.")



# RESTORING DANIEL'S COUNTRY TO PORTUGAL:



import os
import psycopg
from dotenv import load_dotenv

load_dotenv()

connection = None

try:
    connection = psycopg.connect(
        host = os.getenv("DB_HOST"),
        port = os.getenv("DB_PORT"),
        dbname = os.getenv("DB_NAME"),
        user = os.getenv("DB_USER"),
        password = os.getenv("DB_PASSWORD"),
    )

    print("Successfully connected to PostgreSQL")
    
    with connection.cursor() as cursor:
        cursor.execute(
            """
            UPDATE public.customers
            SET country = %s
            WHERE customer_id = %s
            """,
            ("Portugal",107)
        )
        print("Rows updated:", cursor.rowcount)

    connection.commit()
    print("Restoration committed.")

    with connection.cursor() as cursor:
        cursor.execute(
            """
            SELECT customer_id, customer_name, country
            FROM public.customers
            WHERE customer_id = %s
            """,
            (107,)
        )

        result = cursor.fetchone()
        print("Final verified customer:", result)


except psycopg.OperationalError:
    print("Could not connect to PostgreSQL. Check your configuration and database server.")

finally:
    if connection is not None:
        connection.close() 
        print("Database connection closed.")

