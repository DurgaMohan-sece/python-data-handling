import json
from functools import reduce

def get_total_bytes(src, data):
    l = [x["total_bytes"] for x in data if x["src_ip"] == src]
    total[src] = reduce(lambda x, y: x + y, l)

data = json.load(open("sample.json"))
data = data["data"]

src_ip = list(map(lambda data: data["src_ip"], data))
src_ip = list(set(src_ip))
l = {}
total = {}

for src in src_ip:
    get_total_bytes(src, data)
    # l = [x["total_bytes"] for x in data if x["src_ip"] == src]


print(total)