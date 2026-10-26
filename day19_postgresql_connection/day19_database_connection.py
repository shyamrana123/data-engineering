"""import os
import psycopg
from dotenv import load_dotenv

load_dotenv()

db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_name = os.getenv("DB_NAME")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")

### FUNCTIONS OF THE ABOVE COMMANDS:
# import psycopg gives Python the PostgreSQL driver.
# load_dotenv() loads the settings from .env.
# os.getenv() retrieves each setting by name.

connection = None

try:
    connection = psycopg.connect(
        host = db_host,
        port = db_port,
        dbname = db_name,
        user = db_user,
        password = db_password
    )

    print("Successfully connected to PostgreSQL!")

except psycopg.OperationalError:
    print("Could not connect to PostgreSQL. Check your configuration and data server.")

finally:
    if connection is not None:
        connection.close()
        print("Database connection closed.")

### Understanding the important concepts:
# psycopg.connect() attempts to establish a connection using your settings.
# try and except allow the program to handle a connection failure without displaying the full error message to the user.
# finally runs whether the connection succeeds or the handled exception occurs. If a connection was established, we close it to release the database resource.
# The initial connection = None lets us check whether a connection was successfully assigned before trying to close it."""




"""import os
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
        cursor.execute("""
          #  SELECT table_name
          #  FROM information_schema.tables
          #  WHERE table_schema = 'public'
          #  ORDER BY table_name;
""")

        #result = cursor.fetchone()         #fetchone() returns only one row, even if the query finds several tables. 
                                            # For now, that's intentional—we're practising how to retrieve results.
        
        results = cursor.fetchall()         #fetchall() retrieves every row returned by PostgreSQL.
                                            #if results: checks whether the list contains any rows.
                                            #for row in results: loops through the rows one by one.
                                            #row[0] prints the table name from each row.

        if results:
            print("Tables in the public schema:")

            for row in results:
                print(row[0])
        else:
            print("No tables found in the public schema.")
       

except psycopg.OperationalError:
    print("Could not connect to PostgreSQL. Check your configuration and database server.")

finally:
    if connection is not None:
        connection.close()
        print("Database connection closed.")
"""

### NOTES:
# connection.cursor(): Creates a cursor, which lets you execute SQL statements through the database connection.
# cursor.execute(...): Sends the SQL query to PostgreSQL for execution.
# cursor.fetchone(): Retrieves tehe next result row. Here, our query returns one row with three columns.
# result[0], result[1] result[2]: Access the database name, connected user, and PostgreSQL version from that row.
# The "with" statement also ensures that the cursor is closed when the block finishes.

"""
PARAMETERIZED QUERIES: (Parameterized queries help protect your database from SQL injection and handle values safely.)

order_id = 101

with connection.cursor() as cursor:
    cursor.execute(
        "SELECT * FROM orders WHERE order_id = %s",
        (order_id,)
    )

    result = cursor.fetchone()
    print(result)
    
# %s is the placeholder Psycopg uses for the parameter value. You supply the value separately when calling cursor.execute().
# (order_id,) is a one-item tuple. The comma is necessary in Python.

# SQL injection protection: the parameter is treated as a value, rather than being interpreted as part of the SQL command.
# Safe value handling: Psycopg handles the value using the database driver's parameter-binding mechanism.
    
"""

### INSPECT TABLE COLUMNS

"""import os
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
        cursor.execute("""
#            SELECT 
#                table_schema, 
#                table_name,
#                column_name,
#                data_type
#            FROM information_schema.columns
#|            WHERE table_name = 'customers'
#            ORDER BY table_schema, ordinal_position;
""")

        
        
        results = cursor.fetchall()         #fetchall() retrieves every row returned by PostgreSQL.
                                            #if results: checks whether the list contains any rows.
                                            #for row in results: loops through the rows one by one.
                                            #row[0] prints the table name from each row.

        if results:
            

            for row in results:
                print(f"Schema: {row[0]},"
                      f"Table: {row[1]},"
                      f"Column: {row[2]},"
                      f"Data type: {row[3]}")
        else:
            print("No columns found for any table named customers.")
       

except psycopg.OperationalError:
    print("Could not connect to PostgreSQL. Check your configuration and database server.")

finally:
    if connection is not None:
        connection.close()
        print("Database connection closed.")
"""
### OUTPUT OF ABOVE CODE:
"""Successfully connected to PostgreSQL
Schema: public,Table: customers,Column: customer_id,Data type: integer
Schema: public,Table: customers,Column: customer_name,Data type: character varying
Schema: public,Table: customers,Column: email,Data type: character varying
Schema: public,Table: customers,Column: country,Data type: character varying
Database connection closed."""


#QUERING FOR customer_id= 101

"""import os
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

    customer_id = 102

    with connection.cursor() as cursor:
        cursor.execute("""
#            SELECT customer_id, customer_name, email,country
#            FROM public.customers
#           WHERE customer_id = %s;
""",
            (customer_id,)
        )

        
        
        result = cursor.fetchone()      # customer_id = 101 sets the ID we want to search for.
                                        # %s is the placeholder for the ID.
                                        # (customer_id,) passes the ID as a one-item tuple.
                                        # fetchone() retrieves the matching row, or returns None if no row matches.
                                        # The if result condition prevents the script from trying to print columns when no customer exists.

        if result:
            print("Customer ID:", result[0])
            print("Name:", result[1])
            print("Email:", result[2])
            print("Country:", result[3])

        else:
            print("No customer found with that ID.")
       

except psycopg.OperationalError:
    print("Could not connect to PostgreSQL. Check your configuration and database server.")

finally:
    if connection is not None:
        connection.close()
        print("Database connection closed.")
"""


### Retrieve for multiple customers:



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

    country = "Nepal"   

    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT customer_id, customer_name, email, country
            FROM public.customers
           WHERE country = %s
           ORDER BY customer_id
        """,
            (country,)
        )
       
        results = cursor.fetchall()     

        if results:
            for row in results:
                print(row)      

        else:
            print(f"No customers found in {country}.") 

except psycopg.OperationalError:
    print("Could not connect to PostgreSQL. Check your configuration and database server.")

finally:
    if connection is not None:
        connection.close()
        print("Database connection closed.")







