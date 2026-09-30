class Hissi:

    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.nykyinen_kerros = alin_kerros

    def kerros_ylos(self):
        if self.nykyinen_kerros < self.ylin_kerros:
            self.nykyinen_kerros += 1
            print(f"Hissi on nyt kerros : {self.nykyinen_kerros}")

    def kerros_alas(self):
        if self.nykyinen_kerros > self.alin_kerros:
            self.nykyinen_kerros -= 1
            print(f"Hissi on nyt kerros : {self.nykyinen_kerros}")

    def siirry_kerrokseen(self, kohde_kerros):
        if kohde_kerros < self.alin_kerros or kohde_kerros > self.ylin_kerros:
            print("Värää input")
            return

        while self.nykyinen_kerros < kohde_kerros:
            self.kerros_ylos()

        while self.nykyinen_kerros > kohde_kerros:
            self.kerros_alas()

class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_maara):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros

        self.hissit = []

        for _ in range(hissien_maara):
            self.hissit.append(Hissi(alin_kerros,ylin_kerros))

    def aja_hissia(self, hissin_numero, kohdekerros):
        if 1 <= hissin_numero <= len(self.hissit):
            print(f"Hissi numero {hissin_numero} lähtee kerroksen {kohdekerros}.")
            hissi = self.hissit[hissin_numero - 1]
            hissi.siirry_kerrokseen(kohdekerros)
        else:
            print("[!] Tarkista hissin numero!!")


# Tehtävät 10.1 ja 10.2
h = Hissi(1, 10)

h.siirry_kerrokseen(5)


h.siirry_kerrokseen(1)

talo = Talo(1, 7, 3)

talo.aja_hissia(1, 4)

talo.aja_hissia(2, 6)

talo.aja_hissia(1, 1)
