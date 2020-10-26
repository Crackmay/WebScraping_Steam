from bs4 import BeautifulSoup
from urllib.request import urlopen as uReq
import requests
import pandas as pd

filename = "scrap_2.csv"
f = open(filename, "w")

headers = "name,price before and now, date\n"

f.write(headers)


url = 'https://store.steampowered.com/search/?specials=1'


uClient = uReq(url)
page = uClient.read()
uClient.close()


page_soup = BeautifulSoup(page , "html.parser")

containers = page_soup.find_all("div",{"class":"responsive_search_name_combined"})


for container in containers:

    game_names_container = container.findAll("span",{"class":"title"})
    game_names = game_names_container[0].text

    game_price_container = container.findAll("span",{"style":"color: #888888;"})
    game_price = game_price_container[0].text

    game_date_container = container.findAll("div",{"class":"col search_released responsive_secondrow"})
    game_date = game_date_container[0].text

    print("Game name: " + game_names)
    print("Game price before and now: " + game_price)
    print("Game date: " + game_date)

    f.write(game_names + "," + game_price + "," + game_date + "\n")

f.close()