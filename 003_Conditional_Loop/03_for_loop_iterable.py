# 'for' is used to loop through any iterables:
#   - String (single or multiline)
#   - Range
#   - Lists
#   - Dictionary

# Loop through Strings
interface_name = "GigabitEtherent1/1"
# letter    - user defined (can be anything meaningful):
#           - each letter in 'interface_name' will be considered for each iteration
# ":" - MUST as the end of 'for' statement
# all codes within 'for' loop must be indented at same level: single TAB
print("\n--->Letters in the Interface Name:")
for letter in interface_name:
    print(letter)

# Loop through range(0, 10)
#   - range of numbers from 0 to 9, default step is 1
print("\n--->Numbers in the range from 0 t0 10:")
for number in range(0, 10):
    print(number)

# Loop through a list
vlan_id = [10, 11, 12, 14, 15, 17]
print("\n--->VLAN Ids in the list:")
for vlan in vlan_id:
    print(vlan)

# Loop through a dictionary
interface = {'name': 'GigabitEthernet0/2', 'mode': 'access', 'vlan': 10, 'portfast_enabled': True}
print("\n--->Items (keys) in Interface Dictionary:")
# This will get you only the Dict Keys
for item in interface:
    print(item)
# To get both  key and value: use items() method on dictionary
print("\n--->Items (keys & values) in Interface Dictionary:")
for key, value in interface.items():
    print(key, "=", value)