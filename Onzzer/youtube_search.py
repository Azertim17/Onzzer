"""
.. module:: youtube_search
    :platform: Unix, Windows
    :synopsis: permet d'ecouter un titre gratuitement suite à notre recherche sur Youtube 

.. moduleauthor:: Matthieu Brissonnet <matthieu.brissonnet@etu.univ-poitiers.fr>, Tim Mazzoloni <tim.mazzolini@etu.univ-poitiers.fr>, Baptiste Tarte <baptiste.tarte@etu.univ-poitiers.fr>, Eliot Monneau <elio.moneau@etu.univ-poitiers.fr>


"""


import requests
import json
import webbrowser

def yt_search(self, artiste, titre):
    """ This function buil query to lisen a tracks in Youtube (use trask title and singer name )

        :param param1: artiste
        :type param1: str
        :param param2: titre
        :type param2: str
        :returns: build a html link 
        :rtype: str
        :raises: TypeError
        :example:

        .. code-block:: python

         def yt_search(self, celine Dion, Grand maman):

         url_base = "https://www.youtube.com/results?search_query="
         url_complet = url_base + celine dion + "+" +  Grand maman

         
         
        

    """
    
    artiste.strip()
    artiste.replace(" ", "+")
    
    titre.strip()
    titre.replace("'", "\'")
    
    
    url_base = "https://www.youtube.com/results?search_query="
    url_complet = url_base + artiste + "+" + titre
    
    webbrowser.open(url_complet)
    