from utils import clear_screen, read_str_input, read_bool_input
from data_catalogs.aircraft_catalog import aircraft_catalog
from storage import get_manager, storage_new_aircraft, save_manager_state_to_storage
from models.clsSessionManager import clsSessionManager
from models.clsManager import clsManager
from models.clsPlane import clsPlane
from data_catalogs.hub_destination_catalog import HUB_DESTINATIONS_CATALOG
import random
import copy
import sys


def update_success_data(user_name):
    updated_dict = get_manager(user_name)
    new_manager_obj = clsManager.from_dict(updated_dict)
    clsSessionManager.set_active_manager(new_manager_obj)
    print("\n[ok] Data successfully saved and synchronized!")

def is_active_company():
    manager = clsSessionManager.get_active_manager()
    active_company = manager.get_active_company()
    if active_company:
        return True
    else:
        return False

def show_instructions_how_build_plan():
    print("\n=== Game Concept & Planning Guide ===")
    print("1. Goal: You are an airline manager aiming to maximize profits while minimizing CO2 emissions.")
    print("2. Yearly Plan: You will now assign a destination (airport) for each aircraft in your fleet for the coming year.")
    print("3. Tip: Choose destinations that match your plane's optimal range to avoid penalties and reduce risks.")
    print("4. Result: The system will automatically calculate passengers, flights, net profit, and your final ratings.")
    print("=====================================\n")

def print_aircraft_catalog_table(aircraft_catalog: list):
    header = (f"| {'aircraft ID':<12} | {'Manufacturer':<12} | {'Model':<12} | {'Crew':<5} | {'Number of passengers':<20} | {'Range(km)':<10} "
        f"| {'Price (€)':<14} | {'CO2/km':<8} | {'CO2 Rating':<10} |")
    divider = "-" * len(header)
    print("\n" + divider)
    print(header)
    print(divider)

    for aircraft in aircraft_catalog:
        aircraft_ID = aircraft["aircraft_ID"]
        mfr = aircraft["manufacturer"]
        model = aircraft["model"]
        crew = aircraft["required_crew"]
        passengers_capacity = aircraft["passengers_capacity"]
        opt_range = aircraft["optimal_range_km"]
        price = aircraft["financials"]["price"]
        co2_km = aircraft["environmental_impact"]["co2_emissions_per_km"]
        co2_rating = aircraft["environmental_impact"]["co2_rating"]

        print(f"| {aircraft_ID:<12} | {mfr:<12} | {model:<12} | {crew:<5} | {passengers_capacity:<20} | {opt_range:<10,} "
            f"| {price:<14,} | {co2_km:<8.1f} | {co2_rating:<10.1f} |")
    print(divider + "\n")

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
                selected_plane = copy.deepcopy(aircraft)
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


def get_company_fleet():
    manager = clsSessionManager.get_active_manager()
    active_company = manager.get_active_company()

    if not active_company or not active_company.years:
        print("\n[!] No active company or fleet data found.")
        return
    latest_year_label = list(active_company.years.keys())[-1]
    latest_year_obj = active_company.years[latest_year_label]
    owned_planes = latest_year_obj.planes
    return owned_planes

def show_my_fleet():
    manager = clsSessionManager.get_active_manager()
    active_company = manager.get_active_company()
    owned_planes = get_company_fleet()

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
        aircraft_ID = plane.aircraft_ID
        model = plane.model
        crew = plane.required_crew
        opt_range = plane.optimal_range_km
        co2_rating = plane.co2_rating

        print(f"| {idx:<3} | {aircraft_ID:<13} | {model:<12} | {crew:<5} | {opt_range:<10,} | {co2_rating:<10.1f} |")
        idx += 1
    print(divider + "\n")

def get_main_hub_supported_airports_CATALOG(Main_hub: str) -> dict:
    HUBs_List = HUB_DESTINATIONS_CATALOG()
    for main_hub_country in HUBs_List:
        if main_hub_country["hub_code"] == Main_hub:
            return main_hub_country
    return {}

