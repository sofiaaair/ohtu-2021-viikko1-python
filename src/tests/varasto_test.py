import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_alussa_tilaa_varastotilan_verran(self):
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 10)

    def test_varasto_ei_mene_miinukselle(self):
        self.varasto.ota_varastosta(5)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_varasto_ei_tayty_yli(self):
        self.varasto.lisaa_varastoon(8)
        self.varasto.lisaa_varastoon(8)
        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_negatiivinen_varastotila_on_nolla(self):
        self.varasto2 = Varasto(-1)
        self.assertAlmostEqual(self.varasto2.tilavuus, 0)

    def test_negatiivinen_alkusaldo_on_nolla(self):
        self.varasto2 = Varasto(-1, -1)
        self.assertAlmostEqual(self.varasto2.saldo, 0)

    def test_ylisaldo_muuttuu_maksimisaldoksi(self):
        self.varasto2 = Varasto(10, 20)
        self.assertAlmostEqual(self.varasto2.saldo, 10)

    def test_negatiivinen_ottaminen_palauttaa_nolla(self):
        self.varasto.lisaa_varastoon(5)
        self.varasto.ota_varastosta(-5)
        self.assertAlmostEqual(self.varasto.saldo, 5)

    def test_str_palautus_on_oikea(self):
        self.assertEqual(self.varasto.__str__(), "saldo = 0, vielä tilaa 10")

    def test_negatiivinen_lisaa_varaston_palauttaa_return(self):
        self.assertAlmostEqual(self.varasto.lisaa_varastoon(-1), None)
