import json
from pathlib import Path


def file_path(user_name):
    folder_path = Path("managers")
    folder_path.mkdir(parents=True, exist_ok=True)
    return Path(f"managers/{user_name}.json")


def is_user_exist(user_name):
    return file_path(user_name).exists()


def get_manager(user_name):
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
        print(f"Erro when try to save file {e}")
