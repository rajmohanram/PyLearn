# let us convert an integer to binary

# define a variable to hold an integer value
my_int = 10

# convert the integer to binary using built-in bin() function
# bin() - Converts an integer number to a binary string prefixed with “0b”
my_bin = bin(my_int)
print("\nBinary value of {} is {}".format(str(my_int), str(my_bin)))

# let us remove the '0b' prefix - slicing the string [2:] - omitting first 2 characters '0b'
my_bin = bin(my_int)[2:]
print("\nBinary value of {} is {}".format(str(my_int), str(my_bin)))

# let us print the result as 8 bit binary always - using zfill() built-in function
# Zeros are prepended to make a 8 bit binary
my_bin = bin(my_int)[2:].zfill(8)
print("\nBinary value of {} is {}".format(str(my_int), str(my_bin)))
