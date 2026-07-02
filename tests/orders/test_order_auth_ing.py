import allure
from data import ErrorMessages


@allure.suite('Создание заказа')
class TestCreateOrder:

    @allure.title('Создание заказа с авторизацией и ингредиентами')
    def test_order_create_with_auth_and_ingredients(
            self, order_methods, registered_user, ingredients):
        token = registered_user["token"]
        body, status_code = order_methods.create_order(
            ingredients, token=token)
        assert (status_code == 200 and body.get(
            "success") is True and "order" in body)

    @allure.title('Создание заказа без авторизации и с ингредиентами')
    def test_order_create_without_auth_and_with_ingredients(
            self, order_methods, ingredients):
        body, status_code = order_methods.create_order(ingredients)
        assert status_code == 200 and body.get("success") is True

    @allure.title('Создание заказа с авторизацией и без ингредиентов')
    def test_order_create_with_auth_without_ingredients(
            self, order_methods, registered_user):
        token = registered_user["token"]
        body, status_code = order_methods.create_order([], token=token)
        assert (status_code == 400 and body.get("success") is False and body.get(
            "message") == ErrorMessages.INGREDIENT_IDS_REQUIRED)

    @allure.title('Создание заказа без авторизации и без ингредиентов')
    def test_order_create_without_auth_and_without_ingredients(
            self, order_methods):
        body, status_code = order_methods.create_order([])
        assert (status_code == 400 and body.get("success") is False and body.get(
            "message") == ErrorMessages.INGREDIENT_IDS_REQUIRED)

    @allure.title('Создание заказа с неверным хешем ингредиентов')
    def test_order_create_with_invalid_ingredient_hash(
            self, order_methods, registered_user):
        token = registered_user["token"]
        invalid_ingredients = [
            '123123213123131231232132',
            '123123213123131231232132']
        body, status_code = order_methods.create_order(
            invalid_ingredients, token=token)
        assert status_code == 400
