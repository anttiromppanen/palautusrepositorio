import unittest
from ostoskori import Ostoskori
from tuote import Tuote


class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        juusto = Tuote("Juusto", 8)
        self.kori.lisaa_tuote(juusto)

        self.assertEqual(self.kori.tavaroita_korissa(), 1)

    def test_yhden_tuotteen_lisaamisen_jalkeen_ostoskorin_hinta_on_sama_kuin_tuotteen_hinta(self):
        juusto = Tuote("Juusto", 8)
        self.kori.lisaa_tuote(juusto)

        self.assertEqual(self.kori.hinta(), 8)

    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_ostoskorissa_on_kaksi_tavaraa(self):
        juusto = Tuote("Juusto", 8)
        sipuli = Tuote("Sipuli", 1)

        self.kori.lisaa_tuote(juusto)
        self.kori.lisaa_tuote(sipuli)

        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_ostoskorin_hinta_on_sama_kuin_tuotteiden_hintojen_summa(self):
        juusto = Tuote("Juusto", 8)
        sipuli = Tuote("Sipuli", 1)

        self.kori.lisaa_tuote(juusto)
        self.kori.lisaa_tuote(sipuli)

        self.assertEqual(self.kori.hinta(), 9)

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_ostoskorissa_on_kaksi_tavaraa(self):
        juusto = Tuote("Juusto", 8)
        juusto2 = Tuote("Juusto", 8)

        self.kori.lisaa_tuote(juusto)
        self.kori.lisaa_tuote(juusto2)

        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_ostoskorissa_on_kaksi_tavaraa(self):
        juusto = Tuote("Juusto", 8)
        juusto2 = Tuote("Juusto", 8)

        self.kori.lisaa_tuote(juusto)
        self.kori.lisaa_tuote(juusto2)

        self.assertEqual(self.kori.hinta(), 2*8)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio(self):
        juusto = Tuote("Juusto", 8)
        self.kori.lisaa_tuote(juusto)

        ostokset = self.kori.ostokset()

        self.assertEqual(len(ostokset), 1)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio_jolla_oikea_tuotteen_nimi_ja_maara(self):
        juusto = Tuote("Juusto", 8)
        self.kori.lisaa_tuote(juusto)

        ostos = self.kori.ostokset()[0]

        self.assertEqual(ostos.tuotteen_nimi(), "Juusto")
        self.assertEqual(ostos.hinta(), 8)
