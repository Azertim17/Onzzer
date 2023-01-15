"""
.. module:: Onzzer
    :platform: Windows, Unix
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
    This is Onzzer's window

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
        """
        verify the connexion with Internet if true: notink if falsh: he has got a message box with this message :

        :example:

         Pas d'accès internet, "Vous devez être connecté à internet pour utiliser l'application"

        """


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
        
        .. figure:: _static/menu.png 
            :alt: example illustrate
             

            The first page.
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
        # Get the current selected text from the category combo box
        select = self.catcombo.currentText()
        # Check if the selected text is "Album"
        if select == "Album":
            # If so, call the recherche_album function with the text from the line edit widget
            self.recherche_album(self.line.text())
        # Check if the selected text is "Artiste"
        elif select == "Artiste" :
            # If so, call the recherche_artiste function with the text from the line edit widget
            self.recherche_artiste(self.line.text())
    



    def recherche_album(self, recherche):
        """        
        :param recherche: The user's input string
        :type recehrche: str
        :returns:  A table with the names and designations of all album with the given name
                
        :rtype: QTableWidget
        :raises: TypeError
        
        """
        # retrieve the albums and artistes data
        self.liste_albums = request_albums.get_album_name(recherche)
        self.liste_artistes = request_albums.get_artist_list(recherche)
        
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
        
        # Set main layout
        self.wid_table.setLayout(vbox)
        vbox.addWidget(self.table)
        wid_bouttons.setLayout(bouttonshbox)
        bouttonshbox.addWidget(searchButton, alignment=Qt.AlignLeft)
        vbox.addWidget(wid_bouttons, alignment= Qt.AlignLeft)
        
        # Set table properties
        headerH = ["Nom Artiste","Titre Album","Voir les Pistes"] 
        self.table.setHorizontalHeaderLabels(headerH)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # Add data to table and create 'voir' button
        for i in range(len(self.liste_artistes)):
            self.table.setItem(i, 0, QTableWidgetItem(self.liste_artistes[i]))
            self.table.setItem(i, 1, QTableWidgetItem(self.liste_albums[i]))
            selectButton = QPushButton("voir")
            selectButton.setIcon(QIcon(Fenetre_principale.newPath + "\go-last.png"))
            self.table.setCellWidget(i, 2, selectButton)
            selectButton.clicked.connect(lambda _, r=i+1, c=3: self.id_album(r, recherche))


    def recherche_artiste(self, recherche):
        """
        This function searches for artists with the given name and displays the information in a table.

        :param recherche: The name of the artist to search for
        :type recherche: str

        :returns: A table with the names and designations of all artists with the given name
        :rtype: QTableWidget
        :raises: TypeError
        

        .. code-block:: python

            recherche_artiste(self, "celine dion")
    
        .. figure:: _static/celine_dion.png 
            :alt: example illustrate
             

            The result of the search for artist "Celine Dion"
        """      
        self.dic_type = request_artistes.get_artist_id_type(recherche)
        self.dic_name = request_artistes.get_artist_name(recherche)

        #create an image and scale it to a specific size
        image1 = QPixmap(Fenetre_principale.newPath + "\logo_long_blanc.png" )
        image = image1.scaled(255, 68)
        #create a button for new search
        searchButton = QPushButton("Nouvelle recherche")
        searchButton.setStyleSheet("background-color: #E79E41; border-style: outset; border-width: 1px; width: 150px; height: 20px;")
        searchButton.clicked.connect(self.accueil)

        #create a widget for the artist
        self.wid_artiste = QWidget()
        self.wid_artiste.setStyleSheet("background-color: #202124")

        #create a widget for buttons
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

        #set the image in the label
        box_image.setPixmap(image)
        vbox.addWidget(box_image, alignment= Qt.AlignRight)

        # set the layout of the artist widget
        self.wid_artiste.setLayout(vbox)
        # add the table widget to the layout
        vbox.addWidget(self.table)

        # set the layout of the button widget
        wid_bouttons.setLayout(bouttonshbox)
        # add the search button to the button layout
        bouttonshbox.addWidget(searchButton, alignment=Qt.AlignLeft)
        # add the button widget to the main layout
        vbox.addWidget(wid_bouttons, alignment= Qt.AlignLeft)

        # set the headers for the table
        headerH = ["Nom Artiste","Désignation","Voir la discrographie"]
        self.table.setHorizontalHeaderLabels(headerH)

        # set the resize mode for the table headers
        header =self.table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)  

        # prevent editing of the table cells
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # populate the table with data from the dictionaries
        for row, i in enumerate(self.dic_name, start=1):
            self.table.setItem(row-1,0, QTableWidgetItem(self.dic_name[i]))
        for row, i in enumerate(self.dic_type, start=1):         
            self.table.setItem(row-1,1, QTableWidgetItem(self.dic_type[i]))
        # add a "voir" button to each row of the table
        for row, _ in enumerate(range(25), start=1):
            selectButton = QPushButton("voir")
            selectButton.setIcon(QIcon(Fenetre_principale.newPath + "\go-last.png"))
            self.table.setCellWidget(row-1,2,selectButton)
            selectButton.clicked.connect(lambda _, r=row, c=3: self.id_artiste(r, c, recherche))
    
    
    def id_artiste(self, row, column, recherche):
        """
        This function retrieves the number of the row when clicked, and retrieves the artist ID from the request_artistes module using the user's input.

        :param recherche: The user's input string
        :type recherche: str 
        :returns: A list of all artists with the same name and their types
        :param row: The number of the row that was clicked
        :type row: int
        :returns: The number of the row that was clicked
        :rtype: listing of artists with the same name
        :raises: TypeError if any input is of the wrong type
        """
        # Store the text of the item in the first column of the table at the current row
        self.artiste = self.table.item(row-1, 0).text()        
        
        # Retrieve the dictionary of artist IDs from the request_artistes module using the user's input
        dic = request_artistes.get_artist_id(recherche)

        # Retrieve the artist ID for the current row from the dictionary
        id = dic[row]

        # Call the discographie function with the current artist ID
        self.discographie(id)
        
    
  
    def discographie(self, id_artiste):
        """
        Display the discography corresponding to the given artist ID
        
        :param id_artiste: The ID of the artist whose discography should be displayed
        :type id_artiste: str
        :returns: None
        :rtype: None
        :raises: TypeError if id_artiste is not a string
        
        """
        # Create an image object from an image file and scale it to a specific size
        image1 = QPixmap(Fenetre_principale.newPath + "\logo_long_blanc.png" )
        image = image1.scaled(255, 68)

        # Create a button with the text "Nouvelle recherche" and set its style and connect it to the accueil method
        searchButton = QPushButton("Nouvelle recherche")
        searchButton.setStyleSheet("background-color: #E79E41; border-style: outset; border-width: 1px; width: 150px; height: 20px;")
        searchButton.clicked.connect(self.accueil)

        # Create a widget and set its background color
        self.wid_discographie = QWidget()
        self.wid_discographie.setStyleSheet("background-color: #202124")

        # Retrieve the list of albums for the current artist from the request_albums module
        self.liste_albums = request_albums.get_discographie(id_artiste)

        image1 = QPixmap(Fenetre_principale.newPath + "\logo_long_blanc.png" )
        image = image1.scaled(255, 68)
        searchButton = QPushButton("Nouvelle recherche")
        searchButton.setStyleSheet("background-color: #E79E41; border-style: outset; border-width: 1px; width: 150px; height: 20px;")
        searchButton.clicked.connect(self.accueil)

        self.wid_discographie = QWidget()
        self.wid_discographie.setStyleSheet("background-color: #202124")

        # Create a widget, layout and table to display the list of albums
        wid_bouttons = QWidget()
        vbox = QVBoxLayout()
        bouttonshbox = QHBoxLayout()
        box_image = QLabel()
        self.table = QTableWidget()

        # Set the number of rows in the table to the number of albums in the list
        row = len(self.liste_albums)
        self.table.setRowCount(row)
        self.table.setColumnCount(2)
        self.table.setContentsMargins(100, 200, 100, 0)
        self.table.setStyleSheet("QTableWidget::item {color: white;}")
        self.setCentralWidget(self.wid_discographie)

        # Set the image to be displayed in the box_image QLabel using the image QPixmap object
        box_image.setPixmap(image)
        # Add the box_image widget to the vbox layout with alignment set to the right
        vbox.addWidget(box_image, alignment= Qt.AlignRight)

        # Set the layout for the wid_discographie widget to be the vbox layout
        self.wid_discographie.setLayout(vbox)
        # Add the table widget to the vbox layout
        vbox.addWidget(self.table)

        # Set the layout for the wid_bouttons widget to be the bouttonshbox layout
        wid_bouttons.setLayout(bouttonshbox)

        # Add the searchButton widget to the bouttonshbox layout with alignment set to the left
        bouttonshbox.addWidget(searchButton, alignment=Qt.AlignLeft)

        # Add the wid_bouttons widget to the vbox layout with alignment set to the left
        vbox.addWidget(wid_bouttons, alignment= Qt.AlignLeft)

        # Set the horizontal header labels for the table to "Titre Album" and "Voir les Pistes"
        headerH = ["Titre Album","Voir les Pistes"]
        self.table.setHorizontalHeaderLabels(headerH)
        # Get the horizontal header of the table and set its section resize mode to resize to contents
        header = self.table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)
        # Disable editing of the table items
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)


        # Iterate through the list of albums and for each one, add a new row to the table and set the item in the first column to be the album title
        for row, i in enumerate(self.liste_albums, start=1):
            self.table.setItem(row-1,0, QTableWidgetItem(i))


        # Iterate through 25 rows and for each one, add a "voir" button with an icon to the second column of the table
        # Also connect the button to the get_pistes_by_album method, passing in the current row, column and id_artiste as arguments
        for row, _ in enumerate(range(25), start=1):
            selectButton = QPushButton("voir")
            selectButton.setIcon(QIcon(Fenetre_principale.newPath + "\go-last.png"))
            self.table.setCellWidget(row-1,1,selectButton)
            selectButton.clicked.connect(lambda _, r=row, c=3: self.get_pistes_by_album(r, c, id_artiste)) 
    
    
    def get_pistes_by_album(self,row ,column, id_artiste):
        """
        Retrieve the album tracks for the selected album and artist.
        
        :param row: The row number of the selected album in the table.
        :type row: int
        :param column: The column number of the selected album in the table.
        :type column: int
        :param id_artiste: The ID of the selected artist.
        :type id_artiste: str
        :returns: None
        :rtype: None
        """
        # Retrieve the dictionary of album IDs for the current artist from the request_albums module
        dic_album_id = request_albums.get_discographie(id_artiste)
        # Store the text of the item in the first column of the table at the current row
        self.nom_album = self.table.item(row-1, 0).text()
        # Retrieve the album ID for the current row from the dictionary
        album_id = dic_album_id[self.nom_album]
        # Retrieve the list of album tracks for the current album from the request_pistes module
        titres = request_pistes.get_album_titles(album_id)
        # Call the pistes function with the current album tracks
        self.pistes(titres, id_artiste)
        
        
    def pistes(self, titres, recherche):
        """
        attribute a number at piste 
        :param titre : title of piste 
        :type titre: str
        :param recherche: The user's input string
        :type recherche: int
        :returns: None
        :rtype: None
        
        """
        # Create a QPixmap of the logo image and scale it to the desired size
        image1 = QPixmap(Fenetre_principale.newPath + "\logo_long_blanc.png" )
        image = image1.scaled(255, 68)
        
        # Create a "New Search" button that, when clicked, will call the accueil function
        searchButton = QPushButton("Nouvelle recherche")
        searchButton.setStyleSheet("background-color: #E79E41; border-style: outset; border-width: 1px; width: 150px; height: 20px;")
        searchButton.clicked.connect(self.accueil)
        
        # Create a "Return to List" button that, when clicked, will call either the discographie or recherche_album function
        returnButton = QPushButton("Retour liste")
        returnButton.setStyleSheet("background-color: #E79E41; border-style: outset; border-width: 1px; width: 150px; height: 20px;")

        # Check the length of the search string to determine which function to call
        if len(recherche) == 36:
            returnButton.clicked.connect(lambda : self.discographie(recherche))
        else :
            returnButton.clicked.connect(lambda : self.recherche_album(recherche))

        # Create an "Upload" button that, when clicked, will call the action_upload function with the list of track titles as an argument
        uploadButton = QPushButton("Enregistrer")
        uploadButton.setStyleSheet("background-color: #E79E41; border-style: outset; border-width: 1px; width: 150px; height: 20px;")
        uploadButton.clicked.connect(lambda : self.action_upload(titres))

        # Create the main widget for the window and set its background color
        self.wid_pistes = QWidget()
        self.wid_pistes.setStyleSheet("background-color: #202124")

        # Create a vertical layout to hold the widgets
        vbox = QVBoxLayout()

        # Create a widget to hold the buttons and set its layout
        wid_bouttons = QWidget()
        bouttonshbox = QHBoxLayout()

        # Create a label to hold the album cover image
        box_image = QLabel()

        # Create a table widget to display the track titles and set its properties
        self.table = QTableWidget()
        self.table.setColumnCount(2)
        self.table.setContentsMargins(100, 200, 100, 0)
        self.table.setStyleSheet("QTableWidget::item {color: white;}")
        self.setCentralWidget(self.wid_pistes)

        # Set the album cover image to the label and add it to the layout
        box_image.setPixmap(image)
        vbox.addWidget(box_image, alignment= Qt.AlignRight)

        # Set the layout of the main widget and add the table widget to the layout
        self.wid_pistes.setLayout(vbox)
        vbox.addWidget(self.table)

        # Add the buttons to the button widget's layout
        wid_bouttons.setLayout(bouttonshbox)
        bouttonshbox.addWidget(searchButton)
        bouttonshbox.addWidget(returnButton)
        bouttonshbox.addWidget(uploadButton)

        # Add the button widget to the main layout and align it to the left
        vbox.addWidget(wid_bouttons, alignment= Qt.AlignLeft)

        # Set the alignment of the main layout to the top
        vbox.setAlignment(Qt.AlignTop)

        # Set the horizontal headers for the table widget
        headerH = ["Titres de l'Album","Ouvrir youtube"]
        self.table.setHorizontalHeaderLabels(headerH)

        # Set the table widget's horizontal header's resize mode
        header = self.table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)

        # Disable editing on the table widget
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # Set the number of rows in the table widget to the number of track titles
        nb_rows = len(titres)
        self.table.setRowCount(nb_rows)

        # Iterate through the track titles and add them to the table widget
        for row, i in enumerate(titres, start=1):
            self.table.setItem(row-1,0, QTableWidgetItem(i))

            # Create a button for each track title and add it to the table widget
            ytButton = QPushButton(QIcon(Fenetre_principale.newPath + "\youtube.jpg"),"")
            self.table.setCellWidget(row-1, 1, ytButton)
            ytButton.clicked.connect(lambda _, r=row, c=3: self.youtube(r, c, recherche)) 
                
    
    def id_album(self, row, recherche):
        """
        This function retrieves the album id based on the selected row and search query.
        
        :param row: The selected row in the table
        :type row: int
        :param recherche: The search query entered by the user
        :type recherche: str
        :returns: The album id
        :rtype: int
        :raises: TypeError
        """
        # Get the album name from the table
        self.nom_album = self.table.item(row-1, 1).text() 
        # Get the artist name from the table
        self.artiste = self.table.item(row-1, 0).text() 
        # Get a dictionary of album/artist based on the search query
        dic = request_albums.get_album_artist_dic(recherche) 
        # Get the album id from the dictionary using the artist name
        id = dic[self.artiste] 
        # Get a list of track titles for the album
        titres = request_pistes.get_album_titles(id)
        # Pass the track titles and search query to the pistes function
        self.pistes(titres, recherche) 
        
        
            
    def youtube(self, row, col, recherche):
        """
        This function searches for a song on YouTube
        
        :param row: the row of the selected song in the table
        :type row: int
        :param col: the col of the selected song in the table
        :type col: int
        :param recherche: the search term used to find the song
        :type recherche: str
        :returns: None
        """
        
        # get the name of the selected song from the table
        self.nom_piste = self.table.item(row-1, 0).text()
        # call the YouTube search function with the artist name and song name as the search term
        YS.yt_search(self.artiste, self.nom_piste)
    
     
    def action_openfolder(self) :
        """
        This function open forder 
        
        """
        os.startfile("")

        
        
    def action_clear(self):
        """
        This function clear th line edith
        """
        self.line.clear()

    def action_a_propos(self):
        """
        Display information about the application and its developers.

        """
        QMessageBox.information(self, "Onzzer Music Search Application", "Onzzer by Baptiste Tarte, Tim Mazzolini, Eliot Monneau, Matthieu Brissonnet")
            


    def action_upload(self, titres):
        """
        This function saves all tracks from an album in a .txt file.
        
        :param titres: A list of track names
        :type titres: list
        :returns: A .txt file containing the track names
        """
        
        # create the file name
        nom_base = f"{self.nom_album} - {self.artiste}.txt"

        # open a file dialog to choose where to save the file
        file_path, _ = QFileDialog.getSaveFileName(self, "Save File", nom_base, "Text Files (*.txt)")

        # write the track list to the file
        with open(file_path, "w") as fichier:
            fichier.write(
                f"Liste de chansons de l'album {self.nom_album} de l'artiste {self.artiste}"
                + "\n"
            )
            for i in titres:
                fichier.write("\n->" + i)

        # get the file name and show a message box with the file name
        filename = QFileInfo(file_path).fileName()
        QMessageBox.information(
            self, "Et voilà", f"Fichier écrit avec le nom {filename}"
        )

     

    
    def center(self):
        """
        Center the window on the screen
        
        :param self: The current instance of the class
        :type self: object
        """
        # get the rectangle of the main window
        qr = self.frameGeometry()
        # get the center point of the screen
        cp = QDesktopWidget().availableGeometry().center()
        # move the rectangle's center point to the screen's center point
        qr.moveCenter(cp)
        # move the main window to the top left point of the rectangle
        self.move(qr.topLeft())

    # def resource_path(relative_path):

    #     """ 
    #     Get absolute path to resource, works for dev and for PyInstaller 
        
    #     """
    #     try:
    #         base_path = sys._MEIPASS
    #     except Exception:
    #         base_path = os.path.abspath(".")

    #     return os.path.join(base_path, relative_path)

        
        

def main():
    # Create an instance of QApplication, which manages the GUI application's control flow and main settings
    application = QApplication(sys.argv)
    # Create an instance of Fenetre_principale, which is the main window of the application
    fenetre = Fenetre_principale()
    # Show the main window
    fenetre.show()
    # Exit the application and return the specified exit code
    sys.exit(application.exec_())
        
if __name__ == '__main__':
    main()