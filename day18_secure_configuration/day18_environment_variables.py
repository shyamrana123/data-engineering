import os
from dotenv import load_dotenv

load_dotenv()

### 3 KEY STEPS:
# from dotenv import load_dotenv imports the function that reads .env files.
# load_dotenv() loads the values from .env into the process environment.
# os.getenv("DB_HOST") retrieves a particular value.

pipeline_mode = os.getenv("PIPELINE_MODE")
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_name = os.getenv("DB_NAME")
db_user = os.getenv("DB_USER")

### IMPORTANT: environment variables are generally returned as strings. 
# For example, os.getenv("DB_PORT") returns "5432", not the integer 5432. We'll handle conversion when we need it.

print("Pipeline mode:", pipeline_mode)
print("Database host:", db_host)
print("Database port:", db_port)
print("Database name:", db_name)
print("Database user:", db_user)

