from kivi_paperi_sakset import KiviPaperiSakset


class KPSParempiTekoaly(KiviPaperiSakset):
    def __init__(self, parannettu_tekoaly):
        self._parannettu_tekoaly = parannettu_tekoaly
        self._ensimmainen_siirto = True
    
    def _toisen_siirto(self, ensimmaisen_siirto):
        tokan_siirto = self._parannettu_tekoaly.anna_siirto()
        super()._tulosta_tekoalyn_siirto(tokan_siirto)

        if self._ensimmainen_siirto:
            self._ensimmainen_siirto = False
            return tokan_siirto
        
        self._parannettu_tekoaly.aseta_siirto(ensimmaisen_siirto)
        return tokan_siirto