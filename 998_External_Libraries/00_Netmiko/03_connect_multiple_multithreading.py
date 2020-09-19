# import ConnectHandler from netmiko library
from netmiko import ConnectHandler
import time
import concurrent.futures

# start time of script
start = time.perf_counter()

# create device dictionary for all the devices - details required to connect
wan_edge_01 = {'device_type': 'cisco_ios', 'host':   '172.16.255.1', 'username': 'cisco', 'password': 'cisco'}
cor_sw_01 = {'device_type': 'cisco_ios', 'host':   '172.16.255.11', 'username': 'cisco', 'password': 'cisco'}
cor_sw_02 = {'device_type': 'cisco_ios', 'host':   '172.16.255.12', 'username': 'cisco', 'password': 'cisco'}
acc_sw_01 = {'device_type': 'cisco_ios', 'host':   '172.16.1.1', 'username': 'cisco', 'password': 'cisco'}
acc_sw_02 = {'device_type': 'cisco_ios', 'host':   '172.16.1.2', 'username': 'cisco', 'password': 'cisco'}
acc_sw_03 = {'device_type': 'cisco_ios', 'host':   '172.16.1.3', 'username': 'cisco', 'password': 'cisco'}
acc_sw_04 = {'device_type': 'cisco_ios', 'host':   '172.16.1.4', 'username': 'cisco', 'password': 'cisco'}

# list of command to be executed on the device
cmd_list = ['show ip int brief']

my_list = [
    {'device': acc_sw_01, 'cmds': cmd_list},
    {'device': acc_sw_02, 'cmds': cmd_list},
    {'device': acc_sw_03, 'cmds': cmd_list},
    {'device': acc_sw_04, 'cmds': cmd_list},
    {'device': cor_sw_01, 'cmds': cmd_list},
    {'device': cor_sw_02, 'cmds': cmd_list},
    {'device': wan_edge_01, 'cmds': cmd_list}
]


# function to connect and execute a command on a device
def execute_commands(devices):
    device = devices['device']
    cmds = devices['cmds']
    # establish ssh connection to the device
    net_connect = ConnectHandler(**device)
    # collect output of commands
    output = list()
    output.append(f"\n---> Logs collected from {device['host']}\n")
    for cmd in cmds:
        output.append(net_connect.send_command(cmd))
    return ''.join(output)


# multi-threading the device connections
with concurrent.futures.ThreadPoolExecutor() as executor:
    # results = [executor.submit(execute_commands, device) for device in my_list]
    # for f in concurrent.futures.as_completed(results):
    #     print(f.result())

    results = executor.map(execute_commands, my_list)
    for result in results:
        print(result)


# finish time of script
finish = time.perf_counter()
print(f'\nTime take for completion of this script {round(finish - start)} second(s).')