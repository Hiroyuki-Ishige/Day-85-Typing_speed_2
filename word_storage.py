import requests

responce = requests.get(url="http://api.open-notify.org/iss-now.json")
responce.raise_for_status()
data = responce.json()
print(data)

#TODO https://pypi.org/project/Wikipedia-API/