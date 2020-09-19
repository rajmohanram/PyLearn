#
from pathlib import Path

# __file__ : special variable to represent this file on which we are working
path_to_this_file = Path(__file__)
print("Path of this Python file:", path_to_this_file)

# Let's find the parent folder of this file
parent_of_this_file = Path(__file__).parent
print("Parent folder of this Python file:", parent_of_this_file)

# Let's find the parent folder of this file - Another variation using "parents"
parent_of_this_file = Path(__file__).parents[0]
print("Parent folder of this Python file:", parent_of_this_file)

# Let's find the Grandparent :) of this file
grandparent_of_this_file = Path(__file__).parents[1]
print("Grandparent folder of this Python file:", grandparent_of_this_file)

# This way we can use Path().parents[n] to find any path relative to this file
# Use case:
#   If we need to read from / write to a file in a specific location,
#       we can use the relative path found by these methods
