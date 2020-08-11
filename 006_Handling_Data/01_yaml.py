import yaml
from pprint import pprint

with open('ansible-playbook.yml', 'r') as f:
    data = yaml.load(f, Loader=yaml.FullLoader)

pprint(data)


# YAML ---> LOAD ---> Python Objects (List / Dict)
#
# TextFile ---> Parser ---> Python Objects (List / Dict) ---> Dump ---> YAML
#