def print_HUB_DESTINATIONS_CATALOG(Main_hub, plane: clsPlane = None):
    main_hub_airports_supports = get_main_hub_supported_airports_CATALOG(Main_hub)
    hub_name = main_hub_airports_supports['hub_airport_name']
    hub_code = main_hub_airports_supports['hub_code']

    print(f"\nWelcome to main hub [{hub_name}, {hub_code}] supported airports page!\n")
    destinations = main_hub_airports_supports.get("destinations", {})
    Index = 1
    supported_codes = get_supported_airports_of_plane(plane) if plane else []

    for category, airports in destinations.items():
        valid_airports = [a for a in airports if not plane or a.get("code") in supported_codes]
        
        if not valid_airports:
            continue
        print(f"\n=== CATEGORY: {category.upper()} (Within Range) ===")
        header = f"| {'Index':<5} | {'Country':<20} | {'City':<15} | {'Code':<4} | {f'Distance from {hub_code}':<14} |"
        divider = "-" * len(header)

        print(divider)
        print(header)
        print(divider)

        for airport in valid_airports:
            Country = airport["country"]
            City = airport["city"]
            Code = airport["code"]
            Distance_km = airport["distance_km"]
            print(f"| {Index:<5} | {Country:<20} | {City:<15} | {Code:<4} | {Distance_km:14,} km |")
            Index += 1
        print(divider + "\n")

def get_supported_airports_of_plane(plane: clsPlane):
    manager = clsSessionManager.get_active_manager()
    active_company = manager.get_active_company()

    all_airports_mian_hub_destinations = get_main_hub_supported_airports_CATALOG(active_company.hub_airport)
    airports_mian_hub_supported = []
    airports_code_list = []
    destinations = all_airports_mian_hub_destinations.get("destinations", {})
    for category, airports in destinations.items():
        for airport in airports:
            distance_km = airport.get("distance_km", 0)
            if distance_km <= plane.optimal_range_km:
                airports_mian_hub_supported.append(airport)
                airports_code_list.append(airport.get("code", ""))
    return airports_code_list

def get_airportsData_from_airportCode(airportCode: str) -> dict:
    catalog = HUB_DESTINATIONS_CATALOG()
    for hub in catalog:
        destinations = hub.get("destinations", {})
        for category, airports in destinations.items():
            for airport in airports:
                if airport.get("code") == airportCode:
                    return airport
    return {}

def select_airline_with_airportCode_and_return(plane: clsPlane):
    airports_code_list = get_supported_airports_of_plane(plane)
    while True:
        user_select_airline = read_str_input(f"> Select an airline destination for plane [{plane.model}] with airport code like (HEL): ").strip().upper()
        
        if user_select_airline in airports_code_list:
            plane.airline_selected = user_select_airline
            break
        else:
            print(f"\n[!] Airport code '{user_select_airline}' is not supported or out of plane's range. Try again.")  
    return plane.airline_selected

def calculate_total_flights_in_year(flight_distance_km: float, AVERAGE_SPEED_KMH, GROUND_TURNAROUND_HOURS, DAILY_FLYING_LIMIT_HOURS) -> int:
    flight_duration_hours = (flight_distance_km / AVERAGE_SPEED_KMH) + GROUND_TURNAROUND_HOURS
    daily_flights = DAILY_FLYING_LIMIT_HOURS / flight_duration_hours
    return round(daily_flights * 365)

def calculate_failed_landings_in_year(annual_flights: int,co2_rating: float,weather_severity: float = 1.0,runway_condition: float = 1.0) -> int:
    aircraft_risk = 1.5 - (co2_rating / 10.0)
    environment_risk = weather_severity * runway_condition
    failed_landing_per_flight = 0.005 * aircraft_risk * environment_risk
    
    return round(annual_flights * failed_landing_per_flight)

def calculate_single_flight_passengers(passengers_capacity: int, optimal_range_km: float, airport_data: dict) -> int:
    distance_km = airport_data.get("distance_km", 0)
    runway_condition = airport_data.get("runway_condition", 1.0)
    
    load_factor = 0.98
    
    if runway_condition > 1.2:
        runway_penalty_rate = random.uniform(0.05, 0.15)
        load_factor -= (runway_condition - 1.0) * runway_penalty_rate
        
    if optimal_range_km > 0:
        mismatch_ratio = distance_km / optimal_range_km
    else:
        mismatch_ratio = 1.0

    if mismatch_ratio < 0.4:
        if passengers_capacity > 150:
            mismatch_penalty_rate = random.uniform(0.05, 0.15)
            load_factor -= mismatch_penalty_rate
            
    expected_passengers = passengers_capacity * load_factor
    return round(expected_passengers)

