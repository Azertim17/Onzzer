"""
.. module:: youtube_search
    :platform: Windows, Unix
    :synopsis: permet d'ecouter un titre gratuitement suite à notre recherche sur Youtube 

.. moduleauthor:: Matthieu Brissonnet <matthieu.brissonnet@etu.univ-poitiers.fr>, Tim Mazzoloni <tim.mazzolini@etu.univ-poitiers.fr>, Baptiste Tarte <baptiste.tarte@etu.univ-poitiers.fr>, Eliot Monneau <elio.moneau@etu.univ-poitiers.fr>


"""


import requests
import json
import webbrowser

def yt_search(artiste, titre):
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
    # This function takes in two variables, "artiste" and "titre", and uses them to search for 
    # a music video on YouTube by opening the constructed search URL in the default web browser 
    # after cleaning and formatting the input.
    

    # Removes leading and trailing whitespace from the "artiste" variable
    artiste.strip()

    # Replaces spaces with + in the "artiste" variable
    artiste.replace(" ", "+")

    # Removes leading and trailing whitespace from the "titre" variable
    titre.strip()

    # Replaces single quotes with escaped single quotes in the "titre" variable
    titre.replace("'", "\'")


    # Constant string representing the base of the YouTube search URL
    url_base = "https://www.youtube.com/results?search_query="

    # Constructs the final search URL by concatenating the "url_base", "artiste", and "titre" variables
    url_complet = url_base + artiste + "+" + titre

    # Opens the constructed URL in the default web browser
    webbrowser.open(url_complet)
    