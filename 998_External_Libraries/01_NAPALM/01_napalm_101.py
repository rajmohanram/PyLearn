import napalm
from pprint import pprint

driver = napalm.get_network_driver('ios')
device = driver(hostname='172.16.255.1', username='cisco', password='cisco', optional_args={'secret': 'cisco'})
device.open()
pprint(device.get_facts())