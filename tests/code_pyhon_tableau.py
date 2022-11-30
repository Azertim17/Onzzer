
import sys
from PyQt5.QtWidgets import QApplication, QWidget , QTableWidget , QTableWidgetItem
 
app = QApplication(sys.argv)
root = QWidget()
root.setWindowTitle("QTableView Example")
root.setGeometry(100 , 100 , 600 , 600)
 
# create a QTableWidget 
table = QTableWidget(root)
table.setRowCount(4)
table.setColumnCount(1)
table.setGeometry(50 , 50 , 500 ,500)
            
# Header horizontale
headerH = ["Musique de l'album"]
table.setHorizontalHeaderLabels(headerH)

table.setColumnWidth(0,350)

# adding a first row
table.setItem(0,0, QTableWidgetItem(' Albert Einstein'))

root.show()
sys.exit(app.exec_())