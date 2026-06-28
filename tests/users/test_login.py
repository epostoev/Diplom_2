import pytest
import allure


@allure.suite('Логин пользвателя')
class TestLoginUsers:
    @allure.title('Успешный логин под существующим пользователем')
    def test_login_user_success(self, users_methods, registered_user):
        body, status_code = users_methods.login(
            registered_user["email"],
            registered_user["password"],
        )
        assert ("accessToken" in body and status_code ==
                200 and body["success"])

    @allure.title('Логин с неверным логином и паролем')
    @pytest.mark.parametrize("get_email, get_password", [
        (False, False),   # неверные и логин и пароль
        (False, True),    # неверный логин, верный пароль
        (True, False),    # верный логин, неверный пароль
    ])
    def test_login_wrong(
            self,
            users_methods,
            registered_user,
            get_email,
            get_password):
        email = registered_user["email"] if get_email else "wrongemail"
        password = registered_user["password"] if get_password else "wrongpassword"
        # print(f"\n{email} and {password}")
        body, status_code = users_methods.login(email, password)
        assert (
            status_code == 401 and body["message"] == "email or password are incorrect")
