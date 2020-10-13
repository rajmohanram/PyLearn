import dns.resolver
from pprint import pprint

my_resolver = dns.resolver.Resolver()
my_resolver.nameservers = ['208.67.222.222']

answers = my_resolver.resolve('www.cmcloudlab556.info')
pprint(dir(answers))

# print(answers.canonical_name)
# print(answers.expiration)
# print(answers.nameserver)
# print(answers.port)
# print(answers.qname)
# print(answers.rdclass)
# print(answers.rdtype)
# print(answers.response)
print(answers.rrset)


"""
['canonical_name',
 'expiration',
 'nameserver',
 'port',
 'qname',
 'rdclass',
 'rdtype',
 'response',
 'rrset']
"""