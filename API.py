import requests
import json


def getData(pURL):
    response = requests.get(pURL)
    data = json.loads(response.text)
    return data
