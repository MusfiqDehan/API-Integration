import requests
import config
from pprint import pprint

url = "https://api.yelp.com/v3/businesses/search"
headers = {
    "Authorization": "Bearer " + config.api_key
}
params = {
    "term": "food",
    "location": "NYC",
    "limit": 50
}
response = requests.get(url, headers=headers, params=params)
businesses = response.json()["businesses"]
names = [business["name"]
         for business in businesses if business["rating"] > 4.5]  # list comprehension
pprint(names)
