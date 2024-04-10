# Uebung 5: GUI-Programmierung 2

# Aufgabe 1

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import urllib.parse 


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setMinimumWidth(360)
        self.setMinimumHeight(360)

        self.setWindowTitle("GUI-Progrmmierung")
        self.show()


        # Layout erstellen:
        layout = QFormLayout()

        # Widget-Instanzen erstellen:
        self.vornameLineEdit = QLineEdit()
        self.nameLineEdit = QLineEdit()
        self.geburtstag = QDateEdit()
        self.adresseLineEdit = QLineEdit()
        self.plzLineEdit = QLineEdit()
        self.ortLineEdit = QLineEdit()
        self.countries = QComboBox()
        self.countries.addItems(["Schweiz", "Deutschland", "Österreich"])
        self.button = QPushButton("Save")
        self.button2 = QPushButton("Auf Karte anzeigen")
        self.button3 = QPushButton("Laden")

        # Layout füllen:
        layout.addRow("Vorname:", self.vornameLineEdit)
        layout.addRow("Name:", self.nameLineEdit)
        layout.addRow("Geburtstag:", self.geburtstag)
        layout.addRow("Adresse:", self.adresseLineEdit)
        layout.addRow("Postleitzahl:", self.plzLineEdit)
        layout.addRow("Ort:", self.ortLineEdit)
        layout.addRow("Land", self.countries)
        layout.addRow(self.button)
        layout.addRow(self.button2)
        layout.addRow(self.button3)

        # Zentrales Widget erstellen und layout hinzufügen
        center = QWidget()
        center.setLayout(layout)

        # Zentrales Widget in diesem Fenster setzen
        self.setCentralWidget(center)

        # Fenster anzeigen
        self.show()


        # File-Menu
        menubar = self.menuBar()
        filemenu = menubar.addMenu("File")
        filemenu2 = menubar.addMenu("View")
        filemenu3 = menubar.addMenu("Laden")
        
        self.save = QAction("Save", self)
        self.quit = QAction("Quit", self)
        self.view = QAction("Karte", self)
        self.laden = QAction("Laden", self)
        
        filemenu.addAction(self.save)
        filemenu.addAction(self.quit)
        filemenu2.addAction(self.view)
        filemenu3.addAction(self.laden)

        self.save.triggered.connect(self.menu_save)
        self.quit.triggered.connect(self.menu_quit)
        self.view.triggered.connect(self.karte)
        self.laden.triggered.connect(self.laden2)
        self.button.clicked.connect(self.menu_save)
        self.button2.clicked.connect(self.karte)
        self.button3.clicked.connect(self.laden2)


    def menu_quit(self):
        self.close()


    def menu_save(self):
        export = f"{self.vornameLineEdit.text()},{self.nameLineEdit.text()},{self.geburtstag.text()},{self.adresseLineEdit.text()},{self.plzLineEdit.text()},{self.ortLineEdit.text()},{self.countries.currentText()}"

        f = open("output.txt", "w")
        f.write(export)


    def karte(self):
        s = f"{self.adresseLineEdit.text()}+{self.plzLineEdit.text()}+{self.ortLineEdit.text()}+{self.countries.currentText()}"
        link = f"https://www.google.ch/maps/place/{s}"
        l = QDesktopServices.openUrl(QUrl(link))
        urllib.parse.quote(l) # enthält 'Hell%C3%B6%20W%C3%B6rld%40'


    def laden2(self):
        filename, type = QFileDialog.getOpenFileName(self,"Datei öffnen", 
                                                     "", 
                                                     "Textfile (*.txt)")
        if filename != "":        
            datei = open(filename, "r")
            daten = datei.read().split(",")

            self.vornameLineEdit.setText(daten[0])
            self.nameLineEdit.setText(daten[1])
            dformat = QLocale().dateFormat(format=QLocale.FormatType.ShortFormat) 
            self.geburtstag.setDate(QDate.fromString(daten[2],dformat))
            self.adresseLineEdit.setText(daten[3])
            self.plzLineEdit.setText(daten[4])
            self.ortLineEdit.setText(daten[5])
            self.countries.setCurrentText(daten[6]) 
    
            datei.close()
        else:
            QMessageBox.warning(self, "Abbruch", "Der Filedialog wurde abgebrochen, es wird nichts geöffnet!")

    

def main():
    app = QApplication(sys.argv)
    mainwindow = MyWindow()
    mainwindow.raise_()
    app.exec_()

if __name__ == '__main__':
    main()