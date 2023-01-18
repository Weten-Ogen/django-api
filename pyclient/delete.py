import requests
product_id = input("What is your product id? ")
try:
    product_id = int(product_id)
except:
    product_id = None
    print(f"{product_id} is not valid")

if product_id:
    endpoint = f"http://localhost:8000/api/product/{product_id}/delete/"

    get_response = requests.delete(endpoint)

    print(get_response.status_code)