def calculate_annual_net_profit(total_passengers_capacity: int, plane: clsPlane) -> float:
    annual_operating_cost = plane.daily_operating_cost * 365.0
    total_net_profit = (plane.ticket_price * total_passengers_capacity) - (plane.annual_maintenance_cost + annual_operating_cost)
    return round(total_net_profit / 65)

def calculate_annual_co2_icao(annual_flights: int, flight_distance_km: float, co2_emissions_per_km: float) -> float:
    cruise_fuel_per_km = co2_emissions_per_km / 3.16
    lto_fuel_kg = cruise_fuel_per_km * 250.0
    total_fuel_kg = lto_fuel_kg + (flight_distance_km * cruise_fuel_per_km)
    co2_per_flight_tons = (total_fuel_kg * 3.16) / 1000.0
    
    return round(co2_per_flight_tons * annual_flights, 2)

def calculate_company_co2_rating(base_co2_rating: float, flight_distance_km: float, optimal_range_km: float) -> float:
    if flight_distance_km > optimal_range_km:
        distance_difference = flight_distance_km - optimal_range_km
    else:
        distance_difference = optimal_range_km - flight_distance_km

    range_deviation = (distance_difference + 1000) / optimal_range_km
    range_efficiency = 1.0 - range_deviation
    if range_efficiency < 0.0:
        range_efficiency = 0.0

    final_rating = (base_co2_rating / 10.0) * range_efficiency * 100.0

    if final_rating > 100.0:
        final_rating = 100.0
    elif final_rating < 0.0:
        final_rating = 0.0
    return round(final_rating, 1)

def calculate_expected_flight_passengers(total_year_flights: int, passengers_capacity: int, optimal_range_km: float, airport_data: dict) -> int:
    total_passengers_capacity = 0
    for i in range(total_year_flights):
        total_passengers_capacity += calculate_single_flight_passengers(passengers_capacity, optimal_range_km, airport_data)
    return total_passengers_capacity

def calculate_company_profit_rating(plane: clsPlane, annual_net_profit: float, total_passengers_capacity: int, total_year_flights: int) -> float:
    max_annual_passengers = plane.passengers_capacity * total_year_flights
    max_annual_revenue = max_annual_passengers * plane.ticket_price
    
    total_annual_costs = plane.annual_maintenance_cost + (plane.daily_operating_cost * 365.0)
    max_annual_profit = (max_annual_revenue - total_annual_costs) / 65.0
    
    if max_annual_profit <= 0.0:
        return 0.0
        
    profit_ratio = (annual_net_profit / max_annual_profit) * 100.0
    
    if profit_ratio > 100.0:
        profit_ratio = 100.0
    elif profit_ratio < 0.0:
        profit_ratio = 0.0
        
    return round(profit_ratio, 1)


def Main_Definig_plan_for_each_aircraft_coming_year(plane: clsPlane, user_selected_airline, airport_data_dict):
    AVERAGE_SPEED_KMH = 800.0
    GROUND_TURNAROUND_HOURS = 1.5
    DAILY_FLYING_LIMIT_HOURS = 18.0

    total_year_flights = calculate_total_flights_in_year(airport_data_dict["distance_km"], AVERAGE_SPEED_KMH,GROUND_TURNAROUND_HOURS, DAILY_FLYING_LIMIT_HOURS)
    failed_landings = calculate_failed_landings_in_year(total_year_flights, plane.co2_rating, airport_data_dict["weather_severity"], airport_data_dict["runway_condition"])
    total_passengers_capacity = calculate_expected_flight_passengers(total_year_flights, plane.passengers_capacity, plane.optimal_range_km, airport_data_dict)
    net_profit = calculate_annual_net_profit(total_passengers_capacity, plane)
    total_co2_emissions_tonnes = calculate_annual_co2_icao(total_year_flights, airport_data_dict["distance_km"], plane.co2_emissions_per_km)
    supported_airports = get_supported_airports_of_plane(plane)
    airline_selected = user_selected_airline
    total_plane_co2_rating = calculate_company_co2_rating(plane.co2_rating, airport_data_dict["distance_km"], plane.optimal_range_km)
    total_profit_rating = calculate_company_profit_rating(plane, net_profit, total_passengers_capacity, total_year_flights)

    plane.total_flights = total_year_flights
    plane.failed_landings = failed_landings
    plane.total_passengers_capacity = total_passengers_capacity
    plane.net_profit = net_profit
    plane.total_co2_emissions_tonnes = total_co2_emissions_tonnes
    plane.supported_airports = supported_airports
    plane.airline_selected = airline_selected 
    plane.total_plane_co2_rating = total_plane_co2_rating
    plane.total_profit_rating = total_profit_rating

