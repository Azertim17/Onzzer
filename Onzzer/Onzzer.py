"""
.. module:: Onzzer
    :platform: Unix, Windows
    :synopsis: Onzzer module principale du projet

.. moduleauthor:: Matthieu Brissonnet <matthieu.brissonnet@etu.univ-poitiers.fr>, Tim Mazzoloni <tim.mazzolini@etu.univ-poitiers.fr>, Baptiste Tarte <baptiste.tarte@etu.univ-poitiers.fr>, Eliot Monneau <elio.moneau@etu.univ-poitiers.fr>

"""
import sys 
import os
import urllib.request
from PyQt5.QtWidgets import QVBoxLayout, QGridLayout, QPushButton, QDesktopWidget, QFileDialog
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QAction, QToolBar, QStackedLayout
from PyQt5.QtWidgets import QLabel, QLineEdit, QPlainTextEdit, QTableView, QAbstractItemView, QComboBox
from PyQt5.QtWidgets import QMessageBox, QTableWidget, QTableWidgetItem, QHeaderView, QHBoxLayout
from PyQt5.QtGui import QIcon, QPixmap, QPixmap, QPalette, QColor
from PyQt5.QtCore import Qt, QFileInfo
from PyQt5 import sip
import request_albums
import request_pistes
import request_artistes
import youtube_search as YS


