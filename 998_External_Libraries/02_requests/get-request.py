import requests

r = requests.get('http://ec2-52-64-182-247.ap-southeast-2.compute.amazonaws.com/check.php')
print(r.status_code)
web_server = r.json()['name']
print(web_server)