from utils import clear_screen, read_str_input, read_bool_input
from aircraft_catalog import print_aircraft_catalog_table, aircraft_catalog
from storage import create_new_career, get_manager, storage_new_aircraft


def get_active_company(current_manager):
    for company in current_manager.get("career", []):
        if company.get("is_active"):
            return company
    return None


def update_success_data(current_manager_data):
    updated_manager = get_manager(current_manager_data["user_name"])
    current_manager_data.clear()
    current_manager_data.update(updated_manager)
    print("\n[ok] Data successfully saved and synchronized!")


def Select_country_headquarters():
    print("This country for the company headquarters:")
    print("1.[Finland]  2.[Swiden]  3.[Germany]  4.[Turkish]  5.[Syria].")
    is_country_selected = False
    while not is_country_selected:
        country = read_str_input("Select one of them: ").strip().capitalize()
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


def fell_first_company_plan(current_manager):
    print("Interface for appointing a new airline manager:")
    company_name = read_str_input("Enter your company name: ")
    country, hub_airport = Select_country_headquarters()
    company_budget = 500000000
    print(f"Your company budget is : {company_budget:,}€")
    fleet_count = 0

    success = create_new_career(current_manager["user_name"], company_name, country, 
                                hub_airport, company_budget, fleet_count)

    if success:
        update_success_data(current_manager)


def show_aircraft_catalog_table(current_manager: dict):
    active_company = get_active_company(current_manager)
    print(f"\nWelcome to the airline, Manager {current_manager['user_name']}.\n\n")
    print_aircraft_catalog_table(aircraft_catalog())


def by_aircraft(current_manager, catalog_list):
    is_want_by_aircraft = True

    while is_want_by_aircraft:
        active_company = get_active_company(current_manager)
        if not active_company:
            print("\n[!] Error: No active company found!")
            break

        current_budget = active_company["company_budget"]
        print(f"\nYour company budget = {current_budget:,} €")
        user_selection = read_str_input("\nSelect an aircraft by [model name] (e.g., A380-800 or A318): ").strip().upper()

        selected_plane = None
        for aircraft in catalog_list:
            if aircraft["model"].upper() == user_selection:
                selected_plane = aircraft
                break

        if selected_plane:
            plane_price = selected_plane["financials"]["price"]
            if current_budget >= plane_price:
                new_budget = current_budget - plane_price
                success = storage_new_aircraft(current_manager["user_name"], new_budget, selected_plane)

                if success:
                    update_success_data(current_manager)
                    print(f"\n[ok] Successfully purchased {selected_plane['manufacturer']} {selected_plane['model']}!")
            else:
                print(f"\n[!] Budget insufficient! Price: {plane_price:,} €, Your Budget: {current_budget:,} €")
        else:
            print(f"\n[!] Aircraft model '{user_selection}' not found in catalog!")

        is_want_by_aircraft = read_bool_input("\nDo you want to buy another aircraft? [y/n]: ")


def show_my_fleet(current_manager: dict):
    active_company = get_active_company(current_manager)

    if not active_company or not active_company.get("years"):
        print("\n[!] No active company or fleet data found.")
        return

    latest_year = list(active_company["years"].keys())[-1]
    owned_planes = active_company["years"][latest_year]["planes"]

    print(f"\n\t===== {active_company['company_name']} - MY FLEET =====\n")

    if not owned_planes:
        print("Your fleet is currently empty! Buy aircraft from the market.")
        return

    header = f"| {'#':<3} | {'Model':<12} | {'Crew':<5} | {'Range(km)':<10} | {'CO2 Rating':<10} |"
    divider = "-" * len(header)
    print(divider)
    print(header)
    print(divider)

    idx = 1
    for plane in owned_planes:
        model = plane["specs"]["model"]
        crew = plane["specs"]["required_crew"]
        opt_range = plane["specs"]["optimal_range_km"]
        co2_rating = plane["specs"]["environmental_impact"]["co2_rating"]

        print(f"| {idx:<3} | {model:<12} | {crew:<5} | {opt_range:<10,} | {co2_rating:<10.1f} |")
        idx += 1

    print(divider + "\n")


def start_new_managing(current_manager):
    clear_screen()
    fell_first_company_plan(current_manager)

    input("\n> Press Enter to continue to Aircraft Market...")

    clear_screen()
    catalog_list = aircraft_catalog()
    show_aircraft_catalog_table(current_manager)
    by_aircraft(current_manager, catalog_list)
    show_my_fleet(current_manager)
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
