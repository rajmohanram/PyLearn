# Let's use range() to create VLAN ID list
# produces a sequence of integers from start to stop by step.

# range(start, stop, step)
# start - Optional, defaults to 0 if not specified
# stop - mandatory, last in the sequence
# step - Optional, incremental steps. default is 1 step


# create a list of VLANs using range() - Only stop value is given here
vlan_id_list = list(range(10))
print("VLAN ID list:", vlan_id_list)

# create a list of odd VLANs using range(start, stop, end) - Using step '2'
vlan_id_list = list(range(1, 10, 2))
print("Odd VLAN ID list:", vlan_id_list)

# create a list of even VLANs using range(start, stop, end) - Using step '2'
vlan_id_list = list(range(2, 10, 2))
print("Even VLAN ID list:", vlan_id_list)
