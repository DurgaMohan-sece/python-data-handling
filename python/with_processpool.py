import concurrent.futures
import json
import os
from pprint import pprint

def get_vdevice_list():
    l[vdevice] = [x for x in data if x["vdevice_name"] == vdevice]
    print("Executing our Task on Process: {} -".format(os.getpid()))

data = json.load(open('sample.json'))
data = data["data"]
vdevice_name = list(map(lambda data: data["vdevice_name"], data))
vdevice_name = list(set(vdevice_name))
l = {}
with concurrent.futures.ProcessPoolExecutor(max_workers=4) as executor:
    for vdevice in vdevice_name:
        executor.submit(get_vdevice_list)
print("Executing our Task on Process: {} - {}".format(os.getpid(), l))
pprint(l)