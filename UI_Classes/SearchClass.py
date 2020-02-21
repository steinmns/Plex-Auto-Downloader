from PyQt5 import QtWidgets, QtCore, uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog


class Search_Win(QMainWindow):
    def __init__(self):
        super(Search_Win, self).__init__()
        self.ui = uic.loadUi('UI_Files/SearchWindow.ui', self)   #Loads Main Menu Window


        self.searchButton = self.findChild(QtWidgets.QPushButton, 'searchButton')
        #self.searchButton.clicked.connect(self.runSearch)
        self.cancelButton = self.findChild(QtWidgets.QPushButton, 'cancelButton')
        self.cancelButton.clicked.connect(self.close)