import requests
import json

URL = "http://127.0.0.1:8000/stucreate/"

data = {
    'name': 'shivani',
    'roll': 103,
    'city': 'indore'
}

json_data = json.dumps(data)
k = requests.post(url=URL, data=json_data)
# r = requests.post(url=URL, data=json_data)
data = k.json()
print(data)
