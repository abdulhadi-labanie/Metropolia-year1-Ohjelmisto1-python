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


def read_user_nums(exception):
    smaller = None
    larger = None

    while True:
        user_input = read_int_input_with_exception(
            "Enter a number (or \"enter\" to finish): ",
            exception
        )

        if user_input == exception:
            return smaller, larger

        if smaller is None or user_input < smaller:
            smaller = user_input

        if larger is None or user_input > larger:
            larger = user_input

    

def start():
    print("\n\n############## Tehtävä 5: ##############\n\n")


    print(f"\n5.1 -\n")
    divided_by_three_list = is_divided_into_three(1, 1000)
    print_nums_divided_into_three(divided_by_three_list)


    print(f"\n5.2 -\n\n")
    smaller, larger = read_user_nums("")
    print(f"\n- The smaller number is = {smaller}.")
    print(f"- The larger number is = {larger}.")






start()