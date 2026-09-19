from utils import read_int_input
from main_meun import clear_screen


def continue_management_role():
    pass


def start_new_managing():
    pass


def show_top_managers():
    pass


def star_game_switcher():
    user_choice = read_int_input("Enter your choice (1-4): ",1,4)

    if user_choice == 1:
        continue_management_role()
    elif user_choice == 2:
        start_new_managing()
    elif user_choice == 3:
        show_top_managers()
    else:
        return


def show_start_game():
    print("\n\t\t -- Start the game as an airline CEO -- \n")
    print("1. Continue your management role whit (company) company.")
    print("2. Start managing a position at new company.")
    print("3. Show the best managers in game.\n")
    print("4. Return to Main Menu.\n")


def start_game():
    clear_screen()
    show_start_game()
    star_game_switcher()
