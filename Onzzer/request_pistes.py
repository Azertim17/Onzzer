"""
.. module:: request_pistes
    :platform: Unix, Windows
    :synopsis: request_albums recherche album

.. moduleauthor:: Matthieu Brissonnet <matthieu.brissonnet@etu.univ-poitiers.fr>, Tim Mazzoloni <tim.mazzolini@etu.univ-poitiers.fr>, Baptiste Tarte <baptiste.tarte@etu.univ-poitiers.fr>, Eliot Monneau <elio.moneau@etu.univ-poitiers.fr>

"""

import json
import requests
import request_albums


def get_album_pays(album_id):
    """
        
        
        :param param1: album_id
        :type param1: str
        :returns: liste list
        
        :rtype:  
        :raises: TypeError
        
        """
        

    recherche = str(album_id)
    traitement1 = recherche.strip()
    replace = traitement1.replace(" ", "%20in%20")
    replace.replace("'", "\'")

    
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





def get_pistes_album(album_id):
    """
        
        
        :param param1: album_id
        :type param1: str
        :returns: liste list
        
        :rtype:  
        :raises: TypeError
        
        """

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