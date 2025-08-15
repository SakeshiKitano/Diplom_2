import allure
import pytest

from data import Messages
from user_methods import UserMethods
from order_methods import OrderMethods

class TestCreateOrder:


    @allure.epic("Создание заказа")
    @allure.title("Создание заказа с авторизацией")
    def test_create_order_with_auth(self, auth_user):
        ingredients = OrderMethods.get_ingredients().json()["data"]
        ids = [i["_id"] for i in ingredients[:2]]
        with allure.step("Отправляем запрос на создание заказа с авторизацией"):
            response = OrderMethods.create_order(token=auth_user["access_token"], ingredients=ids)
        with allure.step("Проверяем, что заказ создан успешно"):
            assert response.status_code == 200
            assert response.json()["success"] is True

    @allure.epic("Создание заказа")
    @allure.title("Создание заказа без авторизации")
    def test_create_order_without_auth(self):
        ingredients = OrderMethods.get_ingredients().json()["data"]
        ids = [i["_id"] for i in ingredients[:2]]
        with allure.step("Отправляем запрос на создание заказа без авторизации"):
            response = OrderMethods.create_order(ingredients=ids)
        with allure.step("Проверяем, что заказ всё равно создан"):
            assert response.status_code == 200
            assert response.json()["success"] is True

    @allure.epic("Создание заказа")
    @allure.title("Создание заказа без ингредиентов")
    def test_create_order_with_no_ingredients(self, auth_user):
        with allure.step("Отправляем запрос на создание заказа с пустым списком ингредиентов"):
            response = OrderMethods.create_order(token=auth_user["access_token"], ingredients=[])
        with allure.step("Проверяем, что вернулась ошибка 400 и сообщение об обязательных ингредиентах"):
            assert response.status_code == 400
            assert response.json()["message"] == "Ingredient ids must be provided"

    @allure.epic("Создание заказа")
    @allure.title("Создание заказа с неверным хешем ингредиента")
    def test_create_order_invalid_hash(self, auth_user):
        with allure.step("Отправляем запрос на создание заказа с неверным ID ингредиента"):
            response = OrderMethods.create_order(token=auth_user["access_token"], ingredients=["61c0c5a71d1f82001bdaaa6d2"])
        with allure.step("Проверяем, что вернулся статус 500 Internal Server Error"):
            assert response.status_code == 500
