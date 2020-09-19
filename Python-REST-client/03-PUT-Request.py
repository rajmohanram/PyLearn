import requests
import json
from pprint import pprint


# user input
endpoint = input("API Endpoint:")
resource_id = input("Resource Id:")

base_url = "http://127.0.0.1:8000/inv/api"
url = base_url + "/" + endpoint + "/" + resource_id + "/"
print(url)

headers = {'content-type': 'application/json'}


# Payload for POST
location_payload = {
    "location": "Chennai Beach"
    }

vendor_payload = {
    "vendor": "Cisco Systems"
    }

device_payload = {
    "hostname": "kol5-5-rt-1",
    "location": 12,
    "vendor": 10,
    "management_ip": "192.168.255.90"
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

response = requests.put(url=url, data=json.dumps(payload), headers=headers)

print(f'\nHTTP Response status code: {response.status_code}\n')

if response.status_code == 200:
    pprint(response.headers)
    data = response.json()
    print(json.dumps(data, indent=4, sort_keys=True))