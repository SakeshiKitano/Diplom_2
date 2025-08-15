import allure
import pytest
from user_methods import UserMethods

class TestLoginUser:

    @allure.epic("Авторизация пользователя")
    @allure.title("Успешный вход под существующим пользователем")
    def test_login_existing_user(self, new_user):
        with allure.step("Отправляем запрос на авторизацию с корректными данными"):
            response = UserMethods.login_user(new_user)
        with allure.step("Проверяем, что авторизация успешна"):
            assert response.status_code == 200
            assert "accessToken" in response.json()



    @allure.epic("Авторизация пользователя")
    @allure.title("Вход с неверными данными")
    @pytest.mark.parametrize(
        "email_mod,password_mod,case_name",
        [
            ("wrong@mail.com", None, "Неверный e-mail"),
            (None, "wrongpass", "Неверный пароль"),
            ("wrong@mail.com", "wrongpass", "Неверный e-mail и пароль")
        ]
    )
    def test_login_wrong_credentials_param(self, new_user,  case_name, email_mod, password_mod):
        """Проверка авторизации с различными неправильными комбинациями логина и пароля"""

        # Берём правильные данные пользователя, созданного фикстурой
        email = email_mod if email_mod else new_user["email"]
        password = password_mod if password_mod else new_user["password"]

        wrong_data = {
            "email": email,
            "password": password
        }

        with allure.step(f"Отправляем запрос на авторизацию: {case_name}"):
            response = UserMethods.login_user(wrong_data)

        with allure.step("Проверяем, что вернулась ошибка 401 и сообщение о неверных данных"):
            assert response.status_code == 401
            assert response.json()["message"] == "email or password are incorrect"