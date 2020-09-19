# texts are handles as string

# single line text
interface = "interface GigabitEthernet0/1"
print("Your text:", interface)
print("Length of your text:", len(interface), "characters.")
print("Interface Number:", interface[-3:])
print("Upper case Interface:", interface.upper())
print("Lower case Interface:", interface.lower())

# multi line text
interface_config = """
!
interface GigabitEthernet0/1
 switchport mode access
 switchport acces vlan 10
 spanning-tree portfast
 !
"""
print("\nYour multi-line text:", interface_config)

# convert text to list - each line becomes an item in the list
interface_config_list = interface_config.splitlines()
print("Text to list:", interface_config_list)

# find the mode of the port
# get the 4tbh element in the list
# split it again
# get the 3rd element
interface_mode = interface_config_list[3].split()[2]
print("Port mode:", interface_mode)

