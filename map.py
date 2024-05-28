# -*- coding: utf-8 -*-

from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtWidgets import QApplication
from PyQt6 import QtCore, QtWidgets
from PyQt6 import QtWebEngineWidgets
from PyQt6.QtWidgets import QVBoxLayout
from PyQt6.QtGui import QFont
from jinja2 import Environment, FileSystemLoader
from geofunctions import*
from browser import*
import numpy as np
import os, sys

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtWidgets.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig)

class Map_Widget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(QtWidgets.QWidget, self).__init__(parent)

        self.webView = QtWebEngineWidgets.QWebEngineView()
        self.webView.setGeometry(QtCore.QRect(170, 10, 421, 291))
        self.webView.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.webView.setObjectName(_fromUtf8("webView"))

        self.updateButton = QtWidgets.QPushButton()
        self.updateButton.setText('Update map')
        self.updateButton.setFont(QFont('SansSerif', 12))
        self.updateButton.setFixedWidth(500)
        self.updateButton.setSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding,
                                        QtWidgets.QSizePolicy.Policy.MinimumExpanding)


        self.initMap()
        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.updateButton, alignment=QtCore.Qt.AlignmentFlag.AlignCenter)
        self.mainLayout.addWidget(self.webView)
        self.mainLayout.setStretch(1,2)


        self.setLayout(self.mainLayout)

    def initMap(self):
        directory = os.getcwd()
        defaultDir = os.path.join(directory, "DefaultSettings")
        initialMapFile = os.path.join(defaultDir, 'initMap.html')
        environment = Environment(loader=FileSystemLoader("DefaultSettings/"))
        with open(initialMapFile, 'r') as f:
            map_html = environment.get_template("initMap.txt")
            map = map_html.render(API_KEY=keys['private_key_id'])
            print(map)
        self.webView.setHtml(map)

    def drawLocations(self, vdata, cdata):
        Vnames = (vdata['Nombre'] + ' ' + vdata['Apellidos']).to_numpy()
        Cnames = (cdata['Nombre'] + ' ' + cdata['Apellidos']).to_numpy()
        Vaddresses = get_addresses(vdata['Dirección (Calle, Nº de portal)'])
        Vcoordinates = np.asarray(addresses_to_coordinates(Vaddresses))
        Caddresses = get_addresses(cdata['Dirección (Calle, Nº de portal)'])
        Ccoordinates = np.asarray(addresses_to_coordinates(Caddresses))
        newMap = location(write_v_markers_html(Vcoordinates, Vnames),
                          write_c_markers_html(Ccoordinates,
                                               Cnames,
                                               cdata['Estado'].to_numpy()),
                          keys['private_key_id'])
        self.webView.setHtml(newMap)

class initGUI(QMainWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.title = 'Help needed'
        self.left = 0
        self.top = 0
        self.width = 1800
        self.height = 900
        self.setWindowTitle(self.title)
        self.map = Map_Widget()
        self.setCentralWidget(self.map)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    myapp = initGUI()
    myapp.show()
    sys.exit(app.exec())