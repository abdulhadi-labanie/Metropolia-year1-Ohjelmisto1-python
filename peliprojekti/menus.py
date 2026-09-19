from utils import read_str_input

def show_instructions_menu():
    print("\n[Instructions] Manage your flights and fuel to maximize profit and reduce CO2 emissions!\n")


def main_menu_switcher():
    user_choice = read_str_input("Enter your choice (1-3 or 'lopeta'): ").strip().lower()

    if user_choice == "1":
        print("\n-> Starting the game... (Will be implemented in Projekti 3)\n")
        return True
    
    elif user_choice == "2":
        show_instructions_menu()
        return True
    
    elif user_choice == "3" or user_choice == "lopeta":
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
    show_main_menu()
    return main_menu_switcher()