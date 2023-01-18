import requests

endpoint = "http://localhost:8000/api/product/1/update/"

data = {
    'title' : "west world",
    "price" : 5000
}
get_response = requests.put(endpoint, json = data)

print(get_response.json())