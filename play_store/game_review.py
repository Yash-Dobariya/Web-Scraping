from serpapi import GoogleSearch
import json

# user_input = input("Search : ")

params = {
    "api_key": "fee25911efabd4373b43091d5277e88817d72dec2b373593ed6e36d903ba3dbb",
    "engine": "google_play_product",
    "gl": "in",
    "store": "apps",
    "product_id": 'com.dts.freefiremax',
    "all_reviews": "true"
}

search = GoogleSearch(params)
results = search.pagination()

for i in results:
    
    print(i['reviews'])
    with open ('/play_store/game_review.json', 'w') as file:
        json.dump(i['reviews'], file, indent=4)
