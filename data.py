
BASE_URL = 'https://stellarburgers.nomoreparties.site/api'
ENDPOINTS = {
    "register_user": f"{BASE_URL}/auth/register",
    "login": f"{BASE_URL}/auth/login",
    "user": f"{BASE_URL}/auth/user",
    "orders": f"{BASE_URL}/orders",
    "ingredients": f"{BASE_URL}/ingredients"
}
login_wrong_credentials_param = [
            ("wrong@mail.com", None, "Неверный e-mail"),
            (None, "wrongpass", "Неверный пароль"),
            ("wrong@mail.com", "wrongpass", "Неверный e-mail и пароль")
        ]


class Messages:
    DUPLICATE_DATA_MESS = "User already exists"
    NOT_ENOUGH_DATA_FOR_LOG = "email or password are incorrect"
    NOT_ENOUGH_DATA_FOR_REG = "Email, password and name are required fields"
    NO_INGREDIENTS = "Ingredient ids must be provided"


