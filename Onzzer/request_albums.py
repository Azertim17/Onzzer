import json
import requests
import request_albums2

def get_albums(album_recherche):

        recherche = str(album_recherche)
        traitement1 = recherche.strip()
        replace = traitement1.replace(" ", "%20in%20")
        
        
        url_base = "https://musicbrainz.org/ws/2/release-group/?query=release-group:"
        url_fin = "%20AND%20type:album&fmt=json"
        url_complet = url_base + replace + url_fin
        print(url_complet)
        
        
        reponse = requests.get(url_complet)
        contenu = reponse.json()
        
        
        for i in contenu ["release-groups"]:
                
                #print(i["releases"][0]['title'])
                
                auteur = i['artist-credit'][0]['name']
                id_album = (i['releases'][0]['id'])
                id_auteur = (i['artist-credit'][0]['artist']['id'])

                album_id = {}
                album_id[auteur] = id_album
        
                print(album_id)
                print(id_auteur)

                request_albums2.get_album_pays(album_id)














#fichier = open("data.txt", "a")
#fichier.write(json.dumps(contenu, sort_keys=True, indent=4))
#fichier.close()




























