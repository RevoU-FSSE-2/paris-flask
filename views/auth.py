from auth.login import get_token
from repo.user import find_user_by_email


def user_login(email, password) -> str:
    user = find_user_by_email(email)
    assert user["password"] == password, "Password is incorrect"
    token = get_token(user)
    return token
