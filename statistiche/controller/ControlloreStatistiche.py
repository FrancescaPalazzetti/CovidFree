from statistiche.model.Statistiche import Statistiche


class ControlloreStatistiche():

    def __init__(self):
        super(ControlloreStatistiche, self).__init__()
        self.model = Statistiche()

    def get_elenco_appuntamenti_vaccini(self):
        return self.model.elenco_appuntamenti_vaccini

    def get_elenco_appuntamenti_tamponi(self):
        return self.model.elenco_appuntamenti_tamponi

    def salva_effetti_collaterali(self, effetti_collaterali):
        self.model.salva_effetti_collaterali(effetti_collaterali)

