# Jinja2 - Render using Template file Example
# create and render the template (using input file and Template file)

from jinja2 import Environment, FileSystemLoader
import yaml
from pprint import pprint

# input parameters from yaml file
with open('inputs/105_input.yml', 'r') as stream:
	CfgInput = yaml.load(stream)
pprint(CfgInput)
print('\n')

# find and load the template
file_loader = FileSystemLoader('.')
env = Environment(loader=file_loader)

# get the Jinja2 template
template = env.get_template('106_config.j2')

# Render the output from the template
result = template.render(config = CfgInput)

# Print the output
print(result)

