# We can create a list by spliting strings

# define a single line string
config = "interface GigabitEthernet0/1"

# let us create a list by splitting the string - config
# split() method - By default use space in the strings to split them
config_list = config.split()
print(config_list)

# Let's print the interface name - Item at the index 1 of the config_list
print("Interface name is {}\n".format(config_list[1]))

# Let's now split a string with user specified delimiter - '.'
ip_address = "192.168.1.100"
ip_address_list = ip_address.split('.')
print(ip_address_list)
print("Last octet of the IP address {} is {}".format(ip_address, ip_address_list[-1]))

# Let's join the items in a list to a string back
new_ip_address = '.'.join(ip_address_list)
print("\nIP address is {}".format(new_ip_address))

