"""
.. module:: request_albums
    :platform: Unix, Windows
    :synopsis: request_albums recherche album

.. moduleauthor:: Matt Briss <matt.b@orange.fr>

"""
import json
import requests

def get_dic_album_id(self, album_recherche):
        """ Cette fonction fait quelque chose.

        :param param1: album_recherche
        :type param1: str
        
        :returns: dictionary album with ID 
        :rtype: ?
        :raises: TypeError
        
        
        

        """
        recherche = str(album_recherche)
        traitement1 = recherche.strip()
        replace = traitement1.replace(" ", "%20in%20")
        replace.replace("'", "\'")


        url_base = "https://musicbrainz.org/ws/2/release-group/?query=release-group:"
        url_fin = "%20AND%20type:album&fmt=json"
        url_complet = url_base + replace + url_fin


        reponse = requests.get(url_complet)
        contenu = reponse.json()

        return {
            i['artist-credit'][0]['name']: i['releases'][0]['id']
            for i in contenu["release-groups"]
        }
     
        
     


def get_dic_album_id_artiste(self, album_recherche):
        """ create a dictionary album / Artist 
        :param param1: album_recherche
        :type param1: str
        :returns: description de la variable retournée.
        :rtype: int
        :raises: TypeError
        
        
        

        """

        recherche = str(album_recherche)
        traitement1 = recherche.strip()
        replace = traitement1.replace(" ", "%20in%20")
        replace.replace("'", "\'")


        url_base = "https://musicbrainz.org/ws/2/release-group/?query=release-group:"
        url_fin = "%20AND%20type:album&fmt=json"
        url_complet = url_base + replace + url_fin


        reponse = requests.get(url_complet)
        contenu = reponse.json()

        return {
            i['artist-credit'][0]['name']: i['releases'][0]['id']
            for i in contenu["release-groups"]
        }


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

        """ 
        Returne a ID for album 

        :param param1: album_recherche
        :type param1: str
        :param param2: artiste
        :type param2: str
        :returns: album id
        :rtype: int
        :raises: TypeError
        
        
        

        """

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
                if auteur == artiste:

                        id_album = i['releases'][0]['id']
                        album_id = id_album
        return album_id



         
def get_nom_album(self, album_recherche):
        """ 
        This function intterogates API withe name enter in Line Edith

        :param param1: album_recherche
        :type param1: str
        :returns: album name 
        :rtype: str
        :raises: TypeError
        
        
        

        """

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

        return [i['releases'][0]['title'] for i in contenu ["release-groups"]]





def get_nom_artiste(self, album_recherche):
        """ 
        This function research all singer's music album in API

        :param param1: album_recherche
        :type param1: str
        :returns: author name 
        :rtype: str
        :raises: TypeError
        
        
        

        """

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
        """ 
        
        
        :param param1: album_recherche
        :type param1: str
        :returns: author name 
        :rtype: str
        :raises: TypeError
        
        
        

        """

        recherche = str(album_recherche)
        traitement1 = recherche.strip()
        replace = traitement1.replace(" ", "%20in%20")
        replace.replace("'", "\'")


        url_base = "https://musicbrainz.org/ws/2/release-group/?query=release-group:"
        url_fin = "%20AND%20type:album&fmt=json"
        url_complet = url_base + replace + url_fin

        reponse = requests.get(url_complet)
        contenu = reponse.json()

        return [
            i['artist-credit'][0]['artist']['name']
            for i in contenu["release-groups"]
        ]



def get_discographie(self, id_artiste):

        """ 
        This fonction list all singer's album 
        
        
        :param param1: id_artiste
        :type param1: str
        :returns:  list all singer's album
        :rtype: str
        :raises: TypeError
        
        
        

        """
    
        url_fin = "?inc=releases&fmt=json"
        url_complet = f"https://musicbrainz.org/ws/2/artist/{id_artiste}{url_fin}"

        reponse = requests.get(url_complet)
        contenu = reponse.json()


        return {i['title']: i['id'] for i in contenu ["releases"]}


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






























