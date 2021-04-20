import json

with open('stdout-np.txt', 'r') as f:
    output = f.read()

parent_site = 'nrt55-55'
context = {'parent_site': parent_site}

response_output_list = output.splitlines()

if "Physical ports to reserve" in output:
    for line in response_output_list:
        if line.startswith('Physical ports to reserve:'):
            tmp_string = line.split('reserve: ')[1]
            tmp_dict = json.loads(tmp_string.replace("'", '"'))
            ports_dict = tmp_dict[parent_site]
            routers_list = list(ports_dict.keys())
            context['r1_hostname'] = routers_list[0]
            context['r2_hostname'] = routers_list[1]
            context['r1_ports'] = ports_dict[routers_list[0]]
            context['r2_ports'] = ports_dict[routers_list[1]]

if "Aggregate port to reserve" in output:
    for line in response_output_list:
        if line.startswith('Aggregate port to reserve:'):
            tmp_string = line.split('reserve: ')[1]
            tmp_dict = json.loads(tmp_string.replace("'", '"'))
            ae_dict = tmp_dict[parent_site]
            context['r1_ae'] = ae_dict[context['r1_hostname']]
            context['r2_ae'] = ae_dict[context['r2_hostname']]

print(context)