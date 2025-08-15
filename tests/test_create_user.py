from user_methods import UserMethods
from generators import generate_user_data

import allure
import pytest




class TestCreateUser:

    @allure.title("Создание уникального пользователя")
    def test_create_unique_user(self):
        user_data = generate_user_data()
        with allure.step("Отправляем запрос на регистрацию нового пользователя"):
            response = UserMethods.create_user(user_data)
        with allure.step("Проверяем статус-код и успех операции"):
            assert response.status_code == 200
            assert response.json()["success"] is True