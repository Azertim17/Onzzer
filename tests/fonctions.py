import sys 
import os
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QFormLayout, QGridLayout
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QMenu, QAction, QToolBar, QDockWidget
from PyQt5.QtWidgets import QLabel, QLineEdit, QTextEdit, QGroupBox
from PyQt5.QtWidgets import QMessageBox, QInputDialog, QPushButton
from PyQt5.QtGui import QCursor, QIcon, QPixmap, QKeySequence 
from PyQt5.QtCore import Qt, QDir
import fonctions





def menu(self):
    eraseButton = QAction(QIcon('Icones/edit-undo.png'), 'Effacer', self)
    eraseButton.setShortcut('Ctrl+N')
    openButton = QAction(QIcon('Icones/mail-send.png'), "Ouvrir l'emplacement d'enregistrement", self)
    openButton.setShortcut('Ctrl+O')
    exitButton = QAction(QIcon('Icones/application-exit.png'), 'Quitter', self)
    exitButton.setShortcut('Ctrl+Q')
    manButton = QAction('A Propos', self)
    manButton.setShortcut('F1')
    
    exitButton.triggered.connect(self.close)
    openButton.triggered.connect(fonctions.action_openfolder)
    manButton.triggered.connect(fonctions.action_a_propos)
    eraseButton.triggered.connect(fonctions.action_clear)



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

    self.show()



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

    self.show()
    

def central(self):
    
    wid_onzzer = QWidget()
    grid_box = QGridLayout()
    box_image = QLabel()
    line = QLineEdit()
    image = QPixmap('Icones/logo_long.png')
    wid_search = QWidget()

    searchButton = QPushButton("Recherche")
    self.setCentralWidget(wid_onzzer)
    wid_onzzer.setLayout(grid_box)
    box_image.setPixmap(image)
    
    grid_box.addWidget(box_image, 0, 2)
    grid_box.addWidget(line, 1, 1, 1, 3)
    grid_box.addWidget(searchButton, 1, 4)
    grid_box.setVerticalSpacing(2)
    wid_onzzer.setFixedWidth(800)
    line.setStyleSheet("background-color: white;")
    searchButton.setStyleSheet("background-color: white; border-style: outset; border-width: 1px;")

    self.show()


def action_openfolder(self) :
    os.system("%SystemRoot%\explorer.exe /n,/e, monurl")
   
def action_clear(line):
    line.clear()

def action_a_propos(self):
    QMessageBox.information(self,"Onzzer Application de Recherche Musicale", "Onzzer par Baptiste Tarte, Tim Mazzolini, Eliot Monneau, Matthieu Brissonnet")
















































