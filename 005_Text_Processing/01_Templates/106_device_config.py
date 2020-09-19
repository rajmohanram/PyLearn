# Jinja2 - Render using Template file Example
# create and render the template (using multiple input files and multiple Template file)

from jinja2 import Environment, FileSystemLoader
import yaml
from pprint import pprint
import os

# list of all YAML files
input_files = []
for file in os.listdir('.'):
	if file.endswith('.yml'):
		input_files.append(file)
pprint(input_files)
print('\n')

# input parameters from yaml file
CfgInput = {}
for file in input_files:
	with open(file, 'r') as stream:
		tmp_dict = yaml.load(stream)
		CfgInput.update(tmp_dict)
pprint(CfgInput)
print('\n')


# find and load the template
file_loader = FileSystemLoader('.')
env = Environment(loader=file_loader, trim_blocks=True, lstrip_blocks=True)

# get the Jinja2 template
template = env.get_template('106_config.j2')

# Render the output from the template
result = template.render(config = CfgInput)

# Print the output
print(result)

