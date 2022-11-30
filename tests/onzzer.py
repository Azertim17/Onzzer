import sys 
import os
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QFormLayout, QGridLayout, QPushButton
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QMenu, QAction, QToolBar, QDockWidget
from PyQt5.QtWidgets import QLabel, QLineEdit, QTextEdit, QGroupBox
from PyQt5.QtWidgets import QMessageBox, QInputDialog
from PyQt5.QtGui import QCursor, QIcon, QPixmap, QKeySequence, QPixmap
from PyQt5.QtCore import Qt, QDir
import fonctions


class Fenetre_principale(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Onzzer")
        self.setWindowIcon(QIcon('Icones/logo.png'))
        #self.setStyleSheet("background-color: Blue;")
        self.setGeometry(600,300,500,500)
        fonctions.menu(self)
        fonctions.central(self)  
        self.show() 

    
        

def main():
    application = QApplication(sys.argv)
    fenetre = Fenetre_principale()
    fenetre.show()
    sys.exit(application.exec())
        
if __name__ == '__main__':
    main()



















































