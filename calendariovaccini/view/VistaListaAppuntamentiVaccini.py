import os
import pickle
from datetime import datetime, date, timedelta

from PyQt5 import QtGui
from PyQt5.QtGui import QStandardItem, QStandardItemModel, QIcon
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QListView, QVBoxLayout, QPushButton, QGridLayout, QLabel, QMessageBox

from appuntamentovaccino.view.VistaAppuntamentoVaccino import VistaAppuntamentoVaccino
from calendariovaccini.controller.ControlloreCalendarioVaccini import ControlloreCalendarioVaccini
from calendariovaccini.view.VistaModificaAppuntamentoVaccino import VistaModificaAppuntamentoVaccino


class VistaListaAppuntamentiVaccini(QWidget):

    def __init__(self, data, callback):
        super(VistaListaAppuntamentiVaccini, self).__init__()
        self.controller = ControlloreCalendarioVaccini()
        self.callback = callback


        appuntamento = datetime.strptime(data, '%Y-%m-%d')
        d = str(appuntamento.strftime('%d-%m-%Y'))
        self.data = d

        self.elenco_astrazeneca = []
        self.elenco_moderna = []
        self.elenco_pfizer = []

        h_layout = QHBoxLayout()
        self.list_view = QListView()
        h_layout.addWidget(self.list_view)

        self.grid_layout = QGridLayout()

        self.list_view_astrazeneca = QListView()
        self.list_view_moderna = QListView()
        self.list_view_pfizer = QListView()

        self.update_ui()

        self.get_list("Appuntamenti Astrazeneca", 0)
        self.get_list("Appuntamenti Moderna", 1)
        self.get_list("Appuntamenti Pfizer", 2)

        self.grid_layout.addWidget(self.list_view_astrazeneca, 1, 0)
        self.grid_layout.addWidget(self.list_view_moderna, 1, 1)
        self.grid_layout.addWidget(self.list_view_pfizer, 1, 2)

        visualizza_astrazeneca = QPushButton("Visualizza")
        modifica_astrazeneca = QPushButton("Modifica")
        elimina_astrazeneca = QPushButton("Elimina")
        self.grid_layout.addWidget(visualizza_astrazeneca, 2, 0)
        self.grid_layout.addWidget(elimina_astrazeneca, 3, 0)
        self.grid_layout.addWidget(modifica_astrazeneca, 4, 0)
        visualizza_astrazeneca.clicked.connect(self.show_selected_info_astrazeneca)
        elimina_astrazeneca.clicked.connect(self.elimina_appuntamento_astrazeneca)
        modifica_astrazeneca.clicked.connect(self.modifica_appuntamento_astrazeneca)

        visualizza_moderna = QPushButton("Visualizza")
        elimina_moderna = QPushButton("Elimina")
        self.grid_layout.addWidget(visualizza_moderna, 2, 1)
        self.grid_layout.addWidget(elimina_moderna, 3, 1)
        visualizza_moderna.clicked.connect(self.show_selected_info_moderna)
        elimina_moderna.clicked.connect(self.elimina_appuntamento_moderna)

        visualizza_pfizer = QPushButton("Visualizza")
        elimina_pfizer = QPushButton("Elimina")
        self.grid_layout.addWidget(visualizza_pfizer, 2, 2)
        self.grid_layout.addWidget(elimina_pfizer, 3, 2)
        visualizza_pfizer.clicked.connect(self.show_selected_info_pfizer)
        elimina_pfizer.clicked.connect(self.elimina_appuntamento_pfizer)

        self.setLayout(self.grid_layout)
        self.resize(600, 300)
        self.setWindowTitle('Lista Appuntamenti Vaccini Giorno: {}'.format(self.data))
        self.setWindowIcon(QIcon('appuntamentovaccino/data/CovidFree_Clinica.png'))

    def get_list(self, tipologia, colonna):

        v_layout_tipologia = QVBoxLayout()
        label_tipologia = QLabel(tipologia)
        font_tipologia = label_tipologia.font()
        font_tipologia.setFamily('Georgia')
        font_tipologia.setPointSize(15)
        font_tipologia.setItalic(True)
        label_tipologia.setFont(font_tipologia)
        v_layout_tipologia.addWidget(label_tipologia)

        self.grid_layout.addLayout(v_layout_tipologia, 0, colonna)

    def show_selected_info_astrazeneca(self):
        if self.list_view_astrazeneca.selectedIndexes():
            selected = self.list_view_astrazeneca.selectedIndexes()[0].row()
            appuntamento_selezionato = self.elenco_astrazeneca[selected]
            self.vista_vaccino = VistaAppuntamentoVaccino(appuntamento_selezionato)
            self.vista_vaccino.show()
            self.update_ui()

    def show_selected_info_moderna(self):
        if self.list_view_moderna.selectedIndexes():
            selected = self.list_view_moderna.selectedIndexes()[0].row()
            appuntamento_selezionato = self.elenco_moderna[selected]
            self.vista_vaccino = VistaAppuntamentoVaccino(appuntamento_selezionato)
            self.vista_vaccino.show()
            self.update_ui()

    def show_selected_info_pfizer(self):
        if self.list_view_pfizer.selectedIndexes():
            selected = self.list_view_pfizer.selectedIndexes()[0].row()
            appuntamento_selezionato = self.elenco_pfizer[selected]
            self.vista_vaccino = VistaAppuntamentoVaccino(appuntamento_selezionato)
            self.vista_vaccino.show()
            self.update_ui()

    def update_ui(self):
        self.list_view_astrazeneca_model = QStandardItemModel(self.list_view_astrazeneca)
        self.list_view_moderna_model = QStandardItemModel(self.list_view_moderna)
        self.list_view_pfizer_model = QStandardItemModel(self.list_view_pfizer)

        for appuntamento in self.controller.get_elenco_appuntamenti():
            item = QStandardItem()
            if appuntamento.data_appuntamento == self.data:
                item.setText(appuntamento.cartella_paziente.nome + " " + appuntamento.cartella_paziente.cognome)
                item.setEditable(False)
                font = item.font()
                font.setFamily('Georgia')
                font.setPointSize(12)
                item.setFont(font)

                if appuntamento.is_a_domicilio:
                    item.setBackground(QtGui.QColor(255,255,153))

                if appuntamento.id == 'Seconda Dose':
                    item.setBackground(QtGui.QColor(200, 255, 153))

                if appuntamento.vaccino == "Astrazeneca":
                    self.list_view_astrazeneca_model.appendRow(item)
                    self.elenco_astrazeneca.append(appuntamento)
                elif appuntamento.vaccino == "Moderna":
                    self.list_view_moderna_model.appendRow(item)
                    self.elenco_moderna.append(appuntamento)
                elif appuntamento.vaccino == "Pfizer":
                    self.list_view_pfizer_model.appendRow(item)
                    self.elenco_pfizer.append(appuntamento)

        self.list_view_astrazeneca.setModel(self.list_view_astrazeneca_model)
        self.list_view_moderna.setModel(self.list_view_moderna_model)
        self.list_view_pfizer.setModel(self.list_view_pfizer_model)

    def elimina_appuntamento_astrazeneca(self):
        if self.list_view_astrazeneca.selectedIndexes():
            selected = self.list_view_astrazeneca.selectedIndexes()[0].row()
            appuntamento_selezionato = self.elenco_astrazeneca[selected]

            data_appuntamento_selezionato = datetime.strptime(appuntamento_selezionato.data_appuntamento, '%d-%m-%Y')
            selezionato = str(data_appuntamento_selezionato.strftime('%Y-%m-%d'))
            if selezionato < str(date.today()):
                QMessageBox.critical(self, 'Errore', 'Non è possibile eliminare appuntamenti passati',
                                     QMessageBox.Ok, QMessageBox.Ok)
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Sei sicuro di voler eliminare l'appuntamento?")
                msg.setWindowIcon(QIcon('appuntamentovaccino/data/CovidFree_Clinica.png'))
                msg.setInformativeText("La decisione è irreversibile!")
                msg.setWindowTitle("Conferma eliminazione")
                msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

                if msg.exec() == QMessageBox.Ok:
                    self.controller.lettura_magazzino()
                    self.controller.aggiorna_magazzino(appuntamento_selezionato.vaccino)
                    self.controller.elimina_appuntamento(appuntamento_selezionato)
                    self.elenco_astrazeneca.remove(appuntamento_selezionato)
                self.update_ui()

    def elimina_appuntamento_moderna(self):
        if self.list_view_moderna.selectedIndexes():
            selected = self.list_view_moderna.selectedIndexes()[0].row()
            appuntamento_selezionato = self.elenco_moderna[selected]

            data_appuntamento_selezionato = datetime.strptime(appuntamento_selezionato.data_appuntamento, '%d-%m-%Y')
            selezionato = str(data_appuntamento_selezionato.strftime('%Y-%m-%d'))
            if selezionato < str(date.today()):
                QMessageBox.critical(self, 'Errore', 'Non è possibile eliminare appuntamenti passati',
                                     QMessageBox.Ok, QMessageBox.Ok)
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Sei sicuro di voler eliminare l'appuntamento?")
                msg.setInformativeText("La decisione è irreversibile!")
                msg.setWindowTitle("Conferma eliminazione")
                msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

                if msg.exec() == QMessageBox.Ok:
                    self.controller.lettura_magazzino()
                    self.controller.aggiorna_magazzino(appuntamento_selezionato.vaccino)
                    self.controller.elimina_appuntamento(appuntamento_selezionato)
                    self.elenco_moderna.remove(appuntamento_selezionato)
                self.update_ui()


    def elimina_appuntamento_pfizer(self):
        if self.list_view_pfizer.selectedIndexes():
            selected = self.list_view_pfizer.selectedIndexes()[0].row()
            appuntamento_selezionato = self.elenco_pfizer[selected]

            data_appuntamento_selezionato = datetime.strptime(appuntamento_selezionato.data_appuntamento, '%d-%m-%Y')
            selezionato = str(data_appuntamento_selezionato.strftime('%Y-%m-%d'))
            if selezionato < str(date.today()):
                QMessageBox.critical(self, 'Errore', 'Non è possibile eliminare appuntamenti passati',
                                     QMessageBox.Ok, QMessageBox.Ok)
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Sei sicuro di voler eliminare l'appuntamento?")
                msg.setInformativeText("La decisione è irreversibile!")
                msg.setWindowTitle("Conferma eliminazione")
                msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

                if msg.exec() == QMessageBox.Ok:
                    self.controller.lettura_magazzino()
                    self.controller.aggiorna_magazzino(appuntamento_selezionato.vaccino)
                    self.controller.elimina_appuntamento(appuntamento_selezionato)
                    self.elenco_pfizer.remove(appuntamento_selezionato)
                self.update_ui()

    def modifica_appuntamento_astrazeneca(self):
        if self.list_view_astrazeneca.selectedIndexes():
            selected = self.list_view_astrazeneca.selectedIndexes()[0].row()
            appuntamento_selezionato = self.elenco_astrazeneca[selected]
            vista_modifica = VistaModificaAppuntamentoVaccino(appuntamento_selezionato)
            vista_modifica.show()
            self.close()

