from utils import read_int_input, read_str_input
from menus import main_menu

def login():
    user_name = read_str_input("> Please enter your name: ")
    user_age = read_int_input("> Please enter your age: ", 1, 99)

    if user_age >= 12:
        print(f"\nWelcome pilot {user_name} to the plane! Sorry the game :)")
        print(f"Your age are {user_age} year.\n")
        return True
    else:
        print("You cannot register for the game if you are under 12 years old!!!\n")
        return False


def main():
    print("\n*********** Projekti 1 & 2 ***********\n")
    if login():
        is_running = True
        
        while is_running:
            is_running = main_menu()
    else:
        print("\nGoodbye!!!")
        


if __name__ == "__main__":
    main()