from utils import read_str_input
from start_game_menu import start_game
from instructions_menu import instructions_menu
import os


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def main_menu_switcher():
    user_choice = read_str_input("Enter your choice (1-3 or 'lopeta'): ").strip().lower()

    if user_choice == "1":
        start_game()     
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
        return True


def show_main_menu():
    print("\n\t\t -- Main Menu -- \n")
    print("1. Start Game")
    print("2. Instructions")
    print("3. Quit (lopeta)\n")


def main_menu():
    clear_screen()
    show_main_menu()
    return main_menu_switcher()
