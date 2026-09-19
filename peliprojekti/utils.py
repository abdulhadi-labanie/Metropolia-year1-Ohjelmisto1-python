import os


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


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


def read_int_input_with_exception(string, min_val, max_val, exception):
    while True:
        try:
            user_input = input(string)
            if user_input == exception:
                return exception
            user_input = int(user_input)
            if user_input < min_val or user_input > max_val:
                print(f"\t\tPlease choose a number between {min_val} and {max_val}!!!!!")
                continue
            return user_input  
        except ValueError:
            print("Please enter an integer!!!")


def read_float_input(string, min_val=-1000000.0, max_val=1000000.0) -> float:
    while True:
        try:
            user_input = float(input(string))
            if user_input < min_val or user_input > max_val:
                print(f"Please choose a number between {min_val} and {max_val}")
                continue
            return user_input
        except ValueError:
            print("Please enter a number!!!")
