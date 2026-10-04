from utils import read_int_input, clear_screen
from logic import start_game_logic, continue_game_logic
from models.clsSessionManager import clsSessionManager

def show_top_managers():
    clear_screen()
    
    input("> Coming soon!! \n> Press any key to return: ")

def star_game_switcher():
    manager = clsSessionManager.get_active_manager()
    active_company = manager.get_active_company()
    if active_company:
        user_choice = read_int_input("Enter your choice (1-4): ", 1, 4)
        if user_choice == 1:
            continue_game_logic.cntinue_game_with_active_company()
        elif user_choice == 2:
            start_game_logic.start_new_managing()
        elif user_choice == 3:
            show_top_managers()
        else:
            return
    else:
        user_choice = read_int_input("Enter your choice (1-3): ", 1, 3)
        if user_choice == 1:
            start_game_logic.start_new_managing()
        elif user_choice == 2:
            show_top_managers()
        else:
            return

def show_start_game():
    manager = clsSessionManager.get_active_manager()
    active_company = manager.get_active_company()

    print("\n\t\t -- Start the game as an airline CEO -- \n")
    if active_company:
        company_name_display = active_company.company_name
        print(f"1. Continue your management role with [{company_name_display}] company.")
        print("2. Start managing a position at new company.")
        print("3. Show the best managers in game.\n")
        print("4. Return to Main Menu.\n")
    else:
        print("1. Start managing a position at new company.")
        print("2. Show the best managers in game.\n")
        print("3. Return to Main Menu.\n")

def start_game():
    clear_screen()
    show_start_game()
    star_game_switcher()
