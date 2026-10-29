### CODE FOR DELETING RECORD BEFORE INSERTING TEMPORARY BECAUSE THE CODE TO INSERT CAUSES ERROR WHEN TRYING TO RUN TWO TIMES:
### (TRYING NOT TO DELETE THE CODES)
### UPDATING A RECORD:

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
            SET country= %s
            WHERE customer_id = %s
            """,
            ("Portugal",107)                                                                                      
        )              

        print(f"Rows updated: {cursor.rowcount}")

    connection.commit()
    print("Update committed.")

    ### UPDATE public.customers tells PostgreSQL which table to modify.
    ### SET country = %s specifies the column and new value
    ### WHERE customer_id = %s limits the change to Daniels record.
    ### cursor.rowcount reports how many rows the command affected.####
    ### connection.commit() saves the changes permanently


    with connection.cursor() as cursor:
        cursor.execute(
            """
            SELECT customer_id, customer_name, email, country
            FROM public.customers
            WHERE customer_id = %s
            """,
            (107,)
        )
        result = cursor.fetchone()
        print("Verified customer:",result)

       
except psycopg.OperationalError:
    print("Could not connect to PostgreSQL. Check your configuration and database server.")

finally:
    if connection is not None:
        connection.close() 
        print("Database connection closed.")

### DELETING A RECORD:

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

    test_customer = (108, "Test Customer", "test108@example.com", "Portugal")


    with connection.cursor() as cursor:
        cursor.execute(
            """
            DELETE FROM public.customers
            WHERE customer_id = %s
            """,
            (108,)                                                                               
        )              

        print(f"Rows deleted: {cursor.rowcount}")

    connection.commit()
    print("Deletion committed.")
     # DELETE FROM public.customers identifies the table.
     #WHERE customer_id = %s restricts teh deletion to customer 108.
     #(108,) passes the ID as a one-item tuple.
     # cursor.rowcoutn tells us how many rows were deleted.
     #connection.commit() saves teh deletion.
    
    #NEVER RUN A DELETE STATEMENT WITHOUT CHECKING ITS "WHERE" CONDITION FIRST. WITHOUT THAT CONDITION EVERY ROW IN THE TABLE CAN GET DELETED.

    
    with connection.cursor() as cursor:
        cursor.execute(
            """
            SELECT customer_id, customer_name, email, country
            FROM public.customers
            WHERE customer_id = %s
            """,
            (test_customer[0],)
        )
        result = cursor.fetchone()

        if result is None:
            print("Verified: Customer 108 no longer exists.")
        else:
            print("Customer still exists:", result)

       
except psycopg.OperationalError:
    print("Could not connect to PostgreSQL. Check your configuration and database server.")

finally:
    if connection is not None:
        connection.close() 
        print("Database connection closed.")





### INSERTING TEMPORARY CUSTOMER RECORD

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

    test_customer = (108, "Test Customer", "test108@example.com", "Portugal")


    with connection.cursor() as cursor:
        cursor.execute(
            """
            INSERT INTO public.customers
                (customer_id, customer_name, email, country)
            VALUES (%s, %s, %s, %s)
            
            """,
            test_customer                                                                               
        )              

    connection.commit()
    print("Temporary test customer inserted.")

    
    with connection.cursor() as cursor:
        cursor.execute(
            """
            SELECT customer_id, customer_name, email, country
            FROM public.customers
            WHERE customer_id = %s
            """,
            (test_customer[0],)
        )
        result = cursor.fetchone()
        print("Test customer:",result)

       
except psycopg.OperationalError:
    print("Could not connect to PostgreSQL. Check your configuration and database server.")

finally:
    if connection is not None:
        connection.close() 
        print("Database connection closed.")



























