from tuote import Tuote
from ostos import Ostos


class Ostoskori:
    def __init__(self):
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote
        self.ostoskori = {}

    def tavaroita_korissa(self):
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2
        summa = 0
        for ostos in self.ostoskori.values():
            summa += ostos.lukumaara()

        return summa

    def hinta(self):
        # kertoo korissa olevien ostosten yhteenlasketun hinnan
        summa = 0
        for ostos in self.ostoskori.values():
            summa += ostos.hinta()

        return summa

    def lisaa_tuote(self, lisattava: Tuote):
        # lisää tuotteen
        if lisattava.nimi() in self.ostoskori:
            ostos = self.ostoskori[lisattava.nimi()]
            ostos.muuta_lukumaaraa(1)
            return

        self.ostoskori[lisattava.nimi()] = (Ostos(lisattava))

    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        if poistettava.nimi() not in self.ostoskori:
            return

        ostos = self.ostoskori[poistettava.nimi()]
        ostos.muuta_lukumaaraa(-1)

    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
        return list(self.ostoskori.values())
