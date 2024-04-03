# Uebung 4: GUI-Programmierung 1

# Aufgabe 1

import sys
from PyQt5.QtWidgets import *


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setMinimumWidth(360)
        self.setMinimumHeight(300)

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

        # Layout füllen:
        layout.addRow("Vorname:", self.vornameLineEdit)
        layout.addRow("Name:", self.nameLineEdit)
        layout.addRow("Geburtstag:", self.geburtstag)
        layout.addRow("Adresse:", self.adresseLineEdit)
        layout.addRow("Postleitzahl:", self.plzLineEdit)
        layout.addRow("Ort:", self.ortLineEdit)
        layout.addRow("Land", self.countries)
        layout.addRow(self.button)

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
        self.save = QAction("Save", self)
        self.quit = QAction("Quit", self)
        
        filemenu.addAction(self.save)
        filemenu.addAction(self.quit)


        self.save.triggered.connect(self.menu_save)
        self.quit.triggered.connect(self.menu_quit)
        self.button.clicked.connect(self.menu_save)


    def menu_quit(self):
        self.close()

    def menu_save(self):
        export = f"{self.vornameLineEdit.text()},{self.nameLineEdit.text()},{self.geburtstag.text()},{self.adresseLineEdit.text()},{self.plzLineEdit.text()},{self.ortLineEdit.text()},{self.countries.currentText()}"

        f = open("output.txt", "w")
        f.write(export)
        f.close()



def main():
    app = QApplication(sys.argv)
    mainwindow = MyWindow()
    mainwindow.raise_()
    app.exec_()

if __name__ == '__main__':
    main()