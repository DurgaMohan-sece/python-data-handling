import json
from functools import reduce

def get_total_bytes(src, data):
    return reduce(
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

def load_data():
    data = json.load(open("sample.json"))
    return data["data"]

def get_src_ip(data):
    src_ip = list(map(lambda data: data["src_ip"], data))
    return list(set(src_ip))

def calc_total_bytes(src_ip, data):
    total = {}

    for src in src_ip:
        total[src] = get_total_bytes(src, data)

    return total

data = load_data()
src_ip = get_src_ip(data)
total = calc_total_bytes(src_ip, data)
print(total)