from dns_resover import query_dns
import requests

dns_name = 'www.cmcloudlab556.info'
response = query_dns(dns_name)
print(f'DNS response for {dns_name} is {response}')
ip_list = response[dns_name+'.']
#print(ip_list)

ip =ip_list[0]
r = requests.get(f'http://{ip}/check.php')
#print(r.status_code)
web_server = r.json()['name']
print(f'HTTP Response from {ip} is {web_server}')