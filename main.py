#!/usr/bin/python
# -*- coding: utf-8 -*-

from map import *
from data import *
from PyQt6.QtWidgets import QMainWindow, QTabWidget
from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QPalette, QColor, QFont


class initGUI(QMainWindow):
    def __init__(self, parent=None):
        super().__init__()

        self.title = 'HELP NEEDED'
        self.left = 0
        self.top = 0
        self.width = 1800
        self.height = 900
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.tabs = QTabWidget()
        self.tabs.setFont(QFont('SansSerif', 12))
        self.tabs.resize(300, 200)
        # Add Tabs from data.py and map.py
        self.dataTab = data_GUI()
        self.map = Map_Widget()

        self.map.updateButton.clicked.connect(self.updateLocations)

        self.tabs.addTab(self.dataTab, "Data")
        self.tabs.addTab(self.map, "Map")
        self.setCentralWidget(self.tabs)

    def updateLocations(self):
        self.map.drawLocations(self.dataTab.VolDf, self.dataTab.CliDf)

if __name__ == "__main__":

    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    dark_palette = QPalette()

    dark_palette.setColor(QPalette.ColorRole.Window, QColor(53, 53, 53))
    dark_palette.setColor(QPalette.ColorRole.WindowText, Qt.GlobalColor.white)
    dark_palette.setColor(QPalette.ColorRole.Base, QColor(25, 25, 25))
    dark_palette.setColor(QPalette.ColorRole.AlternateBase, QColor(53, 53, 53))
    dark_palette.setColor(QPalette.ColorRole.ToolTipBase, Qt.GlobalColor.white)
    dark_palette.setColor(QPalette.ColorRole.ToolTipText, Qt.GlobalColor.white)
    dark_palette.setColor(QPalette.ColorRole.Text, Qt.GlobalColor.white)
    dark_palette.setColor(QPalette.ColorRole.Button, QColor(53, 53, 53))
    dark_palette.setColor(QPalette.ColorRole.ButtonText, Qt.GlobalColor.white)
    dark_palette.setColor(QPalette.ColorRole.BrightText, Qt.GlobalColor.red)
    dark_palette.setColor(QPalette.ColorRole.Link, QColor(42, 130, 218))
    dark_palette.setColor(QPalette.ColorRole.Highlight, QColor(42, 130, 218))
    dark_palette.setColor(QPalette.ColorRole.HighlightedText, Qt.GlobalColor.black)
    app.setPalette(dark_palette)
    app.setStyleSheet("QToolTip { color: #ffffff; background-color: #2a82da; border: 1px solid white; }")
    myapp = initGUI()
    myapp.show()
    sys.exit(app.exec())