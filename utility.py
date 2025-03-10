def kalkulasi_luas(panjang, lebar):
    return panjang * lebar

def remove_password(user: dict):
    user_copy = user.copy()
    del user_copy["password"]
    return user_copy

def create_full_name(user: dict):
    user_copy = user.copy()
    user_copy["full_name"] = f"{user_copy['first_name']} {user_copy['last_name']}"
    return user_copy
