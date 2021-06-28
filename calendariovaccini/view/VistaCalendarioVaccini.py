from datetime import datetime
import calendar
from PyQt5.QtGui import QFont, QStandardItemModel, QStandardItem, QIcon
from PyQt5.QtWidgets import QWidget, QCalendarWidget, QSizePolicy, QVBoxLayout, QPushButton, QHBoxLayout, QLabel
from PyQt5.QtCore import QDate

from calendariovaccini.controller.ControlloreCalendarioVaccini import ControlloreCalendarioVaccini
from calendariovaccini.view.VistaInserisciAppuntamentoVaccino import VistaInserisciAppuntamentoVaccino
from calendariovaccini.view.VistaListaAppuntamentiVaccini import VistaListaAppuntamentiVaccini


class VistaCalendarioVaccini(QWidget):

    def __init__(self, parent=None):
        super(VistaCalendarioVaccini, self).__init__(parent)

        self.controller = ControlloreCalendarioVaccini()
        self.calendario_vaccini = self.init_calendario()

        h_layout = QHBoxLayout()
        calendar_layout = QVBoxLayout()
        calendar_layout.addWidget(self.calendario_vaccini)

        self.calendario_vaccini.selectionChanged.connect(self.calendar_date)
        self.label = QLabel('')
        calendar_layout.addWidget(self.label)

        buttons_layout = QVBoxLayout()
        buttons_layout.addWidget(self.get_generic_button("Visualizza", self.show_selected_data))
        buttons_layout.addWidget(self.get_generic_button("Aggiungi Appuntamento", self.show_add_appuntamento))

        h_layout.addLayout(calendar_layout)
        h_layout.addLayout(buttons_layout)

        self.setLayout(h_layout)
        self.setWindowTitle("Calendario Appuntamenti Vaccini")
        self.resize(500, 300)
        self.setWindowIcon(QIcon('appuntamentovaccino/data/CovidFree_Clinica.png'))

    def init_calendario(self):
        calendario = QCalendarWidget(self)
        currentMonth = datetime.now().month
        currentYear = datetime.now().year

        calendario.setMinimumDate(QDate(currentYear, currentMonth, 1))
        calendario.setMaximumDate(
            QDate(currentYear + 1, currentMonth, calendar.monthrange(currentYear, currentMonth)[1]))
        calendario.setSelectedDate(QDate(currentYear, currentMonth, 1))

        calendario.setFont(QFont('Georgia', 10))
        calendario.setStyleSheet('background-color: lightblue')
        calendario.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        calendario.setGeometry(200, 200, 300, 200)
        calendario.setGridVisible(True)
        return calendario

    def get_generic_button(self, titolo, on_click):
        button = QPushButton(titolo)
        button.setFont(QFont('Georgia', 10))
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.clicked.connect(on_click)
        return button

    def show_selected_data(self):
        self.vista_visualizza_appuntamenti = VistaListaAppuntamentiVaccini(self.calendar_date(), self.update_ui)
        self.vista_visualizza_appuntamenti.show()

    def show_add_appuntamento(self):
        self.vista_inserisci_appuntamento = VistaInserisciAppuntamentoVaccino(self.update_ui)
        self.vista_inserisci_appuntamento.show()

    def update_ui(self):
        pass

    def calendar_date(self):
        dateselected = self.calendario_vaccini.selectedDate()
        data_selezionata = str(dateselected.toPyDate())
        self.label.setText("Data selezionata : " + data_selezionata)
        return data_selezionata