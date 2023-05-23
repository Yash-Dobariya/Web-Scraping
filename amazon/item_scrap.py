import requests
from bs4 import BeautifulSoup

search_term = input('search your item : ')

url = f"https://www.amazon.com/s?k={search_term}"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'Accept-Language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,hi;q=0.7',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
}

response = requests.get(url, headers=headers)

""" get html page """
soup = BeautifulSoup(response.content, "html.parser")

search_results = soup.find_all(
    "div", {"data-component-type": "s-search-result"})

for result in search_results:

    """ get title of product """
    title = result.find("h2", {
                        "class": "a-size-mini a-spacing-none a-color-base s-line-clamp-2"}).text.strip()

    """ get price of product """
    price = result.find("span", {"class": "a-offscreen"})

    if price is not None:
        price = price.text.strip()
    else:
        "price not available"

    """ get rating of product """
    rating = result.find("span", {"class": "a-icon-alt"})

    if rating is not None:
        rating = rating.text.strip()

    """ get status of product """
    status = result.find("span", {"class": "a-size-base a-color-price"})

    if status is not None:
        status = status.text.strip()

    """ get image url of product """
    image_url = result.find("img", {"class": "s-image"})["src"]

    """ get product link """
    link_url = result.find("a", {"class": "a-link-normal"})["href"]

    print({"Tital": title})
    print({"Price": price})
    print({"Rating": rating})
    print({"Image URL": image_url})
    print({"Link URL": link_url})
    print({"status": status})
    print("")
