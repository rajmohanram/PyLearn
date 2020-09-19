# import ConnectHandler from netmiko library
from netmiko import ConnectHandler
import time

# start time of script
start = time.perf_counter()

# create device dictionary - details required to connect
acc_sw_01 = {'device_type': 'cisco_ios', 'host':   '172.16.1.1', 'username': 'cisco', 'password': 'cisco',}

# command to be executed on the device
cmd = 'show ip int brief'

# establish ssh connection to the device
net_connect = ConnectHandler(**acc_sw_01)

# collect output of a sample show command
output = net_connect.send_command(cmd)

# print the collected output
print("\n---->  Output from {}:".format(acc_sw_01['host']))
print(output)

# finish time of script
finish = time.perf_counter()
print(f'\nTime take for completion of this script {round(finish - start)} second(s).')