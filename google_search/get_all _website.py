from serpapi import GoogleSearch
import os
from dotenv import load_dotenv
import json

user_search = input("Search : ")

load_dotenv()

params = {
    "apikey": os.environ.get('API_KEY'),
    "engine": "google",
    "q": user_search,
    "location": "Delhi, india",
    "google_domain": "google.com",
    "gl": "us",
    "hl": "en",
    "tbm": "nws",
}

search = GoogleSearch(params)
pages = search.pagination()

news_results = []

for page_num, page in enumerate(pages, start=1):
    print(f"Extract data form the {page_num}")

    with open('google_search/website_data.json', 'w') as file:
        for news_result in page["news_results"]:

            news_results.append({
                "position": news_result["position"],
                "title": news_result["title"],
                "link": news_result["link"],
                "source": news_result["source"],
                "date_published": news_result["date"],
                "snippet": news_result["snippet"],
                "image": news_result["thumbnail"]
            })

            json.dump({"result": news_results}, file, indent=4)
            