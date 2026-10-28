### CHECKING IF THE RECORD ALREADY EXISTS , IF DOES NOT THEN INSERTING NEW RECORD:

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

    customer = (107, "Daniel", "daniel@example.com", "Portugal")

    with connection.cursor() as cursor:
        cursor.execute(
            """
            INSERT INTO public.customers
                (customer_id, customer_name, email, country)
            VALUES(%s, %s, %s, %s)
            ON CONFLICT (customer_id) DO NOTHING;
            """,
            customer                                                                                                      
        )                                                   
       

        connection.commit()                             # A database transaction groups changes together. In this example, commit() tells PostgreSQL to save the insertion permanently. 
                                                        # Without committing, the change may be rolled back when the connection closes.
        print("Insert attempted; checking the database record.")


    with connection.cursor() as cursor:
        cursor.execute(
            """
            SELECT customer_id, customer_name, email, country
            FROM public.customers
            WHERE customer_id = %s
            """,
            (customer[0],)
        )
        result = cursor.fetchone()
        print("Verified customer:",result)

       
except psycopg.OperationalError:
    print("Could not connect to PostgreSQL. Check your configuration and database server.")

finally:
    if connection is not None:
        connection.close()
        print("Database connection closed.")



### UPDATING A RECORD WITH UPSERT:

### CHECKING IF THE RECORD ALREADY EXISTS , IF DOES NOT THEN INSERTING NEW RECORD:

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

    customer = (107, "Daniel", "daniel@example.com", "Spain")

    with connection.cursor() as cursor:
        cursor.execute(
            """
            INSERT INTO public.customers
                (customer_id, customer_name, email, country)
            VALUES(%s, %s, %s, %s)
            ON CONFLICT (customer_id)
            DO UPDATE SET
                customer_name = EXCLUDED.customer_name,
                email = EXCLUDED.email,
                country = EXCLUDED.country;
            """,
            customer                                                # When a conflict occurs, EXCLUDED refers to the row you attempted to insert.                                                      
        )                                                           # "country = EXCLUDED.country" means: update the existing customer's country using the country value from the incoming row.
       

        connection.commit()                             # A database transaction groups changes together. In this example, commit() tells PostgreSQL to save the insertion permanently. 
                                                        # Without committing, the change may be rolled back when the connection closes.
        print("Insert attempted; checking the database record.")


    with connection.cursor() as cursor:
        cursor.execute(
            """
            SELECT customer_id, customer_name, email, country
            FROM public.customers
            WHERE customer_id = %s
            """,
            (customer[0],)
        )
        result = cursor.fetchone()
        print("Verified customer:",result)

       
except psycopg.OperationalError:
    print("Could not connect to PostgreSQL. Check your configuration and database server.")

finally:
    if connection is not None:
        connection.close()
        print("Database connection closed.")














