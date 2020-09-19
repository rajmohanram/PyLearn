import requests
import json
from pprint import pprint


# user input
endpoint = input("API Endpoint:")

base_url = "http://127.0.0.1:8000/inv/api"
url = base_url + "/" + endpoint + "/"
print(url)

headers = {'content-type': 'application/json'}


# Payload for POST
location_payload = {
    "location": "Mumbai"
    }

vendor_payload = {
    "vendor": "Quanta"
    }

device_payload = {
    "hostname": "mum-5-rt-1",
    "location": 20,
    "vendor": 16,
    "management_ip": "192.168.255.70"
}

# choosing the payload
if endpoint == "locations":
    payload = location_payload
elif endpoint == "vendors":
    payload = vendor_payload
elif endpoint == "devices":
    payload = device_payload
else:
    payload = None

response = requests.post(url=url, data=json.dumps(payload), headers=headers)

print(f'\nHTTP Response status code: {response.status_code}\n')

if response.status_code == 201:
    pprint(response.headers)
    data = response.json()
    print(json.dumps(data, indent=4, sort_keys=True))