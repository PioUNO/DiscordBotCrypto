from bs4 import BeautifulSoup
import requests
import time
import webbrowser

#bitcoin
btc = requests.get("https://btc.com/btc") #https://whattomine.com/coins/1-btc-sha-256
soup1 = BeautifulSoup(btc.content, "html.parser")

resultadobtc = soup1.find("span", {"class":"font-size-sm mr-sm default-text"}) #text-decoration-none text-reset
preciobtc = resultadobtc.text

#ethereum
eth = requests.get("https://btc.com/eth") #https://whattomine.com/coins/1-btc-sha-256
soup2 = BeautifulSoup(eth.content, "html.parser")

resultadoeth = soup2.find("span", {"class":"font-size-sm mr-sm default-text"}) #text-decoration-none text-reset
precioeth = resultadoeth.text

inflacion = requests.get("https://btc.com/eth") #https://whattomine.com/coins/1-btc-sha-256
soup3 = BeautifulSoup(inflacion.content, "html.parser")

inflacionresult = soup3.find("span", {"class":"font-size-sm font-size-xs positive-text"}) #text-decoration-none text-reset
inflaciontotal = inflacionresult.text

