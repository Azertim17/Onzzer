import json
import requests
import request_albums


def get_album_pays(album_id):

    recherche = str(album_id)
    traitement1 = recherche.strip()
    replace = traitement1.replace(" ", "%20in%20")
    
    url_base = "https://musicbrainz.org/ws/2/release/"
    url_fin = "?inc=artist-credits+labels+discids+recordings&fmt=json"
    url_complet = url_base + replace + url_fin
        
    reponse = requests.get(url_complet)
    contenu = reponse.json()

    liste_titres = []
    for i in contenu ['media'][0]['tracks'] :
        
        
        titre = i['title']
        liste_titres.append(titre)
        
    return liste_titres