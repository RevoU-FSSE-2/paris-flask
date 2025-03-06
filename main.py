import uuid

from flask import Flask, jsonify, render_template, request

from auth.login import claim_user, login_required
from models.user import dummy_db
from router.auth import auth_router
from router.user import user_router

app = Flask(__name__)
app.register_blueprint(user_router)
app.register_blueprint(auth_router)


@app.before_request
def before_request():
    print("MIDDLEWARE BEFORE REQUEST")
    authrorization_token = request.headers.get("Authorization")
    if authrorization_token:
        user = claim_user(authrorization_token)
        request.user = user


@app.after_request
def after_request(response):
    # give  request id response header
    request_id = str(uuid.uuid4())
    response.headers["X-Request-ID"] = request_id

    return response


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@app.route("/account", methods=["GET"])
@login_required
def account():
    return jsonify({"data": {"you": request.user}, "success": True}), 200


@app.route("/")
def index():
    return render_template("index.html", users=dummy_db["users"])
