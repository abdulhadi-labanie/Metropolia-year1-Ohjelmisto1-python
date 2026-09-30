class Julkaisu:

    def __init__(self, nimi):
        self.nimi = nimi


class Kirja(Julkaisu):

    def __init__(self, nimi, kirjoittaja, sivumaara):
        super().__init__(nimi)
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivumaara

    def tulosta_tiedot(self):
        print(f"Julkaisun nimi: {self.nimi}")
        print(f"Kirjailija: {self.kirjoittaja}")
        print(f"Sivumäärä: {self.sivumaara}\n")


class Lehti(Julkaisu):

    def __init__(self, nimi, paatoimittaja):
        super().__init__(nimi)
        self.paatoimittaja = paatoimittaja

    def tulosta_tiedot(self):
        print(f"Julkaisun nimi: {self.nimi}")
        print(f"Päätoimittaja: {self.paatoimittaja}\n")

# Tehtävä 11.1
lehti = Lehti("Aku Ankka", "Aki Hyyppä")
kirja = Kirja("Hytti n:o 6", "Rosa Liksom", 200)

lehti.tulosta_tiedot()
kirja.tulosta_tiedot()
