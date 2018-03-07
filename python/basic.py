import timeit

mysetup = '''
import json
from pprint import pprint

'''
mycode = '''
data = json.load(open('sample.json'))
data = data["data"]
vdevice_name = list(map(lambda data: data["vdevice_name"], data))
vdevice_name = list(set(vdevice_name))
l = {}
for vdevice in vdevice_name:
    l[vdevice] = [x for x in data if x["vdevice_name"] == vdevice]

pprint(len(l["172.17.0.3"]))

'''
print (timeit.timeit(setup = mysetup,
                    stmt = mycode,
                    number = 1))
