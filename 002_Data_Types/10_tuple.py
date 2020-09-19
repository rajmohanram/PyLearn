# tuple

# tuple of vlan_id
vlan_id = (10, 12, 14, 16)
print("VLAN ID tuple:", vlan_id)
print("Type of VLAN ID is:", type(vlan_id))

# access tuple elements
print("Your VLAN ID is:", vlan_id[2])

# NO add / remove possible on tuple elements - IMMUTABLE !!!

# a way to extend the tuple
vlan_id_set1 = (10, 12, 14, 16)
vlan_id_set2 = (11, 13, 15, 17)

vlan_id = vlan_id_set1 + vlan_id_set2
print("VLAN ID tuple:", vlan_id)
