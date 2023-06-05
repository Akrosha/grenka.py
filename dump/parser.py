import requests
from json import loads
from urllib.request import urlopen
import bs4
 
#s = requests.session()
#s.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'})
 
#r = s.get('https://www.google.ru/search?q=яблоко&tbm=isch')

mems = "https://ru.pinterest.com/alinkafr20/%D1%81%D0%BC%D0%B5%D1%88%D0%BD%D1%8B%D0%B5-%D0%BC%D0%B5%D0%BC%D1%8B/;https://ru.pinterest.com/karamelllca223/%D0%BC%D0%B5%D0%BC%D1%8B/;https://ru.pinterest.com/demotos_ru/".split(";")
k = 0
for j in mems:
    quote = requests.get(j)

    parsed = bs4.BeautifulSoup(quote.text, "html.parser")
    select = parsed.findAll("img")

    x = [i["src"] for i in select if i["src"] != "https://i.pinimg.com/75x75_RS/59/0e/21/590e2138f7e9290441d9abb87d966a45.jpg"]

    print(x)
    for i in x:
        with open(f"{k}.png", "wb") as file:
            file.write(urlopen(i).read())
        k+=1
"""
for text in soup.findAll(attrs={'class': 'rg_meta notranslate'}):
    text = loads(text.text)
    print(text["ou"])
"""