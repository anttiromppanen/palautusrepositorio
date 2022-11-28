import unittest
from unittest.mock import Mock
from kauppa import Kauppa
from tuote import Tuote
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto


class TestKauppa(unittest.TestCase):
    def varasto_saldo(self, tuote_id):
        if tuote_id == 1:
            return 10
        elif tuote_id == 2:
            return 5

    def varasto_hae_tuote(self, tuote_id):
        if tuote_id == 1:
            return Tuote(1, "maito", 5)
        elif tuote_id == 2:
            return Tuote(2, "juusto", 8)

    def setUp(self):
        self.pankki_mock = Mock()
        self.viitegeneraattori_mock = Mock()
        self.varasto_mock = Mock()
        self.kauppa = Kauppa(self.varasto_mock, self.pankki_mock,
                             self.viitegeneraattori_mock)

        self.viitegeneraattori_mock.uusi.return_value = 42
        self.varasto_mock.saldo.side_effect = self.varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = self.varasto_hae_tuote

    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan(self):
        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called()
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista

    def test_ostos_suoritetaan_oikeilla_parametreilla(self):
        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka", 42, "12345", self.kauppa._kaupan_tili, 5)

    def test_kaksi_ostosta_eri_tuotteilla_suoritetaan_oikeilla_parametreilla(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("simo", "54321")

        self.pankki_mock.tilisiirto.assert_called_with(
            "simo", 42, "54321", self.kauppa._kaupan_tili, 13
        )

    def test_kaksi_ostosta_samalla_tuotteella_suoritetaan_oikeilla_parametreilla(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("simo", "54321")

        self.pankki_mock.tilisiirto.assert_called_with(
            "simo", 42, "54321", self.kauppa._kaupan_tili, 10
        )

    def test_tuotetta_ei_veloiteta_jos_ei_loydy_varastosta(self):
        def varasto_saldo_tuotetta_nolla_kpl(tuote_id):
            if tuote_id == 1:
                return 10
            if tuote_id == 2:
                return 0

        self.varasto_mock.saldo.side_effect = varasto_saldo_tuotetta_nolla_kpl

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("simo", "54321")

        self.pankki_mock.tilisiirto.assert_called_with(
            "simo", 42, "54321", self.kauppa._kaupan_tili, 5
        )

    def test_aloita_asiointi_nollaa_edellisen_ostoksen_tiedot(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(1)

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)

        self.assertEqual(len(self.kauppa._ostoskori._tuotteet), 1)

    def test_pyydetaan_uusi_viite_jokaiselle_maksutapahtumalle(self):
        viitegeneraattori_mock = Mock(wraps=Viitegeneraattori())
        kauppa = Kauppa(self.varasto_mock, self.pankki_mock,
                        viitegeneraattori_mock)

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("simo", "12345")

        self.assertEqual(viitegeneraattori_mock.uusi.call_count, 1)

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(2)
        kauppa.tilimaksu("pasi", "54321")

        self.assertEqual(viitegeneraattori_mock.uusi.call_count, 2)

    def test_ostoskorista_poistaminen_lisaa_varaston_saldoa_oikein(self):
        varasto = Mock(wraps=Varasto())
        kauppa = Kauppa(varasto, self.pankki_mock, self.viitegeneraattori_mock)

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.lisaa_koriin(1)
        kauppa.lisaa_koriin(1)
        kauppa.poista_korista(1)

        self.assertEqual(varasto.saldo(1), 98)
