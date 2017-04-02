import requests
import json

with open("api.key") as f:
    API_KEY = f.read().strip()

url='https://webdrink.csh.rit.edu/api/index.php'
head = {"request": "test/api/{}".format(API_KEY), "api_key": API_KEY}
ret=requests.get(url,params=head)
print(ret.text)
print(ret.json())
