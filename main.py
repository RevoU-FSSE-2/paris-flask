from flask import Flask, request, render_template, jsonify
import copy

app = Flask(__name__)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


# dummy_db = {
#     "users": {
#         "babebo@gmail.com": {
#             "password": "123456",
#             "first_name": "Babe",
#             "last_name": "Bo",
#             "full_name": "Babe Bo",
#             "email": "babebo@gmail.com",
#         }
#     }
# }
dummy_db = {
    "users": {
        "babebo@gmail.com": {
            "password": "EkoCmiwSimilikity",
            "first_name": "babe",
            "last_name": "bo",
            "full_name": "babe bo",
            "email": "babebo@gmail.com",
        },
        "eko@gmail.com": {
            "password": "babekiewkiew",
            "first_name": "eko",
            "last_name": "aja",
            "full_name": "eko aja",
            "email": "eko@gmail.com",
        },
    }
}


def all_users_repository() -> dict:
    return copy.deepcopy(dummy_db)


def create_user_repository(email: str, user_data: dict):
    dummy_db["users"][email] = user_data


def get_all_users():
    users = all_users_repository()["users"]
    formated_responses = []
    for email, user_data in users.items():
        user_data.pop("password")
        user_data.pop("first_name")
        user_data.pop("last_name")
        formated_responses.append(user_data)
    return formated_responses


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
    create_user_repository(data_masuk.get("email"), data_masuk)
    return jsonify(
        {"data": {"message": f"{email} is registered"}, "success": True}
    ), 201


@app.route("/")
def index():
    return render_template("index.html", users=dummy_db["users"])


@app.route("/account")
def account_api():
    # logika
    try:
        # authorisasi ke vendor
        raise Exception("Vendor not found")
        # dari vendor mendapatkan token api
    except Exception as e:
        return jsonify({"data": {"message": "vendor error"}, "success": False}), 400

    return jsonify({"data": {"apiKey": "alshd831uy374bgsd"}, "success": True}), 200


@app.route("/users", methods=["GET", "POST", "PUT", "DELETE"])
def user_api():
    print("=" * 10, "METHOD ->", request.method, "=" * 10)
    match request.method.lower():
        case "get":
            response = get_all_users()
            return jsonify({"data": response, "success": True}), 200
        case "post":
            return create_users(request.json)
        case "put":
            pass
        case "delete":
            pass
