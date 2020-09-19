# functions: Positional argument
import ipaddress
from pprint import pprint


# use this function whenever an IP address needs to be analyzed - Code Reuse
# positional arguments
#   - IP address
#   - Prefix Length
# Process the Inputs given and find the following
#   - Netmask / Network / IP Address Type
def analyze_ip(ip, prefix_len):
    """ Function documentation string: Function to analyze the given IP and prefix length."""

    # concatenate ip and prefix length. Example: 10.10.10.100/24
    iface_ip = ip + "/" + prefix_len
    # create a dictionary 'ip_result' to capture all results
    ip_result = dict()

    # Use built-in 'ipaddress' library to analyze the IP addess
    interface = ipaddress.IPv4Interface(iface_ip)

    ip_result['ipMask'] = interface.with_netmask    # find netmaks
    ip_result['ipNetwork'] = interface.network      # find the network

    if interface.is_global:                         # check the IP address type
        ip_type = "global"
    elif interface.is_private:
        ip_type = "private"
    else:
        ip_type = "unknown"
    ip_result['ipType'] = ip_type

    # return the result
    return ip_result


# main program - program starting point
if __name__ == "__main__":
    # IP address of an interface in CIDR format
    interface_ip  = input("Enter your IP Address:")
    cidr = input("Enter the CIDR / Prefix Length:")

    # call the function by its name - The function returns a result
    # Positional argument
    #   - first argument - IP address
    #   - second argument - cidr
    result = analyze_ip(interface_ip, cidr)

    # print the returned value from the function
    pprint(result)