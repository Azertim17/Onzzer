"""
.. module:: request_artistes
    :platform: Unix, Windows
    :synopsis: request_artistes recherche artistes

.. moduleauthor:: Matthieu Brissonnet <matthieu.brissonnet@etu.univ-poitiers.fr>, Tim Mazzoloni <tim.mazzolini@etu.univ-poitiers.fr>, Baptiste Tarte <baptiste.tarte@etu.univ-poitiers.fr>, Eliot Monneau <elio.moneau@etu.univ-poitiers.fr>

"""

import json
import requests



def get_id_type(self, artiste_recherche):
        """
        this fonction recuvers type of artiste and give a ID 
        
        :param param1: artiste_recherche
        :type param1: str
        :returns: dictionnary
        
        :rtype:  
        :raises: TypeError
        
        """

        recherche = str(artiste_recherche)
        traitement1 = recherche.strip()
        traitement1 = traitement1.replace(" ", "%20in%20")
        traitement1 = traitement1.replace("'", "%27")

        
        url_base = "https://musicbrainz.org/ws/2/artist/?query=artist:"
        url_fin = "&type:artist&fmt=json"
        url_complet = url_base + traitement1 + url_fin
        
        reponse = requests.get(url_complet)
        contenu = reponse.json()
        
        dic_artiste_id = {}
        
        for i in contenu ['artists']:
            try:
                type_artiste = i['disambiguation']
            except KeyError:
                    pass
            try:    
                id_artiste = i['id']
                dic_artiste_id[id_artiste] = type_artiste
                
            except UnboundLocalError:
                dic_artiste_id[id_artiste] = ""
                
        return dic_artiste_id


def get_artiste_name(self, artiste_recherche):
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
             
        # create an empty dictionary
        dic_artiste_name = {}
        
        # iterate over the artists in the json response
        for i in contenu ['artists']:
            # get the name of the artist
            nom_artiste = i['name']
            # get the id of the artist
            id_artiste = i['id']
            # add the artist's id and name to the dictionary
            dic_artiste_name[id_artiste] = nom_artiste
        
        # return the dictionary
        return dic_artiste_name


def get_artiste_id(self, artiste_recherche):

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
                
        dic_artiste_id = {}
        id = 0
        
        # iterate over the artists in the json response
        for i in contenu ['artists']:
                
                id += 1
                # get the id of the artist
                id_artiste = i['id']
                # add the artist's id and name to the dictionary
                dic_artiste_id[id] = id_artiste
        
        # return the dictionary
        return dic_artiste_id
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    