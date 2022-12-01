import urllib.request, requests
import json
import csv

recherche = "f6f47e1d-926b-4c47-bf00-8464dce88c65"
traitement1 = recherche.strip()
replace = traitement1.replace(" ", "%20in%20")

url_base = "https://musicbrainz.org/ws/2/release-group/?query=release-group:"
url_fin = "%20AND%20type:album&fmt=json"
#url_complet = url_base + replace + url_fin
url_complet =  

   
reponse = requests.get(url_complet)
contenu = reponse.json()

print(json.dumps(contenu, sort_keys=True, indent=4))