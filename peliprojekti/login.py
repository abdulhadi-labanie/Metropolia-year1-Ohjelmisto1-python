from utils import read_int_input, read_str_input, clear_screen
from storage import create_new_manager_file, is_user_exist, get_manager



def register():
    print("Register page:")
    print("Please save your user name and age to be able to login again and track your progress.\n\n")
    user_name = read_str_input("> Please enter your name: ")
    user_age = read_int_input("> Please enter your age: ", 1, 99)

    while is_user_exist(user_name):
        print(f"\n[!] Sorry, the username '{user_name}' already exists. Please choose another one!!")
        user_name = read_str_input("> Please enter your name: ")

    if user_age >= 12:
        print(f"\nWelcome {user_name} to the game! to the airline :)")
        print(f"Your age are {user_age} year.\n")
        create_new_manager_file(user_name, user_age)

        input("\n> Press Enter to continue... ")
        return user_name
    else:
        print("You cannot register for the game if you are under 12 years old!!!\n")
        input("\n> Press Enter to continue... ")
        return None


def login():
    print("Login page:")
    user_name = read_str_input("> Please enter your user name to login: ")

    if is_user_exist(user_name):
        print(f"\nWelcome manager {user_name} to the airline!")
        input("\n> Press Enter to continue... ")
        return user_name
    else:
        print(f"Check your user name {user_name} not exist!!!\n")
        print("If you do not have an accuont please register first!!!\n")
        input("\n> Press Enter to continue... ")
        return None


def star_session_switcher():
    user_choice = read_int_input("\nEnter your choice (1-2): ",1,2)

    if user_choice == 1:
        clear_screen()
        return register()
    elif user_choice == 2:
        clear_screen()
        return login()
    return None



def show_start_session():
    print(f"=== AIRLINE MANAGEMENT SYSTEM ===")
    print("\n -- Start the game in airline -- \n")
    print("1. Register if you do not already have an account.")
    print("2. Login if you already have an account.")


def start_session():
    active_username = None

    while not active_username:
        clear_screen()
        show_start_session()
        active_username = star_session_switcher()

    current_manager = get_manager(active_username)

    return current_manager
