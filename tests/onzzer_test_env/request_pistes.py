import json
import requests
import request_albums


def get_pistes_album(album_id):

    recherche = str(album_id)
    traitement1 = recherche.strip()
    traitement1 = traitement1.replace(" ", "%20in%20")
    traitement1 = traitement1.replace("'", "%27")

    url_fin = "?inc=artist-credits+labels+discids+recordings&fmt=json"
    url_complet = f"https://musicbrainz.org/ws/2/release/{traitement1}{url_fin}"

    reponse = requests.get(url_complet)
    contenu = reponse.json()

    return [i['title'] for i in contenu ['media'][0]['tracks']]

