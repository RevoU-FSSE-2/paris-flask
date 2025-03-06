from flask import Blueprint, request

from views.auth import user_login

auth_router = Blueprint("auth_router", __name__, url_prefix="/api/v1/auth")


@auth_router.route("/login", methods=["POST"])
def login():
    email = request.json.get("email")
    password = request.json.get("password")
    try:
        token = user_login(email, password)
    except AssertionError as e:
        return {"message": str(e), "success": False}, 401
    return {"data": {"token": token}, "success": True}, 200
