from utils import clear_screen, read_str_input, read_bool_input
from aircraft_catalog import print_aircraft_catalog_table, aircraft_catalog
from storage import create_new_career, get_manager, storage_new_aircraft
from models.clsSessionManager import clsSessionManager
from models.clsManager import clsManager


def update_success_data(user_name):
    updated_dict = get_manager(user_name)
    new_manager_obj = clsManager.from_dict(updated_dict)
    clsSessionManager.set_active_manager(new_manager_obj)
    print("\n[ok] Data successfully saved and synchronized!")


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


def fell_first_company_plan():
    manager = clsSessionManager.get_active_manager()
    print("Interface for appointing a new airline manager:")
    company_name = read_str_input("Enter your company name: ")
    country, hub_airport = Select_country_headquarters()
    company_budget = 1000000000
    print(f"Your company budget is : {company_budget:,}€")
    fleet_count = 0

    success = create_new_career(manager.user_name, company_name, country, hub_airport, company_budget, fleet_count)

    if success:
        update_success_data(manager.user_name)


def show_aircraft_catalog_table_view():
    manager = clsSessionManager.get_active_manager()
    print(f"\nWelcome to the airline, Manager {manager.user_name}.\n\n")
    print_aircraft_catalog_table(aircraft_catalog())


def buy_aircraft(catalog_list):
    is_want_buy_aircraft = True

    while is_want_buy_aircraft:
        manager = clsSessionManager.get_active_manager()
        active_company = manager.get_active_company()
        if not active_company:
            print("\n[!] Error: No active company found!")
            break

        current_budget = active_company.company_budget
        print(f"\nYour company budget = {current_budget:,} €")
        user_selection = read_str_input("\nSelect an aircraft buy [model name] or [aircraft ID]: ").strip().upper()

        selected_plane = None
        for aircraft in catalog_list:
            if aircraft["model"].upper() == user_selection or aircraft["aircraft_ID"].upper() == user_selection:
                selected_plane = aircraft
                break

        if selected_plane:
            plane_price = selected_plane["financials"]["price"]
            if current_budget >= plane_price:
                new_budget = current_budget - plane_price
                selected_plane["aircraft_ID"] += "-" + str(active_company.fleet_count +1)
                success = storage_new_aircraft(manager.user_name, new_budget, selected_plane)

                if success:
                    update_success_data(manager.user_name)
                    print(f"\n[ok] Successfully purchased {selected_plane['manufacturer']} {selected_plane['model']}!")
            else:
                print(f"\n[!] Budget insufficient! Price: {plane_price:,} €, Your Budget: {current_budget:,} €")
        else:
            print(f"\n[!] Aircraft model '{user_selection}' not found in catalog!")

        manager = clsSessionManager.get_active_manager()
        active_company = manager.get_active_company()
        
        if active_company.fleet_count != 0:
            is_want_buy_aircraft = read_bool_input("\nDo you want to buy another aircraft? [y/n]: ")
        else:
            print("[!] Your fleet_count should have a minmom one aircraft. buy your first aircraft.")


def show_my_fleet():
    manager = clsSessionManager.get_active_manager()
    active_company = manager.get_active_company()

    if not active_company or not active_company.years:
        print("\n[!] No active company or fleet data found.")
        return

    latest_year_label = list(active_company.years.keys())[-1]
    latest_year_obj = active_company.years[latest_year_label]
    owned_planes = latest_year_obj.planes

    print(f"\n\t===== {active_company.company_name} - MY FLEET =====\n")

    if not owned_planes:
        print("Your fleet is currently empty! Buy aircraft from the market.")
        return

    header = f"| {'#':<3} | {'aircraft ID':<13} | {'Model':<12} | {'Crew':<5} | {'Range(km)':<10} | {'CO2 Rating':<10} |"
    divider = "-" * len(header)
    print(divider)
    print(header)
    print(divider)

    idx = 1
    for plane in owned_planes:
        aircraft_ID = plane.specs["aircraft_ID"]
        model = plane.specs["model"]
        crew = plane.specs["required_crew"]
        opt_range = plane.specs["optimal_range_km"]
        co2_rating = plane.specs["environmental_impact"]["co2_rating"]

        print(f"| {idx:<3} | {aircraft_ID:<13} | {model:<12} | {crew:<5} | {opt_range:<10,} | {co2_rating:<10.1f} |")
        idx += 1

    print(divider + "\n")


def start_new_managing():
    clear_screen()
    fell_first_company_plan()

    input("\n> Press Enter to continue to Aircraft Market...")

    clear_screen()
    catalog_list = aircraft_catalog()
    show_aircraft_catalog_table_view()
    buy_aircraft(catalog_list)
    show_my_fleet()
    input("\n> Press Enter to return...")



# My data structure plan :)
'''
{
    "user_name": "abdulhadi",
    "age": 25,
    "career": [
        {
            "company_name": "Finnair Express",
            "country": "Finland",
            "hub_airport": "HEL",
            "company_budget": 500000000,
            "is_active": true,
            "fleet_count": 1,
            "years": 
            {
                "2026": 
                {
                    "planes":
                    [
                        {
                            "specs": 
                            {
                                "aircraft_ID": "001-1",
                                "manufacturer": "Airbus",
                                "model": "A320neo",
                                "required_crew": 6,
                                "optimal_range_km": 820,
                                "financials": {
                                    "price": 110600000,
                                    "annual_maintenance_cost": 900000,
                                    "daily_operating_cost": 28500,
                                    "daily_net_profit": 15000 # * 5
                                },
                                "operations_24h": {
                                    "flights_per_24h": 3
                                },
                                "environmental_impact": {
                                    "co2_emissions_per_km": 5.7,
                                    "co2_rating": 9.2
                                }
                            },
                            "stats": 
                            {
                                "total_flights": 10,
                                "successful_landings": 10,
                                "failed_landings": 1,
                                "gross_profit": 25000 # * 5,
                                "net_profit": 25000,
                                "total_co2_emissions": 570.0
                            },
                            "supported_airports": ["HEL", "OUL", "RVN", "CPH"]
                        }
                    ],
                    "total_company_co2_rating": 92 #/100
                }
            }
        }
    ]
}
'''
