# let's look at an examples of for loop
#   - using range()
#   - if conditions
#   - bypass an iteration of for loop: continue
#   - break the for loop once and for all: break


# create an empty list
vlan_id_list = list()
last_vlan_id = 10

# range of 1 - 100 is considered with step value of 2
# escape an iteration when the value of item is Zero (0) - not a valid VLAN
# break the loop when the VLAN Id is greater than 10
# if the VLAN ID vlaue is between 1 and 10 - append the value to the list: vlan_id_list

for item in range(0, 100, 2):
    print("Value of item:", item)
    if item == 0:
        print("\tZero is not a valid VLAN ID. Skipping this iteration..")
        continue
    elif item > last_vlan_id:
        print("\tVLAN ID is greater than", last_vlan_id, ". Exiting the for loop...")
        break
    else:
        print("\tappending this to the list...")
        vlan_id_list.append(item)
    print("\tVLAN ID List:", vlan_id_list)

# print the vlan_id list created using for loop
print("\nFinal VLAN ID List:", vlan_id_list)
