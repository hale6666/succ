import requests
import json

with open("api.key") as f:
    API_KEY = f.read().strip()
    """
    This is for security online, so the API key is not publicized.
    """

url='https://webdrink.csh.rit.edu/api/index.php'

def test():
    """
    This is not usually called, other than for testing the API.
    """
    head = {"request": "test/api/{}".format(API_KEY), "api_key": API_KEY}
    ret=requests.get(url,params=head)
    print(ret.text)
    print(ret.json())
    print(ret.json()['message'])

def ibutton2uid(ibutton, ib_url="http://ibutton2uid.app.csh.rit.edu/"):
    """
    Thanks to James Forcier for writing this.  https://github.com/csssuf
    """
    r = requests.get(ib_url + ibutton)
    if r.status_code == 200:
        return r.text

def get_credits(uid):
    """
    This is to return the credits a user has, so that it can be shown on the screen.
    """
    head = {"request": "users/credits/{}".format(uid), "uid": uid, "api_key": API_KEY}
    ret = requests.get(url,params=head)
    if ret.status_code != 200:
        raise ValueError
    else:
        return ret.json()['data']

def give_credits(uid, credits):
    """
    Takes the uid and amount to give.
    This cannot be used until permission to change balances is given.
    """
    head = {"request": "users/credits/{}/{}/{}".format(uid, credits, "add"), "uid": uid,
        "value": credits, "type": "add", "api_key": API_KEY}
    ret = requests.post(url,params=head)
    if ret.status_code != 200:
        raise ValueError
    else:
        return ret.json()['data']
