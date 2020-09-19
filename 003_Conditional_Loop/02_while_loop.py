# let's look at an example of while loop

# define a BGP local AS number
local_as = 64520
remote_as = 64512

# check whether local_as is NOT EQUALS to remote_as
#   - execute the code block
while local_as != remote_as:
    print(local_as, " - eBGP peering with -", remote_as)
    remote_as += 1  # increment remote_as on every iteration

print("\nwhile loop terminated when the local_as is equal to remote_as")