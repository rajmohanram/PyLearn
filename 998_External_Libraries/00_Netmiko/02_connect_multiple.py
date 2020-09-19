# import ConnectHandler from netmiko library
from netmiko import ConnectHandler
import time

# start time of script
start = time.perf_counter()

# create device dictionary for all the devices - details required to connect
acc_sw_01 = {'device_type': 'cisco_ios', 'host':   '172.16.1.1', 'username': 'cisco', 'password': 'cisco',}
acc_sw_02 = {'device_type': 'cisco_ios', 'host':   '172.16.1.2', 'username': 'cisco', 'password': 'cisco',}
acc_sw_03 = {'device_type': 'cisco_ios', 'host':   '172.16.1.3', 'username': 'cisco', 'password': 'cisco',}
acc_sw_04 = {'device_type': 'cisco_ios', 'host':   '172.16.1.4', 'username': 'cisco', 'password': 'cisco',}

# list of devices to connect and execute commands
device_list = [acc_sw_01, acc_sw_02, acc_sw_03, acc_sw_04]

# list of command to be executed on the device
cmd_list = ['show version', 'show ip int brief']

# for loop to iterate through each device in the 'device_list'
for device in device_list:
    # establish ssh connection to the device
    net_connect = ConnectHandler(**device)

    # for loop to iterate through each command in the 'cmd_list'
    for cmd in cmd_list:
        # collect output of a command
        output = net_connect.send_command(cmd)

        # print the collected output
        print("\n---->  '{}' output from '{}':".format(cmd, device['host']))
        print(output)

# finish time of script
finish = time.perf_counter()
print(f'\nTime take for completion of this script {round(finish - start)} second(s).')