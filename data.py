# Тестируемый сайт
class URLS:
    BASE_URL = "https://qa-stellarburgers.education-services.ru"


class UserEndpoints:
    REGISTER = "/api/auth/register"    # POST  создание пользователя
    LOGIN = "/api/auth/login"          # POST  логин
    USER = "/api/auth/user"            # PATCH изменение / GET получение / DELETE удаление


class OrderEndpoints:
    ORDERS = "/api/orders"             # POST создание заказа / GET заказы пользователя
    INGREDIENTS = "/api/ingredients"   # GET  получение ингредиентов

class ErrorMessages:
    USER_ALREADY_EXISTS = "User already exists"
    MISSING_REQUIRED_FIELDS = "Email, password and name are required fields"
    WRONG_EMAIL_OR_PASSWORD = "email or password are incorrect"
    NOT_AUTHORISED = "You should be authorised"
    INGREDIENT_IDS_REQUIRED = "Ingredient ids must be provided"
