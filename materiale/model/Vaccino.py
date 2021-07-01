from materiale.model.Materiale import Materiale


class Vaccino(Materiale):
    def __init__(self, tipologia, doppiadose, distanza, id, quantita):
        super(Vaccino, self).__init__(tipologia, id, quantita)
        self.categoria = "Vaccino"
        self.is_doppia_dose = doppiadose
        self.distanza_seconda_dose = distanza