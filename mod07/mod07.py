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


def random_dice(sides = 6) -> int:
    return random.randint(1,sides)


def get_dice_count_for_6():
    result = 0
    count = 0
    while result != 6:
        result = random_dice()
        count += 1

    return result, count


def roll_dise_for_max_sides():
    max_sides = read_int_input("Enter maximum sides of the dice: ", 2, 1000)
    result = 0
    while result != max_sides:
        result = random_dice(max_sides)
    return result


def get_liters(gallons: float) -> float:
    return gallons * 3.785


def gallons_to_liters():
    gallons = read_float_input("Enter gallons: ",0,1000000)
    liters = get_liters(gallons)

    print(f"{gallons} gallons = {liters:.2f} liters.")


def calculate_sum(numbers: list[int]) -> int:
    total = 0
    for num in numbers:
        total += num
    return total


def remove_odd_numbers(numbers: list[int]) -> list[int]:
    even_numbers = []
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers


def start():
    print("\n\n############## Tehtävä 7: ##############\n\n")

    print(f"\n\n7.1 -\n")
    result_of_roll_dice, roll_count = get_dice_count_for_6()
    print(f"The dice rolled count are {roll_count} to get {result_of_roll_dice}.")


    print(f"\n\n7.2 -\n")
    roll_dice_max_sides = roll_dise_for_max_sides()
    print(f"The dice is rolled {roll_dice_max_sides}")


    print(f"\n\n7.3 -\n")
    gallons_to_liters()


    print(f"\n\n7.4 -\n")
    list7_4 = [10, 25, 30, 47, 50]
    total_sum7_4 = calculate_sum(list7_4)
    print(f"Original list: {list7_4}")
    print(f"Sum of elements: {total_sum7_4}")


    print(f"\n\n7.5 -\n")
    original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    filtered_list = remove_odd_numbers(original_list)
    print(f"Original list: {original_list}")
    print(f"Filtered (even numbers only): {filtered_list}")


    print(f"\n\n7.6 -\n")



start()