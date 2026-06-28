import pytest
import json
import allure
from helpers import generate_user_data


@allure.suite('Создание Уникальног пользвателя')
class TestCtreateUsers:
    @allure.title('Успешное создание пользователя')
    def test_create_user_success(self, users_methods, new_user):
        body, status_code = users_methods.create_user(
            new_user["name"],
            new_user["password"],
            new_user["email"],
        )
        assert (status_code == 200 and body["success"])

    @allure.title('Создание уже существующего пользователя')
    def test_create_user_already_exists(self, users_methods, registered_user):
        body, status_code = users_methods.create_user(
            registered_user["name"],
            registered_user["password"],
            registered_user["email"],
        )
        print("\n")
        print(json.dumps(body))
        assert (
            status_code == 403 and body["message"] == "User already exists")

    @allure.title('Создание пользователя без обязательного поля')
    @pytest.mark.parametrize("missing_field", ["name", "password", "email"])
    def test_create_user_missing_field(self, users_methods, missing_field):
        user_data = generate_user_data()
        with allure.step(f"Удаляем поле {missing_field}"):
            user_data.pop(missing_field)
        with allure.step("Отправить POST-запрос на создание пользователя"):
            body, status_code = users_methods.create_user(
                user_data.get("name"),
                user_data.get("password"),
                user_data.get("email"),
            )
        assert (status_code == 403 and body["message"] ==
                "Email, password and name are required fields")
