from bs4 import BeautifulSoup
import requests
import os

source = requests.get("https://www.rottentomatoes.com/browse/movies_at_home/sort:popular?page=1")

soup = BeautifulSoup(source.text, 'html.parser')

links = []

for item in soup.find("div", class_ = "discovery-grids-container").find_all('img'):
    links.append((item['src']))

os.mkdir("rottenttomatoes_img")


for index ,link in enumerate(links):

    img_data = requests.get(link).content
    with open("rottenttomatoes_img/"+str(index+1)+".jpg", "wb+") as f:
        f.write(img_data)
