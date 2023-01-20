import requests

endpoint = "http://localhost:8000/api/product/"

get_response = requests.post(endpoint, json={'title':'Done deal'})

print(get_response.json())