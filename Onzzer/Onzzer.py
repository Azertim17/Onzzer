import sys 
import os
from PyQt5.QtWidgets import QVBoxLayout, QGridLayout, QPushButton, QDesktopWidget
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QAction, QToolBar
from PyQt5.QtWidgets import QLabel, QLineEdit, QPlainTextEdit, QTableView, QAbstractItemView
from PyQt5.QtWidgets import QMessageBox, QTableWidget, QTableWidgetItem, QHeaderView, QHBoxLayout
from PyQt5.QtGui import QIcon, QPixmap, QPixmap
from PyQt5.QtCore import Qt
import request_albums



class Fenetre_principale(QMainWindow):
    
    def __init__(self):
    
        super().__init__()
        self.setWindowTitle("Onzzer")
        self.setWindowIcon(QIcon('Icones/logo.png'))
        self.setGeometry(600,100,800,800)
        self.setStyleSheet("background-color: #202124")
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
        searchButton = QPushButton("Recherche") 
        self.line = QLineEdit()         
                
        self.wid_onzzer = QWidget()
        vbox = QVBoxLayout()
        wid_grid = QWidget()
        grid = QGridLayout()
        box_image = QLabel()
        self.setCentralWidget(self.wid_onzzer)
        
        self.wid_onzzer.setLayout(vbox)
        box_image.setPixmap(image)
        box_image.setAlignment(Qt.AlignCenter)
        
        grid.addWidget(self.line, 0, 0, 1, 3)
        grid.addWidget(searchButton, 0, 4)
        wid_grid.setLayout(grid)
        
        vbox.addWidget(box_image, alignment= Qt.AlignBottom)
        vbox.setAlignment(Qt.AlignCenter)
        vbox.addWidget(wid_grid, alignment= Qt.AlignCenter)

        searchButton.setStyleSheet("background-color: #E79E41; border-style: outset; border-width: 1px; height: 20px;")
        searchButton.clicked.connect(self.action_fen2)

        wid_grid.setFixedWidth(600)
        box_image.setFixedWidth(600)
        
        self.line.setStyleSheet("background-color: white;")
        
        
 
        
    def tableau(self):

        

        image1 = QPixmap('Icones/logo_long_blanc.png' ) 
        image = image1.scaled(255, 68)
        searchButton = QPushButton("Nouvelle recherche")
        searchButton.setStyleSheet("background-color: #E79E41; border-style: outset; border-width: 1px; width: 150px; height: 20px;")
        searchButton.clicked.connect(self.action_nouv_rech)
        
        self.wid_table = QWidget()
        wid_bouttons = QWidget()
        vbox = QVBoxLayout()
        bouttonshbox = QHBoxLayout()
        box_image = QLabel()
        table = QTableWidget()
        table.setRowCount(10)
        table.setColumnCount(2)
        table.setContentsMargins(100, 200, 100, 0)
        table.setStyleSheet("background-color: #D0D1D2")
        self.setCentralWidget(self.wid_table)
        
        box_image.setPixmap(image)
        vbox.addWidget(box_image, alignment= Qt.AlignRight)
  
        self.wid_table.setLayout(vbox)
        vbox.addWidget(table)

        wid_bouttons.setLayout(bouttonshbox)
        
        bouttonshbox.addWidget(searchButton, alignment=Qt.AlignLeft)
        
        vbox.addWidget(wid_bouttons, alignment= Qt.AlignLeft)
        
        headerH = ["Nom Artiste","Titre Albums"]
        table.setHorizontalHeaderLabels(headerH)
        
        header = table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)  

        table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        

        for i in self.album_id:


            albumButton = QPushButton("self.nom_album")
            albumButton.clicked.connect(self.action_resulat)
            
            table.setItem(0,0, QTableWidgetItem("Stromae"))
            table.setCellWidget(0,1,albumButton)
        
    
        
        
    def reponse(self):
        
        image1 = QPixmap('Icones/logo_long_blanc.png' ) 
        image = image1.scaled(255, 68)
        searchButton = QPushButton("Nouvelle recherche")
        searchButton.setStyleSheet("background-color: #E79E41; border-style: outset; border-width: 1px; width: 150px; height: 20px;")
        searchButton.clicked.connect(self.action_nouv_rech)
        returnButton = QPushButton("Retour liste")
        returnButton.setStyleSheet("background-color: #E79E41; border-style: outset; border-width: 1px; width: 150px; height: 20px;")
        returnButton.clicked.connect(self.action_return)
        uploadButton = QPushButton("Enregistrer")
        uploadButton.setStyleSheet("background-color: #E79E41; border-style: outset; border-width: 1px; width: 150px; height: 20px;")
        uploadButton.clicked.connect(self.action_upload)
        
        self.wid_table = QWidget()
        vbox = QVBoxLayout()
        wid_bouttons = QWidget()
        bouttonshbox = QHBoxLayout()
        box_image = QLabel()
        table = QTableWidget()
        table.setRowCount(10)
        table.setColumnCount(1)
        table.setContentsMargins(100, 200, 100, 0)
        table.setStyleSheet("background-color: #D0D1D2")
        self.setCentralWidget(self.wid_table)
        
        box_image.setPixmap(image)
        vbox.addWidget(box_image, alignment= Qt.AlignRight)
  
        self.wid_table.setLayout(vbox)
        vbox.addWidget(table)
        
        wid_bouttons.setLayout(bouttonshbox)
        bouttonshbox.addWidget(searchButton)
        bouttonshbox.addWidget(returnButton)
        bouttonshbox.addWidget(uploadButton)

        vbox.addWidget(wid_bouttons, alignment= Qt.AlignLeft)
        vbox.setAlignment(Qt.AlignTop)

        headerH = ["Titres de l'Album"]
        table.setHorizontalHeaderLabels(headerH)
        
        header = table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)  


        table.setItem(0,0, QTableWidgetItem('Santé'))
        
        
        
     
    def action_openfolder(self) :
        os.startfile('..\Onzzer\Icones')
        
        
    def action_clear(self):
        self.line.clear()

    def action_a_propos(self):
        QMessageBox.information(self,"Onzzer Application de Recherche Musicale", "Onzzer par Baptiste Tarte, Tim Mazzolini, Eliot Monneau, Matthieu Brissonnet")
        
    def action_return(self):
        self.wid_table.close() 
        self.tableau()

    def action_fen2(self):
        self.wid_onzzer.close() 
        self.tableau()
        self.recherche = self.line.text()
        print(self.recherche)
        request_albums.get_albums(self, self.recherche)
    
    def action_nouv_rech(self):
        self.wid_table.close()
        self.accueil()

    def action_resulat(self):
        self.wid_table.close()
        self.reponse()
        
    def action_upload(self):
        os.startfile('..\Onzzer\Icones')

    
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






















