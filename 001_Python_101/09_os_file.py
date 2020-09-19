# create a file in the required directory
# Write contents to the file (overwrite mode)
# Write contents to the file (append mode)
# Read contents of the file

from pathlib import Path

# define directory and filename
BASE_DIR = Path(__file__).parents[0]
FILE_DIR = BASE_DIR / "files"
FILE_NAME = FILE_DIR / "test_file.txt"

print("Directory for the file:", FILE_DIR)
print("Filename:", FILE_NAME)


# create the directory: if it does not exist:
# Reference: https://docs.python.org/3/library/pathlib.html#pathlib.Path.mkdir
Path(FILE_DIR).mkdir(parents=True, exist_ok=True)

######## First Iteration ###################
# create the file and add Initial contents
interface1_config = """!
interface GigabitEthernet0/1
 switchport mode access
 switchport access vlan 10
!
 """

# 'w' - write mode
with open(FILE_NAME, 'w') as f:
    f.write(interface1_config)

# read and print the file content
# 'r' - read mode
with open(FILE_NAME, 'r') as f:
    file_contents = f.read()
print("File Content-1: Initial Content")
print(file_contents)

######## Second Iteration ###################
# Add contents for second interface
interface2_config = """!
interface GigabitEthernet0/2
 switchport mode access
 switchport access vlan 20
!
 """

# 'w' - write mode
with open(FILE_NAME, 'w') as f:
    f.write(interface2_config)

# read and print the file content
# 'r' - read mode
with open(FILE_NAME, 'r') as f:
    file_contents = f.read()
print("File Content-2: Content overwritten")
print(file_contents)

######## Third Iteration ###################
# Add contents for third interface
interface3_config = """!
interface GigabitEthernet0/3
 switchport mode access
 switchport access vlan 30
!
 """
# 'a' - write mode
with open(FILE_NAME, 'a') as f:
    f.write(interface3_config)

# read and print the file content
# 'r' - read mode
with open(FILE_NAME, 'r') as f:
    file_contents = f.read()
print("File Content-3: Content Appended")
print(file_contents)