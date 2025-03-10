import pytest


@pytest.fixture
def real_data_user():
    return {
        "username": "admin",
        "password": "12345",
        "id": 1,
        "first_name": "John",
        "last_name": "Travolta",
    }


@pytest.fixture
def something():
    return "kak nurul"
