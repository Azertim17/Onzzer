import sys 
import os
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QFormLayout, QGridLayout, QPushButton
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QMenu, QAction, QToolBar, QDockWidget
from PyQt5.QtWidgets import QLabel, QLineEdit, QTextEdit, QGroupBox
from PyQt5.QtWidgets import QMessageBox, QInputDialog
from PyQt5.QtGui import QCursor, QIcon, QPixmap, QKeySequence, QPixmap
from PyQt5.QtCore import Qt, QDir
import onzzer


class Fenetre_principale(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Onzzer")
        self.setWindowIcon(QIcon('Icones/logo.png'))
        #self.setStyleSheet("background-color: Blue;")
        self.setGeometry(600,300,500,500)
        self.menu()
        self.central()    

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



    def central(self):
        
        self.wid_onzzer = QWidget()
        grid_box = QGridLayout()
        box_image = QLabel()
        image = QPixmap('Icones/logo_long.png')
        wid_search = QWidget()
        self.line = QLineEdit()
        searchButton = QPushButton("Recherche")
        self.setCentralWidget(self.wid_onzzer)

        self.wid_onzzer.setLayout(grid_box)
        box_image.setPixmap(image)
        
        grid_box.addWidget(box_image, 0, 2)
        grid_box.addWidget(self.line, 1, 1, 1, 3)
        grid_box.addWidget(searchButton, 1, 4)
        grid_box.setVerticalSpacing(2)

        self.wid_onzzer.setFixedWidth(800)
        self.line.setStyleSheet("background-color: white;")
        searchButton.setStyleSheet("background-color: white; border-style: outset; border-width: 1px;")
        searchButton.clicked.connect(self.action_fen2)

    
    def action_openfolder(self) :
        os.system("%SystemRoot%\explorer.exe /n,/e, monurl")
       
    def action_clear(self):
        self.line.clear()

    def action_a_propos(self):
        QMessageBox.information(self,"Onzzer Application de Recherche Musicale", "Onzzer par Baptiste Tarte, Tim Mazzolini, Eliot Monneau, Matthieu Brissonnet")

    def action_fen2(self):
        self.wid_onzzer.close() 
        self.bloc()



    def bloc (self):
        bloc1 = QWidget()
        self.setCentralWidget(bloc1)
        bloc1_lay = QVBoxLayout()
        bloc1.setLayout(bloc1_lay)

        bloc2= QWidget()
        bloc1_lay.addWidget(bloc2)
        logo_onzzer = QLabel(self)
        pixmap = QPixmap('Icones/logo.png')
        logo_onzzer.setPixmap(pixmap)
        self.setCentralWidget(logo_onzzer)



def main():
    application = QApplication(sys.argv)
    fenetre = Fenetre_principale()
    fenetre.show()
    sys.exit(application.exec())
        
if __name__ == '__main__':
    main()



















































