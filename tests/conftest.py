import pytest
import requests
from generators import generate_user_data
from user_methods import UserMethods


@pytest.fixture
def new_user():
    user_data = generate_user_data()
    UserMethods.create_user(user_data)

    yield user_data

    login_resp = UserMethods.login_user(user_data)
    if login_resp.status_code == 200 and "accessToken" in login_resp.json():
        token = login_resp.json()["accessToken"].split(" ")[1]
        UserMethods.delete_user(token)


@pytest.fixture
def auth_user():
    user_data = generate_user_data()
    UserMethods.create_user(user_data)
    token = UserMethods.login_user(user_data).json()["accessToken"].split(" ")[1]
    user_data["access_token"] = token
    yield user_data
    UserMethods.delete_user(user_data["access_token"])  # удаляем после теста

