# Чтение данных с сайта
# Создайте словарь, где ключами будут названия, а значениями будут их цены.
# Выведите его в консоль, чтобы убедиться, что всё правильно.
#Примечание: разумеется, цены этих телефонов надо вытащить с сайта, используя показанные в уроке инструменты для парсинга.

import bs4
import requests
 
url = "https://www.stolplit.ru/internet-magazin/katalog-mebeli/3595-detskaya-komnata-dlya-devochki-mebel/"
r = requests.get(url)
r.encoding = "UTF8"
 
b = bs4.BeautifulSoup(r.text, "html.parser")
 
headersParser = b.select("div.product__info a")
pricesParser = b.select('[itemprop="offers"]')
 
headers = []
prices = []
myDict = dict()
 
for a in headersParser:
    header = a.getText()
    headers.append(header.strip())
 
for a in pricesParser:
    price = int((((a.getText()).replace(" ", "")).replace("\n", "")).replace("Р.", ""))
    prices.append(price)
 
i = 0
for h in headers:
    myDict[h] = prices[i]
    i += 1
 
print(myDict)