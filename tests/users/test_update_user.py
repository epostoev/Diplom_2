import allure
import pytest
from data import ErrorMessages


@pytest.mark.parametrize("field, value", [
    ("name", "new_name"),
    ("password", "new_password"),
    ("email", "new_email"),
])
@allure.suite('Изменение данных пользвателя')
class TestUpdateUsers:
    @allure.title('Изменение данных пользователя с авторизацией')
    def test_update_user_with_auth(
            self,
            users_methods,
            registered_user,
            field,
            value):
        token = registered_user["token"]
        date_user = {field: value}
        body, status_code = users_methods.update_user(token, date_user)
        with allure.step("Проверить, что статус-код 200 и в сообщении поле 'status' == True"):
            assert (status_code == 200 and body["success"])

    @allure.title('Изменение данных пользователя с без авторизации')
    def test_update_user_no_auth(self, users_methods, field, value):
        date_user = {field: value}
        body, status_code = users_methods.update_user_no_auth(date_user)
        with allure.step("Проверить, что статус-код 401 и в сообщении поле 'messange' == 'You should be authorised'"):
            assert (
                status_code == 401 and body["message"] == ErrorMessages.NOT_AUTHORISED)
