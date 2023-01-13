"""
.. module:: request_pistes
    :platform: Windows, Unix
    :synopsis: request_albums recherche album

.. moduleauthor:: Matthieu Brissonnet <matthieu.brissonnet@etu.univ-poitiers.fr>, Tim Mazzoloni <tim.mazzolini@etu.univ-poitiers.fr>, Baptiste Tarte <baptiste.tarte@etu.univ-poitiers.fr>, Eliot Monneau <elio.moneau@etu.univ-poitiers.fr>

"""

import json
import requests
import request_albums



def get_album_titles(album_id):
    """
        This code searches album by id and returns a list of song titles using MusicBrainz web service.
        
        :param param1: album_id
        :type param1: str
        :returns: liste list
        
        :rtype:  
        :raises: TypeError
        
     """

    # Removes leading and trailing whitespace from the "album_id" variable and replaces spaces and single quotes with the appropriate encoding
    album_id = album_id.strip().replace(" ", "%20in%20").replace("'", "%27")
    # Constructs the final search URL using f-strings
    url = f"https://musicbrainz.org/ws/2/release/{album_id}?inc=artist-credits+labels+discids+recordings&fmt=json"
    # Make a request to the MusicBrainz server using the constructed URL
    response = requests.get(url)
    # Get the response in json format
    content = response.json()
    # Extract the song title using list comprehension
    return [i['title'] for i in content['media'][0]['tracks']]






# def get_album_pays(album_id):
#     """
        
        
#         :param param1: album_id
#         :type param1: str
#         :returns: liste list
        
#         :rtype:  
#         :raises: TypeError
        
#         """
        
#     album_id = album_id.strip().replace(" ", "%20in%20").replace("'", "\'")
#     # Constructs the final search URL using f-strings
#     url = f"https://musicbrainz.org/ws/2/release/{album_id}?inc=artist-credits+labels+discids+recordings&fmt=json"
#     # Make a request to the MusicBrainz server using the constructed URL
#     response = requests.get(url)
#     # Get the response in json format
#     content = response.json()
#     # Extract the song title using list comprehension
#     return [i['title'] for i in content['media'][0]['tracks']]




