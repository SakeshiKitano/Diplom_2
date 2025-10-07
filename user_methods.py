import requests

from data import ENDPOINTS

class UserMethods:

    @staticmethod
    def create_user(user_data):
        return requests.post(ENDPOINTS["register_user"], json=user_data)

    @staticmethod
    def login_user(user_data):
        return requests.post(ENDPOINTS["login"], json=user_data)

    @staticmethod
    def delete_user(token):
        headers = {"Authorization": f"Bearer {token}"}
        return requests.delete(ENDPOINTS["user"], headers=headers)

