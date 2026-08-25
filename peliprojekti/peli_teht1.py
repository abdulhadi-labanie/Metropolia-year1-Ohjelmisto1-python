
def read_str_input(string):
    return input(string)


def read_int_input(string):
    while True:
        try:
            return int(input(string))
        except ValueError:
            print("Please enter an integer.")


def start():
    print("\n\n*********** Projekti 1. Ohjelmointiprojektitehtävän ***********\n\n")
    user_name = read_str_input("Please enter your name: ")
    user_age = read_int_input("Please enter your age: ")

    print(f"\nWelcome {user_name} to the play!")
    print(f"Your age is {user_age} year.\n")


start()