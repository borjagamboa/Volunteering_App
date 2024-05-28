
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QVBoxLayout, QHBoxLayout
from PyQt6.QtGui import QFont
from PyQt6.QtCore import QAbstractTableModel, Qt

from google_functions import *

class data_GUI(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(QtWidgets.QWidget, self).__init__(parent)
        self.df = pd.DataFrame()
        # Volunteer data
        self.VolDf = pd.DataFrame()
        # Client data
        self.CliDf = pd.DataFrame()
        # My file name with the data of the Google Forms
        self.forms_answers = "Event Registration (respuestas)"

        # Layouts
        self.mainLayout = QVBoxLayout()
        self.settingsLayout = QHBoxLayout()

        #Widgets
        self.fileNameLabel = QtWidgets.QLabel('File')
        self.fileNameLabel.setFont(QFont('SansSerif', 12))
        self.fileNameGap = QtWidgets.QLineEdit()
        self.fileNameGap.setFont(QFont('SansSerif', 12))
        self.loadButton = QtWidgets.QPushButton('Load data')
        self.loadButton.setFont(QFont('SansSerif', 12))
        self.volLabel = QtWidgets.QLabel('Volunteer information')
        self.volLabel.setFont(QFont('SansSerif', 12))
        self.cliLabel = QtWidgets.QLabel('Requester information')
        self.cliLabel.setFont(QFont('SansSerif', 12))

        self.volunteerTable = QtWidgets.QTableView()
        self.clientsTable = QtWidgets.QTableView()

        ### to update
        self.fileNameGap.setText(self.forms_answers)
        self.loadButton.clicked.connect(self.setTables)

        self.settingsLayout.addWidget(self.fileNameLabel)
        self.settingsLayout.addWidget(self.fileNameGap)
        self.settingsLayout.addWidget(self.loadButton)

        self.mainLayout.addLayout(self.settingsLayout)
        self.mainLayout.addWidget(self.volLabel)
        self.mainLayout.addWidget(self.volunteerTable)
        self.mainLayout.addWidget(self.cliLabel)
        self.mainLayout.addWidget(self.clientsTable)

        self.setLayout(self.mainLayout)

    def setTables(self):
        try:
            self.volunteerTable.reset()
            self.clientsTable.reset()

            sheet = getsheet(self.forms_answers)
            self.df = gsheet2df(sheet)
            self.VolDf = (self.df[self.df['Tipo'] == "Voluntario"]).drop(['Marca temporal',
                                                         'Estado', 'Tipo', '¿Tienes WhatsApp?',
                                                         'Voluntario(s)', 'Necesidad'], axis=1)
            self.CliDf = (self.df[self.df['Tipo'] == "Ayuda"]).drop(['Marca temporal','¿Tienes WhatsApp?', 'DNI',
                                                                     'Tipo', 'Horario'], axis=1)
            self.setVolunteerTable(self.VolDf)
            self.setClientsTable(self.CliDf)

            self.volunteerTable.verticalHeader().hide()  # hide vertical/row headers

            # -- +++
            self.volunteerTable.setAlternatingRowColors(True)
            self.volunteerTable.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
            self.volunteerTable.horizontalHeader().setSectionResizeMode(0,
                                                                        QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
            self.volunteerTable.horizontalHeader().setSectionResizeMode(1,
                                                                        QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
            self.volunteerTable.horizontalHeader().setSectionResizeMode(3,
                                                                        QtWidgets.QHeaderView.ResizeMode.ResizeToContents)

            # size policy
            self.clientsTable.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
            self.clientsTable.verticalHeader().hide()  # hide vertical/row headers

            # -- +++
            self.clientsTable.setAlternatingRowColors(True)
            self.clientsTable.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
            self.clientsTable.horizontalHeader().setSectionResizeMode(0,
                                                                      QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
            self.clientsTable.horizontalHeader().setSectionResizeMode(1,
                                                                      QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
            self.clientsTable.horizontalHeader().setSectionResizeMode(3,
                                                                      QtWidgets.QHeaderView.ResizeMode.ResizeToContents)

            # size policy
            self.clientsTable.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding,
                                            QtWidgets.QSizePolicy.Policy.Expanding)
        except:
            print("Failed to set tables")

    def setVolunteerTable(self, volunteerData):
        VModel = pandasModel(volunteerData)
        self.volunteerTable.setModel(VModel)

    def setClientsTable(self, clientsData):
        CModel = pandasModel(clientsData)
        self.clientsTable.setModel(CModel)


class pandasModel(QAbstractTableModel):

    def __init__(self, data):
        QAbstractTableModel.__init__(self)
        self._data = data

    def rowCount(self, parent=None):
        return self._data.shape[0]

    def columnCount(self, parent=None):
        return self._data.shape[1]

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        if index.isValid():
            if role == Qt.ItemDataRole.DisplayRole:
                return str(self._data.iloc[index.row(), index.column()])
        return None

    def headerData(self, col, orientation, role):
        if orientation == Qt.Orientation.Horizontal and role == Qt.ItemDataRole.DisplayRole:
            return self._data.columns[col]
        return None