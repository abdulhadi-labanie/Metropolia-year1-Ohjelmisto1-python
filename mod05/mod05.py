import random

def read_str_input(string):
    return input(string)


def read_int_input(string):
    while True:
        try:
            return int(input(string))
        except ValueError:
            print("Please enter an integer.")


def read_int_input_with_exception(string, exception):
    while True:
        num = input(string)

        if num == exception:
            return exception

        try:
            return int(num)
        except ValueError:
            print("Please enter an integer.")



def is_divided_into_three(start, end):
    num = start
    divided_nums = []

    while num < end:
        if num % 3 == 0:
            divided_nums.append(num)
        num += 1

    return divided_nums


def print_nums_divided_into_three(nums_list):
    for num in nums_list:
        print(num, end=" ")


def read_and_print_user_inch_values():
    inch = 2.54

    while True:
        user_input = read_int_input(
            "Enter an inchs to switch it to cm: ")

        if user_input < 0:
            break

        else:
            total = user_input * inch
            print(f"The inchs {user_input} = {total}cm.")



def read_user_nums(exception):
    smaller = None
    larger = None

    while True:
        user_input = read_int_input_with_exception(
            "Enter a number (or \"Enter\" to finish and get smaller and larger numbers): ",
            exception
        )

        if user_input == exception:
            return smaller, larger

        if smaller is None or user_input < smaller:
            smaller = user_input

        if larger is None or user_input > larger:
            larger = user_input


def guess_random_number(rand_start, rand_end):
    rand_num = random.randint(rand_start, rand_end)
    user_input = read_int_input("Enter a number to gess random number: ")

    while True:
        if user_input == rand_num:
            print(f"Yes, you gess the random number. you number is ({user_input}) and the random number in ({rand_num})")
            break

        elif  user_input < rand_num:
            print(f"No, the random number is larger than ({user_input})!!")
        elif  user_input > rand_num:
            print(f"No, the random number is smaller than ({user_input})!!")

        user_input = read_int_input("Enter a number to gess random number: ")


def user_login():
    user_name = "python"
    password = "rules"

    print("Hello, login with user name and password:\n")

    user_name_input = read_str_input("Enter a user name: ")
    password_input = read_str_input("Enter a password: ")

    i = 5
    while True:
        if i > 1:
            if user_name_input == user_name and password_input == password:
                print("\nAccepted the user name and password, Welcome to our program.")
                break
            else:
                i -= 1
                print("\nIncorrect username or password!!!")
                print(f"You have {i} attempts\n")

                user_name_input = read_str_input("Enter a user name again: ")
                password_input = read_str_input("Enter a password again: ")

        else:
            print("\nYou have exhausted your attempts!!\nYour tries to register 5 times with incorrect information!!!")
            break


def start():
    print("\n\n############## Tehtävä 5: ##############\n\n")


    print(f"\n5.1 -\n")
    divided_by_three_list = is_divided_into_three(1, 1000)
    print_nums_divided_into_three(divided_by_three_list)


    print(f"\n5.2 -\n\n")
    read_and_print_user_inch_values()


    print(f"\n5.3 -\n\n")
    smaller, larger = read_user_nums("")
    print(f"\n- The smaller number is = {smaller}.")
    print(f"- The larger number is = {larger}.")


    print(f"\n5.4 -\n\n")
    guess_random_number(1, 10)


    print(f"\n5.5 -\n\n")
    user_login()


    print(f"\n5.6 -\n\n")



start()