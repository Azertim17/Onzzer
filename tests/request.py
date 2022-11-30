#import json
import requests

url = "https://musicbrainz.org/ws/2/release-group/?query=release-group:Back%20in%20Black%20AND%20type:album&fmt=json"
reponse = requests.get(url)
contenu = reponse.json()

for i in contenu:

  try:

      title = i['release-groups'][6]['releases'][3]['title']
      id_album = i['release-groups'][6]['releases'][0]['id']
      artiste = i['release-groups'][0]['artist-credit'][1]['name']
      id_artiste = i['release-groups'][0]['artist-credit'][0]['artist'][1]['id']


      print("Titre :", title)
      print("Id de l'album :", id_album)
      print("Artiste :", artiste)
      print("Id de l'artiste :", id_artiste)
      print()

    
  except:

    pass


'''
fichier = open("data.txt", "a")
fichier.write(json.dumps(contenu, sort_keys=True, indent=4))
fichier.close()
'''
