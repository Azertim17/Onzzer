"""
.. module:: request_albums
    :platform: Unix, Windows
    :synopsis: request_albums recherche album

.. moduleauthor:: Matthieu Brissonnet <matthieu.brissonnet@etu.univ-poitiers.fr>, Tim Mazzoloni <tim.mazzolini@etu.univ-poitiers.fr>, Baptiste Tarte <baptiste.tarte@etu.univ-poitiers.fr>, Eliot Monneau <elio.moneau@etu.univ-poitiers.fr>

"""
import json
import requests

# def get_dic_album_id(album_recherche):
#         """ Cette fonction fait quelque chose.

#         :param param1: album_recherche
#         :type param1: str
        
#         :returns: dictionary album with ID 
#         :rtype: ?
#         :raises: TypeError
        
        
        

#         """
#         # Store the user's search for an album as a string
#         recherche = str(album_recherche)
#         traitement1 = recherche.strip()
#         # Replace any spaces in the user's input with "%20in%" for use in the MusicBrainz API URL
#         replace = traitement1.replace(" ", "%20in%20")
#         # Escape any apostrophes in the user's input for use in the MusicBrainz API URL
#         replace.replace("'", "\'")
        
#         # Define the base URL for the MusicBrainz API
#         url_base = "https://musicbrainz.org/ws/2/release-group/?query=release-group:"
#         # Define the end of the URL for the MusicBrainz API
#         url_fin = "%20AND%20type:album&fmt=json"
#         # Combine the base and end of the URL with the user's input to create the complete API URL
#         url_complet = url_base + replace + url_fin
        
#         # Send a GET request to the MusicBrainz API with the complete URL
#         reponse = requests.get(url_complet)
#         # Retrieve the JSON content of the API response
#         contenu = reponse.json()
        
#         # Create an empty dictionary to store album IDs
#         dic_album_id = {}

#         # Iterate through the release groups in the API response
#         for i in contenu ["release-groups"]:
                
#                 # Store the name of the artist credit of the current release group
#                 auteur = i['artist-credit'][0]['name']
#                 # Store the ID of the first release associated with the current release group
#                 id_album = i['releases'][0]['id']
#                 # Add the artist credit and album ID to the dictionary as a key-value pair
#                 dic_album_id[auteur] = id_album
#         # Return the dictionary of album IDs
#         return dic_album_id
     
        
     


def get_album_artist_dic(album_name):
    """
    This function receives an album name as input, and returns a dictionary containing the album name as key and the artist name as value.
    
    :param album_name: The name of the album to search for.
    :type album_name: str
    :return: A dictionary with album name as key and artist name as value.
    :rtype: dict
    """
    # Removes leading and trailing whitespace from the "album_name" variable and replaces spaces and single quotes with the appropriate encoding
    album_name = album_name.strip().replace(" ", "%20in%20").replace("'", "%27")
    # Constructs the final search URL using f-strings
    url = f"https://musicbrainz.org/ws/2/release-group/?query=release-group:{album_name} AND type:album&fmt=json"
    # Make a request to the MusicBrainz server using the constructed URL
    response = requests.get(url)
    # Get the response in json format
    content = response.json()
    # Extract the album's id and album's artist using dictionary comprehension
    return {i['artist-credit'][0]['name']:i['releases'][0]['id'] for i in content["release-groups"]}
    

