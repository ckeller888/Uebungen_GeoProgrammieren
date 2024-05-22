# Uebung 6: GUI-Programmierung 3

# Aufgabe 1

from PyQt5.QtWidgets import *
from PyQt5.uic import *
from PyQt5.QtCore import *
from sys import *
from PyQt5.QtGui import *
import urllib.parse 


class Fenster(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("Semester2/Uebungen/showmap.ui",self)
        self.show()


        self.Karte.clicked.connect(self.karte)

    def karte(self):
        s = f"{self.Laenge.text()},{self.Breite.text()}"    
        link = f"https://www.google.ch/maps/place/{s}"
        l = QDesktopServices.openUrl(QUrl(link))
        urllib.parse.quote(l) # enthält 'Hell%C3%B6%20W%C3%B6rld%40'

app = QApplication ([])
window = Fenster()
app.exec()