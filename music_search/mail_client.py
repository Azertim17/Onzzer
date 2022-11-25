#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 08:46:58 2022

@author: Tim
"""

import sys 
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QFormLayout, QGridLayout
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QMenu, QAction, QToolBar, QDockWidget
from PyQt5.QtWidgets import QLabel, QLineEdit, QTextEdit, QGroupBox
from PyQt5.QtWidgets import QMessageBox, QInputDialog

from PyQt5.QtGui import QCursor, QIcon, QPixmap, QKeySequence
from PyQt5.QtCore import Qt, QDir


class MaPremiereAppli(QMainWindow):

    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mon éditeur")
        self.setWindowIcon(QIcon('Icones/icone-appli.png'))
        self.resize(1000,800)
        self.menu()


        
    
    def menu(self):
        eraseButton = QAction(QIcon('Icones/edit-undo.png'), 'Effacer', self)
        eraseButton.setShortcut('Ctrl+N')
        eraseButton.setStatusTip('Ouvrir un fichier')
        # newButton.triggered.connect()

        sendButton = QAction(QIcon('Icones/mail-send.png'), 'Envoyer', self)
        sendButton.setShortcut('Ctrl+O')
        sendButton.setStatusTip('Ouvrir un fichier')
        # openButton.triggered.connect()

        
        exitButton = QAction(QIcon('Icones/application-exit.png'), 'Quitter', self)
        exitButton.setShortcut('Ctrl+Q')
        exitButton.setStatusTip('Exit application')
        exitButton.triggered.connect(self.close)




        serverButton = QAction('Serveur SMTP', self)
        serverButton.setShortcut('Ctrl+X')
        
        expButton = QAction('Expéditeur', self)
        expButton.setShortcut('Ctrl+C')
        
        signButton = QAction('Signature', self)
        signButton.setShortcut('Ctrl+V')
        
        manButton = QAction('A Propos', self)
        manButton.setShortcut('F1')
        manButton.triggered.connect(self.man)
        


        
        menu = self.menuBar()
        menufichier = menu.addMenu("&Fichier")
        menufichier.addAction(eraseButton)
        menufichier.addAction(sendButton)
        menufichier.addAction(exitButton)
        
        menuedition = menu.addMenu("&Parametres")
        menuedition.addAction(serverButton)
        menuedition.addAction(expButton)
        menuedition.addAction(signButton)
        
        menuAide = menu.addMenu("&Aide")
        menuAide.addAction(manButton)
               
        toolbar = QToolBar("Ma barre d'outils")
        self.addToolBar(toolbar)
        toolbar.addAction(eraseButton)
        toolbar.addAction(sendButton)
        



        texte = QTextEdit()
        
        
        mail = QWidget()
        self.setCentralWidget(mail)
        
        mailVbox = QVBoxLayout()
        mail.setLayout(mailVbox)
        
        entete = QGroupBox("Entête du mail")
        layform = QGridLayout()
        
        entete.setLayout(layform)
        
        de = QLabel("De :")
        de2 = QLineEdit()
        
        layform.addWidget(de, 1, 1)
        layform.addWidget(de2, 2, 1)
        
        
        
        mailVbox.addWidget(entete)
        mailVbox.addWidget(texte)
        
            
        
        
        
    def man(self):
            
        QMessageBox.information(self,"A propos", "Tout un programme !")



def main():
    application = QApplication(sys.argv)
    fenetre = MaPremiereAppli()
    fenetre.show()
    sys.exit(application.exec())
        
if __name__ == '__main__':
    main()



















































