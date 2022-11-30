import sys 
import os
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QFormLayout, QGridLayout
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QMenu, QAction, QToolBar, QDockWidget
from PyQt5.QtWidgets import QLabel, QLineEdit, QTextEdit, QGroupBox
from PyQt5.QtWidgets import QMessageBox, QInputDialog
from PyQt5.QtGui import QCursor, QIcon, QPixmap, QKeySequence 
from PyQt5.QtCore import Qt, QDir

from onzzer.onzzer import MaPremiereAppli



class Fenetre2(QMainWindow):

    def __init__(self):
        super(Fenetre2,self).__init__(MaPremiereAppli)
        self.setWindowTitle("Onzzer")
        self.setWindowIcon(QIcon('Icones/logo.png'))
        self.resize(1000,800)
        self.menu()
        self.bloc()

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

    def action_openfolder(self) :
        os.system("%SystemRoot%\explorer.exe /n,/e, monurl")
       

    def action_a_propos(self):
        QMessageBox.information(self,"Onzzer Application de Recherche Musicale", "Onzzer par Baptiste Tarte, Tim Mazzolini, Eliot Monneau, Matthieu Brissonnet")


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
        





        

        
        



    #def action_clear():


    def action_a_propos(self):
            
        QMessageBox.information(self,"Onzzer Application de Recherche Musicale", "onzzer par Baptiste Tarte, Tim Mazzolini, Eliot Monneau, Matthieu Brissonnet")


def main():
    application = QApplication(sys.argv)
    fenetre = MaPremiereAppli()
    fenetre.show()
    sys.exit(application.exec())
        
if __name__ == '__main__':
    main()



















































