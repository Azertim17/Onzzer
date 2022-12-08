import sys 
import os
from PyQt5.QtWidgets import QVBoxLayout, QGridLayout, QPushButton, QDesktopWidget, QFileDialog
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QAction, QToolBar, QStackedLayout
from PyQt5.QtWidgets import QLabel, QLineEdit, QPlainTextEdit, QTableView, QAbstractItemView, QComboBox
from PyQt5.QtWidgets import QMessageBox, QTableWidget, QTableWidgetItem, QHeaderView, QHBoxLayout
from PyQt5.QtGui import QIcon, QPixmap, QPixmap
from PyQt5.QtCore import Qt, QFileInfo
import request_albums
import request_pistes
import request_artistes
import youtube_search as YS


class Fenetre_principale(QMainWindow):
    
    def __init__(self):
    
        super().__init__()
        self.setWindowTitle("Onzzer")
        self.setWindowIcon(QIcon('Icones/logo.png'))
        self.setGeometry(600,100,800,800)
        self.menu()
        self.accueil()
        self.center()


        
    def menu(self):
        eraseButton = QAction(QIcon('Icones/edit-undo.png'), 'Effacer', self)
        eraseButton.setShortcut('Ctrl+N')
        openButton = QAction(QIcon('Icones/mail-send.png'), "Ouvrir l'emplacement d'enregistrement", self)
        openButton.setShortcut('Ctrl+O')
        exitButton = QAction(QIcon('Icones/application-exit.png'), 'Quitter', self)
        exitButton.setShortcut('Ctrl+Q')
        manButton = QAction('A Propos', self)
        manButton.setShortcut('F1')
        
        eraseButton.triggered.connect(self.action_clear)
        exitButton.triggered.connect(self.close)
        openButton.triggered.connect(self.action_openfolder)
        manButton.triggered.connect(self.action_a_propos)

        menu = self.menuBar()
        menufichier = menu.addMenu("&Fichier")
        menufichier.addAction(eraseButton)
        menufichier.addAction(openButton)
        menufichier.addAction(exitButton)
        
        menuAide = menu.addMenu("&Aide")
        menuAide.addAction(manButton)
               
        toolbar = QToolBar("Ma barre d'outils")
        self.addToolBar(toolbar)
        toolbar.addAction(eraseButton)
        toolbar.addAction(exitButton)
        
        menu.setStyleSheet("background-color: #3655B2")
        toolbar.setStyleSheet("background-color: #3655B2")
        


    def accueil(self):
        
        image = QPixmap('Icones/logo_long_blanc.png')
        self.catcombo = QComboBox()
        self.catcombo.addItems(["Album" , "Artiste" , "Chanson"])
        # self.catcombo.activated.connect(self.categorie)

        self.searchButton = QPushButton("Recherche") 
        self.line = QLineEdit()         
        self.wid_onzzer = QWidget()
        self.wid_onzzer.setStyleSheet("background-color: #202124")

        vbox = QVBoxLayout()
        wid_grid = QWidget()
        grid = QGridLayout()
        box_image = QLabel()
        self.setCentralWidget(self.wid_onzzer)
        
        self.wid_onzzer.setLayout(vbox)
        box_image.setPixmap(image)
        box_image.setAlignment(Qt.AlignCenter)
        
        grid.addWidget(self.line, 0, 0, 1, 3)
        grid.addWidget(self.searchButton, 1, 1, 1, 2)
        grid.addWidget(self.catcombo, 0, 4)
        wid_grid.setLayout(grid)
        
        vbox.addWidget(box_image, alignment= Qt.AlignBottom)
        vbox.setAlignment(Qt.AlignCenter)
        vbox.addWidget(wid_grid, alignment= Qt.AlignCenter)

        self.searchButton.setStyleSheet("background-color: #E79E41; border-style: outset; border-width: 1px; height: 20px;")
        self.searchButton.clicked.connect(self.categorie)

        self.catcombo.setStyleSheet("background-color: white; border-style: outset; height: 22px;")

        wid_grid.setFixedWidth(600)
        box_image.setFixedWidth(600)
        
        self.line.setStyleSheet("background-color: white;")


    def categorie(self):
        select = self.catcombo.currentText()
        
        if select == "Album":
            self.recherche_album(self.line.text())

        elif select == "Artiste" :
            self.recherche_artiste(self.line.text())
        
        elif select == "Chanson" :
            self.recherche_chanson(self.line.text())
            
    
    
    
    
    def recherche_artiste(self, recherche):
    
        
        image1 = QPixmap('Icones/logo_long_blanc.png' ) 
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
        self.table.setRowCount(25)
        self.table.setColumnCount(3)
        self.table.setContentsMargins(100, 200, 100, 0)
        self.table.setStyleSheet("background-color: #D0D1D2")
        self.setCentralWidget(self.wid_artiste)
        
        box_image.setPixmap(image)
        vbox.addWidget(box_image, alignment= Qt.AlignRight)
  
        self.wid_artiste.setLayout(vbox)
        vbox.addWidget(self.table)

        wid_bouttons.setLayout(bouttonshbox)
        
        bouttonshbox.addWidget(searchButton, alignment=Qt.AlignLeft)
        
        vbox.addWidget(wid_bouttons, alignment= Qt.AlignLeft)
        
        headerH = ["Nom Artiste","Titre Album","Voir les Pistes"]
        self.table.setHorizontalHeaderLabels(headerH)
        
        header =self.table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)  

        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        
        
        self.dic = request_artistes.get_artiste_id(self, recherche)
        print(self.dic)
        
        # row = 0
        # for i in self.liste_artistes:
        #     row += 1
        #     self.table.setItem(row-1,0, QTableWidgetItem(i))

        # row = 0  
        # for i in self.liste_albums:             
        #     row += 1
        #     self.table.setItem(row-1,1, QTableWidgetItem(i))
                      
        # row = 0
        # for i in range(0,25):             
        
        #     row += 1
            
        #     selectButton = QPushButton("voir")
        #     selectButton.setIcon(QIcon('Icones/go-last.png'))
        #     self.table.setCellWidget(row-1,2,selectButton)
        #     selectButton.clicked.connect(lambda _, r=row, c=3: self.id_album(r, c, recherche)) 
    
    
    
    
    
        
    def recherche_album(self, recherche):
    
        image1 = QPixmap('Icones/logo_long_blanc.png' ) 
        image = image1.scaled(255, 68)
        searchButton = QPushButton("Nouvelle recherche")
        searchButton.setStyleSheet("background-color: #E79E41; border-style: outset; border-width: 1px; width: 150px; height: 20px;")
        searchButton.clicked.connect(self.accueil)
        
        self.wid_table = QWidget()
        self.wid_table.setStyleSheet("background-color: #202124")

        wid_bouttons = QWidget()
        vbox = QVBoxLayout()
        bouttonshbox = QHBoxLayout()
        box_image = QLabel()
        self.table = QTableWidget()
        self.table.setRowCount(25)
        self.table.setColumnCount(3)
        self.table.setContentsMargins(100, 200, 100, 0)
        self.table.setStyleSheet("background-color: #D0D1D2")
        self.setCentralWidget(self.wid_table)
        
        box_image.setPixmap(image)
        vbox.addWidget(box_image, alignment= Qt.AlignRight)
  
        self.wid_table.setLayout(vbox)
        vbox.addWidget(self.table)

        wid_bouttons.setLayout(bouttonshbox)
        
        bouttonshbox.addWidget(searchButton, alignment=Qt.AlignLeft)
        
        vbox.addWidget(wid_bouttons, alignment= Qt.AlignLeft)
        
        headerH = ["Nom Artiste","Titre Album","Voir les Pistes"]
        self.table.setHorizontalHeaderLabels(headerH)
        
        header =self.table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)  

        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        
        
        self.liste_albums = request_albums.get_nom_album(self, recherche)
        self.liste_artistes = request_albums.get_liste_artiste(self, recherche)
        
        
        row = 0
        for i in self.liste_artistes:
            row += 1
            self.table.setItem(row-1,0, QTableWidgetItem(i))

        row = 0  
        for i in self.liste_albums:             
            row += 1
            self.table.setItem(row-1,1, QTableWidgetItem(i))
                      
        row = 0
        for i in range(0,25):             
            row += 1
            
            selectButton = QPushButton("voir")
            selectButton.setIcon(QIcon('Icones/go-last.png'))
            self.table.setCellWidget(row-1,2,selectButton)
            selectButton.clicked.connect(lambda _, r=row, c=3: self.id_album(r, c, recherche)) 

        
        
    def reponse(self, titres, recherche):
        
        image1 = QPixmap('Icones/logo_long_blanc.png' ) 
        image = image1.scaled(255, 68)
        searchButton = QPushButton("Nouvelle recherche")
        searchButton.setStyleSheet("background-color: #E79E41; border-style: outset; border-width: 1px; width: 150px; height: 20px;")
        searchButton.clicked.connect(self.accueil)
        returnButton = QPushButton("Retour liste")
        returnButton.setStyleSheet("background-color: #E79E41; border-style: outset; border-width: 1px; width: 150px; height: 20px;")
        returnButton.clicked.connect(lambda : self.tableau(recherche))
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
        self.table.setStyleSheet("background-color: #D0D1D2")
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
            
            ytButton = QPushButton(QIcon("Icones/youtube.jpg"),"")
            self.table.setCellWidget(row-1, 1, ytButton)
            ytButton.clicked.connect(lambda _, r=row, c=3: self.youtube(r, c, recherche)) 

                
    
    def id_album(self, row, col, recherche):
        
        self.nom_album = self.table.item(row-1, 1).text()
        self.artiste = self.table.item(row-1, 0).text()
        dic = request_albums.get_dic_album_id_artiste(self, recherche)
        id = dic[self.artiste]
        titres = request_pistes.get_pistes_album(id)
        self.reponse(titres, recherche)
        
        
    def youtube(self, row, col, recherche):
        
        self.nom_piste = self.table.item(row-1, 0).text()
        YS.yt_search(self, self.artiste, self.nom_piste)
    
     
    def action_openfolder(self) :
        os.startfile('..\Onzzer\Icones')
        
        
    def action_clear(self):
        self.line.clear()

    def action_a_propos(self):
        QMessageBox.information(self,"Onzzer Application de Recherche Musicale", "Onzzer par Baptiste Tarte, Tim Mazzolini, Eliot Monneau, Matthieu Brissonnet")
        
        
    def action_upload(self, titres):
        
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
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

        
        
def main():
    application = QApplication(sys.argv)
    fenetre = Fenetre_principale()
    fenetre.show()
    sys.exit(application.exec())
        
if __name__ == '__main__':
    main()






















