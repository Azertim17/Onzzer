import json
import requests



def get_dic_album_id(self, album_recherche):

        recherche = str(album_recherche)
        traitement1 = recherche.strip()
        traitement1 = traitement1.replace(" ", "%20in%20")
        traitement1 = traitement1.replace("'", "%27")

        
        url_base = "https://musicbrainz.org/ws/2/release-group/?query=release-group:"
        url_fin = "%20AND%20type:album&fmt=json"
        url_complet = url_base + traitement1 + url_fin
        
        reponse = requests.get(url_complet)
        contenu = reponse.json()
        
        dic_album_id = {}

        for i in contenu ["release-groups"]:
                                
                auteur = i['artist-credit'][0]['name']
                id_album = i['releases'][0]['id']

                dic_album_id[auteur] = id_album
        
        return dic_album_id
     
        
     


def get_dic_album_id_artiste(self, album_recherche):

        recherche = str(album_recherche)
        traitement1 = recherche.strip()
        traitement1 = traitement1.replace(" ", "%20in%20")
        traitement1 = traitement1.replace("'", "%27")

        
        url_base = "https://musicbrainz.org/ws/2/release-group/?query=release-group:"
        url_fin = "%20AND%20type:album&fmt=json"
        url_complet = url_base + traitement1 + url_fin
                
        reponse = requests.get(url_complet)
        contenu = reponse.json()
        
        dic_album_artiste = {}

        for i in contenu ["release-groups"]:
                                
                auteur = i['artist-credit'][0]['name']
                id_album = i['releases'][0]['id']


                dic_album_artiste[auteur] = id_album        
        return dic_album_artiste

    
    
    

def get_album_id(self, album_recherche, artiste):

        recherche = str(album_recherche)
        traitement1 = recherche.strip()
        traitement1 = traitement1.replace(" ", "%20in%20")
        traitement1 = traitement1.replace("'", "%27")

        
        url_base = "https://musicbrainz.org/ws/2/release-group/?query=release-group:"
        url_fin = "%20AND%20type:album&fmt=json"
        url_complet = url_base + traitement1 + url_fin
        #print(url_complet)
        
        
        reponse = requests.get(url_complet)
        contenu = reponse.json()
        
        album_id = "0"
        
        # print(artiste)
        for i in contenu ["release-groups"]:
                
                auteur = i['artist-credit'][0]['name']
                id_album = i['releases'][0]['id']
                if auteur == artiste:
                
                    album_id = id_album
                else :
                    pass
                    
        return album_id



         
def get_nom_album(self, album_recherche):

        recherche = str(album_recherche)
        traitement1 = recherche.strip()
        traitement1 = traitement1.replace(" ", "%20in%20")
        traitement1 = traitement1.replace("'", "%27")

        
        url_base = "https://musicbrainz.org/ws/2/release-group/?query=release-group:"
        url_fin = "%20AND%20type:album&fmt=json"
        url_complet = url_base + traitement1 + url_fin
        
        
        reponse = requests.get(url_complet)
        contenu = reponse.json()
        
        liste_albums = []
        
        for i in contenu ["release-groups"]:
    
                nom_album = i['releases'][0]['title']
                liste_albums.append(nom_album)
        return liste_albums





def get_nom_artiste(self, album_recherche):

        recherche = str(album_recherche)
        traitement1 = recherche.strip()
        traitement1 = traitement1.replace(" ", "%20in%20")
        traitement1 = traitement1.replace("'", "%27")

        
        url_base = "https://musicbrainz.org/ws/2/release-group/?query=release-group:"
        url_fin = "%20AND%20type:album&fmt=json"
        url_complet = url_base + traitement1 + url_fin
        
        reponse = requests.get(url_complet)
        contenu = reponse.json()
              
        liste_auteurs = []
        
        for i in contenu ["release-groups"]:
                                
                nom_auteur = i['artist-credit'][0]['artist']['name']
                liste_auteurs.append(nom_auteur)
                
        return nom_auteur



def get_liste_artiste(self, album_recherche):

        recherche = str(album_recherche)
        traitement1 = recherche.strip()
        traitement1 = traitement1.replace(" ", "%20in%20")
        traitement1 = traitement1.replace("'", "%27")

        
        url_base = "https://musicbrainz.org/ws/2/release-group/?query=release-group:"
        url_fin = "%20AND%20type:album&fmt=json"
        url_complet = url_base + traitement1 + url_fin
        
        reponse = requests.get(url_complet)
        contenu = reponse.json()
              
        liste_auteurs = []
        
        for i in contenu ["release-groups"]:
                                
                nom_auteur = i['artist-credit'][0]['artist']['name']
                liste_auteurs.append(nom_auteur)
                
        return liste_auteurs



def get_discographie(self, id):
    
        url_base = "https://musicbrainz.org/ws/2/artist/"
        url_fin = "?inc=releases&fmt=json"
        url_complet = url_base + id + url_fin
        
        reponse = requests.get(url_complet)
        contenu = reponse.json()
              
        liste_albums = []
        
        for i in contenu ["releases"]:
                                
                album = i['title']
                liste_albums.append(album)
                
        return liste_albums
    




