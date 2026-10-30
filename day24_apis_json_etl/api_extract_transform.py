import requests
import json

url = "https://jsonplaceholder.typicode.com/users"

#EXTRACT: Retrieve data from the API.

response = requests.get(url, timeout = 15)
response.raise_for_status()

users = response.json()

print("Extracted records:", len(users))

#TRANSFORM: Select the fields we need.

cleaned_users = []

for user in users:
    customer = {
        "customer_id": user["id"],
        "customer_name": user["name"],
        "email":user["email"],
        "city": user["address"]["city"]
    }

    cleaned_users.append(customer)

#LOAD: Save transformed data into a JSON file.

output_file = "day24_apis_json_etl/cleaned_customers.json"

with open(output_file, "w", encoding = "utf-8") as file:
    json.dump(cleaned_users, file, indent = 4)

print("Transformed records:", len(cleaned_users))
print("Data saved to:", output_file)

print("\nFirst transformed customer:")
print(cleaned_users[0])