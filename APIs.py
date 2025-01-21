import requests
import sys
import json


if len(sys.argv)!=2:
    sys.exit()
    
response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&terms=weezer")

print(response.json())

obj = response.json()

for result in obj["results"]:
    print(result["trackName"])