# def get_album_id(album_name,artist_name):
#     """
#     This function receives an album name and artist name as input, and returns the album id.
#     :param album_name: The name of the album to search for.
#     :type album_name: str
#     :param artist_name: The name of the artist.
#     :type artist_name: str
#     :return: The album id.
#     :rtype: int
#     """
#     # Removes leading and trailing whitespace from the "album_name" variable and replaces spaces and single quotes with the appropriate encoding
#     album_name = album_name.strip().replace(" ", "%20in%20").replace("'", "%27")
#     # Constructs the final search URL using f-strings
#     url = f"https://musicbrainz.org/ws/2/release-group/?query=release-group:{album_name} AND type:album&fmt=json"
#     # Make a request to the MusicBrainz server using the constructed URL
#     response = requests.get(url)
#     # Get the response in json format
#     content = response.json()
#     #Initialize album_id with 0
#     album_id = "0"
#     #iterate over the albums in the json response
#     for i in content["release-groups"]:
#         #check if the artist name matches the artist name in the album
#         if i['artist-credit'][0]['name'] == artist_name:
#             #if matches set the album_id to the id of the album
#             album_id = i['releases'][0]['id']
#     #return the album id
#     return album_id



         
def get_album_name(album_name):
    """
    This function receives an album name as input and returns the album name from MusicBrainz.
    :param album_name: The name of the album to search for.
    :type album_name: str
    :return: The album name.
    :rtype: str
    """
    # Removes leading and trailing whitespace from the "album_name" variable and replaces spaces and single quotes with the appropriate encoding
    album_name = album_name.strip().replace(" ", "%20in%20").replace("'", "%27")
    # Constructs the final search URL using f-strings
    url = f"https://musicbrainz.org/ws/2/release-group/?query=release-group:{album_name} AND type:album&fmt=json"
    # Make a request to the MusicBrainz server using the constructed URL
    response = requests.get(url)
    # Get the response in json format
    content = response.json()
    # Initialize an empty list
    list_albums = []
    #iterate over the albums in the json response
    for i in content["release-groups"]:
        #append the album name to the list
        list_albums.append(i['releases'][0]['title'])
    #return the list of album names
    return list_albums





# def get_artist_name(self, album_recherche):
#         """ 
#         This function research all singer's music album in API

#         :param param1: album_recherche
#         :type param1: str
#         :returns: author name 
#         :rtype: str
#         :raises: TypeError
        
        
        

#         """

#         recherche = str(album_recherche)
#         traitement1 = recherche.strip()
#         replace = traitement1.replace(" ", "%20in%20")
#         replace.replace("'", "\'")

        
#         url_base = "https://musicbrainz.org/ws/2/release-group/?query=release-group:"
#         url_fin = "%20AND%20type:album&fmt=json"
#         url_complet = url_base + replace + url_fin
        
#         reponse = requests.get(url_complet)
#         contenu = reponse.json()
              
#         liste_auteurs = []
        
#         for i in contenu ["release-groups"]:
                                
#                 nom_auteur = i['artist-credit'][0]['artist']['name']
#                 liste_auteurs.append(nom_auteur)
                
#         return nom_auteur



def get_artist_list(album_name):
    """
    This function receives an album name as input and returns a list of the artist name(s) associated with that album from MusicBrainz.
    :param album_name: The name of the album to search for.
    :type album_name: str
    :return: List of artist names.
    :rtype: list
    """
    # Removes leading and trailing whitespace from the "album_name" variable and replaces spaces and single quotes with the appropriate encoding
    album_name = album_name.strip().replace(" ", "%20in%20").replace("'", "%27")
    # Constructs the final search URL using f-strings
    url = f"https://musicbrainz.org/ws/2/release-group/?query=release-group:{album_name} AND type:album&fmt=json"
    # Make a request to the MusicBrainz server using the constructed URL
    response = requests.get(url)
    # Get the response in json format
    content = response.json()
    # Initialize an empty list
    artist_list = []
    #iterate over the albums in the json response
    for i in content["release-groups"]:
        #append the artist name to the list
        artist_list.append(i['artist-credit'][0]['artist']['name'])
    #return the list of artist names
    return artist_list



def get_discographie(id_artiste):
        """
        This function lists all the albums of a singer using their MusicBrainz ID.
        :param id_artiste: MusicBrainz ID of the artist
        :type id_artiste: str
        :returns: list of all singer's albums
        :rtype: dict
        """
        url_base = "https://musicbrainz.org/ws/2/artist/"
        url_fin = "?inc=releases&fmt=json"
        url_complet = url_base + id_artiste + url_fin
        
        # Send a GET request to the MusicBrainz API using the complete URL
        response = requests.get(url_complet)
        # Parse the JSON response
        content = response.json()

        # Initialize an empty dictionary to store the album name and its MusicBrainz ID
        album_list = {}

        # Iterate over the list of releases in the response
        for release in content["releases"]:
        # Get the title of the release (i.e. the album name)
                album_name = release['title']
                # Get the MusicBrainz ID of the release (i.e. the album)
                album_id = release['id']
                # Add the album name and its ID to the dictionary
                album_list[album_name] = album_id
        # Return the dictionary
        return album_list

