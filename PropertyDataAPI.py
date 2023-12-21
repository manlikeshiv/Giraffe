import requests
import json

URL = "https://api.propertydata.co.uk/prices"

key = 'RQRJZLTZLM'
postcode = 'DN31 2QP'

queryURL = URL + f"?key={key}&postcode={postcode}"

response = requests.get(queryURL)

housedata = json.loads(response.text)

price = housedata['data']['average']

print(price)