import allure
import requests
from data import URLS, UserEndpoints


class UserMethods:
    def __init__(self, url):
        self.url = URLS.BASE_URL

    @allure.step("Cоздать пользователя")
    def create_user(self, name, password, email):
        """Создаёт пользователя, возвращает данные + токен. После теста удаляет."""
        payload = {
            "name": name,
            "password": password,
            "email": email
        }
        with allure.step('Отправить POST-запрос на создание курьера'):
            response = requests.post(
                f"{self.url}{UserEndpoints.REGISTER}",
                json=payload
            )
        return response.json(), response.status_code

    @allure.step("Логин пользователя")
    def login(self, email, password):
        payload = {
            "email": email,
            "password": password
        }
        with allure.step('Отправить POST-запрос на логин'):
            response = requests.post(
                f"{self.url}{UserEndpoints.LOGIN}",
                json=payload
            )
        return response.json(), response.status_code

    @allure.step("Удаление пользователя")
    def delete_user(self, token):
        headers = {"Authorization": token}
        with allure.step("Отправить DELETE-запрос на удаление пользователя"):
            response = requests.delete(
                f"{self.url}{UserEndpoints.USER}",
                headers=headers
            )
        return response.json(), response.status_code

    @allure.step("Изменение данных пользователя")
    def update_user(self, token, user_data):
        header = {"Authorization": token}
        with allure.step("Отправить PATCH-запрос на изменение данных"):
            response = requests.patch(
                f"{self.url}{UserEndpoints.USER}",
                json=user_data,
                headers=header
            )
        return response.json(), response.status_code

    @allure.step("Изменение данных пользователя без авторизации")
    def update_user_no_auth(self, user_data):
        with allure.step("Отправить PATCH-запрос на изменение данных"):
            response = requests.patch(
                f"{self.url}{UserEndpoints.USER}",
                json=user_data
            )
        return response.json(), response.status_code
