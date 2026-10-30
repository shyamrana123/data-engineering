import json

json_data = """
{
    "customer_id":201,
    "customer_name": "Alex",
    "country": "Portugal",
    "active": true
}"""

#Convert JSON string into a python dictionary:

customer = json.loads(json_data)

print("Customer data:", customer)
print("Data type:", type(customer))

#Access individual values:

print("Customer ID:", customer["customer_id"])
print("Customer name:", customer["customer_name"])
print("Country:", customer["country"])

# Modify the customer information:

customer["country"] = "Spain"

#Convert the Python dictionary back into JSON.

json_output = json.dumps(customer, indent = 4)

print("Updated JSON:")
print(json_output)


###NOTES:
#1. json.loads() converted the JSON string into a Python dictionary (dict).
#2. JSON's true became Python's True (JSON uses lowercase true; Python uses uppercase True).
#3. You accessed individual values using dictionary keys, such as customer["customer_id"].
#4. You changed the country from Portugal to Spain.
#5. json.dumps(customer, indent=4) converted the updated dictionary back into readable JSON.