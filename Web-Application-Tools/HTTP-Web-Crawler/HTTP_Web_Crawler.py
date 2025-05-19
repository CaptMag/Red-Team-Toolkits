import requests

def crawler():

    r = requests.get('https://hackthissite.org')
    print(r)
