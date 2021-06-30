from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy, QLabel, QVBoxLayout, QDesktopWidget

from calendariotamponi.view.VistaCalendarioTamponi import VistaCalendarioTamponi
from calendariovaccini.view.VistaCalendarioVaccini import VistaCalendarioVaccini
from magazzino.view.VistaMagazzino import VistaMagazzino
from statistiche.view.VistaStatistiche import VistaStatistiche


class VistaHome(QWidget):

    def __init__(self, parent=None):
        super(VistaHome, self).__init__(parent)

        grid_layout = QGridLayout()
        v_layout =QVBoxLayout()

        v_layout.addWidget(self.get_generic_button("Calendario Vaccini", "rgb(60,123,174)", self.go_calendario_vaccini))
        v_layout.addWidget(self.get_generic_button("Calendario Tamponi", "rgb(73,160,216)", self.go_calendario_tamponi))
        v_layout.addWidget(self.get_generic_button("Magazzino", "rgb(117,185,204)", self.go_magazzino))
        v_layout.addWidget(self.get_generic_button("Statistiche", "rgb(152,231,221)", self.go_statistiche))

        label = QLabel()
        pixmap = QPixmap('appuntamentovaccino/data/CovidFree_Clinica.png')
        pixmap.size()
        label.setPixmap(pixmap)
        label.setAlignment(Qt.AlignCenter)

        grid_layout.addWidget(label, 0, 0)
        grid_layout.addLayout(v_layout, 0, 1)

        self.setLayout(grid_layout)
        self.setMaximumSize(1000, 600)
        self.resize(1000, 600)

        self.center()

        self.setWindowTitle("Clinica COVID FREE")
        self.setWindowIcon(QIcon('appuntamentovaccino/data/CovidFree_Clinica.png'))

    def get_generic_button(self, titolo, colore, on_click):
        button = QPushButton(titolo)
        button.setStyleSheet("background-color: {}".format(colore))
        button.setFont(QFont('Georgia', 10))
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.clicked.connect(on_click)
        return button

    def go_calendario_vaccini(self):
        self.vista_calendario_vaccini = VistaCalendarioVaccini()
        self.vista_calendario_vaccini.show()

    def go_calendario_tamponi(self):
        self.vista_calendario_tamponi = VistaCalendarioTamponi()
        self.vista_calendario_tamponi.show()

    def go_magazzino(self):
        self.vista_magazzino = VistaMagazzino()
        self.vista_magazzino.show()

    def go_statistiche(self):
        self.vista_statistiche = VistaStatistiche()
        self.vista_statistiche.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())