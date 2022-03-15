from bs4 import BeautifulSoup
import requests
import re

product = input("What product do you want to search for? ")
link = f" https://www.newegg.com/global/in-en/p/pl?d={product}&N=4131"
page = requests.get(link).text

items_found = {}
doc = BeautifulSoup(page, "html.parser")

page_text = doc.find(class_="list-tool-pagination-text").strong

pages = int(str(page_text).split("/")[-2].split(">")[-1][:-1])
items_found = {}

for page in range(1, pages+1):
    link = f" https://www.newegg.com/global/in-en/p/pl?d={product}&N=4131&page={page}"
    page = requests.get(link).text
    doc = BeautifulSoup(page, "html.parser")
    div = doc.find(class_="item-cells-wrap border-cells items-grid-view four-cells expulsion-one-cell")
items = doc.find_all(text=re.compile(product))


for item in items:
    parent = item.parent

    if parent.name != "a":
        continue
    url = parent['href']
    next_parent = item.find_parent(class_="item-container")
    price = next_parent.find(class_="price-current").text
    # items_found[item] = {"price" : int(price.replace(",", "")), "url" : url}

    print(price)
