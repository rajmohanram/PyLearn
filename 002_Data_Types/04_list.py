# Let's create a list of VLANs configured on a swtich
# A list may contain different types of data (int, str, etc.,)
vlan_id_list = [10, 11, '12', '13', '14']

# print the first VLAN ID in the list
print("\nVLAN ID List is {}".format(vlan_id_list))
print("First VLAN ID in the list is {}".format(vlan_id_list[0]))
print("Last VLAN ID in the list is {}".format(vlan_id_list[-1]))

# list slicing
print("First three VLAN IDs in the list is {}".format(vlan_id_list[:3]))
print("VLAN IDs after third element in the list is {}".format(vlan_id_list[3:]))


# list of MTU of four interfaces in the device
mtu_list = [1500, 1400, 9100, 1300]
print("\nMTU List is {}".format(mtu_list))
print("Sorted MTU List (ascending) is {}".format(sorted(mtu_list)))
print("Lowest MTU among the four interfaces is {}".format(min(mtu_list)))
print("Highest MTU among the four interfaces is {}".format(max(mtu_list)))

# define an interface as a list [interface_name, mode, vlan]
access_port = ['GigabitEthernet0/1', 'ACCESS', 10]
print("\n{} is operating in {} mode and VLAN {} is allowed on this interface".format(access_port[0], access_port[1], access_port[2]))

# nested list - one of the element of your list can be an another list - "allowed vlans int the trun port"
trunk_port = ['GigabitEthernet1/1', 'TRUNK', [10,20,30]]
print("\n{} is operating in {} mode and VLANs {} is allowed on this interface".format(trunk_port[0], trunk_port[1], trunk_port[2]))


# initiate an empty list for holding VLAN IDs
vlan_id_list = list()
print("\nVLAN ID list is {} empty now".format(vlan_id_list))

# add an element manually to the list
vlan_id_list = [10]

# add a VLAN to the list - append method - always adds the new element to the next position (index) of the list
vlan_id_list.append(12)
print("VLAN ID list is {}".format(vlan_id_list))

# add a VLAN to the list - insert method - specify the index on which to add this element
vlan_id_list.insert(1, 11)
print("VLAN ID list is {}".format(vlan_id_list))

# add VLANs from other list - Extending the List (vlan_id_list) from another list (vlan_id_tmp_list)
vlan_id_tmp_list = [13, 14, 15, 16, 17, 16, 17]
vlan_id_list.extend(vlan_id_tmp_list)
print("VLAN ID list is {}".format(vlan_id_list))

# remove an element from the list - remove by value: first occurrence of the matched elements will be removed
vlan_id_list.remove(17)
print("VLAN ID list is {}".format(vlan_id_list))

# remove an element from the list - remove by index position: elements at this index will be removed
vlan_id_list.pop(-3)
print("VLAN ID list is {}".format(vlan_id_list))

# find the index of an element
index_value = vlan_id_list.index(13)
print("\nIndex value of VLAN 13 in the list is {}\n".format(index_value))

# List is an Iterator. Iteration - loop through !!! do not worry much about the for loop now !!!
for vlan_id in vlan_id_list:
    print(vlan_id)

# The example list can go into pages
# Explore yourselves with other methods available for Lists
# https://docs.python.org/3/tutorial/datastructures.html


