import json
import requests
import request_albums


def get_pistes_album(album_id):

    recherche = str(album_id)
    traitement1 = recherche.strip()
    traitement1 = traitement1.replace(" ", "%20in%20")
    traitement1 = traitement1.replace("'", "%27")
      
    url_base = "https://musicbrainz.org/ws/2/release/"
    url_fin = "?inc=artist-credits+labels+discids+recordings&fmt=json"
    url_complet = url_base + traitement1 + url_fin
        
    reponse = requests.get(url_complet)
    contenu = reponse.json()

    liste_titres = []
    for i in contenu ['media'][0]['tracks'] :
        
        
        titre = i['title']
        liste_titres.append(titre)
        
    return liste_titres

