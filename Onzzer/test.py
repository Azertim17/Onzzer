
import sys
from PyQt5.QtWidgets import QApplication,QToolBar,QAction, QWidget, QTableWidget , QTableWidgetItem
 

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