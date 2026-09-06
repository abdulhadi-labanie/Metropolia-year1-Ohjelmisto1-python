import random

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


def random_dice():
    return random.randint(1,6)


def sum_total_of_dice(dice_cont):
    sum_total = 0
    for i in range(1, dice_cont+1):
        dice = random_dice()
        print(f"dice{i} = {dice}")
        sum_total += dice

    return sum_total




def start():
    print("\n\n############## Tehtävä 6: ##############\n\n")

    print(f"\n6.1 -\n")
    dice_count = read_int_input("Enter how many dice to roll: ", 1, 10000)
    print(f"The sum total of dice are = {sum_total_of_dice(dice_count)}")


    print(f"\n6.2 -\n\n")


    print(f"\n6.3 -\n\n")


    print(f"\n6.4 -\n\n")




start()