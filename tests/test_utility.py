import pytest

from utility import create_full_name, kalkulasi_luas, remove_password


@pytest.mark.parametrize(
    "panjang, lebar, expected",
    [
        (5, 4, 20),
        (10, 2, 20),
        (3, 3, 9),
        (3, 4, 12),
    ],
)
def test_kalkulasi_luas(panjang, lebar, expected):
    print(f"Panjang: {panjang}, Lebar: {lebar}, Expected: {expected}")
    assert kalkulasi_luas(panjang, lebar) == expected


def test_kalkulasi_luas_berulang_ulang():
    assert kalkulasi_luas(5, 4) == 20
    assert kalkulasi_luas(10, 2) == 20
    assert kalkulasi_luas(3, 3) == 9
    assert kalkulasi_luas(3, 4) == 12


def test_remove_password(real_data_user):
    assert remove_password(real_data_user) == {
        "username": "admin",
        "id": 1,
        "first_name": "John",
        "last_name": "Travolta",
    }
    assert real_data_user == {
        "username": "admin",
        "password": "12345",
        "id": 1,
        "first_name": "John",
        "last_name": "Travolta",
    }


def test_create_full_name(real_data_user):
    create_full_name(real_data_user) == {
        "username": "admin",
        "password": "12345",
        "id": 1,
        "first_name": "John",
        "last_name": "Travolta",
        "full_name": "John Travolta",
    }


def test_something(something):
    print(something)
