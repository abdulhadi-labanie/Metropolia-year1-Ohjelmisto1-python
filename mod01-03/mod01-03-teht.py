import math
import random


def read_str_input(string):
    return input(string)


def read_float_input(string):
    return float(input(string))


def get_full_name():
    first_name = read_str_input("Enter your first name: ")
    last_name = read_str_input("Enter your last name: ")

    return f"{first_name} {last_name}"


def calculating_area_of_circle(radius):
    return f"{(math.pi * radius**2):.2f}"


def start():
    print("\n\n############## Tehtävä 3: ##############\n\n")

    print(f"\n3.1-\nTerve : {get_full_name()}")

    print("\n\n3.2-")
    radius = read_float_input("Enter a radius of circle: ")
    print(f"Ympyrän pinta alan on = {calculating_area_of_circle(radius)}")

    print("\n\n3.3-")


    print("\n\n3.4-")


    print("\n\n3.5-")



    print("\n\n3.6-")


start()