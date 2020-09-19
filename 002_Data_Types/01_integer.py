# Numeric data type
# integer

# collect user input using built-in input() function
vlan_id = input("Enter your VLAN ID:")

# Convert the collected input to Integer data type [as input() function alway give string data type]
vlan_id = int(vlan_id)
print("Your VLAN ID is of type {}".format(type(vlan_id)))


'''
Following Arithmetic Operations are possible on Integers
--------------------------------------------------------
    +       addition
    -       subtraction
    *       multiplication
    /       division
    %       modulus
    //      floor division
    **      power
'''

# addition
print("Next VLAN ID is {}".format(vlan_id + 1))

# subtraction
print("Previous VLAN ID is {}".format(vlan_id - 1))

# try other Arithmetic operations by yourselves
'''
Following Assignment Operators
------------------------------

    =       assignment
    +=      increment & assign
    -=      decrement & assign
    *=      multiply & assign
    /=      divide & assign
    %=      modulus & assign
    //=     floor division & assign
    **=     power & assign
'''

# assignment [assigning the vlan id to other variable]
new_vlan_id = vlan_id
print("New VLAN id is {}".format(new_vlan_id))

# increment the vlan id
vlan_id += 1
print("Incremented VLAN id is {}".format(vlan_id))

# decrement the vlan  id
vlan_id -= 1
print("Incremented VLAN id is {}".format(vlan_id))

# try other Assignment operations by yourselves
