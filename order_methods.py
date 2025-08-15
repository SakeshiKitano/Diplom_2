import requests
import allure

from data import ENDPOINTS

class OrderMethods:
    @staticmethod
    def create_order(token=None, ingredients=None):
        headers = {}
        if token:
            headers["Authorization"] = f"Bearer {token}"
        return requests.post(ENDPOINTS["orders"], json={"ingredients": ingredients}, headers=headers)

    @staticmethod
    def get_ingredients():
        return requests.get(ENDPOINTS["ingredients"])

