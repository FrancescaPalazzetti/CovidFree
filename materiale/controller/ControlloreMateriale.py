class ControlloreMateriale():
    def __init__(self, materiale):
        self.model = materiale

    def is_vaccino(self):
        pass

    def is_tampone(self):
        pass

    def get_tipologia_materiale(self):
        return self.model.tipologia

    def get_id_materiale(self):
        return self.model.id

    def get_quantita_materiale(self):
        return self.model.quantita

    def get_scadenza_materiale(self):
        return self.model.scadenza

    def get_is_doppia_dose_vaccino(self):
        return self.model.is_doppia_dose

    def get_distanza_seconda_dose_vaccino(self):
        return self.model.distanza_seconda_dose

    def get_limitazioni_vaccino(self):
        return self.model.limitazioni

    def get_prezzo_tampone(self):
        return self.model.prezzo




