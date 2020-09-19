# Jinja2 - Render using Template file Example
# create and render the template (using Template file)

from jinja2 import Environment, FileSystemLoader
from pprint import pprint

# input parameters
hostname = 'router-01'
domain = {'name':'cisco.com', 'servers':['8.8.8.8', '8.8.4.4']}
vlans_dict = {'123': 'TEST-VLAN-123', '234': 'TEST-VLAN-234', '345': 'TEST-VLAN-345'}
iface_dict = {'ifname':'Ethernet0/0', 'desc':'Test interface description', 'ipaddr':'192.168.1.1', 'mask':'255.255.255.0', 'ospf': {'configured':'no'}}
bgp_dict = {'localas':'200', 'rid':'10.10.10.10', 'nei':'192.168.1.2', 'remoteas':'300', 'updatesrc':'Loopback0'}

# find and load the template
file_loader = FileSystemLoader('.')
env = Environment(loader=file_loader)

# get the Jinja2 template
template = env.get_template('104_config.j2')

# Render the output from the template
result = template.render(hostname=hostname, domain=domain, vlans = vlans_dict, iface = iface_dict, bgp = bgp_dict)

# Print the output
print(result)

