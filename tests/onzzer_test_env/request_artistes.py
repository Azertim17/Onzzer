"""
.. module:: request_artistes
    :platform: Unix, Windows
    :synopsis: request_artistes recherche artistes

.. moduleauthor:: Matthieu Brissonnet <matthieu.brissonnet@etu.univ-poitiers.fr>, Tim Mazzoloni <tim.mazzolini@etu.univ-poitiers.fr>, Baptiste Tarte <baptiste.tarte@etu.univ-poitiers.fr>, Eliot Monneau <elio.moneau@etu.univ-poitiers.fr>

"""

import json
import requests



def get_artist_id_type(artist_name):
    """
        this fonction recuvers type of artiste and give a ID 
        
        :param artiste_recherche: info entrée dans la lineedith
        :type param1: str

        :returns: dictionnary
        
        :rtype:  
        :raises: TypeError
        
    """
    # Removes leading and trailing whitespace from the "artist_name" variable and replaces spaces and single quotes with the appropriate encoding
    artist_name = artist_name.strip().replace(" ", "%20in%20").replace("'", "%27")
    # Constructs the final search URL using f-strings
    url = f"https://musicbrainz.org/ws/2/artist/?query=artist:{artist_name}&type:artist&fmt=json"
    # Make a request to the MusicBrainz server using the constructed URL
    response = requests.get(url)
    # Get the response in json format
    content = response.json()
    # Extract the artist's id and artist's type using dictionary comprehension, store empty string if type is not found
    return {i['id']: i.get('disambiguation','') for i in content['artists']}


def get_artist_name(artiste_recherche):
    """
        this fonction recuvers name of artiste and give a ID 
        
        :param param1: artiste_recherche
        :type param1: str
        :returns: dictionnary
        
        :rtype:  
        :raises: TypeError
        
        """
    # convert the input to a string
    recherche = str(artiste_recherche)
    # remove any leading or trailing whitespace from the string
    traitement1 = recherche.strip()
    # replace spaces with "%20in%20"
    traitement1 = traitement1.replace(" ", "%20in%20")
    # replace apostrophes with "%27"
    traitement1 = traitement1.replace("'", "%27")


    # create the base url
    url_base = "https://musicbrainz.org/ws/2/artist/?query=artist:"
    # create the end of the url
    url_fin = "&type:artist&fmt=json"
    # concatenate the base url, the modified search term and the end of the url
    url_complet = url_base + traitement1 + url_fin

    # make a GET request to the url
    reponse = requests.get(url_complet)
    # parse the response as json
    contenu = reponse.json()

    return {i['id']: i['name'] for i in contenu ['artists']}


def get_artist_id(artiste_recherche):

    """
        this fonction recuvers artiste and give a ID 
        
        :param param1: artiste_recherche
        :type param1: str
        :returns: dictionnary
        
        :rtype:  
        :raises: TypeError
        
        """

    # convert the input to a string
    recherche = str(artiste_recherche)
    # remove any leading or trailing whitespace from the string
    traitement1 = recherche.strip()
    # replace spaces with "%20in%20"
    traitement1 = traitement1.replace(" ", "%20in%20")
    # replace apostrophes with "%27"
    traitement1 = traitement1.replace("'", "%27")


    # create the base url
    url_base = "https://musicbrainz.org/ws/2/artist/?query=artist:"
    # create the end of the url
    url_fin = "&type:artist&fmt=json"
    # concatenate the base url, the modified search term and the end of the url
    url_complet = url_base + traitement1 + url_fin

    # make a GET request to the url
    reponse = requests.get(url_complet)
    # parse the response as json
    contenu = reponse.json()

    return {id: i['id'] for id, i in enumerate(contenu ['artists'], start=1)}