class Fenetre_principale(QMainWindow):
    """
    this is Onzzer's window

    """   
    #Creation of the path used to find the pictures in directory 'Icones'
    #Path of the current file
    absolutepath = os.path.abspath(__file__)
    fileDirectory = os.path.dirname(absolutepath)

    #Navigate to 'Icones' directory
    newPath = os.path.join(fileDirectory, 'Icones')


    def __init__(self):
    
        """The constructor."""
        super().__init__()
        """the super constructor"""
        """paramètre de la fenetre 
        :param titre : Onzzer
        
        :returns: contruit les fenêtres de l'application 
        """

        # Defining the main settings of the application window
        self.setWindowTitle("Onzzer")
        self.setWindowIcon(QIcon(Fenetre_principale.newPath + "\logo.png"))
        self.setGeometry(600,100,800,800)
        self.menu()
        self.accueil()
        self.center()

        # Call the connect function that test the internet connexion, if no connection, display a information message 
        if not self.connect():
            QMessageBox.information(self,"Pas d'accès internet", "Vous devez être connecté à internet pour utiliser l'application")

    def connect(self):


        # function that test the internet connection with google website 
        try:
            urllib.request.urlopen("http://google.com") 
            return True
        except:
            return False

        
    def menu(self):
        """
        menu & toolbar creation


        :returns: menu and toolbar
        :rtype: app
        :raises: TypeError
        :exemple:

        .. code-block:: python

        app = menu(self)

        """

        # Fonction who generate the menu (menu bar and toolbar) with shortcuts and informations 

        # Creation of diffents buttons with picture, shortcut and name 
        eraseButton = QAction(QIcon(Fenetre_principale.newPath + "\edit-undo.png"), 'Effacer', self)
        eraseButton.setShortcut('Ctrl+N')
        openButton = QAction(QIcon(Fenetre_principale.newPath + "\mail-send.png"), "Ouvrir l'emplacement d'enregistrement", self)
        openButton.setShortcut('Ctrl+O')
        exitButton = QAction(QIcon(Fenetre_principale.newPath + "\zapplication-exit.png"), 'Quitter', self)
        exitButton.setShortcut('Ctrl+Q')
        manButton = QAction('A Propos', self)
        manButton.setShortcut('F1')

        # Defines the actions associated with the different buttons, calls the corresponding function onclick
        eraseButton.triggered.connect(self.action_clear)
        exitButton.triggered.connect(self.close)
        openButton.triggered.connect(self.action_openfolder)
        manButton.triggered.connect(self.action_a_propos)

        # Added menus to the menu bar: File and Help
        menu = self.menuBar()
        menufichier = menu.addMenu("&Fichier")
        menufichier.addActions([eraseButton, openButton, exitButton])

        menuAide = menu.addMenu("&Aide")
        menuAide.addAction(manButton)

        # Added shortcut to the toolbar 
        toolbar = QToolBar("Ma barre d'outils")
        self.addToolBar(toolbar)
        toolbar.addActions([eraseButton, exitButton])

        # Set the styleSheet of the menu (the blue background-color)
        menu.setStyleSheet("background-color: #3655B2")
        toolbar.setStyleSheet("background-color: #3655B2")
        


    def accueil(self):
        """
        This function creates the first page and includes styles.
        It retrieves the inscription in "LINEedit" and calls the "categorie" function.
        
        :returns: It calls the "categorie" function.
        :raises: TypeError
        :example:
            self.searchButton.clicked.connect(self.categorie) 
        """
        # This is the main page of our application, the one allowing to search for an album or an artist

        # Create the various widgets for the home page: the edit line, the drop-down list, the search button, the Onzzer logo,
        # and other invisible but useful widgets for the layout of the interface
        image = QPixmap(Fenetre_principale.newPath + "\logo_long_blanc.png")
        self.catcombo = QComboBox()
        self.catcombo.addItems(["Album" , "Artiste"])
        # This line set the style of the dropdown list view of the combobox to white.
        self.catcombo.setStyleSheet("QListView {background-color : white; }")
        self.searchButton = QPushButton("Recherche") 
        self.searchButton.clicked.connect(self.categorie)
        self.line = QLineEdit()
        self.wid_onzzer = QWidget()
        # This line set the background color of the main widget to dark gray
        self.wid_onzzer.setStyleSheet("background-color: #202124")

        # Use a vertical layout for the main widget
        vbox = QVBoxLayout()
        wid_grid = QWidget()
        grid = QGridLayout()
        box_image = QLabel()
        self.setCentralWidget(self.wid_onzzer)

        self.wid_onzzer.setLayout(vbox)
        box_image.setPixmap(image)
        box_image.setAlignment(Qt.AlignCenter)
        # add widget to the grid layout
        grid.addWidget(self.line, 0, 0, 1, 3)
        grid.addWidget(self.searchButton, 1, 1, 1, 2)
        grid.addWidget(self.catcombo, 0, 4)
        wid_grid.setLayout(grid)
        # add image to the main layout
        vbox.addWidget(box_image, alignment=Qt.AlignBottom)

        vbox.setAlignment(Qt.AlignCenter)
        # add grid layout to the main layout
        vbox.addWidget(wid_grid, alignment= Qt.AlignCenter)

        # Set styles for various widgets
        self.searchButton.setStyleSheet("background-color: #E79E41; border-style: outset; border-width: 1px; height: 20px;")
        self.catcombo.setStyleSheet("background-color: white; border-style: outset; height: 22px;")
        self.line.setStyleSheet("background-color: white;")

        # set the fixed width for widgets
        wid_grid.setFixedWidth(600)
        box_image.setFixedWidth(600)


    def categorie(self):
        """
        This function calls different functions based on the selection in the drop-down list.

        :returns: If the selection is "Album", it calls the "recherche_album" function with the text from the line edit widget.
                If the selection is "Artiste", it calls the "recherche_artiste" function with the text from the line edit widget.
        :raises: TypeError
        :example:
            select = self.catcombo.currentText()
            if select == "Album":
                self.recherche_album(self.line.text())
            elif select == "Artiste" :
                self.recherche_artiste(self.line.text())
        """
        select = self.catcombo.currentText()
        if select == "Album":
            self.recherche_album(self.line.text())
        elif select == "Artiste" :
            self.recherche_artiste(self.line.text())
    



    def recherche_album(self, recherche):
        """
        
        :param param1: id_artiste
        
        :param param1: recherche
        :type param1: str
        :returns: list all album with the same 
                
        :rtype: 
        :raises: TypeError
        
        """
        # retrieve the albums and artistes data
        self.liste_albums = request_albums.get_nom_album(self, recherche)
        self.liste_artistes = request_albums.get_liste_artiste(self, recherche)
        
        # create the image for the logo
        image1 = QPixmap(Fenetre_principale.newPath + "\logo_long_blanc.png" ) 
        image = image1.scaled(255, 68)
        
        # create the new search button
        searchButton = QPushButton("Nouvelle recherche")
        searchButton.setStyleSheet("background-color: #E79E41; border-style: outset; border-width: 1px; width: 150px; height: 20px;")
        searchButton.clicked.connect(self.accueil)
        
        # Create the main widget, table widget and its layout
        self.wid_table = QWidget()
        self.wid_table.setStyleSheet("background-color: #202124")
        wid_bouttons = QWidget()
        vbox = QVBoxLayout()
        bouttonshbox = QHBoxLayout()
        box_image = QLabel()
        self.table = QTableWidget()
        self.table.setRowCount(len(self.liste_albums))
        self.table.setColumnCount(3)
        self.table.setContentsMargins(100, 200, 100, 0)
        self.table.setStyleSheet("QTableWidget::item {color: white;}")
        self.setCentralWidget(self.wid_table)
        
        # Set image for the logo
        box_image.setPixmap(image)
        vbox.addWidget(box_image, alignment= Qt.AlignRight)

        # Set the main layout of the application
        self.wid_table.setLayout(vbox) # Set the layout of the table widget to be a vertical box layout
        vbox.addWidget(self.table) # Add the table widget to the layout
        
        wid_bouttons.setLayout(bouttonshbox) # Set the layout of the button widget
        bouttonshbox.addWidget(searchButton, alignment=Qt.AlignLeft) # Add the search button to the button layout and align it to the left
        vbox.addWidget(wid_bouttons, alignment= Qt.AlignLeft) # Add the button widget to the main layout and align it to the left
        
        headerH = ["Nom Artiste","Titre Album","Voir les Pistes"] # Define the header labels for the table
        self.table.setHorizontalHeaderLabels(headerH) # Set the header labels for the table
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents) # Set the table header to resize to the contents
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers) # Set the table to not be editable

        for i in range(len(self.liste_artistes)): # Iterate through the list of artists and albums
            self.table.setItem(i, 0, QTableWidgetItem(self.liste_artistes[i])) # Add the artist to the first column of the table
            self.table.setItem(i, 1, QTableWidgetItem(self.liste_albums[i])) # Add the album to the second column of the table
            selectButton = QPushButton("voir") # Create a 'voir' button
            selectButton.setIcon(QIcon(Fenetre_principale.newPath + "\go-last.png")) # Set an icon for the button
            self.table.setCellWidget(i, 2, selectButton) # Add the button to the third column of the table
            selectButton.clicked.connect(lambda _, r=i+1, c=3: self.id_album(r, recherche)) # Connect the button to the 'id_album' function and pass in the row number and the 'recherche' variable when clicked
        



    def recherche_artiste(self, recherche):
        """
        Code of the table grouping the artists bearing the name sought

        He has got a button to retourn in Acceuil and made a new research. 

        She calls and recover the information returned by the request_artist function 
        She builds with this informations the table.

        :param param1: recherche
        :type param1: str 
        :returns: list all artist with same name and their type 
        :rtype: tab
        :raises: TypeError
        :exemple:
        .. code-block:: python

            recherche_artiste = recherche_artiste(self, "celine dion")
        
        .. figure:: docs/source/_static/celine_dion.jpeg
            :scale: 200
            
            résultat de la receherche céline Dion



        """        
        self.dic_type = request_artistes.get_id_type(self, recherche)
        self.dic_name = request_artistes.get_artiste_name(self, recherche)
        
        image1 = QPixmap(Fenetre_principale.newPath + "\logo_long_blanc.png" ) 
        image = image1.scaled(255, 68)
        searchButton = QPushButton("Nouvelle recherche")
        searchButton.setStyleSheet("background-color: #E79E41; border-style: outset; border-width: 1px; width: 150px; height: 20px;")
        searchButton.clicked.connect(self.accueil)
        
        self.wid_artiste = QWidget()
        self.wid_artiste.setStyleSheet("background-color: #202124")

        wid_bouttons = QWidget()
        vbox = QVBoxLayout()
        bouttonshbox = QHBoxLayout()
        box_image = QLabel()
        self.table = QTableWidget()
        row = len(self.dic_name)
        self.table.setRowCount(row)
        self.table.setColumnCount(3)
        self.table.setContentsMargins(100, 200, 100, 0)
        self.table.setStyleSheet("QTableWidget::item {color: white;}")
        self.setCentralWidget(self.wid_artiste)
        
        box_image.setPixmap(image)
        vbox.addWidget(box_image, alignment= Qt.AlignRight)
  
        self.wid_artiste.setLayout(vbox)
        vbox.addWidget(self.table)

        wid_bouttons.setLayout(bouttonshbox)
        
        bouttonshbox.addWidget(searchButton, alignment=Qt.AlignLeft)
        
        vbox.addWidget(wid_bouttons, alignment= Qt.AlignLeft)
        
        headerH = ["Nom Artiste","Désignation","Voir la discrographie"]
        self.table.setHorizontalHeaderLabels(headerH)
        
        header =self.table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)  

        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        
        
        
        row = 0
        for i in self.dic_name:
            row += 1
            self.table.setItem(row-1,0, QTableWidgetItem(self.dic_name[i]))

        row = 0  
        for i in self.dic_type:             
            row += 1
            self.table.setItem(row-1,1, QTableWidgetItem(self.dic_type[i]))
                      
        row = 0
        for i in range(0,25):             
        
            row += 1
            
            selectButton = QPushButton("voir")
            selectButton.setIcon(QIcon(Fenetre_principale.newPath + "\go-last.png"))
            self.table.setCellWidget(row-1,2,selectButton)
            selectButton.clicked.connect(lambda _, r=row, c=3: self.id_artiste(r, c, recherche)) 
    
    
    def id_artiste(self, row, column, recherche):
        """
        Give the number of line if I click in the row. Get back the id_artist 

        :param param1: recherche
        :type param1: str 
        :returns: list all artist with same name and their type
        :param param2: row
        :type param2: int
        :returns: number of line if I click
        :

        
        :rtype: listing about singer with same name 
        :raises: TypeError
        """
        self.artiste = self.table.item(row-1, 0).text()        
        
        dic = request_artistes.get_artiste_id(self, recherche)
        id = dic[row]
        self.discographie(id)
        
    
  
    def discographie(self, id_artiste):
        """
        print discography corresponding at id_artiste
        
        :param param1: id_artiste
        :type param1: str
        :returns:  
                
        :rtype: 
        :raises: TypeError
        
        """
        image1 = QPixmap(Fenetre_principale.newPath + "\logo_long_blanc.png" ) 
        image = image1.scaled(255, 68)
        searchButton = QPushButton("Nouvelle recherche")
        searchButton.setStyleSheet("background-color: #E79E41; border-style: outset; border-width: 1px; width: 150px; height: 20px;")
        searchButton.clicked.connect(self.accueil)
         
        self.wid_discographie = QWidget()
        self.wid_discographie.setStyleSheet("background-color: #202124")
        
        
        self.liste_albums = request_albums.get_discographie(self, id_artiste)

        image1 = QPixmap(Fenetre_principale.newPath + "\logo_long_blanc.png" ) 
        image = image1.scaled(255, 68)
        searchButton = QPushButton("Nouvelle recherche")
        searchButton.setStyleSheet("background-color: #E79E41; border-style: outset; border-width: 1px; width: 150px; height: 20px;")
        searchButton.clicked.connect(self.accueil)
         
        self.wid_discographie = QWidget()
        self.wid_discographie.setStyleSheet("background-color: #202124")

        wid_bouttons = QWidget()
        vbox = QVBoxLayout()
        bouttonshbox = QHBoxLayout()
        box_image = QLabel()
        self.table = QTableWidget()
        row = len(self.liste_albums)
        self.table.setRowCount(row)
        self.table.setColumnCount(2)
        self.table.setContentsMargins(100, 200, 100, 0)
        self.table.setStyleSheet("QTableWidget::item {color: white;}")
        self.setCentralWidget(self.wid_discographie)
        
        box_image.setPixmap(image)
        vbox.addWidget(box_image, alignment= Qt.AlignRight)
   
        self.wid_discographie.setLayout(vbox)
        vbox.addWidget(self.table)

        wid_bouttons.setLayout(bouttonshbox)
         
        bouttonshbox.addWidget(searchButton, alignment=Qt.AlignLeft)
         
        vbox.addWidget(wid_bouttons, alignment= Qt.AlignLeft)
         
        headerH = ["Titre Album","Voir les Pistes"]
        self.table.setHorizontalHeaderLabels(headerH)
        header = self.table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)  
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
         
         
        row = 0
        for i in self.liste_albums:
             row += 1
             self.table.setItem(row-1,0, QTableWidgetItem(i))
             
       
        row = 0
        for i in range(0,25):             
             row += 1
             
             selectButton = QPushButton("voir")
             selectButton.setIcon(QIcon(Fenetre_principale.newPath + "\go-last.png"))
             self.table.setCellWidget(row-1,1,selectButton)
             selectButton.clicked.connect(lambda _, r=row, c=3: self.get_pistes_by_album(r, c, id_artiste)) 
    
    
    def get_pistes_by_album(self,row ,column, id_artiste):
        """
        
        
        :param param1: row
        :type param1: str
        :returns: 
        :param param2: row
        :type param2: str
        :returns:
                
        :rtype: listing about singer with same name 
        :raises: TypeError
        
        """
        
        dic_album_id = request_albums.get_discographie(self, id_artiste)
        self.nom_album = self.table.item(row-1, 0).text()
        album_id = dic_album_id[self.nom_album]
        titres = request_pistes.get_pistes_album(album_id)
        self.pistes(titres, id_artiste)
        


        
    

        
        
    def pistes(self, titres, recherche):
        """
        
        
        :param param1: titres
        :type param1: str
        :returns: 
        :param param2: recherche 
        :type param2: str
        :returns:       
        :rtype: 
        :raises: TypeError
        
        """
        
        image1 = QPixmap(Fenetre_principale.newPath + "\logo_long_blanc.png" ) 
        image = image1.scaled(255, 68)
        searchButton = QPushButton("Nouvelle recherche")
        searchButton.setStyleSheet("background-color: #E79E41; border-style: outset; border-width: 1px; width: 150px; height: 20px;")
        searchButton.clicked.connect(self.accueil)
        returnButton = QPushButton("Retour liste")
        returnButton.setStyleSheet("background-color: #E79E41; border-style: outset; border-width: 1px; width: 150px; height: 20px;")
        
        
        if len(recherche) == 36:
            returnButton.clicked.connect(lambda : self.discographie(recherche))
        else :
            returnButton.clicked.connect(lambda : self.recherche_album(recherche))
            
            
        uploadButton = QPushButton("Enregistrer")
        uploadButton.setStyleSheet("background-color: #E79E41; border-style: outset; border-width: 1px; width: 150px; height: 20px;")
        uploadButton.clicked.connect(lambda : self.action_upload(titres))
        
        self.wid_pistes = QWidget()
        self.wid_pistes.setStyleSheet("background-color: #202124")

        vbox = QVBoxLayout()
        wid_bouttons = QWidget()
        bouttonshbox = QHBoxLayout()
        box_image = QLabel()
        self.table = QTableWidget()
        self.table.setColumnCount(2)
        self.table.setContentsMargins(100, 200, 100, 0)
        self.table.setStyleSheet("QTableWidget::item {color: white;}")
        self.setCentralWidget(self.wid_pistes)
        
        box_image.setPixmap(image)
        vbox.addWidget(box_image, alignment= Qt.AlignRight)
  
        self.wid_pistes.setLayout(vbox)
        vbox.addWidget(self.table)
        
        wid_bouttons.setLayout(bouttonshbox)
        bouttonshbox.addWidget(searchButton)
        bouttonshbox.addWidget(returnButton)
        bouttonshbox.addWidget(uploadButton)

        vbox.addWidget(wid_bouttons, alignment= Qt.AlignLeft)
        vbox.setAlignment(Qt.AlignTop)

        headerH = ["Titres de l'Album","Ouvrir youtube"]
        self.table.setHorizontalHeaderLabels(headerH)
        
        header = self.table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)  
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        
        nb_rows = len(titres)
        self.table.setRowCount(nb_rows)

        row = 0
        for i in titres:
            row += 1
            self.table.setItem(row-1,0, QTableWidgetItem(i))
            
            ytButton = QPushButton(QIcon(Fenetre_principale.newPath + "\youtube.jpg"),"")
            self.table.setCellWidget(row-1, 1, ytButton)
            ytButton.clicked.connect(lambda _, r=row, c=3: self.youtube(r, c, recherche)) 
                
    
    def id_album(self, row, recherche):
        """
        
        
        :param param1: row
        :type param1: int
        :returns: number of row
        :param param2: recherche
        :type param2: str
        :returns: listing about singer with same name 
                
        :rtype: 
        :raises: TypeError
        
        """
        
        self.nom_album = self.table.item(row-1, 1).text()
        self.artiste = self.table.item(row-1, 0).text()
        dic = request_albums.get_dic_album_id_artiste(self, recherche)
        id = dic[self.artiste]
        titres = request_pistes.get_pistes_album(id)
        self.pistes(titres, recherche)
        
        
        
    def youtube(self, row, col, recherche):
        """
        
        
        :param param1: id_artiste
        :type param1: str
        :returns: 
                
         
        :raises: TypeError
        
        """
        
        self.nom_piste = self.table.item(row-1, 0).text()
        YS.yt_search(self, self.artiste, self.nom_piste)
    
     
    def action_openfolder(self) :
        os.startfile("")
        """
        This function open forder 
        
        """
        os.startfile('..\Onzzer\Icones')
        
        
    def action_clear(self):
        """
        This function clear th line edith
        
        
                
        
        
        """
        self.line.clear()

    def action_a_propos(self):
        """
        This fonction give informations about programmer's application 
        
           
        """
        QMessageBox.information(self,"Onzzer Application de Recherche Musicale", "Onzzer par Baptiste Tarte, Tim Mazzolini, Eliot Monneau, Matthieu Brissonnet")
        
        
    def action_upload(self, titres):
        """
        This function allow save all tracks from an album in file .txt 
        
        :param param1: titre
        :type param1: str
        :returns: file .txt
                
        
        
        """
        
        nom_base = self.nom_album + (" - ") + self.artiste + (".txt")

        
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_path, _ = QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()",nom_base,"All Files (*);;Text Files (*.txt)", options=options)
        
        
        with open(file_path, "w") as fichier:
            
                fichier.write("Liste de chansons de l'album ")
                fichier.write(self.nom_album)
                fichier.write(" de l'artiste ")
                fichier.write(self.artiste)
                fichier.write("\n ")
                
                for i in titres:
                    fichier.write("\n->")
                    fichier.write(i)
                      
                    
                    
        filename = QFileInfo(file_path).fileName()
        QMessageBox.information(self,"Et voilà", "Fichier écrit avec le nom " + filename)

     

    
    def center(self):
        """
        
        
        
        
                
        
        
        """
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def resource_path(relative_path):

        """ 
        Get absolute path to resource, works for dev and for PyInstaller 
        
        """
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)

        
        

def main():
    application = QApplication(sys.argv)
    fenetre = Fenetre_principale()
    fenetre.show()
    sys.exit(application.exec())
        
if __name__ == '__main__':
    main()