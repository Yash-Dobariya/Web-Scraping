import requests

url = "https://api.sandbox.co.in/authenticate"

headers = {
    "accept": "application/json",
    "x-api-version": "1.0"
}

response = requests.post(url, headers=headers)

print(response.text)
