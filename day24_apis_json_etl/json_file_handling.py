import json

customers = [
    {
        "customer_id": 201,
        "customer_name": "Alex",
        "country": "Portugal"
    },
    {
        "customer_id": 202,
        "customer_name": "Maria",
        "country": "Spain"
    },
    {
        "customer_id": 203,
        "customer_name": "Raj",
        "country": "Nepal"
    }
]

#Write Python data into a JSON file:

with open("day24_apis_json_etl/customers.json", "w", encoding= "utf-8") as file:
    json.dump(customers, file , indent = 4)

print("Customer data saved successfully.")

#Read the JSON file.

with open("day24_apis_json_etl/customers.json", "r", encoding = "utf-8") as file:
    loaded_customers = json.load(file)

print("\nLoaded customers:")
print(loaded_customers)

print("\nCustomer names:")
for customer in loaded_customers:
    print(customer["customer_name"])
