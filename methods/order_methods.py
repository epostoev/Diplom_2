import allure
import requests
from data import URLS, OrderEndpoints


class OrderMethods:
    def __init__(self, url):
        self.url = url

    @allure.step("Получить список ингридиентов")
    def get_orders(self):
        with allure.step("Отравить GET-запрос на получение ингридиентов"):
            response = requests.get(
                f"{URLS.BASE_URL}{OrderEndpoints.INGREDIENTS}",
            )
        return response.json(), response.status_code

    @allure.step("Создать заказ")
    def create_order(self, ingredients, token=None):
        headers = {}
        if token:
            headers["Authorization"] = token

        with allure.step("Отправить POST-запрос на создание заказа"):
            response = requests.post(
                f"{URLS.BASE_URL}{OrderEndpoints.ORDERS}",
                json={"ingredients": ingredients},
                headers=headers,
            )
        return response.json(), response.status_code

    @allure.step("Отравить GET-запрос на получение списка заказов пользователя")
    def get_user_orders(self, token=None):
        headers = {}
        if token:
            headers["Authorization"] = token
        response = requests.get(
            f"{self.url}{OrderEndpoints.ORDERS}",
            headers=headers
        )
        return response.json(), response.status_code
