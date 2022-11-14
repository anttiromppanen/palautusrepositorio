class Kirjanpito:
    def __init__(self):
        self.tapahtumat = []

    def lisaa_tapahtuma(self, tapahtuma):
        self.tapahtumat.append(tapahtuma)

    def get_tapahtumat(self):
        return self.tapahtumat

the_kirjanpito_olio = Kirjanpito()