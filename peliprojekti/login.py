from utils import read_int_input, read_str_input, clear_screen
from storage import create_new_manager_file, is_user_exist



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
        return True
    else:
        print("You cannot register for the game if you are under 12 years old!!!\n")
        input("\n> Press Enter to continue... ")
        return False


def login():
    print("Login page:")
    user_name = read_str_input("> Please enter your user name to login: ")

    if is_user_exist(user_name):
        print(f"\nWelcome manager {user_name} to the airline!")
        input("\n> Press Enter to continue... ")
        return True
    else:
        print("Check your user name or age!!!\n")
        print("If you do not have an accuont please register first!!!\n")
        input("\n> Press Enter to continue... ")
        return False


def start_seshen():
    pass    