import random
import math

def read_str_input(string):
    return input(string)


def read_int_input(string, min_val, max_val) -> int:
    while True:
        try:
            user_input = int(input(string))
            if user_input < min_val or user_input > max_val:
                print(f"Please choose a number between {min_val} and {max_val}")
                continue
            return user_input      
        except ValueError:
            print("Please enter an integer!!!")


def read_float_input(string, min_val, max_val) -> float:
    while True:
        try:
            user_input = float(input(string))
            if user_input < min_val or user_input > max_val:
                print(f"Please choose a number between {min_val} and {max_val}")
                continue
            return user_input      
        except ValueError:
            print("Please enter an number!!!")


def random_dice():
    return random.randint(1,6)


def get_dice_count_for_6():
    result = 0
    count = 0
    while result != 6:
        result = random_dice()
        count += 1

    return result, count


def start():
    print("\n\n############## Tehtävä 7: ##############\n\n")

    print(f"\n7.1 -\n")
    result_of_roll_dice, roll_count = get_dice_count_for_6()
    print(f"The dice rolled count are {roll_count} to get {result_of_roll_dice}.")


    print(f"\n7.2 -\n\n")



    print(f"\n7.3 -\n\n")



    print(f"\n7.4 -\n\n")



    print(f"\n7.5 -\n\n")



    print(f"\n7.6 -\n\n")



start()