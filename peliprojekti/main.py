from login import start_session
from menus.main_meun import main_menu


def main():
    print("\n*********** Projekti 1 & 2 & 3 ***********\n")

    current_manager = start_session()

    if current_manager:
        is_running = True

        while is_running:
            is_running = main_menu(current_manager)


if __name__ == "__main__":
    main()
