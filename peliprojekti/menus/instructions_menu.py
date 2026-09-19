from main_meun import clear_screen
from utils import read_str_input


def instructions_menu_switcher():
    user_choice = read_str_input("Enter any key to return Main Menu: ")
    return


def show_instructions_menu():
    print("\n[Instructions] Manage your flights and fuel to maximize profit and reduce CO2 emissions!\n")


def instructions_menu():
    clear_screen()
    show_instructions_menu()
    instructions_menu_switcher()