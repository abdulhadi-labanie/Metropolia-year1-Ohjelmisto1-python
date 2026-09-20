import json
from pathlib import Path


def file_path(user_name):
    folder_path = Path("managers")
    folder_path.mkdir(parents=True, exist_ok=True)
    return Path(f"managers/{user_name}.json")


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


    base_of_new_career = {
        "company_name": company_name,
        "country": country,
        "hub_airport": hub_airport,
        "company_budget": budget,
        "is_active": True,
        "fleet_count": fleet_count,
        "years": {
            "2026": {
                "planes": [],
                "total_company_co2_rating": 0,
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
