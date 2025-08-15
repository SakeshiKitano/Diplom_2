import requests
import allure

from data import ENDPOINTS

class UserMethods:


    @staticmethod
    def create_user(body):
        return requests.post(ENDPOINTS['CREATE_USER_URL'], json=body)


