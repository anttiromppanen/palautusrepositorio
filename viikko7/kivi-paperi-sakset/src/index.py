from tekoaly import Tekoaly
from tekoaly_parannettu import TekoalyParannettu
from kps_tehdas import KPSTehdas


def main():
    while True:
        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              )

        vastaus = input()

        print(
            "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
        )

        pelimuoto = KPSTehdas().luo_peli(
            vastaus,
            Tekoaly(),
            TekoalyParannettu(10)
        )

        if not pelimuoto:
            break

        pelimuoto.pelaa()

if __name__ == "__main__":
    main()
