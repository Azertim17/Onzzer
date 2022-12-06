import requests
import json
import webbrowser

def yt_search(self, artiste, titre):
    
    
    artiste.strip()
    artiste.replace(" ", "+")
    
    titre.strip()
    titre.replace("'", "\'")
    
    
    url_base = "https://www.youtube.com/results?search_query="
    url_complet = url_base + artiste + "+" + titre
    
    webbrowser.open(url_complet)
    