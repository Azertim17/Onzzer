#import json
import requests

recherche = input('Nom de l Album: ')
traitement1 = recherche.strip()
replace = traitement1.replace(" ", "%20in%20")


url_base = "https://musicbrainz.org/ws/2/release-group/?query=release-group:"
url_fin = "%20AND%20type:album&fmt=json"
url_complet = url_base + replace + url_fin
print(url_complet)

"""
reponse = requests.get(url)
contenu = reponse.json()


for i in contenu:

      title = i['release-groups'][6]['releases'][3]['title']
      id_album = i['release-groups'][6]['releases'][0]['id']
      artiste = i['release-groups'][0]['artist-credit'][1]['name']
      id_artiste = i['release-groups'][0]['artist-credit'][0]['artist'][1]['id']


      print("Titre :", title)
      print("Id de l'album :", id_album)
      print("Artiste :", artiste)
      print("Id de l'artiste :", id_artiste)
      print()



fichier = open("data.txt", "a")
fichier.write(json.dumps(contenu, sort_keys=True, indent=4))
fichier.close()
"""
