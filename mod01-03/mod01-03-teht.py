import math
import random


def read_str_input(string):
    return input(string)


def read_int_input(string):
    return int(input(string))


def read_float_input(string):
    return float(input(string))


def int_range_loops(end):
    nums = []
    for i in range(1, end +1):
        number = read_int_input(f"{i}. Enter a number: ")
        nums.append(number)

    return nums


def get_full_name():
    first_name = read_str_input("Enter your first name: ")
    last_name = read_str_input("Enter your last name: ")

    return f"{first_name} {last_name}"


def calculating_area_of_circle(radius):
    return f"{(math.pi * radius**2):.2f}"


def calculate_area_of_rectangle(rectangle_width, rectangle_length):
    return rectangle_width * rectangle_length


def sum_number(nums):
    total = 0

    for num in nums:
        total += num

    return total


def product_number(nums):
    total = 1

    for num in nums:
        total *= num

    return total


def average_of_numbers(nums):
    total = 0
    i = 0
    for num in nums:
        total += num
        i += 1

    return total / i


def start():
    print("\n\n############## Tehtävä 3: ##############\n\n")

    print(f"\n3.1-\nTerve : {get_full_name()}")

    print("\n\n3.2-")
    radius = read_float_input("Enter a radius of circle: ")
    print(f"Ympyrän pinta alan on = {calculating_area_of_circle(radius)}")

    print("\n\n3.3-")
    rectangle_width = read_float_input("Enter a rectangle width: ")
    rectangle_length = read_float_input("Enter a rectang lelength: ")
    print(f"The area of rectangle is : {calculate_area_of_rectangle(rectangle_width,rectangle_length)}")

    print("\n\n3.4-")
    number3_4 = int_range_loops(3)
    print(f"\n- The sum of numbers is = {sum_number(number3_4)}")
    print(f"\n- The product of numbers is = {product_number(number3_4)}")
    print(f"\n- The average of numbers is = {average_of_numbers(number3_4)}")

    print("\n\n3.5-")



    print("\n\n3.6-")


start()