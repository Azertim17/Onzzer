import sys 
import os
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QFormLayout, QGridLayout, QPushButton
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QMenu, QAction, QToolBar, QDockWidget
from PyQt5.QtWidgets import QLabel, QLineEdit, QTextEdit, QGroupBox
from PyQt5.QtWidgets import QMessageBox, QInputDialog, QTableWidget, QTableWidgetItem, QHeaderView
from PyQt5.QtGui import QCursor, QIcon, QPixmap, QKeySequence, QPixmap, QLinearGradient
from PyQt5.QtCore import Qt, QDir
import onzzer


class Fenetre_principale(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Onzzer")
        self.setWindowIcon(QIcon('../onzzer/Icones/logo.png'))
        #self.setStyleSheet("background-color: Blue;")
        self.setGeometry(600,100,800,800)
        self.setStyleSheet("background-color: black")
        self.menu()
        self.accueil()

    def menu(self):
        eraseButton = QAction(QIcon('../onzzer/Icones/edit-undo.png'), 'Effacer', self)
        eraseButton.setShortcut('Ctrl+N')
        openButton = QAction(QIcon('../onzzer/Icones/mail-send.png'), "Ouvrir l'emplacement d'enregistrement", self)
        openButton.setShortcut('Ctrl+O')
        exitButton = QAction(QIcon('../onzzer/Icones/application-exit.png'), 'Quitter', self)
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
        
        menu.setStyleSheet("background-color: grey")
        toolbar.setStyleSheet("background-color: grey")
        


    def accueil(self):
        
        image = QPixmap('../onzzer/Icones/logo_long.png')
        searchButton = QPushButton("Recherche") 
        line = QLineEdit()          

        self.wid_onzzer = QWidget()
        vbox = QVBoxLayout()
        wid_grid = QWidget()
        grid = QGridLayout()
        box_image = QLabel()
        self.setCentralWidget(self.wid_onzzer)
        
        self.wid_onzzer.setLayout(vbox)
        box_image.setPixmap(image)
        box_image.setAlignment(Qt.AlignCenter)

        grid.addWidget(line, 0, 0, 1, 3)
        grid.addWidget(searchButton, 0, 4)
        wid_grid.setLayout(grid)
        
        vbox.addWidget(box_image, alignment= Qt.AlignBottom)
        vbox.addWidget(wid_grid, alignment= Qt.AlignCenter)

        searchButton.setStyleSheet("background-color: white; border-style: outset; border-width: 1px;")
        searchButton.clicked.connect(self.action_fen2)
        
        wid_grid.setFixedWidth(800)
        box_image.setFixedWidth(800)
        
        line.setStyleSheet("background-color: white")
        #self.wid_onzzer.setFixedSize(600, 800)
        #self.wid_onzzer.setContentsMargins(0 , 50, 0, 0)
        
        #box_image.resize(200, 10)        
        
    def tableau(self):

        table = QTableWidget()
        table.setRowCount(10)
        table.setColumnCount(1)
        table.setGeometry(150 , 150 , 300 ,500)
        table.setContentsMargins( 100, 200, 100, 0)
        self.setCentralWidget(table)

        headerH = ["Albums correspondants"]
        table.setHorizontalHeaderLabels(headerH)
        
        header = table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)       


        table.setItem(0,0, QTableWidgetItem(''))
    


    def action_openfolder(self) :
        os.system("%SystemRoot%\explorer.exe /n,/e, monurl")
       
    def action_clear(self):
        self.line.clear()

    def action_a_propos(self):
        QMessageBox.information(self,"Onzzer Application de Recherche Musicale", "Onzzer par Baptiste Tarte, Tim Mazzolini, Eliot Monneau, Matthieu Brissonnet")

    def action_fen2(self):
        self.wid_onzzer.close() 
        self.tableau()



def main():
    application = QApplication(sys.argv)
    fenetre = Fenetre_principale()
    fenetre.show()
    sys.exit(application.exec())
        
if __name__ == '__main__':
    main()






















