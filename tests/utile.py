import urllib.request, requests
import json
import csv

recherche = "celine dion"
traitement1 = recherche.strip()
replace = traitement1.replace("'", "%27")

url_base = "https://musicbrainz.org/ws/2/release-group/?query=release-group:"
url_fin = "%20AND%20type:album&fmt=json"
url_complet = url_base + replace + url_fin

url_complet = "https://musicbrainz.org/ws/2/release-group/d6cfccc8-026d-4028-b567-4f762354ff91?inc=releases&fmt=json"

# urlcomplet = "https://musicbrainz.org/search?query=d%27eux&type=release&method=indexed&fmt=json"

# url_complet = "https://musicbrainz.org/ws/2/artist/?query=artist:847e8a0c-cc20-4213-9e16-975515c2a926&type:artist&fmt=json"
   
# url_base = "https://musicbrainz.org/ws/2/artist/?query=artist:"
# url_fin = "&type:artist&fmt=json"
# url_complet = url_base + replace + url_fin


reponse = requests.get(url_complet)
contenu = reponse.json()

print(json.dumps(contenu, sort_keys=True, indent=4),)



print(url_complet)