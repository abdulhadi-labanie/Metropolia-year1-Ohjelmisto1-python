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


def read_float_input(string, min_val=-1000000.0, max_val=1000000.0) -> float:
    while True:
        try:
            user_input = float(input(string))
            if user_input < min_val or user_input > max_val:
                print(
                    f"Please choose a number between {min_val} and {max_val}"
                )
                continue
            return user_input
        except ValueError:
            print("Please enter a number!!!")


def random_dice(sides = 6) -> int:
    return random.randint(1,sides)


def get_dice_count_for_6():
    result = 0
    count = 0
    while result != 6:
        result = random_dice()
        count += 1
        print(f"Roll {count}: {result}")

    return result, count


def roll_dise_for_max_sides():
    max_sides = read_int_input("Enter maximum sides of the dice: ", 2, 1000)
    result = 0
    count = 0
    while result != max_sides:
        result = random_dice(max_sides)
        count += 1
        print(f"Roll {count}: {result}")
    return result


def get_liters(gallons: float) -> float:
    return gallons * 3.785


def gallons_to_liters_loop():
    while True:
        gallons = read_float_input("Enter gallons (negative value to quit): ")
        if gallons < 0:
            print("Stopping fuel conversion.")
            break
        liters = get_liters(gallons)
        print(f"{gallons} gallons = {liters:.2f} liters")


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


def calculate_pizza_unit_price(diameter_cm: float, price_eur: float) -> float:
    radius_m = (diameter_cm / 100) / 2
    area_m2 = math.pi * (radius_m**2)
    return price_eur / area_m2


def start_pizza_comparator():
    print("Pizza 1:")
    d1 = read_float_input("  Diameter (cm): ", 1, 1000)
    p1 = read_float_input("  Price (€): ", 0.1, 1000)

    print("Pizza 2:")
    d2 = read_float_input("  Diameter (cm): ", 1, 1000)
    p2 = read_float_input("  Price (€): ", 0.1, 1000)

    unit_price1 = calculate_pizza_unit_price(d1, p1)
    unit_price2 = calculate_pizza_unit_price(d2, p2)

    print(f"\nPizza 1 unit price: {unit_price1:.2f} €/m²")
    print(f"Pizza 2 unit price: {unit_price2:.2f} €/m²")

    if unit_price1 < unit_price2:
        print("-> Pizza 1 provides better value for money!")
    elif unit_price2 < unit_price1:
        print("-> Pizza 2 provides better value for money!")
    else:
        print("-> Both pizzas have the exact same value!")


def start():
    print("\n\n############## Tehtävä 7: ##############\n\n")

    print(f"\n\n7.1 -\n")
    result_of_roll_dice, roll_count = get_dice_count_for_6()
    print(f"The dice rolled count are {roll_count} to get {result_of_roll_dice}.")


    print(f"\n\n7.2 -\n")
    roll_dice_max_sides = roll_dise_for_max_sides()
    print(f"The dice is rolled {roll_dice_max_sides}")


    print(f"\n\n7.3 -\n")
    gallons_to_liters_loop()


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
    start_pizza_comparator()


start()