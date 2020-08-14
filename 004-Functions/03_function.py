# functions: Positional argument
import ipaddress
from pprint import pprint


#  Input to functions - arguments - parameters within the brackets/paranthesis
#   - positional argument - required argument
#       func(ipaddr, pfx_len) - 2 arguments MUST be passed while calling this function
#   - keyword argument
#       func(ipaddr, pfx_len="24")
#           - ipaddr - required argument (must always come before named arguments)
#           - pfx_len - optional named argument (default value = 24)
#   .
#   func(*args, **kwargs)
#       - *args - arbitrary number of positional argument
#           - unpacked as tuple of all argument
#       - *kwargs - arbitrary number of keyword argument
#           - unpacked as dictionary of all keyword args
#       - student_info(*courses, **info)
#           - courses - list
#           - info - dictionary
#




# use this function whenever an IP address needs to be analyzed - Code Reuse
# positional arguments
#   - IP address
#   - Prefix Length
# Process the Inputs give and find the following
#   - IP address / Netmask / Network / IP Address Type
def analyze_ip(ip, prefix_len):
    """ Function documentation string:
    Function to anlayze the given IP and prefix length."""

    # concatenate ip and prefix length. Example: 10.10.10.100/24
    iface_ip = ip + "/" + prefix_len
    # create a dictionary 'ip_result' to capture all results
    ip_result = dict()

    # Use built-in 'ipaddress' library to analyze the IP addess
    interface = ipaddress.IPv4Interface(iface_ip)
    ip_result['ipAddress'] = interface.ip
    ip_result['ipMask'] = interface.with_netmask
    ip_result['ipNetwork'] = interface.network
    # check the type of IP address
    if interface.is_global:
        ip_type = "global"
    elif interface.is_private:
        ip_type = "private"
    else:
        ip_type = "unknown"
    ip_result['ipType'] = ip_type

    # return the result
    return ip_result


# main program
if __name__ == "__main__":
    # IP address of an interface in CIDR format
    interface_ip  = input("Enter your IP Address:")
    cidr = input("Enter the CIDR / Prefix Length:")

    # call the function by its name
    # Positional argument
    #   - first argument - IP address
    #   - second argument - cidr
    result = analyze_ip(interface_ip, cidr)

    # print the returned value from the function
    pprint(result)