import unittest
from statistics import Statistics
from player import Player
from sort_by import SortBy

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )

    def test_team_palauttaa_oikean_maaran(self):
        pelaajat = self.statistics.team("EDM")

        self.assertEqual(len(pelaajat), 3)

    def test_team_palauttaa_nolla_olemattomalla_joukkueella(self):
        pelaajat = self.statistics.team("PI")

        self.assertEqual(len(pelaajat), 0)

    def test_search_loytaa_pelaajan(self):
        pelaaja = self.statistics.search("Kurri")

        self.assertEqual(pelaaja.name, "Kurri")

    def test_search_palauttaa_pelaajan_osittaisella_nimella(self):
        pelaaja = self.statistics.search("Yzer")
        
        self.assertEqual(pelaaja.name, "Yzerman")

    def test_search_ei_palauta_kun_nimea_ei_loydy(self):
        pelaaja = self.statistics.search("abcdefg")

        self.assertFalse(pelaaja)

    def test_top_palauttaa_oikean_maaran(self):
        maara = 3
        pelaajat = self.statistics.top(maara)

        self.assertEqual(len(pelaajat), maara + 1)

    def test_top_ei_palauta_negatiivisella_arvolla(self):
        pelaajat = self.statistics.top(-1)

        self.assertEqual(len(pelaajat), 0)

    def test_top_palauttaa_oikein_eniten_maaleja_tehneet(self):
        pelaajat = self.statistics.top(4, SortBy.GOALS)
        alkuperaiset_pelaajat = PlayerReaderStub().get_players()

        alkuperaiset_pelaajat_sorted = sorted(
            alkuperaiset_pelaajat,
            reverse=True,
            key=lambda pelaaja: pelaaja.goals
        )
        
        self.assertEqual(pelaajat[0].name, alkuperaiset_pelaajat_sorted[0].name)
        self.assertEqual(pelaajat[1].name, alkuperaiset_pelaajat_sorted[1].name)
        self.assertEqual(pelaajat[3].name, alkuperaiset_pelaajat_sorted[3].name)

    def test_top_palauttaa_oikein_eniten_syottoja_tehneet(self):
        pelaajat = self.statistics.top(4, SortBy.ASSISTS)
        alkuperaiset_pelaajat = PlayerReaderStub().get_players()

        alkuperaiset_pelaajat_sorted = sorted(
            alkuperaiset_pelaajat,
            reverse=True,
            key=lambda pelaaja: pelaaja.assists
        )
        
        self.assertEqual(pelaajat[0].name, alkuperaiset_pelaajat_sorted[0].name)
        self.assertEqual(pelaajat[1].name, alkuperaiset_pelaajat_sorted[1].name)
        self.assertEqual(pelaajat[3].name, alkuperaiset_pelaajat_sorted[3].name)

    def test_top_palauttaa_oikein_eniten_pisteita_tehneet(self):
        pelaajat = self.statistics.top(4, SortBy.POINTS)
        alkuperaiset_pelaajat = PlayerReaderStub().get_players()

        alkuperaiset_pelaajat_sorted = sorted(
            alkuperaiset_pelaajat,
            reverse=True,
            key=lambda pelaaja: pelaaja.points
        )
        
        self.assertEqual(pelaajat[0].name, alkuperaiset_pelaajat_sorted[0].name)
        self.assertEqual(pelaajat[1].name, alkuperaiset_pelaajat_sorted[1].name)
        self.assertEqual(pelaajat[3].name, alkuperaiset_pelaajat_sorted[3].name)