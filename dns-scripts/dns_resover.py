import dns.resolver
from pprint import pprint


def query_dns(record, dns_server="8.8.8.8"):
    """Resolve query"""
    response = dict()
    my_resolver = dns.resolver.Resolver()
    my_resolver.nameservers = [dns_server]
    result = my_resolver.resolve(record)
    # print(result.rrset)
    # print(result.rrset.name)
    # print(result.rrset.items)
    # for i in result.rrset.items:
    #     print(i)
    response[f'{result.rrset.name}'] = [f'{i}' for i in result.rrset.items]
    return response


if __name__ == "__main__":
    response = query_dns('amazon.com')
    pprint(response)