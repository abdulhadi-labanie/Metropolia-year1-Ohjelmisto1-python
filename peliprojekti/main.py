from login import start_session
from menus.main_meun import main_menu
from models.clsSessionManager import clsSessionManager

def main():
    print("\n*********** ECO-Airline Manager ***********\n")
    start_session()
    if clsSessionManager.get_active_manager():
        is_running = True

        while is_running:
            is_running = main_menu()

if __name__ == "__main__":
    main()
