import random

class Auto:

    def __init__(self, rekisteritunnus, huippunopeus, tamanhtkinen_nopeus = 0, kulettu_matka = 0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tamanhtkinen_nopeus = tamanhtkinen_nopeus
        self.kulettu_matka = kulettu_matka


    def kiihdyta(self, nopeuden_muutos):
        self.tamanhtkinen_nopeus += nopeuden_muutos

        if self.tamanhtkinen_nopeus > self.huippunopeus:
            self.tamanhtkinen_nopeus = self.huippunopeus
        if self.tamanhtkinen_nopeus < 0:
            self.tamanhtkinen_nopeus = 0


    def kulje(self, aika):
        self.kulettu_matka += aika * self.tamanhtkinen_nopeus


    def print_auto(self):
        print(f"Auto rekisteritunnus = {self.rekisteritunnus}")
        print(f"Auto huippunopeus = {self.huippunopeus}")
        print(f"Auto tamanhtkinen_nopeus = {self.tamanhtkinen_nopeus}")
        print(f"Auto kulettu_matka = {self.kulettu_matka}")


def generate_cars():
    autot = []
    for i in range(1, 11):
        rekisteri = f"ABC-{i}"
        huippu = random.randint(100, 200)
        autot.append(Auto(rekisteri, huippu))
    return autot


def start_game():
    autot = generate_cars()

    kilpailu_kaynnissa = True

    while kilpailu_kaynnissa:
        for auto in autot:
            auto.kiihdyta(random.randint(-10, 15))
            auto.kulje(1)

            if auto.kulettu_matka >= 10000:
                kilpailu_kaynnissa = False

    print(f"{'Rekisteri':<12} | {'Huippunopeus':<14} | {'Nopeus':<10} | {'Matka (km)':<12}")
    print("-" * 58)

    for auto in autot:
        print(f"{auto.rekisteritunnus:<12} | {auto.huippunopeus:<14} km/h | {auto.tamanhtkinen_nopeus:<10} km/h | {auto.kulettu_matka:<12.1f} km")

# Mod 9.1
OP_auto = Auto("ABC-123", 142, 20,1000)
OP_auto.print_auto()

# Mod 9.2
OP_auto.kiihdyta(30)
OP_auto.kiihdyta(70)
OP_auto.kiihdyta(50)
print(f"Tamanhtkinen nopeus = {OP_auto.tamanhtkinen_nopeus} km/h")

OP_auto.kiihdyta(-200)
print(f"Tamanhtkinen nopeus = {OP_auto.tamanhtkinen_nopeus} km/h")

# Mod 9.3
OP_auto.kulje(20)
print(f"Kulettu matka = {OP_auto.kulettu_matka} km")

# Mod 9.4
start_game()
