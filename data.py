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
