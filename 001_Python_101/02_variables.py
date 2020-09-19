# A variable is a container for a value. The value can be of various types
#   - String / Integer / Float etc.,
"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
"""
# Let's define few variables here
# We can just define a variable and start assigning a value to it directly
# Python automatically will identity the type of the data


# variable to hold hostname of a switch (user defined name for this variable)
host_name = "access-switch-floor1"

# variable to hold a port number on this switch
port_number = "GigabitEthernet1/5"

# variable to hold the VLAN ID of this port
vlan_id  = 10

# Let's find out the Data Type of these variables defined above
print("Data type of host_name variable is {}".format(type(host_name)))
print("Data type of port_number variable is {}".format(type(port_number)))
print("Data type of vlan_id variable is {}".format(type(vlan_id)))

# Let's print the value of these variables
print("\n") # next line - One line spacing
print("VLAN {} is configured on {} of switch '{}'".format(vlan_id, port_number, host_name))