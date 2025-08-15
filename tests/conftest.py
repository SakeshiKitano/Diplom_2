import pytest
import requests
from generators import generate_user_data
from user_methods import UserMethods

from data import ENDPOINTS

# 1️⃣ Фикстура — создаёт нового пользователя (без логина)
# Используется в тестах регистрации, чтобы проверить саму регистрацию.
@pytest.fixture
def new_user():
    user_data = generate_user_data()
    UserMethods.create_user(user_data)
    return user_data


# 2️⃣ Фикстура — создаёт нового пользователя и сразу логинится
# Возвращает словарь с email, паролем и токеном.
# Используется в тестах, где нужна авторизация (например, создание заказа с авторизацией).
@pytest.fixture
def auth_user():
    user_data = generate_user_data()
    UserMethods.create_user(user_data)
    token = UserMethods.login_user(user_data).json()["accessToken"].split(" ")[1]
    user_data["access_token"] = token
    yield user_data
    UserMethods.delete_user(user_data["access_token"])  # удаляем после теста


# 3️⃣ Фикстура — логинит уже существующего пользователя
# Используется в тестах логина, когда пользователь создан заранее.
@pytest.fixture
def login_existing_user():
    def _login(user_data):
        return UserMethods.login_user(user_data)
    return _login