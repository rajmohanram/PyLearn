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
# convert Subnet mask to binary
# count the number of '1' from left - This is the prefix length

# ip address and mask variables
ip_address = "192.168.0.1"
subnet_mask = "255.255.255.0"
print("Subnet Mask:", subnet_mask)

# create the octet list - split the string 'subnet_mask' into 4 octets : delimiter '.'
octets_list = subnet_mask.split('.')
print("List of items (string):", octets_list)

# All 4 items in the list is of type 'string'
# Only integers can be converted into binary using bin() function
# convert all the 4 items in the list to integer - using built-in function map()
octets_list = list(map(int, octets_list))
print("List of items (integer):", octets_list)

# convert each item in the list to binary - Using list comprehension
binary_list = [bin(i)[2:].zfill(8) for i in octets_list]
print("List of items (binary):", binary_list)

# Join all the items in the list to form a string
binary_string = "".join(binary_list)
print("Binary string:", binary_string)

# prefix length - count the number of '1' in binary_string
prefix_length = binary_string.count('1')
print("Prefix Length:", prefix_length)

# IP address in CIDR format
print("IP address in CIDR format is {}/{}".format(ip_address, prefix_length))
