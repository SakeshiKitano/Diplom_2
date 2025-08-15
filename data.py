
BASE_URL = 'https://stellarburgers.nomoreparties.site/api'
ENDPOINTS = {
    "register_user": f"{BASE_URL}/auth/register",
    "login": f"{BASE_URL}/auth/login",
    "user": f"{BASE_URL}/auth/user",
    "orders": f"{BASE_URL}/orders",
    "ingredients": f"{BASE_URL}/ingredients"
}



class DataForOrder:
    CREATE_ORDER = {
    "firstName": "Test",
    "lastName": "User",
    "address": "Test street",
    "metroStation": 4,
    "phone": "+7 999 999 99 99",
    "rentTime": 2,
    "deliveryDate": "2025-06-01",
    "comment": "Test order",
    "color": []
}

class Messages:
    DUPLICATE_DATA_MESS = "User already exists"
    NOT_ENOUGH_DATA_FOR_LOG = "email or password are incorrect"
    NOT_ENOUGH_DATA_FOR_REG = "Email, password and name are required fields"