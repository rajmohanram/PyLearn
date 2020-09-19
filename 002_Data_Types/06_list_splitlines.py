# We can create a list by spliting Multi-Line strings

# define a multi line string - enclosed in triple quotes
config = """interface GigabitEthernet0/1
 switchport mode access
 switchport access vlan 10
"""

# let us create a list by splitting the multi line string - config
# split() method - By default use space in the strings to split them
config_list = config.splitlines()
print(config_list)

# how do you find the VLAN of this interface
# Item at index number 2 of config_list
# split that item using default space as delimiter
# Item at index number 3 of new list - VLAN ID
vlan_id = config_list[2].split()[3]
print("VLAN ID of this port is {}".format(vlan_id))