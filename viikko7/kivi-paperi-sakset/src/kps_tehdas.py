from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly

class KPSTehdas():
    def luo_peli(self, tyyppi, tekoaly, tekoaly_parannettu):
        if tyyppi.endswith("a"):
            return self.luo_pelaaja_vs_pelaaja()
        if tyyppi.endswith("b"):
            return self.luo_pelaaja_vs_tekoaly(tekoaly)
        if tyyppi.endswith("c"):
            return self.luo_pelaaja_vs_parempi_tekoaly(tekoaly_parannettu)
        
        return None

    def luo_pelaaja_vs_pelaaja(self):
        return KPSPelaajaVsPelaaja()
    
    def luo_pelaaja_vs_tekoaly(self, tekoaly):
        return KPSTekoaly(tekoaly)

    def luo_pelaaja_vs_parempi_tekoaly(self, tekoaly_parannettu):
        return KPSParempiTekoaly(tekoaly_parannettu)