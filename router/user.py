from flask import Blueprint, jsonify, request

from views.user import (
    create_users,
    delete_user,
    get_all_users,
    get_user,
    update_user,
)

user_router = Blueprint("user_router", __name__, url_prefix="/api/v1/users")


@user_router.route("", methods=["GET", "POST"])
def user_api():
    match request.method.lower():
        case "get":
            response = get_all_users()
            return jsonify({"data": response, "success": True}), 200
        case "post":
            return create_users(request.json)


@user_router.route("/<int:user_id>", methods=["GET", "PUT", "DELETE"])
def get_user_by_email(user_id):
    match request.method.lower():
        case "get":
            return get_user(user_id)
        case "put":
            return update_user(user_id, request.json)
        case "delete":
            return delete_user(user_id)

