import requests
from time import sleep

for i in range (8000, 8005):
    try:
        response = requests.get(f"http://192.168.128.128:{i}", timeout=0.5)
    except requests.exceptions.ConnectTimeout:
        continue


