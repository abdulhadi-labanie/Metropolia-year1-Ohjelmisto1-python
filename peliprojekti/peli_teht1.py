def read_str_input(string):
    return input(string)


def read_int_input(string, min_val, max_val):
    while True:
        try:
            user_input = int(input(string))
            if user_input < min_val or user_input > max_val:
                print(f"Please choose a number between {min_val} and {max_val}")
                continue
            return user_input      
        except ValueError:
            print("Please enter an integer!!!")


def login():
    user_name = read_str_input("> Please enter your name: ")
    user_age = read_int_input("> Please enter your age: ", 1, 99)

    if user_age >= 12:
        print(f"\nWelcome pilot {user_name} to the plane! Sorry the game :)")
        print(f"Your age is {user_age} year.\n")
        return True
    else:
        print("You cannot register for the game if you are under 12 years old!!!\n")
        return False


def show_instructions_menu():
    print("\n[Instructions] Manage your flights and fuel to maximize profit and reduce CO2 emissions!\n")


def show_main_menu():
    print("\n\t\t -- Main Menu -- \n")
    print("1. Start Game")
    print("2. Instructions")
    print("3. Quit (lopeta)\n")


def start():
    print("\n*********** Projekti 1 & 2 ***********\n")
    if login():
        is_running = True
        
        while is_running:
            show_main_menu()
            user_choice = read_str_input("Enter your choice (1-3 or 'lopeta'): ").strip().lower()

            if user_choice == "1":
                print("\n-> Starting the game... (Will be implemented in Projekti 3)\n")
            elif user_choice == "2":
                show_instructions_menu()
            elif user_choice == "3" or user_choice == "lopeta":
                print("\nQuitting the game... Goodbye!")
                is_running = False
            else:
                print("\nInvalid choice! Please enter 1, 2, 3 or 'lopeta'.")
    else:
        print("\nGoodbye!!!")


start()