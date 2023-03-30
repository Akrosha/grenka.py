import requests
from math import ceil

def getStrings(lang: str = "ru", str_id: str = "hello.world"):
    with open(f"languages/{lang}.lang", "r") as file:
        strings = file.read().split("\n")
        while "" in strings:
            strings.remove("")
        for string in strings:
            string = string.split(" == ")
            if string[0] == str_id:
                return string[1].replace("\\n", "\n")
    return "NaN"

def trueRandom(one: int = 0, two: int = 100, c: int = 1):
    if one not in range(-1000000000, 1000000000):
        return getStrings(str_id = "helpers.randomFunctions.trueRandom.min")
    if two not in range(-1000000000, 1000000000):
        return getStrings(str_id = "helpers.randomFunctions.trueRandom.max")
    if c not in range(1, 10000):
        return getStrings(str_id = "helpers.randomFunctions.trueRandom.count")
    r = requests.get(f"https://www.random.org/integers/?num={c}&min={one}&max={two}&col=1&base=10&format=plain&rnd=new")
    return " ".join(r.text.split())

def showAsList(daList: list, name: str = "NaN", page: int = 1, iterator: int = 5):
    if page > 0 and page <= ceil(len(daList)/iterator):
        daList = [f"({i+1}) {element}" for i, element in enumerate(daList)]
        text = """{} ({}: {}):
{}
{} {} {}""".format(name, getStrings(str_id = "helpers.randomFunctions.showAsList.all"), len(daList), "\n".join(daList[(page - 1)*iterator:(page - 1)*iterator + iterator]), page, getStrings(str_id = "helpers.randomFunctions.showAsList.opened_page"), ceil(len(daList)/iterator))
    else:
        text = f"{page} {getStrings(str_id = 'helpers.randomFunctions.showAsList.not_in_range')}: 1 - {ceil(len(daList)/iterator)}"
    return text

def similar(first: str, second: str):
    if not len(first) == len(second):
        return False
    if len(first) - sum(l1==l2 for l1, l2 in zip(first, second)) > 3:
        return False
    return True

def similarList(first: str, seconds: list):
    for second in seconds:
        if similar(first, second):
            return second
    return