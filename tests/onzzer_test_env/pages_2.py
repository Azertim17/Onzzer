import requests
import json
import webbrowser

    def recherche_album(self, recherche):
    
        image1 = QPixmap('Icones/logo_long_blanc.png' ) 
        image = image1.scaled(255, 68)
        searchButton = QPushButton("Nouvelle recherche")
        searchButton.setStyleSheet("background-color: #E79E41; border-style: outset; border-width: 1px; width: 150px; height: 20px;")
        searchButton.clicked.connect(self.accueil)
        
        self.wid_table = QWidget()
        self.wid_table.setStyleSheet("background-color: #202124")

        wid_bouttons = QWidget()
        vbox = QVBoxLayout()
        bouttonshbox = QHBoxLayout()
        box_image = QLabel()
        self.table = QTableWidget()
        self.table.setRowCount(25)
        self.table.setColumnCount(3)
        self.table.setContentsMargins(100, 200, 100, 0)
        self.table.setStyleSheet("background-color: #D0D1D2")
        self.setCentralWidget(self.wid_table)
        
        box_image.setPixmap(image)
        vbox.addWidget(box_image, alignment= Qt.AlignRight)
  
        self.wid_table.setLayout(vbox)
        vbox.addWidget(self.table)

        wid_bouttons.setLayout(bouttonshbox)
        
        bouttonshbox.addWidget(searchButton, alignment=Qt.AlignLeft)
        
        vbox.addWidget(wid_bouttons, alignment= Qt.AlignLeft)
        
        headerH = ["Nom Artiste","Titre Album","Voir les Pistes"]
        self.table.setHorizontalHeaderLabels(headerH)
        
        header =self.table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)  

        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        
        
        self.liste_albums = request_albums.get_nom_album(self, recherche)
        self.liste_artistes = request_albums.get_liste_artiste(self, recherche)
        

        row = 0
        for i in self.liste_artistes:
            row += 1
            self.table.setItem(row-1,0, QTableWidgetItem(i))

        row = 0  
        for i in self.liste_albums:             
            row += 1
            self.table.setItem(row-1,1, QTableWidgetItem(i))
                      
        row = 0
        for i in range(0,25):             
            row += 1
            
            selectButton = QPushButton("voir")
            selectButton.setIcon(QIcon('Icones/go-last.png'))
            self.table.setCellWidget(row-1,2,selectButton)
            selectButton.clicked.connect(lambda _, r=row, c=3: self.id_album(r, c, recherche)) 