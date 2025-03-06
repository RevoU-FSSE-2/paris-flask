from flask import jsonify

from repo.user import (
    all_users_repository,
    create_user_repository,
    delete_user_repository,
    update_user_repository,
)


def serialize_user(user_data: dict):
    user_data.pop("password")
    user_data.pop("first_name")
    user_data.pop("last_name")
    return user_data


def create_users(data_masuk: dict):
    email = data_masuk.get("email")
    password = data_masuk.get("password")
    first_name = data_masuk.get("first_name")
    last_name = data_masuk.get("last_name")
    full_name = f"{first_name} {last_name}"
    if not email:
        return jsonify(
            {"data": {"message": "Email is required"}, "success": False}
        ), 400
    if not password:
        return jsonify(
            {"data": {"message": "Password is required"}, "success": False}
        ), 400
    if not first_name:
        return jsonify(
            {"data": {"message": "First name is required"}, "success": False}
        ), 400
    if not last_name:
        return jsonify(
            {"data": {"message": "Last name is required"}, "success": False}
        ), 400
    data_masuk["full_name"] = full_name
    create_user_repository(data_masuk)
    return jsonify(
        {"data": {"message": f"{email} is registered"}, "success": True}
    ), 201


def get_all_users():
    users = all_users_repository()["users"]
    formated_responses = []
    for email, user_data in users.items():
        formated_responses.append(serialize_user(user_data))
    return formated_responses


def find_user_by_id(_id: int):
    users = all_users_repository()["users"]
    if user_data := users.get(_id):
        return serialize_user(user_data)
    return None


def delete_user(user_id):
    user = find_user_by_id(user_id)
    if not user:
        return jsonify({"data": {"message": "User not found"}, "success": False}), 404
    delete_user_repository(user_id)
    return jsonify({}), 204


def get_user(user_id):
    user = find_user_by_id(user_id)
    if not user:
        return jsonify({"data": {"message": "User not found"}, "success": False}), 404

    return jsonify({"data": user, "success": True}), 200


def update_user(user_id, data_masuk):
    user = find_user_by_id(user_id)
    if not user:
        return jsonify({"data": {"message": "User not found"}, "success": False}), 404
    user_data = update_user_repository(user_id, data_masuk)
    return jsonify({"data": serialize_user(user_data), "success": True}), 200
