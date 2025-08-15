from user_methods import UserMethods
from generators import generate_user_data
from data import Messages

import allure
import pytest

class TestCreateUser:

    @allure.epic("Регистрация пользователя")
    @allure.title("Создание уникального пользователя")
    def test_create_unique_user(self):
        user_data = generate_user_data()
        with allure.step("Отправляем запрос на регистрацию нового пользователя"):
            response = UserMethods.create_user(user_data)
        with allure.step("Проверяем статус-код и успех операции"):
            assert response.status_code == 200
            assert response.json()["success"] is True
        with allure.step("Удаляем созданного пользователя"):
            token = UserMethods.login_user(user_data).json()["accessToken"].split(" ")[1]
            UserMethods.delete_user(token)

    @allure.epic("Регистрация пользователя")
    @allure.title("Создание пользователя, который уже зарегистрирован")
    def test_create_existing_user(self, new_user):
        with allure.step("Отправляем повторный запрос на регистрацию с теми же данными"):
            response = UserMethods.create_user(new_user)
        with allure.step("Проверяем, что вернулась ошибка 403 и сообщение о существующем пользователе"):
            assert response.status_code == 403
            assert response.json()["message"] == Messages.DUPLICATE_DATA_MESS


    @allure.epic("Регистрация пользователя")
    @allure.title("Создание пользователя без обязательного поля")
    @pytest.mark.parametrize("missing_field", ["email", "password", "name"])
    def test_create_user_missing_field(self, missing_field):
        user_data = generate_user_data()
        user_data[missing_field] = ""
        with allure.step(f"Отправляем запрос с пропущенным обязательным полем {missing_field}"):
            response = UserMethods.create_user(user_data)
        with allure.step("Проверяем, что вернулась ошибка 403 и сообщение о недостающих полях"):
            assert response.status_code == 403
            assert response.json()["message"] == Messages.NOT_ENOUGH_DATA_FOR_REG