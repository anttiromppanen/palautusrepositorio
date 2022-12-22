from kivi_paperi_sakset import KiviPaperiSakset

class KPSTekoaly(KiviPaperiSakset):
    def __init__(self, tekoaly):
        self._tekoaly = tekoaly

    def _toisen_siirto(self, ensimmaisen_siirto):
        tokan_siirto = self._tekoaly.anna_siirto()
        super()._tulosta_tekoalyn_siirto(tokan_siirto)

        return tokan_siirto