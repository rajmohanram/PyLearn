# let's look at an examples of for loop
#   - using a list

# define an interfaces list - items: interface names
interfaces = ["GigabitEthernet0/1", "GigabitEthernet0/2", "GigabitEthernet1/1", "GigabitEthernet1/2", "GigabitEthernet3/3"]

# loop through items in the list: interfaces
# find the host facing ports: if the interface name starts with "GigabitEtherent0/"
# find the Uplink ports: if the interface name starts with "GigabitEtherent1/"
# Report error if anything else:

for item in interfaces:
    if item.startswith("GigabitEthernet0/"):
        print(item, ": Host Facing port")
    elif item.startswith("GigabitEthernet1/"):
        print(item, ": Uplink port")
    else:
        print(item, ": Error ! Unknown Port")
