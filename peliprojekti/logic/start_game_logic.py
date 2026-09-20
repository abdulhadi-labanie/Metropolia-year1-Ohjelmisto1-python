from utils import clear_screen, read_str_input, read_int_input
from aircraft_catalog import print_aircraft_catalog_table, aircraft_catalog
from storage import create_new_career, get_manager

def Select_country_headquarters():
    print("This country for the company headquarters:")
    print("1.[Finland]  2.[Swiden]  3.[Germany]  4.[Turkish]  5.[Syria].")
    is_country_selected = False
    while not is_country_selected:
        country = read_str_input("Select one of them: ").strip().capitalize()
        hub_airport = ""

        if country == "Finland" or country == "1":
            hub_airport = "HEL"
            is_country_selected = True
        elif country == "Swiden" or country == "2":
            hub_airport = "ARN"
            is_country_selected = True
        elif country == "Germany" or country == "3":
            hub_airport = "BER"
            is_country_selected = True
        elif country == "Turkish" or country == "4":
            hub_airport = "IST"
            is_country_selected = True
        elif country == "Syria" or country == "5":
            hub_airport = "DAM"
            is_country_selected = True
    return country, hub_airport


def show_start_new_managing_screen(current_manager: dict):
    print(f"\nWelcome to the airline, Manager {current_manager["user_name"]}.\n\n")
    print_aircraft_catalog_table(aircraft_catalog())


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
        updated_manager = get_manager(current_manager["user_name"])
        current_manager.clear()
        current_manager.update(updated_manager)
        print("\nCompany successfully created and saved :)")


def start_new_managing(current_manager):
    clear_screen()
    fell_first_company_plan(current_manager)

    show_start_new_managing_screen(current_manager)

    input("\n> Press Enter to continue to company creation...")



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
                                "model_quantity": 1,
                                "required_crew": 6,
                                "optimal_range_km": 820,
                                "financials_all": {
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
