import random

def read_str_input(string):
    return input(string)


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


def get_number_form_user():
    user_input_numbers = []

    i = 0
    while True:
        print(i+1, end="")
        user_input_num = read_int_input_with_exception(".Plase Enter a number: ",-1000000,1000000,"")

        if user_input_num == "":
            break
        else:
            user_input_numbers.append(user_input_num)
            i += 1

    return user_input_numbers, i


def get_largest_numbers_in_list(user_list: list, nums=5):
    user_list.sort(reverse=True)
    return user_list[:nums]


def start():
    print("\n\n############## Tehtävä 6: ##############\n\n")

    print(f"\n6.1 -\n")
    dice_count = read_int_input("Enter how many dice to roll: ", 1, 10000)
    print(f"The sum total of dice are = {sum_total_of_dice(dice_count)}")


    print(f"\n6.2 -\n\n")
    user_input_list_numbers , count = get_number_form_user()
    largest_numbers_in_list = get_largest_numbers_in_list(user_input_list_numbers,5)
    print(f"\nThe number you enter count are {count} and the largest 5 numbers you enter are: {largest_numbers_in_list}")

    print(f"\n6.3 -\n\n")
    

    print(f"\n6.4 -\n\n")




start()