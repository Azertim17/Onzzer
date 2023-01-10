import requests
import json

recherche = "55304866-1b79-4365-a6b1-961c95e9fc57"
# traitement1 = recherche.strip()
# replace = traitement1.replace("'", "%27")

url_base = "https://musicbrainz.org/ws/2/artist/"
url_fin = "?inc=releases&fmt=json"
url_complet = url_base + recherche + url_fin

# url_complet = "https://musicbrainz.org/ws/2/artist/55304866-1b79-4365-a6b1-961c95e9fc57?inc=releases&fmt=json"
# url_complet = "https://musicbrainz.org/ws/2/releases/a8976fbd-9225-4c79-b607-6b1917e176dc?inc=artist-credits+labels+discids+recordings&fmt=json"

# urlcomplet = "https://musicbrainz.org/search?query=d%27eux&type=release&method=indexed&fmt=json"

# url_complet = "https://musicbrainz.org/ws/2/artist/?query=artist:847e8a0c-cc20-4213-9e16-975515c2a926&type:artist&fmt=json"
   
# url_base = "https://musicbrainz.org/ws/2/artist/?query=artist:"
# url_fin = "&type:artist&fmt=json"
# url_complet = url_base + replace + url_fin


reponse = requests.get(url_complet)
contenu = reponse.json()

print(json.dumps(contenu, sort_keys=True, indent=4),)

print(url_complet)

