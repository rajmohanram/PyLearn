from dns import resolver
from pprint import pprint
import time

host = 'cmcloudlab1931.info'
resolver = resolver.Resolver()
mylist = []
for i in range(0,10):
    result = resolver.resolve(host)
    answer = result.response.answer[0]
    name = answer.name
    for item in answer.items:
        mylist.append(str(item))
    time.sleep(0)

total = len(mylist)
unique_list = list((set(mylist)))
my_dict = dict()
for item in unique_list:
    percentage = (mylist.count(item) / total) * 100
    my_dict[item] = f'{percentage}%'
pprint(my_dict)
exit()
for i in range(0,20):
    a = resolver.resolve(host)
    # pprint(dir(a.response))
    # print(a.nameserver)
    # print(a.response.question)
    print(a.response.answer)
