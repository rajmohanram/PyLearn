import requests
import json
from pprint import pprint

base_url = "http://127.0.0.1:8000/inv/api"
endpoint = input("API Endpoint:")
url = base_url + "/" + endpoint + "/"
print(url)

response = requests.get(url=url)

print(f'\nHTTP Response status code: {response.status_code}\n')

if response.status_code == 200:
    pprint(response.headers)
    data = response.json()
    print(json.dumps(data, indent=4, sort_keys=True))
