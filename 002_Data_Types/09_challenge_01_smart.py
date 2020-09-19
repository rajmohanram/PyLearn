"""
Challenge - 01                      

Given input:
    ip_address = "192.168.0.1"
    subnet_mask = "255.255.255.0"

Required output:                    
    ip_address_cidr = "192.168.0.1/24"

"""
# write down your code here and try to get the output required !!!
# Code Logic:
# use built-in module ipaddr to achieve the goal

import ipaddress

# ip address and mask variables
ip_address = "192.168.0.1"
subnet_mask = "255.255.255.0"
print("Subnet Mask:", subnet_mask)

# find prefix length using built-in 'ipaddress' module
# https://docs.python.org/3/library/ipaddress.html
prefix_length = ipaddress.IPv4Network("0.0.0.0/" + subnet_mask).prefixlen
print("Prefix Length:", prefix_length)

# IP address in CIDR format
print("IP address in CIDR format is {}/{}".format(ip_address, prefix_length))
