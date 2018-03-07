import json
from pprint import pprint
from functools import reduce

def get_total_bytes(src, data):
    total[src] = reduce(
        lambda x, y: x + y,
        list(
            map(
                lambda data: data["total_bytes"],
                filter(
                    lambda data: data["src_ip"] == src,
                    data
                )
            )
        )
    )

data = json.load(open("sample.json"))
data = data["data"]

src_ip = list(map(lambda data: data["src_ip"], data))
src_ip = list(set(src_ip))
l = {}
total = {}

for src in src_ip:
    get_total_bytes(src, data)
    # l = [x["total_bytes"] for x in data if x["src_ip"] == src]


pprint(total)