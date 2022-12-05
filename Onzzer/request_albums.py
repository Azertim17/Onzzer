import json
import requests

def get_dic_album_id(self, album_recherche):

        recherche = str(album_recherche)
        traitement1 = recherche.strip()
        replace = traitement1.replace(" ", "%20in%20")
        replace.replace("'", "\'")
        
        
        url_base = "https://musicbrainz.org/ws/2/release-group/?query=release-group:"
        url_fin = "%20AND%20type:album&fmt=json"
        url_complet = url_base + replace + url_fin
        
        
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
        replace = traitement1.replace(" ", "%20in%20")
        replace.replace("'", "\'")

        
        url_base = "https://musicbrainz.org/ws/2/release-group/?query=release-group:"
        url_fin = "%20AND%20type:album&fmt=json"
        url_complet = url_base + replace + url_fin
        
        
        reponse = requests.get(url_complet)
        contenu = reponse.json()
        
        dic_album_artiste = {}

        for i in contenu ["release-groups"]:
                                
                auteur = i['artist-credit'][0]['name']
                id_album = i['releases'][0]['id']


                dic_album_artiste[auteur] = id_album        
        return dic_album_artiste


# def get_album_id(self, album_recherche, artiste):

#         recherche = str(album_recherche)
#         traitement1 = recherche.strip()
#         replace = traitement1.replace(" ", "%20in%20")
        
        
#         url_base = "https://musicbrainz.org/ws/2/release-group/?query=release-group:"
#         url_fin = "%20AND%20type:album&fmt=json"
#         url_complet = url_base + replace + url_fin
        
        
#         reponse = requests.get(url_complet)
#         contenu = reponse.json()
        
        
#         for i in contenu ["release-groups"]:
                
#                 #print(i["releases"][0]['title'])
                
#                 auteur = i['artist-credit'][0]['name']
#                 id_album = i['releases'][0]['id']

#                 dic_album_id = {}
#                 dic_album_id[auteur] = id_album
        
#         return id_album
    
    
    
    

def get_album_id(self, album_recherche, artiste):

        recherche = str(album_recherche)
        traitement1 = recherche.strip()
        replace = traitement1.replace(" ", "%20in%20")
        replace.replace("'", "\'")

        
        url_base = "https://musicbrainz.org/ws/2/release-group/?query=release-group:"
        url_fin = "%20AND%20type:album&fmt=json"
        url_complet = url_base + replace + url_fin
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
        replace = traitement1.replace(" ", "%20in%20")
        replace.replace("'", "\'")

        
        url_base = "https://musicbrainz.org/ws/2/release-group/?query=release-group:"
        url_fin = "%20AND%20type:album&fmt=json"
        url_complet = url_base + replace + url_fin
        #print(url_complet)
        
        
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
        replace = traitement1.replace(" ", "%20in%20")
        replace.replace("'", "\'")

        
        url_base = "https://musicbrainz.org/ws/2/release-group/?query=release-group:"
        url_fin = "%20AND%20type:album&fmt=json"
        url_complet = url_base + replace + url_fin
        
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
        replace = traitement1.replace(" ", "%20in%20")
        replace.replace("'", "\'")

        
        url_base = "https://musicbrainz.org/ws/2/release-group/?query=release-group:"
        url_fin = "%20AND%20type:album&fmt=json"
        url_complet = url_base + replace + url_fin
        
        reponse = requests.get(url_complet)
        contenu = reponse.json()
              
        liste_auteurs = []
        
        for i in contenu ["release-groups"]:
                                
                nom_auteur = i['artist-credit'][0]['artist']['name']
                liste_auteurs.append(nom_auteur)
                
        return liste_auteurs





# def get_dic_album_id(self, album_recherche):

#         recherche = str(album_recherche)
#         traitement1 = recherche.strip()
#         replace = traitement1.replace(" ", "%20in%20")
        
        
#         url_base = "https://musicbrainz.org/ws/2/release-group/?query=release-group:"
#         url_fin = "%20AND%20type:album&fmt=json"
#         url_complet = url_base + replace + url_fin
#         #print(url_complet)
        
        
#         reponse = requests.get(url_complet)
#         contenu = reponse.json()
        
        
#         for i in contenu ["release-groups"]:
                
#                 #print(i["releases"][0]['title'])
                
#                 auteur = i['artist-credit'][0]['name']
#                 id_album = i['releases'][0]['id']
#                 id_auteur = i['artist-credit'][0]['artist']['id']
#                 nom_auteur = i['artist-credit'][0]['artist']['name']
                
#                 nom_album = i['releases'][0]['title']

#                 dic_album_id = {}
#                 dic_album_id[auteur] = id_album
        
#                 print(dic_album_id)
#                 print(id_auteur)
#                 print(nom_auteur)
        
#         return dic_album_id






























