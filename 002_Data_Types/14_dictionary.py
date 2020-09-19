# dictionaries or hash
# key:value pairs
# vlaue - can be any data type [integer, float, string, list or another dictionary]
# enclosed within curly braces
from pprint import pprint


# initialize a dictionary
interface_1 = {}
print("Interface-1 configuration:", interface_1)
# another way: interface_1 = dict()
print("Type of Interface-1", type(interface_1))


# load values to interface_1 dictionary
interface_1['name'] = "GigabitEthernet0/1"
interface_1['mode'] = "access"
interface_1['vlan'] = 10
interface_1['portfast_enabled'] = True
print("\nInterface-1 dictionary:", interface_1)

# load values to interface_2 dictionary
interface_2 = {'name': 'GigabitEthernet0/2', 'mode': 'trunk', 'vlan': [10, 20, 30], 'portfast_enabled': False}
print("Interface-2 dictionary:", interface_2)

# Access the values from dictionary - use key name to access its value
# two different methods to get the value of a key
print("\nInterface", interface_1['name'], "operates in", interface_1['mode'], "mode.")
print("Interface", interface_2.get('name'), "operates in", interface_2.get('mode'), "mode.")

# Operations that dictionary support: https://docs.python.org/3/library/stdtypes.html#mapping-types-dict

# zip 3 lists to create a dictionary
key_list = ["name", "mode", "vlan", "portfast_enabled"]
value_list = ["GigabitEthernet0/3", "access", "30", "True"]
interface_3 = dict(zip(key_list, value_list))
print("\nInterface-3 dictionary:", interface_3)

# add another key to the existing dictionary
interface_3["status"] = "up"
print("Interface-3 dictionary:", interface_3)

# add another key - using update method
# dictionaries must have unique keys - if same key is added again - it replaces/overwrites the existing key:value
interface_3.update({"status": "down", "portfast_enabled": "False"})
print("Interface-3 dictionary:", interface_3)

# delete a key:value
interface_3.pop('status')
print("Interface-3 dictionary:", interface_3)

# get only the keys of a dictionary
dict_keys = interface_3.keys()
print("Interface-3 dictionary keys:", dict_keys)

# get only the values of a dictionary
dict_values = interface_3.values()
print("Interface-3 dictionary values:", dict_values)

# copy and create new dictionary
interface_4 = interface_3.copy()
interface_4.update({'name': 'GigabitEthernet0/4', 'vlan': '40'})
print("\nInterface-4 dictionary:", interface_4)

# clear the dictionary
interface_4.clear()
print("Interface-4 dictionary:", interface_4)

# nested dictionary - let's use pretty print (pprint) to print nested dict
interfaces = {"iface1": interface_1, "iface2": interface_2, "iface3": interface_3, "iface4": interface_4}
print("\n Nested Interfaces Dict:")
pprint(interfaces)

# merging two dictionary
mode_access = {'mode': 'access', 'vlan': '', 'portfast_enabled': True }
mode_trunk = {'mode': 'trunk', 'vlan': [], 'portfast_enabled': False }
interface_5 = {'name': 'GigabitEthernet0/5'}

# merge dictionaries
interface_5 = dict(**interface_5, **mode_access)
interface_5['vlan'] = 50
print("\n Dict created by merging 2 dictionaries:", interface_5)


# follow-ups: using conditionals
#   Check if a key exist in a dict
#   Check if a dict is empty
#   Check the length of a dict
#   Iterate over a dict find the key:value pairs
#