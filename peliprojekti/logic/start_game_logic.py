from utils import clear_screen, read_str_input
from data_catalogs.aircraft_catalog import aircraft_catalog
from storage import create_new_career
from logic import continue_game_logic
from models.clsSessionManager import clsSessionManager

def Select_country_headquarters():
    print("This country for the company headquarters:")
    print("1.[Finland]  2.[Swiden]  3.[Germany]  4.[Turkish]  5.[Syria].")
    is_country_selected = False
    while not is_country_selected:
        country = read_str_input("Select one of them [country name or numbers]: ").strip().capitalize()
        hub_airport = ""

        if country in ["Finland", "1"]:
            country, hub_airport = "Finland", "HEL"
            is_country_selected = True
        elif country in ["Swiden", "2"]:
            country, hub_airport = "Sweden", "ARN"
            is_country_selected = True
        elif country in ["Germany", "3"]:
            country, hub_airport = "Germany", "BER"
            is_country_selected = True
        elif country in ["Turkish", "4"]:
            country, hub_airport = "Turkey", "IST"
            is_country_selected = True
        elif country in ["Syria", "5"]:
            country, hub_airport = "Syria", "DAM"
            is_country_selected = True
    return country, hub_airport

def fell_first_company_data():
    manager = clsSessionManager.get_active_manager()
    print("Interface for appointing a new airline manager:")
    company_name = read_str_input("Enter your company name: ")
    country, hub_airport = Select_country_headquarters()
    company_budget = 1000000000
    print(f"Your company budget is : {company_budget:,}€")
    fleet_count = 0

    success = create_new_career(manager.user_name, company_name, country, hub_airport, company_budget, fleet_count)
    if success:
        continue_game_logic.update_success_data(manager.user_name)

def start_new_managing():
    clear_screen()
    fell_first_company_data()
    input("\n> Press Enter to continue to Aircraft Market...")

    clear_screen()
    continue_game_logic.show_aircraft_catalog_table_view()
    continue_game_logic.buy_aircraft(aircraft_catalog())
    continue_game_logic.show_my_fleet()
    input("\n> Press Enter to create company plan for next year...")

    clear_screen()
    continue_game_logic.cntinue_game_with_active_company(True)
