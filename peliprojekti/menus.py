from utils import read_str_input, read_int_input

# 1.1 start game menu
def star_game_switcher():
    user_choice = read_int_input("Enter your choice (1-4): ")

    if user_choice == 1:
        pass
    elif user_choice == 2:
        pass
    elif user_choice == 3:
        pass
    else:
        main_menu()


def show_start_game():
    print("\n\t\t -- Start the game as an airline CEO -- \n")
    print("1. Continue your management role whit (company) company.")
    print("2. Start managing a position at new company.")
    print("3. Show the best managers in game.\n")
    print("4. Return to Main Menu.\n")

# 1.2 instructionsmenu

def show_instructions_menu():
    print("\n[Instructions] Manage your flights and fuel to maximize profit and reduce CO2 emissions!\n")

# 1.main menu

def main_menu_switcher():
    user_choice = read_str_input("Enter your choice (1-3 or 'lopeta'): ").strip().lower()

    if user_choice == "1":
        show_start_game()
        star_game_switcher()      
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