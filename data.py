
BASE_URL = 'https://stellarburgers.nomoreparties.site'
ENDPOINTS = {
        'CREATE_USER_URL': '/api/auth/register',
        'LOGIN_USER_URL': '/api/auth/login',
        'CREATE_ORDER_URL': '/api/orders',
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
    DUPLICATE_LOGIN_MESS ="Этот логин уже используется. Попробуйте другой."
    NOT_ENOUGH_DATA = "Недостаточно данных для создания учетной записи"
    NOT_ENOUGH_DATA_FOR_LOGIN = "Недостаточно данных для входа"