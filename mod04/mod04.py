def read_str_input(string):
    return input(string)


def read_int_input(string):
    while True:
        try:
            return int(input(string))
        except ValueError:
            print("Please enter an integer.")


def check_num_size(num, min_size, equals = True):
    if equals:
        return num >= min_size
    else:
        return num > min_size


def print_bool_ckeck_str(bool_result, true_result_str, false_result_str):
    if bool_result:
        print(true_result_str)
    else:
        print(false_result_str)


def check_cabin_class(answer):
    answer = answer.upper()
    if answer == "LUX".upper() or answer == "A" or answer == "B" or answer == "C":
        if answer == "LUX":
            print("Thank you seat reservation LUX: upper-deck cabin with a balcony.")
        elif answer == "A":
            print("Thank you seat reservation above the car deck, equipped with a window.")
        elif answer == "B":
            print("Thank you seat reservation windowless cabin above the car deck.")
        else:
            print("Thank you seat reservation windowless cabin below the car deck.")
    else:
        print("Error message! Invalid cabin class (LUX, A, B or C)")



def start():
    print("\n\n############## Tehtävä 4: ##############\n\n")


    print(f"\n4.1 -\n")
    fish_length = read_int_input("Enter a fish length: ")
    print_bool_ckeck_str(check_num_size(fish_length, 42), "the fish length is good.", "A zander must be 42 centimeters or longer to meet the size limit.")


    print(f"\n4.2 -\n")
    print("Chouse a cabin class:\n \
    1. LUX: upper-deck cabin with a balcony.\n \
    2. A: above the car deck, equipped with a window.\n \
    3. B: windowless cabin above the car deck.\n \
    4. C: windowless cabin below the car deck.\n")
    user_cabin_class = read_str_input("Enter a cabin class: ")
    check_cabin_class(user_cabin_class)


start()