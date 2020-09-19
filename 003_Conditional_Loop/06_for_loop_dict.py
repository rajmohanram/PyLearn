# let's look at an examples of for loop
#   - using a dictionary

# define an interfaces dictionary - items: interface names
interface = {'name': 'GigabitEthernet0/2', 'mode': 'trunk', 'vlan': [10, 20, 30], 'portfast_enabled': False}

# let's check the items() method for dictionary
interface_items = interface.items()
print("Dictionary items:", interface_items)
print("\t---> items() method produce Tuples in a list")

# loop through items in the list
print("\n---> Iterating through dictionary...")
for key, value in interface.items():
    print("key:", key, " - value:", value)

