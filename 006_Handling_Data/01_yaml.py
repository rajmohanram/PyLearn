import yaml
from pprint import pprint

with open('ospf1.yaml', 'r') as f:
    data = yaml.load(f, Loader=yaml.FullLoader)

pprint(data)
