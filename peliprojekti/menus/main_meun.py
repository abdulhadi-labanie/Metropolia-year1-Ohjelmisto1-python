from utils import read_str_input, clear_screen
from menus.start_game_menu import start_game
from menus.instructions_menu import instructions_menu


def main_menu_switcher(current_manager):
    while True:
        user_choice = read_str_input("Enter your choice (1-3 or 'lopeta'): ").strip().lower()

        if user_choice == "1":
            start_game(current_manager)     
            return True
        
        elif user_choice == "2":
            instructions_menu()
            return True
        
        elif user_choice == "3" or user_choice == "lopeta":
            clear_screen()
            print("\nQuitting the game... Goodbye!")
            return False
        
        else:
            print("\n\nPlease Invalid choice! Please enter 1, 2, 3 or 'lopeta'.")


def show_main_menu(current_manager):
    print("\n\t\t -- Main Menu -- \n")
    print(f"***** Active Manager: {current_manager['user_name']} *****\n\n")
    print("1. Start Game")
    print("2. Instructions")
    print("3. Quit (lopeta)\n")


def main_menu(current_manager):
    clear_screen()
    show_main_menu(current_manager)
    return main_menu_switcher(current_manager)
