import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top?ref_=nv_mv_250"

html = requests.get(url).content

soup = BeautifulSoup(html, 'html.parser')

List = soup.find("tbody", {"class": "lister-list"}).find_all("tr", limit=10)
i = 1
for tr in List:
    title = tr.find("td", {"class": "titleColumn"}).find("a").text
    year = tr.find("td", {"class": "titleColumn"}).find("span").text.strip("()")
    rating = tr.find("td", {"class": "ratingColumn imdbRating"}).find("strong").text.strip("()")

    print(f"{i}.Movie: {title.ljust(50)} Year: {year} Rating: {rating}")
    i += 1
