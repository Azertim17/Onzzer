import json
import requests

url = "https://musicbrainz.org/ws/2/release/78ff42d3-cb7b-416b-b3d1-a3f0535468af?inc=artist-credits+labels+discids+recordings&fmt=json"
reponse = requests.get(url)
contenu = reponse.json()

fichier = open("data.txt", "a")
fichier.write(json.dumps(contenu, sort_keys=True, indent=4))
fichier.close()

