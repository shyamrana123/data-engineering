### Retrieve for  customer:

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
   
    """with connection.cursor() as cursor:
        cursor.execute("""
            #INSERT INTO public.customers
            #    (customer_id, customer_name , email, country)
            #VALUES (%s, %s, %s, %s)             
    """
            customer                                            # Four parameter placeholders: Each placeholder receives one value from the tuple. 
                                                                    #Psycopg safely passes these values separately from the SQL statement.
        )
       
        print("Customer inserted successfully!")
    connection.commit()                                         # A database transaction groups changes together. In this example, commit() tells PostgreSQL to save the insertion permanently. 
                                                                # Without committing, the change may be rolled back when the connection closes.
    print("Transaction committed.")

    with connection.cursor() as cursor:
        cursor.execute(
            """
            #SELECT customer_id, customer_name, email, country
            #FROM public.customers
            #WHERE customer_id = %s
    """
            (104,)

        )
        result = cursor.fetchone()

        if result:
             print("Verified customer:", result)

        else:
            print("Customer was not found.")
"""
    with connection.cursor() as cursor:
        cursor.execute(
            """SELECT customer_id, customer_name, email, country
            FROM public.customers
            WHERE customer_id IN (%s, %s)
            """,
            (104, 106)
        )
        results = cursor.fetchall()
        for row in results:
            print("Verified customer:", row)
        
except psycopg.OperationalError:
    print("Could not connect to PostgreSQL. Check your configuration and database server.")

finally:
    if connection is not None:
        connection.close()
        print("Database connection closed.")


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

    customer = (106, "Sophia", "sophia@example.com", "UK")
    customer_id = customer[0]                               #We use customer[0] to obtain the ID from the tuple. This avoids typing the same ID separately in the existence check.

    with connection.cursor() as cursor:
        cursor.execute(
            """
            SELECT 1                                                
            FROM public.customers                                  
            WHERE customer_id = %s
            """,
            (customer_id,)                                   # SELECT 1 simply checks whether a matching row exists.                                                                   
        )                                                    # It doesn't retrieve the customer's name, email, or country because we don't need those details for this check.
        existing_customer = cursor.fetchone()                   
    
        if existing_customer:
            print(f"Customer ID  {customer_id} already exists. Skipping insertion.")

        else:
            cursor.execute(
                """
                INSERT INTO public.customers
                    (customer_id, customer_name, email, country)
                VALUES(%s, %s, %s, %s)
                """,
                customer
            )

            connection.commit()                             # A database transaction groups changes together. In this example, commit() tells PostgreSQL to save the insertion permanently. 
                                                            # Without committing, the change may be rolled back when the connection closes.
            print("Customer inserted successfully.")


    with connection.cursor() as cursor:
        cursor.execute(
            """
            SELECT customer_id, customer_name, email, country
            FROM public.customers
            WHERE customer_id = %s
            """,
            (customer_id,)
        )
        result = cursor.fetchone()
        print("Verified customer:",result)

       
except psycopg.OperationalError:
    print("Could not connect to PostgreSQL. Check your configuration and database server.")

finally:
    if connection is not None:
        connection.close()
        print("Database connection closed.")







