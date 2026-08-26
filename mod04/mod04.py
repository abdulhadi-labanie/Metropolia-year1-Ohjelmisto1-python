from mod01_03 import mod01_03_teht


def check_num_size(num, min_size, equals = True):
    if equals:
        if num >= min_size:
            return True
        else:
            return False
    else:
        if num > min_size:
            return True
        else:
            return False


def print_bool_ckeck_str(bool_result, true_result_str, false_result_str):
    if bool_result:
        print(true_result_str)
    else:
        print(false_result_str)



def start():
    print("\n\n############## Tehtävä 4: ##############\n\n")


    print(f"\n4.1 -\n")
    fish_length = mod01_03_teht.read_int_input("Enter a fish length: ")
    print_bool_ckeck_str(check_num_size(fish_length, 42), "the fish length is good.", "A zander must be 42 centimeters or longer to meet the size limit.")

