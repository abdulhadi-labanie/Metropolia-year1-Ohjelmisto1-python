def read_str_input(string):
    return f"{input(string)}"

def get_full_name():
    first_name = read_str_input("Enter your first name: ")
    last_name = read_str_input("Enter your last name: ")

    return f"{first_name} {last_name}"

def print_full_name(full_name):
    print(f"Terve : {full_name}")

def get_age():
    return int(input("Enter your age: "))

def start():


    print_full_name(get_full_name())

start()