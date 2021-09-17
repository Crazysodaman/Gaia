import json


def readdata(*args):
    with open("data.json", "r") as data:
        jdata = json.load(data)
        for i in args:
            
        return jdata


def writedata():
    with open("data.json", "r") as data:
        jdata = json.dump(data)


ozzy = json.load(open("data.json", "r"))["Diagnostics"]["ledtest"]
print(ozzy)
print(readdata("Emotions", "mcm"))
