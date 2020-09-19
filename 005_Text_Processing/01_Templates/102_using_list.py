# Jinja2 - Render using Python List example
# create and render the template  (Inline Template)

from jinja2 import Template
from pprint import pprint

# list of ntp servers
ntp_servers = ['1.1.1.1', '2.2.2.2', '3.3.3.3']
pprint(ntp_servers)
print('\n')

# create a template
t = Template("""
!
{% for server in servers -%}
ntp server {{ server }}
{% endfor -%}
!
""")

# render the template
result = t.render(servers = ntp_servers)
print(result)
