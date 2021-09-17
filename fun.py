import json

EM = 0


def EM_read(data):
    global EM
    EM = data


with open("data.json", "r") as starts:
    jstart = json.load(starts)
    print(jstart["Start"]["mode"])
