import json
from pathlib import Path
from datetime import datetime

def file_path(user_name):
    BASE_DIR = Path(__file__).resolve().parent
    managers_folder = BASE_DIR / "managers"
    managers_folder.mkdir(parents=True, exist_ok=True)
    return managers_folder / f"{user_name}.json"

def is_user_exist(user_name):
    return file_path(user_name).exists()

def get_manager(user_name) -> dict:
    if(is_user_exist(user_name)):
        with open(file_path(user_name), "r", encoding="utf-8") as file:
            return json.load(file)
    return None

def create_new_manager_file(user_name,user_age):
    manager_data = {
        "user_name": user_name,
        "age": user_age,
        "career": [],
    }
    try:
        with open(file_path(user_name), "w", encoding="utf-8") as file:
            json.dump(manager_data, file, indent=4)
        return True
    except OSError as e:
        print(f"Error when try to save file {e}")

def create_new_career(user_name, company_name, country, hub_airport, budget, fleet_count: int):
    manager_data = get_manager(user_name)
    if not manager_data:
        print(f"[!] Manager '{user_name}' not found.")
        return False

    for company in manager_data.get("career", []):
        company["is_active"] = False
        
    current_year_str = str(datetime.now().year)
    base_of_new_career = {
        "company_name": company_name,
        "country": country,
        "hub_airport": hub_airport,
        "company_budget": budget,
        "is_active": True,
        "fleet_count": fleet_count,
        "years": {
            current_year_str: {
                "planes": []
            }
        },
    }
    manager_data["career"].append(base_of_new_career)
    try:
        with open(file_path(user_name), "w", encoding="utf-8") as file:
            json.dump(manager_data, file , indent=4)
        return True
    except OSError as e:
        print(f"Error when try to save file {e}")

def storage_new_aircraft(user_name, new_budget, plane: dict):
    manager_data = get_manager(user_name)
    if not manager_data:
        print(f"[!] Manager '{user_name}' not found.")
        return False

    active_company = None
    for company in manager_data.get("career", []):
        if company.get("is_active"):
            active_company = company
            break

    if not active_company:
        print("[!] No active company found.")
        return False

    latest_year = list(active_company["years"].keys())[-1]
    new_plane = {
        "specs": plane,
        "stats": {
            "total_flights": 0,
            "failed_landings": 0,
            "total_passengers_capacity": 0,
            "net_profit": 0,
            "total_co2_emissions_tonnes": 0.0,
            "supported_airports": [active_company["hub_airport"]],
            "airline_selected": "",
            "total_plane_co2_rating": 0,
            "total_profit_rating": 0
        }
    }
    active_company["years"][latest_year]["planes"].append(new_plane)
    active_company["company_budget"] = new_budget
    active_company["fleet_count"] = len(active_company["years"][latest_year]["planes"])
    try:
        with open(file_path(user_name), "w", encoding="utf-8") as file:
            json.dump(manager_data, file , indent=4)
        return True
    except OSError as e:
        print(f"Error when try to save file {e}")

def save_manager_state_to_storage(manager_dict: dict):
    user_name = manager_dict.get("user_name")
    
    if not user_name:
        print("[!] Error: Manager dict missing 'user_name'")
        return False

    try:
        with open(file_path(user_name), "w", encoding="utf-8") as file:
            json.dump(manager_dict, file, indent=4)
        return True
    except OSError as e:
        print(f"[!] Error when try to save file {e}")
        return False
