import json


def readdataa(key1: str, key2: str):
    """
    do not for get ( " " )
    :param key1: 1st Key will have cap letter for 1st letter ex "Start"
    :param key2: 2nd Key ex "mode"
    :return: value
    """
    with open("data.json", "r") as data:
        jdata = json.load(data)
        return jdata[key1][key2]


def writedataa(value, key1: str, key2: str):
    with open("data.json", "r") as data:
        jdata = json.load(data)
    jdata[key1][key2] = value
    with open("data.json", "w") as data1:
        json.dump(jdata, data1, indent=4)


if __name__ == '__main__':
    #print(readdataa("Emotions", "mcm"))
    writedataa(50, "Emotions", "mcm")
    #print(readdataa("Emotions", "mcm"))
    with open("data.json", "r") as data:
        print(json.load(data))
