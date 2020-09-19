# Task - Convert an IPv4 address to equivalent binary

ip_address = "10.10.10.100"
print(ip_address)
# split the string into 4 octets : delimiter '.'
octets = ip_address.split('.')
print(octets)

# convert each octet to integer
first_octet = int(octets[0])
second_octet = int(octets[1])
third_octet = int(octets[2])
fourth_octet = int(octets[3])

# refer to 02_integer_to_binary.py exercise
first_octet_binary = bin(first_octet)[2:].zfill(8)
second_octet_binary = bin(second_octet)[2:].zfill(8)
third_octet_binary = bin(third_octet)[2:].zfill(8)
fourth_octet_binary = bin(fourth_octet)[2:].zfill(8)

# create a binary list and populate the items
binary_list = [first_octet_binary, second_octet_binary, third_octet_binary, fourth_octet_binary]
print(binary_list)

# jon the binary_list using '.' as delimiter
ip_address_binary = '.'.join(binary_list)
print(ip_address_binary)
