from utils import read_int_input, clear_screen
from logic import start_game_logic


def continue_management_role(current_manager):
    pass


def show_top_managers():
    pass


def star_game_switcher(current_manager):
    user_choice = read_int_input("Enter your choice (1-4): ",1,4)

    if user_choice == 1:
        continue_management_role(current_manager)
    elif user_choice == 2:
        start_game_logic.start_new_managing(current_manager)
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


def start_game(current_manager):
    clear_screen()
    show_start_game()
    star_game_switcher(current_manager)
