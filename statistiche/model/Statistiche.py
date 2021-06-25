import os
import pickle


class Statistiche():
    def __init__(self):
        super(Statistiche, self).__init__()
        self.elenco_appuntamenti_vaccini = []
        self.elenco_appuntamenti_tamponi = []

        if os.path.isfile('calendariovaccini/data/elenco_appuntamenti_fissati.pickle'):
            with open('calendariovaccini/data/elenco_appuntamenti_fissati.pickle', 'rb') as f:
                self.elenco_appuntamenti_vaccini = pickle.load(f)

        if os.path.isfile('calendariotamponi/data/elenco_appuntamenti_salvati.pickle'):
            with open('calendariotamponi/data/elenco_appuntamenti_salvati.pickle', 'rb') as f:
                self.elenco_appuntamenti_tamponi = pickle.load(f)