def show_plans_result():
    clear_screen()
    manager = clsSessionManager.get_active_manager()
    active_company = manager.get_active_company()
    company_fleet = get_company_fleet()
    if not company_fleet:
        print("\n[!] No fleet data available to show results.")
        return
    print(f"\n{'='*25} ANNUAL PLAN RESULTS FOR: {active_company.company_name.upper()} {'='*25}\n")

    total_company_profit = 0
    total_company_co2 = 0
    
    header = (f"| {'Aircraft ID':<13} | {'Model':<12} | {'Dest':<5} | {'Flights':<7} | "
        f"{'Passeng.':<9} | {'Failed':<6} | {'Net Profit (€)':<15} | {'CO2 (T)':<8} | {'CO2 Rtg':<7} | {'Prf Rtg':<7} |")
    divider = "-" * len(header)
    print(divider)
    print(header)
    print(divider)

    for plane in company_fleet:
        a_id = plane.aircraft_ID
        model = plane.model
        dest = plane.airline_selected
        flights = plane.total_flights
        passengers = plane.total_passengers_capacity
        failed = plane.failed_landings
        profit = plane.net_profit
        co2 = plane.total_co2_emissions_tonnes
        co2_rtg = plane.total_plane_co2_rating
        prf_rtg = plane.total_profit_rating
        total_company_profit += profit
        total_company_co2 += co2

        print(f"| {a_id:<13} | {model:<12} | {dest:<5} | {flights:<7,} | "
            f"{passengers:<9,} | {failed:<6} | {profit:<15,} | {co2:<8.1f} | {co2_rtg:<7.1f} | {prf_rtg:<7.1f} |")

    print(divider)
    print("\n" + "="*15 + " COMPANY SUMMARY " + "="*15)
    print(f"Total Expected Annual Profit : {total_company_profit:,} €")
    print(f"Total Expected CO2 Emissions : {total_company_co2:,.1f} Tonnes")
    print("="*47 + "\n")

def Want_play_switcher():
    manager = clsSessionManager.get_active_manager()
    print(f"\n***** Active Manager: {manager.user_name} *****\n")
    print("1. Play more")
    print("2. Return to Main Menu")
    print("3. Quit (lopeta)\n")
    while True:
        user_choice = read_str_input("Enter your choice (1-3 or 'lopeta'): ").strip().lower()
        if user_choice == "1":
            cntinue_game_with_active_company(came_from_start_new_managing=True)
            return True
        elif user_choice == "2":
            return True
        elif user_choice == "3" or user_choice == "lopeta":
            clear_screen()
            print("\nQuitting the game... Goodbye!")
            sys.exit() 
        else:
            print("\n[!] Invalid choice! Please enter 1, 2, 3 or 'lopeta'.")

def cntinue_game_with_active_company(came_from_start_new_managing: bool = False):
    manager = clsSessionManager.get_active_manager()
    active_company = manager.get_active_company()

    clear_screen()
    if not is_active_company():
        print("\n[!] You do not have an active company yet. Please Star new career first!!!")
        input("> Press any key to return Start Game Menu")
        return 
    show_instructions_how_build_plan()
    input("\n\n> Press any key to continue game: ")
    clear_screen()

    if not came_from_start_new_managing:
        if read_bool_input("Do you want to buy an aircraft (yes/no): "):
            show_my_fleet()
            show_aircraft_catalog_table_view()
            buy_aircraft(aircraft_catalog())
            input("> Press any key to start make company plan ")
    clear_screen()
    show_my_fleet()
    company_fleet = get_company_fleet()

    if company_fleet:
        total_fleet_profit = 0

        for plane in company_fleet:
            clear_screen()
            print_HUB_DESTINATIONS_CATALOG(active_company.hub_airport, plane)
            user_selected_airline = select_airline_with_airportCode_and_return(plane)
            airport_data_dict = get_airportsData_from_airportCode(user_selected_airline)

            Main_Definig_plan_for_each_aircraft_coming_year(plane, user_selected_airline, airport_data_dict)
            total_fleet_profit += plane.net_profit
        active_company.company_budget += total_fleet_profit
        save_manager_state_to_storage(manager.to_dict()) 
        print("\n[ok] Yearly plan successfully saved to database!")
    input("\n> Press any key to show plans result!")
    show_plans_result()
    Want_play_switcher()
