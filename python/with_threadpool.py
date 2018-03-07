import timeit

mysetup ='''
import concurrent.futures
import json
from pprint import pprint
'''

mycode = '''
def get_vdevice_list():
    l[vdevice] = [x for x in data if x["vdevice_name"] == vdevice]

data = json.load(open('sample.json'))
data = data["data"]
vdevice_name = list(map(lambda data: data["vdevice_name"], data))
vdevice_name = list(set(vdevice_name))
l = {}
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
    for vdevice in vdevice_name:
        executor.submit(get_vdevice_list)
# pprint(l)
'''

print (timeit.timeit(setup = mysetup,
                    stmt = mycode,
                    number = 1))