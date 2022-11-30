
import sys
from PyQt5.QtWidgets import QApplication,QToolBar,QAction, QWidget, QTableWidget , QTableWidgetItem
 
def menu(self):
    eraseButton = QAction( 'Effacer', self)
    eraseButton.setShortcut('Ctrl+N')
    openButton = QAction( "Ouvrir l'emplacement d'enregistrement", self)
    openButton.setShortcut('Ctrl+O')
    exitButton = QAction( 'Quitter', self)
    exitButton.setShortcut('Ctrl+Q')
    manButton = QAction('A Propos', self)
    manButton.setShortcut('F1')

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



def tableau(self):
    app = QApplication(sys.argv)
    root = QWidget()
    root.setWindowTitle("QTableView Example")
    root.setGeometry(100 , 100 , 600 , 600)
 
    # create a QTableWidget 
    table = QTableWidget(root)
    table.setRowCount(10)
    table.setColumnCount(1)
    table.setGeometry(150 , 150 , 300 ,500)
                
    # Header horizontale
    headerH = ["Musique de l'album"]
    table.setHorizontalHeaderLabels(headerH)
    
    table.setColumnWidth(0,350)

    # adding a first row
    table.setItem(0,0, QTableWidgetItem(' Albert Einstein'))

    root.show()
    sys.exit(app.exec_())