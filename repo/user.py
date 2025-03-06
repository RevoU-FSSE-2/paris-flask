import copy

from models.user import dummy_db


def all_users_repository() -> dict:
    return copy.deepcopy(dummy_db)


def create_user_repository(user_data: dict):
    key_ids = list(dummy_db["users"].keys())
    if key_ids:
        new_key = max(key_ids) + 1
    else:
        new_key = 1
    dummy_db["users"][new_key] = user_data


def delete_user_repository(user_id):
    dummy_db["users"].pop(user_id)


def update_user_repository(user_id, user_data):
    dummy_db["users"][user_id] = {**dummy_db["users"][user_id], **user_data}
    return copy.deepcopy(dummy_db["users"][user_id])


def find_user_by_email(email) -> dict:
    for user_id, user_data in dummy_db["users"].items():
        if user_data["email"] == email:
            user = copy.deepcopy(user_data)
            user["id"] = user_id
            return user
    return None
