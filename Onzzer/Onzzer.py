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
        self.setWindowTitle("Onzzer")
        self.setWindowIcon(QIcon('Icones/logo.png'))
        self.resize(1000,800)
        self.menu()


        
    
    def menu(self):
        eraseButton = QAction(QIcon('Icones/edit-undo.png'), 'Effacer', self)
        eraseButton.setShortcut('Ctrl+N')
        eraseButton.setStatusTip('Ouvrir un fichier')

        openButton = QAction(QIcon('Icones/mail-send.png'), 'Envoyer', self)
        openButton.setShortcut('Ctrl+O')
        openButton.setStatusTip("Ouvrir l'emplacement d'enregistrement")
        
        exitButton = QAction(QIcon('Icones/application-exit.png'), 'Quitter', self)
        exitButton.setShortcut('Ctrl+Q')
        exitButton.setStatusTip('Exit application')


        serverButton = QAction('Serveur SMTP', self)
        serverButton.setShortcut('Ctrl+X')
        
        expButton = QAction('Expéditeur', self)
        expButton.setShortcut('Ctrl+C')
        
        signButton = QAction('Signature', self)
        signButton.setShortcut('Ctrl+V')
        
        manButton = QAction('A Propos', self)
        manButton.setShortcut('F1')
        manButton.triggered.connect(self.action_a_propos)
        

        exitButton.triggered.connect(self.close)

        menu = self.menuBar()
        menufichier = menu.addMenu("&Fichier")
        menufichier.addAction(eraseButton)
        menufichier.addAction(openButton)
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
        toolbar.addAction(openButton)
       


    #def action_clear():


    def action_a_propos(self):
            
        QMessageBox.information(self,"Onzzer Application de Recherche Musicale", "Tout un programme !")


def main():
    application = QApplication(sys.argv)
    fenetre = MaPremiereAppli()
    fenetre.show()
    sys.exit(application.exec())
        
if __name__ == '__main__':
    main()



















































