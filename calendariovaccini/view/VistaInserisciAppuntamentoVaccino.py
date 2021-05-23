from datetime import datetime

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QSpacerItem, QSizePolicy, QPushButton, QLabel, QLineEdit, QMessageBox, \
    QGridLayout, QCheckBox, QRadioButton, QComboBox

from appuntamentovaccino.model.AppuntamentoVaccino import AppuntamentoVaccino
from calendariovaccini.view.VistaInserisciAnamnesi import VistaInserisciAnamnesi
from cartellapaziente.model.CartellaPaziente import CartellaPaziente


class VistaInserisciAppuntamentoVaccino(QWidget):

    def __init__(self, controller, callback):
        super(VistaInserisciAppuntamentoVaccino, self).__init__()
        self.controller = controller
        self.callback = callback
        self.info = {}

        self.v_layout = QVBoxLayout()

        self.get_form_entry("Nome")
        self.get_form_entry("Cognome")
        self.get_form_entry("Data di nascita")
        self.get_form_entry("Codice Fiscale")
        self.get_form_entry("Indirizzo")
        self.get_form_entry("Telefono")

        button = QPushButton("Anamnesi")
        button.clicked.connect(self.go_inserisci_anamnesi)

        self.v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))
        self.v_layout.addWidget(button)

        self.v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))
        self.v_layout.addWidget(QLabel("Preferenza (opzionale)"))
        self.preferenza = QComboBox()
        self.preferenza.addItems([" ","Pfizer", "Moderna", "Astrazeneca"])
        self.v_layout.addWidget(self.preferenza)

        self.consenso1 = QCheckBox("Consenso al trattamento dei dati personali")
        self.v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))
        self.v_layout.addWidget(self.consenso1)

        self.consenso2 = QCheckBox("Consenso al trattamento sanitario")
        self.v_layout.addWidget(self.consenso2)

        self.v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_ok = QPushButton("OK")
        btn_ok.clicked.connect(self.add_appuntamento)

        self.v_layout.addWidget(btn_ok)

        self.setLayout(self.v_layout)
        self.setWindowTitle("Nuovo Appuntamento")

    def get_form_entry(self, tipo):
        self.v_layout.addWidget(QLabel(tipo))
        current_text_edit = QLineEdit(self)
        self.v_layout.addWidget(current_text_edit)
        self.info[tipo] = current_text_edit

    def get_checkbox(self):
        pass

    def onClicked(self):
        pass

    def add_appuntamento(self):
        nome = self.info["Nome"].text()
        cognome = self.info["Cognome"].text()
        data_nascita = self.info["Data di nascita"].text()
        cf = self.info["Codice Fiscale"].text()
        indirizzo = self.info["Indirizzo"].text()
        telefono = self.info["Telefono"].text()
        preferenze = self.preferenza.currentText()

        try:
            date = datetime.strptime(self.info["Data di nascita"].text(), '%d/%m/%Y')
        except:
            QMessageBox.critical(self, 'Errore', 'Inserisci la data nel formato richiesto: dd/MM/yyyy', QMessageBox.Ok, QMessageBox.Ok)

        if nome == "" or cognome == "" or data_nascita == "" or cf == "" or indirizzo == "" or telefono == "":
            QMessageBox.critical(self, 'Errore', 'Per favore, completa tutti i campi', QMessageBox.Ok, QMessageBox.Ok)

        elif self.consenso1.isChecked() == False or self.consenso2.isChecked() == False:
            QMessageBox.critical(self, 'Errore',
                                 'Se non viene fornito il consenso non è possibile procedere con la prenotazione',
                                 QMessageBox.Ok, QMessageBox.Ok)
        else:
            cartella_paziente = CartellaPaziente(nome, cognome, data_nascita, cf, indirizzo, telefono, preferenze)
            self.callback()
            self.close()

    def go_inserisci_anamnesi(self):
        self.vista_inserisci_anamnesi = VistaInserisciAnamnesi(self.controller, self.update_ui)
        self.vista_inserisci_anamnesi.show()

    def update_ui(self):
        pass