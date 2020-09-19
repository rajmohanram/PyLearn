# Jinja2 - Render using dictionary Example
# create and render the template (Inline Template)

from jinja2 import Template
from pprint import pprint

# list of ntp servers
ntp_servers = {'servers':['1.1.1.1', '2.2.2.2', '3.3.3.3'], 'source_iface':'Loopback0', 'key':'C!sc0123'}
pprint(ntp_servers)
print('\n')

# create a template
t = Template("""
!
{% for server in servers.servers -%}
ntp server {{ server }}
{% endfor -%}
ntp source-interface {{ servers.source_iface }}
ntp authentication-key {{ servers.key }}
!
""")

# render the template
result = t.render(servers = ntp_servers)
print(result)
