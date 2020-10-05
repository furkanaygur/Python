import requests
from bs4 import BeautifulSoup

url = "https://www.n11.com/bilgisayar/dizustu-bilgisayar"

html = requests.get(url).content
soup = BeautifulSoup(html, 'html.parser')

List = soup.find_all("li", {"class": "column"})

for li in List:
    productName = li.div.a.h3
    link = li.div.a.get('href')
    oldPrice = li.find('div', {"class": "proDetail"}).find_all('a')[0].text.strip().strip('TL')
    newPrice = li.find('div', {"class": "proDetail"}).find('a', {"class": "newPrice"})
    if productName == None:
        continue
    else:
        print(f"{productName.text.strip()} \nLink: {link} \nOld Price: {oldPrice} \nNew Price: {newPrice.text.strip().strip('TL')}")
