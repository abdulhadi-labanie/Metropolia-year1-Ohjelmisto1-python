def read_str_input(string):
    return input(string)


def read_int_input(string, min_val, max_val) -> int:
    while True:
        try:
            user_input = int(input(string))
            if user_input < min_val or user_input > max_val:
                print(f"Please choose a number between {min_val} and {max_val}")
                continue
            return user_input      
        except ValueError:
            print("Please enter an integer!!!")


def task8_1():
    vuodenajan = "kevät", "kesä", "syksy", "talvi"

    user_month_input = read_int_input("Enter a month number: ", 1, 12)

    if user_month_input in [12,1,2]:
        print(f"The season of month {user_month_input} is : {vuodenajan[3]}")
    elif user_month_input in [3,4,5]:
        print(f"The season of month {user_month_input} is : {vuodenajan[0]}")
    elif user_month_input in [6,7,8]:
        print(f"The season of month {user_month_input} is : {vuodenajan[1]}")
    else:
        print(f"The season of month {user_month_input} is : {vuodenajan[2]}")


def task8_2():
    names_set = set()

    while True:
        name_input = read_str_input("\n-> Please enter a name: ").strip()

        if name_input == "":
            break

        if name_input in names_set:
            print(f"Aiemmin syötetty nimi : {name_input}")
        else:
            print(f"Uusi nimi : {name_input}")
            names_set.add(name_input)

    print("\nAll names you entered:")
    for name in names_set:
        print(name)


def task8_3():
    lentoasemat = {}

    while True:
        print("Valitse toiminto:")
        print("1 = Syötä uusi lentoasema")
        print("2 = Hae lentoaseman tiedot")
        print("3 = Lopeta")

        valinta = input("Valintasi (1-3): ").strip()

        if valinta == "1":
            icao = input("Anna ICAO-koodi: ").strip().upper()
            nimi = input("Anna lentoaseman nimi: ").strip()
            lentoasemat[icao] = nimi
            print(f"Lentoasema {nimi} ({icao}) tallennettu.")

        elif valinta == "2":
            icao = input("Anna ICAO-koodi: ").strip().upper()
            if icao in lentoasemat:
                print(f"ICAO-koodia {icao} vastaa lentoasema: {lentoasemat[icao]}")
            else:
                print(f"Lentoasemaa koodilla {icao} ei löytynyt!")

        elif valinta == "3":
            print("Kiitos ja näkemiin!")
            break
        else:
            print("Virheellinen valinta, yritä uudelleen.")


def start():
    print("\n\n############## Tehtävä 8: ##############\n\n")

    print(f"\n\n8.1 -\n")
    task8_1()

    print(f"\n\n8.2 -\n")
    task8_2()

    print(f"\n\n8.3 -\n")
    task8_3()

start()