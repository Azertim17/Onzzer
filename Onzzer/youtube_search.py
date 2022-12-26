"""
.. module:: youtube_search
    :platform: Unix, Windows
    :synopsis: permet d'ecouter un titre gratuitement suite à notre recherche sur Youtube 

.. moduleauthor:: Matt Briss <matt.b@orange.fr>

"""


import requests
import json
import webbrowser

def yt_search(self, artiste, titre):
    """ Cette fonction fait quelque chose.

        :param param1: premier paramètre.
        :type param1: str
        :param param2: deuxième paramètre.
        :type param2: bool
        :returns: description de la variable retournée.
        :rtype: int
        :raises: TypeError
        
        
        

    """
    
    artiste.strip()
    artiste.replace(" ", "+")
    
    titre.strip()
    titre.replace("'", "\'")
    
    
    url_base = "https://www.youtube.com/results?search_query="
    url_complet = url_base + artiste + "+" + titre
    
    webbrowser.open(url_complet)
    