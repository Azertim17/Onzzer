import json
import requests
import request_albums


def get_album_pays(id_album):

    url_base = "https://musicbrainz.org/ws/2/release-group/"
    url_fin = "?inc=releases&fmt=json"
    url_complet = url_base + id_album + url_fin


    print(url_complet)

        
    reponse = requests.get(url_complet)
    contenu = reponse.json()


    for i in contenu ["releases"][0]:
            
            #print(i["releases"][0]['title'])
            
            auteur = i['id']


        
            print(auteur)