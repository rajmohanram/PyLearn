"""
If/ Else conditions are used to decide to do something based on something being true or false
let's look at an example for 'if' conditional
Comparison Operators (==, !=, >, <, >=, <=) - Used to compare values
Logical operators (and, or, not) - Used to combine conditional statements
Membership Operators (in, not in) - Membership operators are used to test if a sequence is presented in an object
Identity Operators (is, is not) - Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:
"""

# single = is used for assigning value to a variable
interface = {"name": "GigabitEthernet0/1", "vlanId": 10}

# add "mode" to interface dictionary
# change this value to check the variation of code output
#   - access
#   - trunk
#   - any random string
#   - comment out the mode
interface['mode'] = 'access'

# check if interface dict has a key named - mod
# check if the mode's value is "access"
#   if it is access mode, enable STP portfast
# check if the mode's value is "trunk"
#   if it is trunk mode, disable STP portfast
# if the mode is neither access nor trunk, report error

if 'mode' in interface:
    if interface['mode'] == "access":
        interface['portfast'] = 'enabled'
    elif interface['mode'] == "trunk":
        interface['portfast'] = 'disabled'
    else:
        print("\nError: Unknown port mode. Exiting program...")
        exit()
else:
    print("\nInterface mode is not defined in the dictionary", interface)
    exit()

# print the modified interface dictionary
print("\nInterface dictionary:", interface)
