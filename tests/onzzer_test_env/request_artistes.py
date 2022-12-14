import json
import requests



def get_id_type(self, artiste_recherche):

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

        recherche = str(artiste_recherche)
        traitement1 = recherche.strip()
        traitement1 = traitement1.replace(" ", "%20in%20")
        traitement1 = traitement1.replace("'", "%27")

        
        url_base = "https://musicbrainz.org/ws/2/artist/?query=artist:"
        url_fin = "&type:artist&fmt=json"
        url_complet = url_base + traitement1 + url_fin
        
        reponse = requests.get(url_complet)
        contenu = reponse.json()
                
        dic_artiste_name = {}
        
        for i in contenu ['artists']:
                
                nom_artiste = i['name']
                id_artiste = i['id']
                
                dic_artiste_name[id_artiste] = nom_artiste
            
            
        return dic_artiste_name


def get_artiste_id(self, artiste_recherche):

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
        id = 0
        
        for i in contenu ['artists']:
                
                id += 1
                id_artiste = i['id']
                dic_artiste_id[id] = id_artiste
        

        return dic_artiste_id
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    