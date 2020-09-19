import requests
import json
from pprint import pprint


# user input
endpoint = input("API Endpoint:")
resource_id = input("Resource Id:")

base_url = "http://127.0.0.1:8000/inv/api"
url = base_url + "/" + endpoint + "/" + resource_id + "/"
print(url)


response = requests.delete(url=url)

print(f'\nHTTP Response status code: {response.status_code}\n')

if response.status_code == 204:
    pprint(response.headers)
    data = response.text
    print(data)
