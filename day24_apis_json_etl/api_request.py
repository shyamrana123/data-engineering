import requests

#API endpoint
url = "https://jsonplaceholder.typicode.com/users"

# Send an HTTP GET request to the API
response = requests.get(url, timeout = 15)

#Check the HTTP status code
print("Status code:", response.status_code)    #response.status_code tells us whether the server responded successfully. 200 means OK.

#Raise an error if the request was unsuccessful
response.raise_for_status()

#Convert the JSON response into Python data
users = response.json()

#Inspect the returned data
print("Data type:", type(users))
print("Number of users:", len(users))

#Display the first user
print("\nFirst user:")
print(users[0])



"""Output of the above code:

Status code: 200
Data type: <class 'list'>
Number of users: 10

First user:
{'id': 1, 'name': 'Leanne Graham', 'username': 'Bret', 'email': 'Sincere@april.biz', 'address': {'street': 'Kulas Light', 'suite': 'Apt. 556', 'city': 'Gwenborough', 'zipcode': '92998-3874', 'geo': {'lat': '-37.3159', 'lng': '81.1496'}}, 'phone': '1-770-736-8031 x56442', 'website': 'hildegard.org', 'company': {'name': 'Romaguera-Crona', 'catchPhrase': 'Multi-layered client-server neural-net', 'bs': 'harness real-time e-markets'}}"""