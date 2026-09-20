from utils import clear_screen

def show_start_new_managing_screen(current_manager):
    print("\tInterface for appointing a new airline manager")
    print(f"\n\tWelcome to the airline, Manager {current_manager}")


def start_new_managing(current_manager):
    clear_screen()
    show_start_new_managing_screen(current_manager)
